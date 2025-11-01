# Units

| _This article is about units of measurement. For the vehicle nicknamed 'The Unit', see[Truck](/wiki/Truck "Truck")._  
---|---  
  
This page covers various measurement **units** and derived units used in _Satisfactory_. 

All units should follow [SI unit styling guidelines](https://physics.nist.gov/cuu/Units/checklist.html). More details about styling can be found in the [style guide](/wiki/Satisfactory_Wiki:Style_guide "Satisfactory Wiki:Style guide"). 

## Contents

  * 1 Base units
    * 1.1 Time
    * 1.2 Item throughput
    * 1.3 Distance
    * 1.4 Fluid volume
    * 1.5 Fluid flow rate
    * 1.6 Head lift
    * 1.7 Speed
    * 1.8 Power
    * 1.9 Fuel energy
    * 1.10 Power Storage charge
  * 2 Derived units
    * 2.1 Belt speed
    * 2.2 Crafting cycle energy
    * 2.3 Power efficiency



## Base units

### Time

The base unit of time is a second, or `s`. 60 seconds is one minute, 60 minutes is one hour, obviously. 

The duration of one day in _Satisfactory_ is 50 minutes, consisting of a 45-min daytime and 5-min nighttime. 

### Item throughput

Item transportation, production and consumption rate is measured in `items per minute` (items/min or ipm), also `parts per minute` (ppm). By default, per minute values are displayed in-game, except for fuel burn time in generators, where the burn duration of one item in seconds is shown instead. 

### Distance

The game solely uses meters, `m`, to describe distance, with fractions of it being used in favor of decimeters, centimeters, etc. However, internally, centimeters are used (as the default Unreal Engine distance unit). 

### Fluid volume

The volume of [fluids](/wiki/Fluids "Fluids") is measured in cubic meters, `m3`. Internally, liters are used instead, and to the player, 0.01 m3 is the smallest amount of fluid displayed (= 10 liters). 

### Fluid flow rate

The flow rate of [fluids](/wiki/Fluids "Fluids") is measured in cubic meters per minute, `m3/min`. Some buildings even indicate a direction, with positive values showing inflow and negative values for drainage. 

### Head lift

[Head lift](/wiki/Head_lift "Head lift") is measured in meters. It indicates how high a fluid can be pushed up without its flow rate being reduced below maximum, until stopping entirely. 

### Speed

[Vehicle](/wiki/Vehicle "Vehicle") speed is measured in kilometers per hour, `km/h` or kph. This can be converted to meters/sec by dividing it by 3.6, which are used internally. 

### Power

[Power](/wiki/Power "Power"), or rate of energy flow is measured in Megawatts, or `MW`, which is equal to 1,000,000 Watts. This unit is used to measure either [building](/wiki/Building "Building")'s power production or consumption, as well as [equipment](/wiki/Equipment "Equipment") or [vehicle](/wiki/Vehicle "Vehicle")'s [fuel](/wiki/Fuel "Fuel") burning rate. 

Larger amounts of power can be displayed with other prefixes, such as 1,000 MW = 1 GW, and 1 TW = 1,000 GW = 1,000,000 MW. The smallest amount of power both displayed and used in-game is 0.1 MW, which is how much all powered machines consume while their [Indicator Light](/wiki/Indicator_Light "Indicator Light") is red or yellow. 

### Fuel energy

Every type of [fuel](/wiki/Fuels "Fuels") has a `MJ` (Megajoule) value which determines how long it is burned in a generator or a vehicle. For fluid fuels, the MJ value is per one cubic meter. 1 MJ corresponds to 1 MW over 1 second. Fuel energy values are shown in tooltips. 

For example, one piece of [Coal](/wiki/Coal "Coal") has 300 MJ, and one [Coal Generator](/wiki/Coal_Generator "Coal Generator") provides 75 MW at 100% [clock speed](/wiki/Clock_speed "Clock speed"). Thus, it takes 300/75 = 4 seconds to burn one piece of Coal, which results in 60/4 = 15 pieces burned per minute. 

### Power Storage charge

The charge of [Power Storages](/wiki/Power_Storage "Power Storage") is listed in Megawatthours, or `MWh`. 1 MWh corresponds to 1 MW over 1 hour, which equals to 2 MW over 0.5 h, 10 MW over 0.1 h, etc. 1 MWh is equal to 3600 MJ. One Power Storage can store up to 100 MWh of charge. 

## Derived units

### Belt speed

Not to be confused with belt throughput, or item flow rate (see above). 

To measure belt speed, build a 48-meters long straight belt (six [Foundations](/wiki/Foundations "Foundations")) and measure the time taken to transport the player from one end to the other. Divide the distance (48 m) by the time and you got the speed in meters per second, `m/s`. You can convert it into km/h by multiplying it by 3.6. 

Higher accuracy measurement can be achieved with longer belts, by chaining multiple belts in a straight line. 

### Crafting cycle energy

Similar to fuel energy, the `MJ` required to complete one crafting cycle or to produce one item of that crafting cycle can be calculated using `building power consumption * crafting cycle duration`, e.g. a building consuming 30 MW and completing one production cycle every five seconds consumes 150 MJ per crafting cycle, which equals to half of a piece of Coal being burned in a Coal Generator. If that crafting cycle yields 1 item, it cost 150 MJ, if two items 75 MJ, etc. 

Take note as idling buildings constantly consume 0.1 MW while not completing any crafting cycles. 

### Power efficiency

Power efficiency is measured in percentage `%`. It is calculated by dividing the net power by gross power. 

The gross power is the total amount of power produced by a power generating setup. Net power is gross power minus the internal power consumption used to run the setup, which includes [Miners](/wiki/Miner "Miner"), [Water Extractors](/wiki/Water_Extractor "Water Extractor"), [Pipeline Pumps](/wiki/Pipeline_Pump "Pipeline Pump"), etc. 

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
Technical| [Console release](/wiki/Console_release "Console release") • [Debug console](/wiki/Debug_console "Debug console") • [Launch arguments](/wiki/Launch_arguments "Launch arguments") • [Save files](/wiki/Save_files "Save files") • [System requirements](/wiki/System_requirements "System requirements") • Units • [Unreal Engine](/wiki/Unreal_Engine "Unreal Engine")  
Guides and tutorials| | Basics| [Walkthrough/How to play](/wiki/Tutorial:How_to_play "Tutorial:How to play") • [New Pioneer Guide](/wiki/Tutorial:New_Pioneer_Guide "Tutorial:New Pioneer Guide") • [Production line basics](/wiki/Tutorial:Production_line "Tutorial:Production line") • [Advanced production line tips](/wiki/Tutorial:Production_line_design_tips "Tutorial:Production line design tips") • [Picking an alternate recipe](/wiki/Tutorial:Picking_an_alternate_recipe "Tutorial:Picking an alternate recipe") • [Independency](/wiki/Tutorial:Independency "Tutorial:Independency") • [Aluminum Ingot production](/wiki/Tutorial:Setting_up_Aluminum_Ingot_production "Tutorial:Setting up Aluminum Ingot production")  
---|---  
Logistics| [Manifold](/wiki/Manifold "Manifold") • [Balancer](/wiki/Balancer "Balancer") • [Pipeline manifold](/wiki/Pipeline_manifold "Pipeline manifold") • [Prime Splitter Arrays](/wiki/Tutorial:Prime_splitter_arrays "Tutorial:Prime splitter arrays") • [Trains](/wiki/Tutorial:Trains "Tutorial:Trains") • [Train throughput](/wiki/Tutorial:Train_throughput "Tutorial:Train throughput")  
Dedicated servers| [Dedicated servers](/wiki/Dedicated_servers "Dedicated servers") • [Running as a Service](/wiki/Dedicated_servers/Running_as_a_Service "Dedicated servers/Running as a Service") • [Configuration files](/wiki/Dedicated_servers/Configuration_files "Dedicated servers/Configuration files") • [Automatic updates](/wiki/Dedicated_servers/Automatic_updates "Dedicated servers/Automatic updates") • [HTTPS API](/wiki/Dedicated_servers/HTTPS_API "Dedicated servers/HTTPS API") • [Lightweight Query API](/wiki/Dedicated_servers/Lightweight_Query_API "Dedicated servers/Lightweight Query API")  
Other| [Hypertube cannon](/wiki/Tutorial:Hypertube_cannon "Tutorial:Hypertube cannon") • [Hypertube brake](/wiki/Tutorial:Hypertube_brake "Tutorial:Hypertube brake") • [Steam Deck & Controller setup](/wiki/Tutorial:Controller_setup "Tutorial:Controller setup") • [Extracting UI icons](/wiki/Tutorial:Extracting_UI_icons "Tutorial:Extracting UI icons")
  *[v]: View this template
  *[e]: Edit this template
  *[h]: History of this template
  *[his]: his trivia section
