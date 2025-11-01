# Multiplayer

[](/wiki/File:Clapping_Engineers_E3.png)  
  
[](/wiki/File:Clapping_Engineers_E3.png "Enlarge")

Four players in a multiplayer session.

_Satisfactory_ can be played in **multiplayer** , with up to four players officially supported, but with no hard player-limit see below.[1] The game is co-op only and there will be no PvP elements, although pioneers can damage each other.[2] This means that [HUB](/wiki/HUB "HUB"), [MAM](/wiki/MAM "MAM") and [Space Elevator](/wiki/Space_Elevator "Space Elevator") progress as well as [AWESOME Shop](/wiki/AWESOME_Shop "AWESOME Shop") unlocks are shared among all players. 

Cross-platform multiplayer is available across Steam and Epic Games. 

## Contents

  * 1 Hosting a session
    * 1.1 Session privacy
    * 1.2 Network configuration
    * 1.3 Sessions with more than 4 players
    * 1.4 Dedicated servers
  * 2 Joining a session
    * 2.1 Join Game menu
    * 2.2 Session ID
  * 3 Other options
    * 3.1 Troubleshooting tips
      * 3.1.1 LogMeIn Hamachi VPN
      * 3.1.2 pfSense Firewall/Router
    * 3.2 Performance improvements
    * 3.3 Temporary lag solution
      * 3.3.1 Engine.ini
      * 3.3.2 Game.ini
      * 3.3.3 Scalability.ini
  * 4 FICSIT checkmark
  * 5 Trivia
  * 6 History
  * 7 References



## Hosting a session

Currently there are 2 ways to play multiplayer. A player can host a session or a [dedicated server](/wiki/Dedicated_server "Dedicated server") can be used. 

To start a player-hosted multiplayer session, the host has to start an online session (a normal session like when playing in single-player, as long as the host has internet access and authentication servers are working normally) and then allow other players to join, or to invite those players (see sections below). 

### Session privacy

The following session privacy settings are available: 

  * Friends Only - Allows anyone in the host's friend list to join the hosted session from the Join Game menu without invitation. This also allows Session ID to be used, regardless of friend list status.
  * Private - Clients can only join the hosted session if invited using in-game invites. Attempting to join the session via Session ID will result in it not being found.



There are no plans for a "Public" option, due to griefing concerns.[1]

### Network configuration

It might be necessary to configure the network in some scenarios, notably on NAT: Strict, which disallows hosting sessions and allows joining sessions only on NAT: Open. Should both the host and client/s have NAT: Moderate or Open, joining sessions should be normally possible. 

The game uses the following ports: 

  * 5222 TCP[3]
  * 6666 TCP & UDP[4]
  * 7777-7827 UDP[5]



Additionally, ensure Windows Firewall rules weren't refused when asked for permission. 

### Sessions with more than 4 players

For more than four players to be able to play in one session simultaneously, the game's config has to be edited. 

The host has to navigate to `%LOCALAPPDATA%\FactoryGame\Saved\Config\Windows\Game.ini`, and add the following lines to the end of that file: 
    
    
     [/Script/Engine.GameSession]
     MaxPlayers=X
    

where X corresponds to the desired maximum amount of players. Up to 127 players are theoretically possible, but not practically. 

### Dedicated servers

_Main article:_[Dedicated servers](/wiki/Dedicated_servers "Dedicated servers")

Dedicated servers are available on Windows and Linux. See the linked page for details. 

## Joining a session

### Join Game menu

Players can join online sessions of players in their friend list from the Join Game menu. As mentioned above, an invitation may or may not be required based on the session privacy setting. It is easy to join players on the same platform this way, to crossplay, Steam players must have linked their Epic account upon prompted. 

### Session ID

