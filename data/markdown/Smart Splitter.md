# Smart Splitter

## Smart Splitter  
  
[ ](/wiki/File:Smart_Splitter.png "Smart Splitter.png")

_Splits one Conveyor Belt into two or three.  
A filter can be set for each output to allow a specific part to pass through._

### Unlocked by

[MAM Caterium Research](/wiki/Caterium_Research "Caterium Research") \- Smart Splitter

### Class name

Desc_ConveyorAttachmentSplitterSmart_C

## Building

### Conveyor  
inputs

1

### Conveyor  
outputs

3

## Dimensions

### Width

4 m

### Length

4 m

### Height

2n+1 m

### Area

16 m2

Stackable

## Ingre­dients

**2 ×[](/wiki/Reinforced_Iron_Plate "Reinforced Iron Plate") [Reinforced Iron Plate](/wiki/Reinforced_Iron_Plate "Reinforced Iron Plate")**

**2 ×[](/wiki/Rotor "Rotor") [Rotor](/wiki/Rotor "Rotor")**

**1 ×[](/wiki/AI_Limiter "AI Limiter") [AI Limiter](/wiki/AI_Limiter "AI Limiter")**

The **Smart Splitter** is an upgraded version of the [Splitter](/wiki/Splitter "Splitter") capable of filtering its input and handling overflow. 

Given the most advanced item required to unlock them is the [](/wiki/AI_Limiter "AI Limiter") [AI Limiter](/wiki/AI_Limiter "AI Limiter"), Smart Splitters can be researched and unlocked as soon as in [Tier 2](/wiki/Tier_2 "Tier 2"). 

## Contents

  * 1 Obtaining
    * 1.1 Unlocking
  * 2 Usage
    * 2.1 Filters
    * 2.2 Buffer
    * 2.3 Upgrading and changing
  * 3 Tips
  * 4 Current issues
  * 5 See also
  * 6 Gallery
  * 7 History
  * 8 Early game development



## Obtaining

### Unlocking

**[](/wiki/Smart_Splitter "Smart Splitter")Smart Splitter** is unlocked via the **[Caterium Research chain](/wiki/Caterium_Research "Caterium Research")** in the [](/wiki/MAM "MAM") [MAM](/wiki/MAM "MAM") using:  
[](/wiki/AI_Limiter "AI Limiter")10| [](/wiki/Reinforced_Iron_Plate "Reinforced Iron Plate")50  
---|---  
  
## Usage

A Smart Splitter can be easily distinguished from other Splitters or a Conveyor Merger, as it has a **single input** labelled ≡ and is orange-colored at the top _(unless[customized to use a different color](/wiki/Customizer "Customizer"))_, and has **three outputs** that are labelled with a 〕 arrow and are silver-colored at the top. Additionally, there is a single light ▐ on each of the corners. 

Unlike a standard Splitter, the Smart Splitter can be interacted with to access its UI. In this menu, a single rule (or 'filter') can be set to each output, labeled Left Output, Center Output, and Right Output. 

The capabilities of the Smart Splitter can be useful on several occasions, such as for sorting mixed [conveyors](/wiki/Conveyor_Belts "Conveyor Belts") or handling overflow by feeding excess parts into the [AWESOME Sink](/wiki/AWESOME_Sink "AWESOME Sink"). 

### Filters

  * **Any** : The output will behave just like a normal Splitter. Parts will be evenly distributed across this output and any other available outputs. Appears by default in the center output.
  * **None** : The output is unused. Appears by default in the right and left outputs.
  * **Any undefined** : Only parts that do not have their own _Item_ rule will pass through. For example, if a [](/wiki/Rotor "Rotor") [Rotor](/wiki/Rotor "Rotor") has its own output, no Rotors will ever pass through.
  * **Overflow** : This output will only be used if there are no other outputs to use (due to being full, or having no suitable rule). If multiple outputs have this filter, overflowing parts will be distributed evenly among them.
  * _**Item**_ : Only the selected item will pass through. Its recipe has to be unlocked first for it to appear in the list.



