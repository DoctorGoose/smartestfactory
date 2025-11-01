# Production amplifier

## Production amplifier

[ ](/wiki/File:Production_amplifier.png "Production amplifier.png")

### Unlocked by

[Alien Technology Research](/wiki/Alien_Technology_Research "Alien Technology Research") \- Production Amplifier

**Production amplification** (dubbed **slooping** or **overslooping**) is a mechanic that allows select factory buildings to increase their output without increasing their input cost, at the cost of inserting [](/wiki/Somersloop "Somersloop") [Somersloops](/wiki/Somersloop "Somersloop") and a huge increase in [power demand](/wiki/Power "Power"). 

## Contents

  * 1 Obtaining
  * 2 Usage
    * 2.1 Somersloop slots
    * 2.2 Amplified production cycles
    * 2.3 Power usage
  * 3 Strategy
    * 3.1 Somersloops are tools
    * 3.2 Production amplification favors small buildings
    * 3.3 Recipe selection
  * 4 Tips
  * 5 See also
  * 6 Gallery
  * 7 History



## Obtaining

**[](/wiki/Production_amplifier "Production amplifier")Production amplifier** is unlocked via the **[Alien Technology Research chain](/wiki/Alien_Technology_Research "Alien Technology Research")** in the [](/wiki/MAM "MAM") [MAM](/wiki/MAM "MAM") using:  
[](/wiki/Somersloop "Somersloop")1| [](/wiki/SAM_Fluctuator "SAM Fluctuator")100| [](/wiki/Circuit_Board "Circuit Board")50  
---|---|---  
  
[](/wiki/Somersloop "Somersloop") [Somersloops](/wiki/Somersloop "Somersloop") required for production amplification can be found in set locations across the [world](/wiki/World "World"). There are a total of 106 Somersloops as of [Patch 1.0](/wiki/Patch_1.0 "Patch 1.0"), so as such they are a [non-renewable resource](/wiki/Resource_renewability "Resource renewability"). 

## Usage

With Somersloops being limited in quantity, it is recommended they primarily be used for production amplification at the end of a production chain, instead of in one or more intermediate productions, but the pioneer is free to use them wherever and however they wish. 

Non-idle buildings and machines that are actively producing items, and have production amplified can be identified by the use of a purple glowing power nub along with purple smoke exhaust and purple sparks all over. If building is idle (not producing items) the production amplification indicators won't appear. 

### Somersloop slots

Production amplification increases the amount of products produced by a given machine, or in other words reduces the cost to produce a given part. Buildings that are being amplified will produce a low droning noise and emit red and purple steam when active. 

The following machines can have their production amplified: 

Somersloop slots | Buildings   
---|---  
1 | [Smelter](/wiki/Smelter "Smelter"), [Constructor](/wiki/Constructor "Constructor")  
2 | [Assembler](/wiki/Assembler "Assembler"), [Foundry](/wiki/Foundry "Foundry"), [Refinery](/wiki/Refinery "Refinery"), [Converter](/wiki/Converter "Converter")  
4 | [Manufacturer](/wiki/Manufacturer "Manufacturer"), [Blender](/wiki/Blender "Blender"), [Particle Accelerator](/wiki/Particle_Accelerator "Particle Accelerator"), [Quantum Encoder](/wiki/Quantum_Encoder "Quantum Encoder")  
  
Other buildings, such as [Miners](/wiki/Miner "Miner"), [Water Extractors](/wiki/Water_Extractor "Water Extractor"), [Oil Extractors](/wiki/Oil_Extractor "Oil Extractor"), [Resource Well Pressurizers](/wiki/Resource_Well_Pressurizer "Resource Well Pressurizer"), or the [Packager](/wiki/Packager "Packager") cannot be amplified. 

If a given building has multiple Somersloop slots, then filling only some of them will cause a partial amplification. For example, if there are 4 slots but only 1 has a Somersloop inserted, then the amplification only provides a 25% boost, not a 100% boost. 

### Amplified production cycles

A machine cannot output fractions of items, so the game has to use output patterns to deal with 25%, 50% or 75% boosts. 

The output of a machine without Somersloops is always an integer (displayed above the number of items/minute), if you multiply an integer by 1.25 the decimal part of the result will always be .25, .5, .75 or .0 (another integer). 

