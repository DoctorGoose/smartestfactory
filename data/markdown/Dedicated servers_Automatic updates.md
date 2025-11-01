# Dedicated servers/Automatic updates

## Contents

  * 1 Automating Updates
    * 1.1 Linux
      * 1.1.1 Systemd
      * 1.1.2 Docker
    * 1.2 Windows
      * 1.2.1 NSSM
        * 1.2.1.1 Batch file
        * 1.2.1.2 Automating
  * 2 See also



[](/wiki/File:Merge.svg) | It has been _**suggested**_ that this article or section be **merged with[Dedicated servers](/wiki/Dedicated_servers "Dedicated servers").**

  * Reason: Could be incorporated into § How do I update the Dedicated Server?
  * Please discuss this on the [Discussion page](/wiki/Talk:Dedicated_servers/Automatic_updates?action=edit&redlink=1 "Talk:Dedicated servers/Automatic updates \(page does not exist\)").

  
---|---  
  


It has been _**suggested**_ that this article or section be **merged with[Dedicated servers](/wiki/Dedicated_servers "Dedicated servers").**  


  * Reason: Could be incorporated into § How do I update the Dedicated Server?
  * Please discuss this on the [Discussion page](/wiki/Talk:Dedicated_servers/Automatic_updates?action=edit&redlink=1 "Talk:Dedicated servers/Automatic updates \(page does not exist\)").  




This page describes how to **automate[dedicated server](/wiki/Dedicated_servers "Dedicated servers") updates**. 

## Automating Updates

### Linux

#### Systemd

If the service file shown in [Dedicated_servers/Running_as_a_Service#Systemd](/wiki/Dedicated_servers/Running_as_a_Service#Systemd "Dedicated servers/Running as a Service") is being used, the server will update every time the service is started. 

#### Docker

Check the Docker image's documentation. 

### Windows

#### NSSM

You can use the [Non-Sucking Service Manager](https://nssm.cc/) to automate the update process 

##### Batch file

First, you need to make a batch file to update FactoryServer.exe. Open a text editor of your choice, and paste the below code: 

For Early Access:
    
    
    "C:\Program Files (x86)\Steam\steamcmd.exe" +force_install_dir "C:\GameServers\SatisfactoryServer" +login anonymous +app_update 1690800 -beta public validate +quit
    "C:\GameServers\nssm.exe" start SatisfactoryServerService
    

For Experimental:
    
    
    "C:\Program Files (x86)\Steam\steamcmd.exe" +force_install_dir "C:\GameServers\SatisfactoryServer" +login anonymous +app_update 1690800 -beta experimental validate +quit
    "C:\GameServers\nssm.exe" start SatisfactoryServerService
    

Where the first path is to SteamCMD, the second path is to the folder with FactoryServer.exe, and the third path is to the folder with nssm.exe. 

Now press Ctrl+S, and save the file to the directory with FactoryServer.exe (in our case, C:\GameServers\SatisfactoryServer) as "update.bat" 

##### Automating

Once you've downloaded and installed NSSM, navigate to the directory containing nssm.exe and run the below command: 
    
    
    nssm.exe install SatisfactoryServerUpdate
    

This will pull up a GUI for configuration. Set the "**Path** " to the location of update.bat. Then, go to "**Details** ", change "**Startup Type** " to "**Automatic** ", and then click "install". Next, run this command: 
    
    
    nssm.exe edit SatisfactoryServerService
    

Now, Go to "**Details** " and change "**Startup Type** " to "**Manual** ". Then go the the "**Shutdown** " tab and un-check the "**Generate Control-C** " box. When finished, click "Edit Service". 

Finally, run this command: 
    
    
    nssm.exe start SatisfactoryServerUpdate
    

This will start the update process, and then start the server once finished. 

Other useful `nssm` commands: 
    
    
    nssm.exe status SatisfactoryServerUpdate # Checks the status of the Service
    

## See also

  * [Dedicated Servers - Main Page](/wiki/Dedicated_servers "Dedicated servers")
  * [Dedicated Servers - Configuration Files](/wiki/Dedicated_servers/Configuration_files "Dedicated servers/Configuration files")
  * [Dedicated Servers - Running as a Service](/wiki/Dedicated_servers/Running_as_a_Service "Dedicated servers/Running as a Service")
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
Dedicated servers| [Dedicated servers](/wiki/Dedicated_servers "Dedicated servers") • [Running as a Service](/wiki/Dedicated_servers/Running_as_a_Service "Dedicated servers/Running as a Service") • [Configuration files](/wiki/Dedicated_servers/Configuration_files "Dedicated servers/Configuration files") • Automatic updates • [HTTPS API](/wiki/Dedicated_servers/HTTPS_API "Dedicated servers/HTTPS API") • [Lightweight Query API](/wiki/Dedicated_servers/Lightweight_Query_API "Dedicated servers/Lightweight Query API")  
Other| [Hypertube cannon](/wiki/Tutorial:Hypertube_cannon "Tutorial:Hypertube cannon") • [Hypertube brake](/wiki/Tutorial:Hypertube_brake "Tutorial:Hypertube brake") • [Steam Deck & Controller setup](/wiki/Tutorial:Controller_setup "Tutorial:Controller setup") • [Extracting UI icons](/wiki/Tutorial:Extracting_UI_icons "Tutorial:Extracting UI icons")
  *[v]: View this template
  *[e]: Edit this template
  *[h]: History of this template
  *[his]: his trivia section
