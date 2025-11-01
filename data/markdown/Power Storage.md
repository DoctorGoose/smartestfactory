# Power Storage

## Power Storage

[ ](/wiki/File:Power_Storage.png "Power Storage.png")

_Connects to a power grid to store excess power produced. The stored power can be harnessed if power grid consumption exceeds production.  
Storage Capacity: 100 MWh (100 MW for 1 hour)  
Maximum Charge Rate: 100 MW  
Maximum Discharge Rate: Unlimited_

### Unlocked by

[Tier 4](/wiki/Tier_4 "Tier 4") \- Expanded Power Infrastructure

### Class name

Desc_PowerStorageMk1_C

## Dimensions

### Width

6 m

### Length

6 m

### Height

12 m

### Area

36 m2

## Ingre­dients

**5 ×[](/wiki/Encased_Industrial_Beam "Encased Industrial Beam") [Encased Industrial Beam](/wiki/Encased_Industrial_Beam "Encased Industrial Beam")**

**10 ×[](/wiki/Modular_Frame "Modular Frame") [Modular Frame](/wiki/Modular_Frame "Modular Frame")**

**100 ×[](/wiki/Wire "Wire") [Wire](/wiki/Wire "Wire")**

The **Power Storage** is a mid-game [building](/wiki/Building "Building") used for buffering [electrical](/wiki/Power "Power") energy. Each can store up to 100 MWh, or 100 MW for 1 hour. As it allows 2 power connections, multiple Power Storages can be daisy-chained to store large amounts of energy. 

## Contents

  * 1 Usage
    * 1.1 Charge indicator
    * 1.2 Buffering fluctuating power
  * 2 Trivia
  * 3 History



## Usage

When connected to a power grid that is supplied by generators other than [Biomass Burners](/wiki/Biomass_Burner "Biomass Burner"), it will charge using the excess generated power, up to a rate of 100 MW each. Therefore, it will take at least an hour in real-time to fully charge an empty Power Storage, or longer if the spare power is less than to satisfy all Power Storages on the grid (Power Storages that are not fully charged will split the spare power, reducing their charge rate to the available spare power divided by the number of partially charged Power Storages). Charging Power Storage does not add to the grid power consumption or max consumption figures, nor does it diminish capacity since it will slow or stop charging if there are other demands for the available power. 

As long as there is stored charge in the Power Storage and there is a power shortage (consumption exceeding production), all Power Storages will discharge to satisfy the difference, powering up instantly. There is no limit on the discharge rate; it will exactly match the power deficiency. The Power Storage will emit a warning similar to a power grid trip when any Power Storage discharges below 80% capacity. This allows the pioneer to quickly react to restore the power situation, whether to increase power production or to install a [Power Switch](/wiki/Power_Switch "Power Switch"). Once all the stored energy has been discharged and the power is still insufficient, the power grid will trip. 

There are two meters in the Power Storage interface. The left meter is the individual Power Storage charge level. The right meter is the collective charge level of all Power Storage attached to the grid. 

Connecting additional Power Storages will not impact the individual charge level of other Power Storages, but will reduce the charge level of the system on the right meter. This will also increase the time remaining until full charge. Power Storages cannot charge each other. 

### Charge indicator

Power Storage lacks an [Indicator Light](/wiki/Indicator_Light "Indicator Light"); instead, a charge indicator bar is displayed on the structure, in the power graph and in the Power Storage UI, showing how much energy is stored. It is colored as follows: 

  * Blue – Charging
  * Orange – Discharging (the upper part of the building rises and begins to spin)
  * Grey – Idle (either full capacity or there is no power to charge with nor discharge)



The power graph and Power Storage UI displays time to fully charge/discharge at the current power input/drain. 

### Buffering fluctuating power

Power Storages can be used to buffer fluctuating power generation and consumption. These fluctuations can be divided into avoidable and unavoidable: 

  * Avoidable fluctuations are caused by factories running below 100% efficiency, and thus stalling due to resource starvation or backup
  * Unavoidable fluctuations are caused by buildings that either aren't always in operation at all times, or by buildings that only operate with fluctuating power: 
    * Buildings which aren't always in operation include [Truck Stations](/wiki/Truck_Station "Truck Station"), [Freight Platforms](/wiki/Freight_Platform "Freight Platform"), [Electric Locomotives](/wiki/Electric_Locomotive "Electric Locomotive"), etc. Their power draw is chaotic and cannot be reliably nullified.
    * Buildings that operate with fluctuating power are [Geothermal Generators](/wiki/Geothermal_Generator "Geothermal Generator") (generation) and [Particle Accelerators](/wiki/Particle_Accelerator "Particle Accelerator"), [Converters](/wiki/Converter "Converter") and [Quantum Encoders](/wiki/Quantum_Encoder "Quantum Encoder") (consumption).  
