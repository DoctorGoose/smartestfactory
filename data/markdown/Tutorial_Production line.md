# Tutorial:Production line

This article describes the **basics of setting up production lines** , how to read the UI of buildings (such as input and output item rates), and how to calculate building ratios.   
  
For more information on planning a production line, see [Tutorial:Production line design tips](/wiki/Tutorial:Production_line_design_tips "Tutorial:Production line design tips"). 

## Contents

  * 1 Reading building interfaces
    * 1.1 Miner
    * 1.2 Smelter
    * 1.3 Constructor
      * 1.3.1 Per-cycle and per-minute rates
    * 1.4 Conveyor Belt
    * 1.5 Storage Container
    * 1.6 Overclocking
  * 2 Splitting and merging
    * 2.1 Miner
    * 2.2 Smelter
    * 2.3 Constructor (Wire)
    * 2.4 Constructor (Cable)
    * 2.5 Conveyor Belt
    * 2.6 Storage Container
  * 3 Overclocking and Flow Rate
    * 3.1 Miner
    * 3.2 Smelter
    * 3.3 Conveyor Belt
    * 3.4 Manifold
  * 4 Fractions and decimals
    * 4.1 Build more machines
    * 4.2 Overclocking and Underclocking
    * 4.3 Overclock the Miner
    * 4.4 Overclock the Constructor
    * 4.5 Underclock the last machine
    * 4.6 Underclock all machines
  * 5 Complex production line
    * 5.1 Miner
    * 5.2 Smelter
    * 5.3 Dividing Resources
      * 5.3.1 Reinforced Iron Plate
      * 5.3.2 Iron Plate
      * 5.3.3 Screw
      * 5.3.4 Iron Rod
      * 5.3.5 Math it out
    * 5.4 Constructor (Iron Plate)
    * 5.5 Constructor (Iron Rod)
    * 5.6 Constructor (Screw)
    * 5.7 Assembler (Reinforced Iron Plate)
    * 5.8 Conveyor Belt
  * 6 Online tools



## Reading building interfaces

[](/wiki/File:Simple_production_line.png)

[](/wiki/File:Simple_production_line.png "Enlarge")

A simple production line, showing the UI of each building. (Click to enlarge)

A simple production line involves [Miner](/wiki/Miner "Miner") → [Smelter](/wiki/Smelter "Smelter") → [Constructor](/wiki/Constructor "Constructor") → [Storage Container](/wiki/Storage_Container "Storage Container"). The example shows the buildings' UI, which can be accessed by approaching and interacting [`E`](/wiki/Controls "Controls") with each [building](/wiki/Building "Building"). In this example, each machine's item production matches up perfectly with item consumption (marked in red) making a 1:1 ratio. 

### Miner

A [Miner](/wiki/Miner "Miner") extracts ore at a rate that depends on both [Resource Node](/wiki/Resource_Node "Resource Node")'s [purity](/wiki/Purity "Purity") and the [Miner](/wiki/Miner "Miner")'s mark. The Resource Node's purity, either impure, normal, or pure is fixed based on its location on the [map](/wiki/Map "Map"). Higher marks of Miners can be unlocked in later [Milestones](/wiki/Milestones "Milestones"), which have a higher extraction rate. In this example, the [Miner Mk.1](/wiki/Miner_Mk.1 "Miner Mk.1") extracts 30 [Iron Ore](/wiki/Iron_Ore "Iron Ore")/min from the [Resource Node](/wiki/Resource_Node "Resource Node") below it. 

### Smelter

A [Smelter](/wiki/Smelter "Smelter") smelts ore into ingots. In the above example, 1 [Iron Ore](/wiki/Iron_Ore "Iron Ore") is consumed to produce 1 [Iron Ingot](/wiki/Iron_Ingot "Iron Ingot"). The smelting of one ore takes 2 seconds. 

### Constructor

A [Constructor](/wiki/Constructor "Constructor") processes the input into useful parts. In the above example, 3 [Iron Ingots](/wiki/Iron_Ingot "Iron Ingot") are consumed to craft 2 [Iron Plates](/wiki/Iron_Plate "Iron Plate"). 

