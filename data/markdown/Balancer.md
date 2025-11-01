# Balancer

**Balancer** may refer to Load Balancer or Belt Balancer. [Splitters](/wiki/Splitter "Splitter") are built in a nested way, such that all downstream belts or buildings receive an equal amount of material, regardless if the supply belt is providing sufficient input. A factory that is built this way tends to start up faster, as there is no need to wait for the internal storage to pile up. The size of a balancer grows quadratically as the number of buildings increases.   
  
It is the opposite fill method to the [manifold](/wiki/Manifold "Manifold"). 

## Contents

  * 1 Load balancer
    * 1.1 Construction
  * 2 Belt balancer
    * 2.1 Construction
    * 2.2 Elimination
  * 3 Belt compressor
  * 4 Balancer examples
  * 5 Alternate Examples:
    * 5.1 **2-2:**
    * 5.2 **3-3:**
    * 5.3 **4-4:**
    * 5.4 **6-6:**
    * 5.5 **9-9:**
  * 6 External links
  * 7 See also



## Load balancer

A **load balancer** splits 1:n belts equally (one input belt, n output belts). 

### Construction

  * A [Splitter](/wiki/Splitter "Splitter") has a single belt input that can split into two or three outputs.
  * To make 1:4 or 1:8 balancer, simply nest the 1:2 balancers. To make a 1:9 or 1:27 balancer, simply nest the 1:3 balancers.
  * Similar to above, any balancer that can be made from multiplications of two and three can be built. Example, 6, 12, 18, 24, etc.
  * Balancers with other numbers can be built with simple loop-backs. This loopback will consume some of the belt capacity, reducing the overall throughput. Loop-backs of this sort are necessary for producing fractional splits with denominators that have a prime number composition of values other than two or three. This topic is discussed in detail at [Tutorial:Prime splitter arrays](/wiki/Tutorial:Prime_splitter_arrays "Tutorial:Prime splitter arrays"). 
    * Round up the number and build the nearest perfect balancer, then loop back all the unused output.
    * In some cases, there may be more than one unused output. Use mergers to combine them into a single belt before loopback.
  * To maintain the throughput, the loopback can be split and distributed evenly among the split outputs, using additional splitters and mergers.
  * All the above principles apply to balanced [Mergers](/wiki/Merger "Merger"). Just flip the entire setup vertically and swap all the splitters and mergers.

Odd-number balancers  1:n  | Modified from 1:m  | Outputs to loopback  | Remarks   
---|---|---|---  
5 | 6 | 1 |   
7 | 8 | 1 |   
10 | - | - | Split into two, each using 1:5 balancer   
11 | 12 | 1 |   
13 | 16 | 3 | Combine three unused outputs before loopback   
14 | - | - | Split into two, each using 1:7 balancer   
15 | 16 | 1 | Alternative to 1:15 split - split into 1:5, then each futher split into three.   
17 | 18 | 1 |   
  
  * [](/wiki/File:Balancer_nested.png "Nested balancers built from simple 1:2 or 1:3 balancers.")

Nested balancers built from simple 1:2 or 1:3 balancers.

  * [](/wiki/File:Balancer_compound.png "Balancers built from a combination of 1:2 and 1:3 balancers.")

Balancers built from a combination of 1:2 and 1:3 balancers.

  * [](/wiki/File:Balancer_odd.png "Odd-number balancers with loop-back \(prime splitter arrays\). The top examples have bottleneck problem, the bottom examples don't.")

Odd-number balancers with loop-back ([prime splitter arrays](/wiki/Tutorial:Prime_splitter_arrays "Tutorial:Prime splitter arrays")). The top examples have bottleneck problem, the bottom examples don't.




## Belt balancer

A **belt balancer** splits n:m belts equally (n input belt, m output belts). 

### Construction

A belt balancer can be built by interlacing multiple load balancers such that they have multiple inputs and multiple outputs. 

  * To maintain the throughput, make sure no segment of the belt is having an item flow rate higher than the capacity of the belt.
  * As such, always split before the merge.



### Elimination

Whenever possible, avoid the usage of belt balancers. Balancers take up a great deal of space, so it is generally _much_ easier to use another strategy to split up items. 

  * Consider using [manifolds](/wiki/Manifold "Manifold") instead, if the total item throughput is within the capacity of a belt.
  * Use modular building style for low-compression items, such as [Screws](/wiki/Screw "Screw") and [Quickwire](/wiki/Quickwire "Quickwire"). Group them near the buildings that use these ingredients.
  * If the output of a building exactly matches the input of another building, pair these buildings up. 
    * For example, pair an [Iron Ingot](/wiki/Iron_Ingot "Iron Ingot") [Smelter](/wiki/Smelter "Smelter") with an [Iron Plate](/wiki/Iron_Plate "Iron Plate") [Constructor](/wiki/Constructor "Constructor") or two [Wire](/wiki/Wire "Wire") Constructors with a [Cable](/wiki/Cable "Cable") Constructor.
  * If the item flow rates of the incoming belts are known to be equal, there is no need to balance them, regardless if each belt is full or not. 
    * E.g. two belts carrying 780 Iron Ore each.


  * [](/wiki/File:Belt_balancer_schematic.png "Schematics of belt balancer n:m.")

