# Head lift

[](/wiki/File:Head_lift_demonstration.png)

[](/wiki/File:Head_lift_demonstration.png "Enlarge")

Head lift is only affected by the elevation difference but not the shape of the [Pipeline](/wiki/Pipeline "Pipeline").

[](/wiki/File:Head_lift_indicator.mp4 "Enlarge")

When building a new [Pipeline Pump](/wiki/Pipeline_Pump "Pipeline Pump"), its Head lift indicators appear as blue markings, which shows the maximum height fluids can go. Additional pumps can be snapped at these markings.

**Head lift** determines how high [fluids](/wiki/Fluids "Fluids") can be pushed up. Only the vertical distance, or the difference between the elevation of starting and ending points, matters; it does not depend on the [Pipeline](/wiki/Pipeline "Pipeline")'s shape. Each meter of head lift can lift the fluid by one meter vertically. Fluids can flow freely along perfectly horizontal pipelines. 

Head lift does not depend on the flow rate. It does not apply to [Gases](/wiki/Gases "Gases") (gas can overcome any vertical height difference). 

While not exactly the same, head lift is an approximation for _pressure_ inside a pipe. However, it doesn't affect flow rate _directly_ , so it cannot be compared to real pressure. 

As such, when talking about head lift, it is "applied" or "generated" by pumps and machines and it is _increased_ through gravity. 

The following [buildings](/wiki/Building "Building") can apply head lift: 

  * [](/wiki/Pipeline_Pump_Mk.1 "Pipeline Pump Mk.1") [Pipeline Pump Mk.1](/wiki/Pipeline_Pump_Mk.1 "Pipeline Pump Mk.1") – 20 meters
  * [](/wiki/Pipeline_Pump_Mk.2 "Pipeline Pump Mk.2") [Pipeline Pump Mk.2](/wiki/Pipeline_Pump_Mk.2 "Pipeline Pump Mk.2") – 50 meters
  * [](/wiki/Water_Extractor "Water Extractor") [Water Extractor](/wiki/Water_Extractor "Water Extractor"), [](/wiki/Oil_Extractor "Oil Extractor") [Oil Extractor](/wiki/Oil_Extractor "Oil Extractor"), [](/wiki/Refinery "Refinery") [Refinery](/wiki/Refinery "Refinery"), [](/wiki/Fluid_Freight_Platform "Fluid Freight Platform") [Fluid Freight Platform](/wiki/Fluid_Freight_Platform "Fluid Freight Platform"), [](/wiki/Packager "Packager") [Packager](/wiki/Packager "Packager"), [](/wiki/Resource_Well_Extractor "Resource Well Extractor") [Resource Well Extractor](/wiki/Resource_Well_Extractor "Resource Well Extractor"), [](/wiki/Blender "Blender") [Blender](/wiki/Blender "Blender") – 10 meters



The following [buildings](/wiki/Building "Building") can store and relay head lift: 

  * [](/wiki/Industrial_Fluid_Buffer "Industrial Fluid Buffer") [Industrial Fluid Buffer](/wiki/Industrial_Fluid_Buffer "Industrial Fluid Buffer") – up to 12 meters
  * [](/wiki/Fluid_Buffer "Fluid Buffer") [Fluid Buffer](/wiki/Fluid_Buffer "Fluid Buffer") – up to 8 meters
  * [](/wiki/Pipeline "Pipeline") [Pipeline](/wiki/Pipeline "Pipeline") (Mk.1 and Mk.2) and – horizontal: 1.3 meters, vertical: same as pipe length



For example, a Water Extractor outputs [Water](/wiki/Water "Water") with a head lift of 10 meters; this means the Water Extractor can push Water up to 10 meters vertically. 

Head lift applied by different buildings has a different base starting point, see below. 

## Contents

  * 1 Head lift and elevation difference
  * 2 Recommended, actual and maximum head lift
  * 3 Pipelines and Fluid Buffers
  * 4 Head lift merging and splitting
  * 5 Pipeline Pumps
    * 5.1 Exploits
  * 6 Fluid Freight Platform
  * 7 Gallery



## Head lift and elevation difference

The head lift required to fill a fluid container is equal to the elevation difference, measured from the base point of the source of fluid to the top level of the fluid container. 

Head lift is never mesured from top to bottom, only from bottom to top. 

Diagonal pipelines are an exception: the reading of head lift, as displayed on a Pipeline Pump, will be slightly higher and not linear. 

