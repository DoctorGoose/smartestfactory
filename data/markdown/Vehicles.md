# Vehicles

There are 7 types of **vehicles** that [pioneers](/wiki/Pioneer "Pioneer") can use for either personal travel, transporting items or both: [Tractors](/wiki/Tractor "Tractor"), [Trucks](/wiki/Truck "Truck"), [Explorers](/wiki/Explorer "Explorer"), [Cyber Wagons](/wiki/Cyber_Wagon "Cyber Wagon"), [Factory Carts](/wiki/Factory_Cart "Factory Cart"), [Trains](/wiki/Train "Train") and [Drones](/wiki/Drone "Drone"). There is no limit on the number of vehicles in the world.[1]

[Pioneers](/wiki/Pioneer "Pioneer") can be run over by vehicles[2] but receive no [damage](/wiki/Damage "Damage"), however living creatures (such as [Lizard Doggos](/wiki/Lizard_Doggo "Lizard Doggo")) that are run over by vehicles, will receive damage. 

Every vehicle except for the Drone can be driven by the Pioneer. 

## Contents

  * 1 Motor vehicles
    * 1.1 Fuel consumption
    * 1.2 Piloting
    * 1.3 Drifting
    * 1.4 Creature interactions
    * 1.5 Damage
      * 1.5.1 Fall
      * 1.5.2 Fire
      * 1.5.3 Poison
      * 1.5.4 Radiation
    * 1.6 Water
    * 1.7 Out-of-bounds damage
    * 1.8 Automation
      * 1.8.1 Path recording and usage
      * 1.8.2 Collision avoidance
      * 1.8.3 Deadlocking
      * 1.8.4 Ghosting
      * 1.8.5 Queueing
      * 1.8.6 Refueling
      * 1.8.7 Adding truck stations
      * 1.8.8 History
  * 2 Railed vehicles
    * 2.1 Automation
    * 2.2 Fuel
    * 2.3 Damage
    * 2.4 Water
  * 3 Flying vehicles
    * 3.1 Automation
    * 3.2 Fuel
    * 3.3 Throughput
  * 4 Achievements
  * 5 Gallery
  * 6 History
  * 7 Early game development
  * 8 References



## Motor vehicles

[](/wiki/File:Vehicles_gallery.png)

[](/wiki/File:Vehicles_gallery.png "Enlarge")

A gallery of wheeled vehicles.

### Fuel consumption

Motor vehicles (excluding the [Factory Cart](/wiki/Factory_Cart "Factory Cart")) require [fuel](/wiki/Fuels "Fuels") to operate, and can use every kind of fuel item. Fuel is input into a fuel slot by accessing the vehicle's inventory, which is usually a red box in the rear of the vehicle. 

Different fuels are consumed at different rates, based on the item's fuel value and the vehicle's energy consumption rate. The Tractor consumes the least fuel, followed by the Truck, then the Explorer, and finally the Cyber Wagon which consumes the most. Below is a table of how long, in seconds, each fuel type lasts at maximum acceleration. 

