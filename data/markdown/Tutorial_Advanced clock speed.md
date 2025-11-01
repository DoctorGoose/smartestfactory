# Tutorial:Advanced clock speed

This page contains more in-depth information about [Clock speed](/wiki/Clock_speed "Clock speed") to help with more advanced over/under clocking use-cases. If you're looking for basic information, please visit [Clock speed](/wiki/Clock_speed "Clock speed").   


## Contents

  * 1 Clock speed for production buildings
    * 1.1 Remarkable clock speeds
    * 1.2 Basic underclocking
    * 1.3 Advanced underclocking
    * 1.4 Somersloop underclocking ("underslooping")
    * 1.5 Equalization of clock speeds
  * 2 Clock speed for power generators
    * 2.1 Fuel burn time formula
    * 2.2 Power capacity/fuel consumption rate formula
  * 3 Clock speed for miners and extractors
    * 3.1 Clock speed for water extractors
    * 3.2 Clock speed for resource well pressurizer
    * 3.3 Optimization
  * 4 See also



## Clock speed for production buildings

Production buildings craft at a rate proportional to their clock speed, but their power consumption changes polynomially N=1.321928. As the item production rate increases, the ingredient consumption rate increases as well. This means that it costs more power to produce the same amount of resources using buildings at higher clock speeds, but saves space. 

The table below shows five different clock speeds on a [](/wiki/Constructor "Constructor") [Constructor](/wiki/Constructor "Constructor") producing [](/wiki/Iron_Rod "Iron Rod") [Iron Rods](/wiki/Iron_Rod "Iron Rod"). 

[](/wiki/File:Clock_speed_power_consumption_graph.png)

[](/wiki/File:Clock_speed_power_consumption_graph.png "Enlarge")

The ratio of power consumption per craft based on clock speed. The ratio is compared to the amount of power for each craft at default clock speed. This is just for production buildings. Power Generator overclocking is linear

Clock speed | Craft time | Power required | Energy per Iron Rod   
---|---|---|---  
10% | 40s | 0.19 MW | 7.62 MJ | 47.6%   
50% | 8s | 1.6 MW | 12.8 MJ | 80%   
100% (Default) | 4s | 4 MW | 16 MJ | 100%   
150% | 2.67s | 6.8MW | 18.2 MJ | 113.9%   
200% | 2s | 10 MW | 20 MJ | 125%   
250% | 1.6s | 13.4 MW | 21.5 MJ | 134.3%   
  
[](/wiki/File:Overclocking_at_999.jpg)

[](/wiki/File:Overclocking_at_999.jpg "Enlarge")

Overclocking can be given any value, but the game will automatically clip it to between 1% to 250%.

The formula for power usage is: 

power usage=initial power usage×(clock speed100)1.321928  
---  
  
where clockspeed is a number with up to 4 decimals between 1 and 250, and   
both powerusage and initialpowerusage are measured in MW.  


The exponent 1.321928 is log2(2.5) rounded down, meaning you need 2.5x more power to double your productivity, this applies at any clock speed. 

For relative energy usage per item produced, subtract the exponent factor by 1, that is, 

energy usage=initial energy usage×(clock speed100)0.321928  
---  
  
Note that power usage is further influenced by [production amplification](/wiki/Production_amplification "Production amplification"). 

### Remarkable clock speeds

  * At 59% clock speed (59.1943) your power consumption is halved but you still produce 59% of the items, so by adding another 59% building you will produce 18% more items than a single 100% building for the same power usage.
  * At 169% clock speed (168.9353) your power consumption is equal to the consumption of 2 100% buildings but you will produce 169/200≈16% fewer items.
  * At 230% clock speed (229.5770) your power consumption is equal to the consumption of 3 100% buildings but you will produce 230/300≈23% fewer items.
  * At max clock speed (250) your power consumption is equal to the consumption of 3.36 100% buildings but you will produce 250/336≈26% fewer items.



