# Future content/Archive Update 5

_This page is an archive of past versions of the current page._

_The contents are kept for reference purposes only, and should be preserved in their current form. Do not add new comments here or edit this page._

## Contents

  * 1 Release date
  * 2 Summary
  * 3 Buildings
  * 4 World
  * 5 Gameplay
  * 6 Vehicles
    * 6.1 Motor vehicles
    * 6.2 Trains
  * 7 References



## Release date

**October 26, 2021, 6pm CEST**

Update 5 is planned to release on the Experimental branch on October 26, 2021, as revealed in a video uploaded on September 24, 2021.[U5 1] On the October 19, 2021 Dev Stream, it was further clarified that Update 5 is planned to release at 6pm CEST (16:00 UTC October 26, 2021).[U5 2] A general release window of fall 2021 was confirmed earlier.[U5 3]

On the January 26, 2021, Dev Stream, it was revealed that Update 5 is planned and could be the last major update until 1.0.[U5 4]

Feature teasers or informational videos are expected to be uploaded weekly, in a similar fashion to Update 4.[U5 5]

## Summary

  * Northern Forest overhaul, with new foliage but little to no terrain changes
  * Dune Desert minor terrain changes
  * Added many cosmetic structures, including roofs and beams, new wall, window, pillar and fence variants and walkways
  * Mass-build mode named Zooping, that allows up to 10 wall or floor structures to be built in a row (excluding factory machines or logistic structures)[U5 6]
  * Separation of clearance into soft and hard, allowing structures with soft clearance (e.g. Conveyor Belts) to be built freely through each other and structures with hard clearance (factory buildings)
  * Major improvements to motor vehicle automation, pre-calculated fuel consumption, better pathing system using splines, more reliable object avoidance with ghosting, copying and pasting recorded vehicle paths and a new Truck Station with 2 input and 2 output ports
  * Train signaling (using Block and Path Signals) and collisions, ability to set loaded and unloaded cargo type in Train Stations and set a wait duration and/or wait until full
  * Unreal Engine upgrade to 4.26, option to use DirectX 12 or Vulkan instead of the default DirectX 11



## Buildings

New buildings and structures were introduced by a dev vlog uploaded on September 3, 2021.[U5 7] The features include: 

  * New category in the build menu [`Q`](/wiki/Controls "Controls"): **Architecture**
    * It contains 6 sub-categories: Frames, Roofs, Beams, Pillars, Attachments, and Walkways
  * New buildings: 
    * Small Pillar 
      * Size 4x4m, come with 3 varieties: Concrete, Metal, Frame for the middle pillar, with Small Pillar Base and Small Pillar Top
    * Large Pillar 
      * Now with 2 more varieties: Concrete and Frame
      * Now renamed to Pillar Base, (*name of material) Pillar, Pillar Top 
        * Pillar Base with protruding pillar part trimmed for seamless construction.
    * Fence 
      * New varieties added: Railing and Barrier 
        * Can be Quick Switched [`E`](/wiki/Controls "Controls")
      * Is now 4 meters long on horizontal foundation edges and 8 meters long on slopes
      * Automatically switches to the sloped variant when placed on a slope
    * Roof 
      * New material: Glass Roof, Metal Roof, FICSIT Roof
      * Varieties of slopes: Flat roof, Roof 1m, 2m, and 4m
    * Wall 
      * New material: Wall Frame
      * New windows: Window Thin 8m x 4m 01 (Full Glass), Window Thin 8m x 4m 02 (Glass with thin hexagonal frame)
      * Angular Walls: 8m x 1m, 8m x 2m, 8m x 4m, 8m x 8m 
        * Resemble a roof piece
      * Diagonal Wall: 1m, 2m, 4m, 8m 
        * Match ramps of the same height
      * Shorter Wall: Basic Orange Wall 1m, the default 4m Wall is renamed to Basic Orange Wall
    * Foundations 
      * New variants: Inverted Ramps
      * Now needs Iron Plates to be constructed
    * Beams 
      * Beam Horizontal, Beam Connector
      * Beam Horizontal can be built between 2 points, similar to Power Lines
    * Walkways 
      * Visually changed
      * Renamed to Catwalks



