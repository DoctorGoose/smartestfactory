# Blueprint

Blueprints are made using one of the three [Blueprint Designers](/wiki/Blueprint_Designer "Blueprint Designer"). 

## Contents

  * 1 Usage
    * 1.1 Construction
      * 1.1.1 Hotbar assignment
      * 1.1.2 Auto-connect
      * 1.1.3 Hologram lock and nudge mode
      * 1.1.4 Dismantle mode
    * 1.2 Snapping
      * 1.2.1 Designing
      * 1.2.2 Snapping point
      * 1.2.3 Blueprint snapping
      * 1.2.4 World grid
  * 2 Designing
  * 3 Categories
    * 3.1 Adding
    * 3.2 Moving
  * 4 Blueprint files
    * 4.1 Naming
    * 4.2 Saving
    * 4.3 Save Location
      * 4.3.1 Single Player
      * 4.3.2 Dedicated Server
    * 4.4 Types
    * 4.5 Sharing
    * 4.6 Removal
    * 4.7 Transfer to new game save
  * 5 Blueprint file format
    * 5.1 Blueprint File Header
    * 5.2 Blueprint File Body
  * 6 To-Do List
  * 7 Tips
  * 8 Narrative
  * 9 Gallery
  * 10 History
  * 11 References



## Usage

Blueprints are placed using the [Build Gun](/wiki/Build_Gun "Build Gun")

### Construction

