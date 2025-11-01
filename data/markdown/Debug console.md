# Debug console

The **debug console** in _Satisfactory_ can be used to access debug data (like player coordinates or a list of [radiation](/wiki/Radiation "Radiation") sources) or for changing some options not available in the game's settings, such as disabling the fog or enabling an FPS counter. It cannot be used for cheating (e.g. spawning items), [Advanced Game Settings](/wiki/Advanced_Game_Settings "Advanced Game Settings") and [save editors](/wiki/Online_tools "Online tools") serve that purpose.   
  
The effects of commands are reset once the game is closed to desktop, but persist between sessions (the only exception is the Suicide command, which will remain if the game is saved). 

Config files can be edited in order to persistently apply console commands, see [Settings § Options not available in the settings menu](/wiki/Settings#Options_not_available_in_the_settings_menu "Settings"). 

## Contents

  * 1 Accessing
    * 1.1 Changing the activation key
  * 2 List of commands
    * 2.1 Functional commands
    * 2.2 ShowDebug Parameters
    * 2.3 Non-functional commands
  * 3 Options not available in the settings menu
  * 4 External link
  * 5 History



## Accessing

The debug console can be accessed by [`§`](/wiki/Controls "Controls")(paragraph)/[```](/wiki/Controls "Controls") (backtick)/[`~`](/wiki/Controls "Controls") (tilde) key. This will open the console command line; press it again to open a larger window (at least one command requires a large window in order to be used properly). 

It might be necessary to change the keyboard layout to English - UK on some keyboard layouts, as the console can only be opened if the keyboard layout has at least one of the 3 activation keys ([`§`](/wiki/Controls "Controls"), [```](/wiki/Controls "Controls") or [`~`](/wiki/Controls "Controls")). The activation key will not work if it requires a modifier key like [`⇧ Shift`](/wiki/Controls "Controls"), [`Ctrl`](/wiki/Controls "Controls") or [`Alt`](/wiki/Controls "Controls") to type, it has to be a single key stroke. 

### Changing the activation key

There is a solution that does not require switching the keyboard layout. Navigate to and edit the `%LOCALAPPDATA%\FactoryGame\Saved\Config\Windows\Input.ini` file. Add the following line(s): 
    
    
    [/Script/Engine.InputSettings]
    ConsoleKeys=F6
    

This will allow the debug console to be opened with [`F6`](/wiki/Controls "Controls"). Any other key or character can be, as long as it doesn't require to use a modifying key such as [`Ctrl`](/wiki/Controls "Controls"), [`⇧ Shift`](/wiki/Controls "Controls") or [`Alt`](/wiki/Controls "Controls"), also avoid using any keys that the game already uses by default. 

