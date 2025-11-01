# Dedicated servers

## Contents

  * 1 Summary
    * 1.1 Who this page is for
  * 2 Requirements
  * 3 Installation
    * 3.1 Distribution
    * 3.2 SteamCMD
      * 3.2.1 Linux
      * 3.2.2 Windows
      * 3.2.3 Experimental branch selection
        * 3.2.3.1 Linux
        * 3.2.3.2 Windows
    * 3.3 Steam GUI
    * 3.4 Epic Games
    * 3.5 Docker
    * 3.6 Other
    * 3.7 Third-party cloud hosting solutions
  * 4 Port forwarding and firewall settings
    * 4.1 Setting a static IP on the server
    * 4.2 Server setup
      * 4.2.1 Linux
      * 4.2.2 Windows
    * 4.3 Router setup
      * 4.3.1 OpenWRT
      * 4.3.2 Other
    * 4.4 Verifying that the ports are open to the public
      * 4.4.1 nmap
      * 4.4.2 Port check websites
  * 5 Starting the server
    * 5.1 Manual - Steam GUI
    * 5.2 Manual - Command line
      * 5.2.1 Windows
      * 5.2.2 Linux
    * 5.3 Command line options
    * 5.4 Verifying that the server is running
      * 5.4.1 Browser
      * 5.4.2 Linux/Windows
    * 5.5 Automatic - Running as a Service
  * 6 Configuration
    * 6.1 Claiming the server and starting a game
    * 6.2 Server settings
    * 6.3 Loading a save file
  * 7 Console commands
  * 8 Server file Locations
    * 8.1 Server settings file
    * 8.2 Save files
    * 8.3 Blueprint files
    * 8.4 Configuration files
  * 9 Logs and crash dumps
  * 10 Common errors or problems
    * 10.1 Is the server actually running?
      * 10.1.1 Linux
      * 10.1.2 Windows
    * 10.2 Is the server listening on the correct ports?
      * 10.2.1 Checking listening ports on Windows
      * 10.2.2 Checking listening ports on Linux
    * 10.3 Is the server bound to the correct interface?
    * 10.4 Is the server firewall allowing ingress on the correct ports?
    * 10.5 Are the port forwarding settings at the NAT pointing to the correct address and all three correct ports?
    * 10.6 Is the server accessible on the LAN?
    * 10.7 Are you or anyone else able to connect to the server via the internet?
    * 10.8 SDL Priority Manager
    * 10.9 SteamAPI_Init(): Sys_LoadModule failed to load: /path/to/.steam/sdk64/steamclient.so
    * 10.10 SteamCMD errors
      * 10.10.1 state is 0x606 after update job
    * 10.11 Trains not loading or unloading
    * 10.12 Running on ARM
    * 10.13 Running in a VM in Proxmox VE
    * 10.14 The server becomes unreachable after disconnecting from the game
  * 11 FAQ
    * 11.1 How do I set a join password?
    * 11.2 My players can't join my server !!!
    * 11.3 My players are timing out !!!
    * 11.4 How do I gracefully shut down the Dedicated Server?
      * 11.4.1 Linux
      * 11.4.2 Windows
    * 11.5 How do I update the dedicated server?
      * 11.5.1 Manually updating
        * 11.5.1.1 Steam client
        * 11.5.1.2 SteamCMD
      * 11.5.2 Automatically
    * 11.6 How do I reset the Administrator password?
    * 11.7 What to do when client gets error "Certificate Verify Result: certificate is not yet valid"
    * 11.8 How can I have more than four players in my server?
    * 11.9 I thought the Dedicated Server was multi-threaded- why am I only seeing one core being used?
    * 11.10 I was running an Experimental server, but I want to move it to Stable, and it's not converting. What do I do?
    * 11.11 How can I get my friends to join my server?
    * 11.12 How can I have the server restart at a certain time?
    * 11.13 The Dedicated Server stops after throwing two warnings; what do I do?
    * 11.14 I added the server to the Server Browser via IPv6 and get a ping, but it says "Failed to Connect to the Server API", what do I do?
  * 12 Community tools
    * 12.1 Connection testers
    * 12.2 CLI tools
    * 12.3 Discord bots
    * 12.4 GUI tools
    * 12.5 SDKs
    * 12.6 API documentation
    * 12.7 Docker images
  * 13 API
  * 14 Trivia
  * 15 See also
  * 16 History
  * 17 References



This page provides basic instructions on setting up and operating a **_Satisfactory_ dedicated server**. 

## Summary

