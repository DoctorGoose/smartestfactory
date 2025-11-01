# Train Signals

BlockPath

## Block Signal

[ ](/wiki/File:Block_Signal.png "Block Signal.png")

_Directs the movement of trains to avoid collisions and bottlenecks.  
Block Signals can be placed on Railways to create 'Blocks' between them. When a train is occupying one of these Blocks, other trains will be unable to enter it.  
Caution: Signals are directional! Trains are unable to move against this direction, so be sure to set up Signals in both directions for bi-directional Railways._

### Unlocked by

[Tier 6](/wiki/Tier_6 "Tier 6") \- Railway Signalling

### Class name

Desc_RailroadBlockSignal_C

## Ingre­dients

**2 ×[](/wiki/Steel_Pipe "Steel Pipe") [Steel Pipe](/wiki/Steel_Pipe "Steel Pipe")**

**1 ×[](/wiki/Computer "Computer") [Computer](/wiki/Computer "Computer")**

## Path Signal

[ ](/wiki/File:Path_Signal.png "Path Signal.png")

_Directs the movement of trains to avoid collisions and bottlenecks.  
Path Signals are advanced signals that are especially useful for bi-directional Railways and complex intersections. They function similarly to Block Signals, but rather than occupying the entire Block, trains can reserve a specific path through it and will only enter the Block if their path allows them to fully pass through.  
Caution: Signals are directional! Trains are unable to move against this direction, so be sure to set up Signals in both directions for bi-directional Railways._

### Unlocked by

[Tier 6](/wiki/Tier_6 "Tier 6") \- Railway Signalling

### Class name

Desc_RailroadPathSignal_C

## Ingre­dients

**2 ×[](/wiki/Steel_Pipe "Steel Pipe") [Steel Pipe](/wiki/Steel_Pipe "Steel Pipe")**

**1 ×[](/wiki/Computer "Computer") [Computer](/wiki/Computer "Computer")**

**Block Signals** and **Path Signals** are structures that attach to [Railways](/wiki/Railway "Railway"), used to control the flow of [trains](/wiki/Train "Train"). They are necessary if you wish to have two or more trains using the same railway without collisions. 

## Contents

  * 1 Construction
    * 1.1 Build modes
  * 2 Usage
    * 2.1 Pathfinding
    * 2.2 Blocks
  * 3 Block Signal
  * 4 Path Signal
    * 4.1 Advanced description
  * 5 States
  * 6 Tips
  * 7 Trivia
  * 8 Current issues
  * 9 External links
  * 10 History
  * 11 References



## Construction

Both types of train signals can only be built on [Railway](/wiki/Railway "Railway") tracks. Their placement automatically snaps to track joints. Alternatively, they may be also built freely along track segments,[1] as long as they're at least 12m from the end of the segment. Doing so will split the segment to form a new joint, which will not rejoin even if the signal is dismantled afterwards. 

The forward direction of the signal is determined by which side of the joint is targeted. It helps to point at the track rather than the edge of the track. An arrow also indicates the forward direction. 

Up to 2 signals facing opposite directions can be placed on each track joint. If only one signal is present, it will prevent trains in the opposite direction from passing through. A bi-directional track can be achieved by placing signals on both sides of the track. 

### Build modes

Train signals can be set up for right-hand traffic (common) by placing on the right in direction of travel, or left-hand drive (less common) by placing on the left in direction of travel. 

Both Path signals and Block signals now have a “Left Side” and “Right Side” build mode that can be alternated by pressing [`R`](/wiki/Controls "Controls") when having the hologram active. 

  * [](/wiki/File:Train_Signal_-_Placement_1.png "Block Signal placement")

Block Signal placement

  * [](/wiki/File:Train_Signal_-_Placement_2.png "Double Signal \(Path and Block\) placement")

Double Signal (Path and Block) placement




## Usage

### Pathfinding

Automated trains will stop at a red or error signal. They will also brake ahead, although they will be forcefully stopped if they fail to slow down on their own. 

An important aspect of train pathfinding is that it does not re-route. A path is determined by the shortest distance to the destination, regardless of whether it is occupied by other trains. Trains won't pass the back of a signal, so an incorrect setup can make the destination unreachable. 