If n is the integer part of the boost and the decimal part is not 0, the game will need to output n items on some cycles, n+1 on others, and will use the following patterns: 

Displayed output | Number of n+1 cycles | Output pattern   
---|---|---  
n.25 | 1/4 | nnnn+1   
n.5 | 2/4 | n n+1 n n+1   
n.75 | 3/4 | n n+1 n+1 n+1   
  
For instance, using the [](/wiki/Radio_Control_Unit "Radio Control Unit") [Radio Control System](/wiki/Radio_Control_Unit "Radio Control Unit") recipe which outputs 3 items, the following patterns will be created depending on the number of Somersloops: 

Somersloops | Displayed output | Number of n+1 cycles | Output pattern   
---|---|---|---  
1 | 3 x 1.25 = 3.75 | .75 -> 3/4 | 3 4 4 4   
2 | 3 x 1.5 = 4.5 | .5 -> 2/4 | 4 5 4 5   
3 | 3 x 1.75 = 5.25 | .25 -> 1/4 | 5 5 5 6   
  
Notes: 

  * Ouput patterns may start at any step in the sequence, depending on when you put Somersloops in the machine and/or which cycle the machine is in, but after seeing 4 consecutive outputs they will repeat in a regular loop.


  * This variable output fits the "chaotic alien technology" theme of the game perfectly and can have consequences. For instance, temporarily exceeding the capacity of your conveyor belts if too many machines are on their n+1 cycles at a given moment, or not providing enough resources on their n cycles. The differences between n, the displayed output and n+1 can become significant when the number of machines is large.



### Power usage

The power usage of an amplified building increases with the following formula: 

Power multiplier = (1 + Filled slots / Total slots)2  
Power usage = Base power usage × Power multiplier × (Clock speed100)1.321928  
---  
  
This results in 4 times the power usage for a fully amplified machine. 

The power increase with increased [clock speed](/wiki/Clock_speed "Clock speed") is multiplicative. This means that a fully amplified and 250% overclocked machine will consume 13.431× its base power usage. 

## Strategy

### Somersloops are tools

Somersloops are very useful temporary tools and, provided you have enough power available, can be moved around without disturbing anything to: 

  * Temporarily increase the production of an item you need.
  * Correct miscalculations on something you have just built and don't want to rebuild right away.
  * Kickstart new buildings or manifolds by allowing them to fill up twice as fast, or more if you use overclocking at the same time.



This is so useful you should always keep some Somersloops in your inventory to use as tools. 

When used as temporary boosts it is also advisable to keep track of them, for instance using building coloring or signs, to be able to get them back later more easily. 

### Production amplification favors small buildings

Production amplification favors small buildings like [Constructors](/wiki/Constructor "Constructor") because they have only one amplification slot: 

  * Their output can be doubled using only one Somersloop,
  * Their power usage is very low, so 4x power usage is still low (4 MW for constructors, 4 x 4 = 16 MW for an amplified constructor).



You can think of Somersloops as virtual machines converting MW into items: inserting a Somersloop in a constructor is like adding a virtual machine next to it, producing the same output, needing no resources and consuming 12 MW (16×3/4). 

Note: When you add one Somersloop to a constructor, the total power is multiplied by 4. So, if the constructor uses 4 MW initially and you add a Somersloop, the total power usage is now 16 MW, this means the Somersloop uses 16−4=12 MW. So 1/4 of the total power is consumed by the constructor and 3/4 by the Somersloop. 

With that in mind, you can have another look at alternate recipes having valuable input resources and/or outputting lots of items: 

  * [](/wiki/Screw "Screw") [Steel Screw](/wiki/Screw "Screw"): one Somersloop will convert 12 MW into 260 Screws/min and the constructor will output 520 Screws/min.
  * If you don't like screws, using [](/wiki/Wire "Wire") [Caterium Wire](/wiki/Wire "Wire"), one Somersloop will convert 12 MW into 120 Wires/min and the constructor will output 240 Wires/min.
  * Using [](/wiki/Iron_Rod "Iron Rod") [Aluminum Rod](/wiki/Iron_Rod "Iron Rod"), one Somersloop will convert 12 MW into 52.5 Iron Rods/min and the constructor will output 105 Iron Rods/min.