### Basic underclocking

Power is an important parameter in any factory and some basic underclocking can help you reduce its usage. 

If you replace a building set at 100% clock speed with 2 buildings set at 50%, your production will remain the same but your power usage will be reduced by 20%. 

This can be computed as follows: 

Each 50% building will use 100×(50100)1.321928≈40% of the initial power, 2 buildings 80%, so you will save 20% of the initial power usage. 

By spreading your production evenly over more buildings you can save more power, but gains are less and less substantial as more buildings are added: 

Number of buildings | Clock speed | Power usage | Comment   
---|---|---|---  
1 | 100 | 100% |   
2 | 50 | 80% | -20% best gain for one more building   
3 | 33.3333 | 70.21% | -9.79% for one more building   
4 | 25 | 64% | -6.21%   
5 | 20 | 59.56% | -4.44%   
  
This example uses a base clock speed of 100% but you can use a different one. You will always get 20% power savings by spreading your production evenly over 2 buildings and other savings will be identical for n buildings as well. 

Underclocking can also save [](/wiki/Power_Shard "Power Shard") [Power Shards](/wiki/Power_Shard "Power Shard") which are best used in power generators, miners and extractors (see below), so it's even more profitable when some of your buildings are set at clock speeds higher than 100%. For instance: 

Number of buildings | Clock speed | Power usage | Power usage ratio | Comment   
---|---|---|---|---  
1 | 250 | 335.77% | 100% | Requires 3 power shards   
2 | 125 | 268.62% | 80% | -20% power usage and one less power shard   
3 | 83.3333 | 235.75% | 70.21% | Almost -30% power usage and no more power shards   
  
  
To sum up, this method allows you to maintain your production while reducing power usage, but there is a more advanced underclocking method allowing you to increase your production while maintaining the same power usage, described in the next section. 

### Advanced underclocking

The following setups have the same power usage: 

Number of buildings | Clock speed | Production | Comment   
---|---|---|---  
1 | 100.0000 | 100% |   
2 | 59.1943 | 118% | +18% best gain for one more building   
3 | 43.5584 | 131% | +13% for one more building   
4 | 35.0396 | 140% | +9%   
5 | 29.5971 | 148% | +8%   
10 | 17.5198 | 175% | 10 buildings may not be worth it...   
100 | 3.0694 | 307% | Good luck!   
440 | 1.0007 | 440% | You have time to spare   
441 | 0.9990 | - | You cannot set clock speeds < 1%   
  
You have to balance the complexity of logistics for having multiple buildings with production gains. 

In the table above production is rounded for clarity, but exact values can be computed using the following formulas: 

Clock speed for n buildings: 

clock speed=base clock speed×exp⁡(−ln⁡(n)1.321928)  
---  
  
Production % for n buildings: 

production=n×clock speed  
---  
  
In the table above base clock speed=100, but you can use any base clock speed between 1 and 250 in the formula, allowing you to underclock any of your buildings while maintaining the same power usage and getting additional power-free production. 

Production gains will always be the same for n buildings compared to the base clock speed. For instance, for a base clock speed of 250: 

Number of buildings | Clock speed | Production | Comment   
---|---|---|---  
1 | 250.0000 | 250% | 3 power shards   
2 | 147.9856 | 296% | Same production gain 118% (and one less power shard)   
3 | 108.8959 | 327% | Same production gain 131% compared to the base   
4 | 87.5990 | 350% | Same production gain 140% (and no more power shards)   
  
Additional notes regarding this technique: 

  * Added production is power-free but obviously not resource-free, you must have enough resources to support it.
  * If the added production is not needed in your current production line, you can send the surplus off to another line using a [](/wiki/Smart_Splitter "Smart Splitter") [Smart Splitter](/wiki/Smart_Splitter "Smart Splitter"), into the [](/wiki/AWESOME_Sink "AWESOME Sink") [AWESOME Sink](/wiki/AWESOME_Sink "AWESOME Sink") or into a green [](/wiki/Storage_Container "Storage Container") [Storage Container](/wiki/Storage_Container "Storage Container") with an adequate "eco" [](/wiki/Signs "Signs") [Sign](/wiki/Signs "Signs") on it.



