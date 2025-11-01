# To-Do List

The **To-Do List** is an interface that allows the registration of [buildings](/wiki/Building "Building") and [blueprints](/wiki/Blueprint_Designer "Blueprint Designer") and [components](/wiki/Category:Crafting_components "Category:Crafting components") that the [pioneer](/wiki/Pioneer "Pioneer") planned to create, so that the required materials can be calculated and be viewed. If several items are added, you can view the summary of the total [components](/wiki/Category:Crafting_components "Category:Crafting components") required to make all of it. Each time an item on the list is made or built, one will be subtracted from the list. If all are done crafting or built, the To-Do List will be closed. 

## Contents

  * 1 Appearance
    * 1.1 Notes
      * 1.1.1 Formatting
    * 1.2 Recipes
  * 2 Adding and removing items
  * 3 Scrolling
  * 4 Gallery
  * 5 History
  * 6 References



## Appearance

[](/wiki/File:To-Do_List.png)

[](/wiki/File:To-Do_List.png "Enlarge")

To-Do List UI. Lists the materials you need to build or craft what you want.

The **To-Do List** is located on the right side of the screen and is comprised of three Sections (Public Notes, Private Notes, and Recipes). 

### Notes

The To-Do List optionally have two types of Notes: 

  * **Public** \- These are seen by everyone in a [Multiplayer](/wiki/Multiplayer "Multiplayer") Session, or on [Dedicated Servers](/wiki/Dedicated_Servers "Dedicated Servers").
  * **Private** \- These are only seen by the Player.



#### Formatting

Both Private and Public Notes can be formatted[1] using various codes as follows: 

Code [note 1] | Text Result   
---|---  
None  | Plain Text   
`<b>Your Text</>` | **Bolded Text**  
`<o>Your Text</>` | Orange Text  
`<ob>Your Text</>` | **Orange Bold Text**  
`<h>Your Text</>` | Header Text  
`[]` _(No Space)_ | [ ] Unchecked Checkbox   
`[×]` _(with small "x")_ | [**x**] Checked Checkbox   
  
Notes:

  1. ↑ In the Note Section Header **click on the "?" on the left** to see example formatting codes.



### Recipes

The top of the Recipe Section in the To-Do List UI shows the amount of [buildings](/wiki/Building "Building") and/or [components](/wiki/Category:Crafting_components "Category:Crafting components") that have been added. The lower section shows the total components required, as well as the current amount in inventory. 

  * If you have none of a certain material, its progress bar will be displayed as a solid gray line ▅▅▅▅.
  * If you have less than half of the amount of a certain material, its progress bar will be displayed a combination white and gray line ▅▅▅▅ showing how much resources is lacking.
  * If you have more than half of the amount of a certain material, its progress bar will be displayed a combination light orange and gray line ▅▅▅▅ showing how much resources is lacking.
  * If you have the full amount of a certain material, its progress bar will be displayed as a solid orange line ▅▅▅▅, and a tick will be displayed.



The maximum amount of each building or material that can be displayed is 2,147,483,647.[2]

## Adding and removing items

There are several ways to add and remove items to the To-Do List. 

  1. Open the [Codex](/wiki/Codex "Codex") using [`O`](/wiki/Controls "Controls"), view Recipe Tab[3], hover over an item and select it, select a recipe _(if more than one)_ , and then use the buttons to add it to the To-Do List to create it.
  2. Press Build Mode [`Q`](/wiki/Controls "Controls") to open the [Build Menu](/wiki/Build_Gun "Build Gun"), or Blueprint Menu, to add [buildings](/wiki/Building "Building"), and click the **+** icon that appears when you mouse over the desired building, or blueprint. Once added, a **–** icon appears as well, which will remove one of those buildings from the list.
  3. To add [components](/wiki/Category:Crafting_components "Category:Crafting components"), [`Right-click`](/wiki/Controls "Controls") the component in the [Craft Bench](/wiki/Craft_Bench "Craft Bench") or [Equipment Workshop](/wiki/Equipment_Workshop "Equipment Workshop") and click "Add to To-Do List". Once added, you can also [`Right-click`](/wiki/Controls "Controls") and click "Remove from To-Do List" to remove it.



By default, you can hold down the [`⇧ Left Shift`](/wiki/Controls "Controls") key to adjust the amount by 10. You can also type the number into the text box. 

Once there are items in the list, you can add or subtract items directly in the **To-Do List** UI by opening the [build menu](/wiki/Build_Gun "Build Gun"). You can also delete the whole list by selecting "Clear List" at the bottom, provided the [build menu](/wiki/Build_Gun "Build Gun") is active. 

If you always a maintain a recipe in the To-Do List that isn't a Note, it makes it very easy to edit the lists at will by opening any menu (examples: inventory, build) that displays the cursor, and moving the cursor to the right side of the screen. 

## Scrolling

Some material may be hidden at the lower window so that it requires the player to scroll down to view it. To scroll through the **To-Do List** , open the [build menu](/wiki/Build_Gun "Build Gun") first. You could also enable the scrolling of the to-do list by open any of the in-game UI. 

## Gallery

  * [](/wiki/File:To-Do_List_UI.png "Update 5 - To-Do List UI")

