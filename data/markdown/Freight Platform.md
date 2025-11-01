# Freight Platform

SolidFluid  
  
## Freight Platform

[ ](/wiki/File:Freight_Platform.png "Freight Platform.png")

_Loads and unloads Freight Cars that stop at the Freight Platform.  
Loading and unloading options can be set by configuring the building.  
Snaps to other Platforms and Stations.  
Needs to be connected to a powered Railway to function._

### Unlocked by

[Tier 6](/wiki/Tier_6 "Tier 6") \- Monorail Train Technology

### Class name

Desc_TrainDockingStation_C

## Building

### [Power  
usage](/wiki/Power "Power")

50 MW

### [Overclock­able](/wiki/Clock_speed "Clock speed")

No

### Conveyor  
inputs

2

### Conveyor  
outputs

2

## Dimensions

### Width

34 m

### Length

16 m

### Height

20 m

### Area

544 m2

## Ingre­dients

**5 ×[](/wiki/Motor "Motor") [Motor](/wiki/Motor "Motor")**

**10 ×[](/wiki/Encased_Industrial_Beam "Encased Industrial Beam") [Encased Industrial Beam](/wiki/Encased_Industrial_Beam "Encased Industrial Beam")**

**25 ×[](/wiki/Plastic "Plastic") [Plastic](/wiki/Plastic "Plastic")**

**50 ×[](/wiki/Concrete "Concrete") [Concrete](/wiki/Concrete "Concrete")**

**100 ×[](/wiki/Wire "Wire") [Wire](/wiki/Wire "Wire")**

## Fluid Freight Platform

[ ](/wiki/File:Fluid_Freight_Platform.png "Fluid Freight Platform.png")

_Loads and unloads Freight Cars that stop at the Freight Platform.  
Loading and unloading options can be set by configuring the building.  
Snaps to other Platforms and Stations.  
Needs to be connected to a powered Railway to function._

### Unlocked by

[Tier 6](/wiki/Tier_6 "Tier 6") \- Monorail Train Technology

### Class name

Desc_TrainDockingStationLiquid_C

## Building

### [Power  
usage](/wiki/Power "Power")

50 MW

### [Overclock­able](/wiki/Clock_speed "Clock speed")

No

### Pipeline  
inputs

2

### Pipeline  
outputs

2

## Dimensions

### Width

34 m

### Length

16 m

### Height

20 m

### Area

544 m2

## Ingre­dients

**5 ×[](/wiki/Motor "Motor") [Motor](/wiki/Motor "Motor")**

**10 ×[](/wiki/Encased_Industrial_Beam "Encased Industrial Beam") [Encased Industrial Beam](/wiki/Encased_Industrial_Beam "Encased Industrial Beam")**

**25 ×[](/wiki/Plastic "Plastic") [Plastic](/wiki/Plastic "Plastic")**

**50 ×[](/wiki/Concrete "Concrete") [Concrete](/wiki/Concrete "Concrete")**

**100 ×[](/wiki/Wire "Wire") [Wire](/wiki/Wire "Wire")**

A **Freight Platform** is a building on the [Railway](/wiki/Railway "Railway") where [Freight Cars](/wiki/Freight_Car "Freight Car") can be loaded or unloaded, based on the setting of each Freight Platform. 

It has to be attached to a [Train Station](/wiki/Train_Station "Train Station") to work and only snaps to it (alongside other platforms). It has two inputs and two outputs and 48 item slots for Solid Freight Platforms or 2 400 m3 of capacity for Fluid Freight Platforms, which is 1.5× the capacity of a single Freight Car. 

## Contents

  * 1 Usage
    * 1.1 UI
    * 1.2 Loading and unloading
    * 1.3 Animation
      * 1.3.1 Viable path requirements
    * 1.4 Power
    * 1.5 Flushing
  * 2 Train throughput
  * 3 Head lift
  * 4 Use of external buffers
  * 5 Trivia
  * 6 See also
  * 7 Gallery
  * 8 History
  * 9 Early game development
  * 10 References



## Usage

### UI

