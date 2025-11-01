# Power Line

## Power Line

[ ](/wiki/File:Power_Line.png "Power Line.png")

_Connects Power Poles, Power Generators, and factory buildings._

### Unlocked by

[Tier 0](/wiki/Tier_0 "Tier 0") \- HUB Upgrade 2

### Class name

Desc_PowerLine_C

## Dimensions

### Width

0 m

### Length

1-300 m

### Height

0 m

## Ingre­dients

**1 ×[](/wiki/Cable "Cable") [Cable](/wiki/Cable "Cable")**

**Power Lines** are used to connect [Power Poles](/wiki/Power_Poles "Power Poles") and [buildings](/wiki/Building "Building") to provide or draw [power](/wiki/Power "Power"). Just like Power Poles, they have no capacity limit and can transmit as much power as provided, losslesly. 

Beside power transmitting capabilities, they also allow [Pioneers](/wiki/Pioneer "Pioneer") to travel on them using the [](/wiki/Zipline "Zipline") [Zipline](/wiki/Zipline "Zipline"). 

## Contents

  * 1 Construction
  * 2 Usage
  * 3 Tips
  * 4 Trivia
  * 5 See also
  * 6 History
  * 7 Early game development



## Construction

To start building a Power Line, at least one end of the connection must be already built (this can be either a [Power Pole](/wiki/Power_Pole "Power Pole"), Wall Outlet or any building). After confirming the first connection, if the destination target is not a building, a Power Pole or Wall Outlet will be added automatically on the ground or wall/ceiling respectively if possible; the additional cost of the Power Pole or Wall Outlet is taken into account when it is required. 

Most buildings may only have one Power Line connected to it, [Power Storages](/wiki/Power_Storage "Power Storage") and [Lights](/wiki/Lights "Lights") can have two; Power Poles four, seven or ten (based on the mark). It is advised to connect the other end of the Power Line to a Power Pole or Wall Outlet to allow further expansion of a power grid. 

