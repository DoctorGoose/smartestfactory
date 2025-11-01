# Oil Extractor

## Oil Extractor

[ ](/wiki/File:Oil_Extractor.png "Oil Extractor.png")

_Extracts Crude Oil when built on an oil node. Extraction rates vary based on node purity.  
Default Extraction Rate: 120 m³ of oil per minute.  
Head Lift: 10 m  
(Allows fluids to be transported 10 meters upwards.)_

### Unlocked by

[Tier 5](/wiki/Tier_5 "Tier 5") \- Oil Processing

### Class name

Desc_OilPump_C

## Building

### [Power  
usage](/wiki/Power "Power")

40 MW

### [Overclock­able](/wiki/Clock_speed "Clock speed")

Yes

### Pipeline  
outputs

1

## Dimensions

### Width

8 m

### Length

14 m

### Height

20 m

### Area

112 m2

## Ingre­dients

**15 ×[](/wiki/Motor "Motor") [Motor](/wiki/Motor "Motor")**

**20 ×[](/wiki/Encased_Industrial_Beam "Encased Industrial Beam") [Encased Industrial Beam](/wiki/Encased_Industrial_Beam "Encased Industrial Beam")**

**60 ×[](/wiki/Cable "Cable") [Cable](/wiki/Cable "Cable")**

The **Oil Extractor** is a building used to extract [fluid](/wiki/Fluid "Fluid") [Crude Oil](/wiki/Crude_Oil "Crude Oil") from its [Resource Node](/wiki/Resource_Node "Resource Node"). The default extraction rate is 120 m3/min, based on normal node purity (see below). 

## Contents

  * 1 Construction
  * 2 Extraction
  * 3 Head lift
  * 4 Overclocking
  * 5 See also
  * 6 Gallery
  * 7 History
  * 8 Early game development



## Construction

Oil Extractors can be built on top of an [Oil](/wiki/Oil "Oil") [node](/wiki/Node "Node") regardless if the node is fully covered by [Foundations](/wiki/Foundations "Foundations"). When building on Foundations, its pipe outlet center is positioned exactly one meter above the floor. 

## Extraction

[](/wiki/Crude_Oil "Crude Oil") [Crude Oil](/wiki/Crude_Oil "Crude Oil") extraction rate (m3/min), with respect to [Clock Speed](/wiki/Clock_Speed "Clock Speed") and Oil node purity: 

Items produced per minute

100% Clock Speed250% Clock Speed

| Oil Extractor  
---|---  
Impure| 60  
Normal| 120  
Pure| 240  
  
| Oil Extractor  
---|---  
Impure| 150  
Normal| 300  
Pure| 600  
  
To calculate the **Oil Extractor** extraction speed:  
`120 x (node purity modifier) x (Clock Speed in decimal) = Extraction rate`  
**_Node purity modifier_** : 

  * Impure = 0.5x,
  * Normal = 1x,
  * Pure = 2x.



An Oil Extractor on a pure node can only benefit from clockspeeds beyond 125% with [Mk.2 Pipelines](/wiki/Pipeline "Pipeline") due to the 300 m3/min flowrate limit of [Mk.1 Pipelines](/wiki/Pipeline "Pipeline"). 

## Head lift

_Main article:_[Head lift](/wiki/Head_lift "Head lift")

An Oil Extractor provides a [head lift](/wiki/Head_lift "Head lift") of 10 meters, measured from the center of its pipe outlet. 

## Overclocking

_Main article:_[Clock speed](/wiki/Clock_speed "Clock speed")

The Oil Extractor can be overclocked using [Power Shards](/wiki/Power_Shard "Power Shard"). Overclocking increases the input/output speed of the Oil Extractor at the cost of exponentially increased [power](/wiki/Power "Power") demand. 

Clock speed | 25% | 50% | 75% | 100% | 150% | 200% | 250%   
---|---|---|---|---|---|---|---  
Consumption (MW)  | 6.4 | 16 | 27.35 | 40 | 68.37 | 100 | 134.31   
  
## See also

  * [](/wiki/Refinery "Refinery") [Refinery](/wiki/Refinery "Refinery")
  * [](/wiki/Crude_Oil "Crude Oil") [Crude Oil](/wiki/Crude_Oil "Crude Oil")
  * [](/wiki/Water_Extractor "Water Extractor") [Water Extractor](/wiki/Water_Extractor "Water Extractor")



## Gallery

  * [](/wiki/File:Early_Access_-_Oil_Pump.png "Oil Pump during Early Access Release before Update 1.")

Oil Pump during Early Access Release before Update 1.

  * [](/wiki/File:Early_Access_-_Oil_Pump_UI.png "Oil Pump UI during Early Access Release before Update 1.")

Oil Pump UI during Early Access Release before Update 1.

  * [](/wiki/File:Oil_Extractor_Front.png "Front of an oil extractor as of Update 3 \(and after\).")