### Somersloop underclocking ("underslooping")

[](/wiki/Somersloop "Somersloop") [Somersloops](/wiki/Somersloop "Somersloop") can be used for [production amplification](/wiki/Production_amplification "Production amplification") so it may seem counter-intuitive to use them in an underclocked building, however this technique is very useful if you need to produce an item you don't have enough resources for. 

When all Somersloops slots are filled, a building uses 4x more power but produces 2 times more items for the same input, so if you set your clock speed at 50%, you will produce the items you need at 100% rate using only half the resources and 60% more power (for power usage formula, see [Production amplifier](/wiki/Production_amplifier "Production amplifier")). 

Different results can be achieved by "underslooping" and are summarized in the following table: 

Clock speed | Production | Power usage | Comment   
---|---|---|---  
35.0396 | 70.0792 | 100 | Maintaining power usage at 100%, you can produce 70% of the items for 35% of the resources   
50 | 100 | 160 | For 60% more power, you can produce 100% of the items for 50% of the resources   
59.1943 | 118.3885 | 200 | For 2x more power, you can produce 118% of the items for 59% of the resources   
80.4429 | 160.8857 | 300 | For 3x more power, you can produce 160% of the items for 80% of the resources   
100 | 200 | 400 | Basic data: for 4x more power, you can produce 2x the items for 100% of the resources   
  
If, using Somersloops, your power usage is too high, you can also apply the technique explained in Basic underclocking. For instance, if you replace a slooped building set at 100% clock speed with 2 slooped buildings set at 50%, your production will remain the same but your power usage will be 160+160=320% instead of 400%, so you will gain 320/400=20% power. However, this costs additional Somersloops and they exist in a limited quantity. 

### Equalization of clock speeds

To optimize power usage it's always better to equalize clock speeds rather than having different clock speeds on the same production line. 

For instance if you have 2 [](/wiki/Blender "Blender") [Blenders](/wiki/Blender "Blender"), one set at 100% and the other one at 50%, they require 75+30=105 MW, by setting them both at (100+50)/2=75% they only require 2×51.27≈102.5 MW. 

Equalization can save [](/wiki/Power_Shard "Power Shard") [Power Shards](/wiki/Power_Shard "Power Shard") (150% + 50% -> 100% + 100%, you gain one power shard), however if the resulting clock speed is higher than 100% (for instance 150% + 100% -> 125% + 125%), equalization may also require more power shards. In this case you can solve the problem by adding more production buildings. 

## Clock speed for power generators

Power generators both generate power and consume fuel proportionally to their clock speed. A 1% increase in their clock speed causes them to produce 1% more power and consume 1% more fuel. The same amount of power is always produced from the same amount of fuel. Thus, overclocking generators simply saves space, but might cost a large amount of [](/wiki/Power_Shard "Power Shard") [Power Shards](/wiki/Power_Shard "Power Shard") for large power plants. 

The table below details the rates of a [](/wiki/Coal_Generator "Coal Generator") [Coal Generator](/wiki/Coal_Generator "Coal Generator") fuelled with [](/wiki/Coal "Coal") [Coal](/wiki/Coal "Coal"). The same logic applies to all other power generators, excluding [](/wiki/Geothermal_Generator "Geothermal Generator") [Geothermal Generators](/wiki/Geothermal_Generator "Geothermal Generator"), which cannot be overclocked at all. 

Clock speed | Coal burn time | Coal per minute | Energy per Coal | Operating rate   
---|---|---|---|---  
10% | 40 s | 1.5 | 300 MJ | 7.5 MW | 10%   
100% (Default) | 4 s | 15 | 300 MJ | 75 MW | 100%   
250% | 1.6 s | 37.5 | 300 MJ | 187.5 MW | 250%   
  
