# Community resources

There is a number of **resource files** included with every public build of _Satisfactory_ to simplify the development of [community-made tools and mods](/wiki/Online_tools "Online tools"). 

## Contents

  * 1 File location
  * 2 Docs.json
    * 2.1 History
  * 3 Header files
    * 3.1 PDB files
  * 4 Dedicated Server API Docs



## File location

These files are located in at the game's install location (not in the save file location), by default: 

  * Steam: `C:\Program Files\Steam\steamapps\common\Satisfactory\CommunityResources`
  * Epic Games: `C:\Program Files\Epic Games\SatisfactoryEarlyAccess\CommunityResources`



## Docs.json

The `Docs.json` file is a data dump of class descriptors in the game. It contains information about _Satisfactory_ 's [items](/wiki/Items "Items"), [equipment](/wiki/Equipment "Equipment"), [fluids](/wiki/Fluids "Fluids"), [buildings](/wiki/Buildings "Buildings"), [recipes](/wiki/Recipes "Recipes") and schematics (unlocks). 

The file itself is readable in any text editor, but primarily intended to be machine-readable. It allows to easily develop tools by the player community. The wiki itself relies on Docs.json as well to generate recipe tables and infoboxes, among other features. 

While a large amount of data is contained in the file, it does not cover the game in its entirety. For example, any data about [creatures](/wiki/Creatures "Creatures"), the location of [Resource Nodes](/wiki/Resource_Node "Resource Node"), [Crash Sites](/wiki/Crash_Site "Crash Site"), collectibles, etc. is not included. 

Docs.json does not come with any explicit license. 

### History

The first version of the Docs.json file was shared by developer Markus Rannare in the now defunct Closed Alpha Discord server on January 20, 2019. The file contained a lot of information on dropped, prototype and (at the time) unreleased features. Once players noticed, it was quickly removed and replaced with a more sanitized version which had that information removed. The file can be downloaded [here](https://drive.google.com/file/d/1Ehni2mz0rrZLO-V-zNJfYKVMZLm0hc3r/view?usp=sharing). 

The first few versions of the file were manually generated and distributed with the game, although subsequent versions of the file are automatically generated as the game is compiled and included with the distribution and updates of the game. 

## Header files

Header files contain information about how the game's code is structured and some developer comments about its purpose. The information has little practical use for typical users. However, they drastically improve the quality of information and available to [mod developers](https://docs.ficsit.app) and help them modify existing game behavior. 

### PDB files

The Program Debug Database (PDB) files have information that enables crash logs to contain useful information for both game developers and mod developers, and enable mod developers to attach debugging tools. 

## Dedicated Server API Docs

The release of 1.0 adds and documents two APIs: the [HTTPS API](/wiki/Dedicated_servers/HTTPS_API "Dedicated servers/HTTPS API") and the [Lightweight Query API](/wiki/Dedicated_servers/Lightweight_Query_API "Dedicated servers/Lightweight Query API")

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
Gameplay| [Controls](/wiki/Controls "Controls") • [Settings](/wiki/Settings "Settings") • [Future content](/wiki/Future_content "Future content") • [Old unreleased content](/wiki/Old_unreleased_content "Old unreleased content") • [Online tools](/wiki/Online_tools "Online tools") • Community resources • [Advanced Game Settings](/wiki/Advanced_Game_Settings "Advanced Game Settings") • [Acronyms](/wiki/Acronyms "Acronyms") • [Achievements](/wiki/Achievements "Achievements") • [Easter eggs](/wiki/Easter_eggs "Easter eggs") • [Game menus](/wiki/Game_menus "Game menus") • [Indicator Light](/wiki/Indicator_Light "Indicator Light") • [Multiplayer](/wiki/Multiplayer "Multiplayer") • [Music](/wiki/Music "Music")  
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
