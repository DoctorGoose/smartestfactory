# Tutorial:Prime splitter arrays

[](/wiki/File:1-5th_splitter_array.png)  
  
[](/wiki/File:1-5th_splitter_array.png "Enlarge")

A simple 1/5th splitter array

**Prime splitter arrays** are a type of [load balancer](/wiki/Balancer#Load_balancer "Balancer"), splitting one conveyor belt input into a prime number of outputs. This can help in creating efficient production lines where a prime number of outputs (e.g. to machines) is needed. Splitter arrays and balancers in general differ from [manifolds](/wiki/Manifold "Manifold"), in that they fill every output simultaneously and don't require the first outputs in line to overfill. 

## Contents

  * 1 The problem
  * 2 Solution
    * 2.1 Proof of existence
    * 2.2 Creating the array
  * 3 Examples
    * 3.1 1 to 5
    * 3.2 1 to 11
    * 3.3 1 to 13
  * 4 Problems



## The problem

[](/wiki/Conveyor_Splitter "Conveyor Splitter") [Conveyor Splitters](/wiki/Conveyor_Splitter "Conveyor Splitter") can only split one input into one, two, or three outputs. This makes it easy to create load balancers with outputs that are multiples of these (e.g. 4,6,8,9,...) by chaining splitters. Prime numbers (by nature of being prime) on the other hand cannot be made from the simple chaining of splitters, requiring more complex arrays including "loop back", where one splitter moves items to a [](/wiki/Conveyor_Merger "Conveyor Merger") [Conveyor Merger](/wiki/Conveyor_Merger "Conveyor Merger") at a previous step in the array. 

So the problem is: What set of Splitters and Mergers creates outputs of 1/p of the input, where p is the wanted prime number of outputs? 

## Solution

The solution presented here, is to split the input into two, on part being a 1/p fraction of the input and the other being the remaining (p-1)/p of the input. The second output is then not prime and can be balanced further through more simple means. The entire setup consist of a line (or array) of mergers and splitters subdividing the input until the desired fraction 1/p is achieved. 

### Proof of existence

Here is a (not quite rigorous) proof that, such a setup exists. A way to create splitter arrays is given in the segment below. 

The problem can be simplified by saying the total input is 1 and viewing each Merger and Splitter as either adding to or dividing the throughput, e.g. a Splitter might create two outputs of 12 each. The goal is to find an array a of n divisions or additions, such that an=1p. Without loss of generality, the last step can be assumed to be a Splitter, dividing the input by 2 or 3. This means the array's last step (step #n) is: 

an=an−1s=1p⟺an−1=sps∈[2,3]

Or in other words: The input from the second to last step an−1 has to be sp. This is the same statement as before, just scaled by s. It follows, that a row of Splitters can produce the output an=1p , for any input in, that follows: 

in=qp

where q is a multiple of 1, 2 and 3. The problem becomes, to form such an input. By chaining enough Splitters q becomes large than p, and: 

in=qp ⟹q>p in=1+q′p

where the new q' is a multiple of 1,2 and 3 too. The input of 1 can come from the total input into the array and the q′ppart can be made, by merging outputs from Splitters. This is always possible, as the splitters themselves only produce fractions that are multiples of 1,2, and 3. Therefore, for any desired prime number p (actually any whole number) there exists a row of Mergers and Splitters such that the reciprocal of p is the output. It also follows, that the array consists first of a row of mergers creating a throughput of 1+q′p which then feeds into a row of splitters dividing this into the desired fraction of 1p. 

### Creating the array

This is a simple algorithm for creating a prime splitter array. It works by keeping track of the Splitter outputs and a number c: 

  1. Start at the output. This will be 1/p in the end. Set c to 1/p.
  2. Add a Splitter 
     * One belt goes into the previous step
     * All other belts will be set aside for later
     * Write down the output of each belt (this is c)
     * Multiply c by the number of outgoing belts
  3. If c less than 1 repeat step 2. Try to make c as close to 1 as possible.
  4. If c is greater than 1 add the necessary Mergers 
     * Subtract 1 from c
     * The remaining c has to be made up from adding the output of the splitters
     * All other remaining Splitter-outputs add up to (p-1)/p



For example a 1/11 splitter array can be constructed as such: 

[](/wiki/File:1_to_11_load_balancer.svg)

[](/wiki/File:1_to_11_load_balancer.svg "Enlarge")

1:11 prime splitter array. Rounded squares are Mergers, squares Splitters.

  * Set c to 1/11
  * Add a three-way Splitter (c = 3/11)
  * Add a two-way Splitter (c = 6/11)
  * Add another two-way splitter (c = 12/11)
  * Because c is now greater than 1 add a merger and belt the input to it
  * Remove 1 from c, c is now 1/11. This is what we additionally have to move into the merger
  * (Optional) Merge all remaining belts into one 10/11 belt.



  


## Examples

### 1 to 5

  * [](/wiki/File:1-5th_splitter_array.png "1 to 5 setup")

1 to 5 setup

  * [](/wiki/File:1_to_5_prime_splitter.svg "1 to 5 diagram")

1 to 5 diagram




### 1 to 11

  * [](/wiki/File:1-11th_splitter_array.png "1 to 11 setup")

1 to 11 setup

  * [](/wiki/File:1_to_11_load_balancer.svg "1 to 11 diagram")

1 to 11 diagram




### 1 to 13

  * [](/wiki/File:1-13th_splitter_array.png "1 to 13 setup")

1 to 13 setup

  * [](/wiki/File:1_to_13_prime_splitter.svg "1 to 13 diagram")

1 to 13 diagram




## Problems

This approach is not perfect, but it works for all prime numbers. Because the idea is to simplify the problem of creating one big 1:p load balancer into two easier steps (making on 1/p belt and (p-1)/p belt, subdividing the (p-1)/p belt) the entire setup becomes quite large. There exist[where?] "all-in-one" solutions for 1:p load balancers that are smaller and less costly. 

Additionally, due to the "loop-back" the belt directly after the merger carries more items per minute than the input belt. This means splitter arrays create a bottleneck and have to be supplied by a belt with empty slots. Also, the "loop-back" adds a slight delay, during which the splitter array has a slightly lower throughput than designed. 

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
Logistics| [Manifold](/wiki/Manifold "Manifold") • [Balancer](/wiki/Balancer "Balancer") • [Pipeline manifold](/wiki/Pipeline_manifold "Pipeline manifold") • Prime Splitter Arrays • [Trains](/wiki/Tutorial:Trains "Tutorial:Trains") • [Train throughput](/wiki/Tutorial:Train_throughput "Tutorial:Train throughput")  
Dedicated servers| [Dedicated servers](/wiki/Dedicated_servers "Dedicated servers") • [Running as a Service](/wiki/Dedicated_servers/Running_as_a_Service "Dedicated servers/Running as a Service") • [Configuration files](/wiki/Dedicated_servers/Configuration_files "Dedicated servers/Configuration files") • [Automatic updates](/wiki/Dedicated_servers/Automatic_updates "Dedicated servers/Automatic updates") • [HTTPS API](/wiki/Dedicated_servers/HTTPS_API "Dedicated servers/HTTPS API") • [Lightweight Query API](/wiki/Dedicated_servers/Lightweight_Query_API "Dedicated servers/Lightweight Query API")  
Other| [Hypertube cannon](/wiki/Tutorial:Hypertube_cannon "Tutorial:Hypertube cannon") • [Hypertube brake](/wiki/Tutorial:Hypertube_brake "Tutorial:Hypertube brake") • [Steam Deck & Controller setup](/wiki/Tutorial:Controller_setup "Tutorial:Controller setup") • [Extracting UI icons](/wiki/Tutorial:Extracting_UI_icons "Tutorial:Extracting UI icons")
  *[v]: View this template
  *[e]: Edit this template
  *[h]: History of this template
  *[his]: his trivia section