Update 5 - To-Do List UI

  * [](/wiki/File:To-Do_List_Tutorial.png "To add a building into To-Do List, click on the '+' button as shown.")

To add a building into To-Do List, click on the '+' button as shown.

  * [](/wiki/File:Codex_and_To-Do_List.png "You can also add an item to the To-Do List via the Codex O then on the item recipe.")

You can also add an item to the To-Do List via the Codex [`O`](/wiki/Controls "Controls") then [](/wiki/File:Keyboard_White_Mouse_Right.png "Right") on the item recipe.

  * [](/wiki/File:To-Do_List_Formatting_U6.png "Update 6 - Example use of To-Do List Formatting")

Update 6 - Example use of To-Do List Formatting

  * [](/wiki/File:Todo_List_Blueprints_U7.png "Update 7 - Example of adding a Blueprint to the To-Do List")

Update 7 - Example of adding a Blueprint to the To-Do List




## History

  * [Patch 0.7.1.1](/wiki/Patch_0.7.1.1 "Patch 0.7.1.1")
    * Fixed the To-Do list showing 0’s on recipes and crashing the game while trying to edit it sometimes when reloading a save
  * [Patch 0.7.0.6](/wiki/Patch_0.7.0.6 "Patch 0.7.0.6"): Fixed To-Do List not updating
  * [Patch 0.7.0.5](/wiki/Patch_0.7.0.5 "Patch 0.7.0.5"): 
    * Fixed an issue where the To-Do List would lose focus after using the text boxes
    * To-Do List should now handle alternate recipe names and multi-product recipes better
    * To-Do list now supports Blueprints
  * [Patch 0.7.0.2](/wiki/Patch_0.7.0.2 "Patch 0.7.0.2"): Fixed To-Do List not having a character limit
  * [Patch 0.6.0.5](/wiki/Patch_0.6.0.5 "Patch 0.6.0.5"): Fixed an issue where the Edit To-Do List Button would appear when loading/joining a session
  * [Patch 0.5.0.9](/wiki/Patch_0.5.0.9 "Patch 0.5.0.9"): Fixed the + and - buttons on the To-Do List being highlighted by default when adding items to the list
  * [Patch 0.5.0.8](/wiki/Patch_0.5.0.8 "Patch 0.5.0.8"): Fixed To-Do List not saving when reconnecting to a [Multiplayer](/wiki/Multiplayer "Multiplayer") session
  * [Patch 0.5.0.4](/wiki/Patch_0.5.0.4 "Patch 0.5.0.4"): Shopping List colours are now clearer to distinguish
  * [Patch 0.3.3.0](/wiki/Patch_0.3.3.0 "Patch 0.3.3.0"): 
    * Updated the look of the “Add to To-Do List” menu
    * Added “Add to To-Do List” functionality to the Codex
  * [Patch 0.2.1.10](/wiki/Patch_0.2.1.10 "Patch 0.2.1.10"): Fixed some minor visual bugs in the To-Do List
  * [Patch Closed Alpha 2](/wiki/Patch_Closed_Alpha_2 "Patch Closed Alpha 2"): 
    * Not visually blocked anymore when using Workshop or Craft Bench.
    * (Craft Bench Menu): Fixed focus issue when removing parts from the list.



## References

  1. ↑ [YouTube - NEW Ammo types and Equipment System Improvements - To-Do List Notes Formatting](https://www.youtube.com/watch?v=QYMHs1aTyOs&t=879s)
  2. ↑ [Satisfactory Q&A - Large numbers don't go well on todo list.](https://questions.satisfactorygame.com/post/5f1ecfab6f3c82fe950ba693)
  3. ↑ [YouTube - NEW Ammo types and Equipment System Improvements - To-Do List Addition](https://www.youtube.com/watch?v=QYMHs1aTyOs&t=834s)



  * [v](/wiki/Template:PioneerNav "Template:PioneerNav")
  * [e](https://satisfactory.wiki.gg/wiki/Template:PioneerNav?action=edit)
  * [h](https://satisfactory.wiki.gg/wiki/Template:PioneerNav?action=history)

[Satisfactory](/wiki/Satisfactory "Satisfactory") game mechanics  
---  
Player abilities| [Codex](/wiki/Codex "Codex") • [Resource Scanner](/wiki/Resource_Scanner "Resource Scanner") • [Build Gun](/wiki/Build_Gun "Build Gun") • [Inventory](/wiki/Inventory "Inventory") • [Health](/wiki/Health "Health") • [Combat](/wiki/Combat "Combat") • [Movement](/wiki/Movement "Movement") • [Flashlight](/wiki/Flashlight "Flashlight") • [HUD](/wiki/HUD "HUD") • [Crate](/wiki/Crate "Crate") • To-Do List  
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
Other| [Hypertube cannon](/wiki/Tutorial:Hypertube_cannon "Tutorial:Hypertube cannon") • [Hypertube brake](/wiki/Tutorial:Hypertube_brake "Tutorial:Hypertube brake") • [Steam Deck & Controller setup](/wiki/Tutorial:Controller_setup "Tutorial:Controller setup") • [Extracting UI icons](/wiki/Tutorial:Extracting_UI_icons "Tutorial:Extracting UI icons")
  *[v]: View this template
  *[e]: Edit this template
  *[h]: History of this template
  *[his]: his trivia section