## World

[](/wiki/File:Biome_changes_in_U5.png)

[](/wiki/File:Biome_changes_in_U5.png "Enlarge")

Biome changes in Update 5

[](/wiki/File:Biome_changes_U5_through_release.png)

[](/wiki/File:Biome_changes_U5_through_release.png "Enlarge")

Biome changes from Update 5 onward

On July 31, 2021, a before/after [video](https://youtu.be/2-JM_JP8RNc) of the [Northern Forest](/wiki/Northern_Forest "Northern Forest") was uploaded. It includes new vegetation, prominent pine trees, harvestables, a previously-unseen cave design and more. The terrain changes are minimal, meaning that after the update, only (destructible) trees will reappear, and span the entirety of the Northern Forest, Maze Canyons and Lake Forest.[U5 5]

The Dune Desert will receive minor changes, but are landscape-based. The changes affect the "wall" separating the Spire Coast, making it less barren, dunes in the north-eastern part of the biome, where a crater will now be, the eastern portion with minor changes, and a prominent large rock in the middle of the Dune Desert.[U5 5]

The changes to these two biomes are considered final with no plans to change them until at least 1.0.[U5 5]

Caves all around the world will be overhauled with a brand new look, initially seen in the Northern Forest teaser. By the update's release, not all caves will be done. The intent is to unify caves as they are considered a biome as well.[U5 5]

In one tweet by the official Satisfactory account, it was vaguely teased that Update 5 will have something to do with exploration.[U5 8]

## Gameplay

Build modes were teased in a video uploaded one June 18, 2021, explaining it means building will become easier.[U5 9] A group build mode named Zooping was introduced in a video from September 9, 2021. It allows foundations, ramps, walls, roofs, fences/railings, pillars and beams to be mass constructed in a row of ten. It is enabled by pressing [`R`](/wiki/Controls "Controls") while in Build Mode.[U5 7] Zooping will work horizontally and vertically, it also allows for the placement of multiple stackable poles at the same time.[U5 10] Zooping was named for the onomatopoeia made by game director Mark when building [Ladders](/wiki/Ladder "Ladder").[U5 11][U5 12]

Building encroachment will be separated into Soft and Hard Clearance. All buildings with functionality (production buildings, resource extractors, power generators, [Power Switches](/wiki/Power_Switch "Power Switch"), [Power Poles](/wiki/Power_Poles "Power Poles"), [The HUB](/wiki/The_HUB "The HUB"), [MAM](/wiki/MAM "MAM"), etc.) will have Hard Clearance, while factory buildables and cosmetic building pieces, as well as Conveyor Belts and Pipelines will have Soft Clearance.[U5 13][U5 14] Buildings with Hard Clearance cannot intersect each other in any way, but buildings with Soft Clearance can intersect each other and buildings with Hard Clearance. Some buildings with hard clearance will also get complex clearance, allowing buildings with hard clearance to be built within the hitbox.[U5 15] This allows, for example, Walkways or Pipelines to be built through the [Coal Generator](/wiki/Coal_Generator "Coal Generator")'s tall boundary due to its chimney, or Conveyor Belts to go through the [Particle Accelerator](/wiki/Particle_Accelerator "Particle Accelerator").[U5 7] The shortcuts bar has got 2 new icons, one icon is for the quick search bar/calculator, the other is for an unknown feature, it has the icon of a paint brush. Pillars can now be built and snapped to [Railways](/wiki/Railway "Railway") allowing them to act as supports. Walkways, renamed to Catwalks, now snap to machines where the pioneer can walk, for example the top of the [Constructor](/wiki/Constructor "Constructor").[U5 16] Placing foundations while snapping to other foundations will also be easier with the ability to rotate in increments of 45°, even smaller increments are achievable when holding [`Ctrl`](/wiki/Controls "Controls").[U5 17] Stairs are now not locked to specific angles while snapping to each other.[U5 18] It will also now be possible to build ramps diagonally without the use of foundations or double ramps, the zoop build mode will also be able to do this.[U5 19] [Conveyor Belts](/wiki/Conveyor_Belt "Conveyor Belt") will now snap to inputs and outputs of machines, while building [Conveyor Splitters](/wiki/Conveyor_Splitter "Conveyor Splitter"), [Conveyor Mergers](/wiki/Conveyor_Merger "Conveyor Merger") and [Pipeline Junction Crosses](/wiki/Pipeline_Junction_Cross "Pipeline Junction Cross") off of existing [Pipelines](/wiki/Pipeline "Pipeline") or [Conveyor Belts](/wiki/Conveyor_Belt "Conveyor Belt") they will also snap to machine inputs and outputs.[U5 20] While building [Conveyor Belts](/wiki/Conveyor_Belt "Conveyor Belt") you will also be able to snap to the origin of the belt, allowing for straight belts without foundations.[U5 21] Hologram colors can now be changed independently.[U5 22]

## Vehicles

### Motor vehicles

Motor vehicle automation will receive major improvements.[U5 23]

  * The [Truck Station](/wiki/Truck_Station "Truck Station") will have 2 inputs and 2 outputs, a more clearly labelled fuel input, and new UI 
    * Now displays fuel consumption per minute, maximum throughput and actual throughput (transfer rate)
  * Vehicles will follow recorded paths better as smooth splines will be made between each point (in the current system, vehicles drive straight to the next point, ignoring other points and not turning smoothly)
  * If a vehicle gets stuck on its route, it may 'ghost' (phase through terrain and structures) where it needs to go
  * Fuel consumption will be pre-calculated for the whole round trip 
    * Vehicles will not depart from the Truck Station until enough fuel is provided
    * Should the vehicle get stuck on the route, it will not consume any more fuel than it was calculated to use
    * It appears the required fuel is calculated in MJ, allowing [Nuclear Fuel Rods](/wiki/Nuclear_Fuel_Rod "Nuclear Fuel Rod") or possibly other high-energy items to be conserved and used in multiple round trips
    * This means vehicle routes have to be closed loops to function
  * Routes can be copied by saving them once recorded and loading in another vehicle 
    * This only works in the same kind of vehicle, e.g. Explorer routes can only be copied into other Explorers, not Tractors or Trucks etc.
  * Truck Stations placed on existing routes will adjust the route slightly to allow the vehicle to stop there without the need to re-record



### Trains

[Train](/wiki/Train "Train") collisions will be added, trains will be able to crash into each other and derail from the [Railway](/wiki/Railway "Railway"). To prevent this, rail Signals have to be set up.[U5 4]

  * Two types of Signals: Block and Path Signals.[U5 24]
    * Block Signals divide the track into blocks, which are sections between 2 or more Signals; if any part of a train is in a block, the Block Signal will turn red and incoming trains will have to wait for the first train to leave
    * Path Signals allow multiple trains to pass through a single block as long as their paths don't intersect, as well as ensure the following block is free to prevent trains backing up within the intersecting block
    * Train Signals will work with overlapping train tracks[U5 25]
      * Tracks detect if they intersect each other using their hitboxes rather than relying on being connected, forming a block shared between all intersecting railways
    * Both types of Signals have these common properties: 
      * Attach to the edges of Railways
      * Show red/green when set up properly and flash warning signs when not
      * Can be interacted with to show errors
      * Make Railways one-directional, displaying a red wrong way sign on their back, unless built on both sides of the track
      * Cost 2 [](/wiki/Steel_Beam "Steel Beam") [Steel Beams](/wiki/Steel_Beam "Steel Beam") and 1 [](/wiki/Circuit_Board "Circuit Board") [Circuit Board](/wiki/Circuit_Board "Circuit Board") to construct[U5 26][U5 27]
  * Trains may crash into each other, causing the carriages to unjoin and derail 
    * Trains can crash into each other in such interections where tracks aren't connected but do intersect; however, they will not collide with terrain[U5 28]
    * After a crash, trains can simply be re-railed by approaching any Locomotive or Freight car of the train and pressing [`E`](/wiki/Controls "Controls"), or interacting by a hologram of the train which appears where the train was before derailment, useful when a crash occurs above a ravine or the void[U5 29]
    * There is no explosion during a train collision, cargo nor timetable data isn't lost
  * The [Freight Platform](/wiki/Freight_Platform "Freight Platform") will have a new UI displaying average throughput and a simplified load/unload switch[U5 30]
  * The timetable UI will receive a complete rework[U5 31]
    * Timetables can be set up dragging stations from a list, showing the world map next to the list menu
    * Timetable changes can be discarded rather than being always applied when the menu is closed
  * Stop Settings feature will be added to the timetable menu, which sets the behavior of a train visiting a selected station using the following two settings:[U5 32]
    * Wait until all Freight Cars are fully loaded or unloaded and/or to wait for a set amount of time
    * Only load or unload selected item types
  * Possibly added vehicle recoloring 
    * Freight Cars with both the default theme[U5 33] and a silvey-gray theme[U5 34] appear in the video, implying they can be recolored
  * Likely added a way to switch railway switches while riding a Locomotive 
    * For a split-second, it appears a list of possible keypresses appears while riding a Locomotive, similar to those currently under the build menu and [inventory](/wiki/Inventory "Inventory"); one of the listed keypresses is "Switch Intersection Path" with [`A`](/wiki/Controls "Controls")/[`D`](/wiki/Controls "Controls")



[](/wiki/File:Train_Controls_U5_Preview.png)

[](/wiki/File:Train_Controls_U5_Preview.png "Enlarge")

New train controls in Update 5

## References

  1. ↑ [YouTube - Coffee Stain - Satisfactory Update 5 Release Date (Experimental) & some extra info](https://youtu.be/W3YBFCO1NMg?t=18)
  2. ↑ [Twitch - October 19th, 2021 Livestream - Q&A: At what time is Update 5 being released](https://clips.twitch.tv/AffluentVenomousBatteryStrawBeary-J6Z7byOgwLEVQ4lc)
  3. ↑ [YouTube - June 18th, 2021 video - Q&A: When is Update 5 coming](https://youtu.be/slNYE26evgc?t=83)
  4. ↑ 4.0 4.1 [Twitch - January 26th, 2021 Livestream - Q&A: How many updates til 1.0 + train collisions when?](https://clips.twitch.tv/MoistSmallMetalPipeHype)
  5. ↑ 5.0 5.1 5.2 5.3 5.4 [YouTube - Coffee Stain - Everything you need to know about the Update 5 Map Changes (and more)](https://www.youtube.com/watch?v=MxvGbCCc6DI)
  6. ↑ [YouTube - September 7th, 2021 Livestream - Q&A: What can be Zooped?](https://youtu.be/tOkr62V4ks4)
  7. ↑ 7.0 7.1 7.2 [YouTube - Coffee Stain - Dev Vlog: New Build Pieces and Build System changes coming to Update 5](https://www.youtube.com/watch?v=yZGq-W7r2sk)
  8. ↑ [Twitter - @SatisfactoryAF - July 6th, 2020 - LEAK!!](https://twitter.com/SatisfactoryAF/status/1280053159377936387)
  9. ↑ [YouTube - June 18th, 2021 video - Jace Talk: Build Modes in Update 5](https://youtu.be/slNYE26evgc?t=131)
  10. ↑ [Youtube - October 15th, 2021 video - Vertical and horizontal zooping](https://youtu.be/jTIAMuPqSlI?t=97)
  11. ↑ [YouTube - September 7th, 2021 Livestream - Q&A: Why did you go with the term "Zoop", what were the other possibilities?](https://youtu.be/RGDvSGvf7qg)
  12. ↑ [YouTube - September 7th, 2021 Livestream - Q&A: Where's the term "Zoop" come from?](https://youtu.be/HNK0TDmQBVU)
  13. ↑ [YouTube - September 7th, 2021 Livestream - Q&A: Why is Power Pole considered Hard Clearance?](https://youtu.be/TKH7DyKIets)
  14. ↑ [YouTube - September 7th, 2021 Livestream - Q&A: Will Splitters & Mergers have Soft or Hard Clearance?](https://youtu.be/1sI1tJLivp4)
  15. ↑ [Youtube - October 15th, 2021 - Complex clearance](https://youtu.be/jTIAMuPqSlI?t=396)
  16. ↑ [Youtube - October 15th, 2021 - snapping walkways to buildings](https://youtu.be/jTIAMuPqSlI?t=173)
  17. ↑ [Youtube - October 15th, 2021 - Additional rotations for snapping foundations](https://youtu.be/jTIAMuPqSlI?t=252)
  18. ↑ [Youtube - October 15th, 2021 - More freedom with stairs](https://youtu.be/jTIAMuPqSlI?t=149)
  19. ↑ [Youtube - October 15th, 2021 - Ramp snapping improvements](https://youtu.be/jTIAMuPqSlI?t=54)
  20. ↑ [Youtube - October 15th, 2021 - Input/Output snapping](https://youtu.be/jTIAMuPqSlI?t=285)
  21. ↑ [Youtube - October 15th, 2021 - Straight conveyor belts and pipes](https://youtu.be/jTIAMuPqSlI?t=341)
  22. ↑ [Youtube, October 15th, 2021 - Modify hologram colors](https://youtu.be/jTIAMuPqSlI?t=370)
  23. ↑ [YouTube - Coffee Stain - Changes to Truck Station and Vehicle Automation coming in Update 5](https://www.youtube.com/watch?v=kh3lVrBdjFE)
  24. ↑ [YouTube - Coffee Stain - Update 5 Trains Collisions, Signals, New "Stop Settings" & more (Signals - Introduction)](https://youtu.be/CskxkIepX6Y?t=327)
  25. ↑ [YouTube - Coffee Stain - Update 5 Trains Collisions, Signals, New "Stop Settings" & more (Are intersecting tracks supported?)](https://youtu.be/CskxkIepX6Y?t=789)
  26. ↑ [YouTube - Coffee Stain - Update 5 Trains Collisions, Signals, New "Stop Settings" & more - Block Signal cost](https://youtu.be/CskxkIepX6Y?t=662)
  27. ↑ [YouTube - Coffee Stain - Update 5 Trains Collisions, Signals, New "Stop Settings" & more - Path Signal Cost](https://youtu.be/CskxkIepX6Y?t=677)
  28. ↑ [Twitch - CoffeeStainStudiosDevs - Trains will not collide with terrain](https://clips.twitch.tv/CloudyTacitJellyfishAliens-IU-HIpU_rEgBcbVS)
  29. ↑ [YouTube - Coffee Stain - Update 5 Trains Collisions, Signals, New "Stop Settings" & more - Repairing de-railed trains](https://youtu.be/CskxkIepX6Y?t=202)
  30. ↑ [YouTube - Coffee Stain - Update 5 Trains Collisions, Signals, New "Stop Settings" & more - Freight Station UI Changes](https://youtu.be/CskxkIepX6Y?t=873)
  31. ↑ [YouTube - Coffee Stain - Update 5 Trains Collisions, Signals, New "Stop Settings" & more - Train Timetable UI Changes](https://youtu.be/CskxkIepX6Y?t=889)
  32. ↑ [YouTube - Coffee Stain - Update 5 Trains Collisions, Signals, New "Stop Settings" & more - New "Stop Settings" Feature](https://youtu.be/CskxkIepX6Y?t=911)
  33. ↑ [YouTube - Coffee Stain - Update 5 Trains Collisions, Signals, New "Stop Settings" & more -Default theme Freight Car](https://youtu.be/CskxkIepX6Y?t=422)
  34. ↑ [YouTube - Coffee Stain - Update 5 Trains Collisions, Signals, New "Stop Settings" & more - Gray theme Freight Car](https://youtu.be/CskxkIepX6Y?t=811)


  *[v]: View this template
  *[e]: Edit this template
  *[h]: History of this template
  *[his]: his trivia section