### Fuel burn time formula

fuel burn time=initial fuel burn time×100clock speed  
---  
  
where clock speed is a number with up to 4 decimals between 1 and 250, and   
both fuel burn time and initial fuel burn time are measured in seconds. 

### Power capacity/fuel consumption rate formula

power capacity=initial power capacity×clock speed100  
---  
  
Clock speed is a number with up to 4 decimals between 1 and 250. Both power capacity and initial power capacity are measured in MW.  
Replace power capacity and initial power capacity with fuel consumption rate and initial fuel consumption rate measured in parts per minute or m3/min to get the fuel consumption rate. 

## Clock speed for miners and extractors

Overclocking [](/wiki/Miner "Miner") [Miners](/wiki/Miner "Miner") and [Oil Extractors](/wiki/Oil_Extractor "Oil Extractor") is highly beneficial as it allows you to extract more ore/oil per node. In terms of energy per ore/oil extracted, an overclocked miner/extractor on a higher-purity node can also be more efficient than a non-overclocked one on a lower-purity node. Defining the energy efficiency as the energy required per ore or oil extracted: 

  * mining a pure node at 250% has the same energy efficiency as mining a normal node at 78.74% or an impure node at 24.80%
  * mining a normal node at 250% has the same energy efficiency as mining an impure node at 78.74%



More generally, stepping up the node purity by one level while simultaneously multiplying the clock speed by 25/3≈3.175 results in the same energy efficiency (energy requirement per ore or oil extracted). 

Since, for the same clock rate, higher-purity nodes require significantly less energy per ore or oil extracted, a simple strategy for reducing power consumption associated with extraction is: 

  1. fully overclock pure nodes before extracting anything from normal nodes, then
  2. fully overclock normal nodes before extracting anything from impure nodes.



A more optimal approach is detailed below, but the power savings relative to this simple strategy are generally modest. 

### Clock speed for water extractors

