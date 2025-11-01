# Coal-Powered Generator

## Coal-Powered Generator  
  
[ ](/wiki/File:Coal-Powered_Generator.png "Coal-Powered Generator.png")

_Burns Coal to boil Water. The steam produced rotates turbines that generate electricity for the power grid.  
Has Conveyor Belt and Pipeline input ports that allow the Coal and Water supply to be automated.  
Caution: Always generates power at the set clock speed. Shuts down if fuel requirements are not met._

### Unlocked by

[Tier 3](/wiki/Tier_3 "Tier 3") \- Coal Power

### Class name

Desc_GeneratorCoal_C

## Building

### [Power  
generated](/wiki/Power "Power")

75 MW

### [Overclock­able](/wiki/Clock_speed "Clock speed")

Yes

### Conveyor  
inputs

1

### Pipeline  
inputs

1

## Dimensions

### Width

10 m

### Length

26 m

### Height

36 m

### Area

260 m2

## Fuel

### Supplement  
input rate

45 / min

  * **[](/wiki/Petroleum_Coke "Petroleum Coke")[Petroleum Coke](/wiki/Petroleum_Coke "Petroleum Coke")** \+ [](/wiki/Water "Water") [Water](/wiki/Water "Water")
  * **[](/wiki/Coal "Coal")[Coal](/wiki/Coal "Coal")** \+ [](/wiki/Water "Water") [Water](/wiki/Water "Water")
  * **[](/wiki/Compacted_Coal "Compacted Coal")[Compacted Coal](/wiki/Compacted_Coal "Compacted Coal")** \+ [](/wiki/Water "Water") [Water](/wiki/Water "Water")



## Ingre­dients

**20 ×[](/wiki/Reinforced_Iron_Plate "Reinforced Iron Plate") [Reinforced Iron Plate](/wiki/Reinforced_Iron_Plate "Reinforced Iron Plate")**

**10 ×[](/wiki/Rotor "Rotor") [Rotor](/wiki/Rotor "Rotor")**

**30 ×[](/wiki/Cable "Cable") [Cable](/wiki/Cable "Cable")**

The **Coal-Powered Generator** is a [power generator](/wiki/Power_generator "Power generator") [building](/wiki/Building "Building") that generates [power](/wiki/Power "Power") by burning [](/wiki/Coal "Coal") [Coal](/wiki/Coal "Coal"), [](/wiki/Compacted_Coal "Compacted Coal") [Compacted Coal](/wiki/Compacted_Coal "Compacted Coal") or [](/wiki/Petroleum_Coke "Petroleum Coke") [Petroleum Coke](/wiki/Petroleum_Coke "Petroleum Coke") and [](/wiki/Water "Water") [Water](/wiki/Water "Water"). It is the first fully automated power source the pioneer has access to and also the first power source to use a mined resource. 

One Coal-Powered Generator produces 75 MW at 100% [clock speed](/wiki/Clock_speed "Clock speed"). 

## Contents

  * 1 Fuel consumption
  * 2 Generators per Coal node
  * 3 Generators fueled by Compacted Coal
  * 4 Generators fueled by Petroleum Coke
  * 5 Overclocking
  * 6 Coal power setup tutorial
  * 7 External link
  * 8 Current issues
  * 9 Narrative
  * 10 See also
  * 11 Gallery
  * 12 History
  * 13 Early game development



## Fuel consumption

At 100% clock speed, one Coal-Powered Generator consumes 45 m3 [Water](/wiki/Water "Water")/min, no matter what fuel is used. 

This means 3 [Water Extractors](/wiki/Water_Extractor "Water Extractor") will produce enough water for 8 Coal-Powered Generators, provided the 300 m3/min throughput limit of the Mk.1 Pipeline isn't exceeded (see below for a layout of possible setups which don't exceed the Pipeline limit). 

