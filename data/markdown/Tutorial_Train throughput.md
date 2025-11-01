# Tutorial:Train throughput

The **actual in-game throughput of a[Freight Platform](/wiki/Freight_Platform "Freight Platform")** can be calculated if one wishes to be that precise. The most important variable in this determination is how long it takes a train to do a complete round trip, called Round-trip Duration (RtD). This is measured between the first and last departure "choo" at any single station on the route. 

After measuring the **Round-trip Duration (RtD)** using a stopwatch, the next thing you need to find is your **Time to Fill (TtF)**. This governs which equation is used to solve for throughput. 

## Contents

  * 1 Time to Fill
    * 1.1 Examples
  * 2 Calculating throughput
  * 3 Solved maximum throughput
    * 3.1 Note about Fluid Cars
    * 3.2 Use of external buffers
  * 4 Gallery
  * 5 References



## Time to Fill

Time to Fill is not in reference to how long it takes to fill a [Freight Platform](/wiki/Freight_Platform "Freight Platform"). It deals with how much time is required to fill the capacity of a [Freight Car](/wiki/Freight_Car "Freight Car"). 

Freight Car Capacity is 32 stacks for item cars, and 1600 m³ for fluid cars. Fluid isn't variable, as 1600 m³ is the same regardless of fluid type. Item freight's TtF however, will change based on the Stack Size of the items being moved. 

It is vital to remember that during each loading and unloading animation, the freight/fluid platform blocks all in-and outputs for 27.08 seconds[1] (0.4513 min). Bringing the lockout timer variable into the equation gives you the following: 

Time to Fill=Stack Size×Car capacityBelt Speed+0.4513‾min

As previously stated, the 0.4513 is converting 27.08s to minutes. Belt Speed is the combination of belts leading into the platform. At _most_ this number will be 2400 (when using ×2 Mk6 belts). Any combination of belt marks is possible, simply add the two numbers together for the maximum _theoretical_ throughput. For _actual_ maximum throughput, Belt Speed is equal to the exact items per minute being sent to the platform. 

### Examples

The TtF of an item with a Stack Size of 500, such as [](/wiki/Quickwire "Quickwire") [Quickwire](/wiki/Quickwire "Quickwire"), using 2× [](/wiki/Conveyor_Belt_Mk.5 "Conveyor Belt Mk.5") [Conveyor Belt Mk.5](/wiki/Conveyor_Belt_Mk.5 "Conveyor Belt Mk.5"): 

Time to Fill=500×321560+0.4513‾min=10.71min

Whereas an item with a Stack Size of 50, such as [](/wiki/Computer "Computer") [Computers](/wiki/Computer "Computer") takes: 

Time to Fill=50×321560+0.4513‾min=1.48min

About one seventh the amount of time compared to Quickwire. 

Doing [](/wiki/Quickwire "Quickwire") [Quickwire](/wiki/Quickwire "Quickwire") again, but with 2× [](/wiki/Conveyor_Belt_Mk.3 "Conveyor Belt Mk.3") [Conveyor Belt Mk.3](/wiki/Conveyor_Belt_Mk.3 "Conveyor Belt Mk.3") gives you: 

Time to Fill=500×32540+0.4513‾min=30.08min

## Calculating throughput

[](/wiki/File:Train_throughput_as_function_of_trip_time.jpg)

[](/wiki/File:Train_throughput_as_function_of_trip_time.jpg "Enlarge")

Throughput as a function of Round-trip Duration for a train car carrying items with a Stack Size of 500 and being loaded by ×2 Mk.4 Conveyor Belts.

> In both formulas, the maximum _theoretical_ throughput will have Belt Speed = 2400. For the _actual_ maximum throughput, Belt Speed is your actual item input rate. 

  * **TtF ≥ RtD**



If the Time to Fill is longer than (or equal to) the Round-trip Duration, the train car will be semi-loaded in most cases. The throughput formula used in this context is: 

Throughput=RtD−0.4513‾RtD×Belt Speed

> Note: You _can_ solve for the actual, in-game throughput using this formula if you take precise timing measurements. 
> 
> However, for ease of use, it is recommended to roughly time the route and solve for the maximum theoretical throughput. Once you know the maximum in theory, you can just compare that to how much you were planning to move. If you're under max theoretical throughput, you're good. 

  * **TtF < RtD**



If the Time to Fill is shorter than the Round-trip Duration, the train car will be fully loaded on every pickup. You do, however, lose throughput in this scenario due to wasted potential while waiting for the train to arrive. Throughput formula: 

Throughput=TtFRtD×Belt Speed

* * *

The only way to reach maximum theoretical throughput per car is if your Round-trip Duration is exactly equal to your Time to Fill. This is nearly impossible to do in a vacuum, and becomes even less likely in train systems with multiple trains, junctions, or even simply if the Stack Size of the items being loaded isn't a uniform number. 

Keep in mind, all of this is solving the throughput of a **single Freight/Fluid Platform**. If you wish to solve the throughput potential of an entire _train_ , it is more complicated. As you must do the above for each individual platform of the train, and that's assuming the train commutes only between 2 stations. In systems where one or more trains are making multiple stops, it is better to solve throughput for the drop-off platforms themselves, rather than try to equate how much an individual train is moving. 

## Solved maximum throughput

After solving the above, the maximum throughput numbers based on Stack Size are as follows: 

