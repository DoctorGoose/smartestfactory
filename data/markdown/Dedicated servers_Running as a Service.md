# Dedicated servers/Running as a Service

## Contents

  * 1 Running as a Service
    * 1.1 Linux
      * 1.1.1 Systemd
        * 1.1.1.1 NixOS (and other Atomic distros) Systemd Quirks
        * 1.1.1.2 Experimental Branch
        * 1.1.1.3 Planned graceful Restart
      * 1.1.2 OpenRC
    * 1.2 Windows
      * 1.2.1 NSSM
      * 1.2.2 NSSM to update your server
      * 1.2.3 Automating Server Updates With Task Scheduler
    * 1.3 Docker
  * 2 See also



This page describes how to set up the Satisfactory [dedicated server](/wiki/Dedicated_server "Dedicated server") as a service. 

## Running as a Service

Running the dedicated server as a service allows the game server to automatically restart in the event of a crash, as well as to automatically start after system boot. How this is handled depends on the operating system used. 

### Linux

#### Systemd

Systemd is the default service management system for many Linux distributions. 

The following is an **example** systemd unit file for the Satisfactory service. It uses SteamCMD to check for updates any time the server is started or restarted. It will also start the server after the host is booted. 

Edit the user and path to reflect the location and owner of the Satisfactory installation. The unit file should be placed at `/etc/systemd/system/satisfactory.service`
    
    
    [Unit]
    Description=Satisfactory dedicated server
    Wants=network-online.target
    After=syslog.target network.target nss-lookup.target network-online.target
    
    [Service]
    ExecStartPre=/usr/games/steamcmd +force_install_dir "/home/your_user/SatisfactoryDedicatedServer" +login anonymous +app_update 1690800 validate +quit
    ExecStart=/home/your_user/SatisfactoryDedicatedServer/FactoryServer.sh
    User=your_user
    Group=your_user
    Restart=on-failure
    RestartSec=60
    KillSignal=SIGINT
    WorkingDirectory=/home/your_user/SatisfactoryDedicatedServer
    
    [Install]
    WantedBy=multi-user.target
    