**Any undefined** and **Overflow** : When used together, if _Any undefined_ exit is full, the undefined items will be directed to the _Overflow_ exit. To achieve the effect of only outputting undefined items to one exit and only main overflown items to the other, you need a second smart splitter downstream set to (_Any_ or _Item_ and _)_ _Overflow_ and the first one set to _Item_ and _Any undefined_. 

### Buffer

Similar to normal Conveyor Splitters, the Smart Splitter can buffer up to 9 items. If at least one output has overflow, 2 items will always be buffered and prevented from overflowing. However, this buffer may hold items that cannot possibly exit through any output other than overflow, leading to them being contained forever (unless rules are changed or the Splitter is dismantled). This may pose an issue if, for example, [radioactive](/wiki/Radioactive "Radioactive") items are sent through, as they will emit radiation while buffered. 

### Upgrading and changing

  * All Splitter variants (default, Smart, Programmable) can be swapped between each other by holding **Snap To Guidelines/Snap Mode** ( [`Ctrl`](/wiki/Controls "Controls") by default) while aiming at the Splitter to be replaced.
  * Additionally, they can be swapped to a Merger if only the center conveyors are connected.



## Tips

  * The functionality of [Programmable Splitters](/wiki/Programmable_Splitter "Programmable Splitter") can be replicated by chaining Smart Splitters.
  * Smart Splitters can be used to construct a belt compressor. _Read more:[Balancer#Belt compressor](/wiki/Balancer#Belt_compressor "Balancer")_
  * Smart Splitters can be used to make a pressure relief valve for a circular Conveyor Belt. Build a Splitter and a Merger on the main belt with the splitter downstream, connect the two with a side belt, then place a Smart Splitter on the side belt with its free output set to Overflow.



## Current issues

  * Smart Splitters currently display fluids as a sorting filter despite not having any fluid inputs



## See also

  * [](/wiki/Conveyor_Merger "Conveyor Merger") [Conveyor Merger](/wiki/Conveyor_Merger "Conveyor Merger")
  * [](/wiki/Conveyor_Splitter "Conveyor Splitter") [Conveyor Splitter](/wiki/Conveyor_Splitter "Conveyor Splitter")
  * [](/wiki/Programmable_Splitter "Programmable Splitter") [Programmable Splitter](/wiki/Programmable_Splitter "Programmable Splitter")



## Gallery

  * [](/wiki/File:Smart_Splitter_UI.png "The UI of a Smart Splitter. Using the 'Overflow' setting will allow the Smart Splitter to function as an Overflow Splitter.")

The UI of a Smart Splitter. Using the 'Overflow' setting will allow the Smart Splitter to function as an Overflow Splitter.

  * [](/wiki/File:Splitter-sort-single.png "The old appearance of a Smart Splitter as in the dev blog video")

The old appearance of a Smart Splitter as in the dev blog video

  * [](/wiki/File:Smart_Splitter_overflow_Packaged_Fuel.png "Using Smart Splitter to manage belt overflows. The belt on the right outputs to a Storage Container.")

Using Smart Splitter to manage belt overflows. The belt on the right outputs to a Storage Container.

  * [](/wiki/File:Near_priority_splitter.png "A near-priority splitter built with Splitters, Mergers and Conveyor Lifts. This setup can be used before the Smart Splitter is unlocked.")

A near-priority splitter built with [Splitters](/wiki/Splitter "Splitter"), [Mergers](/wiki/Merger "Merger") and [Conveyor Lifts](/wiki/Conveyor_Lift "Conveyor Lift"). This setup can be used before the Smart Splitter is unlocked.

  * [](/wiki/File:Priority_Splitter_schematic.png "Build these in three layers, then remove the middle temporary splitters.")

Build these in three layers, then remove the middle temporary splitters.




## History

[](/wiki/File:Icon-boilerplate.png) | The history section is incomplete in this article. Please help [expanding it](https://satisfactory.wiki.gg/wiki/Smart_Splitter?action=edit) if you can. Information can be gathered from [patch notes](/wiki/Category:Patch_notes "Category:Patch notes").   
---|---  
  
  * [Patch 0.8.0.1](/wiki/Patch_0.8.0.1 "Patch 0.8.0.1"): Fixed a crash when trying to upgrade a splitter/merger
  * [Patch 0.8.0.0](/wiki/Patch_0.8.0.0 "Patch 0.8.0.0"): Added the option to upgrade Splitters (regular, Smart Splitter, Programmable Splitter) by holding [`Ctrl`](/wiki/Controls "Controls") (default input) while aiming any Splitter variant hologram at any other already build Splitter variant
  * [Patch 0.7.0.7](/wiki/Patch_0.7.0.7 "Patch 0.7.0.7"): Fixed [Plutonium Waste](/wiki/Plutonium_Waste "Plutonium Waste") and [Alien DNA Capsule](/wiki/Alien_DNA_Capsule "Alien DNA Capsule") being missing from [Programmable Splitter](/wiki/Programmable_Splitter "Programmable Splitter") and Smart Splitter
  * [Patch 0.7.0.4](/wiki/Patch_0.7.0.4 "Patch 0.7.0.4"): Potential fix for Smart Splitter overflow issues
  * [Patch 0.6.1.2](/wiki/Patch_0.6.1.2 "Patch 0.6.1.2"): 
    * Updated UI
    * Settings can now be copied and pasted
  * [Patch 0.5.0.6](/wiki/Patch_0.5.0.6 "Patch 0.5.0.6"): Changed conveyor attachments ([Conveyor Merger](/wiki/Conveyor_Merger "Conveyor Merger"), [Conveyor Splitter](/wiki/Conveyor_Splitter "Conveyor Splitter"), Smart Splitter, and [Programmable Splitter](/wiki/Programmable_Splitter "Programmable Splitter")) to have soft clearance
  * [Patch 0.5.0.0](/wiki/Patch_0.5.0.0 "Patch 0.5.0.0"): Overhauled [Programmable Splitter](/wiki/Programmable_Splitter "Programmable Splitter") and Smart Splitter UI
  * [Patch 0.3.4.6](/wiki/Patch_0.3.4.6 "Patch 0.3.4.6"): Added “Overflow” rule
  * [Patch 0.3.4.2](/wiki/Patch_0.3.4.2 "Patch 0.3.4.2"): Now should no longer back up on duplicate rule definitions
  * [Patch 0.2.1.11](/wiki/Patch_0.2.1.11 "Patch 0.2.1.11"): Added “Any Undefined” rule, which only sends items through that are not defined to go to any other output
  * [Patch 0.2.1.9](/wiki/Patch_0.2.1.9 "Patch 0.2.1.9"): Now should use more than one output when there are multiple outputs with a matching rule
  * [Patch 0.1.5](/wiki/Patch_0.1.5 "Patch 0.1.5"): Changed crafting cost from 3 [Reinforced Iron Plate](/wiki/Reinforced_Iron_Plate "Reinforced Iron Plate") to 2



## Early game development

Prior to Closed Alpha, in Sprint 23 (week 46) there was a Splitter Advanced, with two outputs, that became the smart splitter. 

  * See also: [Game Development - Smart Splitter](/wiki/Early_game_development#Smart_Splitter "Early game development")



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
Sorting| [](/wiki/Conveyor_Merger "Conveyor Merger") [Conveyor Merger](/wiki/Conveyor_Merger "Conveyor Merger") • [](/wiki/Priority_Merger "Priority Merger") [Priority Merger](/wiki/Priority_Merger "Priority Merger") • [](/wiki/Conveyor_Splitter "Conveyor Splitter") [Conveyor Splitter](/wiki/Conveyor_Splitter "Conveyor Splitter") • [](/wiki/Smart_Splitter "Smart Splitter") Smart Splitter • [](/wiki/Programmable_Splitter "Programmable Splitter") [Programmable Splitter](/wiki/Programmable_Splitter "Programmable Splitter")  
  
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