Fuel Consumption Table  [Fuel Type](/wiki/Fuels "Fuels") | Fuel Value  
([MJ](/wiki/MJ "MJ")) | [Biomass  
Burner](/wiki/Biomass_Burner "Biomass Burner")  
(30 MW) | [Coal-Powered  
Generator](/wiki/Coal-Powered_Generator "Coal-Powered Generator")  
(75 MW) | [Fuel-Powered  
Generator](/wiki/Fuel-Powered_Generator "Fuel-Powered Generator")  
(250 MW) | [Nuclear  
Power  
Plant](/wiki/Nuclear_Power_Plant "Nuclear Power Plant")  
(2500 MW) | [Cyber  
Wagon](/wiki/Cyber_Wagon "Cyber Wagon")  
(150 MW) | [Tractor](/wiki/Tractor "Tractor")  
(55 MW) | [Truck](/wiki/Truck "Truck")  
(75 MW) | [Explorer](/wiki/Explorer "Explorer")  
(90 MW) | [Chainsaw](/wiki/Chainsaw "Chainsaw")  
(75 MW) | [Jetpack](/wiki/Jetpack "Jetpack")  
(60-600 MW)   
---|---|---|---|---|---|---|---|---|---|---|---  
[](/wiki/Leaves "Leaves") [Leaves](/wiki/Leaves "Leaves") | 15 | 0.50s | - | - | - | 0.10s | 0.27s | 0.2s | 0.17s | - | \-   
[](/wiki/Wood "Wood") [Wood](/wiki/Wood "Wood") | 100 | 3.33s | - | - | - | 0.67s | 1.82s | 1.33s | 1.11s | - | \-   
[](/wiki/Mycelia "Mycelia") [Mycelia](/wiki/Mycelia "Mycelia") | 20 | 0.67s | - | - | - | 0.13s | 0.36s | 0.27s | 0.22s | - | \-   
[](/wiki/Hog_Remains "Hog Remains") [Hog Remains](/wiki/Hog_Remains "Hog Remains") | 250 | 8.33s | - | - | - | 1.67s | 4.55s | 3.33s | 2.78s | - | \-   
[](/wiki/Plasma_Spitter_Remains "Plasma Spitter Remains") [Plasma Spitter Remains](/wiki/Plasma_Spitter_Remains "Plasma Spitter Remains") | 250 | 8.33s | - | - | - | 1.67s | 4.55s | 3.33s | 2.78s | - | \-   
[](/wiki/Stinger_Remains "Stinger Remains") [Stinger Remains](/wiki/Stinger_Remains "Stinger Remains") | 250 | 8.33s | - | - | - | 1.67s | 4.55s | 3.33s | 2.78s | - | \-   
[](/wiki/Hatcher_Remains "Hatcher Remains") [Hatcher Remains](/wiki/Hatcher_Remains "Hatcher Remains") | 250 | 8.33s | - | - | - | 1.67s | 4.55s | 3.33s | 2.78s | - | \-   
[](/wiki/Biomass "Biomass") [Biomass](/wiki/Biomass "Biomass") | 180 | 6.00s | - | - | - | 1.20s | 3.27s | 2.40s | 2.00s | - | \-   
[](/wiki/Solid_Biofuel "Solid Biofuel") [Solid Biofuel](/wiki/Solid_Biofuel "Solid Biofuel") | 450 | 15.00s | - | - | - | 3.00s | 8.18s | 6.00s | 5.00s | 6.00s | 2.83s   
[](/wiki/Liquid_Biofuel "Liquid Biofuel") [Liquid Biofuel](/wiki/Liquid_Biofuel "Liquid Biofuel") | 750 | - | - | 3.00s | - | - | - | - | - | - | \-   
[](/wiki/Packaged_Liquid_Biofuel "Packaged Liquid Biofuel") [Packaged Liquid Biofuel](/wiki/Packaged_Liquid_Biofuel "Packaged Liquid Biofuel") | 750 | 25.00s | - | - | - | 5.00s | 13.64s | 10.00s | 8.33s | - | 12.50s   
[](/wiki/Coal "Coal") [Coal](/wiki/Coal "Coal") | 300 | - | 4.00s | - | - | 2.00s | 5.45s | 4.00s | 3.33s | - | \-   
[](/wiki/Compacted_Coal "Compacted Coal") [Compacted Coal](/wiki/Compacted_Coal "Compacted Coal") | 630 | - | 8.40s | - | - | 4.20s | 11.45s | 8.40s | 7.00s | - | \-   
[](/wiki/Petroleum_Coke "Petroleum Coke") [Petroleum Coke](/wiki/Petroleum_Coke "Petroleum Coke") | 180 | - | 2.40s | - | - | 1.20s | 3.27s | 2.40s | 2.00s | - | \-   
[](/wiki/Fuel "Fuel") [Fuel](/wiki/Fuel "Fuel") | 750 | - | - | 3.00s | - | - | - | - | - | - | \-   
[](/wiki/Packaged_Fuel "Packaged Fuel") [Packaged Fuel](/wiki/Packaged_Fuel "Packaged Fuel") | 750 | - | - | - | - | 5.00s | 13.64s | 10.00s | 8.33s | - | 5.00s   
[](/wiki/Turbofuel "Turbofuel") [Turbofuel](/wiki/Turbofuel "Turbofuel") | 2000 | - | - | 8.00s | - | - | - | - | - | - | \-   
[](/wiki/Packaged_Turbofuel "Packaged Turbofuel") [Packaged Turbofuel](/wiki/Packaged_Turbofuel "Packaged Turbofuel") | 2000 | - | - | - | - | 13.33s | 36.36s | 26.67s | 22.22s | - | 3.33s   
[](/wiki/Rocket_Fuel "Rocket Fuel") [Rocket Fuel](/wiki/Rocket_Fuel "Rocket Fuel") | 3600 | - | - | 14.40s | - | - | - | - | - | - | \-   
[](/wiki/Packaged_Rocket_Fuel "Packaged Rocket Fuel") [Packaged Rocket Fuel](/wiki/Packaged_Rocket_Fuel "Packaged Rocket Fuel") | 7200 | - | - | - | - | 48.00s | 130.91s | 96.00s | 80.00s | - | 4.00s   
[](/wiki/Ionized_Fuel "Ionized Fuel") [Ionized Fuel](/wiki/Ionized_Fuel "Ionized Fuel") | 5000 | - | - | 20.00s | - | - | - | - | - | - | \-   
[](/wiki/Packaged_Ionized_Fuel "Packaged Ionized Fuel") [Packaged Ionized Fuel](/wiki/Packaged_Ionized_Fuel "Packaged Ionized Fuel") | 10000 | - | - | - | - | 66.67s | 181.81s | 133.33s | 111.11s | - | 7.00s   
[](/wiki/Packaged_Heavy_Oil_Residue "Packaged Heavy Oil Residue") [Packaged Heavy Oil Residue](/wiki/Packaged_Heavy_Oil_Residue "Packaged Heavy Oil Residue") | 400 | - | - | - | - | 2.67s | 7.27s | 5.33s | 4.44s | - | \-   
[](/wiki/Packaged_Oil "Packaged Oil") [Packaged Oil](/wiki/Packaged_Oil "Packaged Oil") | 320 | - | - | - | - | 2.13s | 5.82s | 4.27s | 3.56s | - | \-   
[](/wiki/Battery "Battery") [Battery](/wiki/Battery "Battery") | 6000 | - | - | - | - | 40.00s | 109.00s   
(1m 49s) | 80.00s   
(1m 20.00s) | 66.70s   
(1m 6.70s) | - | \-   
[](/wiki/Uranium_Fuel_Rod "Uranium Fuel Rod") [Uranium Fuel Rod](/wiki/Uranium_Fuel_Rod "Uranium Fuel Rod") | 750000 | - | - | - | 300.00s   
(5m) | 5000.00s   
(1h 23m 20s) | 13636.00s   
(3h 47m 16s) | 10000.00s   
(2h 46m 40s) | 8333.00s   
(2h 18m 53s) | - | \-   
[](/wiki/Plutonium_Fuel_Rod "Plutonium Fuel Rod") [Plutonium Fuel Rod](/wiki/Plutonium_Fuel_Rod "Plutonium Fuel Rod") | 1500000 | - | - | - | 600.00s   
(10m) | 10000.00s   
(2h 46m 40s) | 27272.00s   
(7h 34m 32s) | 20000.00s   
(5h 33m 20s) | 16666.00s   
(4h 37m 46s) | - | \-   
[](/wiki/Ficsonium_Fuel_Rod "Ficsonium Fuel Rod") [Ficsonium Fuel Rod](/wiki/Ficsonium_Fuel_Rod "Ficsonium Fuel Rod") | 150000 | - | - | - | 60.00s   
(1m) | 1000.00s   
(16m 40s) | 2727.00s   
(45m 27s) | 2000.00s   
(33m 20s) | 1666.00s   
(27m 46s) | - | \-   
  
Fuel energy MJVehicle power MW=acceleration time where the fuel consumption rate is 55MW for the Tractor, 75MW for the Truck, 90MW for the Explorer and 150MW for the Cyber Wagon. 