Changing the activation keys disables the default [`§`](/wiki/Controls "Controls")/[```](/wiki/Controls "Controls")/[`~`](/wiki/Controls "Controls"), but allows those keys to be bound to [controls](/wiki/Controls "Controls") in-game, which isn't possible otherwise. 

If the above method doesn’t work for you an alternate is the free Microsoft Branded “Power Toys” application from the Microsoft AppStore or Website. Select Keyboard Manager. Enable the Keyboard Manager toggle. Under Keys select remap a key. Under select, use the key you want to disable or remap. Under “To Send” set the bottom box to either “Disable” or whichever key you want it remapped to. This is a Windows wide fix not specific to Satisfactory. 

## List of commands

The "window" column is to differentiate between commands that require the large console window to be properly used and commands that do not require it. Since _Satisfactory_ is made in Unreal Engine, many commands from the Unreal Engine itself appear in this list. 

### Functional commands

Command  | Window  | Default  | Use/effect   
---|---|---|---  
space (without pressing enter)  |  |  | Shows a complete list of all commands, some with brief explanations. There are 5705 commands in total as of [Patch 1.0.0.5](/wiki/Patch_1.0.0.5 "Patch 1.0.0.5"), though not all of them are available as a public user. Use Up/Down arrow keys to navigate thru the list Searching the list is automatic. Anything typed in console will be searched for. Space is the global 'wildcard' to list all. (Originally was the question mark) 

  * Green commands: Executable as a public user, alteration possible


  * Purple commands: Executable as administrator _(possibly accessible by commands like "Admin" and/or "AdminLogin"),_ but some have been made accessible for public users, could be host in a multiplayer game
  * Grey commands: Only readable

  
materialFlowAnalysis _recipeName[FString]_ | Large |  | This command can be used to find the items required _per second_ for all craftable items in the game. To use the command, type "materialFlowAnalysis" (not case sensitive) and then type in the item name you wish to find out about (this is case sensitive). The 'name' of the item, or 'FString', shall follow the exact string as indicated in the individual item's Blueprint Path, which can be found in the infobox of each item on its respective page.   
Gamma [number]  | Small  | 2.2  | Changes the gamma (brightness) level.   
Pause  |  | Pauses the game, enter the command again to continue playing.   
r.HDR.EnableHDROutput  | 0  | Set to 1 to enable HDR (High Dynamic Range) for higher contrast and a wider color gamut. Has no effect if HDR is not supported by the display _and_ enabled in the operating system.   
r.Atmosphere [0/1]  | 1  | Activates/deactivates the atmosphere.   
r.Fog [0/1]  | 1  | Activates/deactivates the fog.   
r.ViewDistanceScale  | 1  | Sets the render distance of things like trees/foliage/rocks. Value is multiplicative*   
foliage.LODDistanceScale  | 1  | Controls how are higher quality LOD models being shown further out. It primarily affects foliage and buildings and can have a major impact on performance, but can make the game look better. Set this to higher values to increase the distance (recommended high is 5).   
r.Shadow.DistanceScale  | 1  | Sets the render distance of shadows cast by objects. Value is multiplicative*   
r.ScreenPercentage [percent]  | 100  | Sets internal resolution scale. It can be used together with r.TemporalAA.Upsampling set to 1 to get a "fake" full resolution image achieved with temporal anti-aliasing (TAA). This can improve performance a lot.   
r.TemporalAACurrentFrameWeight [number]  | 0.2  | Range 0-1. Sets the impact of the current internal frame on the final image. Set this to a low value e.g. 0.05 for better anti-aliasing or better upsampling at the cost of more artifacts (especially smearing) in motion. Also, increase r.TemporalAASamples to something larger like 16 when using low values.   
r.TemporalAAFilterSize  | 1  | Sets the spread of the TAA samples. Use values below 1 like 0.25 to sharpen the image (only works if r.TemporalAASamples > 6).   
r.TemporalAASamples [number]  | 8  | Sets the number of samples to use for TAA. Set this to 2 - 5 to reduce jitter.   
r.Tonemapper.Sharpen [number]  | 0  | Sets the amount of a simple sharpen filter.   
r.StaticMeshLODDistanceScale [number]  | 1  | Controls the level of detail (LOD) for static meshes. Set this to 0 to improve graphics but possibly decrease performance, or higher than 1 to make it significantly worse.   
r.LandscapeLODBias [number]  | 0  | Fixes terrain geometry in the far distance. Set this to -2 or -3 to improve graphics but possibly decrease performance.   
Grass.densityscale [number]  | 1  | Sets the grass density. 0 disables it entirely, values between 0 and 1 reduce it, and values over 1 increase it.   
r.streaming.poolsize [number]  | ?  | Specifies the maximum amount of memory, **in megabytes** , that the texture streaming system can use. This is placed in the _Engine.ini_ file in the `[/Script/Engine.RendererSettings]` section.❗This might cause performance issues if values higher than 1000 are used.   
pool.light.count [number]  | ?  | Sets the amount of lights to render.   
pool.light.lightshaft.count [number]  | ?  | Sets the amount of light shafts to render.   
ShowDebug _DebugType[FName]_ |  | Activating this command with any valid parameter will also show the following information in the top left corner of the screen regardless of the command executed (unless otherwise stated): 

  * Player name
  * Coordinates in the world (X, Y, Z)
  * Rotation
  * Instigator
  * Owner
  * Base eye height

Replace `DebugType[FName]` with a parameter from [Console#ShowDebug_Parameters](/wiki/Console#ShowDebug_Parameters "Console")  
Stat FPS  |  | Activates Unreal Engine 4's built-in FPS counter, all command fields are non-case-sensitive. The FPS counter will work in all environments, even on loading screens or the main menu.   
Stat Levels  |  | From the description: "Displays level streaming info".   
Stat Unit  |  | Activating it shows a small readout of various statistics including Frame time (1000/Frame time = FPS), Game time (1000/Game time = UPS), Draw time (unknown), GPU time (unknown), RHIT time (unknown) and whether or not DynRes is supported (use unknown).   
Suicide  |  | Has the same effect as using the Respawn option from the [`Esc`](/wiki/Controls "Controls") in-game menu.   
t.MaxFPS [number]  | 0  | Sets the maximum framerate to any value, other than the options in video settings. 0 makes the framerate unlimited.   
FOV [number]  |  | Sets field of view to the entered value, however, values over 150 can become unstable and glitches will occur. The FOV can be changed by a slider in the game's option, but this console command allows to set it to any value beyond the slider.   
ToggleDebugOverlay [0/1]  | 0  | Displays a window with various debug info.   
SaveWithNewSessionName [name]  |  | Saves the current session under a new session name, separating it in the "Load Game" menu.   
r.AOGlobalDistanceField.MinMeshSDFRadius [number]  | 1  | Temporary fix to make emissive materials (like [Signs](/wiki/Signs "Signs")) in Global Illumination (Lumen) illuminate further. Values up to 20 seem to work in varying degrees.   
r.LumenScene.SurfaceCache.CardTexelDensityScale [number]  | 100  | Temporary fix to increase render distance of emissive Signs. Values up to 3000 seem to work fine. May decrease performance.   
r.DFDistanceScale [number]  | 1  | Higher values increase shadow distance at the cost of FPS. HEAVY FPS impact.   
  
*Multiplicative values means setting it to 2 will render at double the default distance and setting it to 0.5 will render at half of the default. It appears to be limited to a maximum value of 3. Can be FPS heavy if set too high values and can give you more FPS if set to lower values. 

### ShowDebug Parameters

Parameter | Description   
---|---  
AI | Use unknown. Presumably shows information regarding enemies and/or automated vehicles near the player.   
AKAUDIOSOURCES | Shows the number of active audio sources + other information. Execute again to show default information.   
ANIMATION | Use unknown. Presumably shows information regarding what frame of an animation is being played, the name of the animation, etc.   
BONES | Use unknown. Presumably shows information regarding bone connections and their orientation in non-static models.   
CAMERA | Shows extra information about the camera position underneath default information.   
CIRCUITS | Shows information regarding any power networks (circuits) in the world including; the number of circuits, ID(s), and information about the circuits including; components, power produced, the power consumed, and fuse status. Execute again to show default information.   
COLLISION | Unknown. Presumably shows collision information.   
FACTORY | Shows the number of player-built structures (not including vehicles) in order from most to least.   
FACTORYCONNNECTIONS | Use Unknown. Notes: Causes extreme lag, use at own risk. Execute again to show default information.   
FORCEFEEDBACK | Shows information about current force feedback values and what is contributing to that calculation underneath default information.   
INPUT | Shows information about which input method is currently being used (keyboard/mouse) which key is being used, the input value of the input, and the time the input has been executed. It also shows information about the input stack. All of this information is shown underneath the default information.   
NET | Use unknown. Presumably used to show multiplayer connection info.   
NONE | Shows only default information, hiding the rest.   
PHYSICS | Shows information about; Current player velocity components, total player speed in cm/s, total player speed (2D), acceleration experienced by the player, and other physics-related information. This is all shown underneath default information.   
POWER | Use unknown. Note: Causes Lag, use at your own risk.   
RADIATION | Shows information related to the radioactivity subsystem including; Number of radiation sources, emitters and levels of radiation emitted, and player exposure level. Execute again to show default information.   
RADIATIONSPHERES | Presumably shows spheres where radiation would begin to affect the player. Execute again to show default information.   
Reset | Hides all debug information, including default information.   
SIGNIFICANCEMANAGER | Shows information on the significance of sounds currently being played and their volume relative to each other.   
TRACKS | Shows information on the railroad subsystem on tracks, such as track segments and blocks, divided into graphs (graphs are loops or stretches of tracks). Execute again to show default information.   
TRAINCOUPLERS | Does not work.   
TRAINSCHEDULER | Shows train scheduling information. Priority: xxxxxx | Rail [Segment] Number the train has priority for Train: xxxxx | Train Name Dependency Level: x | Currently Unknown RN: xxxx | Rail [Segment] Number Potential Deadlock: [Yes] [No] | Further Detail Required Reservations: x | Further Detail Required Dependencies: x | Further Detail Required   
TRAINSIGNALS | Shows Train Signal and block information, such as what the entry signal is, whether a block is defined by Path or Block signals, reservation requests, what train is in the block etc.   
TRAINS | Shows information about all existing trains (weight, pulling force, braking force, power usage, slave and master etc.). Execute again to show default information.   
VEHICLE | Shows information on the vehicle the player is currently in including speed, steering angle, throttle information, whether or not the brake is on, current gear, engine RPM, drag force being experienced, and physics information about each wheel on the vehicle.   
WEAPON | Use unknown. Presumably shows information regarding held weapons/tools.   
  
### Non-functional commands

The following commands appear in the autocomplete list in the console but have never worked since [Early Access release](/wiki/Patch_0.1 "Patch 0.1"), as they either don't do anything when executed or aren't even recognized by the console when executed. 

  * Fly
  * Ghost
  * GiveItem
  * Cheats
  * Teleport
  * God



## Options not available in the settings menu

It's possible to achieve higher visual fidelity than "Ultra quality" by modifying the game settings file directly. The following changes will have a drastic negative impact on your framerate, but will eliminate rocks and foliage magically appearing a few meters away from you. For a more detailed explanation of these settings and pictures, see this old but still relevant post: [Force good LOD, Draw distance](https://www.reddit.com/r/SatisfactoryGame/comments/f75pxf/useful_console_commands_inside_force_good_lod/)

Two steps to apply these changes (close the game first): 

  1. Open Notepad, then open this file: `%LOCALAPPDATA%\FactoryGame\Saved\Config\Windows\Engine.ini`
  2. Add (or replace if you've already done this) the following to the bottom of the file then save it:


    
    
    [SystemSettings]
    r.TemporalAACurrentFrameWeight=0
    r.TemporalAASamples=32
    r.PostProcessAAQuality=5
    r.ToneMapper.Sharpen=1
    r.ViewDistanceScale=5
    r.Shadow.MinResolution=256
    r.Shadow.DistanceScale=5
    foliage.LODDistanceScale=2
    foliage.DitheredLOD=5
    r.MaxAnisotropy=16
    

You've done the change right if your file looks similar to this when you're done: [picture of modified Engine.ini](https://i.imgur.com/23dw407.png)

## External link

  * [Unreal Engine 5 All Console Variables and Commands](https://forums.unrealengine.com/t/unreal-engine-5-all-console-variables-and-commands/608054)



## History

  * [Patch 0.4.0.0](/wiki/Patch_0.4.0.0 "Patch 0.4.0.0")?: The console no longer needs to be activated using [`Ctrl`](/wiki/Controls "Controls")+[`⇧ Shift`](/wiki/Controls "Controls")+[`L`](/wiki/Controls "Controls")
  * [Patch 0.3.6.7](/wiki/Patch_0.3.6.7 "Patch 0.3.6.7"): Added ToggleDebugOverlay command
  * [Patch 0.3.5.4](/wiki/Patch_0.3.5.4 "Patch 0.3.5.4")?: r.Gamma is replaced with Gamma, Pause is functional again
  * [Patch 0.3](/wiki/Patch_0.3 "Patch 0.3")?: r.Gamma and Pause commands no longer work



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
Technical| [Console release](/wiki/Console_release "Console release") • Debug console • [Launch arguments](/wiki/Launch_arguments "Launch arguments") • [Save files](/wiki/Save_files "Save files") • [System requirements](/wiki/System_requirements "System requirements") • [Units](/wiki/Units "Units") • [Unreal Engine](/wiki/Unreal_Engine "Unreal Engine")  
Guides and tutorials| | Basics| [Walkthrough/How to play](/wiki/Tutorial:How_to_play "Tutorial:How to play") • [New Pioneer Guide](/wiki/Tutorial:New_Pioneer_Guide "Tutorial:New Pioneer Guide") • [Production line basics](/wiki/Tutorial:Production_line "Tutorial:Production line") • [Advanced production line tips](/wiki/Tutorial:Production_line_design_tips "Tutorial:Production line design tips") • [Picking an alternate recipe](/wiki/Tutorial:Picking_an_alternate_recipe "Tutorial:Picking an alternate recipe") • [Independency](/wiki/Tutorial:Independency "Tutorial:Independency") • [Aluminum Ingot production](/wiki/Tutorial:Setting_up_Aluminum_Ingot_production "Tutorial:Setting up Aluminum Ingot production")  
---|---  
Logistics| [Manifold](/wiki/Manifold "Manifold") • [Balancer](/wiki/Balancer "Balancer") • [Pipeline manifold](/wiki/Pipeline_manifold "Pipeline manifold") • [Prime Splitter Arrays](/wiki/Tutorial:Prime_splitter_arrays "Tutorial:Prime splitter arrays") • [Trains](/wiki/Tutorial:Trains "Tutorial:Trains") • [Train throughput](/wiki/Tutorial:Train_throughput "Tutorial:Train throughput")  
Dedicated servers| [Dedicated servers](/wiki/Dedicated_servers "Dedicated servers") • [Running as a Service](/wiki/Dedicated_servers/Running_as_a_Service "Dedicated servers/Running as a Service") • [Configuration files](/wiki/Dedicated_servers/Configuration_files "Dedicated servers/Configuration files") • [Automatic updates](/wiki/Dedicated_servers/Automatic_updates "Dedicated servers/Automatic updates") • [HTTPS API](/wiki/Dedicated_servers/HTTPS_API "Dedicated servers/HTTPS API") • [Lightweight Query API](/wiki/Dedicated_servers/Lightweight_Query_API "Dedicated servers/Lightweight Query API")  
Other| [Hypertube cannon](/wiki/Tutorial:Hypertube_cannon "Tutorial:Hypertube cannon") • [Hypertube brake](/wiki/Tutorial:Hypertube_brake "Tutorial:Hypertube brake") • [Steam Deck & Controller setup](/wiki/Tutorial:Controller_setup "Tutorial:Controller setup") • [Extracting UI icons](/wiki/Tutorial:Extracting_UI_icons "Tutorial:Extracting UI icons")
  *[v]: View this template
  *[e]: Edit this template
  *[h]: History of this template
  *[his]: his trivia section
