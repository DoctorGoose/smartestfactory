# Patch Closed Alpha 2

Patch notes: **Closed Alpha 2** – Build 89623 – _Rocky Desert_. This version was released on November 23, 2018. The original post came from the Closed Alpha Discord.[1]  
  
## Contents

  * 1 Intro
  * 2 Bug fixes
  * 3 World
  * 4 Progression
  * 5 Performance
  * 6 Quality of Life
  * 7 Manual crafting
  * 8 Main & escape menus
  * 9 Building overhaul
  * 10 Factory buildings
  * 11 UI
  * 12 Resources
  * 13 Enemies
  * 14 Intro sequence
  * 15 Equipment
  * 16 References



## Intro

Hello there, FICSIT Pioneers! 

We've just uploaded the first big update to the closed alpha! You will now start in a new area, the Rocky Desert, be able to build the Space Elevator and advance until Tier 4, which will introduce some new logistical challenges. With this update we have addressed around 60 of your reports with 600+ combined upvotes. So, thank you for providing us with feedback and suggestions! Keep it up and make sure to continue upvoting all the reports that are important to you. 

Enjoy the update! 

## Bug fixes

  * [Portable Miner](/wiki/Portable_Miner "Portable Miner"): 
    * If the player tries to pick it up while having a full inventory, it stays where it is. (Before this the Portable Miner disappeared)
    * Display bug “1 ore per minute” now says “1 ore per second”.
  * Radial Menus: Fixed Radial Menu bugs, where the Radial Menus could remain open when closed, stack up, and freeze the game.
  * VO Message Emails: Game displayed wrong FISCIT email address. Now the correct email @ficsit.biz is used.
  * Walkways: [Walkway Ramps](/wiki/Walkway_Ramp "Walkway Ramp") now snap properly to other Walkways & Foundations.
  * [Building Holograms](/wiki/Construction_Tool "Construction Tool"): The player now blocks the hologram again, so they can't build themselves in anymore.
  * [Rebar Gun](/wiki/Rebar_Gun "Rebar Gun"): Doesn't play its equip sound twice anymore.
  * Disabled the Oculus VR Plugin.
  * [Power Graph](/wiki/Power#Power_grid "Power"): The first point in the power graph is now not mirroring the last point anymore.
  * [Inventory](/wiki/Inventory "Inventory"): Can't drop items anymore between the inventory & character equipment screen.
  * Edibles: Descriptions no longer refer to health in numeric terms.
  * W.A.T. [Milestones](/wiki/Milestone "Milestone"): Fixed icons not showing.
  * [To-Do List](/wiki/To_Do_List "To Do List"): Not visually blocked anymore when using Workshop or Craft Bench.
  * To-Do List (Craft Bench Menu): Fixed focus issue when removing parts from the list.
  * Spawning: [Hotbar](/wiki/Hotbar "Hotbar") notification doesn't show on respawn anymore.
  * [Personal Storage](/wiki/Personal_Storage_Box "Personal Storage Box"): Squished inventory is fixed.
  * All menus: Close button (X) hover over doesn't hide the button anymore.
  * Production Stats: Are rounded now.
  * Standby buttons: Off/on state updating wrong is fixed.
  * Dismantle/death [crate](/wiki/Crate "Crate"): Inventory will not be squished anymore when extremely full.
  * [Purple Slug](/wiki/Purple_Power_Slug "Purple Power Slug"): Renamed Milestone & Research correctly.
  * [M.A.M](/wiki/M.A.M "M.A.M") Menu: Fixed graphical bug that offset the input information.
  * Recording Menu: Fixed a bug where the menu still stated it was recording after the player stopped it.
  * Generators: Now display their stats in the Generator Menu.
  * Equipment Sounds: 
    * Fixed bugs that had equipment idle sounds stuck in a location.
    * Fixed bugs that muted player walking sounds when holding equipment.
  * Building Sounds: Smelter and miner will no longer animate & make sounds when idle.



## World

  * Updated resource locations in and around Rocky Desert starting area.
  * Tweaked and optimised Rocky Desert and adjacent areas. 
    * _Assets:_
      * Tweaked: Pink grass, blue palm trees, holey fern bushes and trees, red/yellow bushes
      * New: Coral cactus
    * _Areas:_
    * West Beach (Following the coast line south of the Rocky Desert)
    * Savannah (North of the Rocky Desert)
    * Crater Lakes (East of the Rocky Desert)
  * Preparation next starting area: Northern Forest. Tweaked and started optimisation of following areas. 
    * Northern Forest (East of Rocky Desert and Crater Lakes)
    * Maze Canyons (East of Northern Forest)
    * Lake Forest (South of Northern Forest)
  * Creature and exploration reward passes for the following areas: 
    * Rocky Desert
    * Savannah
    * Crater Lakes
    * West Beach
  * Added sounds to [Spore Flowers](/wiki/Spore_Flower "Spore Flower").



## Progression

  * Unlocked [Rocky Desert](/wiki/World#Starting_areas "World") starting area (and locked Grass Fields).
  * Unlocking [Tier 4](/wiki/Tier_4 "Tier 4") Milestones.
  * Added [Space Elevator](/wiki/Space_Elevator "Space Elevator"). (Mesh and UI are temporary)
  * VO messages and narrative updates for Tier 4 Milestones.
  * Added beacons to cost of the [Object Scanner](/wiki/Object_Scanner "Object Scanner") and [Tractors](/wiki/Tractor "Tractor").



## Performance

  * Distance field shadow transition tweaks on ultra and high settings.
  * Reduced triangle count and tweaked collision settings on all cliffs.
  * Draw distance tweaks.
  * CSM Shadows & HLODs improvements.



## Quality of Life

  * Shift + click to move entire stacks between inventories.
  * Building [Power Lines](/wiki/Power_Line "Power Line") & [Power Poles](/wiki/Power_Poles "Power Poles"): They can now be built similarly to [Conveyor Belts](/wiki/Conveyor_Belts "Conveyor Belts"). When the player is building power cables, they can either attach them to another building or autobuild a power pole with it.
  * Added functionality for snapping to building guidelines when in build mode. Players can now press CTRL and snap to closeby building guidelines.
  * Ladders can now be climbed down safely. (To climb down approach the ladder backwards)



## Manual crafting

  * Implemented Click based instead of time based manual crafting.
  * Overhaul of the [Craft Bench](/wiki/Craft_Bench "Craft Bench") UI, including FX (sparks and smoke).



## Main & escape menus

  * Options: “Audio, Video, etc.” button fixes. (Only visible on hover-over before, now always visible)
  * Save & Load: Tweaks to make the session/save structure clearer and added a confirm option to deleting saves in the escape menu. 
    * You can't create a new session with existing name anymore and accidentally overwrite your saves.
  * Now verifying that the session name doesn't contain any invalid characters to prevent autosaves from failing.
  * Better error messages when failing to save.



## Building overhaul

  * When a building is being built it now traces from the feet of the building. This means they cannot be built into the landscape anymore. (This doesn't affect buildings being built in foliage or cliffs)
  * Power and conveyor poles foundations now sink a little bit further into the ground. (To prevent floating elements on slopes when building on the landscape)
  * Added a new dismantle material on all buildings.



## Factory buildings

  * Made [splitters](/wiki/Conveyor_Splitter "Conveyor Splitter") and [mergers](/wiki/Conveyor_Merger "Conveyor Merger") smaller.
  * Added new [stackable Conveyor Pole](/wiki/Conveyor_Pole_Stackable "Conveyor Pole Stackable").
  * Added stacking functionality for [Storage Containers](/wiki/Storage_Container "Storage Container").
  * Updated [Conveyor Pole](/wiki/Conveyor_Pole "Conveyor Pole") mesh.
  * Tweaked power loss / power on sounds.
  * Updated SFX for [Hub](/wiki/Hub "Hub") Upgrade & sending the FICSIT Ship.



## UI

  * Fusebox now doesn't cover building UI anymore during a power outage.
  * Added confirmation requirements for exiting to desktop/main menu.
  * Mouse is now automatically centered when opening a menu.
  * [Map](/wiki/Map "Map") shortcut is now hidden before the map has been researched.
  * Added tooltips to all cost slots.
  * Updated ingame feedback form.
  * Updated [Concrete](/wiki/Concrete "Concrete") icon to be more readable.
  * Key quick-reference is now larger.
  * Made [tutorial](/wiki/Tutorial "Tutorial") hints easier to read.
  * [Beacon](/wiki/Beacon "Beacon") name input box tweaks.
  * Added animations to cost slots in the [HUD](/wiki/HUD "HUD") (for example when building).
  * Added Tier selection highlight for completed Tiers.
  * Added confirmation requirement when pressing “Exit to Main Menu” or “Exit to Desktop” in the escape menu.



## Resources

  * Updated [Stone](/wiki/Stone "Stone") and [Coal](/wiki/Coal "Coal") Resource Nodes mesh.
  * Updated Stone and Coal Resource Deposit material.
  * New part mesh for Pigment.



## Enemies

  * [Alpha Hog](/wiki/Alpha_Hog "Alpha Hog") roar behaviour improvements.
  * [Spitter](/wiki/Spitter "Spitter") volley attack now always aims first projectile directly at the target.
  * Added [Baby Crab Hatchers](/wiki/Flying_Crab_Hatcher "Flying Crab Hatcher"). They can be found in and around Rocky Desert and hatch a swarm of flying Baby Crabs that attack the Player. (Spawner is a placeholder asset)
  * Renamed Hog Parts to [Alien Armor Plates](/wiki/Alien_Armor_Plate "Alien Armor Plate").
  * Renamed Spitter Parts to [Alien Organs](/wiki/Alien_Organ "Alien Organ").



## Intro sequence

  * Added intro sequence music.



## Equipment

  * Tweaked sound level for Rebar Gun.
  * Updated Object Scanner sounds and implementation.
  * Sound, animation & VFX tweaks on the [Xeno-Zapper](/wiki/Xeno-Zapper "Xeno-Zapper") (Got rid of idle electricity and implement first-equip animation).



## References

  1. ↑ [Closed Alpha Discord patch notes dump](https://cdn.discordapp.com/attachments/464495516433121281/808312817274978304/Satisfactory_closed_alpha_patch_notes.txt)



  * [v](/wiki/Template:PatchesNav "Template:PatchesNav")
  * [e](https://satisfactory.wiki.gg/wiki/Template:PatchesNav?action=edit)
  * [h](https://satisfactory.wiki.gg/wiki/Template:PatchesNav?action=history)

[Patches](/wiki/Category:Patch_notes "Category:Patch notes")  
---  
1.1| [1.1.1.0](/wiki/Patch_1.1.1.0 "Patch 1.1.1.0") • [1.1.1.1](/wiki/Patch_1.1.1.1 "Patch 1.1.1.1") • [1.1.1.2](/wiki/Patch_1.1.1.2 "Patch 1.1.1.2") • [1.1.1.3](/wiki/Patch_1.1.1.3 "Patch 1.1.1.3") • [1.1.1.4](/wiki/Patch_1.1.1.4 "Patch 1.1.1.4")  
Experimental 1.1| [1.1.0.0](/wiki/Patch_1.1.0.0 "Patch 1.1.0.0") • [1.1.0.1](/wiki/Patch_1.1.0.1 "Patch 1.1.0.1") • [1.1.0.2](/wiki/Patch_1.1.0.2 "Patch 1.1.0.2") • [1.1.0.3](/wiki/Patch_1.1.0.3 "Patch 1.1.0.3") • [1.1.0.4](/wiki/Patch_1.1.0.4 "Patch 1.1.0.4") • [1.1.0.5](/wiki/Patch_1.1.0.5 "Patch 1.1.0.5") • [1.1.0.6](/wiki/Patch_1.1.0.6 "Patch 1.1.0.6") • [1.1.1.5](/wiki/Patch_1.1.1.5 "Patch 1.1.1.5") • [1.1.1.6](/wiki/Patch_1.1.1.6 "Patch 1.1.1.6")  
1.0| [1.0](/wiki/Patch_1.0 "Patch 1.0") • [1.0.0.1](/wiki/Patch_1.0.0.1 "Patch 1.0.0.1") • [1.0.0.2](/wiki/Patch_1.0.0.2 "Patch 1.0.0.2") • [1.0.0.3](/wiki/Patch_1.0.0.3 "Patch 1.0.0.3") • [1.0.0.4](/wiki/Patch_1.0.0.4 "Patch 1.0.0.4") • [1.0.0.5](/wiki/Patch_1.0.0.5 "Patch 1.0.0.5") • [1.0.0.6](/wiki/Patch_1.0.0.6 "Patch 1.0.0.6") • [1.0.0.7](/wiki/Patch_1.0.0.7 "Patch 1.0.0.7") • [1.0.1.0](/wiki/Patch_1.0.1.0 "Patch 1.0.1.0") • [1.0.1.1](/wiki/Patch_1.0.1.1 "Patch 1.0.1.1") • [1.0.1.2](/wiki/Patch_1.0.1.2 "Patch 1.0.1.2") • [1.0.1.3](/wiki/Patch_1.0.1.3 "Patch 1.0.1.3") • [1.0.1.4](/wiki/Patch_1.0.1.4 "Patch 1.0.1.4")  
Experimental 1.0| [1.0.1.5](/wiki/Patch_1.0.1.5 "Patch 1.0.1.5") • [1.0.1.6](/wiki/Patch_1.0.1.6 "Patch 1.0.1.6")  
Update 8| [0.8.3.0](/wiki/Patch_0.8.3.0 "Patch 0.8.3.0") • [0.8.3.2](/wiki/Patch_0.8.3.2 "Patch 0.8.3.2") • [0.8.3.3](/wiki/Patch_0.8.3.3 "Patch 0.8.3.3")  
Experimental Update 8| [0.8.0.0](/wiki/Patch_0.8.0.0 "Patch 0.8.0.0") • [0.8.0.1](/wiki/Patch_0.8.0.1 "Patch 0.8.0.1") • [0.8.0.2](/wiki/Patch_0.8.0.2 "Patch 0.8.0.2") • [0.8.0.3](/wiki/Patch_0.8.0.3 "Patch 0.8.0.3") • [0.8.0.4](/wiki/Patch_0.8.0.4 "Patch 0.8.0.4") • [0.8.0.5](/wiki/Patch_0.8.0.5 "Patch 0.8.0.5") • [0.8.1.0](/wiki/Patch_0.8.1.0 "Patch 0.8.1.0") • [0.8.1.1](/wiki/Patch_0.8.1.1 "Patch 0.8.1.1") • [0.8.1.2](/wiki/Patch_0.8.1.2 "Patch 0.8.1.2") • [0.8.1.3](/wiki/Patch_0.8.1.3 "Patch 0.8.1.3") • [0.8.2.0](/wiki/Patch_0.8.2.0 "Patch 0.8.2.0") • [0.8.2.1](/wiki/Patch_0.8.2.1 "Patch 0.8.2.1") • [0.8.2.2](/wiki/Patch_0.8.2.2 "Patch 0.8.2.2") • [0.8.2.3](/wiki/Patch_0.8.2.3 "Patch 0.8.2.3") • [0.8.2.4](/wiki/Patch_0.8.2.4 "Patch 0.8.2.4") • [0.8.2.5](/wiki/Patch_0.8.2.5 "Patch 0.8.2.5") • [0.8.2.6](/wiki/Patch_0.8.2.6 "Patch 0.8.2.6") • [0.8.2.7](/wiki/Patch_0.8.2.7 "Patch 0.8.2.7") • [0.8.2.8](/wiki/Patch_0.8.2.8 "Patch 0.8.2.8") • [0.8.2.9](/wiki/Patch_0.8.2.9 "Patch 0.8.2.9") • [0.8.3.1](/wiki/Patch_0.8.3.1 "Patch 0.8.3.1")  
Update 7| [0.7.0.8](/wiki/Patch_0.7.0.8 "Patch 0.7.0.8") • [0.7.1.1](/wiki/Patch_0.7.1.1 "Patch 0.7.1.1")  
Experimental Update 7| [0.7.0.0](/wiki/Patch_0.7.0.0 "Patch 0.7.0.0") • [0.7.0.1](/wiki/Patch_0.7.0.1 "Patch 0.7.0.1") • [0.7.0.2](/wiki/Patch_0.7.0.2 "Patch 0.7.0.2") • [0.7.0.3](/wiki/Patch_0.7.0.3 "Patch 0.7.0.3") • [0.7.0.4](/wiki/Patch_0.7.0.4 "Patch 0.7.0.4") • [0.7.0.5](/wiki/Patch_0.7.0.5 "Patch 0.7.0.5") • [0.7.0.6](/wiki/Patch_0.7.0.6 "Patch 0.7.0.6") • [0.7.0.7](/wiki/Patch_0.7.0.7 "Patch 0.7.0.7") • [0.7.0.8 (Experimental)](/wiki/Patch_0.7.0.8_\(Experimental\) "Patch 0.7.0.8 \(Experimental\)")  
Update 6| [0.6.1.0](/wiki/Patch_0.6.1.0 "Patch 0.6.1.0") • [0.6.1.1](/wiki/Patch_0.6.1.1 "Patch 0.6.1.1") • [0.6.1.2](/wiki/Patch_0.6.1.2 "Patch 0.6.1.2") • [0.6.1.3](/wiki/Patch_0.6.1.3 "Patch 0.6.1.3") • [0.6.1.4](/wiki/Patch_0.6.1.4 "Patch 0.6.1.4") • [0.6.1.5](/wiki/Patch_0.6.1.5 "Patch 0.6.1.5")  
Experimental Update 6| [0.6.0.0](/wiki/Patch_0.6.0.0 "Patch 0.6.0.0") • [0.6.0.1](/wiki/Patch_0.6.0.1 "Patch 0.6.0.1") • [0.6.0.2](/wiki/Patch_0.6.0.2 "Patch 0.6.0.2") • [0.6.0.3](/wiki/Patch_0.6.0.3 "Patch 0.6.0.3") • [0.6.0.4](/wiki/Patch_0.6.0.4 "Patch 0.6.0.4") • [0.6.0.5](/wiki/Patch_0.6.0.5 "Patch 0.6.0.5") • [0.6.0.6](/wiki/Patch_0.6.0.6 "Patch 0.6.0.6") • [0.6.0.7](/wiki/Patch_0.6.0.7 "Patch 0.6.0.7") • [0.6.0.8](/wiki/Patch_0.6.0.8 "Patch 0.6.0.8") • [0.6.0.9](/wiki/Patch_0.6.0.9 "Patch 0.6.0.9") • [0.6.0.10](/wiki/Patch_0.6.0.10 "Patch 0.6.0.10") • [0.6.0.11](/wiki/Patch_0.6.0.11 "Patch 0.6.0.11") • [0.6.0.12](/wiki/Patch_0.6.0.12 "Patch 0.6.0.12") • [0.6.0.13](/wiki/Patch_0.6.0.13 "Patch 0.6.0.13") • [0.6.0.14](/wiki/Patch_0.6.0.14 "Patch 0.6.0.14") • [0.6.0.15](/wiki/Patch_0.6.0.15 "Patch 0.6.0.15")  
Update 5| [0.5.1.0](/wiki/Patch_0.5.1.0 "Patch 0.5.1.0") • [0.5.1.1](/wiki/Patch_0.5.1.1 "Patch 0.5.1.1") • [0.5.1.3](/wiki/Patch_0.5.1.3 "Patch 0.5.1.3") • [0.5.1.4](/wiki/Patch_0.5.1.4 "Patch 0.5.1.4") • [0.5.1.5](/wiki/Patch_0.5.1.5 "Patch 0.5.1.5") • [0.5.1.7](/wiki/Patch_0.5.1.7 "Patch 0.5.1.7") • [0.5.1.8](/wiki/Patch_0.5.1.8 "Patch 0.5.1.8") • [0.5.1.10](/wiki/Patch_0.5.1.10 "Patch 0.5.1.10") • [0.5.2.0](/wiki/Patch_0.5.2.0 "Patch 0.5.2.0") • [0.5.2.1](/wiki/Patch_0.5.2.1 "Patch 0.5.2.1")  
Experimental Update 5| [0.5.0.0](/wiki/Patch_0.5.0.0 "Patch 0.5.0.0") • [0.5.0.1](/wiki/Patch_0.5.0.1 "Patch 0.5.0.1") • [0.5.0.2](/wiki/Patch_0.5.0.2 "Patch 0.5.0.2") • [0.5.0.3](/wiki/Patch_0.5.0.3 "Patch 0.5.0.3") • [0.5.0.4](/wiki/Patch_0.5.0.4 "Patch 0.5.0.4") • [0.5.0.5](/wiki/Patch_0.5.0.5 "Patch 0.5.0.5") • [0.5.0.6](/wiki/Patch_0.5.0.6 "Patch 0.5.0.6") • [0.5.0.7](/wiki/Patch_0.5.0.7 "Patch 0.5.0.7") • [0.5.0.8](/wiki/Patch_0.5.0.8 "Patch 0.5.0.8") • [0.5.0.9](/wiki/Patch_0.5.0.9 "Patch 0.5.0.9") • [0.5.0.10](/wiki/Patch_0.5.0.10 "Patch 0.5.0.10") • [0.5.0.11](/wiki/Patch_0.5.0.11 "Patch 0.5.0.11") • [0.5.0.12](/wiki/Patch_0.5.0.12 "Patch 0.5.0.12") • [0.5.0.13](/wiki/Patch_0.5.0.13 "Patch 0.5.0.13") • [0.5.0.14](/wiki/Patch_0.5.0.14 "Patch 0.5.0.14") • [0.5.1.2](/wiki/Patch_0.5.1.2 "Patch 0.5.1.2") • [0.5.1.6](/wiki/Patch_0.5.1.6 "Patch 0.5.1.6") • [0.5.1.9](/wiki/Patch_0.5.1.9 "Patch 0.5.1.9") • [0.5.1.11](/wiki/Patch_0.5.1.11 "Patch 0.5.1.11") • [0.5.1.12](/wiki/Patch_0.5.1.12 "Patch 0.5.1.12") • [0.5.1.13](/wiki/Patch_0.5.1.13 "Patch 0.5.1.13")  
Update 4| [0.4.1.0](/wiki/Patch_0.4.1.0 "Patch 0.4.1.0") • [0.4.1.1](/wiki/Patch_0.4.1.1 "Patch 0.4.1.1") • [0.4.2.0](/wiki/Patch_0.4.2.0 "Patch 0.4.2.0") • [0.4.2.2](/wiki/Patch_0.4.2.2 "Patch 0.4.2.2") • [0.4.2.5](/wiki/Patch_0.4.2.5 "Patch 0.4.2.5") • [0.4.2.7](/wiki/Patch_0.4.2.7 "Patch 0.4.2.7") • [0.4.2.9](/wiki/Patch_0.4.2.9 "Patch 0.4.2.9") • [0.4.2.11](/wiki/Patch_0.4.2.11 "Patch 0.4.2.11")  
Experimental Update 4| [0.4.0.0](/wiki/Patch_0.4.0.0 "Patch 0.4.0.0") • [0.4.0.1](/wiki/Patch_0.4.0.1 "Patch 0.4.0.1") • [0.4.0.2](/wiki/Patch_0.4.0.2 "Patch 0.4.0.2") • [0.4.0.3](/wiki/Patch_0.4.0.3 "Patch 0.4.0.3") • [0.4.0.4](/wiki/Patch_0.4.0.4 "Patch 0.4.0.4") • [0.4.0.5](/wiki/Patch_0.4.0.5 "Patch 0.4.0.5") • [0.4.0.6](/wiki/Patch_0.4.0.6 "Patch 0.4.0.6") • [0.4.0.7](/wiki/Patch_0.4.0.7 "Patch 0.4.0.7") • [0.4.0.8](/wiki/Patch_0.4.0.8 "Patch 0.4.0.8") • [0.4.0.9](/wiki/Patch_0.4.0.9 "Patch 0.4.0.9") • [0.4.0.10](/wiki/Patch_0.4.0.10 "Patch 0.4.0.10") • [0.4.0.11](/wiki/Patch_0.4.0.11 "Patch 0.4.0.11") • [0.4.0.12](/wiki/Patch_0.4.0.12 "Patch 0.4.0.12") • [0.4.2.1](/wiki/Patch_0.4.2.1 "Patch 0.4.2.1") • [0.4.2.2 (Experimental)](/wiki/Patch_0.4.2.2_\(Experimental\) "Patch 0.4.2.2 \(Experimental\)") • [0.4.2.3](/wiki/Patch_0.4.2.3 "Patch 0.4.2.3") • [0.4.2.4](/wiki/Patch_0.4.2.4 "Patch 0.4.2.4") • [0.4.2.6](/wiki/Patch_0.4.2.6 "Patch 0.4.2.6") • [0.4.2.8](/wiki/Patch_0.4.2.8 "Patch 0.4.2.8") • [0.4.2.10](/wiki/Patch_0.4.2.10 "Patch 0.4.2.10") • [0.4.3.0](/wiki/Patch_0.4.3.0 "Patch 0.4.3.0") • [0.4.3.1](/wiki/Patch_0.4.3.1 "Patch 0.4.3.1")  
Update 3  
& Steam Release| [0.3.3.3](/wiki/Patch_0.3.3.3 "Patch 0.3.3.3") • [0.3.3.4](/wiki/Patch_0.3.3.4 "Patch 0.3.3.4") • [0.3.3.5](/wiki/Patch_0.3.3.5 "Patch 0.3.3.5") • [0.3.3.6](/wiki/Patch_0.3.3.6 "Patch 0.3.3.6") • [0.3.4.14](/wiki/Patch_0.3.4.14 "Patch 0.3.4.14") • [0.3.4.15](/wiki/Patch_0.3.4.15 "Patch 0.3.4.15") • [0.3.4.16](/wiki/Patch_0.3.4.16 "Patch 0.3.4.16") • [0.3.5](/wiki/Patch_0.3.5 "Patch 0.3.5") • [0.3.5.1](/wiki/Patch_0.3.5.1 "Patch 0.3.5.1") • [0.3.5.2](/wiki/Patch_0.3.5.2 "Patch 0.3.5.2") • [0.3.5.3](/wiki/Patch_0.3.5.3 "Patch 0.3.5.3") • [0.3.5.4](/wiki/Patch_0.3.5.4 "Patch 0.3.5.4") • [0.3.5.6](/wiki/Patch_0.3.5.6 "Patch 0.3.5.6") • [0.3.6.5](/wiki/Patch_0.3.6.5 "Patch 0.3.6.5") • [0.3.7](/wiki/Patch_0.3.7 "Patch 0.3.7") • [0.3.7.1](/wiki/Patch_0.3.7.1 "Patch 0.3.7.1") • [0.3.7.2](/wiki/Patch_0.3.7.2 "Patch 0.3.7.2") • [0.3.7.3](/wiki/Patch_0.3.7.3 "Patch 0.3.7.3") • [0.3.7.4](/wiki/Patch_0.3.7.4 "Patch 0.3.7.4") • [0.3.7.5](/wiki/Patch_0.3.7.5 "Patch 0.3.7.5") • [0.3.7.6](/wiki/Patch_0.3.7.6 "Patch 0.3.7.6") • [0.3.7.7](/wiki/Patch_0.3.7.7 "Patch 0.3.7.7")  
Experimental Update 3  
& Steam Release| [0.3](/wiki/Patch_0.3 "Patch 0.3") • [0.3.0.1](/wiki/Patch_0.3.0.1 "Patch 0.3.0.1") • [0.3.0.2](/wiki/Patch_0.3.0.2 "Patch 0.3.0.2") • [0.3.1.0](/wiki/Patch_0.3.1.0 "Patch 0.3.1.0") • [0.3.1.1](/wiki/Patch_0.3.1.1 "Patch 0.3.1.1") • [0.3.1.2](/wiki/Patch_0.3.1.2 "Patch 0.3.1.2") • [0.3.2.0](/wiki/Patch_0.3.2.0 "Patch 0.3.2.0") • [0.3.2.1](/wiki/Patch_0.3.2.1 "Patch 0.3.2.1") • [0.3.2.2](/wiki/Patch_0.3.2.2 "Patch 0.3.2.2") • [0.3.3.0](/wiki/Patch_0.3.3.0 "Patch 0.3.3.0") • [0.3.3.1](/wiki/Patch_0.3.3.1 "Patch 0.3.3.1") • [0.3.3.2](/wiki/Patch_0.3.3.2 "Patch 0.3.3.2") • [0.3.3.4](/wiki/Patch_0.3.3.4 "Patch 0.3.3.4") • [0.3.3.5](/wiki/Patch_0.3.3.5 "Patch 0.3.3.5") • [0.3.4.0](/wiki/Patch_0.3.4.0 "Patch 0.3.4.0") • [0.3.4.1](/wiki/Patch_0.3.4.1 "Patch 0.3.4.1") • [0.3.4.2](/wiki/Patch_0.3.4.2 "Patch 0.3.4.2") • [0.3.4.3](/wiki/Patch_0.3.4.3 "Patch 0.3.4.3") • [0.3.4.4](/wiki/Patch_0.3.4.4 "Patch 0.3.4.4") • [0.3.4.5](/wiki/Patch_0.3.4.5 "Patch 0.3.4.5") • [0.3.4.6](/wiki/Patch_0.3.4.6 "Patch 0.3.4.6") • [0.3.4.7](/wiki/Patch_0.3.4.7 "Patch 0.3.4.7") • [0.3.4.8](/wiki/Patch_0.3.4.8 "Patch 0.3.4.8") • [0.3.4.9](/wiki/Patch_0.3.4.9 "Patch 0.3.4.9") • [0.3.4.10](/wiki/Patch_0.3.4.10 "Patch 0.3.4.10") • [0.3.4.11](/wiki/Patch_0.3.4.11 "Patch 0.3.4.11") • [0.3.4.12](/wiki/Patch_0.3.4.12 "Patch 0.3.4.12") • [0.3.4.13](/wiki/Patch_0.3.4.13 "Patch 0.3.4.13") • [0.3.5.5](/wiki/Patch_0.3.5.5 "Patch 0.3.5.5") • [0.3.6](/wiki/Patch_0.3.6 "Patch 0.3.6") • [0.3.6.1](/wiki/Patch_0.3.6.1 "Patch 0.3.6.1") • [0.3.6.2](/wiki/Patch_0.3.6.2 "Patch 0.3.6.2") • [0.3.6.3](/wiki/Patch_0.3.6.3 "Patch 0.3.6.3") • [0.3.6.4](/wiki/Patch_0.3.6.4 "Patch 0.3.6.4") • [0.3.6.6](/wiki/Patch_0.3.6.6 "Patch 0.3.6.6") • [0.3.6.7](/wiki/Patch_0.3.6.7 "Patch 0.3.6.7") • [0.3.6.8](/wiki/Patch_0.3.6.8 "Patch 0.3.6.8") • [0.3.6.9](/wiki/Patch_0.3.6.9 "Patch 0.3.6.9") • [0.3.6.10](/wiki/Patch_0.3.6.10 "Patch 0.3.6.10") • [0.3.6.11](/wiki/Patch_0.3.6.11 "Patch 0.3.6.11") • [0.3.6.12](/wiki/Patch_0.3.6.12 "Patch 0.3.6.12") • [0.3.6.13](/wiki/Patch_0.3.6.13 "Patch 0.3.6.13") • [0.3.8.0](/wiki/Patch_0.3.8.0 "Patch 0.3.8.0") • [0.3.8.1](/wiki/Patch_0.3.8.1 "Patch 0.3.8.1") • [0.3.8.2](/wiki/Patch_0.3.8.2 "Patch 0.3.8.2") • [0.3.8.3](/wiki/Patch_0.3.8.3 "Patch 0.3.8.3") • [0.3.8.4](/wiki/Patch_0.3.8.4 "Patch 0.3.8.4") • [0.3.8.5](/wiki/Patch_0.3.8.5 "Patch 0.3.8.5") • [0.3.8.6](/wiki/Patch_0.3.8.6 "Patch 0.3.8.6") • [0.3.8.7](/wiki/Patch_0.3.8.7 "Patch 0.3.8.7") • [0.3.8.8](/wiki/Patch_0.3.8.8 "Patch 0.3.8.8") • [0.3.8.9](/wiki/Patch_0.3.8.9 "Patch 0.3.8.9") • [0.3.8.10](/wiki/Patch_0.3.8.10 "Patch 0.3.8.10") • [0.3.8.11](/wiki/Patch_0.3.8.11 "Patch 0.3.8.11")  
Update 2| [0.2.1](/wiki/Patch_0.2.1 "Patch 0.2.1") • [0.2.1.1](/wiki/Patch_0.2.1.1 "Patch 0.2.1.1") • [0.2.1.2](/wiki/Patch_0.2.1.2 "Patch 0.2.1.2") • [0.2.1.3](/wiki/Patch_0.2.1.3 "Patch 0.2.1.3") • [ 0.2.1.4](/wiki/Patch_0.2.1.4 "Patch 0.2.1.4") • [ 0.2.1.5](/wiki/Patch_0.2.1.5 "Patch 0.2.1.5") • [0.2.1.7](/wiki/Patch_0.2.1.7 "Patch 0.2.1.7") • [0.2.1.10](/wiki/Patch_0.2.1.10 "Patch 0.2.1.10") • [0.2.1.12](/wiki/Patch_0.2.1.12 "Patch 0.2.1.12") • [0.2.1.17](/wiki/Patch_0.2.1.17 "Patch 0.2.1.17") • [0.2.1.18](/wiki/Patch_0.2.1.18 "Patch 0.2.1.18")  
Experimental Update 2| [0.1.14](/wiki/Patch_0.1.14 "Patch 0.1.14") • [0.1.15](/wiki/Patch_0.1.15 "Patch 0.1.15") • [0.1.16](/wiki/Patch_0.1.16 "Patch 0.1.16") • [0.1.17 (101256)](/wiki/Patch_0.1.17 "Patch 0.1.17") • [0.1.17 (101353)](/wiki/Patch_0.1.17_build_101353 "Patch 0.1.17 build 101353") • [0.1.19](/wiki/Patch_0.1.19 "Patch 0.1.19") • [0.1.20](/wiki/Patch_0.1.20 "Patch 0.1.20") • [0.2.1.6](/wiki/Patch_0.2.1.6 "Patch 0.2.1.6") • [0.2.1.7 (Experimental)](/wiki/Patch_0.2.1.7_\(Experimental\) "Patch 0.2.1.7 \(Experimental\)") • [0.2.1.8](/wiki/Patch_0.2.1.8 "Patch 0.2.1.8") • [0.2.1.9](/wiki/Patch_0.2.1.9 "Patch 0.2.1.9") • [0.2.1.11](/wiki/Patch_0.2.1.11 "Patch 0.2.1.11") • [0.2.1.12 (Experimental)](/wiki/Patch_0.2.1.12_\(Experimental\) "Patch 0.2.1.12 \(Experimental\)") • [0.2.1.13](/wiki/Patch_0.2.1.13 "Patch 0.2.1.13") • [0.2.1.14](/wiki/Patch_0.2.1.14 "Patch 0.2.1.14") • [0.2.1.15](/wiki/Patch_0.2.1.15 "Patch 0.2.1.15") • [0.2.1.16](/wiki/Patch_0.2.1.16 "Patch 0.2.1.16") • [0.2.1.17 (Experimental)](/wiki/Patch_0.2.1.17_\(Experimental\) "Patch 0.2.1.17 \(Experimental\)") • [0.2.1.19](/wiki/Patch_0.2.1.19 "Patch 0.2.1.19") • [0.2.1.20](/wiki/Patch_0.2.1.20 "Patch 0.2.1.20")  
Update 1| [0.1.11](/wiki/Patch_0.1.11 "Patch 0.1.11") • [0.1.12](/wiki/Patch_0.1.12 "Patch 0.1.12") • [0.1.13](/wiki/Patch_0.1.13 "Patch 0.1.13")  
Experimental Update 1| [0.1.5](/wiki/Patch_0.1.5 "Patch 0.1.5") • [0.1.6 (98394)](/wiki/Patch_0.1.6_build_98394 "Patch 0.1.6 build 98394") • [0.1.6 (98445)](/wiki/Patch_0.1.6_build_98445 "Patch 0.1.6 build 98445") • [0.1.7](/wiki/Patch_0.1.7 "Patch 0.1.7") • [0.1.8](/wiki/Patch_0.1.8 "Patch 0.1.8") • [0.1.9](/wiki/Patch_0.1.9 "Patch 0.1.9") • [0.1.10](/wiki/Patch_0.1.10 "Patch 0.1.10")  
Early Access Release| [0.1](/wiki/Patch_0.1 "Patch 0.1") • [0.101](/wiki/Patch_0.101 "Patch 0.101") • [0.102](/wiki/Patch_0.102 "Patch 0.102") • [0.103](/wiki/Patch_0.103 "Patch 0.103") • [0.104](/wiki/Patch_0.104 "Patch 0.104")  
Closed Alpha| [Early game development](/wiki/Early_game_development "Early game development") • [2018-10-11](/wiki/Patch_2018-10-11 "Patch 2018-10-11") • [2018-10-17](/wiki/Patch_2018-10-17 "Patch 2018-10-17") • [2018-10-19](/wiki/Patch_2018-10-19 "Patch 2018-10-19") • [2018-10-27](/wiki/Patch_2018-10-27 "Patch 2018-10-27") • 2 • [2.1](/wiki/Patch_Closed_Alpha_2.1 "Patch Closed Alpha 2.1") • [3](/wiki/Patch_Closed_Alpha_3 "Patch Closed Alpha 3") • [3.1](/wiki/Patch_Closed_Alpha_3.1 "Patch Closed Alpha 3.1") • [3.2](/wiki/Patch_Closed_Alpha_3.2 "Patch Closed Alpha 3.2") • [4](/wiki/Patch_Closed_Alpha_4 "Patch Closed Alpha 4") • [4.1](/wiki/Patch_Closed_Alpha_4.1 "Patch Closed Alpha 4.1") • [Alpha Test Weekend](/wiki/Alpha_Test_Weekend "Alpha Test Weekend") • [5](/wiki/Patch_Closed_Alpha_5 "Patch Closed Alpha 5") • [5.1](/wiki/Patch_Closed_Alpha_5.1 "Patch Closed Alpha 5.1") • [5.3](/wiki/Patch_Closed_Alpha_5.3 "Patch Closed Alpha 5.3")
  *[v]: View this template
  *[e]: Edit this template
  *[h]: History of this template
  *[his]: his trivia section