The Freight Platform UI [1] has a similar look and feel to the [Truck Station UI](/wiki/Truck_Station#UI "Truck Station"), and depending on if the Freight Platform is set to LOAD or UNLOAD will include information about: 

  * Outgoing Transfer Rate (Load)
  * Incoming Transfer Rate (Unload)



There is NO OPTION to have Freight Platforms do both Loading and Unloading in one cycle. 

The Freight Platform is set to LOAD by default. Just toggle the button to set it to UNLOAD (or vice versa). 

  * [](/wiki/File:Freight_platform_UI.png "Update 4 \(and earlier\) - Example of Freight Platform UI")

Update 4 (and earlier) - Example of Freight Platform UI

  * [](/wiki/File:Freight_Platform_UI.png "Update 5 - Example of Freight Platform UI")

Update 5 - Example of Freight Platform UI




### Loading and unloading

During the 27.08 seconds of automatic cargo transfers: 

  * Manual interactions with Freight Platforms and Cars aren't allowed unless that Platform has nothing to transfer.
  * All belts connected to a Platform stop and no items enter or exit.
  * Partial transfers only occur when the receiver has a free slot.



### Animation

Each of the following transfer animations takes 27.08 seconds: 

  * Full loading: The 20T crane hoists the container up and out of the freight platform and puts it onto the freight car.
  * Partial loading: The 20T crane hoists the entire storage module up from the freight platform and hovers it over the freight car. The doors below the module open and the contents flow from the bottom of the module into the top of freight car container. The storage module is then put back to the freight platform. 
    * While the platform storage module is being lifted, the pioneer can walk on the shelf where it normally rests. This is dangerous since the pioneer can be trapped there when the module is returned.
  * Full unloading: The 20T crane hoists up the container from the freight car and drops it into the storage module.
  * Partial unloading: The 20T crane hoists up the container from the freight car and hovers it over the freight platform's storage module. The doors below the container open and the contents flow from the container to the storage module. The container is then placed back on the freight car.



In all cases, the animation is complete only after the crane moves back to its original position. _Continue reading:[Train Station#Docking](/wiki/Train_Station#Docking "Train Station")_

#### Viable path requirements

Freight Platforms are only usable when the train has a viable path along the forward direction of the track. One way to avoid this being a problem with terminating stations is to use a loop in your track. Once the path is viable you can begin to insert cargo into the Freight Platforms. 

### Power

  * Freight Platforms only consume full power when transferring cargo with the Freight Car. At rest they only consume 0.1 MW.
  * Transferring fluids with Fluid Freight Platforms requires connected powered Train Stations.



### Flushing

A Fluid Freight Platform has the 'Flushing' option, similar to [Pipelines](/wiki/Pipelines "Pipelines") and [Fluid Buffers](/wiki/Fluid_Buffer "Fluid Buffer"). 

## Train throughput

_Main article:_[Tutorial:Train throughput](/wiki/Tutorial:Train_throughput "Tutorial:Train throughput")

## Head lift

_Main article:_[Head lift](/wiki/Head_lift "Head lift")

Fluid Freight Platforms apply head lift differently than any other building: 

  * The bottom output applies a head lift of 10 meters and an actual head lift of 12 meters measured from the platform base (the platform is one meter tall).
  * The top output, placed four meters above the bottom output, applies a head lift of 14 meters and an actual head lift of 16 meters measured from the platform base.



Head lift is applied regardless of the Freight Platform's load/unload setting. The generated head lift does not depend on its remaining fluid content, which means it can easily empty itself into [Fluid Buffers](/wiki/Fluid_Buffer "Fluid Buffer") located at the same level. 

Fluid Freight Platforms do not generate opposing head lift when being filled up, and thus a fluid source can easily fill them up as long as the pipe inlet level of the Fluid Platform is within the source's head lift. Because of this, it is advised to always use its lower pipe inlet first, followed by the upper inlet if the desired input rate is higher than a single pipe can handle. 

## Use of external buffers

It is recommended to build out from Freight Platforms some [Storage Containers](/wiki/Storage_Container "Storage Container") to act as "buffers". [2]

## Trivia

  * The stopping (delay) of item loading / unloading was added to prevent issues [3] and is similar in some respects to the delay seen during Autosaves.



## See also

  * [](/wiki/Electric_Locomotive "Electric Locomotive") [Electric Locomotive](/wiki/Electric_Locomotive "Electric Locomotive")
  * [](/wiki/Freight_Car "Freight Car") [Freight Car](/wiki/Freight_Car "Freight Car")
  * [](/wiki/Empty_Platform "Empty Platform") [Empty Platform](/wiki/Empty_Platform "Empty Platform")
  * [](/wiki/Railway "Railway") [Railway](/wiki/Railway "Railway")
  * [](/wiki/Train_Station "Train Station") [Train Station](/wiki/Train_Station "Train Station")



## Gallery

  * [](/wiki/File:Freight_Platform_E3.png "A train docking with three train loading cranes \(as seen in the E3 trailer\).")

A train docking with three train loading cranes (as seen in the E3 trailer).

  * [](/wiki/File:Freight_Platform_buffer.png "Industrial Storage Container with 2 belts connected to a Freight Platform is necessary to maintain the full throughput of a Freight Car.")

[Industrial Storage Container](/wiki/Industrial_Storage_Container "Industrial Storage Container") with 2 belts connected to a Freight Platform is necessary to maintain the full throughput of a [Freight Car](/wiki/Freight_Car "Freight Car").




## History

  * [Patch 1.1.0.4](/wiki/Patch_1.1.0.4 "Patch 1.1.0.4"): Potential fixes for crashes related to Building [Railways](/wiki/Railway "Railway") and [Train Stations](/wiki/Train_Station "Train Station")/Freight Platforms in [Multiplayer](/wiki/Multiplayer "Multiplayer")
  * [Patch 1.1.0.2](/wiki/Patch_1.1.0.2 "Patch 1.1.0.2"): Fixed train tracks being able to be branched and create [switches](/wiki/Railroad_Switch_Control "Railroad Switch Control") from the end of a [Train Station](/wiki/Train_Station "Train Station") or Freight Platform which would result in issues
  * [Patch 1.0.0.4](/wiki/Patch_1.0.0.4 "Patch 1.0.0.4"): Fixed measurement unit being missing in the Fluid Freight platform transfer rate
  * [Patch 1.0](/wiki/Patch_1.0 "Patch 1.0"): Changed cost from 6 Heavy Modular Frame, 2 Computer, 5 Motor, 50 Concrete and 25 Cable to 10 Encased Industrial Beams, 25 Plastic, 5 Motor, 50 Concrete and 100 Wire
  * [Patch 0.6.0.0](/wiki/Patch_0.6.0.0 "Patch 0.6.0.0"): Optimized Freight Platform loading
  * [Patch 0.5.1.7](/wiki/Patch_0.5.1.7 "Patch 0.5.1.7"): Fixed Freight Cars failing to load/unload correctly with the rule set to Fully Load/Unload which lead to them getting stuck in docking until force cancelled
  * [Patch 0.3.4.16](/wiki/Patch_0.3.4.16 "Patch 0.3.4.16"): Fixed too large Track clearance
  * [Patch 0.3.4.15](/wiki/Patch_0.3.4.15 "Patch 0.3.4.15"): Integrated Station Track should no longer rotate separately from the main building
  * [Patch 0.3.4.14](/wiki/Patch_0.3.4.14 "Patch 0.3.4.14"): Icon updated
  * [Patch 0.3.4.13](/wiki/Patch_0.3.4.13 "Patch 0.3.4.13"): 
    * Added a few more details to the meshes
    * Now does the partial load animation when applicable instead of triggering the wrong animation and clipping containers through each other
    * Conveyor Belts and Pipes now connect properly and no longer leave a gap when reconnecting
  * [Patch 0.3.4.12](/wiki/Patch_0.3.4.12 "Patch 0.3.4.12"): Added new meshes
  * [Patch 0.3.4.6](/wiki/Patch_0.3.4.6 "Patch 0.3.4.6"): Now state the correct capacity in their description
  * [Patch 0.3.4.0](/wiki/Patch_0.3.4.0 "Patch 0.3.4.0"): 
    * Increased capacity of Fluid Freight Platforms from 500 to 2400 m3
    * Performance improvements
  * [Patch 0.3.2.0](/wiki/Patch_0.3.2.0 "Patch 0.3.2.0"): Changed name from Freight Platform Fluid to Fluid Freight Platform, updated UI
  * [Patch 0.3.1.1](/wiki/Patch_0.3.1.1 "Patch 0.3.1.1"): Increased capacity of Fluid Freight Platforms from 50 to 500 m3 (properly implemented)
  * [Patch 0.3.1.0](/wiki/Patch_0.3.1.0 "Patch 0.3.1.0"): ~~Increased capacity of Fluid Freight Platforms from 50 to 500 m 3~~ (announced but not actually implemented)
  * [Patch 0.3](/wiki/Patch_0.3 "Patch 0.3"): 
    * Introduced Fluid Freight Platform
    * Clients can now access inventories
  * [Patch 0.2.1.14](/wiki/Patch_0.2.1.14 "Patch 0.2.1.14"): Fixed ladder collision
  * [Patch 0.1.19](/wiki/Patch_0.1.19 "Patch 0.1.19"): 
    * Updated animations and visuals
    * Changed input/outputs of Freight Platforms
  * [Patch 0.1.17 build 101353](/wiki/Patch_0.1.17_build_101353 "Patch 0.1.17 build 101353"): 
    * Now can be dismantled again
    * Shift-click support for the inventory implemented
    * Now stops if a power outage occurs, and resumes when powered up again
  * [Patch 0.1.17](/wiki/Patch_0.1.17 "Patch 0.1.17"): Freight station in the middle of animation work
  * [Patch 0.1.16](/wiki/Patch_0.1.16 "Patch 0.1.16"): Made the Freight Platform available



## Early game development

Prior to Closed Alpha, in Sprint 23 (week 46) trains were first shown, to include an early version of the Freight Platform called a Train Docking Station. 

  * See also: [Game Development - Trains](/wiki/Early_game_development#Trains "Early game development")



## References

  1. ↑ [YouTube - Update 5 Trains Collisions, Signals, New "Stop Settings" & more - Freight Station UI Changes](https://youtu.be/CskxkIepX6Y?t=870)
  2. ↑ [YouTube - October 3rd, 2023 Livestream - Q&A: Will the delay in throughput when loading/unloading of Trains be removed? - Use Storage Container Buffers](https://www.youtube.com/watch?v=4bQakQJ_aY4&t=38s)
  3. ↑ [YouTube - October 3rd, 2023 Livestream - Q&A: Will the delay in throughput when loading/unloading of Trains be removed?](https://www.youtube.com/watch?v=4bQakQJ_aY4)



  * [v](/wiki/Template:VehicleNav "Template:VehicleNav")
  * [e](https://satisfactory.wiki.gg/wiki/Template:VehicleNav?action=edit)
  * [h](https://satisfactory.wiki.gg/wiki/Template:VehicleNav?action=history)

[Transportation](/wiki/Vehicles "Vehicles")  
---  
Motor vehicles| [](/wiki/Tractor "Tractor") [Tractor](/wiki/Tractor "Tractor") • [](/wiki/Truck "Truck") [Truck](/wiki/Truck "Truck") • [](/wiki/Explorer "Explorer") [Explorer](/wiki/Explorer "Explorer") • [](/wiki/Factory_Cart "Factory Cart") [Factory Cart](/wiki/Factory_Cart "Factory Cart") • [](/wiki/Golden_Factory_Cart "Golden Factory Cart") [Golden Factory Cart](/wiki/Golden_Factory_Cart "Golden Factory Cart") • [](/wiki/Cyber_Wagon "Cyber Wagon") [Cyber Wagon](/wiki/Cyber_Wagon "Cyber Wagon") • [](/wiki/Truck_Station "Truck Station") [Truck Station](/wiki/Truck_Station "Truck Station") • [](/wiki/Drone_Port "Drone Port") [Drone Port](/wiki/Drone_Port "Drone Port") • [](/wiki/Drone "Drone") [Drone](/wiki/Drone "Drone")  
Rail vehicles| [](/wiki/Electric_Locomotive "Electric Locomotive") [Electric Locomotive](/wiki/Electric_Locomotive "Electric Locomotive") • [](/wiki/Freight_Car "Freight Car") [Freight Car](/wiki/Freight_Car "Freight Car") • [](/wiki/Train_Station "Train Station") [Train Station](/wiki/Train_Station "Train Station") • [](/wiki/Freight_Platform "Freight Platform") Freight Platform • [](/wiki/Fluid_Freight_Platform "Fluid Freight Platform") [Fluid Freight Platform](/wiki/Fluid_Freight_Platform "Fluid Freight Platform") • [](/wiki/Empty_Platform "Empty Platform") [Empty Platform](/wiki/Empty_Platform "Empty Platform") • [](/wiki/Empty_Platform_With_Catwalk "Empty Platform With Catwalk") [Empty Platform With Catwalk](/wiki/Empty_Platform_With_Catwalk "Empty Platform With Catwalk") • [](/wiki/Railway "Railway") [Railway](/wiki/Railway "Railway") • [](/wiki/Railroad_Switch_Control "Railroad Switch Control") [Railroad Switch Control](/wiki/Railroad_Switch_Control "Railroad Switch Control") • [](/wiki/Buffer_Stop "Buffer Stop") [Buffer Stop](/wiki/Buffer_Stop "Buffer Stop") • [](/wiki/Block_Signal "Block Signal") [Block Signal](/wiki/Block_Signal "Block Signal") • [](/wiki/Path_Signal "Path Signal") [Path Signal](/wiki/Path_Signal "Path Signal")  
Hypertubes| [](/wiki/Hypertube "Hypertube") [Hypertube](/wiki/Hypertube "Hypertube") • [](/wiki/Hypertube_Entrance "Hypertube Entrance") [Hypertube Entrance](/wiki/Hypertube_Entrance "Hypertube Entrance") • [](/wiki/Hypertube_Support "Hypertube Support") [Hypertube Support](/wiki/Hypertube_Support "Hypertube Support") • [](/wiki/Stackable_Hypertube_Support "Stackable Hypertube Support") [Stackable Hypertube Support](/wiki/Stackable_Hypertube_Support "Stackable Hypertube Support") • [](/wiki/Hypertube_Wall_Hole "Hypertube Wall Hole") [Hypertube Wall Hole](/wiki/Hypertube_Wall_Hole "Hypertube Wall Hole") • [](/wiki/Hypertube_Wall_Support "Hypertube Wall Support") [Hypertube Wall Support](/wiki/Hypertube_Wall_Support "Hypertube Wall Support") • [](/wiki/Hypertube_Floor_Hole "Hypertube Floor Hole") [Hypertube Floor Hole](/wiki/Hypertube_Floor_Hole "Hypertube Floor Hole") • [](/wiki/Hypertube_Junction "Hypertube Junction") [Hypertube Junction](/wiki/Hypertube_Junction "Hypertube Junction") • [](/wiki/Hypertube_Branch "Hypertube Branch") [Hypertube Branch](/wiki/Hypertube_Branch "Hypertube Branch")  
Pioneer transport| [](/wiki/Jump_Pad "Jump Pad") [Jump Pad](/wiki/Jump_Pad "Jump Pad") • [](/wiki/U-Jelly_Landing_Pad "U-Jelly Landing Pad") [U-Jelly Landing Pad](/wiki/U-Jelly_Landing_Pad "U-Jelly Landing Pad") • [](/wiki/Personnel_Elevator "Personnel Elevator") [Personnel Elevator](/wiki/Personnel_Elevator "Personnel Elevator") • [](/wiki/Main_Portal "Main Portal") [Main Portal](/wiki/Main_Portal "Main Portal") • [](/wiki/Satellite_Portal "Satellite Portal") [Satellite Portal](/wiki/Satellite_Portal "Satellite Portal")  
  
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
[Railway Transport](/wiki/Trains "Trains")| [](/wiki/Electric_Locomotive "Electric Locomotive") [Electric Locomotive](/wiki/Electric_Locomotive "Electric Locomotive") • [](/wiki/Freight_Car "Freight Car") [Freight Car](/wiki/Freight_Car "Freight Car") • [](/wiki/Train_Station "Train Station") [Train Station](/wiki/Train_Station "Train Station") • [](/wiki/Freight_Platform "Freight Platform") Freight Platform (Fluid) • [](/wiki/Empty_Platform "Empty Platform") [Empty Platform](/wiki/Empty_Platform "Empty Platform") ([With Catwalk](/wiki/Empty_Platform_With_Catwalk "Empty Platform With Catwalk")) • [](/wiki/Railway "Railway") [Railway](/wiki/Railway "Railway") ([Railroad Switch Control](/wiki/Railroad_Switch_Control "Railroad Switch Control")) • [](/wiki/Buffer_Stop "Buffer Stop") [Buffer Stop](/wiki/Buffer_Stop "Buffer Stop") • [Train Signals](/wiki/Train_Signals "Train Signals") ([](/wiki/Train_Signals#Block "Train Signals") [Block](/wiki/Train_Signals#Block "Train Signals") • [](/wiki/Train_Signals#Path "Train Signals") [Path](/wiki/Train_Signals#Path "Train Signals"))  
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