Their fluctuations can be reliably nullified by building enough Power Storages to bridge the difference between their average and maximum power. In this case, Power Storages aren't expected to charge fully, only to provide a temporary buffer for each cycle.



The amount of Power Storages can be calculated as  
Power Storages = Maximum power − Average power100

Average power is calculated by averaging maximum and minimum power. 100 is the maximum charge rate of a Power Storage. In case a decimal amount of Power Storages is required, round up. See the below example for buffering a Geothermal Generator: 

Power Storages to buffer a Geothermal Generator  Geyser | Power | Average power | Difference between  
average and max | Power Storages  
required   
---|---|---|---|---  
Impure | 50–150 MW | 100 MW | 50 MW | 0.5   
Normal | 100–300 MW | 200 MW | 100 MW | 1   
Pure | 200–600 MW | 400 MW | 200 MW | 2   
  
As 0.5 Power Storages are required to buffer an impure Geothermal Generator, one Power Storage can buffer two impure Geothermal Generators. 

## Trivia

  * The energy of fuels is stored in MJ. 100 MWh equals to 360,000 MJ, meaning one Power Storage can store the following amount of energy: 
    * 24,000 [](/wiki/Leaves "Leaves") [Leaves](/wiki/Leaves "Leaves")
    * 2,000 [](/wiki/Biomass "Biomass") [Biomass](/wiki/Biomass "Biomass")
    * 1,200 [](/wiki/Coal "Coal") [Coal](/wiki/Coal "Coal")
    * 800 [](/wiki/Solid_Biofuel "Solid Biofuel") [Solid Biofuel](/wiki/Solid_Biofuel "Solid Biofuel")
    * 480 m3 [](/wiki/Fuel "Fuel") [Fuel](/wiki/Fuel "Fuel")
    * 180 m3 [](/wiki/Turbofuel "Turbofuel") [Turbofuel](/wiki/Turbofuel "Turbofuel")
    * 100 m3 [](/wiki/Rocket_Fuel "Rocket Fuel") [Rocket Fuel](/wiki/Rocket_Fuel "Rocket Fuel")
    * 72 m3 [](/wiki/Ionized_Fuel "Ionized Fuel") [Ionized Fuel](/wiki/Ionized_Fuel "Ionized Fuel")
    * 60 [](/wiki/Battery "Battery") [Batteries](/wiki/Battery "Battery")
    * 2.4 [](/wiki/Ficsonium_Fuel_Rod "Ficsonium Fuel Rod") [Ficsonium Fuel Rods](/wiki/Ficsonium_Fuel_Rod "Ficsonium Fuel Rod")
    * 0.48 [](/wiki/Uranium_Fuel_Rod "Uranium Fuel Rod") [Uranium Fuel Rods](/wiki/Uranium_Fuel_Rod "Uranium Fuel Rod")
    * 0.24 [](/wiki/Plutonium_Fuel_Rod "Plutonium Fuel Rod") [Plutonium Fuel Rods](/wiki/Plutonium_Fuel_Rod "Plutonium Fuel Rod")



## History

  * [Patch 1.0](/wiki/Patch_1.0 "Patch 1.0"): Changed 5 Stator cost to 5 Encased Industrial Beam
  * [Patch 0.4.0.0](/wiki/Patch_0.4.0.0 "Patch 0.4.0.0"): Introduced



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
Power Grid| [](/wiki/Power_Poles "Power Poles") [Power Poles](/wiki/Power_Poles "Power Poles") • [](/wiki/Wall_Outlets "Wall Outlets") [Wall Outlets](/wiki/Wall_Outlets "Wall Outlets") • [](/wiki/Power_Tower "Power Tower") [Power Tower](/wiki/Power_Tower "Power Tower") • [](/wiki/Power_Line "Power Line") [Power Line](/wiki/Power_Line "Power Line") • [](/wiki/Power_Switch "Power Switch") [Power Switch](/wiki/Power_Switch "Power Switch") • [](/wiki/Priority_Power_Switch "Priority Power Switch") [Priority Power Switch](/wiki/Priority_Power_Switch "Priority Power Switch") • [](/wiki/Power_Storage "Power Storage") Power Storage  
  
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