Freight | Stack Size | RtD (Mk.5) | Throughput (Mk.5) | RtD (Mk.6) | Throughput (Mk.6)   
---|---|---|---|---|---  
Items | 50 | 88.62s | 1083.3/min | 67.08s | 1,431.17/min   
100 | 150.16s | 1278.66/min | 102.08s | 1,793.08/min   
200 | 273.23s | 1405.4/min | 187.08s | 2,052.62/min   
500 | 642.46s | 1494.25/min | 427.08s | 2,247.83/min   
Fluid | 107.08 | 896.52 m³/min   
  
If your Round-trip Duration is shorter or longer than the above listed value, your attainable throughput will be lower than the maximum theoretical throughput. 

### Note about Fluid Cars

Freight Cars with Packaged Fluid are equal to the 100 per stack values, but if you're recycling the Empty Cans back, you need twice the amount of Freight Cars. This means in either case, you're using 2 Freight Cars to move 3200 units of fluid. (The only way to get around this would be sending the Empty Cans back via a different train, truck, or drone; or not recycling them at all by simply making them at pick-up and destroying them at drop-off). 

This changes the comparison of Fluid Cars vs. Freight Cars to: 

Freight | Stack Size | RtD (Mk.5) | Throughput (Mk.5) | RtD (Mk.6) | Throughput (Mk.6)   
---|---|---|---|---|---  
Canisters | 100 | 150.16s | 1278.66/min | 102.078s | 1,793.08/min   
Fluid | 107.08 | 1793.04 m³/min   
  
Meaning that, when used properly, Fluid Cars are _better_ in terms of throughput for moving your **liquids** until [](/wiki/Conveyor_Belt_Mk.6 "Conveyor Belt Mk.6") [Conveyor Belt Mk.6](/wiki/Conveyor_Belt_Mk.6 "Conveyor Belt Mk.6") is obtained, at which point they perform approximately equally. [](/wiki/Nitrogen_Gas "Nitrogen Gas") [Nitrogen Gas](/wiki/Nitrogen_Gas "Nitrogen Gas") should always be packaged before shipping as it has a 4x compression ratio (meaning a Freight Car can move 5114.64 (7,172.32) items/min). 

### Use of external buffers

Train logistics is the sole context in Satisfactory where "buffering" is needed.[2] [Industrial Storage Containers](/wiki/Industrial_Storage_Container "Industrial Storage Container") perfectly match the dual input/output of [Freight Platforms](/wiki/Freight_Platform "Freight Platform"), and can even be wrapped next to them to save space. Fluid Platforms require a more complicated configuration. Note that if you want consistently full belt output, you can simply choose to only use one of the output ports of the [Industrial Storage Container](/wiki/Industrial_Storage_Container "Industrial Storage Container"). 

## Gallery

  * [](/wiki/File:Train_Station_with_wrapped_Storage_Containers.jpg "Storage Containers being "wrapped" to save space.")

Storage Containers being "wrapped" to save space.

  * [](/wiki/File:Train_Station_with_600m3_Buffers.jpg "Fluid Buffer configuration, handles 600 m3/min per platform.")

Fluid Buffer configuration, handles 600 m3/min per platform.

  * [](/wiki/File:Train_Station_with_600m3_Industrial_Buffers.jpg "Industrial Fluid Buffers are needed for maximum potential.")

Industrial Fluid Buffers are needed for maximum potential.




## References

  1. ↑ [YouTube - October 3rd, 2023 Livestream - Q&A: Will the delay in throughput when loading/unloading of Trains be removed?](https://www.youtube.com/watch?v=4bQakQJ_aY4)
  2. ↑ [YouTube - October 3rd, 2023 Livestream - Q&A: Will the delay in throughput when loading/unloading of Trains be removed? - Use Storage Container Buffers](https://www.youtube.com/watch?v=4bQakQJ_aY4&t=38s)



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
Logistics| [Manifold](/wiki/Manifold "Manifold") • [Balancer](/wiki/Balancer "Balancer") • [Pipeline manifold](/wiki/Pipeline_manifold "Pipeline manifold") • [Prime Splitter Arrays](/wiki/Tutorial:Prime_splitter_arrays "Tutorial:Prime splitter arrays") • [Trains](/wiki/Tutorial:Trains "Tutorial:Trains") • Train throughput  
Dedicated servers| [Dedicated servers](/wiki/Dedicated_servers "Dedicated servers") • [Running as a Service](/wiki/Dedicated_servers/Running_as_a_Service "Dedicated servers/Running as a Service") • [Configuration files](/wiki/Dedicated_servers/Configuration_files "Dedicated servers/Configuration files") • [Automatic updates](/wiki/Dedicated_servers/Automatic_updates "Dedicated servers/Automatic updates") • [HTTPS API](/wiki/Dedicated_servers/HTTPS_API "Dedicated servers/HTTPS API") • [Lightweight Query API](/wiki/Dedicated_servers/Lightweight_Query_API "Dedicated servers/Lightweight Query API")  
Other| [Hypertube cannon](/wiki/Tutorial:Hypertube_cannon "Tutorial:Hypertube cannon") • [Hypertube brake](/wiki/Tutorial:Hypertube_brake "Tutorial:Hypertube brake") • [Steam Deck & Controller setup](/wiki/Tutorial:Controller_setup "Tutorial:Controller setup") • [Extracting UI icons](/wiki/Tutorial:Extracting_UI_icons "Tutorial:Extracting UI icons")
  *[v]: View this template
  *[e]: Edit this template
  *[h]: History of this template
  *[his]: his trivia section
