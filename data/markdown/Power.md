# Power

Most [buildings](/wiki/Buildings "Buildings") require electricity, or **power** , to function. Power is produced in power generators (see below), stored or discharged from [Power Storages](/wiki/Power_Storage "Power Storage"), and consumed by buildings. Power is transferred via [Power Lines](/wiki/Power_Line "Power Line") connecting [Power Poles](/wiki/Power_Poles "Power Poles"), [Wall Outlets](/wiki/Wall_Outlets "Wall Outlets") and [Power Towers](/wiki/Power_Tower "Power Tower") or [Train Stations](/wiki/Train_Station "Train Station") and [Railways](/wiki/Railway "Railway"). 

Power is measured in megawatts (MW). Stored energy in Power Storages is measured in megawatthours (MWh), whereas the energy density of fuels in megajoules (MJ) (see [units](/wiki/Units "Units")). 

## Contents

  * 1 Overview
  * 2 Power grid
  * 3 Power trip
  * 4 Power graph
  * 5 Power consumers
  * 6 Power generators
    * 6.1 Type of generators
  * 7 Power Storage
  * 8 Clock speed
    * 8.1 Power consumer
    * 8.2 Power generator
  * 9 Production amplifier
  * 10 Energy
  * 11 Achievements
  * 12 Trivia
  * 13 See also
  * 14 History
  * 15 References



## Overview

Buildings that consume (or supply) power will only function when connected to a Power grid (see below section) where either the total supply from all power generators is sufficient to meet the total demand from all power consumers or there is still energy in [Power Storages](/wiki/Power_Storage "Power Storage"). If power demand exceeds supply and all Power Storages are empty, the circuit breaker trips, halting all buildings on that grid until the problem is corrected followed by a breaker reset. 

## Power grid

A power grid is a network consisting of power-generating and power-consuming buildings connected through Power Lines, Power Poles, Power Towers, Train Stations, and Railways. A graph of total power capacity, power production, and power consumption can be viewed by interacting [`E`](/wiki/Controls "Controls") with any Power Pole, generator, Train Station, or Power Switch on that grid. 

Power Grids can be split using a [Power Switch](/wiki/Power_Switch "Power Switch"). Excess energy can be stored in [Power Storages](/wiki/Power_Storage "Power Storage"), to be used in cases of consumption exceeding production. 

## Power trip

[](/wiki/File:Power_trip.wav "Enlarge")

Sound heard when a power trip occurs.

When power consumption exceeds production and there is no energy in Power Storages to use, the power grid will trip. All connected power generators and power consumers in that grid will stop working. The sound effect of the trip can be heard from any part of the map, regardless of the distance between the tripped devices and the [Pioneer](/wiki/Pioneer "Pioneer"). 

However, if there are no connected power generators whatsoever (such as by disconnecting all power generators at once using a switch), the buildings will instead simply switch off no power trip will occur. In this case, the buildings will resume function as soon as an adequate power supply is reconnected, without the need to reset the fuse. 

Unlike other games, buildings won't run slower when the power generation is lacking. The power grid will simply trip and _**all**_ buildings connected to that grid will stop functioning. 

The pioneer can reset the circuit breaker by interacting [`E`](/wiki/Controls "Controls") at any of the connected power generators or Power Poles. In the UI, pull down the lever (refer to the image below) to restore the power. Before resetting it is advised to either attach more power generators to the grid or temporarily remove power cables to some of the areas of the factory. Otherwise, the power grid will simply overload again as soon as it is reactivated. 

❗**IMPORTANT:** The [Hoverpack](/wiki/Hoverpack "Hoverpack") draw 100 MW by default, but that power consumption does not appear on the power chart, which can lead to confusing situations when trying to restart electric grids, especially small ones. If a Hoverpack is being used, it is **strongly recommended** that the Hoverpack be unequipped prior to resetting circuit breaker. 