Currently, the only way to measure head lift is by constructing a Pipeline Pump on the pipeline at the elevation of measurement then interact [`E`](/wiki/Controls "Controls") with it. Head lift can be estimated by calculating the elevation difference, using [Walls](/wiki/Walls "Walls") (four meters high), [Foundations](/wiki/Foundations "Foundations") (four meters, two meters, or one meter high) or [Beams](/wiki/Beams "Beams") (variable length). 

## Recommended, actual and maximum head lift

The recommended head lift can be found in the building's description in the build menu. Within the recommended head lift, fluids flow freely without resistance. The system may continue to work one or two meters higher than that, which marks the actual head lift. Beyond that, flow rate drops abruptly, down to zero flow around two to three meters beyond the recommended head lift, which marks the 'maximum head lift'. When approaching the maximum head lift, fluids start to act in strange ways: fluid may or may not flow, and may sometimes oscillate forward and backward while attempting to achieve the head lift equilibrium, producing inconsistent behavior. Thus, it is always recommended to keep the system within the actual head lift. 

Building | Head lift (in meters)   
---|---  
Recommended | Actual | Maximum   
[](/wiki/Pipeline_Pump_Mk.1 "Pipeline Pump Mk.1") [Pipeline Pump Mk.1](/wiki/Pipeline_Pump_Mk.1 "Pipeline Pump Mk.1") | 20 | 22 | 23   
[](/wiki/Pipeline_Pump_Mk.2 "Pipeline Pump Mk.2") [Pipeline Pump Mk.2](/wiki/Pipeline_Pump_Mk.2 "Pipeline Pump Mk.2") | 50 | 55 | 57   
[](/wiki/Water_Extractor "Water Extractor") [Water Extractor](/wiki/Water_Extractor "Water Extractor") | 10 | 12 | 13   
[](/wiki/Oil_Extractor "Oil Extractor") [Oil Extractor](/wiki/Oil_Extractor "Oil Extractor") | 10 | 12 | 13   
[](/wiki/Refinery "Refinery") [Refinery](/wiki/Refinery "Refinery") | 10 | 11 | 13   
[](/wiki/Packager "Packager") [Packager](/wiki/Packager "Packager") | 10 | 11 | 13   
[](/wiki/Resource_Well_Extractor "Resource Well Extractor") [Resource Well Extractor](/wiki/Resource_Well_Extractor "Resource Well Extractor") | 10 | 11 | 13   
[](/wiki/Blender "Blender") [Blender](/wiki/Blender "Blender") | 10 | 11 | 13   
[](/wiki/Fluid_Buffer "Fluid Buffer") [Fluid Buffer](/wiki/Fluid_Buffer "Fluid Buffer")* | 8 | 8 | 8   
[](/wiki/Industrial_Fluid_Buffer "Industrial Fluid Buffer") [Industrial Fluid Buffer](/wiki/Industrial_Fluid_Buffer "Industrial Fluid Buffer")* | 12 | 12 | 12   
[](/wiki/Fluid_Freight_Platform "Fluid Freight Platform") [Fluid Freight Platform](/wiki/Fluid_Freight_Platform "Fluid Freight Platform") (bottom outlet) | 10 | 11 | 13   
[](/wiki/Fluid_Freight_Platform "Fluid Freight Platform") [Fluid Freight Platform](/wiki/Fluid_Freight_Platform "Fluid Freight Platform") (top outlet) | 10 | 11 | 13   
  
Note: See Pipelines and Fluid Buffers below for how buffers interact with head lift. 

[](/wiki/File:Head_lift_comparison.png "Head lift produced by various buildings")

## Pipelines and Fluid Buffers

A perfect horizontal [Pipeline](/wiki/Pipeline "Pipeline") will show a head lift of around 1.3 meters when filled completely, regardless of its length. Even if the applied head lift is 0m, the pipe will still be able to fill completely. 