[Train Stations](/wiki/Train_Station "Train Station") the train is passing through add a +100m distance penalty. Rail stackers cannot be constructed; instead, long snake tracks have to be used as waiting areas. 

Signals can be completely ignored while driving trains manually. Block Signals will recognize that they are occupied like usual. However, Path Signals will prevent all trains from entering if their block is occupied by a manually-driven train. 

### Blocks

A block is the area between two signals. A block which contains any part of a train is considered to be occupied, otherwise it is vacant. 

Blocks are colored while a signal is being placed. Each block is given a different color and colors can be repeated on "other blocks". It can help understand signal placement errors to select a signal to place then examine where each block begins and ends by looking at their coloring. 

Blocks have to have at least one entry signal, as well as at least one exit signal (which will be the next block's entry signal). Blocks on a linear track will have only one entry and one exit signal, but branches will have multiple exit signals, merges will have multiple entry signals, and more complex intersections can have multiple entry and multiple exit signals. _All entry signals_ for a block have to be of the same type, either all Block Signals or all Path Signals. 

Rails which touch or clip through other rails will be considered part of the same block, even if the rails do not snap together at the ends: this makes it possible to build crossroads where one track crosses another. This can lead to many issues with signalling if two tracks in opposite directions are built too close to each other, and unknowingly "intersect" at curves, for example.[2] Always leave at least one block of space between rails to avoid this. Avoiding clipping will not prevent the issue alone. 

  * [](/wiki/File:Train_Signal_-_Blocks.png "Block examples")

Block examples

  * [](/wiki/File:Train_Signal_-_Blocks_Colors.png "Block colors shown when a Signal is being placed")

Block colors shown when a Signal is being placed




## Block Signal

Block Signals work on a simple principle: they prevent trains from entering a block if another train already occupies it. If any part of a train is within a block ahead, then all Block Signals entering _that block_ will be red, preventing other trains from entering that block. If the block ahead is empty, then all Block Signals entering _that block_ will be green.[3]

Block Signals are typically used on straight double tracks and for stations. Bidirectional tracks and junctions are better handled by Path Signals. 

Note: Block Signals shouldn't be used for blocks where tracks merge from multiple entrances. Due to a bug (see below), multiple trains might be able to enter and collide, even if the junction is signalled properly. 

  * [](/wiki/File:Train_Signal_-_Train_Station.png "Example of placing Block Signals for Train Stations")

Example of placing Block Signals for Train Stations




## Path Signal

Path Signals are more advanced than Block Signals. They use a path reservation system to control trains.[4] While avoidable in many scenarios, Path Signals make managing advanced networks possible. 

The three important aspects of Path Signals are that they allow multiple trains to enter if their paths within the block do not intersect, do not allow a train to enter if it cannot exit, and that a [Train Station](/wiki/Train_Station "Train Station") cannot be within a path block. 

Using Path Signals for junctions is not strictly necessary in most cases. However, it is recommended if you are building high-traffic systems with high chances of multiple trains reaching the same intersection. In this specific context, you will often hear players use the phrase "path in, block out." This is because all entry signals of a block must be of the same type. You cannot have a Block Signal and a Path Signal leading into the same junction. 

Due to a bug (see § Current issues), path blocks have to be level, or trains may collide into each other. 

### Advanced description

Path Signals automatically subdivide a block into paths, and treat them as individual sub-blocks. An automated train will reserve a path through the block as it approaches. Other trains can reserve their own paths at the same time, as long as they do not intersect with a path that is already reserved by another train. This allows multiple trains to pass through the same block simultaneously without colliding. 

Unlike Block Signals, Path Signals will "look ahead" to the Block Signal that follows a train's reserved path. The Path Signal will stop a train if it would have to stop for the next Block Signal while still traversing its reserved path. The Path Signal will turn green once the block at the end of the reserved path is vacant. This system ensures that trains do not stop in the middle of an intersection, which helps to prevent gridlocks. However, trains can be forced to stop within an intersection if their desired exit block becomes occupied with a manually driven train. 

Path Signals remain red until an automated train has reserved a path through that signal, at which time they will turn green to allow the train through. Automated trains treat the Path Signal as red until it turns green because it has approved the path. An approaching automated train will not reserve a path through a Path Signal's block until the next signal is the Path Signal. This means that if there is a Block Signal just before the Path Signal, the Automated train will have to slow down because the Path Signal will remain red until the train passes the Block Signal. 

It is possible to chain Path Signals one after the other for especially complex intersections to increase their throughput. Trains reserve paths through multiple Path Signals at once up to the next Block Signal, and will not pass the first Path Signal if any single portion of the path cannot be reserved. 

There is no way for a player who is manually driving a train to reserve a path through a Path Signal, so a player will always appear to be "running a red" when they pass through a Path Signal, even though the block ahead is vacant. When a player-driven train enters a Path Signal, the entire block seems to be considered occupied, and the Path Signals will act like Block Signals and not allow automated trains to enter. 

  * [](/wiki/File:Train_Signal_-_Path_Signal_-_Block.png "Example Path Signal block")

Example Path Signal block

  * [](/wiki/File:Train_Signal_-_Path_Signal_-_Usage.png "Example Path Signal block usage")

Example Path Signal block usage

  * [](/wiki/File:Train_Signal_-_Complex_1.png "Double track "T" intersection using signals")

Double track "T" intersection using signals

  * [](/wiki/File:Train_Signal_-_Complex_2.png "Single track "+" intersection using signals")

Single track "+" intersection using signals




## States

Individual Train Signals can appear in one of three "states" that reflect if Train is ok to proceed, or must stop, or there is an issue/error with Train Signal placement. Error signals are treated as red. 

  * 🟢 Green 
    * Block Clear (Block Signal default state)
    * Path Approved (Path Signal)
  * 🔴 Red 
    * Block Occupied
    * Waiting for Path Reservation (Path Signal default state)
  * ⚠️ Error 
    * Invalid Signal
    * Signal has missing connections 
      * The signal is placed on the very end of a Railway or is not connected to one, leading nowhere
    * Block has no exit signal
    * Block has conflicting entry signal types 
      * All entry signals have to be either Block or Path; this does not apply to exit signals
    * Path block cannot contain stations 
      * [Stations](/wiki/Train_Station "Train Station") cannot be placed inside Path blocks anymore, path signals now give a proper error message if a Train Station is found inside a block.
    * Signal loops into itself 
      * This error means the signal failed to divide a block, even when no loops are present. It can occur when, for example, two unconnected tracks are too close to each other and a signal is placed on one of them.
      * Sometimes, there is no obvious cause for this error. Using the block color highlight can be used to diagnose which signal is causing the problem. Rebuilding the affected junction can resolve the issue.


  * [](/wiki/File:Train_Signal_-_Error.png "Train Signal error")

Train Signal error

  * [](/wiki/File:Train_Signal_-_Error_-_UI.png "Train Signal error UI")

Train Signal error UI




## Tips

  * Track joints can be found easily by aiming at a Railway in [dismantle mode](/wiki/Dismantle_mode "Dismantle mode").
  * Collisions generally shouldn't happen if any signals are in place. Gridlocks may occur instead. See § Current issues for exceptions.
  * Trains appear to slow down for red/error signals at a distance of about 250 m, or 2.5 maximum track lengths. If they fail to brake in time (if the block has a steep downhill slope, for example), they will be forcefully stopped at the signal, much like with Train Stations. 
    * Path Signals are red until reserved, and they aren't reserved until the train is in a block immediately before the Path Signal. Thus, blocks leading to Path Signals should be long enough to prevent trains slowing down due to approaching a red signal.
  * There isn't a general guidance for appropriate block sizes. A good factor is the length of the longest trains. To avoid signal spam, blocks even 3 or 4 maximum track lengths long (300-400 m) are appropriate.



## Trivia

  * Train signals were originally planned for Update 6.[5]



## Current issues

  * Train collisions can occur even with seemingly properly placed signals: 
    * A train can be made to loop into itself within one block (much like in _Snake_).
    * More than one entry Block Signal may turn green once a block is freed. This allows multiple trains awaiting entry to enter simultaneously. If their paths cross within the block, they will collide.[6]
      * This can be mitigated by using Path Signals for blocks where tracks merge, which don't seem to suffer from this issue.
  * Trains may ignore signals the first few moments after a save file is loaded, causing them to pass a red signal.
  * Path Signals do not properly subdivide blocks if the Railways are not level, and thus may allow trains whose paths intersect to enter.



## External links

  * [Train Signal Guide by TotalXclipse on YouTube](https://www.youtube.com/watch?v=SNyjS6Nw4Tw)
  * [Signal Logic Rules by u/Sevrahn on Reddit](https://www.reddit.com/r/SatisfactoryGame/comments/qgy9z0/signal_logic_rules/)



## History

  * [Patch 1.1.0.5](/wiki/Patch_1.1.0.5 "Patch 1.1.0.5"): Fixed build effect on Train Signals becoming stuck permanently by disallowing upgrading of Signals for now
  * [Patch 1.1.0.0](/wiki/Patch_1.1.0.0 "Patch 1.1.0.0"): Both Path Signals and Block Signals now have a "Left Side" and "Right Side" build mode that can be alternated by pressing [`R`](/wiki/Controls "Controls") when having the hologram active
  * [Patch 1.0.0.4](/wiki/Patch_1.0.0.4 "Patch 1.0.0.4"): Fixed Railway Block visualization, it should now work as intended again
  * [Patch 1.0](/wiki/Patch_1.0 "Patch 1.0"): 
    * Now unlocked at [Tier 6](/wiki/Tier_6 "Tier 6") \- Railway Signalling
    * Now can be placed freely along Railway segments, not only at joints
    * Block Signal: Changed cost from 2 Steel Pipe, 1 Copper Sheet and 1 Circuit Board to 2 Steel Pipe and 1 Computer
    * Path Signal: Removed 1 Copper Sheet cost
  * [Patch 0.8.2.4](/wiki/Patch_0.8.2.4 "Patch 0.8.2.4"): Fixed Railway Block/Path Signal Visualization crashing for [Multiplayer](/wiki/Multiplayer "Multiplayer") / [Dedicated Servers](/wiki/Dedicated_Servers "Dedicated Servers") Clients
  * [Patch 0.8.2.0](/wiki/Patch_0.8.2.0 "Patch 0.8.2.0"): Fixed railroad track signal visualization.
  * [Patch 0.5.2.1](/wiki/Patch_0.5.2.1 "Patch 0.5.2.1")
    * Train Stations cannot be placed inside Path blocks anymore, Path Signals now give a proper error message if a Train Station is found inside a block
    * Short blocks, about 75% the size of a Freight Car, should now work with Path Signals
    * Fixed Path Signals placed right after a Train Station being incorrectly reserved by trains going to the Train Station.
  * [Patch 0.5.1.13](/wiki/Patch_0.5.1.13 "Patch 0.5.1.13"): Multiple fixes related to issues with Path Signals and Block Signals
  * [Patch 0.5.1.11](/wiki/Patch_0.5.1.11 "Patch 0.5.1.11"): Potential fix for multiblock reservation issues for Train Signals
  * [Patch 0.5.1.4](/wiki/Patch_0.5.1.4 "Patch 0.5.1.4")
    * Fixed a bug where trains docked at a Train Station could reserve Path Signals when saving and loading
    * Fixed a case where trains approaching Train Stations with a Path Signal right after the station would reserve the same Path Signal over and over
  * [Patch 0.5.0.11](/wiki/Patch_0.5.0.11 "Patch 0.5.0.11"): Added Block/Path Signal visual feedback when placing down
  * [Patch 0.5.0.0](/wiki/Patch_0.5.0.0 "Patch 0.5.0.0"): Introduced Block Signals and Path Signals



## References

  1. ↑ [YouTube - Satisfactory 1.0 Release Stream! - Train Signal Freehand Placment](https://www.youtube.com/watch?v=1GH5SZkrv2M&t=10830s)
  2. ↑ [YouTube - Update 5 Trains Collisions, Signals, New "Stop Settings" & more - Are intersecting tracks supported (Blocks)?](https://www.youtube.com/watch?v=CskxkIepX6Y&t=823s)
  3. ↑ [YouTube - Update 5 Trains Collisions, Signals, New "Stop Settings" & more - Block Signals](https://www.youtube.com/watch?v=CskxkIepX6Y&t=399s)
  4. ↑ [YouTube - Update 5 Trains Collisions, Signals, New "Stop Settings" & more - Path Signals](https://www.youtube.com/watch?v=CskxkIepX6Y&t=468s)
  5. ↑ [YouTube - October 19th, 2021 Livestream - Q&A: Updates planned to be bigger or smaller in the future?](https://youtu.be/eue3ZXfiBZQ?t=34)
  6. ↑ <https://questions.satisfactorygame.com/post/62ad0e51ca608e0803514f86>



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
[Railway Transport](/wiki/Trains "Trains")| [](/wiki/Electric_Locomotive "Electric Locomotive") [Electric Locomotive](/wiki/Electric_Locomotive "Electric Locomotive") • [](/wiki/Freight_Car "Freight Car") [Freight Car](/wiki/Freight_Car "Freight Car") • [](/wiki/Train_Station "Train Station") [Train Station](/wiki/Train_Station "Train Station") • [](/wiki/Freight_Platform "Freight Platform") [Freight Platform](/wiki/Freight_Platform "Freight Platform") ([Fluid](/wiki/Freight_Platform#Fluid "Freight Platform")) • [](/wiki/Empty_Platform "Empty Platform") [Empty Platform](/wiki/Empty_Platform "Empty Platform") ([With Catwalk](/wiki/Empty_Platform_With_Catwalk "Empty Platform With Catwalk")) • [](/wiki/Railway "Railway") [Railway](/wiki/Railway "Railway") ([Railroad Switch Control](/wiki/Railroad_Switch_Control "Railroad Switch Control")) • [](/wiki/Buffer_Stop "Buffer Stop") [Buffer Stop](/wiki/Buffer_Stop "Buffer Stop") • Train Signals ([](/wiki/Train_Signals#Block "Train Signals") Block • [](/wiki/Train_Signals#Path "Train Signals") Path)  
Hypertubes| [](/wiki/Hypertube "Hypertube") [Hypertube](/wiki/Hypertube "Hypertube") • [](/wiki/Hypertube_Entrance "Hypertube Entrance") [Hypertube Entrance](/wiki/Hypertube_Entrance "Hypertube Entrance") • [](/wiki/Hypertube_Supports "Hypertube Supports") [Hypertube Supports](/wiki/Hypertube_Supports "Hypertube Supports") ([Stackable](/wiki/Hypertube_Supports#Stackable "Hypertube Supports"), [Wall Support](/wiki/Hypertube_Supports#Wall "Hypertube Supports"), [Wall Hole](/wiki/Hypertube_Supports#Hole "Hypertube Supports"), [Floor Hole](/wiki/Hypertube_Supports#Floor "Hypertube Supports")) • [](/wiki/Hypertube_Junction "Hypertube Junction") [Hypertube Junction](/wiki/Hypertube_Junction "Hypertube Junction") ([Branch](/wiki/Hypertube_Branch "Hypertube Branch"))  
Pioneer Transport| [](/wiki/Jump_Pad "Jump Pad") [Jump Pad](/wiki/Jump_Pad "Jump Pad") • [](/wiki/U-Jelly_Landing_Pad "U-Jelly Landing Pad") [U-Jelly Landing Pad](/wiki/U-Jelly_Landing_Pad "U-Jelly Landing Pad") • [](/wiki/Personnel_Elevator "Personnel Elevator") [Personnel Elevator](/wiki/Personnel_Elevator "Personnel Elevator") • [](/wiki/Portal "Portal") [Portal](/wiki/Portal "Portal") ([Main](/wiki/Main_Portal "Main Portal"), [Satellite](/wiki/Satellite_Portal "Satellite Portal"))  
  
Organization| [](/wiki/Lights "Lights") [Lights](/wiki/Lights "Lights") • [](/wiki/Signs "Signs") [Signs](/wiki/Signs "Signs") • [](/wiki/Crate "Crate") [Crate](/wiki/Crate "Crate") • [](/wiki/Personal_Storage_Box "Personal Storage Box") [Personal Storage Box](/wiki/Personal_Storage_Box "Personal Storage Box") ([Medical](/wiki/Personal_Storage_Box#Medical "Personal Storage Box"), [Hazard](/wiki/Personal_Storage_Box#Hazard "Personal Storage Box")) • [](/wiki/Basic_Shelf_Unit "Basic Shelf Unit") [Basic Shelf Unit](/wiki/Basic_Shelf_Unit "Basic Shelf Unit") • [](/wiki/Storage_Container "Storage Container") [Storage Container](/wiki/Storage_Container "Storage Container") ([Industrial](/wiki/Storage_Container#Industrial "Storage Container")) • [](/wiki/Dimensional_Depot_Uploader "Dimensional Depot Uploader") [Dimensional Depot Uploader](/wiki/Dimensional_Depot_Uploader "Dimensional Depot Uploader") • [](/wiki/Fluid_Buffer "Fluid Buffer") [Fluid Buffer](/wiki/Fluid_Buffer "Fluid Buffer") ([Industrial](/wiki/Fluid_Buffer#Industrial "Fluid Buffer")) • [](/wiki/Lookout_Tower "Lookout Tower") [Lookout Tower](/wiki/Lookout_Tower "Lookout Tower") • [](/wiki/Radar_Tower "Radar Tower") [Radar Tower](/wiki/Radar_Tower "Radar Tower")  
Foundations| [](/wiki/Foundations#Foundations "Foundations") [Foundations](/wiki/Foundations#Foundations "Foundations") • [](/wiki/Foundations#Ramps "Foundations") [Ramps](/wiki/Foundations#Ramps "Foundations") • [](/wiki/Foundations#Inverted_Ramps "Foundations") [Inverted Ramps](/wiki/Foundations#Inverted_Ramps "Foundations") • [](/wiki/Foundations#Quarter-Pipes "Foundations") [Quarter-Pipes](/wiki/Foundations#Quarter-Pipes "Foundations") • [](/wiki/Foundations#Half_Foundations "Foundations") [Half Foundations](/wiki/Foundations#Half_Foundations "Foundations")  
Walls| [](/wiki/Walls#Basic "Walls") [Basic Walls](/wiki/Walls#Basic "Walls") • [](/wiki/Walls#Ramp "Walls") [Ramp Walls](/wiki/Walls#Ramp "Walls") • [](/wiki/Walls#Inverted_Ramp "Walls") [Inverted Ramp Walls](/wiki/Walls#Inverted_Ramp "Walls") • [](/wiki/Walls#Tilted "Walls") [Tilted Walls](/wiki/Walls#Tilted "Walls") • [](/wiki/Walls#Windows "Walls") [Windows](/wiki/Walls#Windows "Walls") • [](/wiki/Walls#Doors "Walls") [Doors](/wiki/Walls#Doors "Walls") • [](/wiki/Walls#Conveyor "Walls") [Conveyor Walls](/wiki/Walls#Conveyor "Walls")  
Architecture| [](/wiki/Frame_Structures "Frame Structures") [Frames](/wiki/Frame_Structures "Frame Structures") • [](/wiki/Roofs "Roofs") [Roofs](/wiki/Roofs "Roofs") • [](/wiki/Beams "Beams") [Beams](/wiki/Beams "Beams") • [](/wiki/Pillars "Pillars") [Pillars](/wiki/Pillars "Pillars") • [](/wiki/Walkways "Walkways") [Walkways](/wiki/Walkways "Walkways") • [](/wiki/Walls "Walls") [Railings](/wiki/Walls "Walls") • [](/wiki/Foundations#Stairs "Foundations") [Stairs](/wiki/Foundations#Stairs "Foundations") • [](/wiki/Ladder "Ladder") [Ladder](/wiki/Ladder "Ladder") • [](/wiki/Large_Fan "Large Fan") [Large Fan](/wiki/Large_Fan "Large Fan") ([Vent](/wiki/Large_Vent "Large Vent"))
  *[v]: View this template
  *[e]: Edit this template
  *[h]: History of this template
  *[his]: his trivia section
