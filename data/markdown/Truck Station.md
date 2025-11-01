# Truck Station

## Truck Station  
  
[ ](/wiki/File:Truck_Station.png "Truck Station.png")

_Sends or receives resources to/from vehicles.  
Has 48 inventory slots.  
Transfers up to 120 stacks per minute to/from docked vehicles.   
Always refuels vehicles if it has access to a matching fuel type._

### Unlocked by

[Tier 3](/wiki/Tier_3 "Tier 3") \- Vehicular Transport

### Class name

Desc_TruckStation_C

## Building

### [Power  
usage](/wiki/Power "Power")

20 MW

### [Overclock­able](/wiki/Clock_speed "Clock speed")

No

### Conveyor  
inputs

3

### Conveyor  
outputs

2

## Dimensions

### Width

16 m

### Length

22 m

### Height

12 m

### Area

352 m2

## Ingre­dients

**15 ×[](/wiki/Modular_Frame "Modular Frame") [Modular Frame](/wiki/Modular_Frame "Modular Frame")**

**20 ×[](/wiki/Rotor "Rotor") [Rotor](/wiki/Rotor "Rotor")**

**50 ×[](/wiki/Cable "Cable") [Cable](/wiki/Cable "Cable")**

The **Truck Station** is a vehicle building used to automatically move cargo to/from motor [vehicles](/wiki/Vehicles "Vehicles") and refuel them. It is mostly used paired with automated vehicle routes, although it can operate standalone, such as for the purposes of quick refueling. It transfers 2 stacks of items per second (120 stacks per minute) to or from a docked vehicle. 

If maximum efficiency is important then using only [Conveyor Belts](/wiki/Conveyor_Belts "Conveyor Belts") are best since they require neither [power](/wiki/Power "Power") nor fuel. However, laying kilometers of belts is tedious and vehicles moving about are rather satisfying. 

## Contents

  * 1 Usage
    * 1.1 UI
    * 1.2 Ports
    * 1.3 Refueling
    * 1.4 Loading and unloading
    * 1.5 Power usage
    * 1.6 Automation
  * 2 Bottlenecks
  * 3 Example setups
    * 3.1 Two stations
    * 3.2 Four stations
    * 3.3 Three stations
    * 3.4 Dedicated fueling stations
  * 4 Narrative
  * 5 Trivia
  * 6 Gallery
  * 7 History
  * 8 Early game development
  * 9 References



## Usage

### UI