Head lift from machines (such as Refineries, Water Extractors Pipeline Pumps, Fluid Freight Platforms, etc.) can only be propagated between completely filled pipeline segments. Very long pipes take a while to fill, but once full fluids in it can flow with the pipes maximum flow rate (or whatever the source's flow rate is). 

A pipeline segment will require head lift equal to its vertical length in order to be filled completely, measured from its bottom end to the top end, and for fluid to flow from the base to the top. The Head lift in a pipe is proportional to the percentage of the fluid in it; for instance, a half-filled 10-meter vertical pipeline will show a head lift of five meters. A very tall pipe requires a very high head lift to be filled. If a lower head lift is provided, it can only be filled partially. 

If somehow the fluid source is stopped and the source's head lift drops, the previously stored head lift in pipes will attempt to equalize among connected pipelines; this means fluids can backflow from the pipes with higher head lift to the pipes with lower head lift, as pipelines are bi-directional in nature. For example, if there are two horizontal pipelines with identical length connected in series, with one of them filled and the other one emptied, then the fluid within them will equalize themselves until both are filled equally, that is, 50% full. During this equalization process, the fluid flow can oscillate back and forth, taking a long time before it fully stabilizes. 

All of the above principles also hold for [Fluid Buffers](/wiki/Fluid_Buffer "Fluid Buffer") and [Industrial Fluid Buffers](/wiki/Industrial_Fluid_Buffer "Industrial Fluid Buffer") – they are just Pipelines but with much larger capacity and head lift. Note that their stored head lift is counted from the center of the pipe segment ends, not from the Foundation level. Combining all the above knowledge, chaining multiple Fluid Buffers in series is a bad idea as the system requires a very long start-up time – consider attaching buffers to the 'sideways' of a Pipeline instead, by using [Junctions](/wiki/Junction "Junction"). 

  * [](/wiki/File:Buffer_and_Pump_Results.png "Buffers propagate head lift proportional to their fill height.")

Buffers propagate head lift proportional to their fill height.

  * [](/wiki/File:Ficsit_Pipeline_Infograph_2.png "A short guide detailing Buffer Head Lift and behavior in combination with Pipeline Pumps.")

A short guide detailing Buffer Head Lift and behavior in combination with Pipeline Pumps.

  * [](/wiki/File:Fluid_Buffer_connection_types.png "Different styles of connecting Fluid Buffers into a pipeline.")

Different styles of connecting [Fluid Buffers](/wiki/Fluid_Buffer "Fluid Buffer") into a pipeline.




## Head lift merging and splitting

[](/wiki/File:Ficsit_Pipeline_Infograph_1.png)

[](/wiki/File:Ficsit_Pipeline_Infograph_1.png "Enlarge")

Pipeline Pump behavior and usage

When a single fluid source is split into multiple pipelines via a [Pipeline Junction Cross](/wiki/Pipeline_Junction_Cross "Pipeline Junction Cross"), the output head lift of each pipe is equal to the input: `outA = outB = in`. The flow rate is split, but the head lift is not. 

When multiple fluid sources with different head lifts are joined via a Pipeline Junction Cross, the highest head lift among them is applied to the entire pipe network: `out = Max (inA, inB)`. This 'sharing' effect will not hinder the output of fluid buildings with a lower head lift or positioned at the lower points; for instance, a Water Extractor with its output pipe under a head lift of much greater than 12 meters will still be able to push out Water, provided there is space allowed for it to do so. 

Both of the above hold true regardless of the flow rate of input and output pipelines. 

## Pipeline Pumps

A [non-powered](/wiki/Power "Power") Pipeline Pump acts as a one-way valve and resets the head lift back to zero meters. A powered Pipeline Pump resets the head lift to 20 or 50 meters (depending on Mk. level) as long as there is fluid reaching its input, regardless of the head lift preceding it. That also means building multiple Pipeline Pumps nearby is very inefficient, and each of them costs power to function. Pipeline Pumps should be spaced vertically to make full use of their applied head lift. 

  * [](/wiki/File:Pipeline_Pump_max_Head_Lift.png "Pipeline Pumps continue to function with full flow rate even at two meters above its recommended head lift.")

Pipeline Pumps continue to function with full flow rate even at two meters above its recommended head lift.




### Exploits

Pipeline Pumps, if used in large quantities, can be a burden to the [power grid](/wiki/Power_grid "Power grid"), thus an innovative solution is highly desirable to minimize power usage. When multiple fluid sources with different head lifts are connected to a single or multiple pipelines, the highest head lift among them will be applied to the entire connected pipe network. This head lift sharing effect makes head lift exploits possible. By using a water tower with zero output, free-energy lifting can be achieved. 

  * To do so, first construct as many [Water Extractors](/wiki/Water_Extractor "Water Extractor") at the lower area as you need.
  * Build a floating factory above the lower Extractors at any height you wish. Connect the pipes between the factory needing the [Water](/wiki/Water "Water") and those Extractors. In the image below, an [Industrial Fluid Buffer](/wiki/Industrial_Fluid_Buffer "Industrial Fluid Buffer") is used, you can replace it with the actual factory setup.
  * Around the same height, construct a [Fluid Buffer](/wiki/Fluid_Buffer "Fluid Buffer") and fill it up, either by using another Water Extractor or using [Pipeline Pumps](/wiki/Pipeline_Pump "Pipeline Pump") from below. Let's call this Buffer 'water tower'.
  * From the water tower, construct a downward pipe and connect it to the lower [pipeline](/wiki/Pipeline "Pipeline") via [junctions](/wiki/Junction "Junction"). If you have a large setup consisting of multiple parallel pipelines, connect all of them at the lower point.
  * Construct a [Valve](/wiki/Valve "Valve") on the water tower downward pipe to restrict its flow to zero m3/min. The Valve can be located at any position between the water tower and the lower junction, however, if it is above the head lift height of the Water Extractors, the pipe segment between the valve and the junction can become less than 100% full, in which case it will stop transmitting head lift from beyond the valve (this will only happen if the output side also becomes lower than the valve height, otherwise the output will cause enough head lift to refill the pipe). Therefore it's best to put the valve close to the extractors to avoid surprise jams.
  * Once the downward-facing pipe and the water tower are full, you may dismantle the pipes, Extractor, and Pipeline Pumps (if any) that are used to fill up the buffer. Since the water tower will always be full, no energy is required to maintain the head lift for the water tower.
  * All the pipes will then share the head lift from the water tower. Enjoy the free-energy fluid lifts!


  * [](/wiki/File:Head_lift_exploit.png "Demonstrating the head lift exploit. This can also be applied to fluids other than Water.")

Demonstrating the head lift exploit. This can also be applied to [fluids](/wiki/Fluids "Fluids") other than [Water](/wiki/Water "Water").




## Fluid Freight Platform

A [Fluid Freight Platform](/wiki/Fluid_Freight_Platform "Fluid Freight Platform") do not count as pipes and as such do not require any more head lift to be filled, and thus a fluid source can easily fill it up as long as the pipe inlet level of the Fluid Platform is within the source's head lift. As such it is advised to always use its lower pipe inlet first, followed by the upper inlet if the input rate higher than the max flow rate of used pipes is desired. 

A Fluid Freight Platform requires a connected powered Train Station to receive and/or output fluid. It can output fluid regardless if it is set to load or unload. 

The head lift provided by a Fluid Freight Platform is 10 meters, measured from the pipe connector. As such, it is always advantageous to use the upper pipe outlet first, followed by the lower outlet if the output rate higher than the max flow rate of used pipes is desired. 

## Gallery

  * [](/wiki/File:Gravity_in_Pipelines_1.png)

  * [](/wiki/File:Gravity_in_Pipelines_2.png)

  * [](/wiki/File:Gravity_in_Pipelines_3.png)

  * [](/wiki/File:Pipeline_overflow_with_head_lift.png "A setup which causes one Pipeline to be preferred over the other, due to Pipelines lower down being filled as a priority")

A setup which causes one Pipeline to be preferred over the other, due to Pipelines lower down being filled as a priority




  * [v](/wiki/Template:PioneerNav "Template:PioneerNav")
  * [e](https://satisfactory.wiki.gg/wiki/Template:PioneerNav?action=edit)
  * [h](https://satisfactory.wiki.gg/wiki/Template:PioneerNav?action=history)

[Satisfactory](/wiki/Satisfactory "Satisfactory") game mechanics  
---  
Player abilities| [Codex](/wiki/Codex "Codex") • [Resource Scanner](/wiki/Resource_Scanner "Resource Scanner") • [Build Gun](/wiki/Build_Gun "Build Gun") • [Inventory](/wiki/Inventory "Inventory") • [Health](/wiki/Health "Health") • [Combat](/wiki/Combat "Combat") • [Movement](/wiki/Movement "Movement") • [Flashlight](/wiki/Flashlight "Flashlight") • [HUD](/wiki/HUD "HUD") • [Crate](/wiki/Crate "Crate") • [To-Do List](/wiki/To-Do_List "To-Do List")  
Unlockable abilities| [Recipes](/wiki/Recipes "Recipes") • [Power](/wiki/Power "Power") • [Overclocking/Underclocking](/wiki/Clock_speed "Clock speed") • [Production amplifier](/wiki/Production_amplifier "Production amplifier") • [Customizer](/wiki/Customizer "Customizer") • [Map](/wiki/Map "Map") • [Productivity Display](/wiki/Productivity_Display "Productivity Display") • Head lift • [Blueprints](/wiki/Blueprints "Blueprints") • [Fuels](/wiki/Category:Fuels "Category:Fuels") • [FICSIT Productive Packer Deluxe](/wiki/FICSIT_Productive_Packer_Deluxe "FICSIT Productive Packer Deluxe")  
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
