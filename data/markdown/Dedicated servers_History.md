# Dedicated servers/History

This page serves as a categorized history section for the [Dedicated servers](/wiki/Dedicated_servers "Dedicated servers") page, due to the large amount of updates that have been released relating to Dedicated Servers. These changes are categorized by either Early Access or Full Release. 

Dedicated server patches are being released in par with every game patch. This section only lists changes directly related to the dedicated server itself, changes to multiplayer in general are tracked [here](/wiki/Multiplayer/History "Multiplayer/History"). 

## Full Release

All Game Patches from [Patch 1.0](/wiki/Patch_1.0 "Patch 1.0") and onward are now placed in this one unified subsection. 

  * [Patch 1.1.1.5](/wiki/Patch_1.1.1.5 "Patch 1.1.1.5"): Fixed null pointer crash when logging discrepancy between picked up items on client and server
  * [Patch 1.1.1.4](/wiki/Patch_1.1.1.4 "Patch 1.1.1.4"): Potential fixes to desync issues by adding a keep alive mechanism to the TCP implementation of Reliable Messaging
  * [Patch 1.1.1.3](/wiki/Patch_1.1.1.3 "Patch 1.1.1.3"): Potential fixes to desync and high CPU usage issues
  * [Patch 1.1.1.1](/wiki/Patch_1.1.1.1 "Patch 1.1.1.1"): Potential fix for Dedicated Server crash when unequipping the [Zipline](/wiki/Zipline "Zipline")
  * [Patch 1.1.0.6](/wiki/Patch_1.1.0.6 "Patch 1.1.0.6"): Potential fixes for multiple ReliableMessaging related crashes
  * [Patch 1.1.0.4](/wiki/Patch_1.1.0.4 "Patch 1.1.0.4")
    * Fixed infinite loading screen after server save/load cycle on Linux Dedicated Server
    * Potential fixes for Crashes when reloading a Save while the server is running and there are clients in the session
  * [Patch 1.1.0.1](/wiki/Patch_1.1.0.1 "Patch 1.1.0.1"): Potential fix for a crash related to Reliable Replication on Dedicated Servers
  * [Patch 1.1.0.0](/wiki/Patch_1.1.0.0 "Patch 1.1.0.0")
    * Introduced the port TCP 8888 for reliable messaging, and additional command-line and configuration options to control its assignment and external remapping. 
      * Due to the extensive changes made, view [Dedicated Servers - Port Forwarding Updates](/wiki/Patch_1.1.0.0#Dedicated_Servers_-_Port_Forwarding_Updates "Patch 1.1.0.0") in patch notes.
  * [Patch 1.0.1.6](/wiki/Patch_1.0.1.6 "Patch 1.0.1.6")
    * Bulk data replication 
      * This change requires you to open your current TCP Port (7777 by default) on top of the already open UDP port, you also need to port forward the same port as the game port (7777 UDP by default) +20000 TCP (27777 TCP by default)
      * Please note that the game port values should not be set to a value larger than 45535 since we do not have good enough error handling for this at the moment but will be addresed in the future as we are still fleshing the port selection aspect out
    * Improves the Foliage, Lightweight, Recipe and Schematic systems in [Multiplayer](/wiki/Multiplayer "Multiplayer") and Dedicated Servers
  * [Patch 1.0.1.5](/wiki/Patch_1.0.1.5 "Patch 1.0.1.5")
    * Fixed an issue where [lightweight buildable's](/wiki/Unreal_Engine#Lightweight_Actors "Unreal Engine") could be seen but not interacted with, either by walking through them or by dismantling them but not actually being able to remove them until restarting a Dedicated Servers or rejoining a [Multiplayer](/wiki/Multiplayer "Multiplayer") Session 
      * This was most commonly seen with Foundations and Walls, but could also affect other buildable's like Road Barriers, Catwalk Walkways, etc.
    * Fixed an issue where Lightweight buildable's would fail to sample (MMB) in Dedicated Servers or Multiplayer sessions
    * Fixed Windows Dedicated Server not working after a player disconnects until it is restarted 
      * This change required making some changes to port binding, so let us know about any new unexpected behavior
  * [Patch 1.0.1.3](/wiki/Patch_1.0.1.3 "Patch 1.0.1.3"): Added a scroll bar to the Server Options in the Server Manager to prevent the “Disable Seasonal Events” option from flowing out of the UI and displaying over the description text
  * [Patch 1.0.1.2](/wiki/Patch_1.0.1.2 "Patch 1.0.1.2")
    * Always show options that are marked as "Hidden in Game" or "Hidden in Main Menu" in Server Manager Server Options tab, regardless of whether the dedicated server has a save loaded or not. 
      * This allows for toggling options like “Disable Seasonal Events” on servers that are already running, Please note that this setting requires a server restart to take effect
  * [Patch 1.0.1.1](/wiki/Patch_1.0.1.1 "Patch 1.0.1.1"): Fixed incorrect title in Network Errors
  * [Patch 1.0.0.5](/wiki/Patch_1.0.0.5 "Patch 1.0.0.5"): Fixed [Advanced Game Settings](/wiki/Advanced_Game_Settings "Advanced Game Settings") being activated unintentionally transferring from the current save to another when starting a new session through the Server Manager
  * [Patch 1.0.0.4](/wiki/Patch_1.0.0.4 "Patch 1.0.0.4")
    * Updated the text for the Server Restart Interval option to make it clearer to understand
    * Fix for Dedicated Server failing to bind the Server API shutting down in some scenarios
  * [Patch 1.0.0.3](/wiki/Patch_1.0.0.3 "Patch 1.0.0.3")
    * Fixed Advanced Game Settings not being Reset when creating a new game in some scenarios
    * Fixed Dedicated Server failing to bind the Server API shutting down the server
  * [Patch 1.0.0.1](/wiki/Patch_1.0.0.1 "Patch 1.0.0.1")
    * Fixed two crashes related to AbstractInstance that could occur when joining specific saves in [Multiplayer](/wiki/Multiplayer "Multiplayer") or Dedicated servers
    * Fix for Dedicated Server Manager/HTTP API not binding to the correct bind address when there is only one network adapter in the system or multihome active, resulting in Server Manager not working.
  * [Patch 1.0](/wiki/Patch_1.0 "Patch 1.0"):[1][2]
    * Now easier to install due to a decrease in the install size.
    * Now only uses one port: UDP/TCP 7777.
    * Introduced both a Windows application and an in-game console application.
    * Introduced support for both IPv4 and IPv6.
    * Introduced support for TLS end-to-end encryption for both server and game data/traffic.
    * Introduced support for [Advanced Game Settings](/wiki/Advanced_Game_Settings "Advanced Game Settings").
    * Introduced a way for server admins to download the save file directly from within the server manager.
    * Introduced support for [HTTP API](/wiki/Dedicated_servers/HTTPS_API "Dedicated servers/HTTPS API") methods between the server and the client. 
      * Future mod support will allow use of the HTTP API to perform functions from within game mods.
    * Improved the console screen.
    * Made it easier to create new game sessions.
    * Made it easier to set up [server configuration settings](/wiki/Dedicated_servers/Configuration_files "Dedicated servers/Configuration files").
    * Autosave and server status notifications are now sent to all clients.



## Early Access

All Game Patches from [Patch 0.5.0.0](/wiki/Patch_0.5.0.0 "Patch 0.5.0.0") (Introduction) to [Patch 0.8.2.8](/wiki/Patch_0.8.2.8 "Patch 0.8.2.8") are now placed in this one unified subsection. 

  * [Patch 0.8.2.8](/wiki/Patch_0.8.2.8 "Patch 0.8.2.8"): Potential fix for foliage not being removed when playing as Client in both regular [Multiplayer](/wiki/Multiplayer "Multiplayer") and Dedicated Server
  * [Patch 0.8.2.7](/wiki/Patch_0.8.2.7 "Patch 0.8.2.7"): Potential fix to some major log spam on Dedicated Server on Linux
  * [Patch 0.8.2.6](/wiki/Patch_0.8.2.6 "Patch 0.8.2.6"): Potential fix to leftover connectivity issues
  * [Patch 0.8.2.5](/wiki/Patch_0.8.2.5 "Patch 0.8.2.5"): Fixed a crash for [Multiplayer](/wiki/Multiplayer "Multiplayer") / Dedicated Server Clients that sometimes occurred when trying to snap a [Power Pole](/wiki/Power_Pole "Power Pole") to a [Power Line](/wiki/Power_Line "Power Line")
  * [Patch 0.8.2.4](/wiki/Patch_0.8.2.4 "Patch 0.8.2.4"): Fixed Railway [Block/Path Signal](/wiki/Train_Signals "Train Signals") Visualization crashing for [Multiplayer](/wiki/Multiplayer "Multiplayer") / Dedicated Servers Clients
  * [Patch 0.8.2.0](/wiki/Patch_0.8.2.0 "Patch 0.8.2.0")
    * Potential fix for bug where item stacks can not be split in the inventory for Clients
    * Fixed Dedicated Servers Clients not continuing to have [Flight Mode](/wiki/Advanced_Game_Settings#Gameplay "Advanced Game Settings") enabled after logging in and out of a session
  * [Patch 0.8.1.2](/wiki/Patch_0.8.1.2 "Patch 0.8.1.2"): Fixed crash when joining a Dedicated Server related to [signs](/wiki/Signs "Signs")
  * [Patch 0.8.1.1](/wiki/Patch_0.8.1.1 "Patch 0.8.1.1"): Fixed Dedicated Server not working on Linux
  * [Patch 0.8.0.4](/wiki/Patch_0.8.0.4 "Patch 0.8.0.4"): 
    * Fixed a crash on startup for Dedicated Server when the server query port was set to a value that exceeded the maximum value of an int16
    * Temporary fix for audio log spam on Dedicated Servers when using vehicles which would lead into clients being kicked out of the Server
  * [Patch 0.7.1.1](/wiki/Patch_0.7.1.1 "Patch 0.7.1.1"): Fixed [Multiplayer](/wiki/Multiplayer "Multiplayer") and Dedicated Server Clients not being able to place [Power Poles](/wiki/Power_Poles "Power Poles") off a [Power Cable](/wiki/Power_Line "Power Line") in the [Blueprint Designer](/wiki/Blueprint_Designer "Blueprint Designer")
  * [Patch 0.7.0.5](/wiki/Patch_0.7.0.5 "Patch 0.7.0.5"): 
    * Fixed deletion of Blueprints not properly propagating from Host to Clients
    * Fixed holograms temporarily staying stuck in the Blueprint designer after being built by Clients
    * Fixed a crash for Clients when using the [Jetpack](/wiki/Jetpack "Jetpack")
  * [Patch 0.7.0.4](/wiki/Patch_0.7.0.4 "Patch 0.7.0.4"): Fixed invisible buildings built from [Blueprints](/wiki/Blueprint "Blueprint") when reconnecting to Dedicated Servers
  * [Patch 0.7.0.3](/wiki/Patch_0.7.0.3 "Patch 0.7.0.3"): Fixed Crash when joining [Multiplayer](/wiki/Multiplayer "Multiplayer") or Dedicated Servers
  * [Patch 0.7.0.1](/wiki/Patch_0.7.0.1 "Patch 0.7.0.1")
    * Fixed a crash for [Multiplayer](/wiki/Multiplayer "Multiplayer") Clients or Dedicated Server Clients when placing a Blueprint that has the [AWESOME Sink](/wiki/AWESOME_Sink "AWESOME Sink")
    * Fixed a crash for [Multiplayer](/wiki/Multiplayer "Multiplayer") Clients or Dedicated Server Clients when loading a blueprint before data is properly synced with host
    * Fixed [Multiplayer](/wiki/Multiplayer "Multiplayer") Clients or Dedicated Server Clients Blueprints showing up in Blueprint selection when those Blueprints don’t exist on Server
  * [Patch 0.7.0.0](/wiki/Patch_0.7.0.0 "Patch 0.7.0.0"): Overhauled Pioneer name tags for [Multiplayer](/wiki/Multiplayer "Multiplayer") Clients or Dedicated Server Clients
  * [Patch 0.6.1.2](/wiki/Patch_0.6.1.2 "Patch 0.6.1.2")
    * Fixed heavy stuttering for [Multiplayer](/wiki/Multiplayer "Multiplayer") Clients and Dedicated Server Clients when getting hit by a projectile
    * Fixed a crash for [Multiplayer](/wiki/Multiplayer "Multiplayer") Clients and Dedicated Server Clients when trying to remove highlights from a Map Marker
    * Fixed a Crash by making it error normally instead of crash
  * [Patch 0.6.1.1](/wiki/Patch_0.6.1.1 "Patch 0.6.1.1")
    * Fixed [Nobelisk Gas](/wiki/Nobelisk_Detonator#Gas-0 "Nobelisk Detonator") clouds not disappearing on Dedicated Server
    * Server should now error out instead of crash when the server is unable to bind to a query port
    * Fixed a server crash when uploading a save file
  * [Patch 0.6.0.15](/wiki/Patch_0.6.0.15 "Patch 0.6.0.15")
    * Fixed Equipment icon in HUD flickering when equipping an item for [Multiplayer](/wiki/Multiplayer "Multiplayer") Clients and Dedicated Server Clients.
    * Fixed Markers and Stamps placed on the [map](/wiki/Map "Map") disappearing when reconnecting to a [Dedicated Server](/wiki/Dedicated_Server "Dedicated Server")
    * Fixed Markers and Stamps not saving properly on Dedicated Server
  * [Patch 0.6.0.14](/wiki/Patch_0.6.0.14 "Patch 0.6.0.14"): 
    * Fixed [pings](/wiki/Ping "Ping") being invisible for other [Multiplayer](/wiki/Multiplayer "Multiplayer") players or Dedicated Server players
    * Fixed “Press RMB To Respawn” still being displayed after a player is revived
  * [Patch 0.6.0.13](/wiki/Patch_0.6.0.13 "Patch 0.6.0.13"): Potential fix for [Crab Hatchers](/wiki/Flying_Crab_Hatcher "Flying Crab Hatcher") displaying incorrectly when joining for [Multiplayer](/wiki/Multiplayer "Multiplayer") Clients and Dedicated servers Clients
  * [Patch 0.6.0.12](/wiki/Patch_0.6.0.12 "Patch 0.6.0.12")
    * Fixed crash related to [Hatchers](/wiki/Flying_Crab_Hatcher "Flying Crab Hatcher") on Dedicated Server
    * Updated visuals for [Multiplayer](/wiki/Multiplayer "Multiplayer") and Dedicated servers offline player name tags
  * [Patch 0.6.0.10](/wiki/Patch_0.6.0.10 "Patch 0.6.0.10")
    * Other Player characters in the world should now show last used user name when they go offline (Not retroactive)
    * Potential fix for Foliage not being interactable sometimes on Dedicated Servers
  * [Patch 0.6.0.5](/wiki/Patch_0.6.0.5 "Patch 0.6.0.5")
    * Fixed [Multiplayer](/wiki/Multiplayer "Multiplayer") Clients and Dedicated servers Clients not being able to place Extractors on Resource Well Satellite Nodes
    * Fixed Resources not being shown for [Multiplayer](/wiki/Multiplayer "Multiplayer") Clients and Dedicated servers Clients when the [Map](/wiki/Map "Map") or Radar Tower was opened
  * [Patch 0.6.0.4](/wiki/Patch_0.6.0.4 "Patch 0.6.0.4")
    * Fixed [Resource Deposits](/wiki/Resource_Node#Deposit "Resource Node") being Invisible/Non-interactable for [Multiplayer](/wiki/Multiplayer "Multiplayer") Clients or Dedicated Server Clients
    * Potential fix for a crash that starts from players experiencing audio crackling and performance degradation on dedicated server in Northern Forest
    * Fixed issue where the Equipment HUD Slot for Consumables wouldn’t update properly on [Multiplayer](/wiki/Multiplayer "Multiplayer") Clients or Dedicated Server Clients
    * Fixed crash reporter not working on Windows
  * [Patch 0.6.0.3](/wiki/Patch_0.6.0.3 "Patch 0.6.0.3")
    * Equipment [HUD](/wiki/HUD "HUD") is now correctly updated for [Multiplayer](/wiki/Multiplayer "Multiplayer") Clients or Dedicated Server Clients
    * Weapon crosshairs are now correctly updated for Multiplayer Clients or Dedicated Server Clients
  * [Patch 0.6.0.2](/wiki/Patch_0.6.0.2 "Patch 0.6.0.2")
    * [Hatcher](/wiki/Flying_Crab_Hatcher "Flying Crab Hatcher") should now show their status properly for for [Multiplayer](/wiki/Multiplayer "Multiplayer") Clients and [Dedicated Servers](/wiki/Dedicated_Servers "Dedicated Servers") Clients
    * Fixed Resources not being shown to [Multiplayer](/wiki/Multiplayer "Multiplayer") Clients or Dedicated Server Clients when opening [Map](/wiki/Map "Map") or [Radar Tower](/wiki/Radar_Tower "Radar Tower")
    * Dedicated server should not crash anymore when it fails to bind to a port
    * Fixed a crash that may happen if the server settings file is corrupted. In this case, the server will use default settings instead
  * [Patch 0.6.0.1](/wiki/Patch_0.6.0.1 "Patch 0.6.0.1")
  * Fixed a crash when [Multiplayer](/wiki/Multiplayer "Multiplayer") Clients and Dedicated Servers Clients would place a second [Truck Station](/wiki/Truck_Station "Truck Station")
  * Fixed the Truck Stations UI not showing up properly for Multiplayer Clients and Dedicated Servers Clients
  * Fixed a debug icon showing up on the Truck Station inventory when accessed for a second time by Multiplayer Clients and Dedicated Servers Clients
  * [Patch 0.5.2.1](/wiki/Patch_0.5.2.1 "Patch 0.5.2.1"): Current Train Station stop should now properly display for clients in [Multiplayer](/wiki/Multiplayer "Multiplayer") Clients or Dedicated Servers Clients
  * [Patch 0.5.1.13](/wiki/Patch_0.5.1.13 "Patch 0.5.1.13"): Fixed Dedicated Server crash reporter not working properly
  * [Patch 0.5.1.12](/wiki/Patch_0.5.1.12 "Patch 0.5.1.12"): Fixed a crash for [Multiplayer](/wiki/Multiplayer "Multiplayer") Clients and Dedicated Server Clients related to vehicle paths
  * [Patch 0.5.1.9](/wiki/Patch_0.5.1.9 "Patch 0.5.1.9")
    * Fixed a crash related to Vehicle Automation for [Multiplayer](/wiki/Multiplayer "Multiplayer") Clients and Dedicated Server Clients
    * Fixed a bug in the Load Vehicle Path UI where the “Used by this vehicle” checkmark was missing for Multiplayer Clients and Dedicated Server Clients
  * [Patch 0.5.1.8](/wiki/Patch_0.5.1.8 "Patch 0.5.1.8"): Undid all the Networking Optimisation changes from the previous build, which accidentally introduced a bunch of issues for Clients on [Multiplayer](/wiki/Multiplayer "Multiplayer") and Dedicated Servers
  * [Patch 0.5.1.7](/wiki/Patch_0.5.1.7 "Patch 0.5.1.7")
    * Fixed [Multiplayer](/wiki/Multiplayer "Multiplayer") and Dedicated servers Clients not being able to cancel the [docking sequence](/wiki/Electric_Locomotive "Electric Locomotive")
    * Network Optimizations that should result in some performance gain CPU side for Clients on [Multiplayer](/wiki/Multiplayer "Multiplayer") and Dedicated servers
    * Network Optimizations that should result in some performance gain on for Clients on Multiplayer and Dedicated servers hosting games with many Smart Splitters built
  * [Patch 0.5.1.6](/wiki/Patch_0.5.1.6 "Patch 0.5.1.6"): 
    * Improved stability of the packet router
    * Improved CPU usage of the packet router
    * Added a startup argument for disabling the packet router: `-DisablePacketRouting`
  * [Patch 0.5.1.4](/wiki/Patch_0.5.1.4 "Patch 0.5.1.4"): Fixed holograms having the proper position for [Multiplayer](/wiki/Multiplayer "Multiplayer") and Dedicated servers Client but the wrong one for Host/Server in some situations
  * [Patch 0.5.1.2](/wiki/Patch_0.5.1.2 "Patch 0.5.1.2"): 
    * Implemented a mechanism that routes all server packets through the query beacon, in effect reducing the number of ports that need to be open/forwarded to 1, simplifying setup.
  * [Patch 0.5.1.1](/wiki/Patch_0.5.1.1 "Patch 0.5.1.1"): 
    * Fixed a bug that made Clients spam poll the server, now we should poll much less
    * Fixed some more issues with the Crash reporter integration
  * [Patch 0.5.0.14](/wiki/Patch_0.5.0.14 "Patch 0.5.0.14"): 
    * Found an issue where threading was forced to be disabled for dedicated servers in some scenarios. Fixed it so now we should actually make use of multiple CPU cores
    * Added tick rate information on the Server Status UI Menu
    * Production Lights for all buildings should now be working again
  * [Patch 0.5.0.13](/wiki/Patch_0.5.0.13 "Patch 0.5.0.13")
    * Added Crash Reporter integration for Dedicated Server for both Windows and Linux. 
      * This is enabled by default, we plan on including a toggle for this in GUI but for the moment, if you want to disable automatically sending crash logs you can do this:
      * Go to `SatisfactoryDedicatedServer\FactoryGame\Saved\Config\WindowsServer\`
      * Open “Engine.ini”
      * Add the following and save changes:


    
    
    [CrashReportClient]
    bImplicitSend=False
    

  * [Patch 0.5.0.12](/wiki/Patch_0.5.0.12 "Patch 0.5.0.12"): Enabled background and hi-prio task sets for servers to match what they are for the game, This should further improve multicore CPU usage
  * [Patch 0.5.0.11](/wiki/Patch_0.5.0.11 "Patch 0.5.0.11"): Servers should now use all available cores (Up to 26 worker threads) on both Windows and Linux
  * [Patch 0.5.0.9](/wiki/Patch_0.5.0.9 "Patch 0.5.0.9"): 
    * Potential fix for a [Multiplayer](/wiki/Multiplayer "Multiplayer") / Dedicated servers crash related to [tireconfig](/wiki/Unreal_Engine "Unreal Engine") deletion
    * Fixed [Nobelisks](/wiki/Nobelisk "Nobelisk") being invisible when first equipping for Clients
    * Fixed a rare crash when accessing the [Train Station](/wiki/Train_Station "Train Station") UI as Client
    * Fixed ammo count issues for Clients
    * Implemented a first revision of the Save Manager in the “Manage Saves” tab under Server Manager
    * Increased the beacon connection timeout to 30 seconds (Previous value was 5 seconds)
    * Actually fixed invisible [Conveyor Belts](/wiki/Conveyor_Belts "Conveyor Belts"), [Conveyor Lifts](/wiki/Conveyor_Lifts "Conveyor Lifts") and [Pipelines](/wiki/Pipelines "Pipelines") sometimes being invisible for [Multiplayer](/wiki/Multiplayer "Multiplayer")/Dedicated Servers Clients (Triple for real!!!)
  * [Patch 0.5.0.8](/wiki/Patch_0.5.0.8 "Patch 0.5.0.8"): 
    * Hopefully fixed remaining [Nobelisk](/wiki/Nobelisk "Nobelisk") issues for [Multiplayer](/wiki/Multiplayer "Multiplayer") / Dedicated Servers Clients (Firing, Explosions, UI Feedback, Responsiveness)
    * Fixed a bug where complex clearance would not be spawned on the server, blocking Clients from building despite holograms being ok with it on server
    * Fixed Self Driving [Trains](/wiki/Train "Train") being slow when a Client was travelling in them
    * Potential fix for invisible [Conveyor Belts](/wiki/Conveyor_Belts "Conveyor Belts"), [Conveyor Lifts](/wiki/Conveyor_Lifts "Conveyor Lifts") and [Pipelines](/wiki/Pipelines "Pipelines") sometimes being invisible for Clients
    * Fixed player has joined messages not showing up for Clients
    * Fixed spelling mistake in the server is offline message
    * Server state is now polled a lot less by the clients (at most 3 times per second) and clients back off gradually if a server does not respond to pings which makes the client behaviour less consistent with DDOS attacks
    * Clients do not store DNS lookup results in the server manager file and instead the DNS lookups are made every time the client starts up which makes the clients work better for servers with Dynamic DNS
  * [Patch 0.5.0.7](/wiki/Patch_0.5.0.7 "Patch 0.5.0.7"): 
    * Fixed a crash on startup on Dual Stack Linux, IPv6 should now work on more recent kernels
    * Fixed a shutdown crash caused by OnlineSubsystemEOS
  * [Patch 0.5.0.6](/wiki/Patch_0.5.0.6 "Patch 0.5.0.6"): 
    * Potentially fixed a crash related to using the [Rebar Gun](/wiki/Rebar_Gun "Rebar Gun") on Dedicated Server
    * Fixed Hologram snapping always using automatic clearance snapping if a [Multiplayer](/wiki/Multiplayer "Multiplayer") / Dedicated Server Client was [building](/wiki/Build_Gun "Build Gun"), it now updates settings between Client and Host/Server
    * Fixed [Nobelisk](/wiki/Nobelisk "Nobelisk")/[Snowballs](/wiki/FICSMAS#Parts "FICSMAS") on Dedicated servers
    * Added IPv6 Support
    * Made FGAbstractServerWidget public for modders
    * UI should now properly display when new connections are established
    * Potentially fixed a crash related to using the Rebar Gun on Dedicated Server
  * [Patch 0.5.0.4](/wiki/Patch_0.5.0.4 "Patch 0.5.0.4")
    * Fixed Client for crash related to not-yet-replicated member
    * Fixed Dedicated Servers crash related to [Vehicles](/wiki/Vehicles "Vehicles") end play
    * Fixed a crash when using [Parachutes](/wiki/Parachute "Parachute") as Client
    * Changed "-GamePort" server parameter to "-Port"
    * Added a “Save Game” server command (`server.SaveGame <saveName>`)
    * Flipped around the Show/Hide Address Toggle Button text in the Add Server popup
  * [Patch 0.5.0.2](/wiki/Patch_0.5.0.2 "Patch 0.5.0.2") _(Released again in[Patch 0.5.0.3](/wiki/Patch_0.5.0.3 "Patch 0.5.0.3"))_: Fixed [Multiplayer](/wiki/Multiplayer "Multiplayer") / Dedicated Servers Clients not being able to save or remove colour presets in the [Customizer](/wiki/Customizer "Customizer")
  * [Patch 0.5.0.0](/wiki/Patch_0.5.0.0 "Patch 0.5.0.0"): Introduced 
    * First iteration of Dedicated Server support (Still Experimental)



## References

  1. ↑ [Reddit - Dedicated Servers have LEVELED UP! - Video Bookmarks](https://www.reddit.com/r/SatisfactoryGame/comments/1bqp8mj/comment/kx4migg/?utm_source=reddit&utm_medium=web2x&context=3)
  2. ↑ [YouTube - Dedicated Servers have LEVELED UP! - General](https://www.youtube.com/watch?v=v8piXNQwcUw&t=162s)


  *[v]: View this template
  *[e]: Edit this template
  *[h]: History of this template
  *[his]: his trivia section
