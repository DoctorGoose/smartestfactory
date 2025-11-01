# Drone

## Drone

[ ](/wiki/File:Drone.png "Drone.png")

_Transports available input back and forth between its home Port and destination Ports. Drone Status and other details can be viewed at a Drone's home Port.  
Must be built on a Drone Port.  
Has 9 inventory slots.  
Can use any fuel type.  
Refuels at any of its connected Ports if possible._

### Unlocked by

[Tier 8](/wiki/Tier_8 "Tier 8") \- Aeronautical Engineering

### Class name

Desc_DroneTransport_C

## Vehicle

### Inventory size

9 slots

### Max speed

252 km/h

## Dimensions

### Width

16 m

### Length

6 m

### Height

3 m

### Area

96 m2

## Ingre­dients

**4 ×[](/wiki/Motor "Motor") [Motor](/wiki/Motor "Motor")**

**10 ×[](/wiki/Alclad_Aluminum_Sheet "Alclad Aluminum Sheet") [Alclad Aluminum Sheet](/wiki/Alclad_Aluminum_Sheet "Alclad Aluminum Sheet")**

**1 ×[](/wiki/Radio_Control_Unit "Radio Control Unit") [Radio Control Unit](/wiki/Radio_Control_Unit "Radio Control Unit")**

**2 ×[](/wiki/AI_Limiter "AI Limiter") [AI Limiter](/wiki/AI_Limiter "AI Limiter")**

**1 ×[](/wiki/Portable_Miner "Portable Miner") [Portable Miner](/wiki/Portable_Miner "Portable Miner")**

A **Drone** is an aerial vehicle that flies items between its home and selected [Drone Port](/wiki/Drone_Port "Drone Port"). 

## Contents

  * 1 Usage
    * 1.1 Fuel
    * 1.2 Logistics
    * 1.3 Behavior
    * 1.4 Efficiency
  * 2 External links
  * 3 Trivia
  * 4 History
  * 5 References



## Usage