Front of an oil extractor as of Update 3 (and after).

  * [](/wiki/File:Oil_Extractor_Back.png "Back of an oil extractor as of Update 3 \(and after\).")

Back of an oil extractor as of Update 3 (and after).




## History

  * [Patch 1.0.1.0](/wiki/Patch_1.0.1.0 "Patch 1.0.1.0"): [Copy pasting settings](/wiki/Controls "Controls"), using [`Right Ctrl`](/wiki/Controls "Controls")+[`C`](/wiki/Controls "Controls") and [`Right Ctrl`](/wiki/Controls "Controls")+[`V`](/wiki/Controls "Controls"), now works on [Generators](/wiki/Power "Power") and Extractors ([Water](/wiki/Water_Extractor "Water Extractor"),Oil,[Resource Well](/wiki/Resource_Well_Pressurizer "Resource Well Pressurizer"))
  * [Patch 0.3](/wiki/Patch_0.3 "Patch 0.3"): 
    * Replaced the Oil Pump.
    * Build cost changed from 5 [Heavy Modular Frame](/wiki/Heavy_Modular_Frame "Heavy Modular Frame"), 10 [Motor](/wiki/Motor "Motor"), and 30 [Cable](/wiki/Cable "Cable") to 15 [Motor](/wiki/Motor "Motor"), 20 [Encased Industrial Beam](/wiki/Encased_Industrial_Beam "Encased Industrial Beam") and 60 [Cable](/wiki/Cable "Cable")
    * Removed [conveyor](/wiki/Belt "Belt") output, now outputs [Crude Oil](/wiki/Crude_Oil "Crude Oil") as a fluid into a connected [Pipeline](/wiki/Pipeline "Pipeline")
  * [Patch 0.1.5](/wiki/Patch_0.1.5 "Patch 0.1.5"): changed crafting cost from 2 [Heavy Modular Frame](/wiki/Heavy_Modular_Frame "Heavy Modular Frame"), 3 [Motor](/wiki/Motor "Motor"), and 10 [Cable](/wiki/Cable "Cable") to 5 [Heavy Modular Frame](/wiki/Heavy_Modular_Frame "Heavy Modular Frame"), 10 [Motor](/wiki/Motor "Motor"), and 30 [Cable](/wiki/Cable "Cable")
  * [Patch Closed Alpha 4](/wiki/Patch_Closed_Alpha_4 "Patch Closed Alpha 4"): Improved the Oil Pump
  * [Patch 2018-10-11](/wiki/Patch_2018-10-11 "Patch 2018-10-11"): Introduced



## Early game development

Prior to Closed Alpha, the early game had an equivalent of the oil extractor which was called a oil pump. 

  * See also: [Game Development - Oil Extractor](/wiki/Early_game_development#Oil_Extractor "Early game development")



  * [v](/wiki/Template:BuildingNav "Template:BuildingNav")
  * [e](https://satisfactory.wiki.gg/wiki/Template:BuildingNav?action=edit)
  * [h](https://satisfactory.wiki.gg/wiki/Template:BuildingNav?action=history)

[Buildings](/wiki/Buildings "Buildings")  
---  
Special| [](/wiki/The_HUB "The HUB") [The HUB](/wiki/The_HUB "The HUB") • [](/wiki/MAM "MAM") [MAM](/wiki/MAM "MAM") • [](/wiki/Space_Elevator "Space Elevator") [Space Elevator](/wiki/Space_Elevator "Space Elevator") • [](/wiki/AWESOME_Sink "AWESOME Sink") [AWESOME Sink](/wiki/AWESOME_Sink "AWESOME Sink") • [](/wiki/AWESOME_Shop "AWESOME Shop") [AWESOME Shop](/wiki/AWESOME_Shop "AWESOME Shop") • [](/wiki/Blueprint_Designer "Blueprint Designer") [Blueprint Designer](/wiki/Blueprint_Designer "Blueprint Designer") • [](/wiki/Crafting_Bench "Crafting Bench") [Crafting Bench](/wiki/Crafting_Bench "Crafting Bench") • [](/wiki/Equipment_Workshop "Equipment Workshop") [Equipment Workshop](/wiki/Equipment_Workshop "Equipment Workshop")  
Production| | Extractors| [](/wiki/Miner "Miner") [Miner Mk.1](/wiki/Miner "Miner") ([Mk.2](/wiki/Miner#Mk.2-0 "Miner"), [Mk.3](/wiki/Miner#Mk.3-0 "Miner")) • [](/wiki/Water_Extractor "Water Extractor") [Water Extractor](/wiki/Water_Extractor "Water Extractor") • [](/wiki/Oil_Extractor "Oil Extractor") Oil Extractor • [](/wiki/Resource_Well_Pressurizer "Resource Well Pressurizer") [Resource Well Pressurizer](/wiki/Resource_Well_Pressurizer "Resource Well Pressurizer") ([Extractor](/wiki/Resource_Well_Pressurizer#Extractor "Resource Well Pressurizer"))  
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
  *[his]: his trivia section