_Main article:_[ Water Extractor > Overclocking](/wiki/Water_Extractor#Overclocking "Water Extractor")

### Clock speed for resource well pressurizer

_Main article:_[ Resource Well Pressurizer > Overclocking](/wiki/Resource_Well_Pressurizer#Overclocking "Resource Well Pressurizer")

### Optimization

When you have access to more than enough nodes to satisfy your extraction requirements, the _most_ power-efficient way of extracting ore or oil involves taking a lot from the pure nodes, a moderate amount from the normal nodes, and a tiny amount from the impure nodes, so that the energy efficiency per ore or oil extracted is the same across all nodes. Suppose that you have access to 

  * np pure nodes
  * nn normal nodes
  * ni impure nodes



and that you will be tapping each node with an extractor with a base extraction rate of B as described below: 

Extractor | Base Extraction Rate, B  
---|---  
Miner Mk.1 | 60 ore/min   
Miner Mk.2 | 120 ore/min   
Miner Mk.3 | 240 ore/min   
Oil Extractor | 120 oil/min   
  
If your target extraction rate is X ore or oil per minute, the most energy-efficient clock rates can be determined as follows: 

  1. Calculate the power consumption required for the simple approach described above (overclocking high purity before tapping lower purity). This is an optimistic upper bound on the power you could save by fully optimizing the clock speeds - does it seem like a lot to you? If not, then you shouldn't bother with this optimization. 
  2. Solve for c as:  c=XB(2⋅np+2−5/3⏟≈0.315⋅nn+2−13/3⏟≈0.0496⋅ni)  
---  
  3. Assuming no belt or clock limits, the ideal clock rates would be: 
     * 100%⋅c for each pure node
     * 100%⋅c/25/3≈31.5%⋅c for each normal node
     * 100%⋅c/210/3≈9.92%⋅c for each impure node
Unfortunately, this operating point will not always be realizable, either because: 
     * it requires the pure extractors to operate at a clock speed over 250%, or
     * it requires the pure extractors to exceed the Mk.2 pipe limit of 600 fluid/min
In these cases, the pure extractors should be set to the highest usable clock rate (250% for Mk.3 miners with Mk.6 belts and Oil Extractors with Mk.2 pipes) and then the algorithm should be repeated to determine how best to use the normal and impure nodes to gather the balance of the ore or oil. If this second solution requires the normal extractors to be set to a clock rate over 250%, then the normal extractors should be set to 250% and the impure extractors should be set to whatever rate is required to gather the balance of the ore or oil. If this again requires a clock rate over 250%, then X is too high for given nodes. 




For example, if you would like to extract 1800 oil from a combination of 2 pure nodes, 3 normal nodes, and 5 impure nodes, then 

  * B=120 oil/min for an oil extractor
  * np=2, nn=3, and ni=5
  * X=1800 oil/min
  * The simple way to achieve this extraction rate is to fully overclock both pure nodes (1200 oil/min) and then tap and fully overclock just two normal nodes (600 oil/min). This would require 4 fully overclocked Oil Extractors, which would consume 693.14 MW. This is therefore the optimistic upper bound on the power savings. It seems worthwhile, although we should remember that this is an _optimistic_ estimate and our actual savings will likely be lower.
  * The calculation gives c=2.889, so 
    * The pure extractors should be operated at 288.9%. This exceeds 250%, so we instead must assume that the 2 pure extractors operate at 250%, collectively producing 1200 oil/min
    * As a sub-calculation, we repeat with np=𝟎, nn=3, ni=5, X=𝟔𝟎𝟎 oil/min. This gives c=4.19, so 
      * The normal nodes should be operated at 132.0%
      * The impure nodes should be operated at 41.58%



This would require 582.83 MW, a savings of 110.3 MW. 

## See also

  * [Clock speed](/wiki/Clock_speed "Clock speed")
  * [Production amplifier](/wiki/Production_amplifier "Production amplifier")



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
Logistics| [Manifold](/wiki/Manifold "Manifold") • [Balancer](/wiki/Balancer "Balancer") • [Pipeline manifold](/wiki/Pipeline_manifold "Pipeline manifold") • [Prime Splitter Arrays](/wiki/Tutorial:Prime_splitter_arrays "Tutorial:Prime splitter arrays") • [Trains](/wiki/Tutorial:Trains "Tutorial:Trains") • [Train throughput](/wiki/Tutorial:Train_throughput "Tutorial:Train throughput")  
Dedicated servers| [Dedicated servers](/wiki/Dedicated_servers "Dedicated servers") • [Running as a Service](/wiki/Dedicated_servers/Running_as_a_Service "Dedicated servers/Running as a Service") • [Configuration files](/wiki/Dedicated_servers/Configuration_files "Dedicated servers/Configuration files") • [Automatic updates](/wiki/Dedicated_servers/Automatic_updates "Dedicated servers/Automatic updates") • [HTTPS API](/wiki/Dedicated_servers/HTTPS_API "Dedicated servers/HTTPS API") • [Lightweight Query API](/wiki/Dedicated_servers/Lightweight_Query_API "Dedicated servers/Lightweight Query API")  
Other| [Hypertube cannon](/wiki/Tutorial:Hypertube_cannon "Tutorial:Hypertube cannon") • [Hypertube brake](/wiki/Tutorial:Hypertube_brake "Tutorial:Hypertube brake") • [Steam Deck & Controller setup](/wiki/Tutorial:Controller_setup "Tutorial:Controller setup") • [Extracting UI icons](/wiki/Tutorial:Extracting_UI_icons "Tutorial:Extracting UI icons")
  *[v]: View this template
  *[e]: Edit this template
  *[h]: History of this template
  *[his]: his trivia section
