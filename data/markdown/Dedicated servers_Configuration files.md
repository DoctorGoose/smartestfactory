# Dedicated servers/Configuration files

## Contents  
  
  * 1 Overview
  * 2 Configuration Editing
    * 2.1 Default and Configurable Port Ranges
    * 2.2 Disabling Server Crash Reporting
    * 2.3 Client disconnected for Timeout
    * 2.4 Number of Kept Autosaves
    * 2.5 Increasing Player Count
      * 2.5.1 In Server Configuration
      * 2.5.2 Or as a Startup Parameter
    * 2.6 Autosave Interval
    * 2.7 Server tick rate
    * 2.8 Seasonal events
    * 2.9 UObject Limit Increase
  * 3 See also



This page details configuration files used by [dedicated servers](/wiki/Dedicated_servers "Dedicated servers"). 

## Overview

Satisfactory uses Unreal Engine, which stores many of its vital settings and configurations in various "ini" (short for "initialization") files. These files are located in a directory relative to the server's base installation folder, as noted below: 

Configuration files location  Platform | Path   
---|---  
Linux | `<installation_directory>/FactoryGame/Saved/Config/LinuxServer/`  
Windows | `<installation_directory>\FactoryGame\Saved\Config\WindowsServer\`  
  
While the basic server settings may be edited via the in-game options menus, there are many, many more settings that may be changed by manually editing the appropriate ini files. 

## Configuration Editing

Server ini files may not be saved/generated until the server is closed gracefully for the first time, e.g, by using the console 'quit' command, or sending `SIGINT` to the process. 

**Always make ini edit changes with the game server shut down. The ini files are written to on graceful shutdown, and you may find your changes overwritten otherwise.[1]**  


**Be aware that any changes to ini files may be overwritten when a new update or patch is released, possibly necessitating a re-edit. Also, do not set the ini files to be "read-only" after you modify them as this can cause issues with future patches.**  


If you are unable to locate any of the listed ini files, you will need to start the server at least once first. See [Dedicated_servers#Claiming_the_Server_and_Starting_a_Game](/wiki/Dedicated_servers#Claiming_the_Server_and_Starting_a_Game "Dedicated servers"). 

**If a section to be added already exists in the file, append or overwrite its contents to the section. If a section is not present or the file does not exist, create the section or file.**

Below are a few configuration settings that the community has discovered. 

### Default and Configurable Port Ranges

[Version 1.1](/wiki/Patch_1.1.1.0#Default_and_Configurable_Port_Ranges "Patch 1.1.1.0") added the following settings in Engine.ini control port allocation: 

`Engine.ini`
    
    
    [/Script/ReliableMessaging.ReliableMessagingTCPFactory]
    PortRangeBegin=8888
    PortRangeLength=512
    ExternalPortRangeBegin=-1
    

  * The server will attempt to bind within PortRangeBegin + PortRangeLength range.
  * By default, the server starts at port 8888 and tries up to 512 ports until it finds an available one.



### Disabling Server Crash Reporting

When running on Linux, the server uploads crash reports by default. The developers can then use these crash reports to help pinpoint issues for future patches.   
  
`Engine.ini`
    
    
    [CrashReportClient]
    bImplicitSend=False
    

### Client disconnected for Timeout

Client systems with older hardware or slower connections may need a higher connection timeout limit than the default 30 seconds.   
  
`Engine.ini`
    
    
    [/Script/OnlineSubsystemUtils.IpNetDriver]
    InitialConnectTimeout=XX.0
    ConnectionTimeout=XX.0
    

_XX_ is the number of seconds for the connection timeout counter to use. 

  * _InitialConnectTimeout_ = Number of seconds to wait for a new network connection to be established before destroying the connection.
  * _ConnectionTimeout_ = Number of seconds to wait before considering an established connection timed out.



### Number of Kept Autosaves

Currently, the server defaults to three autosaves that are rotated (when the server creates a new autosave, the oldest is deleted and the others are moved down the list. Currently these are: 

  * SessionName_autosave_0.sav
  * SessionName_autosave_1.sav
  * SessionName_autosave_2.sav



To override the default, replace _XX_ with the number of autosaves the server should rotate through.   
  
`Engine.ini`
    
    
    [/Script/FactoryGame.FGSaveSession]
    mNumRotatingAutosaves=XX
    

### Increasing Player Count

Up to 127 players are theoretically possible, but not practically. 

**Before changing the following setting, note that the server is tuned to be most performant with the default player cap of four. Increasing this limit may have negative effects on server stability, performance, and resource usage.**

#### In Server Configuration

Set `MaxPlayers` to the desired player cap for the server:  
  
`Game.ini`
    
    
    [/Script/Engine.GameSession]
    MaxPlayers=8
    

#### Or as a Startup Parameter

Add `-ini:Game:[/Script/Engine.GameSession]:MaxPlayers=8` as a parameter to the server startup script. 

### Autosave Interval

Currently the server defaults to saving the game every 300 seconds (5 minutes). Keep in mind that shorter times mean that while the server will save the game more often, it also means a drop in server performance while the server is saving. To override the default, do the following: 

  1. Start the game client and click on Server Manager
  2. Select the server to modify and authenticate if required
  3. Click on the Console tab
  4. Enter in the command `FG.AutosaveInterval _xxx_`, replacing _xxx_ with the number of seconds between saves.



### Server tick rate

There are three sections of modifications to make. Replace _XX_ with the desired number of ticks per second (default: 30):   
  
`Engine.ini`
    
    
    [/Script/OnlineSubsystemUtils.IpNetDriver]
    NetServerMaxTickRate=xx
    LanServerMaxTickRate=xx
    
    [/Script/SocketSubsystemEpic.EpicNetDriver]
    NetServerMaxTickRate=xx
    LanServerMaxTickRate=xx
    
    [/Script/Engine.Engine]
    NetClientTicksPerSecond=xx
    

Note that this is an upper limit (up-to), and the server will only reach the specified tickrate if hardware allows. Also note that if undesirable side effects are observed, lower the tick rate and retest before further troubleshooting. 

Note that the game's default tick rate is good for most scenarios. Increasing it will _not_ help with lags - if the hardware can't hit the default 30, increasing it won't help. 

### Seasonal events

Seasonal events, such as [FICSMAS](/wiki/FICSMAS "FICSMAS"), can be disabled (0) or enabled (1). Note that the line will disappear after the server is restarted, but will take effect regardless.   
  
`GameUserSettings.ini`
    
    
    [/Script/FactoryGame.FGGameUserSettings]
    FG.DisableSeasonalEvents 0
    

### UObject Limit Increase

_Main article:_[ Unreal Engine > UObject Limit Increase](/wiki/Unreal_Engine#UObject_Limit_Increase "Unreal Engine")

  


## See also

  * [Dedicated Servers - Main Page](/wiki/Dedicated_servers "Dedicated servers")
  * [Dedicated Servers - Running as a Service](/wiki/Dedicated_servers/Running_as_a_Service "Dedicated servers/Running as a Service")
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
Dedicated servers| [Dedicated servers](/wiki/Dedicated_servers "Dedicated servers") • [Running as a Service](/wiki/Dedicated_servers/Running_as_a_Service "Dedicated servers/Running as a Service") • Configuration files • [Automatic updates](/wiki/Dedicated_servers/Automatic_updates "Dedicated servers/Automatic updates") • [HTTPS API](/wiki/Dedicated_servers/HTTPS_API "Dedicated servers/HTTPS API") • [Lightweight Query API](/wiki/Dedicated_servers/Lightweight_Query_API "Dedicated servers/Lightweight Query API")  
Other| [Hypertube cannon](/wiki/Tutorial:Hypertube_cannon "Tutorial:Hypertube cannon") • [Hypertube brake](/wiki/Tutorial:Hypertube_brake "Tutorial:Hypertube brake") • [Steam Deck & Controller setup](/wiki/Tutorial:Controller_setup "Tutorial:Controller setup") • [Extracting UI icons](/wiki/Tutorial:Extracting_UI_icons "Tutorial:Extracting UI icons")  
  
  1. ↑ [I followed the wiki guide but when I rebooted the server it reverted my changes to engine.ini](https://discord.com/channels/370472939054956546/902621736602861588/1291444132111454341)


  *[v]: View this template
  *[e]: Edit this template
  *[h]: History of this template
  *[his]: his trivia section