Dedicated server binaries are available for 64bit [Windows](https://en.wikipedia.org/wiki/Microsoft_Windows "wikipedia:Microsoft Windows") and [Linux](https://en.wikipedia.org/wiki/Linux "wikipedia:Linux") systems. It can be installed using the [Steam](https://en.wikipedia.org/wiki/Steam_\(service\) "wikipedia:Steam \(service\)") client (where it is listed in the user's library as a "tool"), its command line sibling [SteamCMD](https://developer.valvesoftware.com/wiki/SteamCMD), or [Epic Games](https://www.epicgames.com/store/en-US/p/satisfactory--dedicated-server). Game clients from both the Epic and Steam game stores can connect and play on dedicated servers regardless of where the server binaries were downloaded. 

### Who this page is for

If you intend to host the game by running a dedicated server instance, this page is for you. 

If you are simply a player on someone else's server, you do **NOT** need to do anything shown on this page, _they_ do.[1]

## Requirements

These are community recommendations for minimum requirements. The server may or may not run with less powerful hardware, depending on player count and save file size.  
It is highly recommended that servers exceed the minimum requirements, especially for CPU. 

System requirements  **Processor** |  A vaguely recent x86-64 compatible Intel (i5-3570 or better) or AMD (Ryzen 5 3600 or better) processor.  
The server uses multiple cores, but _**heavily favors**_ high single-core performance. Anything with a [single-thread rating](https://www.cpubenchmark.net/singleThread.html) of 2000 or higher should work.  
There is no 32-bit (x86) or ARM support.  
If this is a VM (a VPS most definitely is), a `kvm64` CPU **won't** work!   
---|---  
**Memory** | 8GB. 16GB RAM may be recommended for larger saves or to host more than 4 players.   
**Storage (Windows)** | Server files of 12.4GB. The full game install is not required.   
**Storage (Linux)** | 8GB. Base install of typical server distros is up to 2GB in size, plus game server files of 2GB   
**Operating System** | Windows 10,11, Server 2016, Server 2019 or Server 2022, or a Linux distro like Debian or Ubuntu   
**Internet Connection** | Broadband internet connection. Hosting from home will require the ability to configure port forwarding or a VPN   
  
## Installation

### Distribution

The dedicated server software is currently available via the SteamCMD command-line client, through the graphical Steam client as a tool, or as a [free add-on](https://store.epicgames.com/en-US/p/satisfactory--dedicated-server) in the Epic Games Store (available to all accounts). 

### SteamCMD

Usage of SteamCMD is preferred. The installation of SteamCMD is thoroughly documented for both Windows and Linux on [the official SteamCMD wiki page](https://developer.valvesoftware.com/wiki/SteamCMD#Downloading_SteamCMD). 

If a GUI is desired, use the Steam client instead to download, install, and update the dedicated server. 

Once SteamCMD has been downloaded/installed, see the following **example** commands on downloading or updating the server files: 

**Notes** : 

  * `force_install_dir` should preferably be an absolute path. On Linux, a tilde-prefixed directory is also acceptable. If `force_install_dir` is not specified, steamcmd may install it to `~/Steam/steamapps/common/SatisfactoryDedicatedServer`, `$HOME/.steam/debian-installation/steamapps/common/SatisfactoryDedicatedServer`, or `$HOME/.local/share/Steam/steamapps/common/SatisfactoryDedicatedServer`.
  * If the installation directory contains spaces, remember to wrap it in quotation marks first.
  * The installation directory can be anywhere, but for convenience, probably close to either the root folder (C:\ on Windows, / on Linux) or a user's home folder.



#### Linux

A user without root privileges is recommended. If the SteamCMD wiki instructions were followed, the `steam` user may be used. 
    
    
    steamcmd +force_install_dir ~/SatisfactoryDedicatedServer +login anonymous +app_update 1690800 validate +quit
    

#### Windows

Open a Windows Command Prompt or PowerShell session. 
    
    
    .\steamcmd.exe +force_install_dir "C:\Game Servers\Satisfactory Server\Dont Blindly Copypaste This Line" +login anonymous +app_update 1690800 validate +quit
    

On Windows, SteamCMD uses Steam client files, so a faster initial download of SteamCMD may be done by copying `steamcmd.exe` into the Steam directory (typically `C:\Program Files (x86)\Steam`) and then using a command such as this one instead: 
    
    
    "C:\Program Files (x86)\Steam\steamcmd.exe" +force_install_dir "C:\Game Servers\Satisfactory Server\Dont Blindly Copypaste This Line" +login anonymous +app_update 1690800 validate +quit
    

Where the first path is the Steam directory, and the second is the desired dedicated server installation directory. Note: this is not a requirement. If SteamCMD is run with the command stated above (assuming the file path is where the executable is) and Steam is not installed, SteamCMD will update itself first and download the files that it requires. This is useful to not have to install a full Steam client on the server. 

#### Experimental branch selection

To download the Experimental branch of the Dedicated Server, add `-beta experimental` to the end of the SteamCMD invocation. See the following example commands for Linux and Windows respectively: 

##### Linux
    
    
    steamcmd +force_install_dir ~/SatisfactoryDedicatedServer +login anonymous +app_update 1690800 -beta experimental validate +quit
    

##### Windows
    
    
    steamcmd.exe +force_install_dir C:\GameServers\SatisfactoryServer +login anonymous +app_update 1690800 -beta experimental validate +quit
    

### Steam GUI

You can install the server from your Steam library if the active Steam account owns the game. You will have to change your steam library filters to show tools. 

Coffee Stain is currently working with Valve to make the Dedicated Server visible in the normal Steam client to accounts which do not currently have access to the Satisfactory game client. However, you can still use SteamCMD to download and install the files without needing a Steam account. 

If you want to use the Experimental branch of the Dedicated Server rather than the mainline release, go to the Properties of the entry in your Library, go to the Betas tab, and ensure that the Experimental beta branch is selected. To revert to the mainline release, reverse this process. 

### Epic Games

You can install Dedicated Server Tool add-on by visiting the [Satisfactory Store Page](https://www.epicgames.com/store/en-US/p/satisfactory) and adding [Dedicated Server Tool](https://www.epicgames.com/store/en-US/p/satisfactory--dedicated-server) to your library. Search your library for "Satisfactory Dedicated Server" and select install. 

### Docker

The server can be run in a Docker container.  
A popular up-to-date one is [Wolveix's](https://github.com/wolveix/satisfactory-server).  
There are many more such images available on [GitHub](https://github.com/search?q=satisfactory+docker&type=repositories) and [Docker Hub](https://hub.docker.com/search?q=satisfactory&type=image).  
Please direct any questions about using or troubleshooting containers using these images to their respective maintainers. 

### Other

Common free ones include: 

  * [Pterodactyl](https://pterodactyl.io/)
  * [LinuxGSM](https://linuxgsm.com/)
  * [PowerShellGSM](https://github.com/patrix87/PowerShellGSM)



### Third-party cloud hosting solutions

There are many game server hosting providers available for easy deployment of the game server. 

Using a third-party service may make server management more complex, such as limiting server options or adding hidden options that can break the server or cause unexpected complications.  
Community members may decline to help troubleshoot servers hosted by hosting providers, as they will not likely know specifics about how the server is run. Questions should be directed to the hosting provider instead. 

## Port forwarding and firewall settings

For the server to be reachable from the internet, ensure that the router has the ports forwarded, and that the server running the game server process has its firewall rules set to allow listening on the ports. 

As of [Patch 1.1.0.0](/wiki/Patch_1.1.0.0 "Patch 1.1.0.0"), a Satisfactory server requires two ports to be forwarded to function properly - a standard Port (default 7777) and a Reliable Messaging Port (default 8888). 

Port Number | Protocol | Relevant Command-line Parameters | Usage   
---|---|---|---  
7777 | TCP | `-Port=` | Server traffic, HTTPS API   
7777 | UDP | `-Port=` | Game traffic, Lightweight Query API   
8888 | TCP | `-ReliablePort=`, `-ExternalReliablePort=` | Game traffic, Reliable messaging   
  
(As of [Patch 1.0](/wiki/Patch_1.0 "Patch 1.0"), port numbers 15000 and 15777 are no longer used.) 

The standard port can be set using the `-Port` parameter upon server startup, e.g. `-Port=10000` to run the game server on port number `10000`. The value must be an integer between 0 and 65535. If the default port number is in use, the next higher one will be checked until an available port number is found, which will then be used. The reliable port can be set using the `-ReliablePort=` parameter. If specified, the server will attempt to bind to this port and fail to initialize if the port is unavailable. 

Port redirection is not supported at the moment for the standard port, so the external/internal port numbers must match on the port forward rule(s) (eg: do not forward internal port number 7777 as external port number 7778 on the router). The reliable port can be remapped via the `-ExternalReliablePort=` command-line parameter. If multiple instances of the server are to be available on one public IP, override and set a unique port number per instance, or use the [automatic port allocation configuration](/wiki/Patch_1.1.0.0#Dedicated_Server_-_Port_Forwarding_Updates "Patch 1.1.0.0"). 

To set the primary port 7777 and secondary port 8888 docker-container internal, look for the corresponding environment variables from the container maintainer. 

### Setting a static IP on the server

Remember to set a static LAN IP on the server, otherwise the DHCP server may eventually assign the server a different LAN IP, and the port forwarding will break. 

### Server setup

#### Linux

Whether or not the server needs its firewall configured depends on the Linux distribution used, and any custom configuration applied to it.  


Debian's firewall accepts all traffic by default.[2]  
Ubuntu uses UFW, but UFW is disabled by default.[3]  


For a server with UFW enabled, the following is an example configuration file to put into `applications.d`: 
    
    
    [Satisfactory]
    title=Satisfactory
    description=An extremely satisfying experience
    ports=7777/udp|7777/tcp|8888/tcp
    

#### Windows

The following PowerShell command can be used on a Windows host to open the default ports used by the server: 
    
    
    New-NetFirewallRule -DisplayName "Allow Satisfactory default inbound port udp" -Direction Inbound -Action Allow -EdgeTraversalPolicy Allow -Protocol UDP -LocalPort 7777
    New-NetFirewallRule -DisplayName "Allow Satisfactory default inbound port tcp" -Direction Inbound -Action Allow -EdgeTraversalPolicy Allow -Protocol TCP -LocalPort 7777
    New-NetFirewallRule -DisplayName "Allow Satisfactory default inbound reliable port tcp" -Direction Inbound -Action Allow -EdgeTraversalPolicy Allow -Protocol TCP -LocalPort 8888
    

One can also specifically allow the `FactoryServer-Win64-Shipping-Cmd.exe` executable: 
    
    
    New-NetFirewallRule -DisplayName "Allow Satisfactory Process Inbound" -Direction Inbound -Action Allow -EdgeTraversalPolicy Allow -Program "C:\Game Servers\Satisfactory Server\Dont Blindly Copypaste This Line\Engine\Binaries\Win64\FactoryServer-Win64-Shipping-Cmd.exe"
    

Replace `C:\Game Servers\Satisfactory Server\Dont Blindly Copypaste This Line\` with the base directory of the install location. The final path passed to `-Program` should be of the server executable. 

### Router setup

Assuming the server's internet connection is not behind CGNAT[4], forward the game server's ports on the router.   
See [this TechSpot article](https://www.techspot.com/guides/287-default-router-ip-addresses/) for a list of common home router addresses. 

#### OpenWRT

  1. Go to `http://<router_ip>/cgi-bin/luci/admin/network/firewall/forwards` and add a port forward rule.
  2. Name the port forward rule
  3. Set protocol to both TCP and UDP
  4. Set both external and internal port to the port number.
  5. Set internal IP address to the server's LAN IP
  6. Optionally enable NAT loopback in advanced settings if desired. This will allow accessing the game server from the LAN using the external IP address.
  7. Save and Apply


  * [](/wiki/File:Openwrt_port_forward.png)




#### Other

Check the service provider or router manufacturer's documentation on port forwarding. 

### Verifying that the ports are open to the public

Only try this when the game server process **is running**. If the game server process is not running, these tools may show the port(s) as closed. See Starting the server. 

#### nmap

If NAT loopback is enabled, one can run `nmap` from a device on the LAN: `nmap -sT -sU <external_ip> -p 7777`  
It should show both ports open: 
    
    
    Starting Nmap 7.93 ( https://nmap.org ) at TIME
    Nmap scan report for ADDRESS
    Host is up (0.00069s latency).
    
    PORT     STATE         SERVICE
    7777/tcp open          cbt
    7777/udp open|filtered cbt
    
    Nmap done: 1 IP address (1 host up) scanned in 0.69 seconds

Be sure to check the reliable messaging port (default 8888) as well. 

#### Port check websites

One can also use a port checker site like <https://port.tools/nmap-online-port-scan/> or <https://www.canyouseeme.org/> to check that the TCP port has been forwarded correctly, and that the game server process is listening on it.  
Remember to type in the correct port number before clicking the "Check Port" button.  
Note that this site only checks the TCP port, but as long as it shows the port as open, it _should_ be fine. 

## Starting the server

**NOTE!** Starting the server manually will _not_ automatically restart the server if it crashes or is terminated for other reasons. The server will stop running when the terminal is closed. To avoid these issues, it is **strongly recommend** to configure the server to run as a service. For more information, see: [Running as a Service](/wiki/Dedicated_servers/Running_as_a_Service "Dedicated servers/Running as a Service"). 

### Manual - Steam GUI

Launch the Satisfactory Dedicated Server from Steam just like any other game. It will be found under the Tools category instead of Games. Running the server like this will open a terminal window in which the logs can be viewed in real time. Do not be alarmed if the window stops logging new information after a few moments. This usually means the server is up and simply idling, waiting for connections. 

### Manual - Command line

#### Windows

In either the Command Prompt or PowerShell, navigate to the directory where the dedicated server was installed, and use the following command, with any other options from the below table that are needed:
    
    
    .\FactoryServer.exe -log -unattended
    

#### Linux

Navigate to the directory where the Satisfactory dedicated server is installed, and use the following command, with any other options from the below table that are needed:
    
    
    ./FactoryServer.sh

### Command line options

The below table outlines the available options for use when starting the server, either from the command-line or through Steam (via editing the Properties of the Dedicated Server's entry in Tools): 

Option | Description   
---|---  
`-Port=<portnum>` | Override the port the server uses. The default port is 7777 (UDP and TCP). If the specified port is in use, the server will increment the port number and continue trying port numbers until an available one is found.   
`-ReliablePort=<portnum>` | Override the reliable messaging port the server uses. The default port is 8888 (TCP). If the specified port is in use, the server will fail to initialize.   
`-ExternalReliablePort=<portnum>` | Use with the `-ReliablePort` option if external port remapping is used.   
`-DisablePacketRouting` | Startup argument for disabling the packet router (Automatically disabled with multihome).   
`-DisableSeasonalEvents` | Disables all seasonal events, such as [FICSMAS](/wiki/FICSMAS "FICSMAS").   
`-ini:<INIFILE>:[<SECTION>]:<KEY>=<VALUE>` | Run with an ini configuration value, e.g, `-ini:Game:[/Script/Engine.GameSession]:MaxPlayers=8`  
Windows-only   
`-Log` | Forces the server to display logs in a window on Windows, or in the active terminal on Linux. This option is enabled by default when launching on Linux.   
`-NewConsole` | Run using the Satisfactory 1.0 Unreal console.[5]  
`-Unattended` | Makes it such that the Dedicated Server will not present any dialogs which might otherwise interrupt the server from running if not attended to. This option is enabled by default when launching on Linux.   
  
NOTE: Options may also be set via INI files, for example: 

CLI parameter | INI file   
---|---  
`-Port=<portnum>` | `Engine.ini`
    
    
    [URL]
    Port=<portnum>
      
  
### Verifying that the server is running

Besides checking that the process is running, it is recommended to check that the server is actually listening on the expected port. 

#### Browser

A quick check can be done by opening a browser tab to the server (eg, <https://ip:port/>) to check if the server is up and listening.  
Replace `ip` with the server's LAN IP, and `port` with the port.  
The `https://` part of the url is **required**. Without it, Chrome will show "This page isn't working," and Firefox will show "The connection was reset."  
**Expect to see a certificate warning due to the self-signed certificate generated by the server, and after accepting the certificate, a`errors.com.epicgames.httpserver.route_handler_not_found` error.**

#### Linux/Windows

On Windows, use Command Prompt instead of PowerShell. 

`curl -k <https://ip:port>`  
Running that should return 
    
    
    {"errorCode": "errors.com.epicgames.httpserver.route_handler_not_found", "errorMessage": ""}

### Automatic - Running as a Service

Instead of running the server manually, the server can be configured to run as a background service. This way, the server will: 

  * Automatically restart if it crashes or stops unexpectedly
  * Run in the background
  * Automatically update when the service restarts



For step-by-step instructions, see: [Running as a Service](/wiki/Dedicated_servers/Running_as_a_Service "Dedicated servers/Running as a Service"). 

## Configuration

### Claiming the server and starting a game

Before the server can start a game, it must first be claimed: 

  1. Start the game
  2. From the Server Manager in the main menu, add the server.
  3. Set a name for the server, then set the administrator password.



A new game can now be created. An existing game can also be imported to the server from the ingame server manager. 

Player password protection is not enabled by default, but a player password can be set through the same UI. 

### Server settings

When logged in as Admin via the ingame Server Manager, there are various server settings available. 

Dedicated Server  Setting | In-game Description | Notes   
---|---|---  
Server Name | Name of the Dedicated Server. Shown as the title of the Server in the Server Manager. |   
Admin Password | The Password used to limit Administrator privileges (such as Save Game loading, Server Options and New Game creation) to a certain set of players on a Dedicated Server. |   
Player Password Protection | A password that limits who can connect to the server and see information about the ongoing game session. |   
Auto-Load Session Name | Name of the session the Dedicated Server should automatically load the most recent save of on startup |   
Auto Pause | When the Server should automatically be paused when no players are connected. | Whether the game should automatically pause when no players are connected. Checked for Yes Pause   
Auto-Save on Player Disconnect | When the Server should automatically save the game when a player disconnects. | Whether the server should automatically save the game when a player disconnects. Checked for Yes Save   
Gameplay  Setting | In-game Description | Notes | Example   
---|---|---|---  
Server Restart Interval (hours) | Sets the amount of time in hours for the automatic server restart interval. | NOT AN INTERVAL. Hour at which the server automatically restarts daily. | 06:00   
Autosave Interval (minutes) | Sets the amount of time in minutes for the autosave interval. | Autosave every X minutes. | 10   
Send Gameplay Data | Unchecking this box means you will not send data to Coffee Stain Studios while playing. |  |   
Network Quality | Increasing network quality may improve client load times and network performance at the cost of server framerate. Experiment with these settings to see what works for you. |  |   
  
For settings not available in the UI or for more advanced configuration, see [Dedicated servers/Configuration files](/wiki/Dedicated_servers/Configuration_files "Dedicated servers/Configuration files"). 

### Loading a save file

Local saves can be uploaded from the game to a server through the "Manage Saves" tab of a server in the Server Manager. 

## Console commands

[](/wiki/File:Information.png) | _This list is[incomplete](/wiki/Category:Outdated "Category:Outdated"). You can help Satisfactory Wiki by [adding missing items](https://satisfactory.wiki.gg/wiki/Dedicated_servers?action=edit)._  
---|---  
  
_This article is[incomplete](/wiki/Category:Outdated "Category:Outdated"). You can help Satisfactory Wiki by [adding missing items](https://satisfactory.wiki.gg/wiki/Dedicated_servers?action=edit)._  


Here are a list of known commands for dedicated servers, as of v5.0.4 the console tab in the server manager is the only way to execute commands 

Command | Info   
---|---  
      
    
    quit
    
    
    
    stop
    
    
    
    exit
    

| Shuts down the game server process. If the game server is setup as a system service, it may automatically restart if these commands are used. Instead, stop the game server using the server's service manager.   
      
    
    server.SaveGame _saveName_
    

| Creates a save of the current session named _saveName_. For a _saveName_ with one or more spaces, use quotation marks around the name.   
  
## Server file Locations

### Server settings file

This is _not_ the location of configuration files. See [Dedicated_servers/Configuration_files](/wiki/Dedicated_servers/Configuration_files "Dedicated servers/Configuration files") for that. 

Platform | Filepath | Notes   
---|---|---  
Linux | `~/.config/Epic/FactoryGame/Saved/SaveGames/ServerSettings.PORT.sav` | `PORT` is the port the server is configured to run on. See [Dedicated Server Settings File](/wiki/Save_files#Dedicated_Server_Settings_File "Save files")  
Windows (user) | `%AppData%\Local\FactoryGame\Saved\SaveGames\ServerSettings.PORT.sav`  
Windows (NSSM) | `%WINDIR%\System32\config\systemprofile\AppData\Local\FactoryGame\Saved\SaveGames\ServerSettings.PORT.sav`  
Windows Server (Service) | `%WINDIR%\ServiceProfiles\NetworkService\AppData\Local\FactoryGame\Saved\SaveGames\ServerSettings.PORT.sav`  
  
### Save files

Platform | Path   
---|---  
Linux | `~/.config/Epic/FactoryGame/Saved/SaveGames/server`  
Windows (user) | `%AppData%\Local\FactoryGame\Saved\SaveGames\server`  
Windows (NSSM) | `%WINDIR%\System32\config\systemprofile\AppData\Local\FactoryGame\Saved\SaveGames\server`  
Windows Server (Service) | `%WINDIR%\ServiceProfiles\NetworkService\AppData\Local\FactoryGame\Saved\SaveGames\server`  
  
### Blueprint files

This directory may not exist until at least one blueprint has been created ingame. 

Platform | Path   
---|---  
Linux | `~/.config/Epic/FactoryGame/Saved/SaveGames/blueprints`  
Windows (user) | `%AppData%\Local\FactoryGame\Saved\SaveGames\blueprints`  
Windows (NSSM) | `%WINDIR%\System32\config\systemprofile\AppData\Local\FactoryGame\Saved\SaveGames\blueprints`  
Windows Server (Service) | `%WINDIR%\ServiceProfiles\NetworkService\AppData\Local\FactoryGame\Saved\SaveGames\blueprints`  
  
### Configuration files

_Main article:_[Dedicated_servers/Configuration_files](/wiki/Dedicated_servers/Configuration_files "Dedicated servers/Configuration files")

## Logs and crash dumps

Server logs may be found in the server's install directory in the `FactoryGame/Saved/Logs` directory. Note that depending on build and branch, not all of these may be present. 

The server keeps a running log of all of the messages it prints to the console. Logs are rotated on server start, with the latest (current) log being named `FactoryGame.log`, with the others following a datetime filename pattern `FactoryGame-backup-DATE-TIME.log`. On Linux, up to 15 log files are kept on disk. 

The server by default also uploads crash dump reports of every crashed server instance. A crash report directory with a randomly-generated UUID is created on server start, saved to the `FactoryGame/Saved/Crashes` directory. 

The game client follows a similar pattern, but the logs and crash dumps are kept in the user's `AppData` directory alongside save files. 

## Common errors or problems

If you believe the server is running but are unable to connect to it, the most common cause is a networking issue. The vast majority of common problems with successfully connecting to the Dedicated Server can be resolved by working through these diagnostic questions: 

### Is the server actually running?

The simplest reason for not being able to connect to the server is that it is not running. Either it was not started, or it has crashed and not been subsequently restarted. 

#### Linux

A simple way to check whether the server is running is with the command `pgrep -f FactoryServer.sh`. When running that command, either there will be no response (indicating no instances of the game server process are running), or one or more numbers (multiple indicating that multiple instances of the game server are running). Each number returned is the PID (Process ID) of that instance of the shell script which started the game server. 

#### Windows

Use Task Manager, or run `tasklist | find "FactoryServer.exe"`

### Is the server listening on the correct ports?

If multiple instances of the server were inadvertently started, the server may not be listening on the expected network ports. If the server is indeed running, the next step is to check to see which port the server is actually bound to (or "listening" on.) 

If you have not correctly forwarded the reliable messaging port, players can initiate a connection but will be perpetually stuck on the "loading" screen. 

#### Checking listening ports on Windows

On Windows, you can get a list of bound ports with the `Get-NetUDPEndpoint` and `Get-NetTCPConnection` commands. Adding some extra filters to it will restrict the output of that command to only show a list of IP addresses and ports to which an Unreal game server process (such as the Satisfactory Dedicated Server) is listening. Review that output for the expected port of 7777 or whatever port you have manually specified. The command and its typical output are shown below: 
    
    
    Get-NetUDPEndPoint | Select-Object LocalAddress, LocalPort, @{Name="Process";Expression={(Get-Process -Id $_.OwningProcess).ProcessName}} | Sort-Object -Property LocalPort,Process | Where-Object{$_.Process -like "FactoryServer-Win64-Shipping-Cmd"}
    
    LocalAddress LocalPort Process
    ------------ --------- -------
    0.0.0.0           7777 FactoryServer-Win64-Shipping-Cmd
    ::                7777 FactoryServer-Win64-Shipping-Cmd
    
    
    Get-NetTCPConnection -State Listen | Select-Object LocalAddress, LocalPort, @{Name="Process";Expression={(Get-Process -Id $_.OwningProcess).ProcessName}} | Sort-Object -Property LocalPort,Process | Where-Object{$_.Process -like "FactoryServer-Win64-Shipping-Cmd"}
    
    LocalAddress LocalPort Process
    ------------ --------- -------
    0.0.0.0           7777 FactoryServer-Win64-Shipping-Cmd
    ::                7777 FactoryServer-Win64-Shipping-Cmd
    

#### Checking listening ports on Linux

On Linux, bound ports can be listed with the `ss` command. The command and its expected output are shown below (The header line has been added): 
    
    
    $ ss -plnut | grep FactoryServer
    Netid      State       Recv-Q      Send-Q           Local Address:Port            Peer Address:Port     Process
    udp        UNCONN      0           0                      0.0.0.0:7777                 0.0.0.0:*         users:(("FactoryServer-L",pid=9456,fd=14))
    udp        UNCONN      0           0                            *:7778                       *:*         users:(("FactoryServer-L",pid=9456,fd=15))
    tcp        LISTEN      0           16                     0.0.0.0:7777                 0.0.0.0:*         users:(("FactoryServer-L",pid=9456,fd=12))
    tcp        LISTEN      0           16                           *:47647                      *:*         users:(("FactoryServer-L",pid=9456,fd=13))
    

### Is the server bound to the correct interface?

While checking on the port bindings in the previous step, take a look at the IP address associated with the port in the output from `ss` or `Get-NetUDPEndpoint`. If the `-multihome` switch was not used when starting the game server, the associated address may appear as one of `*`, `0.0.0.0`, or `::`. Any of these are fine, indicating the server is listening on all interfaces. If a specific address is shown, such as `192.168.1.203`, this is also fine, but be aware that _only_ that internal (or LAN) IP address will work for connecting to or forwarding connections to the server. 

### Is the server firewall allowing ingress on the correct ports?

In short, did you follow the steps in the Port Forwarding and Firewall Settings section above? Verify your host's firewall settings are configured to allow inbound connections on the UDP ports the Dedicated Server is using. 

### Are the port forwarding settings at the NAT pointing to the correct address and all three correct ports?

On your router or other network ingress point, double-check that the Port Forwarding settings are correctly configured to direct traffic on all three of the UDP Ports that the Dedicated Server uses to the LAN IP address of the host running the Dedicated Server. Be sure you are forwarding UDP ports, not TCP ports (If you are forwarding both TCP and UDP ports, that is fine, the important thing is that the UDP ports _must_ be forwarded). 

### Is the server accessible on the LAN?

From the same computer or another computer on the same LAN (i.e. generally in the same building), attempt to connect to the game server from the Server Manager in the game client.  
If this works, the server is running and the firewall on the server is allowing incoming connections.  
If not, verify that the server process is running, and double check the server's firewall settings. 

### Are you or anyone else able to connect to the server via the internet?

From a host which is _not_ on the same LAN, attempt to connect to the _public_ IP address of the host running the Dedicated Server from the Server Manager in the game client. If this works, then not only is the server clearly running and the server firewall allowing inbound connections, but the port forwarding settings are now confirmed to work as well-- you server is online and accessible! Have fun, and stay effective! 

### SDL Priority Manager
    
    
    Loading Steam API...Failed to init SDL priority manager: SDL not found
    
    Failed to set thread priority: per-thread setup failed
    
    Failed to set thread priority: per-thread setup failed

This issue can be resolved by downloading the dependency. For example, on a Debian-derived Linux distribution: 
    
    
    sudo apt install libsdl2-2.0-0:i386

### SteamAPI_Init(): Sys_LoadModule failed to load: /path/to/.steam/sdk64/steamclient.so
    
    
    steamclient.so: cannot open shared object file: No such file or directory
    /home/your_user/.steam/sdk64/steamclient.so
    /home/your_user/.steam/sdk64/steamclient.so: cannot open shared object file: No such file or directory
    [S_API] SteamAPI_Init(): Sys_LoadModule failed to load: /home/your_user/.steam/sdk64/steamclient.so

This issue can be resolved by creating a symbolic or hard link from the expected path to the location where the library actually exists, for example: 
    
    
    ln -s /usr/games/steamcmd/linux64/steamclient.so /home/your_user/.steam/sdk64/

Log output should change: 
    
    
    steamclient.so: cannot open shared object file: No such file or directory
    [S_API] SteamAPI_Init(): Loaded '/home/your_user/.steam/sdk64/steamclient.so' OK.  (First tried local 'steamclient.so')

### SteamCMD errors

#### state is 0x606 after update job
    
    
    Error! App '1690800' state is 0x606 after update job.

SteamCMD error `0x606` is thrown when SteamCMD attempts to update a file and the operating system says that it cannot write to the file because it is in use by another process. The most common cause for this is attempting to update while the server is already running. If you have already stopped the server and are still getting this error, the issue can be resolved by rebooting the host. 

### Trains not loading or unloading

This issue can be resolved by loading the save file into the game locally, rebuilding the [Train Station](/wiki/Train_Station "Train Station"), saving and loading the save file back onto the server. 

### Running on ARM
    
    
    user@totally_not_x86_64:~/SatisfactoryDedicatedServer$ ./Engine/Binaries/Linux/FactoryServer-Linux-Shipping FactoryGame
    -bash: ./Engine/Binaries/Linux/FactoryServer-Linux-Shipping: No such file or directory
    
    user@totally_not_x86_64:~/SatisfactoryDedicatedServer$ ./FactoryServer.sh
    ./FactoryServer.sh: 5: /home/user/SatisfactoryDedicatedServer/Engine/Binaries/Linux/FactoryServer-Linux-Shipping: not found
    

The server probably isn't x86_64. If running on ARM, install FEX or Box64 and read their documentation. 

### Running in a VM in Proxmox VE

The `kvm64` CPU type is not compatible with the dedicated server binaries. The dedicated server may run at first, but will crash when creating a new game. Try using `host` instead.[6]  
See Dedicated_servers#Requirements for other minimum system requirements. 

### The server becomes unreachable after disconnecting from the game

This may happen if the server is being hosted from the same machine a user is playing on.  
Known issue, but yet to be officially acknowledged. You can contribute by upvoting [this issue](https://questions.satisfactorygame.com/post/66e08561772a987f4a8a9d67) on the Q&A site. 

## FAQ

### How do I set a join password?

Click the "Change Password" button next to "Player password protection" in the Server Settings tab ingame.  
Yes, that's an interesting choice of name for that option, you're not alone. 

### My players can't join my server !!!

This is for users attempting to join a dedicated server but are encountering a Network Error: "Encryption token missing" error. 

Have them add your server using the Server Manager, then join through there.  
They should not use the 'Join Game' option. 

### My players are timing out !!!

_Main article:_[ Dedicated servers/Configuration files > Client disconnected for Timeout](/wiki/Dedicated_servers/Configuration_files#Client_disconnected_for_Timeout "Dedicated servers/Configuration files")

### How do I gracefully shut down the Dedicated Server?

Regardless of which operating system the server is running on, the best way to shut down the server is with the HTTPS (REST) API, using the Shutdown function. Failing that, it can be gracefully shut down by connecting to the server in the Server Manager in the game client and issuing the `quit` command in the Console tab. Shutting down the server without accessing it via the game client depends on the operating system it is running on. 

#### Linux

The server process can be gracefully shut down by sending `SIGINT` to the process, or if the server is managed by `systemd`, with the command `systemctl stop satisfactory`, where "satisfactory" is the name of the service unit file. 

#### Windows

If the server is running 'interactively' (ie, there is a window showing the server logs in real time), focus on that window by clicking on it, then hold down the `Ctrl` key and press `C`. _Do not_ just close the window by clicking on the "X"; this will kill the server process instantly instead of allowing it to clean up after itself and finish writing files to disk. If it is running as a service, stop it from the Services tab in Task Manager. 

### How do I update the dedicated server?

#### Manually updating

##### Steam client

If the game server was installed using the desktop Steam client, it should automatically update shortly after the update is released. The server instance may need to be shut down, and optionally have Steam verify the local files. Another option is to restart Steam to force an update check. 

##### SteamCMD

If the server was installed using the SteamCMD command-line client, shut down the server instance, then use the same command used to install the server to check for and install an update. 

One can also run SteamCMD as follows: 
    
    
    steamcmd +force_install_dir <game_server_directory_change_this> +login anonymous +app_update 1690800 validate +quit
    

`<game_server_directory_change_this>` should be the directory the game server was downloaded to. 

#### Automatically

_Main article:_[Dedicated_servers/Automatic_updates](/wiki/Dedicated_servers/Automatic_updates "Dedicated servers/Automatic updates")

### How do I reset the Administrator password?

_See:_Dedicated_servers#Server_settings_file

  
Delete the `ServerSettings.PORT.sav` file, where `PORT` is the server port number (e.g. `ServerSettings.7777.sav`), which can be found just above the server savegame directory. Please note that doing this will also reset the server name, player password, auto load session name, and certificate. The next time the server is started, it can be claimed as a new server, and a new administrator password can be set. 

### What to do when client gets error "Certificate Verify Result: certificate is not yet valid"

  * Check that client computer's local time and timezone, or UTC time, are set correctly. If they weren't, correct them and try again.
  * Check that server computer's local time and timezone, or UTC time, are set correctly. If they weren't, correct them and do the following extra steps: 
    1. Stop the server
    2. Delete the `ServerSettings.PORT.sav` file
    3. Restart the server



### How can I have more than four players in my server?

_Main article:_[Dedicated_servers/Configuration_files#Increasing_Player_Count](/wiki/Dedicated_servers/Configuration_files#Increasing_Player_Count "Dedicated servers/Configuration files")

### I thought the Dedicated Server was multi-threaded- why am I only seeing one core being used?

While it is _technically_ multi-threaded, the game and/or game engine's design means that most of the multi-threaded work still relies on the primary thread. [According to](https://discord.com/channels/370472939054956546/902621736602861588/911375176002854932) a developer back in November 2021, 

“  | _We never intended to say the server will evenly use all your cores. We meant more that the server spawns up to 26 threads (per work set). The game loop is still fundamentally single threaded though and all multi threaded work is happening on ticks. So one core will always work harder than others as a result._ | „   
---|---|---  
| ~ **Bogdan** |   
  
### I was running an Experimental server, but I want to move it to Stable, and it's not converting. What do I do?

Sometimes, Steam can helpfully remember which branch you have selected. If you were using `-beta experimental` to stay pinned on the Experimental branch, removing it from your update command may not roll you to Stable. To _force_ this to happen, use `-beta public` to force the switch. 

### How can I get my friends to join my server?

In order for your friends to join your server, you will need to give them your Public IP Address (WAN IP) and the standard port if it differs from 7777. You can obtain this by searching for "what is my ip" in most search engines. The game takes care of communicating the correct reliable messaging port for you. 

Please note however that this will require you setup port forwarding correctly and have the correct firewall entries in place to allow connections into the network where the server is hosted. 

### How can I have the server restart at a certain time?

Change the option labeled "Restart Interval" to the time the server should restart every day.  
Yes, this one is also weirdly named. 

### The Dedicated Server stops after throwing two warnings; what do I do?

There are two common warnings that you will see once the server has finished its startup process. These are _warnings_ , not _errors_ , and in this case they can be ignored. If you see the two messages below there is nothing wrong, and the server is now just waiting for a client connection. Both messages related to the Epic Online Store (EOS), which the server has no interactions with, and so these warnings are completely innocuous.
    
    
    LogOnline: Warning: OSS: EOSSDL-LogEOSP2P: NAT Detection Failed, unable to resolve host
    LogOnline: Warning: OSS: EOSSDK-LogEOSAnalytics: EOS STA Analytics disabled for route
    

### I added the server to the Server Browser via IPv6 and get a ping, but it says "Failed to Connect to the Server API", what do I do?

Connecting to a server via raw IPv6 seems to be bugged. Instead of connectig to a raw IPv6 address (like `1111:2222::8888`), try using literal notation or putting brackets around the address. 

## Community tools

### Connection testers

URL | Description | TCP | UDP   
---|---|---|---  
<https://github.com/dopeghoti/SF-Tools> | Toolkit for the Satisfactory Dedicated Server | ✅ | ✅   
<https://gist.github.com/SparxySys/4e96f18c567a0e33cf37e95980dbfc74> | Tests connection to a Satisfactory Server | ✅ | ✅   
  
### CLI tools

URL | Description | Notes | API Calls Implemented   
---|---|---|---  
<https://github.com/dopeghoti/SF-Tools/> | Tools for the Satisfactory Dedicated Server including REST API endpoint calls and a Discord server status bot  | Requires editing and an existing auth token  | `ApplyServerOptions`, `EnumerateSessions`, `GetServerOptions`, `HealthCheck`, `QueryServerState`, `Shutdown`, `VerifyAuthenticationToken`  
<https://github.com/Feyr/satisfactory-python-cli> | a quick and dirty cli for the satisfactory dedicated server |  | `QueryServerState`, `SaveGame`, `Shutdown`, `EnumerateSessions`, `GetServerOptions`  
<https://github.com/micah686/SatisfactoryAPI> | A C# Server Management utility and library | No binaries, compile it yourself | All, but only `HealthCheck` and `QueryServerState` are used by default.   
<https://github.com/terrordrone5nl/Satisfactory-HTTPS-API-Powershell> | Scripts to manage the Satisfactory Dedicated server via Powershell | Requires editing | `DeleteSaveFile`, `DownloadSaveGame`, `SaveGame`, `Shutdown`  
  
### Discord bots

URL | Description   
---|---  
<https://github.com/inroma/Satisfactory-Bot> | Discord Bot to interact with the dedicated server API   
  
### GUI tools

URL | Description   
---|---  
<https://github.com/asidsx/SatisfactoryPyServerInstaller> | one-click server installer for Windows   
  
### SDKs

URL | Description | Language | Lightweight Query API | HTTPS API   
---|---|---|---|---  
<https://github.com/benjamin-lawson/SatisfactoryClient> | A C# NuGet package for interacting with the HTTPS API | C# | ✅ | ✅   
<https://github.com/oarko/SF-ToolsPHP> | Toolkit for the Satisfactory Dedicated Server using PHP | PHP | ✅ | ✅   
<https://github.com/idebeijer/satisfactory-client-go> | A Go (Golang) client for the Satisfactory Dedicated Server HTTP API | Go | ❌ | ✅   
<https://github.com/Jayy001/PyFactoryBridge> | A Python library for the Satisfactory 1.0 Dedicated Server API | Python | ❌ | ✅   
<https://github.com/micah686/SatisfactoryAPI> | A C# Server Management utility and library | C# | ❌ | ✅   
<https://github.com/Programmer-Timmy/satisfactory-dedicated-server-api-SDK> | A SDK for interacting with the Satisfactory Dedicated Server API | Python | ❌ | ✅   
<https://github.com/Shinigami92/satisfactory-server-api-client> | Universal Satisfactory Server API client for JavaScript | JavaScript | ❌ | ✅   
<https://github.com/jpeggdev/Satisfactory-RemoteAdmin> | A comprehensive Model Context Protocol (MCP) server that provides tools for managing Satisfactory Dedicated Servers remotely.[7] | TypeScript | ✅ | ✅   
<https://github.com/Programmer-Timmy/satisfactory-dedicated-server-sdk> | A TypeScript SDK that provides a typed client (SatisfactoryApi), models, error classes, and helpers to programmatically interact with Satisfactory dedicated servers; fully documented.  | TypeScript  | ❌  | ✅   
  
### API documentation

URL | Description   
---|---  
<https://github.com/satisfactory-oas/spec> | OpenAPI (OAS) specification implementation for the Satisfactory Server HTTPS API   
  
### Docker images

URL | Description   
---|---  
<https://github.com/wolveix/satisfactory-server> | A Dockerized version of the Satisfactory dedicated server   
  
## API

With the release of 1.0, there is now a [Lightweight Query API](/wiki/Dedicated_servers/Lightweight_Query_API "Dedicated servers/Lightweight Query API") and an [HTTPS API](/wiki/Dedicated_servers/HTTPS_API "Dedicated servers/HTTPS API"). 

## Trivia

  * The console of the server (as of Patch 0.5.0.12) serializes boolean values with typos: "IsAwake newState = **flase** ", "IsAwake newState = **ture** ". This is considered a common typo.
  * When [Patch 0.5.0.0](/wiki/Patch_0.5.0.0 "Patch 0.5.0.0") was released, Dedicated Servers were initially only available to those using Steam. On December 7, 2021, it was announced on Twitch Stream by Community Manager Snutt Treptow that [Dedicated Servers were available on Epic Games](https://www.youtube.com/watch?v=7nCntR0EE8g&t=247s).



## See also

  * [Dedicated Servers - Configuration Files](/wiki/Dedicated_servers/Configuration_files "Dedicated servers/Configuration files")
  * [Dedicated Servers - Running as a Service](/wiki/Dedicated_servers/Running_as_a_Service "Dedicated servers/Running as a Service")
  * [Dedicated Servers - Automatic Updates](/wiki/Dedicated_servers/Automatic_updates "Dedicated servers/Automatic updates")
  * [Dedicated Servers - HTTPS API](/wiki/Dedicated_servers/HTTPS_API "Dedicated servers/HTTPS API")



## History

_Due to the extensive length of dedicated server history, it was[moved to a separate page](/wiki/Dedicated_servers/History "Dedicated servers/History")._

## References

  1. ↑ [Discord - Help with Error Message "Failed to connect to the server API"](https://discord.com/channels/370472939054956546/902621736602861588/1291837554865340437)
  2. ↑ <https://wiki.debian.org/DebianFirewall>
  3. ↑ <https://help.ubuntu.com/community/UFW>
  4. ↑ <https://en.wikipedia.org/wiki/Carrier-grade_NAT>
  5. ↑ [YouTube - Dedicated Servers have LEVELED UP! - Unreal Console](https://www.youtube.com/watch?v=v8piXNQwcUw&t=327s)
  6. ↑ <https://pve.proxmox.com/wiki/Qemu/KVM_Virtual_Machines#qm_virtual_machines_settings>
  7. ↑ [Reddit - Satisfactory Dedicated Remote Server MCP Server](https://www.reddit.com/r/SatisfactoryGame/comments/1l9qi4y/satisfactory_dedicated_remote_server_mcp_server/)



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
Dedicated servers| Dedicated servers • [Running as a Service](/wiki/Dedicated_servers/Running_as_a_Service "Dedicated servers/Running as a Service") • [Configuration files](/wiki/Dedicated_servers/Configuration_files "Dedicated servers/Configuration files") • [Automatic updates](/wiki/Dedicated_servers/Automatic_updates "Dedicated servers/Automatic updates") • [HTTPS API](/wiki/Dedicated_servers/HTTPS_API "Dedicated servers/HTTPS API") • [Lightweight Query API](/wiki/Dedicated_servers/Lightweight_Query_API "Dedicated servers/Lightweight Query API")  
Other| [Hypertube cannon](/wiki/Tutorial:Hypertube_cannon "Tutorial:Hypertube cannon") • [Hypertube brake](/wiki/Tutorial:Hypertube_brake "Tutorial:Hypertube brake") • [Steam Deck & Controller setup](/wiki/Tutorial:Controller_setup "Tutorial:Controller setup") • [Extracting UI icons](/wiki/Tutorial:Extracting_UI_icons "Tutorial:Extracting UI icons")
  *[v]: View this template
  *[e]: Edit this template
  *[h]: History of this template
  *[his]: his trivia section