Every online session has a set Session ID. Anyone who has access to this ID can join the session, as long as its privacy is set to Friends Only (despite the name, neither user does actually have to be in each other's friend list on either Epic or Steam). 

This ID is unique to each session and is reset once the game is quit to the main menu or entirely. 

The Session ID can be found by doing the following: 

  * Press [`Esc`](/wiki/Controls "Controls").
  * In the menu, click on 'Manage Session', then click on 'Session Settings'.
  * Here, the session ID can be edited or copied to the clipboard.



The host of the session can then share this Session ID for both Epic and Steam players to be able to join the session. 

## Other options

### Troubleshooting tips

The [Official Discord server](https://discord.com/invite/satisfactory) lists the following multiplayer troubleshooting tips: 

  * Have the host and all clients choose `Network Quality: Ultra` in the options.
  * Make sure you're both using the same version (Release Version or Experimental Version) and version number (displayed in launcher and in-game).
  * Make sure you've all set your computer to the correct time zone as this can cause connectivity issues (for some reason).
  * Try playing solo, to make sure it's not an issue with the save file.
  * Send save file to friend, see if they can load up the game when you join.
  * Check NAT type, cannot be Strict.
  * Consider open/forwarding ports 7777-7827 UDP (firewall and on router)
  * Add the binary in `FactoryGame\Binaries\Win64` to your firewall/anti-virus/windows defender.



#### LogMeIn Hamachi VPN

  * Download [Hamachi](https://vpn.net) and try play through using VPN.
  * Download Hamachi and set router to “DMZ”. To do so you can follow these steps: 
    * Set connection in router to "DMZ" (at your own risk; please be careful)
    * Connect through Hamachi
    * Remove DMZ in router again
    * Close Hamachi
    * Let friend join game again.
    * _(The game may still show NAT 'Strict' but is likely to pose no problems.)_



#### pfSense Firewall/Router

if you are using a [pfSense Firewall/Router](https://www.pfsense.org) you need to change your NAT type to **Hybrid** or **Manual** and add a **outbound mapping** for your computers IP. This will fix the strict NAT issue by itself no port forwarding or anything else needed. 

  * [pfSense Firewall/Router Setup - NAT Outbound Mode](https://prnt.sc/pfjyi5)
  * [pfSense Firewall/Router Setup - Advanced Outbound Entry / Translation](https://prnt.sc/pfjz3b)



### Performance improvements

  * If experiencing high latency, try unchecking `Send Gameplay Data` in the options.



### Temporary lag solution

_Please read this section thoroughly to avoid improperly editing the config files.  
This section may not be applicable for dedicated servers._

There is a way to decrease rubber-banding at the cost of increasing bandwidth by adding the following lines to the game's config files[6] found in `%LOCALAPPDATA%\FactoryGame\Saved\Config\Windows\`. 

Before adding the lines to the config files, ensure they aren't already in place but with different values if so, replace them instead of having duplicates. 

By default, the game's maximum bandwidth appears to be throttled at 64 KB/s. By editing the config files, this limit is increased to 800 Mbit/s.  
At lower-end machines or internet connections, use `480000` everywhere there is `104857600`, this sets the limit to 480 KB/s or ~3.66 Mbit/s. 

This has to be done by all players (both the host and client/s) to have an effect. The increased bandwidth can be even five times as much as it was before, therefore a stable internet connection is required. 

#### Engine.ini

This file should be set as 'read only' to prevent the game from overwriting it. 
    
    
     [/Script/Engine.Player]
     ConfiguredInternetSpeed=104857600
     ConfiguredLanSpeed=104857600
     
     [/Script/OnlineSubsystemUtils.IpNetDriver]
     MaxClientRate=104857600
     MaxInternetClientRate=104857600
     
     [/Script/SocketSubsystemEpic.EpicNetDriver]
     MaxClientRate=104857600
     MaxInternetClientRate=104857600
    

#### Game.ini

This file should be set as 'read only' to prevent the game from overwriting it. 
    
    
     [/Script/Engine.GameNetworkManager]
     TotalNetBandwidth=104857600
     MaxDynamicBandwidth=104857600
     MinDynamicBandwidth=10485760
    

Note: If increasing the bandwitdh to 480 kbit/s, set MinDynamicBandwidth to `200000`

#### Scalability.ini

This file will be initially blank and has to be set as 'read only' to prevent the game from overwriting it. 
    
    
     [NetworkQuality@3]
     TotalNetBandwidth=104857600
     MaxDynamicBandwidth=104857600
     MinDynamicBandwidth=10485760
    

Note: If increasing the bandwitdh to 480 kbit/s, set MinDynamicBandwidth to `200000`

## FICSIT checkmark

[](/wiki/File:FICSIT_Checkmark_Example.png)

[](/wiki/File:FICSIT_Checkmark_Example.png "Enlarge")

Update 8 - Example use of FICSIT Checkmark purchased in Awesome Shop only used in Multiplayer Sessions.

For use only in Multiplayer Sessions, the FICSIT Checkmark[7][8][9] can be purchased in the [AWESOME SHOP - Pioneering Awards](/wiki/AWESOME_Shop#FICSIT_Specials "AWESOME Shop") for 8 [](/wiki/FICSIT_Coupon "FICSIT Coupon") [FICSIT Coupons](/wiki/FICSIT_Coupon "FICSIT Coupon"). It is a single-time purchase that adds a yellow checkmark icon next to the player's rendered username (see example photo). 

## Trivia

  * A total of 128 session participants is currently possible as a signed byte is used to track sessions, but [Snutt](/wiki/Snutt "Snutt") had remarked that switching to an unsigned byte would enable up to 255 participants.[_[citation needed](/wiki/Category:Citation_needed "Category:Citation needed")_]
  * Initially the FICSIT Checkmark was thought to be a April Fools Day joke given the release date of the announcement video[7] on April 1, 2023.



## History

_Due to the extensive length of multiplayer history, it was[moved to a separate page](/wiki/Multiplayer/History "Multiplayer/History")._

## References

  1. ↑ 1.0 1.1 [YouTube - Q&A #2: Satisfactory Multiplayer, mods, lizard doggo plushies, and more!](https://www.youtube.com/watch?v=W1E6EWrAsII&t=258)
  2. ↑ [TechRaptor - Satisfactory Interview - Oscar Jilsén, Orbital Elevators, And The Nitty Gritty](https://techraptor.net/content/satisfactory-interview-oscar-jilsen)
  3. ↑ [Unreal Engine Docs - Tools & Firewall Exceptions](https://dev.epicgames.com/community/learning/courses/qEl/unreal-engine-technical-guide-to-linear-content-creation-pipeline-development/7x29/unreal-engine-tools-firewall-exceptions#:~:text=5062%20\(TCP/UDP\)%2C-,5222%20\(TCP\),-%2C%206250%20\(TCP/UDP) [Web Archive (2023-06-16) - Unreal Engine Docs - Tools & Firewall Exceptions](https://web.archive.org/web/20230615142617/https://dev.epicgames.com/community/learning/courses/qEl/unreal-engine-technical-guide-to-linear-content-creation-pipeline-development/7x29/unreal-engine-tools-firewall-exceptions#:~:text=5062%20\(TCP/UDP\)%2C-,5222%20\(TCP\),-%2C%206250%20\(TCP/UDP)
  4. ↑ [Unreal Engine Docs - Tools & Firewall Exceptions](https://dev.epicgames.com/community/learning/courses/qEl/unreal-engine-technical-guide-to-linear-content-creation-pipeline-development/7x29/unreal-engine-tools-firewall-exceptions#:~:text=230.0.0.1%3A6666%20must,6666%20by%20default.) [Web Archive (2023-06-15) - Unreal Engine Docs - Tools & Firewall Exceptions](https://web.archive.org/web/20230615142617/https://dev.epicgames.com/community/learning/courses/qEl/unreal-engine-technical-guide-to-linear-content-creation-pipeline-development/7x29/unreal-engine-tools-firewall-exceptions#:~:text=230.0.0.1%3A6666%20must,6666%20by%20default.)
  5. ↑ [Discord - #multiplayer-troubleshooting channel - Message of Snutt](https://discord.com/channels/370472939054956546/588704774086721536/1138047117949157396)
  6. ↑ [Satisfactory Q&A - Temporary Multiplayer Lag Solution - At Own Risk (written before Dedicated Servers were released)](https://questions.satisfactorygame.com/post/5f4245f06f3c82fe950bc3f8)
  7. ↑ 7.0 7.1 [YouTube - This will Innovate Your Satisfactory Experience](https://www.youtube.com/watch?v=9GjKn5KyAd0)
  8. ↑ [YouTube - May 9th, 2023 Livestream - Q&A: FICSIT Checkmark, when?](https://www.youtube.com/watch?v=IQhhHHeyfRI)
  9. ↑ [Reddit - FICSIT Checkmark now in the AWESOME shop?](https://www.reddit.com/r/SatisfactoryGame/comments/194od74/ficsit_checkmark_now_in_the_awesome_shop/)



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
Gameplay| [Controls](/wiki/Controls "Controls") • [Settings](/wiki/Settings "Settings") • [Future content](/wiki/Future_content "Future content") • [Old unreleased content](/wiki/Old_unreleased_content "Old unreleased content") • [Online tools](/wiki/Online_tools "Online tools") • [Community resources](/wiki/Community_resources "Community resources") • [Advanced Game Settings](/wiki/Advanced_Game_Settings "Advanced Game Settings") • [Acronyms](/wiki/Acronyms "Acronyms") • [Achievements](/wiki/Achievements "Achievements") • [Easter eggs](/wiki/Easter_eggs "Easter eggs") • [Game menus](/wiki/Game_menus "Game menus") • [Indicator Light](/wiki/Indicator_Light "Indicator Light") • Multiplayer • [Music](/wiki/Music "Music")  
Technical| [Console release](/wiki/Console_release "Console release") • [Debug console](/wiki/Debug_console "Debug console") • [Launch arguments](/wiki/Launch_arguments "Launch arguments") • [Save files](/wiki/Save_files "Save files") • [System requirements](/wiki/System_requirements "System requirements") • [Units](/wiki/Units "Units") • [Unreal Engine](/wiki/Unreal_Engine "Unreal Engine")  
Guides and tutorials| | Basics| [Walkthrough/How to play](/wiki/Tutorial:How_to_play "Tutorial:How to play") • [New Pioneer Guide](/wiki/Tutorial:New_Pioneer_Guide "Tutorial:New Pioneer Guide") • [Production line basics](/wiki/Tutorial:Production_line "Tutorial:Production line") • [Advanced production line tips](/wiki/Tutorial:Production_line_design_tips "Tutorial:Production line design tips") • [Picking an alternate recipe](/wiki/Tutorial:Picking_an_alternate_recipe "Tutorial:Picking an alternate recipe") • [Independency](/wiki/Tutorial:Independency "Tutorial:Independency") • [Aluminum Ingot production](/wiki/Tutorial:Setting_up_Aluminum_Ingot_production "Tutorial:Setting up Aluminum Ingot production")  
---|---  
Logistics| [Manifold](/wiki/Manifold "Manifold") • [Balancer](/wiki/Balancer "Balancer") • [Pipeline manifold](/wiki/Pipeline_manifold "Pipeline manifold") • [Prime Splitter Arrays](/wiki/Tutorial:Prime_splitter_arrays "Tutorial:Prime splitter arrays") • [Trains](/wiki/Tutorial:Trains "Tutorial:Trains") • [Train throughput](/wiki/Tutorial:Train_throughput "Tutorial:Train throughput")  
Dedicated servers| [Dedicated servers](/wiki/Dedicated_servers "Dedicated servers") • [Running as a Service](/wiki/Dedicated_servers/Running_as_a_Service "Dedicated servers/Running as a Service") • [Configuration files](/wiki/Dedicated_servers/Configuration_files "Dedicated servers/Configuration files") • [Automatic updates](/wiki/Dedicated_servers/Automatic_updates "Dedicated servers/Automatic updates") • [HTTPS API](/wiki/Dedicated_servers/HTTPS_API "Dedicated servers/HTTPS API") • [Lightweight Query API](/wiki/Dedicated_servers/Lightweight_Query_API "Dedicated servers/Lightweight Query API")  
Other| [Hypertube cannon](/wiki/Tutorial:Hypertube_cannon "Tutorial:Hypertube cannon") • [Hypertube brake](/wiki/Tutorial:Hypertube_brake "Tutorial:Hypertube brake") • [Steam Deck & Controller setup](/wiki/Tutorial:Controller_setup "Tutorial:Controller setup") • [Extracting UI icons](/wiki/Tutorial:Extracting_UI_icons "Tutorial:Extracting UI icons")
  *[v]: View this template
  *[e]: Edit this template
  *[h]: History of this template
  *[his]: his trivia section
