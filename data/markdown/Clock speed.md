# Clock speed

## Clock speed

[ ](/wiki/File:Clock_speed.png "Clock speed.png")

### Unlocked by

[Power Slugs Research](/wiki/Power_Slugs_Research "Power Slugs Research") \- Overclock Production

Production and power [buildings](/wiki/Buildings "Buildings"), such as [Miners](/wiki/Miner "Miner"), [Constructors](/wiki/Constructor "Constructor") or [Biomass Burners](/wiki/Biomass_Burner "Biomass Burner"), can have their **clock speed** set to any percentage between 1% and 250%, with a precision of up to 4 decimal places. For production buildings, this allows them to operate slower or faster at the cost of greatly reduced or increased power usage. For power buildings, the maximum power output and accompanying fuel consumption can be increased in tandem, granting more utility from a single building. Overclocking and underclocking both have utility in optimizing a factory, helping to synchronize production, increasing energy efficiency and smoothing out the peaks in power consumption. 

## Contents

  * 1 Terminology
  * 2 Obtaining
  * 3 Usage
    * 3.1 Purpose
    * 3.2 Configuration
      * 3.2.1 Example usage
    * 3.3 Precision
  * 4 See also
  * 5 Gallery
  * 6 History
  * 7 References



## Terminology

**Clock speed** is the speed of operation of a building. 250% clock speed means the building will operate 2.5x as fast. 

**Overclocking** refers to setting the clock speed above 100%, and inversely, **underclocking** refers to setting the clock speed below 100%. Underclocking does not require any [](/wiki/Power_Shard "Power Shard") [Power Shards](/wiki/Power_Shard "Power Shard"). 

## Obtaining

The ability to change clock speeds can be unlocked in the [](/wiki/MAM "MAM") [MAM](/wiki/MAM "MAM"). Confusingly, the research is named "Overclock Production", but unlocks underclocking as well. 

**[](/wiki/Clock_speed "Clock speed")Clock speed** is unlocked via the **[Power Slugs Research chain](/wiki/Power_Slugs_Research "Power Slugs Research")** in the [](/wiki/MAM "MAM") [MAM](/wiki/MAM "MAM") using:  
[](/wiki/Power_Shard "Power Shard")1| [](/wiki/Iron_Plate "Iron Plate")50| [](/wiki/Wire "Wire")50  
---|---|---  
  
[](/wiki/Power_Shard "Power Shard") [Power Shards](/wiki/Power_Shard "Power Shard") required to increase clock speeds above 100% can be crafted from [](/wiki/Power_Slug "Power Slug") [Power Slugs](/wiki/Power_Slug "Power Slug"), which can be found in set locations across the [world](/wiki/World "World"). In [Tier 9](/wiki/Tier_9 "Tier 9"), Power Shards can be automated by producing them synthetically. 

## Usage

### Purpose

There are multiple reasons for changing clock speeds, especially matching production and consumption rates of machines to make a factory line operate at maximum efficiency, saving space by overclocking, or saving power by underclocking. 

For matching production and consumption rates, both overclocking and underclocking are viable. It is up to you to decide whether to overclock using [](/wiki/Power_Shard "Power Shard") [Power Shards](/wiki/Power_Shard "Power Shard"), saving a little space and using a little extra power, or vice versa by underclocking, which does not require [](/wiki/Power_Shard "Power Shard") [Power Shards](/wiki/Power_Shard "Power Shard"). 

Clock speed affects production buildings/resource extractors and power generators differently, see below. 

### Configuration

Clock speed can only be configured in production buildings with configurable recipes, resource extractors and power generators. Other power consumers, such as [](/wiki/Hypertube_Entrance "Hypertube Entrance") [Hypertube Entrances](/wiki/Hypertube_Entrance "Hypertube Entrance"), [](/wiki/Pipeline_Pump "Pipeline Pump") [Pipeline Pumps](/wiki/Pipeline_Pump "Pipeline Pump") or [](/wiki/Train_Station "Train Station") [Train Stations](/wiki/Train_Station "Train Station"), cannot be overclocked. 