Schematics of belt balancer n:m.

  * [](/wiki/File:Belt_Balancer_2-2.png "2:2 belt balancer.")

2:2 belt balancer.




## Belt compressor

Sometimes it is useful to compress n-number of belts into m-number of full-belts, with the last belt carrying the remainder. This can be applicable to: Mega-factories and compressing from multiple sources (Eg multiple [Miner](/wiki/Miner "Miner") outputs). 

  * Fluctuating input rates can cause issues with simple belt compressors. 
    * This mainly happens in recipes that output multiple items at once 
      * Eg [Pure Iron Ingots](/wiki/Iron_Ingot "Iron Ingot") output 13 items at a time
    * The Any lines will fill, and the merger takes from them 50:50
    * This incorrectly causes overflow to the top line when space is available at the end of the current load
  * Buffered Belt Compressors utilize an [Industrial Storage Container](/wiki/Storage_Container#Industrial "Storage Container") as a buffered merger 
    * Consumes a much larger footprint
    * Requires 48 stacks to back-fill before overflow line begins
    * Has up to 48 stacks of back-fill to ensure main line is adequately supplied


  * [](/wiki/File:Belt_compressor_schematic.png "Schematics of belt compressor. If the remainder plus the incoming belt is less than a full belt capacity, continue merging to the next belt.")

Schematics of belt compressor. If the remainder plus the incoming belt is less than a full belt capacity, continue merging to the next belt.

  * [](/wiki/File:Implementation_of_a_vertical_Belt_Compressor.png "Top Smart Splitter: any center, overflow left; Bottom Smart Splitter: Any left, overflow center")

Top Smart Splitter: any center, overflow left; Bottom Smart Splitter: Any left, overflow center

  * [](/wiki/File:Implementation_of_a_Vertical_Buffered_Belt_Compressor.png "Utilizing an Industrial Storage Container as a buffer in a Belt Compressor")

Utilizing an Industrial Storage Container as a buffer in a Belt Compressor




## Balancer examples

[](/wiki/File:Two_3-to-3_belt_balancers_in_operation.png)

[](/wiki/File:Two_3-to-3_belt_balancers_in_operation.png "Enlarge")

Two 3-to-3 belt balancers in operation

Perhaps the most important element of factory design in Factorio was balancers. Balancers aren't as critical in Satisfactory for two reasons. The first is that even a massive factory can operate with only a few max-level belts of a single material on the main bus. The second is that Satisfactory machines have much larger buffers on the input and output. This allows for much greater irregularity in belt flow before machines start losing efficiency. That being said, balancers are still important. 

The concept of balancers is pretty simple. The output belts should be able to draw from the input belts at any ratio. There are hundreds of ways of configuring these but here are a few examples. 

**2-to-2 Belts**

[](/wiki/File:Schematic_of_a_2-to-2_belt_balancer.png)

[](/wiki/File:Schematic_of_a_2-to-2_belt_balancer.png "Enlarge")

_Schematic of a 2-to-2 belt balancer_

Definitely the easiest configuration, there is a load of ways to do this one. One possible configuration looks like this. Left shows the first layer, right the second. 

  * [](/wiki/File:Implementation_of_a_2-to-2_belt_balancer_\(1_of_2\).png "Layer 1")

Layer 1

  * [](/wiki/File:Implementation_of_a_2-to-2_belt_balancer_\(2_of_2\).png "Layer 2")

Layer 2




**3-to-3 Belts**

[](/wiki/File:Schematic_of_a_3-to-3_belt_balancer.png)

[](/wiki/File:Schematic_of_a_3-to-3_belt_balancer.png "Enlarge")

_Schematic of a 3-to-3 belt balancer_

The unique thing about Satisfactory, when compared to Factorio, is the fact that splitters and mergers operate on a 3-to-1 ratio. This means that, unlike Factorio, 3-to-3 belt balancers are straightforward. An example configuration looks like this with left-to-right showing the build-up of the layers. 

_Implementation of a 3-to-3 belt balancer._

  * [](/wiki/File:Implementation_of_a_3-to-3_belt_balancer_\(1_of_3\).png "Layer 1")

Layer 1

  * [](/wiki/File:Implementation_of_a_3-to-3_belt_balancer_\(2_of_3\).png "Layer 2")

Layer 2

  * [](/wiki/File:Implementation_of_a_3-to-3_belt_balancer_\(3_of_3\).png "Layer 3")

Layer 3




**4-to-4 Belts**

[](/wiki/File:Schematic_of_a_4-to-4_belt_balancer.png)

[](/wiki/File:Schematic_of_a_4-to-4_belt_balancer.png "Enlarge")

_Schematic of a 4-to-4 belt balancer_

4-to-4 belts are where balancers get interesting. An example using a grid of 2-to-2s as shown in the schematic on the right. 

  * [](/wiki/File:Implementation_of_a_4-to-4_belt_balancer_\(1_of_3\).png "Layer 1")

Layer 1

  * [](/wiki/File:Implementation_of_a_4-to-4_belt_balancer_\(2_of_3\).png "Layer 2")

Layer 2

  * [](/wiki/File:Implementation_of_a_4-to-4_belt_balancer_\(3_of_3\).png "Layer 3")

Layer 3




## Alternate Examples:

### **2-2:**

  * [](/wiki/File:2-2_Flat.png "2-2 Flat")

2-2 Flat

  * [](/wiki/File:2-2_Vertical.png "2-2 Vertical")

2-2 Vertical




### **3-3:**

  * [](/wiki/File:3-3_Flat.png "Left Splitter -> Left Inputs")

Left Splitter -> Left Inputs

  * [](/wiki/File:3-3_Vertical.png "Background: Top -> Bottom, Foreground: Bottom -> Top")

Background: Top -> Bottom, Foreground: Bottom -> Top




### **4-4:**

[](/wiki/File:4-4.png)

2-2 Flat -> 2-2 Vertical -> 2-2 Flat 

### **6-6:**

[](/wiki/File:3x3_flat_to_2x2_vertical_balancer.png)

3-3 flat -> 2-2 vertical (generally easier and smaller than a 5x5) 

### **9-9:**

[](/wiki/File:9-9.png)

3-3 Flat -> 3-3 Vertical -> 3-3 Flat 

## External links

  * [satisfactory-calculator.com - Balancers - by EDSM / Anthor](https://satisfactory-calculator.com/en/balancers)



## See also

  * [Manifold](/wiki/Manifold "Manifold")
  * [Tutorial:Prime splitter arrays](/wiki/Tutorial:Prime_splitter_arrays "Tutorial:Prime splitter arrays")



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
Guides and tutorials| | Basics| [Walkthrough/How to play](/wiki/Tutorial:How_to_play "Tutorial:How to play") • [New Pioneer Guide](/wiki/Tutorial:New_Pioneer_Guide "Tutorial:New Pioneer Guide") • [Production line basics](/wiki/Tutorial:Production_line "Tutorial:Production line") • [Advanced production line tips](/wiki/Tutorial:Production_line_design_tips "Tutorial:Production line design tips") • [Picking an alternate recipe](/wiki/Tutorial:Picking_an_alternate_recipe "Tutorial:Picking an alternate recipe") • [Independency](/wiki/Tutorial:Independency "Tutorial:Independency") • [Aluminum Ingot production](/wiki/Tutorial:Setting_up_Aluminum_Ingot_production "Tutorial:Setting up Aluminum Ingot production")  
---|---  
Logistics| [Manifold](/wiki/Manifold "Manifold") • Balancer • [Pipeline manifold](/wiki/Pipeline_manifold "Pipeline manifold") • [Prime Splitter Arrays](/wiki/Tutorial:Prime_splitter_arrays "Tutorial:Prime splitter arrays") • [Trains](/wiki/Tutorial:Trains "Tutorial:Trains") • [Train throughput](/wiki/Tutorial:Train_throughput "Tutorial:Train throughput")  
Dedicated servers| [Dedicated servers](/wiki/Dedicated_servers "Dedicated servers") • [Running as a Service](/wiki/Dedicated_servers/Running_as_a_Service "Dedicated servers/Running as a Service") • [Configuration files](/wiki/Dedicated_servers/Configuration_files "Dedicated servers/Configuration files") • [Automatic updates](/wiki/Dedicated_servers/Automatic_updates "Dedicated servers/Automatic updates") • [HTTPS API](/wiki/Dedicated_servers/HTTPS_API "Dedicated servers/HTTPS API") • [Lightweight Query API](/wiki/Dedicated_servers/Lightweight_Query_API "Dedicated servers/Lightweight Query API")  
Other| [Hypertube cannon](/wiki/Tutorial:Hypertube_cannon "Tutorial:Hypertube cannon") • [Hypertube brake](/wiki/Tutorial:Hypertube_brake "Tutorial:Hypertube brake") • [Steam Deck & Controller setup](/wiki/Tutorial:Controller_setup "Tutorial:Controller setup") • [Extracting UI icons](/wiki/Tutorial:Extracting_UI_icons "Tutorial:Extracting UI icons")
  *[v]: View this template
  *[e]: Edit this template
  *[h]: History of this template