In the standard recipes, these ones are also worth mentioning: 

  * [](/wiki/Aluminum_Casing "Aluminum Casing") [Aluminum Casing](/wiki/Aluminum_Casing "Aluminum Casing"): the constructor will output 120 Aluminum Casings/min.
  * [](/wiki/Ficsite_Trigon "Ficsite Trigon") [Ficsite Trigon](/wiki/Ficsite_Trigon "Ficsite Trigon"): the constructor will output 60 Ficsite Trigons/min.



As these buildings are small and their power usage is low, you can easily overclock them: an amplified fully overclocked constructor at 250% clock speed will use 53.7 MW which is less than the power usage of a [Manufacturer](/wiki/Manufacturer "Manufacturer") (55 MW). 

Applying a 250% overclock to the examples above, we have the following results: 

  * [](/wiki/Screw "Screw") [Steel Screw](/wiki/Screw "Screw"): one Somersloop will convert 53.7×3/4≈40.3 MW into 260×2.5=650 Screws/min and the constructor will output 1300 Screws/min (yes, it's higher than what a [Mk.6 Conveyor Belt](/wiki/Conveyor_Belts "Conveyor Belts") can carry).
  * [](/wiki/Wire "Wire") [Caterium Wire](/wiki/Wire "Wire"): one constructor and one Somersloop will output 600 Wires/min.
  * [](/wiki/Iron_Rod "Iron Rod") [Aluminum Rod](/wiki/Iron_Rod "Iron Rod"): one constructor and one Somersloop will output 262.5 Iron Rods/min.
  * [](/wiki/Aluminum_Casing "Aluminum Casing") [Aluminum Casing](/wiki/Aluminum_Casing "Aluminum Casing"): one constructor and one Somersloop will output 300 Aluminum Casings/min.
  * [](/wiki/Ficsite_Trigon "Ficsite Trigon") [Ficsite Trigon](/wiki/Ficsite_Trigon "Ficsite Trigon"): one constructor and one Somersloop will output 150 Ficsite Trigons/min.



These are the outputs of a single constructor, so it may change the way you think of and organize factories. Keeping in mind the limited number of Somersloops available, one of these constructors in the right place can considerably simplify your setups. 

The same kind of computation can be made for recipes using other types of buildings (for buildings having 2 slots, power usage for 1 Somersloop is 2.25x instead of 4x and the building will produce 1.5x more items instead of 2x, see the preceding chapters). You can also use Somersloops in 4 slots buildings, but due to their high power usage they should generally be kept at 100% clock speed or underclocked (see [Somersloop underclocking ("underslooping")](/wiki/Tutorial:Advanced_clock_speed#Somersloop_underclocking_\("underslooping"\) "Tutorial:Advanced clock speed")). 

Another good use for Somersloops is for products that are valuable and at the end of a chain, especially if they are produced by a small building. In this category, some of the bests are [](/wiki/Assembly_Director_System "Assembly Director System") [Assembly Director System](/wiki/Assembly_Director_System "Assembly Director System") and [](/wiki/Pressure_Conversion_Cube "Pressure Conversion Cube") [Pressure Conversion Cube](/wiki/Pressure_Conversion_Cube "Pressure Conversion Cube") because they are made by [Assemblers](/wiki/Assembler "Assembler") which need only 2 Somersloops to double their production and have a reasonable power usage. 

### Recipe selection

Buildings having all of their Somersloop slots filled and set at 250% clock speed: 

  * Produce the same output as 5 buildings of the same type (2x from the Somersloops and 2.5x from overclocking, 2×2.5=5).
  * Use only half of the resources 5 buildings would need (because of the Somersloops).



So the most interesting recipes to use are those which: 

  * Produce lots of items (because the output is multiplied by 5),
  * And/or have valuable input resources (because the input is divided by 2).



Here are some examples and comparisons: 

Recipe | Ingredients | Produced in | Products | Power usage | Comment   
---|---|---|---|---|---  
Steel Screw | 12.5 [](/wiki/Steel_Beam "Steel Beam") [Steel Beam](/wiki/Steel_Beam "Steel Beam") / min | [Constructor](/wiki/Constructor "Constructor") | 1300 [](/wiki/Screw "Screw") [Screw](/wiki/Screw "Screw") /min | 53.7 MW | You have to underclock it slightly because of these slow Mk.6 belts.   
Caterium Wire | 37.5 [](/wiki/Caterium_Ingot "Caterium Ingot") [Caterium Ingot](/wiki/Caterium_Ingot "Caterium Ingot") / min | [Constructor](/wiki/Constructor "Constructor") | 600 [](/wiki/Wire "Wire") [Wire](/wiki/Wire "Wire") /min | 53.7 MW |   
Fused Wire | 30 [](/wiki/Copper_Ingot "Copper Ingot") [Copper Ingot](/wiki/Copper_Ingot "Copper Ingot") / min  
7.5 [](/wiki/Caterium_Ingot "Caterium Ingot") [Caterium Ingot](/wiki/Caterium_Ingot "Caterium Ingot") / min | [Assembler](/wiki/Assembler "Assembler") | 450 [](/wiki/Wire "Wire") [Wire](/wiki/Wire "Wire") /min | 201.5 MW | Assembler example, you can use it if you don't have enough caterium, but 450 wires for 201.5 MW is way worse than Caterium Wire which produces 600 wires for 53.7 MW, and in addition uses only one Somersloop instead of two.   
Aluminum Rod | 18.75 [](/wiki/Aluminum_Ingot "Aluminum Ingot") [Aluminum Ingot](/wiki/Aluminum_Ingot "Aluminum Ingot") / min | [Constructor](/wiki/Constructor "Constructor") | 262.5 [](/wiki/Iron_Rod "Iron Rod") [Iron Rod](/wiki/Iron_Rod "Iron Rod") /min | 53.7 MW |   
Aluminum Casing | 225 [](/wiki/Aluminum_Ingot "Aluminum Ingot") [Aluminum Ingot](/wiki/Aluminum_Ingot "Aluminum Ingot") / min | [Constructor](/wiki/Constructor "Constructor") | 300 [](/wiki/Aluminum_Casing "Aluminum Casing") [Aluminum Casing](/wiki/Aluminum_Casing "Aluminum Casing") /min | 53.7 MW |   
Alclad Casing | 375 [](/wiki/Aluminum_Ingot "Aluminum Ingot") [Aluminum Ingot](/wiki/Aluminum_Ingot "Aluminum Ingot") / min  
187.5 [](/wiki/Copper_Ingot "Copper Ingot") [Copper Ingot](/wiki/Copper_Ingot "Copper Ingot") / min | [Assembler](/wiki/Assembler "Assembler") | 562.5 [](/wiki/Aluminum_Casing "Aluminum Casing") [Aluminum Casing](/wiki/Aluminum_Casing "Aluminum Casing") /min | 201.5 MW | You can use it if you're short on aluminum ingots and have a good amount of copper, but it cannot beat 2x Aluminum Casing, which produces 600 aluminum casings for 107 MW (2 Somersloops are used in either case).   
Pure Aluminum Ingot | 150 [](/wiki/Aluminum_Scrap "Aluminum Scrap") [Aluminum Scrap](/wiki/Aluminum_Scrap "Aluminum Scrap") / min | [Smelter](/wiki/Smelter "Smelter") | 150 [](/wiki/Aluminum_Ingot "Aluminum Ingot") [Aluminum Ingot](/wiki/Aluminum_Ingot "Aluminum Ingot") /min | 53.7 MW | Smelter example, if you're short on aluminum ingots the Somersloop makes Aluminum Ingots = Aluminum Scrap instead of half of it, you can use one on occasion, but as the output is rather low you will probably still need several smelters and this can deplete your Somersloops very fast.   
Ficsite Trigon | 25 [](/wiki/Ficsite_Ingot "Ficsite Ingot") [Ficsite Ingot](/wiki/Ficsite_Ingot "Ficsite Ingot") / min | [Constructor](/wiki/Constructor "Constructor") | 150 [](/wiki/Ficsite_Trigon "Ficsite Trigon") [Ficsite Trigon](/wiki/Ficsite_Trigon "Ficsite Trigon") /min | 53.7 MW | The output may not seem great, but saving half of the Ficsite ingots, produced by [Converters](/wiki/Converter "Converter"), is.   
Copper Alloy Ingot | 125 [](/wiki/Copper_Ore "Copper Ore") [Copper Ore](/wiki/Copper_Ore "Copper Ore") / min  
125 [](/wiki/Iron_Ore "Iron Ore") [Iron Ore](/wiki/Iron_Ore "Iron Ore") / min | [Foundry](/wiki/Foundry "Foundry") | 500 [](/wiki/Copper_Ingot "Copper Ingot") [Copper Ingot](/wiki/Copper_Ingot "Copper Ingot") /min | 214.9 MW | The input/ouput numbers look nice, but foundries in general are hard to recommend because they only process basic resources and their power usage is high.   
Petroleum Coke | 100 [](/wiki/Heavy_Oil_Residue "Heavy Oil Residue") [Heavy Oil Residue](/wiki/Heavy_Oil_Residue "Heavy Oil Residue") / min | [Refinery](/wiki/Refinery "Refinery") | 600 [](/wiki/Petroleum_Coke "Petroleum Coke") [Petroleum Coke](/wiki/Petroleum_Coke "Petroleum Coke") /min | 402.9 MW | Refinery example, note that [](/wiki/Aluminum_Scrap "Aluminum Scrap") [Aluminum Scrap](/wiki/Aluminum_Scrap "Aluminum Scrap") recipes will overshoot Mk.6 belts capacity and [](/wiki/Alumina_Solution "Alumina Solution") [Sloppy Alumina](/wiki/Alumina_Solution "Alumina Solution") will overshoot Mk.2 pipes. Also, with refineries power usage is very high, this may not be worth it except in rare cases.   
  
## Tips

  * If unlocked early by finding [Circuit Boards](/wiki/Circuit_Board "Circuit Board") in [Crash Site](/wiki/Crash_Site "Crash Site") wreckage, amplification can be utilized in these early-game production lines. If the recipe is changed within a single machine, only 1 Somersloop is required: 
    * [Alien Remains](/wiki/Alien_Remains "Alien Remains") → [](/wiki/Alien_Protein "Alien Protein") [Alien Protein](/wiki/Alien_Protein "Alien Protein") → [](/wiki/Biomass "Biomass") [Biomass](/wiki/Biomass "Biomass") → [](/wiki/Solid_Biofuel "Solid Biofuel") [Solid Biofuel](/wiki/Solid_Biofuel "Solid Biofuel") for 8× the Solid Biofuel to use in [Biomass Burners](/wiki/Biomass_Burner "Biomass Burner").
    * [Alien Remains](/wiki/Alien_Remains "Alien Remains") → [](/wiki/Alien_Protein "Alien Protein") [Alien Protein](/wiki/Alien_Protein "Alien Protein") → [](/wiki/Alien_DNA_Capsule "Alien DNA Capsule") [Alien DNA Capsule](/wiki/Alien_DNA_Capsule "Alien DNA Capsule") for 4× the Alien DNA Capsules for [AWESOME Sinks](/wiki/AWESOME_Sink "AWESOME Sink").
    * [](/wiki/Power_Slug "Power Slug") [Power Slug](/wiki/Power_Slug "Power Slug") → [](/wiki/Power_Shard "Power Shard") [Power Shard](/wiki/Power_Shard "Power Shard") for 2× the Power Shards to use in [overclocking](/wiki/Overclocking "Overclocking").
    * [Project Assembly parts](/wiki/Category:Project_Assembly_parts "Category:Project Assembly parts"), to halve the cost of [Space Elevator](/wiki/Space_Elevator "Space Elevator") phases.
  * Amplifying machines producing the final product results in the greatest material gains.
  * If you don't intend to amplify all machines producing a given item, then spreading the Somersloops equally between them will lower the power demand without affecting the boost amount. However, keep the following tip in consideration:
  * Combining [overclocking](/wiki/Overclocking "Overclocking") and production amplification results in the greatest utilization of each Somersloop, as the amplification applies to increased clock speed. This means that the boost is effectively applied to 2.5 machines, not just 1 machine. 
    * However, this results in by far the highest power demand, for a 250% clock speed power usage is multiplied by 3.36 (see [Remarkable clock speeds](/wiki/Tutorial:Advanced_clock_speed#Remarkable_clock_speeds "Tutorial:Advanced clock speed")).
    * The [Quantum Encoder](/wiki/Quantum_Encoder "Quantum Encoder")'s power usage peaks at 2,000 MW by default. With a maximum overclock and amplification, it will average at 13,431 MW and peak at 26,862 MW.



## See also

  * [Clock speed](/wiki/Clock_speed "Clock speed")
  * [Power](/wiki/Power "Power")



## Gallery

  * [](/wiki/File:Production_Amplified_Manufacturer.png "Assembler that is using Production Amplification \(note purple power nub and purple exhaust smoke\)")

Assembler that is using Production Amplification _(note purple power nub and purple exhaust smoke)_




## History

  * [Patch 1.0](/wiki/Patch_1.0 "Patch 1.0")
    * Introduced
    * As an alternative to the Power Augmenter, Somersloops can also be used to boost production by inserting them into a production building.
    * This greatly boosts the resource output of that building without requiring any additional resource supply, but instead significantly increasing the power consumption.



  * [v](/wiki/Template:PioneerNav "Template:PioneerNav")
  * [e](https://satisfactory.wiki.gg/wiki/Template:PioneerNav?action=edit)
  * [h](https://satisfactory.wiki.gg/wiki/Template:PioneerNav?action=history)

[Satisfactory](/wiki/Satisfactory "Satisfactory") game mechanics  
---  
Player abilities| [Codex](/wiki/Codex "Codex") • [Resource Scanner](/wiki/Resource_Scanner "Resource Scanner") • [Build Gun](/wiki/Build_Gun "Build Gun") • [Inventory](/wiki/Inventory "Inventory") • [Health](/wiki/Health "Health") • [Combat](/wiki/Combat "Combat") • [Movement](/wiki/Movement "Movement") • [Flashlight](/wiki/Flashlight "Flashlight") • [HUD](/wiki/HUD "HUD") • [Crate](/wiki/Crate "Crate") • [To-Do List](/wiki/To-Do_List "To-Do List")  
Unlockable abilities| [Recipes](/wiki/Recipes "Recipes") • [Power](/wiki/Power "Power") • [Overclocking/Underclocking](/wiki/Clock_speed "Clock speed") • Production amplifier • [Customizer](/wiki/Customizer "Customizer") • [Map](/wiki/Map "Map") • [Productivity Display](/wiki/Productivity_Display "Productivity Display") • [Head lift](/wiki/Head_lift "Head lift") • [Blueprints](/wiki/Blueprints "Blueprints") • [Fuels](/wiki/Category:Fuels "Category:Fuels") • [FICSIT Productive Packer Deluxe](/wiki/FICSIT_Productive_Packer_Deluxe "FICSIT Productive Packer Deluxe")  
Progression| [Story](/wiki/Story "Story") • [Drop-pod](/wiki/Drop-pod "Drop-pod") • [Onboarding (In-game tutorial)](/wiki/Onboarding "Onboarding") • [Milestones](/wiki/Milestones "Milestones") • [MAM](/wiki/MAM "MAM") • [Alternate recipes](/wiki/Hard_Drive#Alternate_recipes "Hard Drive") • [Space Elevator](/wiki/Space_Elevator "Space Elevator") • [AWESOME Sink](/wiki/AWESOME_Sink "AWESOME Sink") • [AWESOME Shop](/wiki/AWESOME_Shop "AWESOME Shop")  
Seasonal events| [April Fools' Day](/wiki/April_Fools%27_Day "April Fools' Day") • [Anniversary](/wiki/Anniversary "Anniversary") • [FICSMAS](/wiki/FICSMAS "FICSMAS")  
Environment| [World](/wiki/World "World") • [Resource Node](/wiki/Resource_Node "Resource Node") • [Resource Well](/wiki/Resource_Well "Resource Well") • [Resource renewability](/wiki/Resource_renewability "Resource renewability") • [Crash Site](/wiki/Crash_Site "Crash Site") • [Radiation](/wiki/Radiation "Radiation") • [Poison Gas](/wiki/Poison_Gas "Poison Gas") • [Cracked boulder](/wiki/Cracked_boulder "Cracked boulder") • [Cave](/wiki/Cave "Cave")  
Gameplay| [Controls](/wiki/Controls "Controls") • [Settings](/wiki/Settings "Settings") • [Future content](/wiki/Future_content "Future content") • [Old unreleased content](/wiki/Old_unreleased_content "Old unreleased content") • [Online tools](/wiki/Online_tools "Online tools") • [Community resources](/wiki/Community_resources "Community resources") • [Advanced Game Settings](/wiki/Advanced_Game_Settings "Advanced Game Settings") • [Acronyms](/wiki/Acronyms "Acronyms") • [Achievements](/wiki/Achievements "Achievements") • [Easter eggs](/wiki/Easter_eggs "Easter eggs") • [Game menus](/wiki/Game_menus "Game menus") • [Indicator Light](/wiki/Indicator_Light "Indicator Light") • [Multiplayer](/wiki/Multiplayer "Multiplayer") • [Music](/wiki/Music "Music")  
Technical| [Console release](/wiki/Console_release "Console release") • [Debug console](/wiki/Debug_console "Debug console") • [Launch arguments](/wiki/Launch_arguments "Launch arguments") • [Save files](/wiki/Save_files "Save files") • [System requirements](/wiki/System_requirements "System requirements") • [Units](/wiki/Units "Units") • [Unreal Engine](/wiki/Unreal_Engine "Unreal Engine")  
Guides and tutorials| | Basics| [Walkthrough/How to play](/wiki/Tutorial:How_to_play "Tutorial:How to play") • [New Pioneer Guide](/wiki/Tutorial:New_Pioneer_Guide "Tutorial:New Pioneer Guide") • [Production line basics](/wiki/Tutorial:Production_line "Tutorial:Production line") • [Advanced production line tips](/wiki/Tutorial:Production_line_design_tips "Tutorial:Production line design tips") • [Picking an alternate recipe](/wiki/Tutorial:Picking_an_alternate_recipe "Tutorial:Picking an alternate recipe") • [Independency](/wiki/Tutorial:Independency "Tutorial:Independency") • [Aluminum Ingot production](/wiki/Tutorial:Setting_up_Aluminum_Ingot_production "Tutorial:Setting up Aluminum Ingot production")  
---|---  
Logistics| [Manifold](/wiki/Manifold "Manifold") • [Balancer](/wiki/Balancer "Balancer") • [Pipeline manifold](/wiki/Pipeline_manifold "Pipeline manifold") • [Prime Splitter Arrays](/wiki/Tutorial:Prime_splitter_arrays "Tutorial:Prime splitter arrays") • [Trains](/wiki/Tutorial:Trains "Tutorial:Trains") • [Train throughput](/wiki/Tutorial:Train_throughput "Tutorial:Train throughput")  
Dedicated servers| [Dedicated servers](/wiki/Dedicated_servers "Dedicated servers") • [Running as a Service](/wiki/Dedicated_servers/Running_as_a_Service "Dedicated servers/Running as a Service") • [Configuration files](/wiki/Dedicated_servers/Configuration_files "Dedicated servers/Configuration files") • [Automatic updates](/wiki/Dedicated_servers/Automatic_updates "Dedicated servers/Automatic updates") • [HTTPS API](/wiki/Dedicated_servers/HTTPS_API "Dedicated servers/HTTPS API") • [Lightweight Query API](/wiki/Dedicated_servers/Lightweight_Query_API "Dedicated servers/Lightweight Query API")  
Other| [Hypertube cannon](/wiki/Tutorial:Hypertube_cannon "Tutorial:Hypertube cannon") • [Hypertube brake](/wiki/Tutorial:Hypertube_brake "Tutorial:Hypertube brake") • [Steam Deck & Controller setup](/wiki/Tutorial:Controller_setup "Tutorial:Controller setup") • [Extracting UI icons](/wiki/Tutorial:Extracting_UI_icons "Tutorial:Extracting UI icons")
  *[v]: View this template
  *[e]: Edit this template
  *[h]: History of this template
  *[his]: his trivia section