Blueprints will have a "forward" direction, as indicated by a white arrow ▶ during placement, showing the "front" of the blueprint determined during the design of the blueprint _(see[Blueprint Designer Control Bench](/wiki/Blueprint_Designer#Blueprint_Designer_Control_Bench "Blueprint Designer"))._[1]

Blueprints can be placed in the World by selecting blueprint from the [Blueprint Build Menu](/wiki/Build_Gun#Build_menu "Build Gun"), or from a hotbar, then using mouse movements to align where you want blueprint to go, followed by use of [](/wiki/File:Keyboard_White_Mouse_Left.png "Left") (LMB) to place. 

Once buildables have been placed they can edited individually just like normal buildings. 

#### Hotbar assignment

Blueprints can be bound to a [Hotbar](/wiki/Hotbar "Hotbar") by hovering over them in the [Blueprint Build Menu](/wiki/Build_Gun#Build_menu "Build Gun") and pressing the respective [`0`](/wiki/Controls "Controls")–[`9`](/wiki/Controls "Controls") key. Each blueprint can only be bound to each hotbar once, but the same blueprint can be bound to multiple hotbars. 

Once a blueprint has been bound to a hotbar, it can be overwritten anytime, but a hotbar can never be cleared once anything has been bound to it. 

Blueprints already bound to hotbars at the bottom of the screen can be then selected with the respective key. There are ten hotbars in total, which can be cycled through by [`Alt`](/wiki/Controls "Controls")+[](/wiki/File:Keyboard_White_Mouse_Middle.png "Middle") scrolling. 

#### Auto-connect

Pressing [`R`](/wiki/Controls "Controls") when having a Blueprint Hologram out will activate the **Blueprint Auto-Connect Build Mode** , and any blueprint that contains [Conveyor Belts](/wiki/Conveyor_Belts "Conveyor Belts"), [Pipelines](/wiki/Pipelines "Pipelines") and [Railways](/wiki/Railway "Railway") will try to automatically connect to any available inputs/outputs on the other end, which you can visually confirm before placing by hovering over with the blueprint hologram. 

#### Hologram lock and nudge mode

During placement, blueprints can make use of [Nudge Mode](/wiki/Build_Gun#Hologram_lock_and_nudge_mode "Build Gun") to align blueprint in 1m (or 0.5m) steps in both the horizontal and vertical planes.[2][3]

#### Dismantle mode

  * Once buildables are built using the blueprint function, by using [Blueprint Dismantle Mode](/wiki/Build_Gun#Dismantle_mode "Build Gun") all blueprint buildables can be dismantled either individually, or by buildable type, or by dismantling the entire blueprint.[4][5][6]
  * When in blueprint dismantle mode, clicking on any buildable in a blueprint will automatically select the entire blueprint and not just the buildable selected.
  * Blueprints are given unique id's when placed, and all buildables in the placed blueprint are linked together. What this means is that if you dismantle some of a blueprint you can still select and dismantle the remainder.[7]
  * Buildables that are not part of a blueprint added later, like conveyor belts, will not be dismantled when using blueprint dismantle mode, but will have to be dismantled separately.
  * TIP: By using the [Building Eyedropper Function](/wiki/Build_Gun#Building_eyedropper "Build Gun") you can sample blueprints using dismantle mode.



### Snapping

#### Designing

On the platform of the Designer, buildables are snapped to 1 x 1 meter grids as on normal Foundations. 

#### Snapping point

The Snapping point of the blueprint is always at the center of the blueprinted buildables. 

#### Blueprint snapping

When on default build mode, blueprints can be snapped to 'loose foundations' - foundations not built using blueprints - at 1 meter in horizontal or 0.5 meter in vertical. This requires careful manual alignment. 

When using 'Blueprint' build mode, blueprints snap to each other based on the center of blueprinted buildables, barring encroachments. 

When using 'Auto Connect' build mode, any blueprint that contains Conveyor, Pipes or Railways will try to automatically connect to any available inputs/outputs on the other end up to 16m (2 foundations away), which you can visually confirm before placing by hovering over with the blueprint hologram. 

  * Blueprint auto connections for [Pipeliness](/wiki/Pipelines "Pipelines") and [Conveyor Beltss](/wiki/Conveyor_Belts "Conveyor Belts") now detect connections that are on top of themselves (Just like train tracks), and additionally prioritize the connection that is most aligned with themselves, instead of the closest connection.



An already built blueprint preserves its snapping point for the other blueprints to snap to. 

#### World grid

Blueprints have difficulty aligning to the [world grid](/wiki/World_grid "World grid") when built on the ground. It is advisable to create 'base' foundations using the world grid, then build blueprinted foundations above or beside it. Once done, the 'loose' foundations can be dismantled. 

## Designing

  * Blueprints are linked to the Mark Level Blueprint Designer in which they are designed, and cannot be individually edited using a different Mark Level Blueprint Designer. 
    * This means, for example, that a blueprint created in a Mk.1 Blueprint Designer cannot be individually edited in a Mk.2 or Mk.3 Blueprint Designer. _This is by design to prevent issues_.
  * Blueprints made in a **lower** Mark Level Blueprint Designer can be **added** to a new blueprint in an upper Mark Level Blueprint Designer, however Blueprints made in a **higher** Mark Level Blueprint Designer cannot be added. _Again, this is by design to prevent issues_. 
    * This means, for example, that a blueprint created in a Mk.1 Blueprint Designer can be added to a Mk.2 or Mk.3 Blueprint Designer _(since it will fit)_. Additionally, for example, a blueprint created in a Mk.2 Blueprint Designer can be added to a Mk.3 Blueprint Designer, but cannot be added to a Mk.1 Blueprint Designer.



## Categories

Blueprint categories and sub-categories are part of the [save game file](/wiki/Save_files "Save files"), and if a blueprint is shared, or moved from a different directory, the category information will not show up, and the added blueprints will show up in the **Undefined Category**.[8]

Once you see the Blueprint in the Undefined Category, you can move it to any category you wish. 

★ IMPORTANT: Additional categories and/or sub-categories **must be created first** before they can be used by a blueprint. 

### Adding

To add a Category or Sub-Category, in the [Blueprint Designer User Interface](/wiki/Blueprint_Designer#User_Interface "Blueprint Designer") __when there is no blueprint on Blueprint Designer Pad__ , click on **Set Directory** , then **Add Category** or **Add Subcategory** , followed by completion of another Dialog, then **Apply Changes** , then click **[X] Button** _(to close Directory Dialog)._

After creation of a new category and/or sub-category , it is recommended you move one blueprint there to prevent issues. 

  * [](/wiki/File:Blueprint_Menu_-_Undefined_Category.png "Blueprint Build Menu showing Default Undefined Category")

Blueprint Build Menu showing Default Undefined Category

  * [](/wiki/File:Blueprint_Menu_-_Defined_Category.png "Blueprint Build Menu showing some Defined Categories")

Blueprint Build Menu showing some Defined Categories




### Moving

To move an _existing blueprint_ to a new category and/or sub-category, in the Blueprint Designer User Interface __when there is no blueprint on Blueprint Designer Pad__ , click on **Set Directory** and then **Edit** _(you will see a white square surrounding Blueprints)_. You can then drag any desired Blueprints to whatever Category / Sub-Category you wish. When done click **Apply Changes** followed by clicking **[X] Button** _(to close Directory Dialog)._

## Blueprint files

### Naming

  * Blueprint names can use most characters. _except as indicated below._
  * **CAUTION** To avoid game issues, blueprint names should not start or end with a [`Space`](/wiki/Controls "Controls") or a [`.`](/wiki/Controls "Controls") (period). Additionally, blueprint names should not contain an [`'`](/wiki/Controls "Controls") (apostrophe), or any of the following Windows Reserve Characters: 
    * [`<`](/wiki/Controls "Controls") (less than)
    * [`>`](/wiki/Controls "Controls") (greater than)
    * [` :`](/wiki/Controls "Controls") (colon)
    * [`"`](/wiki/Controls "Controls") (double quote)
    * [`/`](/wiki/Controls "Controls") (forward slash)
    * [`\`](/wiki/Controls "Controls") (backslash)
    * [`Bar`](/wiki/Controls "Controls") (vertical bar or pipe "|")
    * [`?`](/wiki/Controls "Controls") (question mark)
    * [` *`](/wiki/Controls "Controls") (asterisk)



### Saving

  1. Prior to saving, make sure you add any new Category and/or Subcategory if desired _(see above)_.
  2. In Blueprint Designer Console UI enter: 
     * **Blueprint Name**
       * The Blueprint Name character limit is designed to prevent issues when using the blueprint build menu.
       * Game does not use [Natural Sorting Order](https://en.wikipedia.org/wiki/Natural_sort_order), but uses **Alphabetical Sorting** so Blueprints with names like z1, z2, z11, will be sorted like z1, z11, z2.
       * It is recommended, if desired, to use zeros "0" in your Blueprint Names like z001, z002, z011, which will then sort correctly using Alphabetical Sorting.
     * **Blueprint Description** _(Optional)_
       * The use of the Blueprint Description allows more characters than the Blueprint Name, and provides more information about the use of the blueprint.
     * Click on **Set Directory** and select the added Category _(you should see "+ Add Blueprint Here", and when clicked you will see the Blueprint Name you chose along with "New")_ and then click **[X] Button** _(to close Directory Dialog)._
  3. In Blueprint Designer Console UI verify that correct Directory is shown, and when satisfied click on **Save Blueprint**. **You should now be able to find the New Blueprint in the Category / Sub-Category you chose.**


  * [](/wiki/File:Blueprint_Designer_UI.png "Blueprint Designer User Interface")

Blueprint Designer User Interface




### Save Location

  1. Blueprints are contained in their own Session Name Directory.[9][10]
  2. At least one Blueprint Module must be created and saved in order for the Blueprint Directory to be created.
  3. ★**IMPORTANT: Blueprint Modules are NOT saved in the same location as the game save files and as such are not automatically cloud synced.**[11][12] This means you will manually have to back up your Blueprint Files periodically to a location not used by the game. This also means that blueprints will not persist between sessions on cloud gameplay services such as GeForce NOW.
  4. Blueprints are not global to prevent players from starting a new game session with all previously made Blueprints already available.
  5. Players can choose to move Blueprints over to new Game Session Directory if they want.



#### Single Player

Both Steam and Epic Games version use the same PATH depending on OS used. 

  1. Linux: `~/.steam/root/steamapps/compatdata/526870/pfx/drive_c/users/steamuser/AppData/Local/FactoryGame/Saved/SaveGames/blueprints/{SESSION NAME}`
  2. Windows (either Path will work): 
     * Path 1: `%LOCALAPPDATA%\FactoryGame\Saved\SaveGames\blueprints\{SESSION NAME}`
     * Path 2: `\Users\<your Windows username>\AppData\Local\FactoryGame\Saved\SaveGames\blueprints\{SESSION NAME}`
  3. Steam Deck: `/home/deck/.steam/root/steamapps/compatdata/526870/pfx/dosdevices/c:/users/steamuser/AppData/Local/FactoryGame/Saved/SaveGames/blueprints/{SESSION NAME}`
     * **⭑ NOTE:** Steam Deck blueprints are within a _hidden_ folder, and you must first **show hidden files** before you can view the folder via the Steam Deck File Explorer.[13] Files are contained in a _compacted data folder_ with name of **526870**.



****

#### Dedicated Server

Both Steam and Epic Games versions of the game use the same blueprint directory. 

  1. Linux: `~/.config/Epic/FactoryGame/Saved/SaveGames/blueprints/{SESSION NAME}`
  2. Windows (User): `%LOCALAPPDATA%\FactoryGame\Saved\SaveGames\blueprints\{SESSION NAME}`
  3. Windows (NSSM): `%WINDIR%\System32\config\systemprofile\AppData\Local\FactoryGame\Saved\SaveGames\blueprints\{SESSION NAME}`
  4. Windows Server (Windows Service): `%WINDIR%\ServiceProfiles\NetworkService\AppData\Local\FactoryGame\Saved\SaveGames\blueprints\{SESSION NAME}`
     * Note: The first time the Windows Service paths are accessed (NSSM or Windows Server Service), it is necessary to manually navigate through the folder structure using File Explorer and grant access to each of the folders as they are opened, using a user account with administrative rights.



### Types

  * Blueprints consist of two separate files: [14]
    * **Blueprint Module** (.sbp) - This holds the Blueprint Layout / Design information.
    * **Blueprint Config File** (.sbpcfg) - This holds the information about: 
      * Blueprint Description.
      * Icon used.
      * Icon Color used.



### Sharing

  * Players only need to share the actual Blueprint Module (.sbp) and not the related Blueprint Config File (.sbpcfg).
  * These [websites](/wiki/Online_tools#Downloadable_blueprints "Online tools") are dedicated to the sharing of Blueprints where the **.sbp** files _(and optionally the**.sbpcfg** files)_ may be uploaded, or downloaded and placed in the appropriate Blueprint directory on the Player's PC.
  * ★ IMPORTANT: The game save **must be reloaded** before any shared blueprints that are downloaded will show up in the blueprint build menu.



### Removal

  * Blueprint Modules can be removed at any time.
  * ❗ **WARNING:** By removing a Blueprint it will be deleted from your computer. This cannot be undone, even if you load an older Game Save file.



### Transfer to new game save

Your blueprint files can be transferred from another game save session to a new game save session using the following steps: 

  1. In the new game save session, you need unlock the blueprint designer in [Tier 4, Milestone 1](/wiki/Milestones#Tier_4 "Milestones"), FICSIT Blueprints. 
     * Complete [Space Elevator Phase 1](/wiki/Space_Elevator#Project_Assembly_phases "Space Elevator") to unlock Tier 3 / Tier 4.
     * (OPTIONAL) You can use the [Awesome Shop - Parts](/wiki/AWESOME_Shop#Parts "AWESOME Shop") to purchase the needed ingredients to make [Smart Plating](/wiki/Smart_Plating "Smart Plating") needed to complete Space Elevator Phase 1.
  2. In the new game save session, once the blueprint designer is unlocked, you need to use it to **make one Blueprint** , say a 4x4 foundation blueprint, and save it. 
     * _Doing this will create the Blueprint Save Location / Directory for**that game save session** on your PC._
  3. Go to the blueprint save file location _(see above)_ on your PC for the _other game save session_ , and transfer any desired blueprints to the new game save session blueprint save file location.
  4. ★ IMPORTANT: The game save **must be reloaded** before any blueprints that are transferred will show up in the blueprint build menu.



## Blueprint file format

Blueprint Module (.sbp) files, which holds the blueprint layout / design information, have a format similar to [save files](/wiki/Save_files#Save_file_format "Save files"). Below is a description of the format; it references elements from the save file format definition. 

### Blueprint File Header

basic data type  | description  | example  | notes   
---|---|---|---  
Uint32  | save header version  | 14  | Same as SaveFileHeader.   
Uint32  | save version  | 52  | Same as SaveFileHeader.   
Uint32  | build version  | 418,783  | Same as SaveFileHeader.   
Uint32  | size (X)  | 4  | Size of the blueprint, in 8-meter units.   
Uint32  | size (Y)  | 4  | Size of the blueprint, in 8-meter units.   
Uint32  | size (Z)  | 4  | Size of the blueprint, in 8-meter units.   
Uint32  | number of cost entries  | 11  | Number of entries which describe the blueprint material costs.   
N/A  | cost entries  | N/A  | Array of: 

  * String - item class name
  * Uint32 - quantity

  
Uint32  | number of contents entries  | 3  | Number of entries which describe the blueprint contents.   
N/A  | contents entries  | N/A  | Array of: 

  * String - building class name

  
  
Following the header is a list of compressed chunks, juts like in a save file. Each chunk has the same compressed format (CompressedSaveFileBody). After decompression, the format is as follows: 

### Blueprint File Body

data type  | description  | example  | notes   
---|---|---|---  
Uint32  | uncompressed size of the body  | 34,567  | in number of bytes, for the whole body except this size field itself   
Uint32  | size of object headers  | 12,345  | in number of bytes, including the count below but excluding this field   
Uint32  | number of object headers  | 123  |   
N/A  | object headers  | N/A  | see ObjectHeader (in [Save_files](/wiki/Save_files "Save files")) for a description of the format.   
Uint32  | size of objects  | 23,456  | in number of bytes, including the count below but excluding this field   
Uint32  | number of objects  | 123  | same as number of object headers   
N/A  | objects  | N/A  | see ActorObject or ComponentObject (in [Save_files](/wiki/Save_files "Save files")) for a description of the format. Note that this is not a LevelObject.   
  
## To-Do List

Blueprints can be added at any time to the [To-Do List](/wiki/To-Do_List "To-Do List"). 

## Tips

  * You can build already existing blueprints again in the blueprint designer. For example, if you create a 4 identical constructor levels inside the blueprint designer, you only have to build the first one manually. After you have finished level 1, save it as a new blueprint. Then select that blueprint and place it right above the existing buildings in the blueprint designer. You immediately have level 2. Then place it again for level 3 and for level 4. Now save the entire blueprint again and you have an 4 story constructor assembly with little more work than one story of it.
  * The default blueprint icon color (which is not available as a preset unless saved manually) is #5CAFC5.
  * For production buildings and power generators, any ingredients or fuel in the **Input Buffer** , or items in [Storage Containers](/wiki/Storage_Container "Storage Container"), will be saved when the blueprint is saved and become immediately available when blueprint is placed _(CREDIT: Reddit Member_ u/MatthewMMorrow [15]_)._



## Narrative

**Expand to reveal spoiler**

When performing specific actions, the player will hear [ADA](/wiki/ADA "ADA") speak. 

  * View [Story Player Actions - Pioneer Constructs](/wiki/Story#Player_Actions "Story") to read and hear individual ADA messages related to making a Custom Blueprint.



## Gallery

  * [](/wiki/File:Blueprint_Designer_Control_Bench_With_Storage_Box.png "Blueprint Designer Control Bench With Storage Box")

Blueprint Designer Control Bench With Storage Box

  * [](/wiki/File:Todo_List_Blueprints_U7.png "Example of adding a Blueprint to the To-Do List")

Example of adding a Blueprint to the To-Do List

  * [](/wiki/File:Blueprint_Directional_Arrow.png "Example Blueprint Directional Arrow \(on left\)")

Example Blueprint Directional Arrow (on left)

  * [](/wiki/File:Blueprint_Placement.png "Example of Blueprint placement")

Example of Blueprint placement

  * [](/wiki/File:Blueprint_Dismantle.png "Example use of Blueprint Dismantle Mode \(note missing storage container in front / right\)")

Example use of Blueprint Dismantle Mode _(note missing storage container in front / right)_




## History

  * [Patch 1.1.1.5](/wiki/Patch_1.1.1.5 "Patch 1.1.1.5"): Fix for a specific crash when loading saves that contain Conveyor Belts built by blueprint auto-connect during 1.1 Experimental when it was not working correctly and have not been resaved since
  * [Patch 1.1.1.2](/wiki/Patch_1.1.1.2 "Patch 1.1.1.2"): Fix for a Crash on specific [saves](/wiki/Save_files "Save files") that had faulty Blueprints using auto connected [Conveyor Belts](/wiki/Conveyor_Belts "Conveyor Belts") during a previous update during experimental
  * [Patch 1.1.1.1](/wiki/Patch_1.1.1.1 "Patch 1.1.1.1")
    * Fix for [Conveyor Belts](/wiki/Conveyor_Belts "Conveyor Belts") built using Blueprint Auto Connections not working after saving and reloading 
      * Existing Conveyor Belts that are affected by this issue will have to be rebuilt to work properly after this fix
    * Fixed Blueprint Auto Connect sometimes flipping the direction of the hologram when building a Blueprint that contained [Railways](/wiki/Railway "Railway")
  * [Patch 1.1.0.6](/wiki/Patch_1.1.0.6 "Patch 1.1.0.6")
    * Fixed Blueprints exiting [Nudge Mode](/wiki/Build_Gun#Hologram_lock_and_nudge_mode "Build Gun") when confirming auto connections
    * Fixed Blueprint auto connections not appearing for connections behind the Blueprint
    * Fixed Blueprint auto connections incorrectly confirming connections that aren’t valid (Without the link icon in the hologram)
  * [Patch 1.1.0.5](/wiki/Patch_1.1.0.5 "Patch 1.1.0.5")
    * Fixed Blueprints not syncing correctly between players in [Multiplayer](/wiki/Multiplayer "Multiplayer")
    * Fixed [Conveyor Splitter](/wiki/Conveyor_Splitter "Conveyor Splitter")/[Conveyor Merger](/wiki/Conveyor_Merger "Conveyor Merger") attached to ends of [Conveyor Lifts](/wiki/Conveyor_Lifts "Conveyor Lifts") not working when placed as part of a Blueprint
  * [Patch 1.1.0.4](/wiki/Patch_1.1.0.4 "Patch 1.1.0.4"): Fixed automatic blueprint connections not copying customizations applied to the building they are connecting to
  * [Patch 1.1.0.3](/wiki/Patch_1.1.0.3 "Patch 1.1.0.3"): Fixed Blueprint Auto Connect alignment so it also considers height differences between connections
  * [Patch 1.1.0.2](/wiki/Patch_1.1.0.2 "Patch 1.1.0.2")
    * Potential fix for scenarios where Blueprint Auto connections would sometimes not work in [Multiplayer](/wiki/Multiplayer "Multiplayer")
    * Fixed bug where blueprint auto connection were playing a lot of snapping sound effects when auto connecting to an open-ended Railway junction
    * Increased distance for Blueprint Auto Connection Detection from 10m to 16m (2 foundations)
    * Blueprint auto connections for [Pipeliness](/wiki/Pipelines "Pipelines") and [Conveyor Beltss](/wiki/Conveyor_Belts "Conveyor Belts") now detect connections that are on top of themselves (Just like train tracks)
    * Blueprint auto connections now prioritize the connection that is most aligned with themselves, instead of the closest connection
  * [Patch 1.1.0.0](/wiki/Patch_1.1.0.0 "Patch 1.1.0.0")
    * There is now a new “Auto Connect” build mode for Blueprints that you can select by pressing [`R`](/wiki/Controls "Controls") when having a Blueprint Hologram out 
      * When using this mode, any blueprint that contains [Conveyor Belts](/wiki/Conveyor_Belts "Conveyor Belts"), [Pipelines](/wiki/Pipelines "Pipelines") and [Railways](/wiki/Railways?action=edit&redlink=1 "Railways \(page does not exist\)") will try to automatically connect to any available inputs/outputs on the other end, which you can visually confirm before placing by hovering over with the blueprint hologram
  * [Patch 1.0.1.0](/wiki/Patch_1.0.1.0 "Patch 1.0.1.0")
    * Fixed a Crash when there is a Failure to open [Save game](/wiki/Save_files "Save files") and Blueprint files for reading
    * Fixed white boxes appearing in the compass when [Train Stations](/wiki/Train_Station "Train Station") would be built from Blueprints in some scenarios
  * [Patch 1.0.0.5](/wiki/Patch_1.0.0.5 "Patch 1.0.0.5")
    * Optimized the [Lightweight Subsystem](/wiki/Unreal_Engine#Lightweight_Actors "Unreal Engine"), this improves a bug where hovering over big Blueprint holograms over existing buildable's would drastically lower performance until the hologram was closed
    * Fixed crashes related to dismantling some parts of a Blueprint, mostly affecting [Conveyor Belts](/wiki/Conveyor_Belt "Conveyor Belt"), [Pipelines](/wiki/Pipeline "Pipeline") and [Railways](/wiki/Railway "Railway")
    * Fixed a bug where loading a Blueprint in a designer would load it in all the previously interacted [designers](/wiki/Blueprint_Designer "Blueprint Designer")
    * Fixed a crash related to Blueprint connections when exiting or loading a save
  * [Patch 1.0.0.4](/wiki/Patch_1.0.0.4 "Patch 1.0.0.4"): Fix for Blueprints not showing up or being unusable in sessions that ended with a period/fullstop
  * [Patch 1.0.0.3](/wiki/Patch_1.0.0.3 "Patch 1.0.0.3"): Fixed Blueprints being slightly offset compared to previous updates
  * [Patch 1.0](/wiki/Patch_1.0 "Patch 1.0")
    * Introduced Blueprint Designer Mk.2 and Mk.3
    * Renamed Blueprint Designer to Blueprint Designer Mk.1
    * While dismantling, you can also now change the build mode to completely dismantle all parts of a blueprint instead of only a single element from it at a time
  * [Patch 0.8.2.0](/wiki/Patch_0.8.2.0 "Patch 0.8.2.0")
    * You can now sample blueprints from dismantle mode
    * Pillars can partially intersect the edges of the Blueprint Designer again
  * [Patch 0.8.0.5](/wiki/Patch_0.8.0.5 "Patch 0.8.0.5"): Fixed Blueprints saved over old Update 7 Blueprints having weird issues and crashing when the Blueprint contained Pipelines
  * [Patch 0.8.0.3](/wiki/Patch_0.8.0.3 "Patch 0.8.0.3")
    * Fixed the Railways, Hypertubes and Pipelines visually having incorrect rotation when set via Blueprint 
      * This may also fix sinking/incorrectly rotated foundations in some scenarios
    * Fixed the FICSIT Blueprints milestone not showing the Blueprint Designer in the unlock list
  * [Patch 0.8.0.0](/wiki/Patch_0.8.0.0 "Patch 0.8.0.0")
    * Added a directional indicator to the Blueprint hologram
    * Added a Blueprints Dismantle Mode that can be switched on in the regular Dismantle Mode, allowing an entire Blueprint to be dismantled at once
    * Added Quick Switch functionality to Blueprints, allowing the player to quickly switch between Blueprints in the same sub-category
    * Added Sample functionality to Blueprints (can only be sampled when in Blueprint Dismantle Mode)
  * [Patch 0.7.1.1](/wiki/Patch_0.7.1.1 "Patch 0.7.1.1")
    * Fixed a very rare crash related to the build effect while building Blueprints
    * Fixed being able to place [Coal generators](/wiki/Coal_Generator "Coal Generator") at the edge of Blueprints and still have them hook to power
    * Fixed [Multiplayer](/wiki/Multiplayer "Multiplayer") and [Dedicated Server](/wiki/Dedicated_Server "Dedicated Server") Clients not being able to place [Power Poles](/wiki/Power_Poles "Power Poles") off a [Power Cable](/wiki/Power_Line "Power Line") in the Blueprint Designer
  * [Patch 0.7.0.8](/wiki/Patch_0.7.0.8_\(Experimental\) "Patch 0.7.0.8 \(Experimental\)"): Fixed hologram clearance showing up in the Blueprint build effect
  * [Patch 0.7.0.7](/wiki/Patch_0.7.0.7 "Patch 0.7.0.7")
    * Fixed being unable to save Blueprints in sessions with names with empty spaces
    * Temporary fixes to Blueprint snapping in Foundations, this should make it so Blueprints no longer sink in-between foundations
  * [Patch 0.7.0.6](/wiki/Patch_0.7.0.6 "Patch 0.7.0.6")
    * Fixed being able to build [Geothermal Generators](/wiki/Geothermal_Generator "Geothermal Generator") in the Blueprint Designer
    * Fixed a duplication bug with the Blueprint Designer
    * Fixed being able to access the Blueprint Designer window while the image browser or color picker is open
    * Fixed [Drone Stations](/wiki/Drone_Port "Drone Port") breaking when placing via Blueprint
    * Fixed an issue where the Blueprint info would still be shown in the info box after removing a Blueprint
    * Fixed newly created Blueprints not retaining their selected category/subcategory when saving for the first time
  * [Patch 0.7.0.5](/wiki/Patch_0.7.0.5 "Patch 0.7.0.5")
    * Fixed boomers clearance for Blueprint holograms
    * To-Do list now supports Blueprints
    * [Walkways](/wiki/Walkway "Walkway") and [Pillar](/wiki/Foundations "Foundations") should now affect Blueprint size
    * [Railroad tracks](/wiki/Railway "Railway") should now properly display when placing a Blueprint hologram
    * Blueprints should now snap to the sides of foundations when aiming close to the edge unless Snap To Guidelines is held
    * Fixed a crash caused by snapping Blueprints to walls
    * Fixed a crash when placing a Blueprint in the Blueprint Designer
    * Fixed deletion of Blueprints not properly propagating from Host to Clients
  * [Patch 0.7.0.4](/wiki/Patch_0.7.0.4 "Patch 0.7.0.4")
    * Fixed invisible buildings built from Blueprints when reconnecting to [Dedicated Servers](/wiki/Dedicated_Servers "Dedicated Servers")
    * Fixed an issue where the center point of Blueprints was not perfectly aligned to gird
    * Fixed a rotation issue when snapping Blueprints in a certain way
    * More improvements to Blueprint snapping to [Foundations](/wiki/Foundations "Foundations")
    * Fixed a scenario where buildings could be placed half in, half out of a Blueprint designer when being placed as part of an existing blueprint
    * Fixed some Blueprint snapping issues when aiming at the ground
    * Added Blueprint snapping for [Walls](/wiki/Walls "Walls")
  * [Patch 0.7.0.3](/wiki/Patch_0.7.0.3 "Patch 0.7.0.3")
    * Fixed Double Wall Outlet allowing circuits from outside the Blueprint Designer to connect to those inside of it
    * Fixed issue with snapping Blueprints vertically when aiming on the side
  * [Patch 0.7.0.2](/wiki/Patch_0.7.0.2 "Patch 0.7.0.2")
    * Fixed a crash related to the build effect on Blueprints
    * Better fix for invalid character names in Blueprints
    * Fixed some scenarios where [Railways](/wiki/Railway "Railway"), [Conveyor Belts](/wiki/Conveyor_Belts "Conveyor Belts") and [Pipelines](/wiki/Pipelines "Pipelines") could be placed through the floor of the Blueprint Designer
    * Fixed issues with holograms not detecting the edges of the Blueprint Designer
    * Fixed Blueprints Milestone being displayed incorrectly
  * [Patch 0.7.0.1](/wiki/Patch_0.7.0.1 "Patch 0.7.0.1")
    * Fixed Blueprints containing special buildable's that get auto created by other buildable's (Like [Sign](/wiki/Signs "Signs") poles, [railroad track switches](/wiki/Railroad_Switch_Control "Railroad Switch Control"), etc) not being able to be loaded
    * Assorted fixes to Blueprint Hologram snapping
    * Fixed being able to save Blueprints with invalid characters in the filename
    * Fixed crash for players who have invalid characters on their session names when attempting to save a blueprint
    * Fixed a crash for [Multiplayer](/wiki/Multiplayer "Multiplayer") Clients or [Dedicated Server](/wiki/Dedicated_Server "Dedicated Server") Clients when placing a Blueprint that has the [AWESOME Sink](/wiki/AWESOME_Sink "AWESOME Sink")
    * Fixed a crash for [Multiplayer](/wiki/Multiplayer "Multiplayer") Clients or [Dedicated Server](/wiki/Dedicated_Server "Dedicated Server") Clients when loading a blueprint before data is properly synced with host
    * Fixed [Multiplayer](/wiki/Multiplayer "Multiplayer") Clients or [Dedicated Server](/wiki/Dedicated_Server "Dedicated Server") Clients Blueprints showing up in Blueprint selection when those Blueprints don’t exist on Server
    * Hopefully improved UX of what directory a Blueprint goes to when loading an old Blueprint or when saving a Blueprint with the same name
  * [Patch 0.7.0.0](/wiki/Patch_0.7.0.0 "Patch 0.7.0.0"): Introduced



## References

  1. ↑ [YouTube - NEW Blueprint features doctors dont want you to know about - Directional Arrow](https://www.youtube.com/watch?v=ZDN_b6TX5gg&t=240s)
  2. ↑ [YouTube - NEW Blueprint features doctors dont want you to know about - Use of Nudge Mode](https://www.youtube.com/watch?v=ZDN_b6TX5gg&t=276s)
  3. ↑ [YouTube - What's in 1.1? - Vertical Nudge Mode](https://www.youtube.com/watch?v=Ty7GdZvCETo&t=518s)
  4. ↑ [YouTube - NEW Blueprint features doctors dont want you to know about - Use of Blueprint Dismantle Mode #1](https://www.youtube.com/watch?v=ZDN_b6TX5gg&t=399s)
  5. ↑ [YouTube - Update 8 Quality Of Life Features will blow your MIND - Dismantle Filter](https://www.youtube.com/watch?v=9jDBEpAlS2s&t=352s)
  6. ↑ [YouTube - Update 8 Quality Of Life Features will blow your MIND - Blueprint Dismantle Filter Type](https://www.youtube.com/watch?v=9jDBEpAlS2s&t=400s)
  7. ↑ [YouTube - NEW Blueprint features doctors dont want you to know about - Use of Blueprint Dismantle Mode #2](https://www.youtube.com/watch?v=ZDN_b6TX5gg&t=460s)
  8. ↑ [YouTube - Update 7 Release Stream (Experimental) - Blueprint Categories and Sub-Categories](https://youtu.be/CREPrQ23Dt4?t=5375)
  9. ↑ [YouTube - What does the NEW machine do in Satisfactory? - Blueprint Save File Locations](https://youtu.be/9KBQyjy-a6g?t=856)
  10. ↑ [YouTube - Blueprint File Save Locations - Update 7 Experimental Release Live Stream - November 15, 2022](https://youtu.be/CREPrQ23Dt4?t=4900)
  11. ↑ [YouTube - What does the NEW machine do in Satisfactory? - Blueprint Cloud Sync Info](https://youtu.be/9KBQyjy-a6g?t=875)
  12. ↑ [YouTube - February 21st, 2023 Livestream - Q&A: Why aren't Blueprints being Cloud Synced?](https://www.youtube.com/watch?v=BLah06-wsGM)
  13. ↑ [YouTube - How to find save game files on Steam Deck (2025)](https://www.youtube.com/watch?v=zqYgPf4u2yc)
  14. ↑ [YouTube - Blueprint File Types - Update 7 Experimental Release Live Stream - November 15, 2022](https://youtu.be/CREPrQ23Dt4?t=6130)
  15. ↑ [Reddit - For blueprints, items in a building input or storage containers will be included when built.](https://www.reddit.com/r/SatisfactoryGame/comments/1hpqelu/til_for_blueprints_items_in_a_building_input_or/)



  * [v](/wiki/Template:BuildingNav "Template:BuildingNav")
  * [e](https://satisfactory.wiki.gg/wiki/Template:BuildingNav?action=edit)
  * [h](https://satisfactory.wiki.gg/wiki/Template:BuildingNav?action=history)

[Buildings](/wiki/Buildings "Buildings")  
---  
Special| [](/wiki/The_HUB "The HUB") [The HUB](/wiki/The_HUB "The HUB") • [](/wiki/MAM "MAM") [MAM](/wiki/MAM "MAM") • [](/wiki/Space_Elevator "Space Elevator") [Space Elevator](/wiki/Space_Elevator "Space Elevator") • [](/wiki/AWESOME_Sink "AWESOME Sink") [AWESOME Sink](/wiki/AWESOME_Sink "AWESOME Sink") • [](/wiki/AWESOME_Shop "AWESOME Shop") [AWESOME Shop](/wiki/AWESOME_Shop "AWESOME Shop") • [](/wiki/Blueprint_Designer "Blueprint Designer") [Blueprint Designer](/wiki/Blueprint_Designer "Blueprint Designer") • [](/wiki/Crafting_Bench "Crafting Bench") [Crafting Bench](/wiki/Crafting_Bench "Crafting Bench") • [](/wiki/Equipment_Workshop "Equipment Workshop") [Equipment Workshop](/wiki/Equipment_Workshop "Equipment Workshop")  
Production| | Extractors| [](/wiki/Miner "Miner") [Miner Mk.1](/wiki/Miner "Miner") ([Mk.2](/wiki/Miner#Mk.2-0 "Miner"), [Mk.3](/wiki/Miner#Mk.3-0 "Miner")) • [](/wiki/Water_Extractor "Water Extractor") [Water Extractor](/wiki/Water_Extractor "Water Extractor") • [](/wiki/Oil_Extractor "Oil Extractor") [Oil Extractor](/wiki/Oil_Extractor "Oil Extractor") • [](/wiki/Resource_Well_Pressurizer "Resource Well Pressurizer") [Resource Well Pressurizer](/wiki/Resource_Well_Pressurizer "Resource Well Pressurizer") ([Extractor](/wiki/Resource_Well_Pressurizer#Extractor "Resource Well Pressurizer"))  
---|---  
Smelters| [](/wiki/Smelter "Smelter") [Smelter](/wiki/Smelter "Smelter") • [](/wiki/Foundry "Foundry") [Foundry](/wiki/Foundry "Foundry")  
Manufacturers| [](/wiki/Constructor "Constructor") [Constructor](/wiki/Constructor "Constructor") • [](/wiki/Assembler "Assembler") [Assembler](/wiki/Assembler "Assembler") • [](/wiki/Manufacturer "Manufacturer") [Manufacturer](/wiki/Manufacturer "Manufacturer") • [](/wiki/Packager "Packager") [Packager](/wiki/Packager "Packager") • [](/wiki/Refinery "Refinery") [Refinery](/wiki/Refinery "Refinery") • [](/wiki/Blender "Blender") [Blender](/wiki/Blender "Blender") • [](/wiki/Particle_Accelerator "Particle Accelerator") [Particle Accelerator](/wiki/Particle_Accelerator "Particle Accelerator") • [](/wiki/Quantum_Encoder "Quantum Encoder") [Quantum Encoder](/wiki/Quantum_Encoder "Quantum Encoder") • [](/wiki/Converter "Converter") [Converter](/wiki/Converter "Converter")  
  
[Power](/wiki/Power "Power")| | Generators| [](/wiki/Biomass_Burner "Biomass Burner") [Biomass Burner](/wiki/Biomass_Burner "Biomass Burner") • [](/wiki/Coal-Powered_Generator "Coal-Powered Generator") [Coal-Powered Generator](/wiki/Coal-Powered_Generator "Coal-Powered Generator") • [](/wiki/Fuel-Powered_Generator "Fuel-Powered Generator") [Fuel-Powered Generator](/wiki/Fuel-Powered_Generator "Fuel-Powered Generator") • [](/wiki/Geothermal_Generator "Geothermal Generator") [Geothermal Generator](/wiki/Geothermal_Generator "Geothermal Generator") • [](/wiki/Nuclear_Power_Plant "Nuclear Power Plant") [Nuclear Power Plant](/wiki/Nuclear_Power_Plant "Nuclear Power Plant") • [](/wiki/Alien_Power_Augmenter "Alien Power Augmenter") [Alien Power Augmenter](/wiki/Alien_Power_Augmenter "Alien Power Augmenter")  
---|---  
Power Grid| [](/wiki/Power_Poles "Power Poles") [Power Poles](/wiki/Power_Poles "Power Poles") • [](/wiki/Wall_Outlets "Wall Outlets") [Wall Outlets](/wiki/Wall_Outlets "Wall Outlets") • [](/wiki/Power_Tower "Power Tower") [Power Tower](/wiki/Power_Tower "Power Tower") • [](/wiki/Power_Line "Power Line") [Power Line](/wiki/Power_Line "Power Line") • [](/wiki/Power_Switch "Power Switch") [Power Switch](/wiki/Power_Switch "Power Switch") • [](/wiki/Priority_Power_Switch "Priority Power Switch") [Priority Power Switch](/wiki/Priority_Power_Switch "Priority Power Switch") • [](/wiki/Power_Storage "Power Storage") [Power Storage](/wiki/Power_Storage "Power Storage")  
  
Logistics| | Conveyors| [](/wiki/Conveyor_Belts "Conveyor Belts") [Conveyor Belts](/wiki/Conveyor_Belts "Conveyor Belts") • [](/wiki/Conveyor_Lift "Conveyor Lift") [Conveyor Lifts](/wiki/Conveyor_Lift "Conveyor Lift") • [](/wiki/Conveyor_Poles "Conveyor Poles") [Conveyor Poles](/wiki/Conveyor_Poles "Conveyor Poles") ([Stackable](/wiki/Conveyor_Poles#Stackable "Conveyor Poles"), [Wall Mount](/wiki/Conveyor_Poles#Mount "Conveyor Poles"), [Ceiling Mount](/wiki/Conveyor_Poles#Ceiling "Conveyor Poles"), {[Wall Hole](/wiki/Conveyor_Poles#Wall_Hole "Conveyor Poles"), [Floor Hole](/wiki/Conveyor_Poles#Floor_Hole "Conveyor Poles")) • [](/wiki/Conveyor_Throughput_Monitor "Conveyor Throughput Monitor") [Conveyor Throughput Monitor](/wiki/Conveyor_Throughput_Monitor "Conveyor Throughput Monitor")  
---|---  
Pipelines| [](/wiki/Pipelines "Pipelines") [Pipelines](/wiki/Pipelines "Pipelines") • [](/wiki/Pipeline_Supports "Pipeline Supports") [Pipeline Supports](/wiki/Pipeline_Supports "Pipeline Supports") ([Stackable](/wiki/Pipeline_Supports#Stackable "Pipeline Supports"), [Wall Support](/wiki/Pipeline_Supports#Wall "Pipeline Supports"), [Wall Hole](/wiki/Pipeline_Supports#Hole "Pipeline Supports"), [Floor Hole](/wiki/Pipeline_Supports#Floor "Pipeline Supports")) • [](/wiki/Pipeline_Junction "Pipeline Junction") [Pipeline Junction](/wiki/Pipeline_Junction "Pipeline Junction") • [](/wiki/Pipeline_Pump "Pipeline Pump") [Pipeline Pumps](/wiki/Pipeline_Pump "Pipeline Pump") • [](/wiki/Valve "Valve") [Valve](/wiki/Valve "Valve")  
Sorting| [](/wiki/Conveyor_Merger "Conveyor Merger") [Conveyor Merger](/wiki/Conveyor_Merger "Conveyor Merger") • [](/wiki/Priority_Merger "Priority Merger") [Priority Merger](/wiki/Priority_Merger "Priority Merger") • [](/wiki/Conveyor_Splitter "Conveyor Splitter") [Conveyor Splitter](/wiki/Conveyor_Splitter "Conveyor Splitter") • [](/wiki/Smart_Splitter "Smart Splitter") [Smart Splitter](/wiki/Smart_Splitter "Smart Splitter") • [](/wiki/Programmable_Splitter "Programmable Splitter") [Programmable Splitter](/wiki/Programmable_Splitter "Programmable Splitter")  
  
Transportation| | [Vehicle Transport](/wiki/Vehicles "Vehicles")| [](/wiki/Tractor "Tractor") [Tractor](/wiki/Tractor "Tractor") • [](/wiki/Truck "Truck") [Truck](/wiki/Truck "Truck") • [](/wiki/Cyber_Wagon "Cyber Wagon") [Cyber Wagon](/wiki/Cyber_Wagon "Cyber Wagon") • [](/wiki/Explorer "Explorer") [Explorer](/wiki/Explorer "Explorer") • [](/wiki/Factory_Cart "Factory Cart") [Factory Cart](/wiki/Factory_Cart "Factory Cart") ([Golden](/wiki/Golden_Factory_Cart "Golden Factory Cart")) • [](/wiki/Truck_Station "Truck Station") [Truck Station](/wiki/Truck_Station "Truck Station") • [](/wiki/Drone_Port "Drone Port") [Drone Port](/wiki/Drone_Port "Drone Port") • [](/wiki/Drone "Drone") [Drone](/wiki/Drone "Drone")  
---|---  
[Railway Transport](/wiki/Trains "Trains")| [](/wiki/Electric_Locomotive "Electric Locomotive") [Electric Locomotive](/wiki/Electric_Locomotive "Electric Locomotive") • [](/wiki/Freight_Car "Freight Car") [Freight Car](/wiki/Freight_Car "Freight Car") • [](/wiki/Train_Station "Train Station") [Train Station](/wiki/Train_Station "Train Station") • [](/wiki/Freight_Platform "Freight Platform") [Freight Platform](/wiki/Freight_Platform "Freight Platform") ([Fluid](/wiki/Freight_Platform#Fluid "Freight Platform")) • [](/wiki/Empty_Platform "Empty Platform") [Empty Platform](/wiki/Empty_Platform "Empty Platform") ([With Catwalk](/wiki/Empty_Platform_With_Catwalk "Empty Platform With Catwalk")) • [](/wiki/Railway "Railway") [Railway](/wiki/Railway "Railway") ([Railroad Switch Control](/wiki/Railroad_Switch_Control "Railroad Switch Control")) • [](/wiki/Buffer_Stop "Buffer Stop") [Buffer Stop](/wiki/Buffer_Stop "Buffer Stop") • [Train Signals](/wiki/Train_Signals "Train Signals") ([](/wiki/Train_Signals#Block "Train Signals") [Block](/wiki/Train_Signals#Block "Train Signals") • [](/wiki/Train_Signals#Path "Train Signals") [Path](/wiki/Train_Signals#Path "Train Signals"))  
Hypertubes| [](/wiki/Hypertube "Hypertube") [Hypertube](/wiki/Hypertube "Hypertube") • [](/wiki/Hypertube_Entrance "Hypertube Entrance") [Hypertube Entrance](/wiki/Hypertube_Entrance "Hypertube Entrance") • [](/wiki/Hypertube_Supports "Hypertube Supports") [Hypertube Supports](/wiki/Hypertube_Supports "Hypertube Supports") ([Stackable](/wiki/Hypertube_Supports#Stackable "Hypertube Supports"), [Wall Support](/wiki/Hypertube_Supports#Wall "Hypertube Supports"), [Wall Hole](/wiki/Hypertube_Supports#Hole "Hypertube Supports"), [Floor Hole](/wiki/Hypertube_Supports#Floor "Hypertube Supports")) • [](/wiki/Hypertube_Junction "Hypertube Junction") [Hypertube Junction](/wiki/Hypertube_Junction "Hypertube Junction") ([Branch](/wiki/Hypertube_Branch "Hypertube Branch"))  
Pioneer Transport| [](/wiki/Jump_Pad "Jump Pad") [Jump Pad](/wiki/Jump_Pad "Jump Pad") • [](/wiki/U-Jelly_Landing_Pad "U-Jelly Landing Pad") [U-Jelly Landing Pad](/wiki/U-Jelly_Landing_Pad "U-Jelly Landing Pad") • [](/wiki/Personnel_Elevator "Personnel Elevator") [Personnel Elevator](/wiki/Personnel_Elevator "Personnel Elevator") • [](/wiki/Portal "Portal") [Portal](/wiki/Portal "Portal") ([Main](/wiki/Main_Portal "Main Portal"), [Satellite](/wiki/Satellite_Portal "Satellite Portal"))  
  
Organization| [](/wiki/Lights "Lights") [Lights](/wiki/Lights "Lights") • [](/wiki/Signs "Signs") [Signs](/wiki/Signs "Signs") • [](/wiki/Crate "Crate") [Crate](/wiki/Crate "Crate") • [](/wiki/Personal_Storage_Box "Personal Storage Box") [Personal Storage Box](/wiki/Personal_Storage_Box "Personal Storage Box") ([Medical](/wiki/Personal_Storage_Box#Medical "Personal Storage Box"), [Hazard](/wiki/Personal_Storage_Box#Hazard "Personal Storage Box")) • [](/wiki/Basic_Shelf_Unit "Basic Shelf Unit") [Basic Shelf Unit](/wiki/Basic_Shelf_Unit "Basic Shelf Unit") • [](/wiki/Storage_Container "Storage Container") [Storage Container](/wiki/Storage_Container "Storage Container") ([Industrial](/wiki/Storage_Container#Industrial "Storage Container")) • [](/wiki/Dimensional_Depot_Uploader "Dimensional Depot Uploader") [Dimensional Depot Uploader](/wiki/Dimensional_Depot_Uploader "Dimensional Depot Uploader") • [](/wiki/Fluid_Buffer "Fluid Buffer") [Fluid Buffer](/wiki/Fluid_Buffer "Fluid Buffer") ([Industrial](/wiki/Fluid_Buffer#Industrial "Fluid Buffer")) • [](/wiki/Lookout_Tower "Lookout Tower") [Lookout Tower](/wiki/Lookout_Tower "Lookout Tower") • [](/wiki/Radar_Tower "Radar Tower") [Radar Tower](/wiki/Radar_Tower "Radar Tower")  
Foundations| [](/wiki/Foundations#Foundations "Foundations") [Foundations](/wiki/Foundations#Foundations "Foundations") • [](/wiki/Foundations#Ramps "Foundations") [Ramps](/wiki/Foundations#Ramps "Foundations") • [](/wiki/Foundations#Inverted_Ramps "Foundations") [Inverted Ramps](/wiki/Foundations#Inverted_Ramps "Foundations") • [](/wiki/Foundations#Quarter-Pipes "Foundations") [Quarter-Pipes](/wiki/Foundations#Quarter-Pipes "Foundations") • [](/wiki/Foundations#Half_Foundations "Foundations") [Half Foundations](/wiki/Foundations#Half_Foundations "Foundations")  
Walls| [](/wiki/Walls#Basic "Walls") [Basic Walls](/wiki/Walls#Basic "Walls") • [](/wiki/Walls#Ramp "Walls") [Ramp Walls](/wiki/Walls#Ramp "Walls") • [](/wiki/Walls#Inverted_Ramp "Walls") [Inverted Ramp Walls](/wiki/Walls#Inverted_Ramp "Walls") • [](/wiki/Walls#Tilted "Walls") [Tilted Walls](/wiki/Walls#Tilted "Walls") • [](/wiki/Walls#Windows "Walls") [Windows](/wiki/Walls#Windows "Walls") • [](/wiki/Walls#Doors "Walls") [Doors](/wiki/Walls#Doors "Walls") • [](/wiki/Walls#Conveyor "Walls") [Conveyor Walls](/wiki/Walls#Conveyor "Walls")  
Architecture| [](/wiki/Frame_Structures "Frame Structures") [Frames](/wiki/Frame_Structures "Frame Structures") • [](/wiki/Roofs "Roofs") [Roofs](/wiki/Roofs "Roofs") • [](/wiki/Beams "Beams") [Beams](/wiki/Beams "Beams") • [](/wiki/Pillars "Pillars") [Pillars](/wiki/Pillars "Pillars") • [](/wiki/Walkways "Walkways") [Walkways](/wiki/Walkways "Walkways") • [](/wiki/Walls "Walls") [Railings](/wiki/Walls "Walls") • [](/wiki/Foundations#Stairs "Foundations") [Stairs](/wiki/Foundations#Stairs "Foundations") • [](/wiki/Ladder "Ladder") [Ladder](/wiki/Ladder "Ladder") • [](/wiki/Large_Fan "Large Fan") [Large Fan](/wiki/Large_Fan "Large Fan") ([Vent](/wiki/Large_Vent "Large Vent"))
  *[v]: View this template
  *[e]: Edit this template
  *[h]: History of this template