If running at full speed all the time is wasteful (such as if the vehicle's throughput far exceeds that of the source or sink), the vehicle's path can be "underclocked" by including a lengthy pause, during which it will use no fuel. This pause should not be inside a station, as this will cause the station to consume power. Vehicles do not stop recording if the pioneer dismounts, so the player can get out and watch the bottleneck station fill or empty and then resume driving. Alternatively, you can edit the pause node to any desired length in seconds. 

Acceleration time is a timer counting down whenever the vehicle is accelerating or otherwise trying to move. This countdown does not occur while a vehicle is stationary or "coasting" down a slope. When a vehicle has no Acceleration Time left and tries to move it will pull one item from its fuel tank and adds its value to the Acceleration Time. The type of fuel being consumed is not recorded, only the burn time is added. This means radioactive fuels such as the [Uranium Fuel Rod](/wiki/Uranium_Fuel_Rod "Uranium Fuel Rod") or the [Plutonium Fuel Rod](/wiki/Plutonium_Fuel_Rod "Plutonium Fuel Rod") will only make a vehicle radioactive while sitting in the tank, once consumed and added to the Acceleration Time the radiation it produced will cease. (Additional Fuel Rods in the tank or inventory will still generate radiation however.) 

### Piloting

[](/wiki/File:Wheeled_vehicle_UI.png)

[](/wiki/File:Wheeled_vehicle_UI.png "Enlarge")

The Self-driving menu for a wheeled vehicle.

[Pioneers](/wiki/Pioneer "Pioneer") can enter or exit vehicles by interacting [`E`](/wiki/Controls "Controls") with it from any angle other than the rear side. Interacting a vehicle from its rear will open up its inventory slots instead, including the fuel slot.[3] When piloting a vehicle, the camera switches to a third-person perspective.[3] Pressing [`C`](/wiki/Controls "Controls") while in a vehicle locks the view to straight ahead, a second press unlocks the view. Vehicles cannot be upgraded.[4] Some small foliage can be destroyed when run into by a vehicle. In addition, the Tractors can destroy some smaller trees which Trucks cannot. 

### Drifting

[Trucks](/wiki/Truck "Truck") and [Explorers](/wiki/Explorer "Explorer") can perform drift by pressing [`Spacebar`](/wiki/Controls "Controls") while driving. This allows for tighter, sliding turns, for greater control. It is also possible to "J" turn by backing up [`S`](/wiki/Controls "Controls") quickly, steering [`A`](/wiki/Controls "Controls") or [`D`](/wiki/Controls "Controls"), and pressing [`Spacebar`](/wiki/Controls "Controls") at the same time, essentially a backwards drift. The [Factory Cart](/wiki/Factory_Cart "Factory Cart") has uncontrollable drift when driven forwards on any surface which is not perfectly flat. 

### Creature interactions

If a wheeled vehicle runs over any creatures such as [Hogs](/wiki/Hog "Hog") or [Spitters](/wiki/Spitter "Spitter"), it will damage them and potentially kill them if enough damage is inflicted. Damage dealt is relative to vehicle speed and size. 

Most creatures ignore the pioneer while driving a vehicle. The exception are [Flying Crab Hatchers](/wiki/Flying_Crab_Hatcher "Flying Crab Hatcher") will hatch when the pioneer approaches in a vehicle, and [Flying Crabs](/wiki/Flying_Crab "Flying Crab") will fly at the vehicle, but deal no damage and die when hitting it. 

### Damage

#### Fall

Pioneers do not take [fall damage](/wiki/Fall_damage "Fall damage") when riding in a vehicle, except when falling into the [void](/wiki/Void "Void"). Additionally a pioneer falling from height with the vehicle at the lower ground can avoid the fall damage by entering the vehicle just before hitting the ground (such as, by spamming [`E`](/wiki/Controls "Controls")). 

Vehicles themselves are immune to fall damage. 

#### Fire

Wheeled vehicles can receive minor damage when hit by a [Spitter](/wiki/Spitter "Spitter")'s fireball attacks. When the HP of the vehicle (displayed at bottom left) depletes to zero, the vehicle is dismantled. 

#### Poison

Pioneers in vehicles do not receive poison damage from [Poison Gas](/wiki/Poison_Gas "Poison Gas"), regardless of if they are wearing a [Gas mask](/wiki/Gas_mask "Gas mask") or not, even in vehicles that visually leave the Pioneer exposed, like Tractors, Factory Carts, and Explorers. 

#### Radiation

Pioneers are immune to [Radiation](/wiki/Radiation "Radiation") damage while inside a vehicle. 

### Water

Wheeled vehicles become disabled if they enter deep water, ejecting the pioneer and refusing to let them remount. This appears to happen when the water level reaches the center of the vehicle's hitbox, so Trucks can handle deeper water than Explorers or Tractors. If a vehicle does get stuck, it's sometimes possible to push a Truck back onto land, but usually the only solution is to dismantle the vehicle and rebuild it out of water. 

### Out-of-bounds damage

While in a vehicle the pioneer is not immune to [out-of-bounds damage](/wiki/World#Traversal "World"). This was a glitch which was patched. 

### Automation

[](/wiki/File:Loading_truck.png)

[](/wiki/File:Loading_truck.png "Enlarge")

A Truck arriving at an outpost.

#### Path recording and usage

The automation uses way-points _(displayed as triangles)_ for pathing. Vehicles now follow way-points more exactly by using "splines" to connect one way-point to another way-point.[5][6][note 1] It is a point-to-point system, which means vehicles will always face the current way-point until they reach the next. This means that vehicles will not correctly execute recorded three-point turns, though they can perform multi-point turns on their own initiative. 

Automated driving requires a clear straight path between way-points and a closed path "loop" to work optimally. 

To setup autopilot use the vehicle menu (press [`Q`](/wiki/Controls "Controls") while driving) to record a path. All recorded paths are required to be in a closed "loop" by ending on previous way-point or pause point.[7]

When recording, way-points displayed as blue triangles ▶ are placed periodically along the vehicle path pointing in the direction of travel.[7]

Automated Vehicles have to be instructed to stop at the [Truck Station](/wiki/Truck_Station "Truck Station") while recording, which is indicated by a pause point displayed as a yellow double vertical line ❚❚.[8][note 1]

After recording, way-points and pause points can be edited by interacting with them, to delete superfluous nodes or adjust pause times. 

Automated vehicle paths can be saved after recording, and loaded via the vehicle menu to other vehicles _of the same type_ that was used when path was recorded.[9]

#### Collision avoidance

Vehicles will not actively avoid obstacles (including another vehicle) by driving around the obstacle, but will collide with obstacles without causing any damage to the vehicle. 

If a vehicle collides with an obstacle (including another vehicle), it will reverse in a curve, to either adjust its course, or to get out of the way of another vehicle, before returning to it recorded path after the collision situation has been resolved.[10][11][note 1]

To avoid the need for collision avoidance, players can both record path to avoid stationary obstacles (foliage, landscape, buildings / machines, etc.), and/or have multiple Automated Vehicles following the same "path loop" as long as they are _going in the same direction_ and don't cross over (touch) another "path loop". 

#### Deadlocking

Vehicles can get "deadlocked" if there is no way for vehicles to perform collision avoidance.[12] This is by design and intentional in order to avoid issues.[13]

To prevent deadlocking, Players need to design vehicle path loops that make sense and don't cross over (touch) another "path loop" without using any preventive measures. 

If it is desired to record a vehicle path over another path _(either from same vehicle or another vehicle)_ , such for example when using a cross road intersection "+", the use of a "overpass" or "underpass" that avoids vehicles clipping one another, will prevent deadlocking and eliminate the requirement for vehicles to use collision avoidance maneuvers at that location. 

#### Ghosting

If an automated vehicle falls off a cliff or raised platform (road) the game will "ghost" the vehicle to handle that situation and will automatically pick up automated vehicles that have fallen and return them to the designated path.[14]

Ghosting is the very last obstacle avoidance resort the game will do in an effort to keep vehicles following their given path to the next destination. 

#### Queueing

Vehicles will queue (line up behind one another) at Truck Stations and not collide.[15][note 1]

#### Refueling

Vehicles will calculate how much Fuel they need for their given path and when at a Truck Station the vehicle will only take/use the amount of fuel they need.[16]

Vehicles will wait to be refueled if both the vehicle needs fuel AND the Truck Station is full of fuel or is receiving fuel.[17] Vehicles will receive enough fuel to make one "loop" of the path and get back to that _same Truck Station_ again. 

Vehicles will not wait to be refueled if the Truck Station has no fuel AND no fuel arrives within 5 to 9 seconds _(same time as docking animation)_.[18]

#### Adding truck stations

You have the ability to add a Truck Station to an existing recorded path.[8][note 1] Doing so will replace existing way-points ▶ and add a pause point ❚❚ at that location which can be edited as desired by interacting with it. 

Adding Truck Stations to existing paths can be useful, either as a pickup / drop-off point for resources or items, or even as a vehicle refueling station if needed. 

#### History

Vehicle automation has changed since Closed Alpha.[19] where, other than the Vehicle Menu, the most notable change was changing the blue arrows ⮕ to just triangles for vehicle way-points. 

━━━━━━━━━━ 

Notes: 

  1. ↑ 1.0 1.1 1.2 1.3 1.4 The purple "splines" shown in some reference videos are due to the video being captured during Update 5 Development and **these purple "splines" do NOT appear in actual Game**



## Railed vehicles

[](/wiki/File:Train_time_table.png)

[](/wiki/File:Train_time_table.png "Enlarge")

In the Train Station UI, switch to timetable tab and set the train schedule.

Monorail trains that consist of [Electric Locomotives](/wiki/Electric_Locomotive "Electric Locomotive") and [Freight Cars](/wiki/Freight_Car "Freight Car") can be driven manually or automated using the vehicle menu [`V`](/wiki/Controls "Controls"). Trains are bound to [Railways](/wiki/Railway "Railway") and cannot derail from them (with the exception of a train crash). Trains will drive off a dead end unless a buffer stop is put in place. The automated driving system will never drive off the edge, it will just show a no path error. 

It is not possible to couple or de-couple Freight Cars. Locomotives and Freight Cars have to be snapped to each other when being constructed, otherwise they will be counted as separate trains and will be able to collide with each other. 

### Automation

A train can be automated by adding [Train Stations](/wiki/Train_Station "Train Station") to its schedule. Trains will cycle through them in loops according to their timetables. Automated Trains will always be stopped at a train station if they fail to brake in advance, for example when the station is right after a steep down slope. 

### Fuel

Trains run exclusively on [power](/wiki/Power "Power") which ranges between 25MW for each locomotive when it is idle up to 110 MW when speeding up. All train stations also consume 50 MW constantly, in addition +50 MW for every active [Freight Platform](/wiki/Freight_Platform "Freight Platform"). 

### Damage

Trains and all pioneers riding in it are completely immune to all forms of damage, as they lack the Vehicle Health bar completely. 

  * _Continue reading:[Electric Locomotive](/wiki/Electric_Locomotive "Electric Locomotive")_



### Water

  * Trains cannot be built on [water](/wiki/Water "Water"), they can, however, be automated to pass through a Railway that is built underwater.
  * Pioneers will be ejected out of a Locomotive as soon as the train enter the water's surface.



## Flying vehicles

[Drones](/wiki/Drone "Drone") can be used for low throughput long-range transportation as they don't need any infrastructure besides two [Drone Ports](/wiki/Drone_Port "Drone Port"). Drone Ports only need to be [powered](/wiki/Power "Power"), and one of them supplied with fuel. Unlike motor vehicles or trucks, Drones aren't designed for pioneer transport. 

### Automation

Drones can be automated to bring resources between two Drone Ports, no more or less. It takes 51 seconds for the drone to take off and land, which means a Drone becomes more efficient over longer distances. 

### Fuel

Drones can be supplied by various mid- and late-game fuels. Fuels with higher energy density last longer, and additionally affect the travel speed. 

It is useful to build Drone Port hubs to distribute fuel. In such a hub, one Drone line is responsible from importing fuel from the fuel factory, which is then distributed to other Drone Ports in the hub. 

### Throughput

The throughput of a Drone can be seen at its home port, listing the max throughput, current throughput and trip duration. 

  * _Continue reading:[Drone](/wiki/Drone "Drone") • [Drone Port](/wiki/Drone_Port "Drone Port")_



## Achievements

[](/wiki/Achievements "Achievements")**[Establish dominance](/wiki/Achievements#Establish_dominance "Achievements")** •  _"Hit a creature with a vehicle."_

[](/wiki/Achievements "Achievements")**[Look both ways next time](/wiki/Achievements#Look_both_ways_next_time "Achievements")** •  _"Get knocked over by a vehicle."_

[](/wiki/Achievements "Achievements")**[Railroad tycoon](/wiki/Achievements#Railroad_tycoon "Achievements")** •  _"Build 5 km of Railway."_

[](/wiki/Achievements "Achievements")**[All aboard!](/wiki/Achievements#All_aboard! "Achievements")** •  _"Set up a train schedule."_

[](/wiki/Achievements "Achievements")**[Too fast, Too factory](/wiki/Achievements#Too_fast,_Too_factory "Achievements")** •  _"Move faster than 140 km/h."_

## Gallery

Load video

YouTube

YouTube might collect personal data. [Privacy Policy](https://www.youtube.com/howyoutubeworks/user-settings/privacy/)

ContinueDismiss

  * [](/wiki/File:Vehicles_showcase_dev_blog.png "Wheeled vehicles showcased in the dev blog")

Wheeled vehicles showcased in the dev blog




## History

  * [Patch 1.1.0.2](/wiki/Patch_1.1.0.2 "Patch 1.1.0.2"): Fixed Photo Mode Poses and Pioneer Positioning Nudge affecting Vehicles and [Hypertubes](/wiki/Hypertube "Hypertube")
  * [Patch 1.0.0.3](/wiki/Patch_1.0.0.3 "Patch 1.0.0.3"): Fixed a crash when loading a save while a player was inside a Vehicle
  * [Patch 1.0](/wiki/Patch_1.0 "Patch 1.0"): Pioneers no longer take fall damage while within vehicles.
  * [Patch 0.8.3.2](/wiki/Patch_0.8.3.2 "Patch 0.8.3.2"): You can now enter occupied Vehicles and kick out the [driver](/wiki/Pioneer "Pioneer") if the driver is offline
  * [Patch 0.8.3.1](/wiki/Patch_0.8.3.1 "Patch 0.8.3.1"): [Invert Look](/wiki/Settings#Controls "Settings") option now also works on Vehicles and [Trains](/wiki/Trains "Trains")
  * [Patch 0.8.2.0](/wiki/Patch_0.8.2.0 "Patch 0.8.2.0")
    * Refactored the way Vehicles are outlined
    * Camera should not now rubber band as much when driving vehicles as it is now allowed to clip through various objects
    * Vehicle engines will now shut down when the vehicle is submerged in water
    * Fixed Players being unable to enter a Vehicle if another Player was interacting with the inventory of the Vehicle
    * Fixed sliding not ending when entering Vehicles
  * [Patch 0.8.0.0](/wiki/Patch_0.8.0.0 "Patch 0.8.0.0")
    * Moved Vehicle physics to using Unreal Engine 5 Chaos
    * Overhauled all Vehicle sounds
    * Improved the manual driving of all Vehicles
    * Reworked all Vehicle trunks visually simplifying the animation and adding a new sound
    * Added functionality for Vehicles to deal damage to creatures by hitting them 
      * Damage dealt is relative to vehicle speed and size
    * Undocumented Change - Removed Air Control (ability to do stunts)[20]
  * [Patch 0.7.0.2](/wiki/Patch_0.7.0.2 "Patch 0.7.0.2"): 
    * Vehicles should work again :)
    * Enable Autopilot button now updates to the Disable Autopilot button after stopping a vehicle path recording
  * [Patch 0.6.1.1](/wiki/Patch_0.6.1.1 "Patch 0.6.1.1"): Polish on the Vehicle Path directional arrows in the Load Path Menu
  * [Patch 0.6.0.14](/wiki/Patch_0.6.0.14 "Patch 0.6.0.14")
    * Relevant items now shows fuel types
    * Record Vehicle Path button now updates properly
    * Editing a path node and setting the wait time to 0 now warns that the time needs to be over 0 seconds
    * Added a notification to indicate a path cannot be loaded because there are no paths
    * Fixed Vehicle paths being deleted from the Load Vehicle Path Menu not actually disappearing until the menu was closed
    * Added a warning when trying to record a vehicle path on a vehicle that has no [fuel](/wiki/Fuels "Fuels")
  * [Patch 0.6.0.4](/wiki/Patch_0.6.0.4 "Patch 0.6.0.4"): Fixed all [build and dismantle interactions](/wiki/Build_Gun "Build Gun") getting locked when entering a vehicle by pressing both Q and E at the same time
  * [Patch 0.6.0.1](/wiki/Patch_0.6.0.1 "Patch 0.6.0.1"): Fixed a crash when damaging a player inside a vehicle with explosive damage
  * [Patch 0.5.1.12](/wiki/Patch_0.5.1.12 "Patch 0.5.1.12")
    * Fixed a crash that could happen if there’s a deadlock near a non-automated vehicle
    * Decreased the collision-avoidance distance for automated vehicles
    * Fixed a crash for [Multiplayer](/wiki/Multiplayer "Multiplayer") Clients and [Dedicated Server](/wiki/Dedicated_Server "Dedicated Server") Clients related to vehicle paths
    * Fixed an issue with vehicle path recording inside factories sometimes recording docking to [Truck Station](/wiki/Truck_Station "Truck Station") on floors above the vehicle
    * Fixed a crash related to the vehicle representation on the [Map](/wiki/Map "Map")
  * [Patch 0.5.1.11](/wiki/Patch_0.5.1.11 "Patch 0.5.1.11")
    * Fixed a bug where Vehicles would sometimes get displaced for Clients when far away from other players
    * Fixed issue where vehicles would get stuck ghosting
    * Fixed bug where the Load Vehicle Path UI would display inaccurate path lengths
    * Fixed several minor issues related to vehicle automation
    * Fixed a bug where automated vehicles would sometimes be able to move without fuel
    * Fixed issue where automated vehicles would sometimes stop moving when about to enter a station right after loading a game
    * Fixed issue with automated vehicles sometimes continuing to drive despite being blocked
    * Fixed an issue where removing a vehicle target would result in collision avoidance not working anymore for that path
    * Fixed issue with automated vehicles sometimes driving into other automated vehicles that are waiting in line
    * A [HUD](/wiki/HUD "HUD") message is now displayed every time an automated vehicle gets completely stuck (“deadlock”)
  * [Patch 0.5.1.10](/wiki/Patch_0.5.1.10 "Patch 0.5.1.10")
    * Fixed crash that would happen on startup if there was a vehicle path with zero targets
    * Fixed a crash related to Vehicle Automation for Clients
    * Fixed a bug in the Load Vehicle Path UI where the “Used by this vehicle” checkmark was missing for Clients
    * Fixed the Vehicle Craft Bench UI being a bit off center
  * [Patch 0.5.1.9](/wiki/Patch_0.5.1.9 "Patch 0.5.1.9"): Load/Save Path menu is now disabled when there are no paths
  * [Patch 0.5.1.7](/wiki/Patch_0.5.1.7 "Patch 0.5.1.7")
    * Overhauled the Vehicle Recording UI, no longer a radial menu
    * All Vehicle UIs (Trains and Vehicles) are now opened with [`Q`](/wiki/Controls "Controls") key by default
    * Fixed some bugs with the Vehicle HUD not updating properly when stopping a recording midway without closing the loop
    * Fixed [Freight Cars](/wiki/Freight_Platform "Freight Platform") failing to load/unload correctly with the rule set to Fully Load/Unload which lead to them getting stuck in docking until force cancelled
    * Fixed [Multiplayer](/wiki/Multiplayer "Multiplayer") and [Dedicated servers](/wiki/Dedicated_servers "Dedicated servers") Clients not being able to cancel the docking sequence
    * Fixed the [Map](/wiki/Map "Map") not being properly visible for some players who had previously unlocked more areas of it and added some future proofing so this hopefully doesn’t happen again
    * Fixed an issue with automated vehicle wait times being reset when loading a game
    * Vehicles should no longer claim targets outside of stations when docked
    * Fixed a bug where sometimes vehicle pauses would be longer than intended when they were far from any player
    * Fixed issue where automated vehicles in long-distance mode would sometimes get out of sync for Multiplayer and Dedicated servers Client
    * Fixed bug where Vehicles weren’t placeable in the [Truck Station](/wiki/Truck_Station "Truck Station") docking area
    * Fixed crash that would sometimes happen when Vehicle path recordings were finished
  * [Patch 0.5.1.3](/wiki/Patch_0.5.1.3 "Patch 0.5.1.3")
    * Fixed a bug where pause time on Vehicle Automation was not reset when manually overridden
    * Automated vehicles will stay docked until their inventory is empty if unloading cargo
    * Moved positions of “Cancel” and “Start/Stop Recording” in the Vehicle Record Menu to avert accidental selections of “Stop Recording
  * [Patch 0.5.1.1](/wiki/Patch_0.5.1.1 "Patch 0.5.1.1")
    * Vehicle path arrows in UI now have the correct positions
    * Fixed a possible exploit in Vehicle fuel calculations
    * Made Vehicles take available fuel for as long as they are docked
    * Fixed the fuel consumption metrics in the [Truck Stations](/wiki/Truck_Station "Truck Station") not accounting for pauses and docking times in the path time
    * Fixed a bug where a vehicle might be blocked indefinitely when in long distance mode
  * [Patch 0.5.0.14](/wiki/Patch_0.5.0.14 "Patch 0.5.0.14")
    * Vehicles now try to stop ghosting as soon as possible when blocked
    * Fixed a calculation error when fuel is added manually
    * Directional arrows for the Vehicle in the [Map](/wiki/Map "Map") preview when loading a Vehicle Path are now displayed from the centre of the Vehicle
    * Added a tooltip for insufficient fuel
  * [Patch 0.5.0.13](/wiki/Patch_0.5.0.13 "Patch 0.5.0.13")
    * Fixed an issue where Vehicles would not receive fuel from a [station](/wiki/Truck_Station "Truck Station") if their fuel inventory was empty
    * Fixed an issue where Vehicle Paths were not updated after a station was built over them
    * Fixed issues with Vehicles getting out of sync with their Vehicle Stations after loading a game
    * Fixed Vehicles burning up fuel when standing still
    * Added directional arrows to the path in the [Map](/wiki/Map "Map") preview when loading a Vehicle Path
  * [Patch 0.5.0.12](/wiki/Patch_0.5.0.12 "Patch 0.5.0.12")
    * Fixed an issue with vehicles being stuck docking forever if there were Fuel issues
    * Better detection for when vehicles fall through the ground
    * Fixed issue with vehicles sometimes teleporting upwards when loading a game
  * [Patch 0.5.0.11](/wiki/Patch_0.5.0.11 "Patch 0.5.0.11")
    * Fixed a crash related to Vehicle Automation
    * Fixed a crash when deleting Vehicle path nodes and trying to load that Vehicle Path
    * Removed “Delete Path” option from the Vehicle wheel as you can now use “Cancel Recording” does the same thing
  * [Patch 0.5.0.9](/wiki/Patch_0.5.0.9 "Patch 0.5.0.9")
    * Fixed Vehicle paths selected from the "All Vehicle Path" tab made by a different vehicle remaining selected when returning to the "Load Vehicle Path" tab
    * Fixed a crash in the Vehicle system
    * Fixed remaining issues with Fuel and Vehicles
    * Vehicle docking wait times are now saved
  * [Patch 0.5.0.8](/wiki/Patch_0.5.0.8 "Patch 0.5.0.8")
    * Manually driven Vehicles now take Fuel from [Truck Stations](/wiki/Truck_Station "Truck Station")
    * Fixed a Vehicle related crash
    * Hopefully fixed all issues with the Vehicle Refueling logic
    * Hopefully fixed all issues with Vehicles running out of fuel
  * [Patch 0.5.0.7](/wiki/Patch_0.5.0.7 "Patch 0.5.0.7"): Fixed Vehicles not docking properly when in long-distance simulation mode
  * [Patch 0.5.0.6](/wiki/Patch_0.5.0.6 "Patch 0.5.0.6")
    * Fixed Vehicle physics not working as intended on [Foundations](/wiki/Foundations "Foundations")
    * Fixed Vehicle icons not rotating on the [[Map]
  * [Patch 0.5.0.0](/wiki/Patch_0.5.0.0 "Patch 0.5.0.0"): 
    * Vehicles can now be [painted](/wiki/Customizer "Customizer")
    * Updated [Truck](/wiki/Truck "Truck") visuals
    * Updated [Truck Station](/wiki/Truck_Station "Truck Station") visuals
    * Vehicle recording is now completed by driving back to the first created node
    * Vehicle self-driving AI overhaul, will now consider more than just the next waypoint and avoid obstacles when moving to their destination
    * A queue system between self-driving vehicles has been added so they don't run into each other at Truck Stations and on their routes
    * Vehicle self-driving path behavior has also been overhauled
    * Vehicles will now try to unstuck themselves as a last resort, ensuring that they get back on their route
    * You can now Save and Load recorded vehicle paths for vehicles of the same type
    * Additional Input and Output slots have been added to the Truck Station
    * Vehicles will now only take the proper amount of [fuel](/wiki/Fuels "Fuels") from a Truck Station that is needed to complete a full trip and they will not run out of fuel even when getting stuck or lost
    * Truck Station UI has been updated to show average fuel consumption and delivery throughput
    * Vehicles can now be sampled the same way [buildings](/wiki/Buildings "Buildings") can with the build gun/dismantle gun
    * Fixed vehicles disappearing under the world
    * Vehicles that have disappeared under the world but were still visible on the map have been brought back
    * Fixed up storage boxes in vehicles not being interactable sometimes
  * [Patch 2018-10-11](/wiki/Patch_2018-10-11 "Patch 2018-10-11"): Introduced



## Early game development

Prior to Closed Alpha, in Sprint 23 (week 46) we saw there used to be a Speed Sign that would limit speed for self driving ground vehicles. The Speed Sign was removed. 

  * See also: [Game Development - Signs](/wiki/Early_game_development#Signs "Early game development")



## References

  1. ↑ "no there isnt varrili" - [Jace](/wiki/Jace "Jace") on Discord when asked "Is there a cap of how many vehicles a player can have?" by Varrili
  2. ↑ "you can run over people :smile:" - Jace on Discord
  3. ↑ 3.0 3.1 [\- YouTube Dev Blog #1: Vehicles - Piloting](https://www.youtube.com/watch?v=IxoCzb2M0vQ&t=90)
  4. ↑ "not at the moment" - [Jace](/wiki/Jace "Jace") on Discord when asked "Is there plans to have these vehicles be upgrade-able?"
  5. ↑ [YouTube - Changes to Truck Station and Vehicle Automation coming in Update 5 - Automated Vehicle Paths](https://www.youtube.com/watch?v=kh3lVrBdjFE&t=111s)
  6. ↑ [YouTube - Changes to Truck Station and Vehicle Automation coming in Update 5 - Improved vehicle movement visuals from a long distance](https://www.youtube.com/watch?v=kh3lVrBdjFE&t=434s)
  7. ↑ 7.0 7.1 [YouTube - Changes to Truck Station and Vehicle Automation coming in Update 5 - Vehicles require a "closed loop" when recording](https://www.youtube.com/watch?v=kh3lVrBdjFE&t=365s)
  8. ↑ 8.0 8.1 [YouTube - Changes to Truck Station and Vehicle Automation coming in Update 5 - Add truck stations to recorded paths](https://www.youtube.com/watch?v=kh3lVrBdjFE&t=474s)
  9. ↑ [YouTube - Changes to Truck Station and Vehicle Automation coming in Update 5 - You can now save/load recorded paths](https://www.youtube.com/watch?v=kh3lVrBdjFE&t=384s)
  10. ↑ [YouTube - Changes to Truck Station and Vehicle Automation coming in Update 5 - Better handling of obstacles](https://www.youtube.com/watch?v=kh3lVrBdjFE&t=197s)
  11. ↑ [YouTube - Satisfactory UPDATE 5 Experimental Release Countdown - Vehicle Collision Avoidance Example](https://www.youtube.com/watch?v=Rumqu_lyapg&t=5409s)
  12. ↑ [YouTube - May 3rd, 2022 Livestream - State of Dev - Vehicle deadlocking](https://www.youtube.com/watch?v=HBdLi32e74Q&t=472s)
  13. ↑ [YouTube - May 3rd, 2022 Livestream - State of Dev - Vehicle deadlocking reason](https://www.youtube.com/watch?v=HBdLi32e74Q&t=543s)
  14. ↑ [YouTube - Changes to Truck Station and Vehicle Automation coming in Update 5 - Vehicle "ghosting"](https://www.youtube.com/watch?v=kh3lVrBdjFE&t=234s)
  15. ↑ [YouTube - Satisfactory UPDATE 5 Experimental Release Countdown - Truck Station Queueing](https://www.youtube.com/watch?v=Rumqu_lyapg-2&t=5218s)
  16. ↑ [YouTube - Changes to Truck Station and Vehicle Automation coming in Update 5 - Automated vehicles handle fuel better](https://www.youtube.com/watch?v=kh3lVrBdjFE&t=307s)
  17. ↑ [YouTube - Satisfactory UPDATE 5 Experimental Release Countdown - Vehicle refueling general info](https://www.youtube.com/watch?v=Rumqu_lyapg&t=5619s)
  18. ↑ [YouTube - Satisfactory UPDATE 5 Experimental Release Countdown - Vehicle refueling wait time](https://www.youtube.com/watch?v=Rumqu_lyapg&t=5645s)
  19. ↑ [YouTube - Dev Blog #1: Vehicles - Automation](https://www.youtube.com/watch?v=IxoCzb2M0vQ&t=166s)
  20. ↑ [YouTube - We're upgrading to UNREAL ENGINE 5 - Vehicle physics overhaul](https://www.youtube.com/watch?v=dY__x2dq7Sk&t=1130s)



  * [v](/wiki/Template:VehicleNav "Template:VehicleNav")
  * [e](https://satisfactory.wiki.gg/wiki/Template:VehicleNav?action=edit)
  * [h](https://satisfactory.wiki.gg/wiki/Template:VehicleNav?action=history)

Transportation  
---  
Motor vehicles| [](/wiki/Tractor "Tractor") [Tractor](/wiki/Tractor "Tractor") • [](/wiki/Truck "Truck") [Truck](/wiki/Truck "Truck") • [](/wiki/Explorer "Explorer") [Explorer](/wiki/Explorer "Explorer") • [](/wiki/Factory_Cart "Factory Cart") [Factory Cart](/wiki/Factory_Cart "Factory Cart") • [](/wiki/Golden_Factory_Cart "Golden Factory Cart") [Golden Factory Cart](/wiki/Golden_Factory_Cart "Golden Factory Cart") • [](/wiki/Cyber_Wagon "Cyber Wagon") [Cyber Wagon](/wiki/Cyber_Wagon "Cyber Wagon") • [](/wiki/Truck_Station "Truck Station") [Truck Station](/wiki/Truck_Station "Truck Station") • [](/wiki/Drone_Port "Drone Port") [Drone Port](/wiki/Drone_Port "Drone Port") • [](/wiki/Drone "Drone") [Drone](/wiki/Drone "Drone")  
Rail vehicles| [](/wiki/Electric_Locomotive "Electric Locomotive") [Electric Locomotive](/wiki/Electric_Locomotive "Electric Locomotive") • [](/wiki/Freight_Car "Freight Car") [Freight Car](/wiki/Freight_Car "Freight Car") • [](/wiki/Train_Station "Train Station") [Train Station](/wiki/Train_Station "Train Station") • [](/wiki/Freight_Platform "Freight Platform") [Freight Platform](/wiki/Freight_Platform "Freight Platform") • [](/wiki/Fluid_Freight_Platform "Fluid Freight Platform") [Fluid Freight Platform](/wiki/Fluid_Freight_Platform "Fluid Freight Platform") • [](/wiki/Empty_Platform "Empty Platform") [Empty Platform](/wiki/Empty_Platform "Empty Platform") • [](/wiki/Empty_Platform_With_Catwalk "Empty Platform With Catwalk") [Empty Platform With Catwalk](/wiki/Empty_Platform_With_Catwalk "Empty Platform With Catwalk") • [](/wiki/Railway "Railway") [Railway](/wiki/Railway "Railway") • [](/wiki/Railroad_Switch_Control "Railroad Switch Control") [Railroad Switch Control](/wiki/Railroad_Switch_Control "Railroad Switch Control") • [](/wiki/Buffer_Stop "Buffer Stop") [Buffer Stop](/wiki/Buffer_Stop "Buffer Stop") • [](/wiki/Block_Signal "Block Signal") [Block Signal](/wiki/Block_Signal "Block Signal") • [](/wiki/Path_Signal "Path Signal") [Path Signal](/wiki/Path_Signal "Path Signal")  
Hypertubes| [](/wiki/Hypertube "Hypertube") [Hypertube](/wiki/Hypertube "Hypertube") • [](/wiki/Hypertube_Entrance "Hypertube Entrance") [Hypertube Entrance](/wiki/Hypertube_Entrance "Hypertube Entrance") • [](/wiki/Hypertube_Support "Hypertube Support") [Hypertube Support](/wiki/Hypertube_Support "Hypertube Support") • [](/wiki/Stackable_Hypertube_Support "Stackable Hypertube Support") [Stackable Hypertube Support](/wiki/Stackable_Hypertube_Support "Stackable Hypertube Support") • [](/wiki/Hypertube_Wall_Hole "Hypertube Wall Hole") [Hypertube Wall Hole](/wiki/Hypertube_Wall_Hole "Hypertube Wall Hole") • [](/wiki/Hypertube_Wall_Support "Hypertube Wall Support") [Hypertube Wall Support](/wiki/Hypertube_Wall_Support "Hypertube Wall Support") • [](/wiki/Hypertube_Floor_Hole "Hypertube Floor Hole") [Hypertube Floor Hole](/wiki/Hypertube_Floor_Hole "Hypertube Floor Hole") • [](/wiki/Hypertube_Junction "Hypertube Junction") [Hypertube Junction](/wiki/Hypertube_Junction "Hypertube Junction") • [](/wiki/Hypertube_Branch "Hypertube Branch") [Hypertube Branch](/wiki/Hypertube_Branch "Hypertube Branch")  
Pioneer transport| [](/wiki/Jump_Pad "Jump Pad") [Jump Pad](/wiki/Jump_Pad "Jump Pad") • [](/wiki/U-Jelly_Landing_Pad "U-Jelly Landing Pad") [U-Jelly Landing Pad](/wiki/U-Jelly_Landing_Pad "U-Jelly Landing Pad") • [](/wiki/Personnel_Elevator "Personnel Elevator") [Personnel Elevator](/wiki/Personnel_Elevator "Personnel Elevator") • [](/wiki/Main_Portal "Main Portal") [Main Portal](/wiki/Main_Portal "Main Portal") • [](/wiki/Satellite_Portal "Satellite Portal") [Satellite Portal](/wiki/Satellite_Portal "Satellite Portal")
  *[v]: View this template
  *[e]: Edit this template
  *[h]: History of this template
  *[his]: his trivia section