A building with more than one connection cannot be connected to itself, with some exceptions. It is possible to connect both ends of a [Double Wall Outlet](/wiki/Power_Pole#Double_Wall_Outlets "Power Pole") together, which only reduces the amount of available connections on both sides by one, as they are already connected internally. It is also possible to connect both connectors of a [Power Switch](/wiki/Power_Switch "Power Switch") or [Lights Control Panel](/wiki/Lights_Control_Panel "Lights Control Panel"), which disallows the structures to connect to anything. 

The maximum length of a Power Line is 100 meters (12.5 [Foundation](/wiki/Foundation "Foundation") lengths) for the [Power Pole](/wiki/Power_Pole "Power Pole") and 300 meters (37,5 [Foundation](/wiki/Foundation "Foundation") lengths) for the [Power Tower](/wiki/Power_Tower "Power Tower") at the cost of one [Cable](/wiki/Cable "Cable") per 25 meters, rounded up. 

## Usage

Once a Power Line is built, there is no indication of how much or whether power is flowing through them. Power Poles, Generators and Switches only show the values for the whole grid. Power within Power Lines has no sense of current or voltage. 

Power Generators will not turn on without a Power Line connection. It is not checked whether there is any consumption, meaning connecting to a dead-end Power Pole, or even another Power Generator will suffice. 

Power Lines are "disconnected" simply by dismantling [`F`](/wiki/Controls "Controls") them. 

  
Power Lines can also independently be used to facilitate terrain traversal with the help of a [Zipline](/wiki/Zipline "Zipline") tool. 

## Tips

  * A Power Pole or Wall Outlet should have at least one connector reserved after all machines are connected; this allows connection of the pole/outlet to a power grid.
  * If a Power Pole or Wall Outlet reaches its maximum connections, no further Power Line connections can be added to it.
  * The number of current connections and the maximum connections are shown when aiming a new Power Line at a Pole/Outlet, but not on factory buildings.
  * Removing a Power Pole or Wall Outlet will also remove any connected Power Lines, returning their associated material cost in addition.



## Trivia

  * During [FICSMAS](/wiki/FICSMAS "FICSMAS"), if [FICSMAS Power Lights](/wiki/FICSMAS_Power_Light "FICSMAS Power Light") were unlocked, Power Lines could be "upgraded" into and from them. They were different only visually, otherwise having exactly the same properties as Power Lines have.



## See also

  * [](/wiki/Power_Pole "Power Pole") [Power Pole](/wiki/Power_Pole "Power Pole")
  * [](/wiki/Power_Switch "Power Switch") [Power Switch](/wiki/Power_Switch "Power Switch")
  * [](/wiki/Cable "Cable") [Cable](/wiki/Cable "Cable")
  * [](/wiki/FICSMAS_Power_Light "FICSMAS Power Light") [FICSMAS Power Light](/wiki/FICSMAS_Power_Light "FICSMAS Power Light")
  * [](/wiki/Zipline "Zipline") [Zipline](/wiki/Zipline "Zipline")



## History

  * [Patch 1.0.1.1](/wiki/Patch_1.0.1.1 "Patch 1.0.1.1"): Fixed a crash when Upgrading [Power Poles](/wiki/Power_Poles "Power Poles") or splitting a Wire from a Power Pole or Wall Outlets
  * [Patch 1.0.1.0](/wiki/Patch_1.0.1.0 "Patch 1.0.1.0")
    * Fixed Wires not being upgradable
    * Updated Physics of the Cables on the [Constructor](/wiki/Constructor "Constructor")
  * [Patch 0.8.2.5](/wiki/Patch_0.8.2.5 "Patch 0.8.2.5"): Fixed a crash for [Multiplayer](/wiki/Multiplayer "Multiplayer") / [Dedicated Server](/wiki/Dedicated_Server "Dedicated Server") Clients that sometimes occurred when trying to snap a [Power Pole](/wiki/Power_Pole "Power Pole") to a Power Line
  * [Patch 0.8.2.0](/wiki/Patch_0.8.2.0 "Patch 0.8.2.0")
    * Refactored wire splitting so it works with [Power Towers](/wiki/Power_Tower "Power Tower")
    * Fixed bug where build effects for wires never got cleaned up
    * Fixed so wire build effect works again
    * Fixed so [poles](/wiki/Power_Poles "Power Poles") created from wires copy the rotation of the pole you drag from
  * [Patch 0.8.0.0](/wiki/Patch_0.8.0.0 "Patch 0.8.0.0"): Made the automatic power connections when building Power Lines context sensitive, copying the same type of [pole](/wiki/Power_Pole "Power Pole") the Power Line was initially connected to
  * [Patch 0.7.1.1](/wiki/Patch_0.7.1.1 "Patch 0.7.1.1"): Fixed Multiplayer and Dedicated Server Clients not being able to place [Power Poles](/wiki/Power_Poles "Power Poles") off a Power Line|Power Cable in the [Blueprint Designer](/wiki/Blueprint_Designer "Blueprint Designer")
  * [Patch 0.6.0.6](/wiki/Patch_0.6.0.6 "Patch 0.6.0.6"): Fixed a crash when trying to snap a Power Line to another one during the second build step
  * [Patch 0.5.0.14](/wiki/Patch_0.5.0.14 "Patch 0.5.0.14"): Fixed Power Line Wires being completely stretched in certain scenarios
  * [Patch 0.5.0.13](/wiki/Patch_0.5.0.13 "Patch 0.5.0.13"): Fixed Power Lines being able to be selected as a [Customizer](/wiki/Customizer "Customizer") target which would then result in them looking weird when a colour swatch was applied
  * [Patch 0.3.7.4](/wiki/Patch_0.3.7.4 "Patch 0.3.7.4"): Fixed a bug where the power icon would look out of place for Client after upgrading Power Lines
  * [Patch 0.3.7.2](/wiki/Patch_0.3.7.2 "Patch 0.3.7.2"): Power Lines can now be upgraded to FICSMAS Power Lights and vice versa
  * [Patch 0.3.4.9](/wiki/Patch_0.3.4.9 "Patch 0.3.4.9"): Power Lines should be easier to dismantle again
  * [Patch 0.3](/wiki/Patch_0.3 "Patch 0.3"): 
    * Power Poles placed when building Power Lines now snap to the foundation grid
    * Power Lines can now be built through player-built structures without restrictions
  * [Patch 0.1.8](/wiki/Patch_0.1.8 "Patch 0.1.8"): Fixed a crash related to Power Lines being saved in a bad state
  * [Patch 0.1.5](/wiki/Patch_0.1.5 "Patch 0.1.5"): Fixed a bug with the cost of Power Lines not updating correctly while building



## Early game development

Prior to Closed Alpha, early on, power lines did not need [Cable](/wiki/Cable "Cable") to be crafted in order to use, but could be placed as needed. 

  * See also: [Game Development - Power Line](/wiki/Early_game_development#Power_Line "Early game development")



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
Power Grid| [](/wiki/Power_Poles "Power Poles") [Power Poles](/wiki/Power_Poles "Power Poles") • [](/wiki/Wall_Outlets "Wall Outlets") [Wall Outlets](/wiki/Wall_Outlets "Wall Outlets") • [](/wiki/Power_Tower "Power Tower") [Power Tower](/wiki/Power_Tower "Power Tower") • [](/wiki/Power_Line "Power Line") Power Line • [](/wiki/Power_Switch "Power Switch") [Power Switch](/wiki/Power_Switch "Power Switch") • [](/wiki/Priority_Power_Switch "Priority Power Switch") [Priority Power Switch](/wiki/Priority_Power_Switch "Priority Power Switch") • [](/wiki/Power_Storage "Power Storage") [Power Storage](/wiki/Power_Storage "Power Storage")  
  
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