Fuel type | Energy (MJ) | Stack size | **Stack energy (MJ)** | Burn time (sec) | **Items per minute**  
---|---|---|---|---|---  
[](/wiki/Coal "Coal") [Coal](/wiki/Coal "Coal") | 300 | 100 | 30,000 | 4 | 15   
[](/wiki/Compacted_Coal "Compacted Coal") [Compacted Coal](/wiki/Compacted_Coal "Compacted Coal") | 630 | 100 | 63,000 | 8.4 | 7.142857   
[](/wiki/Petroleum_Coke "Petroleum Coke") [Petroleum Coke](/wiki/Petroleum_Coke "Petroleum Coke") | 180 | 200 | 36,000 | 2.4 | 25   
  
## Generators per Coal node

Use the following equations:  
Number of Coal-Powered Generators required:  
`Coal-Powered Generator = Coal mining rate / 15`  
Number of Water Extractors required:  
`Water Extractor = Coal-Powered Generator / 2.6̅6̅6̅6`  
Spread out the water supply across multiple pipelines as following:  
`Pipelines required = Coal-Powered Generator / 6.6̅6̅6̅6`  


  * Coal burn time is four seconds, which means that a single Coal-Powered Generator consumes 15 Coal/min.
  * [Pipelines Mk.1](/wiki/Pipeline#Mk.1 "Pipeline") only have a capacity of 300 m3/min. Thus, when connecting Water Extractors to a line feeding seven or more Coal-Powered Generators, Water inputs either need to be spaced out or be separated. 
    * Alternatively, [underclock](/wiki/Underclock "Underclock") Water Extractors to 75% and connect each of them to exactly two Coal-Powered Generators. That way, the number of Water Extractors is half the number of Coal-Powered Generators.
    * Using Water Extractors underclocked to 75% require an additional extractor for every eight Coal-Powered Generators, trading space for ratio simplicity. For eight Coal-Powered Generators you either need three Water Extractors at 100% (3 * 20 = 60 MW) or four Water Extractors at 75% (4 * 12.6 = 50.4 MW). This can be useful early on when you still need to save up on energy consumption on Water Extractors.
    * A Water Extractor has about the same width as two Coal-Powered Generators so it would be easier to tile the layout.
  * [Pipelines Mk.2](/wiki/Pipeline#Mk.2 "Pipeline") have a capacity of 600 m3/min. Thus up to 13 Coal-Powered Generators and 5 Water Extractors can be connected to a single Mk.2 Pipeline.
  * As the Miner and Water Extractors consume power, the net power capacity is less. 
    * Water Extractors use about 10% of the gross Power generated. After subtracting 10% from the gross Power, subtract the Power consumption from the [Miners](/wiki/Miner "Miner"), [Pipeline Pumps](/wiki/Pipeline_Pump "Pipeline Pump"), [vehicles](/wiki/Vehicle "Vehicle"), etc. to calculate the net power produced.



100% Miner250% Miner

A 100% [Miner](/wiki/Miner "Miner") on a [Coal](/wiki/Coal "Coal") node can support the following number of Coal-Powered Generators operating at 100% power usage (decimal amounts of machines means that the last machine needs to be [underclocked](/wiki/Underclock "Underclock") for maximum efficiency): 

Miner | Node  
purity | Coal/min | [Water Extractors  
(@ 100%)](/wiki/Water_Extractor "Water Extractor") | [Water Extractors  
(@ 75%)](/wiki/Water_Extractor "Water Extractor") | Water m3/min | No. of  
Coal-Powered Generators | Gross power   
---|---|---|---|---|---|---|---  
**Mk.1** | Impure | 30 | 0.75 | 1 | 90 | 2 | 150 MW   
Normal | 60 | 1.5 | 2 | 180 | 4 | 300 MW   
Pure | 120 | 3 | 4 | 360 | 8 | 600 MW   
**Mk.2** | Impure | 60 | 1.5 | 2 | 180 | 4 | 300 MW   
Normal | 120 | 3 | 4 | 360 | 8 | 600 MW   
Pure | 240 | 6 | 8 | 720 | 16 | 1200 MW   
**Mk.3** | Impure | 120 | 3 | 4 | 360 | 8 | 600 MW   
Normal | 240 | 6 | 8 | 720 | 16 | 1200 MW   
Pure | 480 | 12 | 16 | 1440 | 32 | 2400 MW   
  
A 250% [Miner](/wiki/Miner "Miner") on a [Coal](/wiki/Coal "Coal") node can support the following number of Coal-Powered Generators operating at 100% power usage (decimal amounts of machines means that the last machine needs to be [underclocked](/wiki/Underclock "Underclock") for maximum efficiency): 

Miner | Node  
purity | Coal/min | [Water Extractors  
(@ 100%)](/wiki/Water_Extractor "Water Extractor") | [Water Extractors  
(@ 75%)](/wiki/Water_Extractor "Water Extractor") | Water m3/min | No. of  
Coal-Powered Generators | Gross power   
---|---|---|---|---|---|---|---  
**Mk.1** | Impure | 75 | 1.875 | 2.5 | 225 | 5 | 375 MW   
Normal | 150 | 3.75 | 5 | 450 | 10 | 750 MW   
Pure | 300 | 7.5 | 10 | 900 | 20 | 1500 MW   
**Mk.2** | Impure | 150 | 3.75 | 5 | 450 | 10 | 750 MW   
Normal | 300 | 7.5 | 10 | 900 | 20 | 1500 MW   
Pure | 600 | 15 | 20 | 1800 | 40 | 3000 MW   
**Mk.3** | Impure | 300 | 7.5 | 10 | 900 | 20 | 1500 MW   
Normal | 600 | 15 | 20 | 1800 | 40 | 3000 MW   
Pure | 1200 | 30 | 40 | 3600 | 80 | 6000 MW   
  
## Generators fueled by Compacted Coal

This is a simplified version of the table above that does the same calculations for [](/wiki/Compacted_Coal "Compacted Coal") [Compacted Coal](/wiki/Compacted_Coal "Compacted Coal") as input, so only 7.143 items per minute instead of 15 are needed. This means that belt with 50 Compacted Coal per minute will feed exactly 7 generators on 100%. 

Each Assembler operates at 25 parts per minute. 

Coal and Sulfur/min  | No. of  
Assemblers (@100%)  | Compacted Coal/min  | Water Extractors  
(@100%)  | No. of  
Coal-Powered Generators  | Gross power   
---|---|---|---|---|---  
60  | 2.4  | 60  | 3.15  | 8.4  | 630 MW   
120  | 4.8  | 120  | 6.3  | 16.8  | 1260 MW   
240  | 9.6  | 240  | 12.6  | 33.6  | 2520 MW   
480  | 19.2  | 480  | 25.2  | 67.2  | 5040 MW   
780  | 31.2  | 780  | 40.95  | 109.2  | 8190 MW   
  
## Generators fueled by Petroleum Coke

Burning [](/wiki/Petroleum_Coke "Petroleum Coke") [Petroleum Coke](/wiki/Petroleum_Coke "Petroleum Coke") for power can be a great way to deal with [Heavy Oil Residue](/wiki/Heavy_Oil_Residue "Heavy Oil Residue"), as long as overflow is handled (to prevent the Coke from backing up, which would result in Heavy Oil Residue backing up and subsequently Plastic or Rubber production stopping). One Coal-Powered Generator consumes 25 Coke per minute. 

As the amount of Heavy Oil Residue can vary significantly based on what recipes are used, the table below only calculates with Heavy Oil Residue and not [Crude Oil](/wiki/Crude_Oil "Crude Oil"). 

Heavy Oil Residue/min  | No. of  
Coke Refineries  | Petroleum Coke/min  | Water Extractors  
(@100%)  | No. of  
Coal-Powered Generators  | Gross power   
---|---|---|---|---|---  
40  | 1  | 120  | 1.8  | 4.8  | 360 MW   
100  | 2.5  | 300  | 4.5  | 12  | 900 MW   
120  | 3  | 360  | 5.4  | 14.4  | 1080 MW   
200  | 5  | 600  | 9  | 24  | 1800 MW   
260  | 6.5  | 780  | 11.7  | 31.2  | 2340 MW   
300  | 7.5  | 900  | 13.5  | 36  | 2700 MW   
400  | 10  | 1200  | 18  | 48  | 3600 MW   
  
## Overclocking

_Main article:_[Clock speed](/wiki/Clock_speed "Clock speed")

The Coal-Powered Generator can be overclocked using [Power Shards](/wiki/Power_Shard "Power Shard"). Overclocking increases the fuel and Water consumption rate and produced power linearly. The same amount of power is always produced from the same input resources. 

## Coal power setup tutorial

See the pages below for guides. The guide is written based on [Rocky Desert](/wiki/Rocky_Desert "Rocky Desert") starting area, but can also be applicable for other areas with four [Coal](/wiki/Coal "Coal") nodes and with [Water](/wiki/Water "Water") nearby. 

  * [Part 1](/wiki/Tutorial:How_to_play#Coal_Power "Tutorial:How to play")
  * [Part 2](/wiki/Tutorial:How_to_play#Coal_Power_2 "Tutorial:How to play")
  * [Part 3](/wiki/Tutorial:How_to_play#Coal_Power_3 "Tutorial:How to play")



## External link

  * [An in-depth guide for Coal and Fuel power](https://steamcommunity.com/sharedfiles/filedetails/?id=2124946046)



## Current issues

  * Since the release of [1.0](/wiki/1.0 "1.0"), Coal-Powered Generators no longer have the startup or continuous spin animation on their turbine, despite operating normally.



## Narrative

**Expand to reveal spoiler**

When performing specific actions, the player will hear [ADA](/wiki/ADA "ADA") speak. 

  * View [Story Player Actions - Pioneer Constructs](/wiki/Story#Player_Actions "Story") to read and hear individual ADA messages related to constructing a Coal-Powered Generator.



## See also

  * [](/wiki/Coal "Coal") [Coal](/wiki/Coal "Coal")
  * [](/wiki/Compacted_Coal "Compacted Coal") [Compacted Coal](/wiki/Compacted_Coal "Compacted Coal")
  * [](/wiki/Petroleum_Coke "Petroleum Coke") [Petroleum Coke](/wiki/Petroleum_Coke "Petroleum Coke")
  * [](/wiki/Water_Extractor "Water Extractor") [Water Extractor](/wiki/Water_Extractor "Water Extractor")
  * [](/wiki/Biomass_Burner "Biomass Burner") [Biomass Burner](/wiki/Biomass_Burner "Biomass Burner")
  * [](/wiki/Fuel_Generator "Fuel Generator") [Fuel Generator](/wiki/Fuel_Generator "Fuel Generator")
  * [](/wiki/Geothermal_Generator "Geothermal Generator") [Geothermal Generator](/wiki/Geothermal_Generator "Geothermal Generator")
  * [](/wiki/Nuclear_Power_Plant "Nuclear Power Plant") [Nuclear Power Plant](/wiki/Nuclear_Power_Plant "Nuclear Power Plant")



## Gallery

  * [](/wiki/File:Coal_Generator_Schematic.png "Common setups for Coal Generators respecting the 8:3 ratio, with no throughput limits.")

Common setups for Coal Generators respecting the 8:3 ratio, with no throughput limits.

  * [](/wiki/File:Coal_generator_pipe_analysis.png "Flow rate analysis of a possible piping setup.")

Flow rate analysis of a possible piping setup.

  * [](/wiki/File:Coal_power_Water_Extractor.png "Top view of three Extractors to eight Generators setup, using a common pipeline and two Mk.1 belts, each feed into four generators. The 2 Mk.1 belts can be merged to a single Mk.2 belt.")

Top view of three Extractors to eight Generators setup, using a common pipeline and two Mk.1 belts, each feed into four generators. The 2 Mk.1 [belts](/wiki/Belt "Belt") can be merged to a single Mk.2 belt.

  * [](/wiki/File:Coal_power_ladder.png "Several Coal Generators viewed from the front.")

Several Coal Generators viewed from the front.

  * [](/wiki/File:Coal_Generator_Manifold_2.png "A few more Coal Generators, built-in double manifold style.")

A few more Coal Generators, built-in double [manifold](/wiki/Manifold "Manifold") style.

  * [](/wiki/File:Coal_Power_elevated.png "Coal Generators built above Water Extractors. Each row has nine Generators, fed by two vertical pipes in groups of four. Two vertical pipes are combined at the bottom-fed by three Extractors. The 9th generator has its own individual pipe and Extractor.")

Coal Generators built above [Water Extractors](/wiki/Water_Extractor "Water Extractor"). Each row has nine Generators, fed by two vertical pipes in groups of four. Two vertical pipes are combined at the bottom-fed by three Extractors. The 9th generator has its own individual pipe and Extractor.

  * [](/wiki/File:Coal_Generator_old.png "Coal running into a Coal Generator in a pre-alpha build of the game.")

[Coal](/wiki/Coal "Coal") running into a Coal Generator in a pre-alpha build of the game.

  * [](/wiki/File:Coal_Generator_x_16_%2B_Water_Extractor_x_6.png "A setup of 16 Coal Generators on six Water Extractors with Mk.2 Pipelines and one Pipeline Pump per line, no doubled-lines, no redundancies.")

A setup of 16 Coal Generators on six Water Extractors with Mk.2 Pipelines and one Pipeline Pump per line, no doubled-lines, no redundancies. 




## History

  * [Patch 1.0.1.0](/wiki/Patch_1.0.1.0 "Patch 1.0.1.0"): [Copy pasting settings](/wiki/Controls "Controls"), using [`Right Ctrl`](/wiki/Controls "Controls")+[`C`](/wiki/Controls "Controls") and [`Right Ctrl`](/wiki/Controls "Controls")+[`V`](/wiki/Controls "Controls"), now works on [Generators](/wiki/Power "Power") and Extractors ([Water](/wiki/Water_Extractor "Water Extractor"),[Oil](/wiki/Oil_Extractor "Oil Extractor"),[Resource Well](/wiki/Resource_Well_Pressurizer "Resource Well Pressurizer"))
  * [Patch 1.0.0.4](/wiki/Patch_1.0.0.4 "Patch 1.0.0.4"): Lowered Coal-Powered Generator volume
  * [Patch 1.0.0.1](/wiki/Patch_1.0.0.1 "Patch 1.0.0.1"): Fixed an issue where Coal-Powered Generators would stop working after interacting with them in some scenarios
  * [Patch 1.0](/wiki/Patch_1.0 "Patch 1.0"): Renamed from Coal Generator to Coal-Powered Generator
  * [Patch 0.7.1.1](/wiki/Patch_0.7.1.1 "Patch 0.7.1.1"): Fixed being able to place Coal-Powered Generators at the edge of Blueprints and still have them hook to power
  * [Patch 0.3.8.2](/wiki/Patch_0.3.8.2 "Patch 0.3.8.2"): Fixed Fluid indicator UI not displaying properly in the Coal-Powered Generator
  * [Patch 0.3](/wiki/Patch_0.3 "Patch 0.3"): Now requires Water to operate, appearance changed accordingly to include a Pipeline input. The chimney is now fully within the hitbox.



## Early game development

Prior to Closed Alpha, in Sprint 6 (week 12) the Coal-Powered Generator was introduced with a more simplistic design and was used in addition to the [Wind Turbine](/wiki/Early_game_development#Wind_Turbine "Early game development") as an alternate power generator. 

  * See also: [Game Development - Coal-Powered Generator](/wiki/Early_game_development#Coal_Generator "Early game development")



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
  
[Power](/wiki/Power "Power")| | Generators| [](/wiki/Biomass_Burner "Biomass Burner") [Biomass Burner](/wiki/Biomass_Burner "Biomass Burner") • [](/wiki/Coal-Powered_Generator "Coal-Powered Generator") Coal-Powered Generator • [](/wiki/Fuel-Powered_Generator "Fuel-Powered Generator") [Fuel-Powered Generator](/wiki/Fuel-Powered_Generator "Fuel-Powered Generator") • [](/wiki/Geothermal_Generator "Geothermal Generator") [Geothermal Generator](/wiki/Geothermal_Generator "Geothermal Generator") • [](/wiki/Nuclear_Power_Plant "Nuclear Power Plant") [Nuclear Power Plant](/wiki/Nuclear_Power_Plant "Nuclear Power Plant") • [](/wiki/Alien_Power_Augmenter "Alien Power Augmenter") [Alien Power Augmenter](/wiki/Alien_Power_Augmenter "Alien Power Augmenter")  
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