Clock speed can be set using a menu within each building's UI, accessed by interacting [`E`](/wiki/Controls "Controls") with it.[](/wiki/Power_Shard "Power Shard") [Power Shards](/wiki/Power_Shard "Power Shard") can be inserted into this menu, increasing the maximum allowed clock speed by 50% up to 3 times. There are multiple ways to set a clock speed in this menu: 

  * Dragging the slider, changing values in 1% increments.
  * Entering a percentage or target production rate directly.
  * Entering a formula, similar to the [in-game calculator](/wiki/Controls#In-game_calculator "Controls") accessed using quick search [`N`](/wiki/Controls "Controls"), which will be evaluated left-to-right.



Additionally, recipe and clock speed configuration can be copied [`Ctrl`](/wiki/Controls "Controls")+[`C`](/wiki/Controls "Controls") and pasted [`Ctrl`](/wiki/Controls "Controls")+[`V`](/wiki/Controls "Controls") between buildings of the same type. If [](/wiki/Power_Shard "Power Shard") [Power Shards](/wiki/Power_Shard "Power Shard") are required, they will be automatically inserted into the building if there are enough in the [inventory](/wiki/Inventory "Inventory"). 

Buildings underclocked to have active power consumption below the idle rate of 0.1 MW will still use 0.1 MW while idle.[1]

#### Example usage

The first 4 images are "paired" to show the formula used and the result, while the last is combined on one image: 

  * [](/wiki/File:Clock_Speed_Formula_Example_1a.png "Example of using formulas in clock speed to calculate the exact input value desired.")

Example of using formulas in clock speed to calculate the exact input value desired.

  * [](/wiki/File:Clock_Speed_Formula_Example_1b.png "Example of calculated result of formula showing 46 Heavy Oil Residue input per minute.")

Example of calculated result of formula showing 46 Heavy Oil Residue input per minute.

  * [](/wiki/File:Clock_Speed_Formula_Example_2a.png "Example of using formulas in clock speed when overclocking. This would set the input per minute to 103.155.")

Example of using formulas in clock speed when overclocking. This would set the input per minute to 103.155.

  * [](/wiki/File:Clock_Speed_Formula_Example_2b.png "Example of calculated result of formula showing input per minute at 103.155.")

Example of calculated result of formula showing input per minute at 103.155.

  * [](/wiki/File:Target_Production_Rate_Formula_Example.png "Example of using formulas in target production rate to calculate the desired value which also updates clock speed.")

Example of using formulas in target production rate to calculate the desired value which also updates clock speed.




### Precision

The result configuration is always stored as a percentage with four decimal spaces of precision. Internally, the exact values calculated from the configured clock speed are used. However, the user interface often rounds or truncates values, thus listing inaccurate results. 

For example, a [](/wiki/Constructor "Constructor") [Constructor](/wiki/Constructor "Constructor") producing 15 [](/wiki/Concrete "Concrete") [Concrete](/wiki/Concrete "Concrete")/min can never be set to produce precisely 5/min. The closest clock speed of 33.3333% will produce 15 × 0.333333 = 4.999995/min, despite the UI rounding it to exactly 5/min. 

This level of inaccuracy is negligible for most players; one way to reduce the occurrence of infinitely repeating decimals is to use a so-called **45-81 rule:** If a recipe's production rate is a multiple or fraction of 45/min or 81/min, its clock speed likely won't have repeating decimals. 81 applies to most Oil recipes, 45 to most other recipes. This does not apply to all recipes. 

For example, instead of producing 100 [](/wiki/Plastic "Plastic") [Plastic](/wiki/Plastic "Plastic")/min using the Diluted + Recycled loop, 81 + 20.25 = 101.25/min would be produced. 

## See also

  * [Advanced clock speed](/wiki/Tutorial:Advanced_clock_speed "Tutorial:Advanced clock speed")
  * [Production amplifier](/wiki/Production_amplifier "Production amplifier")



## Gallery

  * [](/wiki/File:Underclocking_tutorial.png "An underclocked Constructor. A value can be entered into the percentage, items per minute or adjusted using the slider.")

An underclocked [Constructor](/wiki/Constructor "Constructor"). A value can be entered into the percentage, items per minute or adjusted using the slider.

  * [](/wiki/File:Overclocking_tutorial.png "An overclocked Miner. Power Shard\(s\) is required for overclocking beyond 100%.")

An overclocked [Miner](/wiki/Miner "Miner"). [Power Shard](/wiki/Power_Shard "Power Shard")(s) is required for overclocking beyond 100%.




## History

[](/wiki/File:Icon-boilerplate.png) | The history section is incomplete in this article. Please help [expanding it](https://satisfactory.wiki.gg/wiki/Clock_speed?action=edit) if you can. Information can be gathered from [patch notes](/wiki/Category:Patch_notes "Category:Patch notes").   
---|---  
  
  * [Patch 0.8.2.0](/wiki/Patch_0.8.2.0 "Patch 0.8.2.0"): Fixed issue where keyboard input was lost after manually entering text when Overclocking
  * [Patch 0.7.0.0](/wiki/Patch_0.7.0.0 "Patch 0.7.0.0")
    * Reduced the energy cost of Overclocking production buildings (including Extractors) to a lower exponent 
      * Changed production building and extractor exponent from 1.6 to 1.321928
    * Made overclocking of power generators match the operating rate with the clock speed 
      * The basic mechanic of Overclocking remains largely unchanged, but the exponential power cost change has been lowered. This means that Overclocking is less expensive than it was before, and Underclocking is not quite as cheap.
      * Generators are the only exception to this rule: They Over- and Underclock completely linear.
  * [Patch 0.6.1.1](/wiki/Patch_0.6.1.1 "Patch 0.6.1.1")
    * Overclocking now has a visible text box so you can enter percentages or numbers manually
    * Manufacturing buildings should now preview the overclocked per minute stat on each input and output before the new overclock is applied on the next cycle
  * [Patch 0.4.0.4](/wiki/Patch_0.4.0.4 "Patch 0.4.0.4"): Fixed overclocking not showing the correct value when pasting settings in some situations
  * [Patch 0.4.0.3](/wiki/Patch_0.4.0.3 "Patch 0.4.0.3"): Changed the number of decimals in overclocking from 1 to 4
  * [Patch 0.4.0.0](/wiki/Patch_0.4.0.0 "Patch 0.4.0.0"): It is now possible to set decimal percentages as clock speed, the game no longer rounds it to the nearest whole percentage



## References

  1. ↑ [Satisfactory Wiki - August 1st, 2021 - Underlocked-below-idle-power-while-active.webp](/wiki/File:Underlocked-below-idle-power-while-active.webp "File:Underlocked-below-idle-power-while-active.webp")



  * [v](/wiki/Template:PioneerNav "Template:PioneerNav")
  * [e](https://satisfactory.wiki.gg/wiki/Template:PioneerNav?action=edit)
  * [h](https://satisfactory.wiki.gg/wiki/Template:PioneerNav?action=history)

[Satisfactory](/wiki/Satisfactory "Satisfactory") game mechanics  
---  
Player abilities| [Codex](/wiki/Codex "Codex") • [Resource Scanner](/wiki/Resource_Scanner "Resource Scanner") • [Build Gun](/wiki/Build_Gun "Build Gun") • [Inventory](/wiki/Inventory "Inventory") • [Health](/wiki/Health "Health") • [Combat](/wiki/Combat "Combat") • [Movement](/wiki/Movement "Movement") • [Flashlight](/wiki/Flashlight "Flashlight") • [HUD](/wiki/HUD "HUD") • [Crate](/wiki/Crate "Crate") • [To-Do List](/wiki/To-Do_List "To-Do List")  
Unlockable abilities| [Recipes](/wiki/Recipes "Recipes") • [Power](/wiki/Power "Power") • Overclocking/Underclocking • [Production amplifier](/wiki/Production_amplifier "Production amplifier") • [Customizer](/wiki/Customizer "Customizer") • [Map](/wiki/Map "Map") • [Productivity Display](/wiki/Productivity_Display "Productivity Display") • [Head lift](/wiki/Head_lift "Head lift") • [Blueprints](/wiki/Blueprints "Blueprints") • [Fuels](/wiki/Category:Fuels "Category:Fuels") • [FICSIT Productive Packer Deluxe](/wiki/FICSIT_Productive_Packer_Deluxe "FICSIT Productive Packer Deluxe")  
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
