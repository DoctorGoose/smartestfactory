# Launch arguments

There are several **launch arguments** that alter the behavior of the game when used. Launch arguments have to be entered into the desktop shortcut address, command line, Steam launch options, or Epic Games additional command-line arguments field. 

## Contents

  * 1 Setting launch arguments
    * 1.1 Steam
    * 1.2 Epic Games
    * 1.3 Shortcut
    * 1.4 Command line
  * 2 List of known launch arguments
  * 3 References



## Setting launch arguments

Wherever launch arguments are entered, **they have to be separated with a space** and must include the dash "-". 

### Steam

[](/wiki/File:Steam_launch_argument_menu.png)

[](/wiki/File:Steam_launch_argument_menu.png "Enlarge")

The properties menu in Steam, with `-NoMultiplayer` as argument.

  1. Open your Steam library
  2. Right click the game's title and select Properties
  3. In the General tab, you'll find a "Launch options" section
  4. Enter the launch options (see below) you wish to apply into the Launch options field at the bottom
  5. Close the game's Properties window and launch the game



### Epic Games

[](/wiki/File:Epic_Games_launch_argument_menu.png)

[](/wiki/File:Epic_Games_launch_argument_menu.png "Enlarge")

The manage menu in the Epic Games client, from the first method, with `-NoMultiplayer` as argument.

Method 1: 

  1. In the Epic Games client, open the library and search for Satisfactory
  2. Click the three dots [...] next to the game title or at the right side, depending on the library view
  3. Select Manage in the menu
  4. Find and check the "Additional Command Line Arguments" option
  5. Add the required launch arguments (see below) you wish to apply into the box
  6. Close Settings and launch the game



Method 2: 

  1. In the Epic Games client, click on the profile icon in the top right, then access Settings in the menu
  2. Scroll down until you find a list of all games you currently have installed
  3. Select the game.
  4. Check the "Additional Command Line Arguments" option
  5. Add the required launch arguments (see below) you wish to apply into the box
  6. Close Settings and launch the game



### Shortcut

This method works for both launchers, and allows creating different sets of launch arguments 

  1. Navigate to the game's install directory (default `C:\Program Files\Steam\steamapps\common\Satisfactory` or `C:\Program Files\Epic Games\Satisfactory` (or `SatisfactoryExperimental`))
  2. Right-click the game executable and select "Create shortcut"
  3. Right-click the shortcut and select "Properties"
  4. Append launch arguments after the path in the Target field



### Command line

This method works for both launchers, and allows a set of launch parameters to be used only once, without having to remove them later 

  1. Navigate to the game's install directory (default `C:\Program Files\Steam\steamapps\common\Satisfactory` or `C:\Program Files\Epic Games\Satisfactory` (or `SatisfactoryExperimental`))
  2. Open any terminal (CMD, PowerShell, Windows Terminal)
  3. Drag the game's executable over to the terminal
  4. Append launch arguments after the path



## List of known launch arguments