Besides logging to the journal (by default), the server also writes its logs to `<satisfactory_install_dir>/FactoryGame/Saved/Logs`. Log files are rotated automatically when the server process is restarted. See [Dedicated_servers#Logs_and_crash_dumps](/wiki/Dedicated_servers#Logs_and_crash_dumps "Dedicated servers") for more. 

Note that `KillSignal=SIGINT` should be set in the Service block of the service file, and `SIGTERM` is the default if not set.[1] Sending SIGTERM to the process kills the process immediately and does not process or log any exit behavior. The server process does not automatically save the game even on graceful shutdown, so when stopping the service, ensure that players are not connected, or if they are, manually run a save command before stopping. Enabling the "Auto-Save on Player Disconnect" server option is recommended. 

After creating the service, systemd will need to be reloaded to load the new service: 
    
    
    $ sudo systemctl daemon-reload
    

To enable and start the service, use the following two commands respectively:
    
    
    $ sudo systemctl enable satisfactory
    $ sudo systemctl start satisfactory
    

Service status can be checked with `sudo systemctl status satisfactory`. If configured correctly, the output should look like:
    
    
    * satisfactory.service - Satisfactory dedicated server
         Loaded: loaded (/etc/systemd/system/satisfactory.service; linked; preset: enabled)
         Active: active (running) since Wed 2024-09-11 23:01:03 UTC; 1s ago
       Main PID: 7813 (FactoryServer.s)
          Tasks: 21 (limit: 18998)
         Memory: 151.3M
            CPU: 1.632s
         CGroup: /system.slice/satisfactory.service
                 |-7813 /bin/sh /home/steam/Steam/SatisfactoryDedicatedServer/FactoryServer.sh
                 `-7820 /home/steam/Steam/SatisfactoryDedicatedServer/Engine/Binaries/Linux/FactoryServer-Linux-Shipping FactoryGame
    

If the service times out before it is loaded, it may restart in a loop. This may happpen if older hardware that doesn't meet the minimum requirements for the server hardware is being used. To prevent this, the following line can be added to the [Service] section:`TimeoutSec=XXX`. Replace the XXX with a numerical value in seconds. On most distros services timeout after 90 seconds by default. 

##### NixOS (and other Atomic distros) Systemd Quirks

If you are creating a Service using steam-run on NixOS with Systemd, ensure you are calling for the steam-run binary via the source binary, with `${pkgs.steam-run}/bin/steam-run`. Attempting to use the binary atomically linked inside `/run/current-system/sw/bin/steam-run` will make the service not start correctly. For an example of the design of the Service unit inside Nix, see this: [Satisfactory Service Nix](https://gitlab.kuca.cz/tom-kuca/nix-config/-/blob/a11e73470c4f9a151afe67c7fa3a960b838d0d98/modules/nixos/satisfactory.nix). See Systemd bug reported here for more information: [Systemd issue 31941](https://github.com/systemd/systemd/issues/31941) for further information and monitoring progress. 

##### Experimental Branch

To have `systemd` pre-fetch the Experimental branch of the Dedicated Server upon restart, adjust the `ExecStartPre` directive to tell SteamCMD to use the `experimental` branch, as follows (truncated for brevity):
    
    
    [Service]
    #...
    ExecStartPre=/usr/games/steamcmd +force_install_dir "/home/your_user/SatisfactoryDedicatedServer" +login anonymous +app_update 1690800 -beta experimental validate +quit
    #...
    

##### Planned graceful Restart

Together with the [HTTPS API](/wiki/Dedicated_servers/HTTPS_API "Dedicated servers/HTTPS API") the Service can be configured to save, update and restart automaticaly. Here is an example using a [cron job](https://www.adminschoice.com/crontab-quick-reference) and curl.
    
    
    ##Example cron tab config
    # m h  dom mon dow   command
    00 <RESTART_TIME>  * * * /usr/bin/curl -s --location 'https://<IP_ADDRESS>:7777/api/v1' --insecure --header 'Content-Type: application/json' --data '{"function" :"PasswordLogin","data": {"Password": "<PASSWORD>","MinimumPrivilegeLevel": "Administrator"}}' | /usr/bin/jq -r '.data.authenticationToken' | xargs -I{} /usr/bin/curl -s --location 'https://<IP_ADDRESS>:<PORT>/api/v1' --insecure --header 'Content-Type: application/json' --header "Authorization: Bearer {}" --data '{"function" :"SaveGame","data": {"SaveName": "main"}}' && sleep 15 && /usr/sbin/service satisfactory restart
    
    ##Restart Command Step-by-Step (without absolut paths)
    #Get authenticationToken
    token=$(curl -s --location 'https://<IP_ADDRESS>:7777/api/v1' --insecure --header 'Content-Type: application/json' --data
    '{
    "function" :"PasswordLogin"
    "data": {"Password": "<PASSWORD>","MinimumPrivilegeLevel": "Administrator"}
    }'
    | jq -r '.data.authenticationToken')
    #Save Game 
    &&
    curl -s --location 'https://<IP_ADDRESS>:7777/api/v1' --insecure --header 'Content-Type: application/json' --header "Authorization: Bearer ${token}" --data
    '{
    "function" :"SaveGame",
    "data": {"SaveName": "<SAVE_GAME_NAME>"}
    }'
    #Wait 15 seconds (unknow if SaveGame function is synchronous)
    &&
    sleep 15
    #Restart Service (also updates the server)
    &&
    service satisfactory restart
    

#### OpenRC

OpenRC is a service management system for [Gentoo Linux](https://gentoo.org). 

Install SteamCMD using Portage, and accept its license. Its installation directory by default is `/opt/steamcmd`. 

The recommended way to get it set up is to link to the already existing SteamCMD init file with `ln -s /etc/init.d/steamcmd /etc/init.d/steamcmd.satisfactory` and then copying the default config from `/etc/conf.d/steamcmd` to `/etc/conf.d/steamcmd.satisfactory`. 

The completed `/etc/conf.d/steamcmd.satisfactory` would look something like this:
    
    
    # Copyright 1999-2020 Gentoo Authors 
    # Distributed under the terms of the GNU General Public License v2 
    
    # Dtach options, which will used, when the `attach` extra command is called. 
    # By default, CTRL+D is used, and no signal is send, 
    # when you want to detach from the attached console. 
    DTACH_OPTS="-e '^D' -r none" 
    # Specifies, which server binary is used. 
    # This could be 'hlds_run' or 'srcds_run', depending on your game. 
    STEAMCMD_BINARY="FactoryServer.sh" 
    # Path to the files of your started server. 
    STEAMCMD_PATH="/opt/steamcmd/sf" 
    # Options for your server binary. 
    STEAMCMD_OPTS=""
    

### Windows

#### NSSM

You can use [Non-Sucking Service Manager](https://nssm.cc/) to easily set up auto-restart for the dedicated server. 

Once you've downloaded and installed NSSM, navigate to the directory containing nssm.exe and run the below command:
    
    
    nssm.exe install SatisfactoryServerService
    

This will pull up a GUI for configuration. Set the "**Path** " to the location of FactoryServer.exe, Set the "**Arguments** " to "-unattended". You can modify other settings if you want, but that's the only required step. Click "install", then run this command.
    
    
    nssm.exe start SatisfactoryServerService
    

Other useful `nssm` commands:
    
    
    nssm.exe status SatisfactoryServerService # Checks the status of the Service
    nssm.exe stop SatisfactoryServerService # Stops the service, and prevents it from auto-restarting
    

#### NSSM to update your server

First create a batch file with the following text and save it as Update.bat in the same directory as Factory.exe. Remember to put the directory on your server for where the Steamcmd.exe and Factory.exe files are. For this example they reside in the C:\Gameservers directory.
    
    
    "C:\GameServers\SteamCMD\steamcmd.exe" +force_install_dir "C:\GameServers\SatisfactoryServer" +login anonymous +app_update 1690800 -beta public validate +quit
    "C:\GameServers\nssm.exe" start SatisfactoryServerService
    "C:\GameServers\nssm.exe" stop SatisfactoryServerUpdate
    

Next open up your command prompt and change directories to where nssm.exe and run the command below:
    
    
    nssm.exe install SatisfactoryServerUpdate
    

Set the "Path" to the location of Update.bat. Set the startup type to Automatic. Under the Exit Actions tab and restart area select: Stop service (oneshot mode). Click "install" Run the command below:
    
    
    nssm.exe edit SatisfactoryServerService
    

Under the Details tab change the Startup type to "Manual" then Click "Edit service." Now run the following command:
    
    
    nssm.exe start SatisfactoryServerUpdate
    

This will have steamcmd look for any update, download, install, and verify it. Then it will quit and start your Satisfactory server. This will also stop the update service. 

#### Automating Server Updates With Task Scheduler

You can further automate this function by using the Windows Task Scheduler. 

Run the task scheduler and open up the library. Right click in the big window and click "Create New Task..." In the General tab under account ensure you put an administrative service account to run the task. On the triggers tab you can set an option to have it run. If you would like to have the server check every day 2am you can set a new trigger. Have the task begin on a schedule. Run it daily at 2:00am. Set the task to enabled and click "Ok." Go to the Actions tab. You're going to want to start the next two programs:
    
    
    NET STOP "SatisfactoryServerService"
    NET START "SatisfactoryServerUpdate"
    

Click "OK" to save. Now your server will automatically shutdown at 2am, search for an update, install it if found, and restart without any human interaction. You can check to see if this is running in the task scheduler window or within the event viewer under the application tab. 

### Docker

_See:_[Dedicated_servers#Docker](/wiki/Dedicated_servers#Docker "Dedicated servers"), [Dedicated_servers#Docker_Images](/wiki/Dedicated_servers#Docker_Images "Dedicated servers")

  


## See also

  * [Dedicated Servers - Main Page](/wiki/Dedicated_servers "Dedicated servers")
  * [Dedicated Servers - Configuration Files](/wiki/Dedicated_servers/Configuration_files "Dedicated servers/Configuration files")
  * [Dedicated Servers - Automatic Updates](/wiki/Dedicated_servers/Automatic_updates "Dedicated servers/Automatic updates")
  * [Dedicated Servers - HTTPS API](/wiki/Dedicated_servers/HTTPS_API "Dedicated servers/HTTPS API")



  * [v](/wiki/Template:PioneerNav "Template:PioneerNav")
  * [e](https://satisfactory.wiki.gg/wiki/Template:PioneerNav?action=edit)
  * [h](https://satisfactory.wiki.gg/wiki/Template:PioneerNav?action=history)

[Satisfactory](/wiki/Satisfactory "Satisfactory") game mechanics  
---  
Player abilities| [Codex](/wiki/Codex "Codex") • [Resource Scanner](/wiki/Resource_Scanner "Resource Scanner") • [Build Gun](/wiki/Build_Gun "Build Gun") • [Inventory](/wiki/Inventory "Inventory") • [Health](/wiki/Health "Health") • [Combat](/wiki/Combat "Combat") • [Movement](/wiki/Movement "Movement") • [Flashlight](/wiki/Flashlight "Flashlight") • [HUD](/wiki/HUD "HUD") • [Crate](/wiki/Crate "Crate") • [To-Do List](/wiki/To-Do_List "To-Do List")  
Unlockable abilities| [Recipes](/wiki/Recipes "Recipes") • [Power](/wiki/Power "Power") • [Overclocking/Underclocking](/wiki/Clock_speed "Clock speed") • [Production amplifier](/wiki/Production_amplifier "Production amplifier") • [Customizer](/wiki/Customizer "Customizer") • [Map](/wiki/Map "Map") • [Productivity Display](/wiki/Productivity_Display "Productivity Display") • [Head lift](/wiki/Head_lift "Head lift") • [Blueprints](/wiki/Blueprints "Blueprints") • [Fuels](/wiki/Category:Fuels "Category:Fuels") • [FICSIT Productive Packer Deluxe](/wiki/FICSIT_Productive_Packer_Deluxe "FICSIT Productive Packer Deluxe")  
Progression| [Story](/wiki/Story "Story") • [Drop-pod](/wiki/Drop-pod "Drop-pod") • [Onboarding (In-game tutorial)](/wiki/Onboarding "Onboarding") • [Milestones](/wiki/Milestones "Milestones") • [MAM](/wiki/MAM "MAM") • [Alternate recipes](/wiki/Hard_Drive#Alternate_recipes "Hard Drive") • [Space Elevator](/wiki/Space_Elevator "Space Elevator") • [AWESOME Sink](/wiki/AWESOME_Sink "AWESOME Sink") • [AWESOME Shop](/wiki/AWESOME_Shop "AWESOME Shop")  
Seasonal events| [April Fools' Day](/wiki/April_Fools%27_Day "April Fools' Day") • [Anniversary](/wiki/Anniversary "Anniversary") • [FICSMAS](/wiki/FICSMAS "FICSMAS")  
Environment| [World](/wiki/World "World") • [Resource Node](/wiki/Resource_Node "Resource Node") • [Resource Well](/wiki/Resource_Well "Resource Well") • [Resource renewability](/wiki/Resource_renewability "Resource renewability") • [Crash Site](/wiki/Crash_Site "Crash Site") • [Radiation](/wiki/Radiation "Radiation") • [Poison Gas](/wiki/Poison_Gas "Poison Gas") • [Cracked boulder](/wiki/Cracked_boulder "Cracked boulder") • [Cave](/wiki/Cave "Cave")  
Gameplay| [Controls](/wiki/Controls "Controls") • [Settings](/wiki/Settings "Settings") • [Future content](/wiki/Future_content "Future content") • [Old unreleased content](/wiki/Old_unreleased_content "Old unreleased content") • [Online tools](/wiki/Online_tools "Online tools") • [Community resources](/wiki/Community_resources "Community resources") • [Advanced Game Settings](/wiki/Advanced_Game_Settings "Advanced Game Settings") • [Acronyms](/wiki/Acronyms "Acronyms") • [Achievements](/wiki/Achievements "Achievements") • [Easter eggs](/wiki/Easter_eggs "Easter eggs") • [Game menus](/wiki/Game_menus "Game menus") • [Indicator Light](/wiki/Indicator_Light "Indicator Light") • [Multiplayer](/wiki/Multiplayer "Multiplayer") • [Music](/wiki/Music "Music")  
Technical| [Console release](/wiki/Console_release "Console release") • [Debug console](/wiki/Debug_console "Debug console") • [Launch arguments](/wiki/Launch_arguments "Launch arguments") • [Save files](/wiki/Save_files "Save files") • [System requirements](/wiki/System_requirements "System requirements") • [Units](/wiki/Units "Units") • [Unreal Engine](/wiki/Unreal_Engine "Unreal Engine")  
Guides and tutorials| | Basics| [Walkthrough/How to play](/wiki/Tutorial:How_to_play "Tutorial:How to play") • [New Pioneer Guide](/wiki/Tutorial:New_Pioneer_Guide "Tutorial:New Pioneer Guide") • [Production line basics](/wiki/Tutorial:Production_line "Tutorial:Production line") • [Advanced production line tips](/wiki/Tutorial:Production_line_design_tips "Tutorial:Production line design tips") • [Picking an alternate recipe](/wiki/Tutorial:Picking_an_alternate_recipe "Tutorial:Picking an alternate recipe") • [Independency](/wiki/Tutorial:Independency "Tutorial:Independency") • [Aluminum Ingot production](/wiki/Tutorial:Setting_up_Aluminum_Ingot_production "Tutorial:Setting up Aluminum Ingot production")  
---|---  
Logistics| [Manifold](/wiki/Manifold "Manifold") • [Balancer](/wiki/Balancer "Balancer") • [Pipeline manifold](/wiki/Pipeline_manifold "Pipeline manifold") • [Prime Splitter Arrays](/wiki/Tutorial:Prime_splitter_arrays "Tutorial:Prime splitter arrays") • [Trains](/wiki/Tutorial:Trains "Tutorial:Trains") • [Train throughput](/wiki/Tutorial:Train_throughput "Tutorial:Train throughput")  
Dedicated servers| [Dedicated servers](/wiki/Dedicated_servers "Dedicated servers") • Running as a Service • [Configuration files](/wiki/Dedicated_servers/Configuration_files "Dedicated servers/Configuration files") • [Automatic updates](/wiki/Dedicated_servers/Automatic_updates "Dedicated servers/Automatic updates") • [HTTPS API](/wiki/Dedicated_servers/HTTPS_API "Dedicated servers/HTTPS API") • [Lightweight Query API](/wiki/Dedicated_servers/Lightweight_Query_API "Dedicated servers/Lightweight Query API")  
Other| [Hypertube cannon](/wiki/Tutorial:Hypertube_cannon "Tutorial:Hypertube cannon") • [Hypertube brake](/wiki/Tutorial:Hypertube_brake "Tutorial:Hypertube brake") • [Steam Deck & Controller setup](/wiki/Tutorial:Controller_setup "Tutorial:Controller setup") • [Extracting UI icons](/wiki/Tutorial:Extracting_UI_icons "Tutorial:Extracting UI icons")  
  
  1. ↑ <https://www.freedesktop.org/software/systemd/man/latest/systemd.kill.html> systemd.kill


  *[v]: View this template
  *[e]: Edit this template
  *[h]: History of this template
  *[his]: his trivia section
