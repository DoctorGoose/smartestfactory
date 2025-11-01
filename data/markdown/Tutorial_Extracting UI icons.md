# Tutorial:Extracting UI icons

This page walks through the steps of **extracting UI icons** for use on the wiki and related tools from _Satisfactory_ 's source `.pak` file. 

## Contents

  * 1 FModel (after 0.8.0.0)
  * 2 UE viewer (before 0.8.0.0)
    * 2.1 Downloading and setting up UE viewer
    * 2.2 Exporting the icons
      * 2.2.1 Method A: Individual icons
      * 2.2.2 Method B: Multiple icons in a specific category
    * 2.3 Locating the exported icons
  * 3 Copyright
  * 4 See also



## FModel (after 0.8.0.0)

Instructions for setting up FModel can be found on the [ficsit.app modding portal](https://docs.ficsit.app/satisfactory-modding/latest/Development/ExtractGameFiles.html#FModel). 

## UE viewer (before 0.8.0.0)

### Downloading and setting up UE viewer

Download UE viewer [here](https://www.gildor.org/downloads). 

Once downloaded, extract the `.zip` folder. Inside, there's an executable called `umodel.exe`. Launch it and wait until the main window appears. 

Do not change any settings besides the game files path. Navigate this to your Epic/Steam games folder and choose either `SatisfactoryEarlyAccess` or `SatisfactoryExperimental`(choose the main folder, not any contents inside). 

When exporting for the first time, a popup will ask for the version. The UE version has changed during development: 

First patch | Last patch | UE version   
---|---|---  
[0.1](/wiki/Patch_0.1 "Patch 0.1") | [0.2.1.18](/wiki/Patch_0.2.1.18 "Patch 0.2.1.18") | 4.20   
[0.2.1.19](/wiki/Patch_0.2.1.19 "Patch 0.2.1.19") | [0.3.7.3](/wiki/Patch_0.3.7.3 "Patch 0.3.7.3") | 4.22   
[0.3.8.0](/wiki/Patch_0.3.8.0 "Patch 0.3.8.0") | [0.4.2.11](/wiki/Patch_0.4.2.11 "Patch 0.4.2.11") | 4.25   
[0.4.3.0](/wiki/Patch_0.4.3.0 "Patch 0.4.3.0") | [0.7.1.1](/wiki/Patch_0.7.1.1 "Patch 0.7.1.1") | 4.26   
[0.8.0.0](/wiki/Patch_0.8.0.0 "Patch 0.8.0.0") | (current) | 5+ **(unsupported)**  
  
Note that every time the UE viewer is closed, the path and UE version have to be set again. 

### Exporting the icons

#### Method A: Individual icons

  1. Tick 'flat view' at the top of the window
  2. Use the search bar to filter for specific icons. The names of all icons end with _64, _128, _256, or _512, noting their resolution.
  3. Once the desired icon is found, there are two ways to export it 
     * A) Right click → Export. The image will have the `.tga` extension. You can change the export format to .png.
     * B) Export button in the bottom right. This way allows to export `.tga`, uncompressed `.tga`, and most importantly `.png`. Again, do not change any options besides the file extension under "Texture Export".



#### Method B: Multiple icons in a specific category

If the exact name is not known, it's also possible to look for them manually by browsing the directory. This is also useful for exporting multiple icons in the same category, e.g. ores. 

  1. Ensure flat view is disabled for this method.
  2. Look into `All Packages/Game/FactoryGame/`
  3. Look for the desired category. Once a folder is chosen, the files within will appear on the right. The names of all icons end with _64, _128, _256, or _512, noting their resolution.
  4. Once the desired icon is found, there are two ways to export it 
     * A) Right click → Export. The image will have the `.tga` extension. You can change the export format to .png.
     * B) Export button in the bottom right. This way allows to export `.tga`, uncompressed `.tga`, and most importantly `.png`. Again, do not change any options besides the file extension under "Texture Export".



### Locating the exported icons

Exported icons can be located in a folder called UmodelExport that appears after the first export in the same location where the Umodel executable is. Exported icons are found in the same (mirrored) directory as in Umodel. 

Additionally, if `.tga` icons were exported, a simple image editing tool like [Paint.net](https://www.getpaint.net/) can be used to convert them into `.png`, as `.tga` files are unsupported on the wiki and `.png` is a much more broadly adopted format. 

## Copyright

Note that the exported content is copyrighted. When uploading the files to the wiki, make sure to select the correct license ("This is from the game or other materials owned by Coffee Stain Studios") or, alternatively, manually add the license after uploading by adding `{{[License/first-party](/wiki/Template:License/first-party "Template:License/first-party")}}` to the file page. 

[](https://www.coffeestainstudios.com/) | This file (or parts of it) comes from _Satisfactory_ (data files or gameplay), from websites, or from any other content created and owned by Coffee Stain Studios, who hold the copyright of _Satisfactory_. Unless specified otherwise, all trademarks and registered trademarks present in the image are proprietary to Coffee Stain Studios. For more information, see the [copyright notice](/wiki/Satisfactory_Wiki:Copyrights "Satisfactory Wiki:Copyrights").  
The use of images to illustrate articles concerning the subject of the images in question is believed to qualify as **[fair use](https://en.wikipedia.org/wiki/fair_use "wikipedia:fair use")** under [United States copyright law](https://en.wikipedia.org/wiki/United_States_copyright_law "wikipedia:United States copyright law"), as such display does not significantly impede the right of the copyright holder to sell the copyrighted material.   
---|---  
  
  


## See also

  * [Upload file](/wiki/Special:Upload "Special:Upload")



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
Dedicated servers| [Dedicated servers](/wiki/Dedicated_servers "Dedicated servers") • [Running as a Service](/wiki/Dedicated_servers/Running_as_a_Service "Dedicated servers/Running as a Service") • [Configuration files](/wiki/Dedicated_servers/Configuration_files "Dedicated servers/Configuration files") • [Automatic updates](/wiki/Dedicated_servers/Automatic_updates "Dedicated servers/Automatic updates") • [HTTPS API](/wiki/Dedicated_servers/HTTPS_API "Dedicated servers/HTTPS API") • [Lightweight Query API](/wiki/Dedicated_servers/Lightweight_Query_API "Dedicated servers/Lightweight Query API")  
Other| [Hypertube cannon](/wiki/Tutorial:Hypertube_cannon "Tutorial:Hypertube cannon") • [Hypertube brake](/wiki/Tutorial:Hypertube_brake "Tutorial:Hypertube brake") • [Steam Deck & Controller setup](/wiki/Tutorial:Controller_setup "Tutorial:Controller setup") • Extracting UI icons
  *[v]: View this template
  *[e]: Edit this template
  *[h]: History of this template
  *[his]: his trivia section