Argument  | Description   
---|---  
Graphics   
`-d3d11` `-DX11` | Forces DirectX 11 to be used (note that DirectX 11 is deprecated as of Update 8)[1][2][3]  
`-d3d12` `-DX12` | Forces DirectX 12 to be used[1][4]  
`-vulkan` | Forces Vulkan to be used[1]  
`-fullscreen` | Forces the engine to start in fullscreen mode   
`-windowed` | Forces the engine to start in windowed mode  
Use in conjunction with `-ResX=HORIZONTAL_RES` and `-ResY=VERTICAL_RES`  
`-ResX=HORIZONTAL_RES`  
`-ResY=VERTICAL_RES` | Specify the horizontal (X) and vertical (Y) resolution size for a client. Example: `-ResX=1920 -ResY=1080`  
Use in conjunction with `-windowed`  
`-w #` | Forces the engine to start with resolution set to # (width)  
The width value will determine the height value automatically   
Connectivity   
`-NoMultiplayer` | Disables all multiplayer related connections in-game by preventing the game to connect to EOS   
`-NoSteamClient` | Prevents Steam from starting when playing on Epic Games   
`-EpicPortal` | Internally used for logging in; when set manually, causes the game to skip login to EOS (akin to `-NoMultiplayer`)   
Gameplay   
`-DisableSeasonalEvents` | Disables seasonal events, such as [FICSMAS](/wiki/FICSMAS "FICSMAS")[5]  
Other   
`-fullcrashdump` | Generates additional debugging information for the developers when the game crashes and logs are sent through the crash reporter   
`-epicapp` | Used when launching the game from Epic Games; the stable branch is set to Crab, experimental to CrabTest   
`-epicenv` | Used when launching the game from Epic Games   
`-epicusername` | Used when launching the game from Epic Games, set to the currently logged in user   
`-epicuserid` | Used when launching the game from Epic Games, set to the currently logged in Epic Account ID   
`-epiclocale` | Used when launching the game from Epic Games, set to the locale of the launcher   
`-NO_EOS_OVERLAY` | Used when launching the game from Steam, prevents EOS overlay from appearing[6]  
`-USEALLAVAILABLECORES` | Forces the game to use all CPU cores   
`-nothreadtimeout` | Disables the max waiting time of 120 seconds for the rendering threads   
`-nosplash` | Disables the splash image on launch[7]  
`-noaudio` | Disable audio upon game launch  
(used to fix an audio bug, see [Patch 0.8.3.0 § Known issues](/wiki/Patch_0.8.3.0#Known_issues "Patch 0.8.3.0"))   
`-nosound`  
  
Other launch arguments can be found in the [Unreal Engine 5 Documentation - Command-Line Arguments](https://docs.unrealengine.com/5.2/en-US/command-line-arguments-in-unreal-engine/), although they may not all be functional. 

## References

  1. ↑ 1.0 1.1 1.2 [NEW Features we've added to Update 5 since release](https://www.youtube.com/watch?v=cn3e-m4a-hU)
  2. ↑ [Unreal Engine 5.2 - Hardware and Software Specifications](https://docs.unrealengine.com/5.2/en-US/hardware-and-software-specifications-for-unreal-engine/)
  3. ↑ [YouTube - Update 8 Bugs and Performance Troubleshooting - Checklist last resort: Force DirectX 11](https://www.youtube.com/watch?v=6H79BTIrlbc&t=1000s)
  4. ↑ <https://www.epicgames.com/unrealtournament/forums/unreal-tournament-discussion/ut-game-general-discussion/14221-starting-in-dx12-mode>
  5. ↑ <https://store.steampowered.com/news/app/526870/view/5916039151451470744>
  6. ↑ <https://steamdb.info/app/526870/config/>
  7. ↑ <https://www.pcgamingwiki.com/wiki/Satisfactory#Skip_splash_screen>



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
Technical| [Console release](/wiki/Console_release "Console release") • [Debug console](/wiki/Debug_console "Debug console") • Launch arguments • [Save files](/wiki/Save_files "Save files") • [System requirements](/wiki/System_requirements "System requirements") • [Units](/wiki/Units "Units") • [Unreal Engine](/wiki/Unreal_Engine "Unreal Engine")  
Guides and tutorials| | Basics| [Walkthrough/How to play](/wiki/Tutorial:How_to_play "Tutorial:How to play") • [New Pioneer Guide](/wiki/Tutorial:New_Pioneer_Guide "Tutorial:New Pioneer Guide") • [Production line basics](/wiki/Tutorial:Production_line "Tutorial:Production line") • [Advanced production line tips](/wiki/Tutorial:Production_line_design_tips "Tutorial:Production line design tips") • [Picking an alternate recipe](/wiki/Tutorial:Picking_an_alternate_recipe "Tutorial:Picking an alternate recipe") • [Independency](/wiki/Tutorial:Independency "Tutorial:Independency") • [Aluminum Ingot production](/wiki/Tutorial:Setting_up_Aluminum_Ingot_production "Tutorial:Setting up Aluminum Ingot production")  
---|---  
Logistics| [Manifold](/wiki/Manifold "Manifold") • [Balancer](/wiki/Balancer "Balancer") • [Pipeline manifold](/wiki/Pipeline_manifold "Pipeline manifold") • [Prime Splitter Arrays](/wiki/Tutorial:Prime_splitter_arrays "Tutorial:Prime splitter arrays") • [Trains](/wiki/Tutorial:Trains "Tutorial:Trains") • [Train throughput](/wiki/Tutorial:Train_throughput "Tutorial:Train throughput")  
Dedicated servers| [Dedicated servers](/wiki/Dedicated_servers "Dedicated servers") • [Running as a Service](/wiki/Dedicated_servers/Running_as_a_Service "Dedicated servers/Running as a Service") • [Configuration files](/wiki/Dedicated_servers/Configuration_files "Dedicated servers/Configuration files") • [Automatic updates](/wiki/Dedicated_servers/Automatic_updates "Dedicated servers/Automatic updates") • [HTTPS API](/wiki/Dedicated_servers/HTTPS_API "Dedicated servers/HTTPS API") • [Lightweight Query API](/wiki/Dedicated_servers/Lightweight_Query_API "Dedicated servers/Lightweight Query API")  
Other| [Hypertube cannon](/wiki/Tutorial:Hypertube_cannon "Tutorial:Hypertube cannon") • [Hypertube brake](/wiki/Tutorial:Hypertube_brake "Tutorial:Hypertube brake") • [Steam Deck & Controller setup](/wiki/Tutorial:Controller_setup "Tutorial:Controller setup") • [Extracting UI icons](/wiki/Tutorial:Extracting_UI_icons "Tutorial:Extracting UI icons")
  *[v]: View this template
  *[e]: Edit this template
  *[h]: History of this template
  *[his]: his trivia section