A power trip may also allow [hostile creatures to respawn](/wiki/Combat#Creature_respawn_mechanism "Combat"). 

  * [](/wiki/File:Power_graph.jpg "A power graph, with power consumption below power capacity.")

A power graph, with power consumption below power capacity.

  * [](/wiki/File:Power_trip.jpg "During a power trip, interact E with any Power Pole or generators on the grid and pull down the lever at the left to reset the breaker.")

During a power trip, interact [`E`](/wiki/Controls "Controls") with any Power Pole or generators on the grid and pull down the lever at the left to reset the breaker.




## Power graph

[](/wiki/File:Power_pole_-_graph.png)

[](/wiki/File:Power_pole_-_graph.png "Enlarge")

A power pole graph, with power consumption overlapping capacity.

The Power Graph displays information about power production and consumption in the current power grid, as well as the sum of energy stored in all [Power Storages](/wiki/Power_Storage "Power Storage") on the grid. Power Storages do not affect any of the lines in the graph, instead, related information is shown in a menu to the right of the graph.  
■ Capacity: The sum of the maximum power output if all existing generators on the grid were to operate at the same time.  
■ Production: The current power output of all power generators on the grid. Only differs from "capacity" if there are [Biomass Burners](/wiki/Biomass_Burner "Biomass Burner") on the grid, as they are the only building to scale to demand.  
■ Consumption: The current power demand by all buildings on the grid. If consumption exceeds production, energy will be drawn from Power Storages if available, else a power trip occurs.  
■ Maximum Consumption: The sum of the maximum power demand if all buildings on the grid were to operate at the same time.  
■ Power Boost: The current amount of boosted power from using an [Alien Power Augmenter](/wiki/Alien_Power_Augmenter "Alien Power Augmenter") that is included in the values for both Capacity and Production. 

  * [](/wiki/File:Alien_Power_Augmenter_Power_Pole_UI.png "Example of Power Pole Graph showing Boost from the use of an Alien Power Augmenter.")

Example of Power Pole Graph showing Boost from the use of an Alien Power Augmenter.




## Power consumers

  * Most [buildings](/wiki/Building "Building") require power to function. They are called power consumers. See individual building pages for their power requirement, measured in MW.
  * Each building in standby mode (whether the pioneer flipped the standby switch, or if the building is not functioning due to a logistic issue) consumes 0.1 MW. 
    * Underclocking early-game buildings to very low clock speeds allows them to consume less power while operating than when idle.
  * [Indicator Lights](/wiki/Indicator_Light "Indicator Light") show whether a building is operating and consuming power or not.



## Power generators

Power generators convert [fuels](/wiki/Fuels "Fuels") into power. Each type of generator building has its own set of fuel item types and power output. 

All power generators with the exception of the Biomass Burner always operate at full capacity. Biomass Burners instead scale to power consumption and burn slower at lesser demand. For example, if grid capacity is 105 MW, provided by one Coal Generator producing 75 MW and one Biomass Burner producing 30 MW, and power consumption is 95 MW, the entire capacity of the Coal Generator will be used first followed by two thirds of the Biomass Burner's capacity, meaning fuel will be burned at two thirds of the rate it would at maximum demand. This also renders Biomass Burners unable to charge Power Storages. 

### Type of generators

There are six total types of power generators: 

  * [](/wiki/Biomass_Burner "Biomass Burner") [Biomass Burner](/wiki/Biomass_Burner "Biomass Burner")
  * [](/wiki/Coal-Powered_Generator "Coal-Powered Generator") [Coal-Powered Generator](/wiki/Coal-Powered_Generator "Coal-Powered Generator")
  * [](/wiki/Fuel_Generator "Fuel Generator") [Fuel-Powered Generator](/wiki/Fuel_Generator "Fuel Generator")
  * [](/wiki/Geothermal_Generator "Geothermal Generator") [Geothermal Generator](/wiki/Geothermal_Generator "Geothermal Generator")
  * [](/wiki/Nuclear_Power_Plant "Nuclear Power Plant") [Nuclear Power Plant](/wiki/Nuclear_Power_Plant "Nuclear Power Plant")
  * [](/wiki/Alien_Power_Augmenter "Alien Power Augmenter") [Alien Power Augmenter](/wiki/Alien_Power_Augmenter "Alien Power Augmenter")



## Power Storage

See main article on [Power Storage.](/wiki/Power_Storage "Power Storage")

[](/wiki/File:Power_Storage.png)

[](/wiki/File:Power_Storage.png "Enlarge")

Power Storage. 

The **[Power Storage](/wiki/Power_Storage "Power Storage")** is a mid-game [building](/wiki/Building "Building") available in [Tier 4](/wiki/Milestones "Milestones") used for buffering electrical energy. Each can store up to 100 MWh, or 100 MW for 1 hour. As it allows 2 power connections, multiple Power Storages can be daisy-chained to store large amounts of energy. 

When connected to a power grid that is supplied by generators other than [Biomass Burners](/wiki/Biomass_Burner "Biomass Burner"), it will charge using the excess generated power, up to a rate of 100 MW each. Therefore, it will take at least an hour in real-time to fully charge an empty Power Storage, or longer if the spare power is less than to satisfy all Power Storages on the grid (Power Storages that are not fully charged will split the spare power, reducing their charge rate to the available spare power divided by the number of partially charged Power Storages). Charging Power Storage does not add to the grid power consumption or max consumption figures, nor does it diminish capacity since it will slow or stop charging if there are other demands for the available power. 

As long as there is stored charge in the Power Storage and there is a power shortage (consumption exceeding production), all Power Storages will discharge to satisfy the difference, powering up instantly. There is no limit on the discharge rate; it will exactly match the power deficiency. This allows the pioneer to quickly react to restore the power situation, whether to increase power production or to install a [Power Switch](/wiki/Power_Switch "Power Switch"). Once all the stored energy has been discharged and the power is still insufficient, the power grid will trip. 

## Clock speed

_Main article:_[Clock speed](/wiki/Clock_speed "Clock speed")

Overclocking is unlocked at the [MAM](/wiki/MAM "MAM"). The clock speed of buildings can be adjusted by interacting [`E`](/wiki/Controls "Controls") with it and adjusting the slider. [](/wiki/Power_Shard "Power Shard") [Power Shards](/wiki/Power_Shard "Power Shard") are required to increase the clock speed beyond 100%, up to 250% maximum. 

Underclocking can be done freely once overclocking has been researched and costs no Power Shards. 

### Power consumer

  * Power consumers work at the rate of user-defined clock speed. For example, a [Constructor](/wiki/Constructor "Constructor") works twice as fast when its clock speed is set to 200%.
  * An active overclocked building is always less power efficient. However, an idle overclocked building will still only consume the standard 0.1MW of idle power. 
    * In the above example, its power consumption will be greater than 2x the usual power consumption. This also means a building at 200% consumes more power than 2 equal buildings each operating at 100%.
  * On the other hand, underclocking a building saves power. 
    * Two constructors each working at 50% use less power compared to 1 Constructor working at 100%.
    * However, the footprint of the factory will be larger.
    * Power consumers that are underclocked to have active power consumption below the idle rate of 0.1MW will still use 0.1MW while idle.[1]



### Power generator

  * Power generators overclock differently from power consumers. Their fuel consumption rate is always proportional to the power production of the building. Hence, overclocking a power generator will neither increase nor decrease fuel efficiency. 
    * This means the generator will burn the fuel faster or slower, but not produce more energy from the same amount of fuel.
    * Production and consumption rate scale directly with Clock Speed, unlike power consumers. See the [Clock Speed](/wiki/Clock_Speed "Clock Speed") article for details.



## Production amplifier

_Main article:_[Production amplifier](/wiki/Production_amplifier "Production amplifier")

Select factory buildings can have their production amplified using [](/wiki/Somersloop "Somersloop") [Somersloops](/wiki/Somersloop "Somersloop"). This increases their power consumption by up to 4×, multiplied with the power usage affected by clock speed. 

## Energy

Energy is a derived unit of Power. When Power is being consumed (or produced) over some time, the product of Power and Time is called Energy. Where power fluctuates over time, the average power can be used instead. 

The base unit of energy is the Joule (J). The exact unit used depends on the unit of Power and time measured. For example, 

  * `4 MW * 4 seconds = 16 MJ` the energy consumption of producing an [Iron Rod](/wiki/Iron_Rod "Iron Rod") in a [Constructor](/wiki/Constructor "Constructor"), with normal [Clock speed](/wiki/Clock_speed "Clock speed") and default recipe
  * `30 MW * 0.5 seconds = 15 MJ` the energy produced by 1 [Leaves](/wiki/Leaves "Leaves") in a [Biomass Burner](/wiki/Biomass_Burner "Biomass Burner")
  * `2.5 GW * 10 minutes = 2.5 GW * 600 seconds = 1,500 GJ = 1.5 TJ` the energy produced by a [Plutonium Fuel Rod](/wiki/Plutonium_Fuel_Rod "Plutonium Fuel Rod") in a [Nuclear Power Plant](/wiki/Nuclear_Power_Plant "Nuclear Power Plant")
  * `100 MW * 1 hour = 100 MWh = 360 GJ` the energy storage capacity of a single [Power Storage](/wiki/Power_Storage "Power Storage")



Notes: 

  * `1 hour = 60 minutes = 3600 seconds`
  * `1 TW = 1000 GW = 1,000,000 MW` Similarly, `1 TJ = 1000 GJ = 1,000,000 MJ`



Power Storages use MWh instead of MJ. 1 MWh equals 3 600 MJ. 

Energy can be used to compare the burning time of [Fuels](/wiki/Fuels "Fuels") in [vehicles](/wiki/Vehicle "Vehicle") or in generators, or comparing the energy efficiency between different [Alternate recipes](/wiki/Alternate_recipes "Alternate recipes") of an item. 

  * Stack energy is simply a product of energy and the number of items in its full [stack](/wiki/Stack "Stack").



## Achievements

[](/wiki/Achievements "Achievements")**[New fear unlocked](/wiki/Achievements#New_fear_unlocked "Achievements")** •  _"Fix blown fuse."_

## Trivia

  * An [Easter egg](/wiki/Easter_egg "Easter egg") happens when the power graph in any UI is clicked 6 times, glitching and showing a warning about abusing FICSIT property.
  * A prototype of Satisfactory featured wind power, but it was removed.[2]


  * [](/wiki/File:Power_graph_glitched.png "This image will be displayed when the Power graph is clicked 6 times.")

This image will be displayed when the Power graph is clicked 6 times.

  * [](/wiki/File:Power_graph_warning.png "Shortly after that, this warning message will appear until you re-open the Power graph.")

Shortly after that, this warning message will appear until you re-open the Power graph.




## See also

  * [Fuels](/wiki/Fuels "Fuels")
  * [Clock speed](/wiki/Clock_speed "Clock speed")
  * [Production amplifier](/wiki/Production_amplifier "Production amplifier")
  * [](/wiki/Power_Line "Power Line") [Power Line](/wiki/Power_Line "Power Line")
  * [](/wiki/Power_Pole "Power Pole") [Power Pole](/wiki/Power_Pole "Power Pole")



## History

  * [Patch 1.0.1.0](/wiki/Patch_1.0.1.0 "Patch 1.0.1.0"): [Copy pasting settings](/wiki/Controls "Controls"), using [`Right Ctrl`](/wiki/Controls "Controls")+[`C`](/wiki/Controls "Controls") and [`Right Ctrl`](/wiki/Controls "Controls")+[`V`](/wiki/Controls "Controls"), now works on Generators and Extractors ([Water](/wiki/Water_Extractor "Water Extractor"),[Oil](/wiki/Oil_Extractor "Oil Extractor"),[Resource Well](/wiki/Resource_Well_Pressurizer "Resource Well Pressurizer"))
  * [Patch 1.0.0.5](/wiki/Patch_1.0.0.5 "Patch 1.0.0.5"): Potential fix for a crash in the Circuit Subsystem
  * [Patch 0.8.3.3](/wiki/Patch_0.8.3.3 "Patch 0.8.3.3"): Fixed the shadow on the Reset Fuse lever being offset
  * [Patch 2018-10-11](/wiki/Patch_2018-10-11 "Patch 2018-10-11"): Made available.



## References

  1. ↑ [Satisfactory Wiki - August 1st, 2021 - Underlocked-below-idle-power-while-active.webp](/wiki/File:Underlocked-below-idle-power-while-active.webp "File:Underlocked-below-idle-power-while-active.webp")
  2. ↑ [Instagram - February 26th, 2021 AMA - Can you bring wind turbines to Satisfactory?](/wiki/File:February_26th,_2021_Instagram_AMA_-_Can_you_bring_solar_power_and_wind_turbines_and_water_power_to_Satisfactory%3F.mp4 "File:February 26th, 2021 Instagram AMA - Can you bring solar power and wind turbines and water power to Satisfactory?.mp4")



  * [v](/wiki/Template:PioneerNav "Template:PioneerNav")
  * [e](https://satisfactory.wiki.gg/wiki/Template:PioneerNav?action=edit)
  * [h](https://satisfactory.wiki.gg/wiki/Template:PioneerNav?action=history)

[Satisfactory](/wiki/Satisfactory "Satisfactory") game mechanics  
---  
Player abilities| [Codex](/wiki/Codex "Codex") • [Resource Scanner](/wiki/Resource_Scanner "Resource Scanner") • [Build Gun](/wiki/Build_Gun "Build Gun") • [Inventory](/wiki/Inventory "Inventory") • [Health](/wiki/Health "Health") • [Combat](/wiki/Combat "Combat") • [Movement](/wiki/Movement "Movement") • [Flashlight](/wiki/Flashlight "Flashlight") • [HUD](/wiki/HUD "HUD") • [Crate](/wiki/Crate "Crate") • [To-Do List](/wiki/To-Do_List "To-Do List")  
Unlockable abilities| [Recipes](/wiki/Recipes "Recipes") • Power • [Overclocking/Underclocking](/wiki/Clock_speed "Clock speed") • [Production amplifier](/wiki/Production_amplifier "Production amplifier") • [Customizer](/wiki/Customizer "Customizer") • [Map](/wiki/Map "Map") • [Productivity Display](/wiki/Productivity_Display "Productivity Display") • [Head lift](/wiki/Head_lift "Head lift") • [Blueprints](/wiki/Blueprints "Blueprints") • [Fuels](/wiki/Category:Fuels "Category:Fuels") • [FICSIT Productive Packer Deluxe](/wiki/FICSIT_Productive_Packer_Deluxe "FICSIT Productive Packer Deluxe")  
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