Each Drone can only be assigned to 1 home [Drone Port](/wiki/Drone_Port "Drone Port"), and that home Drone Port can only be linked to 1 other Drone Port (that Drone Port, in turn, doesn't necessarily need to be linked back to this Drone Port). There is no limitation on the number of assigned Drones unloading on a Drone Port, but only one can unload at a time. Waiting Drones will circle above the Drone Port. 

When flying from one Port to another, a Drone will show a take-off animation, wiggling around; rise vertically, turning mid-air then fly roughly in a straight line to the destination. It then descends, followed by some wiggling animation and finally docks. Drones will attempt to navigate around obstacles mid-flight. As the take-off and landing animation can take a considerable amount of time, the efficiency of Drones increases with distance. 

Drones can potentially be used as a means of player transportation. [Pioneers](/wiki/Pioneer "Pioneer") can stand on the Drone for a ride, but fall protection [equipment](/wiki/Equipment "Equipment"), such as a [Jetpack](/wiki/Jetpack "Jetpack"), is highly recommended, as the Pioneer can fall off mid-air when the Drone starts accelerating forward or changes direction. It is recommended to stand on the wing near the circular hinge part close to the main body as it is the most consistent in preventing falls. 

### Fuel

Drones must use [](/wiki/Battery "Battery") [Batteries](/wiki/Battery "Battery"), [](/wiki/Packaged_Fuel "Packaged Fuel") [Packaged Fuel](/wiki/Packaged_Fuel "Packaged Fuel"), [](/wiki/Packaged_Turbofuel "Packaged Turbofuel") [Packaged Turbofuel](/wiki/Packaged_Turbofuel "Packaged Turbofuel"), [](/wiki/Packaged_Rocket_Fuel "Packaged Rocket Fuel") [Packaged Rocket Fuel](/wiki/Packaged_Rocket_Fuel "Packaged Rocket Fuel"), [](/wiki/Packaged_Ionized_Fuel "Packaged Ionized Fuel") [Packaged Ionized Fuel](/wiki/Packaged_Ionized_Fuel "Packaged Ionized Fuel"), [](/wiki/Uranium_Fuel_Rod "Uranium Fuel Rod") [Uranium Fuel Rods](/wiki/Uranium_Fuel_Rod "Uranium Fuel Rod"), or [](/wiki/Plutonium_Fuel_Rod "Plutonium Fuel Rod") [Plutonium Fuel Rods](/wiki/Plutonium_Fuel_Rod "Plutonium Fuel Rod") as fuel. Drones will use different fuels at different rates depending on their path, the given fuel's energy value, and the speed of the drone, which also varies based on fuel type. 

Use this table below to compare the different fuels' energy density (and thus how long one lasts) to each other. The table also lists the approximate speeds Drones go, and the jet color seen, depending on the different fuel type used. 

[Fuel Type](/wiki/Fuels "Fuels") | Fuel Value  
([MJ](/wiki/MJ "MJ"))  | Speed (m/s)  | Jet color   
---|---|---|---  
[](/wiki/Packaged_Fuel "Packaged Fuel") [Packaged Fuel](/wiki/Packaged_Fuel "Packaged Fuel") | 750  | 25  | Yellow   
[](/wiki/Packaged_Turbofuel "Packaged Turbofuel") [Packaged Turbofuel](/wiki/Packaged_Turbofuel "Packaged Turbofuel") | 2,000  | 30  | Red   
[](/wiki/Battery "Battery") [Battery](/wiki/Battery "Battery") | 6,000  | 37  | Blue-yellow   
[](/wiki/Packaged_Rocket_Fuel "Packaged Rocket Fuel") [Packaged Rocket Fuel](/wiki/Packaged_Rocket_Fuel "Packaged Rocket Fuel") | 7,200  | 37  | Red-yellow   
[](/wiki/Packaged_Ionized_Fuel "Packaged Ionized Fuel") [Packaged Ionized Fuel](/wiki/Packaged_Ionized_Fuel "Packaged Ionized Fuel") | 10,000  | 45  | Orange-yellow   
[](/wiki/Uranium_Fuel_Rod "Uranium Fuel Rod") [Uranium Fuel Rod](/wiki/Uranium_Fuel_Rod "Uranium Fuel Rod") | 750,000  | 42  | Green   
[](/wiki/Plutonium_Fuel_Rod "Plutonium Fuel Rod") [Plutonium Fuel Rod](/wiki/Plutonium_Fuel_Rod "Plutonium Fuel Rod") | 1,500,000  | 45  | Blue   
  
### Logistics

Drones can be used for long-range low-throughput transportation, such as of high-end products, which usually come in small per-minute quantities. Drones can only transport between two Drone Ports, the home Port and any other Port. At least one of the Drone Ports requires a steady supply of fuel to power the Drone(s). Unlike [trains](/wiki/Electric_Locomotive "Electric Locomotive"), Drones don't block the input of items during the cargo loading animation. 

### Behavior

Drones will try to fly from Drone Ports to other Drone Ports as straight as possible. When terrain is in the path, the Drone will try to avoid the object. Drones use a 64 x 64 grid of the [world](/wiki/World "World") to generate their path. 

Drones have only one home Port, which is the Port the Drone is built on. No additional Drones can be built onto a Drone Port, but multiple Drones can use it as their destination Port. If multiple Drones are awaiting to be unloaded at the same time, they will fly around the Port at a 20m radius, stacking vertically with an 8m gap in between. 

A Drone will initially take the required amount of fuel for a round trip from its home Port, consuming the fuel immediately upon takeoff. If the Drone is being supplied with fuel at its destination (non-home) Port instead, it will take the required amount of fuel for a round trip, but not consume it until it returns to its home Port and takes off from it, taking no fuel from the home Port. Thus, it is possible to have 2 drones on a line with 2 drone ports, even if one of them doesn't have fuel. In this scenario, it has to be manually supplied with fuel for its first trip, as it would not take off from the home Port to start transporting otherwise. After that, fuel only needs to be supplied at one of the two drone ports for both drones to function. 

While hovering in the queue waiting to land the drone will not consume any fuel. 

### Efficiency

After the first round trip is finished, the stack throughput of the Drone will be shown in the Drone's home Port, alongside its maximum throughput and fuel required per round trip. The efficiency of Drones increases with travel distance, as the landing and take-off animation takes 51 seconds. If the route is too short, most of it will be the landing animations; it would take 102 seconds to move items from two Drone Ports immediately next to each other. 

## External links

  * [Elaborate Drone guide on Reddit](https://www.reddit.com/r/SatisfactoryGame/comments/mbqex4/the_ultimate_drone_guide/)



## Trivia

  * The development of Drones was vaguely alluded to on May 15th, 2020: "There's going to be a new vehicle in Tier 7 or 8".[1]
  * The inclusion of Drones was jokingly "confirmed" on July 23rd, 2020, via [Jace](/wiki/Jace "Jace")'s high quality screenshots/mspaint art video.[2]
  * During Update 5 and some of Update 6, the drones used the spirit of the portable miner in their recipe to drill straight under the ground, ignoring the world grid and flying under the map. This was fixed during Update 6's Experimental Period.
  * The drones have a theoretically unlimited queue for the holding pattern on drone ports if the port is unpowered and can remain in the air in the holding pattern for an extremely long time



## History

  * [Patch 1.1.0.0](/wiki/Patch_1.1.0.0 "Patch 1.1.0.0"): Many improvements to drone movement and pathing which should improve the way drones interact with their automated routes
  * [Patch 1.0.0.4](/wiki/Patch_1.0.0.4 "Patch 1.0.0.4"): Potential fix for a rare crash when dismantling a drone at the end of its takeoff sequence
  * [Patch 1.0.0.3](/wiki/Patch_1.0.0.3 "Patch 1.0.0.3"): Fixed a crash on load in saves with corrupted Drones in them
  * [Patch 1.0](/wiki/Patch_1.0 "Patch 1.0")
    * Can now use almost all types of [Fuels](/wiki/Fuels "Fuels") instead of only [batteries](/wiki/Battery "Battery").
    * The speed of the Drones is different based on the fuel used, with better fuels providing higher speed.
  * [Patch 0.8.2.0](/wiki/Patch_0.8.2.0 "Patch 0.8.2.0"): Fixed a bug where drones would sometimes consume batteries multiple times when starting a new trip, especially when the player is far away
  * [Patch 0.8.0.0](/wiki/Patch_0.8.0.0 "Patch 0.8.0.0"): Fixed a potential bug with drone queue processing
  * [Patch 0.6.0.12](/wiki/Patch_0.6.0.12 "Patch 0.6.0.12"): Potential fix to a crash related to DroneAction
  * [Patch 0.6.0.7](/wiki/Patch_0.6.0.7 "Patch 0.6.0.7"): Fixed flying through cliffs and similar terrain
  * [Patch 0.6.0.1](/wiki/Patch_0.6.0.1 "Patch 0.6.0.1"): Potential fix when returning to the main menu when having built Drones
  * [Patch 0.4.3.1](/wiki/Patch_0.4.3.1 "Patch 0.4.3.1"): Fixed minor issue related to the world grid
  * [Patch 0.4.0.11](/wiki/Patch_0.4.0.11 "Patch 0.4.0.11"): Reduced default round-trip [Battery](/wiki/Battery "Battery") cost for Drones to 4 (from 5) and reduced cost/distance from 1.66 to 1 Battery per kilometre.
  * [Patch 0.4.0.10](/wiki/Patch_0.4.0.10 "Patch 0.4.0.10"): Fixed bug where the distance between Drone stations wouldn’t be calculated properly, causing incorrect round-trip time estimates and battery consumption, Battery consumption should now properly increase over larger distances.
  * [Patch 0.4.0.6](/wiki/Patch_0.4.0.6 "Patch 0.4.0.6"): 
    * Drone Pathfinding and [World](/wiki/World "World") Grid improvements. Drones will now fly to the closest cell if trying to pathfind outside of the grid instead of crashing. Building outside of the grid might have some weird behaviour but shouldn’t cause crashes anymore
    * Removed an ensure that caused many crashes when loading a big save
    * Fixed a bug where Drones would skip a station if saving when it’s docking, causing it to take off and bring the items back again when loading
  * [Patch 0.4.0.4](/wiki/Patch_0.4.0.4 "Patch 0.4.0.4"): 
    * Potential fix for a scenario where the Drones would take a nonsensical path to their destination
    * Fixed a bug where Drones would teleport when dismantling a Drone Station they are about to dock on
    * Fixed a rare crash related to Drones
    * Fixed Drone Ports allowing duplicate names
  * [Patch 0.4.0.0](/wiki/Patch_0.4.0.0 "Patch 0.4.0.0"): Introduced



## References

  1. ↑ <https://youtu.be/NlIVwoRqjVk?t=850>
  2. ↑ <https://youtu.be/JOBcS413hwY?t=271>



  * [v](/wiki/Template:VehicleNav "Template:VehicleNav")
  * [e](https://satisfactory.wiki.gg/wiki/Template:VehicleNav?action=edit)
  * [h](https://satisfactory.wiki.gg/wiki/Template:VehicleNav?action=history)

[Transportation](/wiki/Vehicles "Vehicles")  
---  
Motor vehicles| [](/wiki/Tractor "Tractor") [Tractor](/wiki/Tractor "Tractor") • [](/wiki/Truck "Truck") [Truck](/wiki/Truck "Truck") • [](/wiki/Explorer "Explorer") [Explorer](/wiki/Explorer "Explorer") • [](/wiki/Factory_Cart "Factory Cart") [Factory Cart](/wiki/Factory_Cart "Factory Cart") • [](/wiki/Golden_Factory_Cart "Golden Factory Cart") [Golden Factory Cart](/wiki/Golden_Factory_Cart "Golden Factory Cart") • [](/wiki/Cyber_Wagon "Cyber Wagon") [Cyber Wagon](/wiki/Cyber_Wagon "Cyber Wagon") • [](/wiki/Truck_Station "Truck Station") [Truck Station](/wiki/Truck_Station "Truck Station") • [](/wiki/Drone_Port "Drone Port") [Drone Port](/wiki/Drone_Port "Drone Port") • [](/wiki/Drone "Drone") Drone  
Rail vehicles| [](/wiki/Electric_Locomotive "Electric Locomotive") [Electric Locomotive](/wiki/Electric_Locomotive "Electric Locomotive") • [](/wiki/Freight_Car "Freight Car") [Freight Car](/wiki/Freight_Car "Freight Car") • [](/wiki/Train_Station "Train Station") [Train Station](/wiki/Train_Station "Train Station") • [](/wiki/Freight_Platform "Freight Platform") [Freight Platform](/wiki/Freight_Platform "Freight Platform") • [](/wiki/Fluid_Freight_Platform "Fluid Freight Platform") [Fluid Freight Platform](/wiki/Fluid_Freight_Platform "Fluid Freight Platform") • [](/wiki/Empty_Platform "Empty Platform") [Empty Platform](/wiki/Empty_Platform "Empty Platform") • [](/wiki/Empty_Platform_With_Catwalk "Empty Platform With Catwalk") [Empty Platform With Catwalk](/wiki/Empty_Platform_With_Catwalk "Empty Platform With Catwalk") • [](/wiki/Railway "Railway") [Railway](/wiki/Railway "Railway") • [](/wiki/Railroad_Switch_Control "Railroad Switch Control") [Railroad Switch Control](/wiki/Railroad_Switch_Control "Railroad Switch Control") • [](/wiki/Buffer_Stop "Buffer Stop") [Buffer Stop](/wiki/Buffer_Stop "Buffer Stop") • [](/wiki/Block_Signal "Block Signal") [Block Signal](/wiki/Block_Signal "Block Signal") • [](/wiki/Path_Signal "Path Signal") [Path Signal](/wiki/Path_Signal "Path Signal")  
Hypertubes| [](/wiki/Hypertube "Hypertube") [Hypertube](/wiki/Hypertube "Hypertube") • [](/wiki/Hypertube_Entrance "Hypertube Entrance") [Hypertube Entrance](/wiki/Hypertube_Entrance "Hypertube Entrance") • [](/wiki/Hypertube_Support "Hypertube Support") [Hypertube Support](/wiki/Hypertube_Support "Hypertube Support") • [](/wiki/Stackable_Hypertube_Support "Stackable Hypertube Support") [Stackable Hypertube Support](/wiki/Stackable_Hypertube_Support "Stackable Hypertube Support") • [](/wiki/Hypertube_Wall_Hole "Hypertube Wall Hole") [Hypertube Wall Hole](/wiki/Hypertube_Wall_Hole "Hypertube Wall Hole") • [](/wiki/Hypertube_Wall_Support "Hypertube Wall Support") [Hypertube Wall Support](/wiki/Hypertube_Wall_Support "Hypertube Wall Support") • [](/wiki/Hypertube_Floor_Hole "Hypertube Floor Hole") [Hypertube Floor Hole](/wiki/Hypertube_Floor_Hole "Hypertube Floor Hole") • [](/wiki/Hypertube_Junction "Hypertube Junction") [Hypertube Junction](/wiki/Hypertube_Junction "Hypertube Junction") • [](/wiki/Hypertube_Branch "Hypertube Branch") [Hypertube Branch](/wiki/Hypertube_Branch "Hypertube Branch")  
Pioneer transport| [](/wiki/Jump_Pad "Jump Pad") [Jump Pad](/wiki/Jump_Pad "Jump Pad") • [](/wiki/U-Jelly_Landing_Pad "U-Jelly Landing Pad") [U-Jelly Landing Pad](/wiki/U-Jelly_Landing_Pad "U-Jelly Landing Pad") • [](/wiki/Personnel_Elevator "Personnel Elevator") [Personnel Elevator](/wiki/Personnel_Elevator "Personnel Elevator") • [](/wiki/Main_Portal "Main Portal") [Main Portal](/wiki/Main_Portal "Main Portal") • [](/wiki/Satellite_Portal "Satellite Portal") [Satellite Portal](/wiki/Satellite_Portal "Satellite Portal")
  *[v]: View this template
  *[e]: Edit this template
  *[h]: History of this template
  *[his]: his trivia section