The Truck Station UI [1] has a similar look and feel to the train [Freight Platform UI](/wiki/Freight_Platform#UI "Freight Platform"), and depending on if the Truck Station is set to LOAD or UNLOAD will include information about: 

  * Max Transfer Rate (Load and Unload)
  * Outgoing Transfer Rate (Load Only)
  * Incoming Transfer Rate (Unload Only)



Additionally the Truck Station UI will show the [Fuel Consumption](/wiki/Vehicles#Fuel_consumption "Vehicles") per Minute used by all Vehicles on a connected automated vehicle Path / Route. 

There is NO OPTION to have Truck Stations do both Loading and Unloading in one cycle. 

The Truck Station is set to LOAD by default. Just toggle the button to set it to UNLOAD (or vice versa). 

  * [](/wiki/File:Truck_Station_UI.png "Update 5 - Example of Truck Station UI")

Update 5 - Example of Truck Station UI




### Ports

The Truck Station has three [Conveyor Belt](/wiki/Conveyor_Belt "Conveyor Belt") inputs and two Conveyor Belt outputs. [2]

Facing the ports side of the station, the leftmost input port _(leading into visual fuel tanks in the structure)_ is used for filling the Truck Station's [fuel](/wiki/Fuels "Fuels") slot only. 

The dual center inputs and dual right outputs are used for moving cargo into/out of the Truck Station. 

  * [](/wiki/File:Truck_Station_Ports_U5.png "Update 5 - Truck Station Ports")

Update 5 - Truck Station Ports




### Refueling

Refueling occurs always as long as the Truck Station has fuel to refuel and it is the same fuel that the vehicle stopped at the Truck Station already has. Vehicles only receive enough fuel to do a full roundtrip using the current recorded path. Truck Stations do not completely refuel the vehicle. 

### Loading and unloading

Whether the Station loads or unloads can be configured in the UI (see above). 

In order for a vehicle to dock, the Truck Station has to be powered and the vehicle has to be within the building hitbox of the Station. 

The loading / unloading animation takes about 5 to 9 seconds _(same as vehicle refuel wait time)_.[3]

During docking, 2 stacks of items (regardless of whether it is a full or partial stack) are transfered between the docked vehicle and the station every second. 

The docking process starts the moment a vehicle is within the interaction range of the station (indicated by the building hitbox). 

### Power usage

Power will be consumed while any vehicle is in range, even while no items are being moved. 

Once all vehicles are clear of the truck station, power usage drops to the standard 0.1 MW standby. 

### Automation

Automated Vehicles have to be instructed to stop at the Truck Station while recording, which is indicated by a "pause" node. The duration of the stop can be adjusted. 

  * See Also: [Vehicle Automation](/wiki/Vehicles#Automation "Vehicles")



## Bottlenecks

The following examples apply to an n-station setup with only one unloading station. 

The tractor can only carry 25 stacks of whatever it is you're loading onto it. A bottleneck would obviously occur if you're expecting more than 25 stacks of [Iron Ore](/wiki/Iron_Ore "Iron Ore") per roundtrip (as the tractor can only carry 25). Another bottleneck would occur if you're mining 120 Iron Ore/min but unloading 240/min (the unloading station will empty before the tractor returns), regardless of the length of the trip. Conversely, if you're mining 240/min and unloading 120/min the unloading station will fill up before it has a chance to empty, meaning there is a waste of materials. Clearly the total amount loaded should ideally equal the amount unloaded (per min) as long as you don't produce more than the tractor can carry – in this case multiple tractors will be needed. 

Assuming the truck starts its trip at point A and it takes 8 minutes exactly to go from A -> B -> C -> ... -> A then it will also take 8 minutes exactly (assuming any pauses are equal) to go from C -> ... -> A -> B -> C. This means if you're mining 240 Iron Ore per minute at C and the truck takes 8 minutes to go from A back to A again, the miner at C will have produced 8 * 240 = 1920 Iron Ore by the time the truck comes back to C (assuming it's not the first trip ever). 

Assuming mining rate equals output rate: if the total route time in minutes (for any roundtrip starting at any point along the way) is greater than the maximum item count per trip divided by the output rate (in items/minute) at the unloading station then you might encounter a bottleneck as the truck will take too long to do its full trip – the miners will produce more than the truck can carry _and_ the unloading station will empty before the truck comes back. 

An example: 

  * The tractor can carry a maximum of 2500 Iron Ore (25 * 100).
  * The unloading station is connected to two Mk.1 Conveyor Belts for a total output rate of 120 items/minute.
  * We're mining a total of 120 Iron Ore per minute.



It will therefore take the unloading station 2500 / 120 = 20.83 minutes to unload everything. If the total roundtrip time for the tractor takes more than 20.83 minutes, the miners will have produced more than the tractor can carry (21 minutes * 120 = 2520 Iron Ore) and the unloading station will have emptied before the tractor comes back (there will be a gap of 20 Iron Ore in the production line). 

## Example setups

### Two stations

  * Input: a miner on a pure coal node producing 120 units/min
  * Build a station near the coal node and connect fuel and one input
  * Build a second station near your base or a water source. Set this station to "Unload". Connect one output to your factory or coal generators.
  * Build a [tractor](/wiki/Tractor "Tractor") and record a round trip path



### Four stations

  * Input: overclocked or multiple miners producing 240 units/min of coal and a maximum of tier 2 belts (120 units/min)
  * Repeat the two station setup, but double the stations at each end. Make sure the single tractor visits all four. Only use multiple [tractors](/wiki/Tractor "Tractor") if the distance is causing throughput issues.



### Three stations

  * Inputs: 
    * A miner on a impure coal node producing 30 units/min
    * A miner on a pure quartz node producing 120 units/min
  * Build a truck station near the coal node. Set it to "Load". Leave it empty though, only connect the fueling portion to the coal miner.
  * Build a second truck station near the quartz node. Set this one to "Load" and connect one input to the quartz.
  * Build a third truck stop near your factory and connect one output. Set this one to "Unload".
  * Build a [tractor](/wiki/Tractor "Tractor") and record a round trip that visits all three stations at least once.



### Dedicated fueling stations

  * Input: A miner on a impure coal node producing 30 units/min
  * Build a truck station near the coal node. Set it to "Load" and connect both inputs.
  * For each truck station pair that lacks its own fuel source, build a dedicated station to receive coal. Set this station to "Unload" and connect one output to the fueling port of the other station.
  * Build a [tractor](/wiki/Tractor "Tractor") and record a round trip that visits all the dedicated fueling stations.



## Narrative

**Expand to reveal spoiler**

When performing specific actions, the player will hear [ADA](/wiki/ADA "ADA") speak. 

  * View [Story Player Actions - Pioneer Constructs](/wiki/Story#Player_Actions "Story") to read and hear individual ADA messages related to constructing a Truck Station.



## Trivia

  * [Factory Carts](/wiki/Factory_Cart "Factory Cart") work with Truck Stations. Despite not requiring fuel of any kind, Truck Stations will load fuel into the cart anyway. This does not provide any kind of bonus and the fuel slot cannot be accessed, and the cart will consume the fuel rapidly similar to a [Cyber Wagon](/wiki/Cyber_Wagon "Cyber Wagon"). To avoid the loading of fuel, it is recommend to not supply fuel to truck stations designed to operate on factory carts.



## Gallery

  * [](/wiki/File:Vehicle_loading_Base_E3.png "A Truck Station in the E3 2018 presentation, along with a Lookout Tower and Oil Refineries")

A Truck Station in the E3 2018 presentation, along with a [Lookout Tower](/wiki/Lookout_Tower "Lookout Tower") and [Oil Refineries](/wiki/Refinery "Refinery")

  * [](/wiki/File:Vehicle_loading_Base_E3_Alt.png "A closer up shot of the Truck Station in the E3 2018 presentation")

A closer up shot of the Truck Station in the E3 2018 presentation

  * [](/wiki/File:Truck_Station_U5.png "Update 5 - Truck Station New Look")

Update 5 - Truck Station New Look




## History

  * [Patch 0.6.0.10](/wiki/Patch_0.6.0.10 "Patch 0.6.0.10"): Names should save properly now
  * [Patch 0.6.0.4](/wiki/Patch_0.6.0.4 "Patch 0.6.0.4"): Fixed Truck Station UI requiring multiple presses of E or ESC to be closed after selecting Load or Unload
  * [Patch 0.6.0.2](/wiki/Patch_0.6.0.2 "Patch 0.6.0.2"): Fixed Truck Station inventories not being visible
  * [Patch 0.6.0.1](/wiki/Patch_0.6.0.1 "Patch 0.6.0.1")
    * Fixed a crash when [Multiplayer](/wiki/Multiplayer "Multiplayer") Clients and [Dedicated Servers](/wiki/Dedicated_Servers "Dedicated Servers") Clients would place a second Truck Station
    * Fixed the Truck Stations UI not showing up properly for Multiplayer Clients and Dedicated Servers Clients
    * Fixed a debug icon showing up on the Truck Station inventory when accessed for a second time by Multiplayer Clients and Dedicated Servers Clients
  * [Patch 0.5.2.1](/wiki/Patch_0.5.2.1 "Patch 0.5.2.1"): Fixed Truck Stations displaying at the center of the map
  * [Patch 0.5.1.12](/wiki/Patch_0.5.1.12 "Patch 0.5.1.12"): Fixed an issue with vehicle path recording inside factories sometimes recording docking to Truck Station on floors above the vehicle
  * [Patch 0.5.1.7](/wiki/Patch_0.5.1.7 "Patch 0.5.1.7"): Fixed bug where Vehicles weren’t placeable in the Truck Station docking area
  * [Patch 0.5.1.1](/wiki/Patch_0.5.1.1 "Patch 0.5.1.1")
    * Made Vehicles take available fuel for as long as they are docked
    * Fixed the fuel consumption metrics in the Truck Stations not accounting for pauses and docking times in the path time
  * [Patch 0.5.0.13](/wiki/Patch_0.5.0.13 "Patch 0.5.0.13")
    * Fixed an issue where [Vehicles](/wiki/Vehicles "Vehicles") would not receive fuel from a Truck Station]] if their fuel inventory was empty
    * Fixed an issue where Vehicle Paths were not updated after a Truck Station was built over them
    * Fixed issues with Vehicles getting out of sync with their Vehicle Stations after loading a game
  * [Patch 0.5.0.9](/wiki/Patch_0.5.0.9 "Patch 0.5.0.9")
    * Fixed a bug where vehicles could get stuck docking until their inventories were full
    * You can now press F to manually dock a vehicle on a Truck Station
    * Added tooltips to Vehicle Truck Station elements (Hover over)
  * [Patch 0.5.0.8](/wiki/Patch_0.5.0.8 "Patch 0.5.0.8"): Manually driven [Vehicles](/wiki/Vehicles "Vehicles") now take Fuel from Truck Stations
  * [Patch 0.5.0.0](/wiki/Patch_0.5.0.0 "Patch 0.5.0.0"): 
    * Updated Truck Station visuals
    * Additional Input and Output slots have been added to the Truck Station
    * Vehicles will now only take the proper amount of [fuel](/wiki/Fuels "Fuels") from a Truck Station that is needed to complete a full trip and they will not run out of fuel even when getting stuck or lost
    * Truck Station UI has been updated to show average fuel consumption and delivery throughput
    * Undocumented Change - Now can be renamed
  * [Patch 0.3.6.10](/wiki/Patch_0.3.6.10 "Patch 0.3.6.10"): Fixed distance field update settings on the Truck Station
  * [Patch 0.3.5.3](/wiki/Patch_0.3.5.3 "Patch 0.3.5.3"): Fuel inventory in Truck Stations no longer breaks after a client player interacts with the building
  * [Patch 0.3](/wiki/Patch_0.3 "Patch 0.3"): Fixed issue with clients being able to resources other than energy sources into the fuel slot of the Truck Station
  * [Patch 0.2.1.4](/wiki/Patch_0.2.1.4 "Patch 0.2.1.4"): Added to the Map
  * [Patch 0.1.15](/wiki/Patch_0.1.15 "Patch 0.1.15"): Changed Sending/Receiving back to Unloading/Loading for clarity
  * [Patch 0.1](/wiki/Patch_0.1 "Patch 0.1"): Fixed vehicles getting stuck in the Truck Station



## Early game development

Prior to Closed Alpha, in Sprint 23 (week 46) Truck Stations were first seen, despite Trucks and Tractors added earlier. Initially truck stations only had a "Load" function. 

  * See also: [Game Development - Truck Station](/wiki/Early_game_development#Truck_Station "Early game development")



## References

  1. ↑ [YouTube - Changes to Truck Station and Vehicle Automation coming in Update 5 - New Truck Station - UI](https://www.youtube.com/watch?v=kh3lVrBdjFE&t=77s)
  2. ↑ [YouTube - Changes to Truck Station and Vehicle Automation coming in Update 5 - New Truck Station - Ports](https://www.youtube.com/watch?v=kh3lVrBdjFE&t=69s)
  3. ↑ [YouTube - Satisfactory UPDATE 5 Experimental Release Countdown - Vehicle refueling wait time](https://www.youtube.com/watch?v=Rumqu_lyapg&t=5645s)



  * [v](/wiki/Template:VehicleNav "Template:VehicleNav")
  * [e](https://satisfactory.wiki.gg/wiki/Template:VehicleNav?action=edit)
  * [h](https://satisfactory.wiki.gg/wiki/Template:VehicleNav?action=history)

[Transportation](/wiki/Vehicles "Vehicles")  
---  
Motor vehicles| [](/wiki/Tractor "Tractor") [Tractor](/wiki/Tractor "Tractor") • [](/wiki/Truck "Truck") [Truck](/wiki/Truck "Truck") • [](/wiki/Explorer "Explorer") [Explorer](/wiki/Explorer "Explorer") • [](/wiki/Factory_Cart "Factory Cart") [Factory Cart](/wiki/Factory_Cart "Factory Cart") • [](/wiki/Golden_Factory_Cart "Golden Factory Cart") [Golden Factory Cart](/wiki/Golden_Factory_Cart "Golden Factory Cart") • [](/wiki/Cyber_Wagon "Cyber Wagon") [Cyber Wagon](/wiki/Cyber_Wagon "Cyber Wagon") • [](/wiki/Truck_Station "Truck Station") Truck Station • [](/wiki/Drone_Port "Drone Port") [Drone Port](/wiki/Drone_Port "Drone Port") • [](/wiki/Drone "Drone") [Drone](/wiki/Drone "Drone")  
Rail vehicles| [](/wiki/Electric_Locomotive "Electric Locomotive") [Electric Locomotive](/wiki/Electric_Locomotive "Electric Locomotive") • [](/wiki/Freight_Car "Freight Car") [Freight Car](/wiki/Freight_Car "Freight Car") • [](/wiki/Train_Station "Train Station") [Train Station](/wiki/Train_Station "Train Station") • [](/wiki/Freight_Platform "Freight Platform") [Freight Platform](/wiki/Freight_Platform "Freight Platform") • [](/wiki/Fluid_Freight_Platform "Fluid Freight Platform") [Fluid Freight Platform](/wiki/Fluid_Freight_Platform "Fluid Freight Platform") • [](/wiki/Empty_Platform "Empty Platform") [Empty Platform](/wiki/Empty_Platform "Empty Platform") • [](/wiki/Empty_Platform_With_Catwalk "Empty Platform With Catwalk") [Empty Platform With Catwalk](/wiki/Empty_Platform_With_Catwalk "Empty Platform With Catwalk") • [](/wiki/Railway "Railway") [Railway](/wiki/Railway "Railway") • [](/wiki/Railroad_Switch_Control "Railroad Switch Control") [Railroad Switch Control](/wiki/Railroad_Switch_Control "Railroad Switch Control") • [](/wiki/Buffer_Stop "Buffer Stop") [Buffer Stop](/wiki/Buffer_Stop "Buffer Stop") • [](/wiki/Block_Signal "Block Signal") [Block Signal](/wiki/Block_Signal "Block Signal") • [](/wiki/Path_Signal "Path Signal") [Path Signal](/wiki/Path_Signal "Path Signal")  
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
  
Transportation| | [Vehicle Transport](/wiki/Vehicles "Vehicles")| [](/wiki/Tractor "Tractor") [Tractor](/wiki/Tractor "Tractor") • [](/wiki/Truck "Truck") [Truck](/wiki/Truck "Truck") • [](/wiki/Cyber_Wagon "Cyber Wagon") [Cyber Wagon](/wiki/Cyber_Wagon "Cyber Wagon") • [](/wiki/Explorer "Explorer") [Explorer](/wiki/Explorer "Explorer") • [](/wiki/Factory_Cart "Factory Cart") [Factory Cart](/wiki/Factory_Cart "Factory Cart") ([Golden](/wiki/Golden_Factory_Cart "Golden Factory Cart")) • [](/wiki/Truck_Station "Truck Station") Truck Station • [](/wiki/Drone_Port "Drone Port") [Drone Port](/wiki/Drone_Port "Drone Port") • [](/wiki/Drone "Drone") [Drone](/wiki/Drone "Drone")  
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