#### Per-cycle and per-minute rates

Each building shows two rates: _per crafting cycle_ and _per minute_. The [Constructor](/wiki/Constructor "Constructor") in the above example has the following rates: 

_Per-cycle_ values are shown in bold text. The cycle duration is shown in the middle of the UI, under a timer icon. 

  * 3 Iron Ingots are consumed per cycle
  * 2 Iron Plates are produced per cycle
  * Crafting cycle duration is 6 seconds



Therefore, each Iron Plate takes 1.5 Ingots to craft (3 Ingots make 2 Plates). 

These per-cycle values are useful for determing item costs. However, in automated setups, it is easier to use _per-minute_ values instead, shown in smaller, orange numbers below the bold text. 

  * 30 Iron Ingots are consumed per minute
  * 20 Iron Plates are produced per minute



### Conveyor Belt

[Conveyor Belts](/wiki/Conveyor_Belts "Conveyor Belts") automatically transport items from one building to the next, removing the need for manual labor to move items between machines. Belts have a maximum item/min flow rate depending on the belt's mark. If a higher item flow rate is required, consider using [higher marks of Conveyor Belts](/wiki/Conveyor_Belt#Marks "Conveyor Belt"), or constructing multiple parallel belts. Else, the entire production line will slow down due to insufficient item flow. 

### Storage Container

The [Storage Container](/wiki/Storage_Container "Storage Container") in the above example is optional. Its purpose is to store and buffer produced items so that the machines before it can run smoothly. Most production buildings can only store up to one [stack](/wiki/Stack "Stack") of items in its output slot, and once it is full, the machine stops. 

### Overclocking

The production speed of machines can be altered with [overclocking](/wiki/Overclocking "Overclocking"), which will be discussed in the section below. 

## Splitting and merging

[](/wiki/File:Splitting_and_merging.png)

[](/wiki/File:Splitting_and_merging.png "Enlarge")

[Splitters](/wiki/Splitter "Splitter") and [Mergers](/wiki/Merger "Merger") may be required to achieve 100% efficiency in some setup, such as for the [Copper](/wiki/Copper "Copper") chain. (Click to enlarge)

Production chains rarely work in a 1:1 crafting ratio; the example shown in the previous section is a special case. If there is a mismatch in the buildings' ratio, the entire chain is slowed down proportionally to the slowest element in the chain. This reduces the efficiency and should be avoided. 

The term 'Efficiency' is used to describe the uptime of a machine, usually denoted in percentage (%). Efficiency is indicated in the lower right of each machine's UI. 

To achieve 100% efficiency, the input rate should be greater or equal to the consumption rate. If more items/min are required, build more machines and use [Mergers](/wiki/Conveyor_Merger "Conveyor Merger") to bring these items onto a single belt. If there are too many items/min are being input, consider using [Splitters](/wiki/Conveyor_Splitter "Conveyor Splitter") to send items into multiple machines. 

### Miner

A [Miner Mk.1](/wiki/Miner_Mk.1 "Miner Mk.1") on a normal [Copper](/wiki/Copper "Copper") [node](/wiki/Node "Node") extracts 60 [Copper Ore](/wiki/Copper_Ore "Copper Ore")/min. 

### Smelter

A [Smelter](/wiki/Smelter "Smelter") consumes 30 [Copper Ore](/wiki/Copper_Ore "Copper Ore")/min. To consume the 60 Ore/min produced by the [Miner](/wiki/Miner "Miner"), build two [Smelters](/wiki/Smelter "Smelter") and use a [Splitter](/wiki/Splitter "Splitter") to split the [Conveyor Belt](/wiki/Conveyor_Belt "Conveyor Belt") two ways ( `60 / 30 = 2 )`

If only one [Smelter](/wiki/Smelter "Smelter") is built, the [Copper Ore](/wiki/Copper_Ore "Copper Ore") produced by the [Miner](/wiki/Miner "Miner") will not be consumed fast enough, and they will backlog into the [Miner](/wiki/Miner "Miner") and causing it to run at only 50% of the time. This is equivalent to 50% efficiency. 

Each [Smelter](/wiki/Smelter "Smelter") produces 30 [Copper Ingots](/wiki/Copper_Ingot "Copper Ingot")/min. 

### Constructor (Wire)

Each [Constructor](/wiki/Constructor "Constructor") consumes 15 [Copper Ingots](/wiki/Copper_Ingot "Copper Ingot")/min. Similarly, split each [Copper Ingot](/wiki/Copper_Ingot "Copper Ingot") belt two ways, which can supply up to four [Constructors](/wiki/Constructor "Constructor").   
`30 / 15 = 2` (each Smelter output belt split into two)   
`2 x 2 = 4` (two Smelters support four Constructors) 

Each Constructor produces 30 [Wire](/wiki/Wire "Wire")/min. 

### Constructor (Cable)

Each [Constructor](/wiki/Constructor "Constructor") consumes 60 [Wire](/wiki/Wire "Wire")/min. Two [Wire](/wiki/Wire "Wire") [Constructors](/wiki/Constructor "Constructor") are required to supply one [Cable](/wiki/Cable "Cable") [Constructor](/wiki/Constructor "Constructor"). Combine the output of two Constructors using a [Merger](/wiki/Merger "Merger").   
`30 * 2 = 60`

If only one [Wire](/wiki/Wire "Wire") [Constructor](/wiki/Constructor "Constructor") is connected to a [Cable](/wiki/Cable "Cable") [Constructor](/wiki/Constructor "Constructor"), the latter will only run 50% of the time due to insufficient input rate. This is equivalent to 50% efficiency. 

Each Constructor produces 30 [Cable](/wiki/Cable "Cable")/min. 

### Conveyor Belt

[Conveyor Belt Mk.1](/wiki/Conveyor_Belt_Mk.1 "Conveyor Belt Mk.1") can only transport 60 items/min. In the above example, the belt carrying [Copper Ores](/wiki/Copper_Ore "Copper Ore") after the Miner, and the belts transporting [Wires](/wiki/Wire "Wire") after the [Mergers](/wiki/Merger "Merger") are operating at their maximum capacity. 

### Storage Container

A [Storage Container](/wiki/Storage_Container "Storage Container") is used to store stacks of items. Avoid mixing items in [Storage Containers](/wiki/Storage_Container "Storage Container"), as they have an output that can be used to further automate your production line and mixed items can cause your production to jam. A [Merger](/wiki/Merger "Merger") is used to merge two [Wire](/wiki/Wire "Wire") belts into one before the [Container](/wiki/Storage_Container "Storage Container") to eliminate the need for two [Wire](/wiki/Wire "Wire") [Containers](/wiki/Storage_Container "Storage Container"). 

## Overclocking and Flow Rate

[](/wiki/File:Overclocked_miner_manifold.png)

[](/wiki/File:Overclocked_miner_manifold.png "Enlarge")

An [overclocked](/wiki/Overclock "Overclock") [Miner](/wiki/Miner "Miner") extracts ores faster, and thus capable to supply more [Smelters](/wiki/Smelter "Smelter"). (Click to enlarge)

[](/wiki/File:Overclocked_Miner_UI.png)

[](/wiki/File:Overclocked_Miner_UI.png "Enlarge")

The overclocking section in a building's UI. (Click to enlarge)

_Main article:_[Clock Speed](/wiki/Clock_Speed "Clock Speed")

As the number of [Resource Nodes](/wiki/Resource_Node "Resource Node") in the [world](/wiki/World "World") is finite, there is a hard limit on the total extraction rate. To maximize the potential of a Resource Node, [Miners](/wiki/Miner "Miner") can be [Overclocked](/wiki/Overclock "Overclock"). The overclocking ability can be [researched](/wiki/MAM#Power_Slugs "MAM") in [MAM](/wiki/MAM "MAM") via [Power Slugs](/wiki/Power_Slug "Power Slug"). 

### Miner

The [Miner Mk.1](/wiki/Miner_Mk.1 "Miner Mk.1") on a normal [Iron](/wiki/Iron "Iron") node in the above example is overclocked to 250% (x 2.5 speed), hence it extracts 150 [Iron Ore](/wiki/Iron_Ore "Iron Ore")/min (`60 x 2.5 = 150)`

### Smelter

Each [Smelter](/wiki/Smelter "Smelter") consumes 30 [Iron Ore](/wiki/Iron_Ore "Iron Ore")/min to yield 30 [Iron Ingot](/wiki/Iron_Ingot "Iron Ingot")/min. Five Smelters should be built to fully utilize the extracted Ore. (`150 / 30 = 5)`

### Conveyor Belt

_Main article:_[Conveyor Belt](/wiki/Conveyor_Belt "Conveyor Belt")

[Conveyor Belt Mk.1](/wiki/Conveyor_Belt_Mk.1 "Conveyor Belt Mk.1") is not fast enough (60 items/min) to pull out all the ore extracted by the [overclocked](/wiki/Overclock "Overclock") [Miner](/wiki/Miner "Miner") (150 items/min), thus higher marks of the belt are required. Else, the [Miner](/wiki/Miner "Miner") will only run at 40% Efficiency and not at its overclocked potential. 

[Conveyor Belt Mk.3](/wiki/Conveyor_Belt_Mk.3 "Conveyor Belt Mk.3") (270 items/min) can handle the 150 items/min flow rate and should be built right after the [Miner](/wiki/Miner "Miner"). [Conveyor Belt Mk.2](/wiki/Conveyor_Belt_Mk.2 "Conveyor Belt Mk.2") (120 items/min) and [Conveyor Belt Mk.1](/wiki/Conveyor_Belt "Conveyor Belt") (60 items/min) are then used as items split off the [Conveyor Belt Mk.3](/wiki/Conveyor_Belt "Conveyor Belt") line. Alternatively, all belts can be built with [Conveyor Belt Mk.3](/wiki/Conveyor_Belt "Conveyor Belt"), if there are sufficient materials to do so. 

### Manifold

[Splitters](/wiki/Splitter "Splitter") are organised in a [manifold](/wiki/Manifold "Manifold"), where each split sends items off the main belt onto belts into the [Constructors](/wiki/Constructor "Constructor"). The main belt will begin sending items 50/50 down the first split off line, and as the [Constructor](/wiki/Constructor "Constructor") backfills the split off line will only consume the 30 [Iron Ore](/wiki/Iron_Ore "Iron Ore")/min (as consumed by the [Smelter](/wiki/Smelter "Smelter")). The last [Splitter](/wiki/Conveyor_Splitter "Conveyor Splitter") at the far left is optional; it is built for future expansions, when [higher marks of Miner](/wiki/Miner "Miner") are unlocked. 

## Fractions and decimals

[](/wiki/File:Fractional_building_ratio.png)

[](/wiki/File:Fractional_building_ratio.png "Enlarge")

A normal, [Limestone](/wiki/Limestone "Limestone") Miner can support more than 1, but less than two Constructors. (Click to enlarge)

There are many occasions where the building ratio doesn't end up as whole numbers. The [Limestone](/wiki/Limestone "Limestone") -> [Concrete](/wiki/Concrete "Concrete") setup is the first production chain that contains a fractional ratio:   
`60 / 45 = 1.333 or 1+1/3`  
The [Limestone](/wiki/Limestone "Limestone") produced by a normal [Miner](/wiki/Miner "Miner") can support one and a third [Constructors](/wiki/Constructor "Constructor"). 

Below are approaches to solve this issue: 

### Build more machines

Exceeding requirements continues to work without issue. Building two constructors will give both approximately 33% idle time (aka 67% Efficiency). In general, any decimal building ratio can be rounded up to the next integer, for example:   
`60 / 45 = 1.333 -> 2`  
  
`400 / 30 = 13.33 -> 14`  
  
`100 / 110 = 0.909 -> 1`

If both Constructors are not underclocked they will just run and stop intermittently, but continue to convert 60 [Limestone](/wiki/Limestone "Limestone")/min to 20 [Concretes](/wiki/Concrete "Concrete")/min. 

### Overclocking and Underclocking

Once overclocking is [researched](/wiki/Hard_Drive "Hard Drive") via [Power Slugs](/wiki/Power_Slug "Power Slug") in the [MAM](/wiki/MAM "MAM"), overclocking and underclocking become available. [Power Shards](/wiki/Power_Shard "Power Shard") are a limited resource, and take most benefit in raw resource production. 

The below show ways to utilise [Clock Speed](/wiki/Clock_speed "Clock speed") to reach maximum efficiency: 

### Overclock the Miner

Overclocking the [Miner](/wiki/Miner "Miner") to 150% or 225% will make the ratio an integer.   
`45 x 2 = 90`   
`90 / 60 = 1.5` (150% overclock, one [Miner](/wiki/Miner "Miner") to two [Constructors](/wiki/Constructor "Constructor"))  
  
`45 x 3 = 135`   
`135 / 60 = 2.25` (225% overclock, one [Miner](/wiki/Miner "Miner") to three [Constructors](/wiki/Constructor "Constructor")) 

### Overclock the Constructor

Build one [Constructor](/wiki/Constructor "Constructor") and overclock it to 134%, and all [Limestone](/wiki/Limestone "Limestone") will be consumed. 

### Underclock the last machine

[Underclocking](/wiki/Underclock "Underclock") the second [Constructor](/wiki/Constructor "Constructor") by either 

  * Dragging the slider to 34% (Underclocking to 33% loses the additional 0.33% processing speed required)
  * Clicking the [Clock Speed](/wiki/Clock_speed "Clock speed") value (Yellow under label) and typing "33.3334"%
  * Clicking the Target Production Rate value (Yellow under label) and typing "15 / 3" (Input fields can handle equations)



### Underclock all machines

Underclock both [Constructors](/wiki/Constructor "Constructor") to 67% has the benefit of improved [power](/wiki/Power "Power") saving compared to the previous method. You can examine the power consumption of each underclocked building and add them up.   
`1.3333 / 2 = 0.6666 = 67%`

## Complex production line

[](/wiki/File:Inefficient_RIP_production.png)

[](/wiki/File:Inefficient_RIP_production.png "Enlarge")

A working Reinforced Iron Plate production with incorrect building ratios. (Click to enlarge)

An example [Reinforced Iron Plate](/wiki/Reinforced_Iron_Plate "Reinforced Iron Plate") production line consists of multiple ingredients. In the above image, the buildings are 1:1 showing each stage of the production line with lower efficiency due to incorrect building ratio. Below is an analysis with a walkthrough to correct ratios: 

### Miner

[Miner Mk.1](/wiki/Miner_Mk.1 "Miner Mk.1") on a pure Iron node extracts 120 [Iron Ore](/wiki/Iron_Ore "Iron Ore")/min. [Pure nodes](/wiki/Purity "Purity") are quite common in [Northern Forest](/wiki/Northern_Forest "Northern Forest") and yield double rate. The [Conveyor Belt Mk.1](/wiki/Conveyor_Belt_Mk.1 "Conveyor Belt Mk.1") after it is not fast enough and should be replaced with [Conveyor Belt Mk.2](/wiki/Conveyor_Belt_Mk.2 "Conveyor Belt Mk.2"). 

### Smelter

A [Smelter](/wiki/Smelter "Smelter") consumes 30 [Iron Ore](/wiki/Iron_Ore "Iron Ore")/min and produces 30 [Iron Ingots](/wiki/Iron_Ingot "Iron Ingot")/min. Therefore the [Miner](/wiki/Miner "Miner") can support four Smelters.   
`120 / 30 = 4`

### Dividing Resources

Iron Ingots are divided among [Iron Rods](/wiki/Iron_Rod "Iron Rod") and [Iron Plates](/wiki/Iron_Plate "Iron Plate"), in an unknown ratio. The top-down method is an effective means to determine how to divide resources: start from the end product, then work backward to its raw ingredients. 

#### Reinforced Iron Plate

The [Assembler](/wiki/Assembler "Assembler") crafting [Reinforced Iron Plates](/wiki/Reinforced_Iron_Plate "Reinforced Iron Plate"), needs 30 [Iron Plates](/wiki/Iron_Plate "Iron Plate")/min and 60 [Screws](/wiki/Screw "Screw")/min. If either of the ingredients faces a shortage, the entire chain will be slowed down. 

#### Iron Plate

Each [Iron Plate](/wiki/Iron_Plate "Iron Plate") requires 1.5 [Iron Ingots](/wiki/Iron_Ingot "Iron Ingot") to craft (as described above). Therefore 30 [Iron Plates](/wiki/Iron_Plate "Iron Plate")/min requires 45 [Iron Ingots](/wiki/Iron_Ingot "Iron Ingot")/min.   
`30 * 1.5 = 45`

#### Screw

Each [Iron Rod](/wiki/Iron_Rod "Iron Rod") can be crafted into 4 [Screws](/wiki/Screw "Screw"). Therefore 60 [Screws](/wiki/Screw "Screw")/min requires 15 [Iron Rods](/wiki/Iron_Rod "Iron Rod")/min.   
`60 / 4 = 15`

#### Iron Rod

Each [Iron Rod](/wiki/Iron_Rod "Iron Rod") requires 1 [Iron Ingot](/wiki/Iron_Ingot "Iron Ingot"). Therefore 15 [Iron Rods](/wiki/Iron_Rod "Iron Rod")/min requires 15 [Iron Ingots](/wiki/Iron_Ingot "Iron Ingot")/min. 

#### Math it out

To produce 5 [Reinforced Iron Plates](/wiki/Reinforced_Iron_Plate "Reinforced Iron Plate")/min, the [Assembler](/wiki/Assembler "Assembler") requires, 45 [Iron Ingots](/wiki/Iron_Ingot "Iron Ingot")/min to produce [Iron Plates](/wiki/Iron_Plate "Iron Plate"), and 15 [Iron Ingots](/wiki/Iron_Ingot "Iron Ingot")/min to produce [Iron Rods](/wiki/Iron_Rod "Iron Rod"), for a total consumption of 60 [Iron Ingots](/wiki/Iron_Ingot "Iron Ingot")/min.   
`45 + 15 = 60`

By dividing these numbers, the ratio can be simplified to 3:1. Three quarters of the [Iron Ingot](/wiki/Iron_Ingot "Iron Ingot") production is dedicated to [Iron Plates](/wiki/Iron_Plate "Iron Plate"), and one quarter dedicated to [Iron Rods](/wiki/Iron_Rod "Iron Rod").   
`45 : 15 == 3 : 1` (divide both by 15) 

The [Miner](/wiki/Miner "Miner") above has the potential to produce 120 [Iron Ore](/wiki/Iron_Ore "Iron Ore")/min, which can be crafted into 120 [Iron Ingots](/wiki/Iron_Ingot "Iron Ingot")/min. This can support up to two [Assemblers](/wiki/Assembler "Assembler") simultaneously.   
`120 / 60 = 2`

After finding the ratio, work from the bottom-up reversing the calculation process, then multiply the setup by 2. 

### Constructor (Iron Plate)

`45 x 2 = 90`  
90 [Iron Ingots](/wiki/Iron_Ingot "Iron Ingot")/min craft into 60 [Iron Plates](/wiki/Iron_Plate "Iron Plate")/min, requiring three [Constructors](/wiki/Constructor "Constructor").   
`90 / 30 = 3`

### Constructor (Iron Rod)

`15 x 2 = 30`  
30 [Iron Ingots](/wiki/Iron_Ingot "Iron Ingot")/min craft into 30 [Iron Rods](/wiki/Iron_Rod "Iron Rod")/min, requiring two [Constructors](/wiki/Constructor "Constructor").   
`30 / 15 = 2`

### Constructor (Screw)

`60 x 2 = 120`  
30 [Iron Rods](/wiki/Iron_Rod "Iron Rod")/min craft into 120 [Screws](/wiki/Screw "Screw")/min, requiring three [Constructors](/wiki/Constructor "Constructor").   
`120 / 40 = 3`

### Assembler (Reinforced Iron Plate)

Two [Assemblers](/wiki/Assembler "Assembler") are required to craft the [Reinforced Iron Plate](/wiki/Reinforced_Iron_Plate "Reinforced Iron Plate"). 

### Conveyor Belt

[Splitters](/wiki/Conveyor_Splitter "Conveyor Splitter") and [Mergers](/wiki/Conveyor_Merger "Conveyor Merger") distribute items as required. Identify belts carrying more than 60 items/min, and construct them with [Conveyor Belt Mk.2](/wiki/Conveyor_Belt_Mk.2 "Conveyor Belt Mk.2") or above. 

[](/wiki/File:Efficient_RIP_production.png)

[](/wiki/File:Efficient_RIP_production.png "Enlarge")

An efficient Reinforced Iron Plate production with correct building ratios. [Foundations](/wiki/Foundations "Foundations") are used for easier alignment. (Click to enlarge)

## Online tools

[Online tools](/wiki/Online_tools "Online tools") can be used to great extent to lay out the production lines of any item using desired [alternate recipes](/wiki/Alternate_recipes "Alternate recipes"). 

  * [v](/wiki/Template:PioneerNav "Template:PioneerNav")
  * [e](https://satisfactory.wiki.gg/wiki/Template:PioneerNav?action=edit)
  * [h](https://satisfactory.wiki.gg/wiki/Template:PioneerNav?action=history)

[Satisfactory](/wiki/Satisfactory "Satisfactory") game mechanics  
---  
Player abilities| [Codex](/wiki/Codex "Codex") • [Resource Scanner](/wiki/Resource_Scanner "Resource Scanner") • [Build Gun](/wiki/Build_Gun "Build Gun") • [Inventory](/wiki/Inventory "Inventory") • [Health](/wiki/Health "Health") • [Combat](/wiki/Combat "Combat") • [Movement](/wiki/Movement "Movement") • [Flashlight](/wiki/Flashlight "Flashlight") • [HUD](/wiki/HUD "HUD") • [Crate](/wiki/Crate "Crate") • [To-Do List](/wiki/To-Do_List "To-Do List")  
Unlockable abilities| [Recipes](/wiki/Recipes "Recipes") • [Power](/wiki/Power "Power") • [Overclocking/Underclocking](/wiki/Clock_speed "Clock speed") • [Production amplifier](/wiki/Production_amplifier "Production amplifier") • [Customizer](/wiki/Customizer "Customizer") • [Map](/wiki/Map "Map") • [Productivity Display](/wiki/Productivity_Display "Productivity Display") • [Head lift](/wiki/Head_lift "Head lift") • [Blueprints](/wiki/Blueprints "Blueprints") • [Fuels](/wiki/Category:Fuels "Category:Fuels") • [FICSIT Productive Packer Deluxe](/wiki/FICSIT_Productive_Packer_Deluxe "FICSIT Productive Packer Deluxe")  
Progression| [Story](/wiki/Story "Story") • [Drop-pod](/wiki/Drop-pod "Drop-pod") • [Onboarding (In-game tutorial)](/wiki/Onboarding "Onboarding") • [Milestones](/wiki/Milestones "Milestones") • [MAM](/wiki/MAM "MAM") • [Alternate recipes](/wiki/Hard_Drive#Alternate_recipes "Hard Drive") • [Space Elevator](/wiki/Space_Elevator "Space Elevator") • [AWESOME Sink](/wiki/AWESOME_Sink "AWESOME Sink") • [AWESOME Shop](/wiki/AWESOME_Shop "AWESOME Shop")  
Seasonal events| [April Fools' Day](/wiki/April_Fools%27_Day "April Fools' Day") • [Anniversary](/wiki/Anniversary "Anniversary") • [FICSMAS](/wiki/FICSMAS "FICSMAS")  
Environment| [World](/wiki/World "World") • [Resource Node](/wiki/Resource_Node "Resource Node") • [Resource Well](/wiki/Resource_Well "Resource Well") • [Resource renewability](/wiki/Resource_renewability "Resource renewability") • [Crash Site](/wiki/Crash_Site "Crash Site") • [Radiation](/wiki/Radiation "Radiation") • [Poison Gas](/wiki/Poison_Gas "Poison Gas") • [Cracked boulder](/wiki/Cracked_boulder "Cracked boulder") • [Cave](/wiki/Cave "Cave")  
Gameplay| [Controls](/wiki/Controls "Controls") • [Settings](/wiki/Settings "Settings") • [Future content](/wiki/Future_content "Future content") • [Old unreleased content](/wiki/Old_unreleased_content "Old unreleased content") • [Online tools](/wiki/Online_tools "Online tools") • [Community resources](/wiki/Community_resources "Community resources") • [Advanced Game Settings](/wiki/Advanced_Game_Settings "Advanced Game Settings") • [Acronyms](/wiki/Acronyms "Acronyms") • [Achievements](/wiki/Achievements "Achievements") • [Easter eggs](/wiki/Easter_eggs "Easter eggs") • [Game menus](/wiki/Game_menus "Game menus") • [Indicator Light](/wiki/Indicator_Light "Indicator Light") • [Multiplayer](/wiki/Multiplayer "Multiplayer") • [Music](/wiki/Music "Music")  
Technical| [Console release](/wiki/Console_release "Console release") • [Debug console](/wiki/Debug_console "Debug console") • [Launch arguments](/wiki/Launch_arguments "Launch arguments") • [Save files](/wiki/Save_files "Save files") • [System requirements](/wiki/System_requirements "System requirements") • [Units](/wiki/Units "Units") • [Unreal Engine](/wiki/Unreal_Engine "Unreal Engine")  
Guides and tutorials| | Basics| [Walkthrough/How to play](/wiki/Tutorial:How_to_play "Tutorial:How to play") • [New Pioneer Guide](/wiki/Tutorial:New_Pioneer_Guide "Tutorial:New Pioneer Guide") • Production line basics • [Advanced production line tips](/wiki/Tutorial:Production_line_design_tips "Tutorial:Production line design tips") • [Picking an alternate recipe](/wiki/Tutorial:Picking_an_alternate_recipe "Tutorial:Picking an alternate recipe") • [Independency](/wiki/Tutorial:Independency "Tutorial:Independency") • [Aluminum Ingot production](/wiki/Tutorial:Setting_up_Aluminum_Ingot_production "Tutorial:Setting up Aluminum Ingot production")  
---|---  
Logistics| [Manifold](/wiki/Manifold "Manifold") • [Balancer](/wiki/Balancer "Balancer") • [Pipeline manifold](/wiki/Pipeline_manifold "Pipeline manifold") • [Prime Splitter Arrays](/wiki/Tutorial:Prime_splitter_arrays "Tutorial:Prime splitter arrays") • [Trains](/wiki/Tutorial:Trains "Tutorial:Trains") • [Train throughput](/wiki/Tutorial:Train_throughput "Tutorial:Train throughput")  
Dedicated servers| [Dedicated servers](/wiki/Dedicated_servers "Dedicated servers") • [Running as a Service](/wiki/Dedicated_servers/Running_as_a_Service "Dedicated servers/Running as a Service") • [Configuration files](/wiki/Dedicated_servers/Configuration_files "Dedicated servers/Configuration files") • [Automatic updates](/wiki/Dedicated_servers/Automatic_updates "Dedicated servers/Automatic updates") • [HTTPS API](/wiki/Dedicated_servers/HTTPS_API "Dedicated servers/HTTPS API") • [Lightweight Query API](/wiki/Dedicated_servers/Lightweight_Query_API "Dedicated servers/Lightweight Query API")  
Other| [Hypertube cannon](/wiki/Tutorial:Hypertube_cannon "Tutorial:Hypertube cannon") • [Hypertube brake](/wiki/Tutorial:Hypertube_brake "Tutorial:Hypertube brake") • [Steam Deck & Controller setup](/wiki/Tutorial:Controller_setup "Tutorial:Controller setup") • [Extracting UI icons](/wiki/Tutorial:Extracting_UI_icons "Tutorial:Extracting UI icons")
  *[v]: View this template
  *[e]: Edit this template
  *[h]: History of this template
  *[his]: his trivia section
