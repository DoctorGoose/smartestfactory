# Freight Car

## Freight Car

[ ](/wiki/File:Freight_Car.png "Freight Car.png")

_Attaches to an Electric Locomotive or other Freight Car to transport resources. Must be built on a Railway.  
Resources are loaded and unloaded at Freight Platforms.  
Has a 1600 m³ or 32-slot capacity, depending on whether resources are liquid or solid._

### Unlocked by

[Tier 6](/wiki/Tier_6 "Tier 6") \- Monorail Train Technology

### Class name

Desc_FreightWagon_C

## Vehicle

### Inventory size

32 slots or 1600 m³

## Dimensions

### Width

6 m

### Length

16 m

### Height

6 m

### Area

96 m2

## Ingre­dients

**5 ×[](/wiki/Modular_Frame "Modular Frame") [Modular Frame](/wiki/Modular_Frame "Modular Frame")**

**10 ×[](/wiki/Steel_Pipe "Steel Pipe") [Steel Pipe](/wiki/Steel_Pipe "Steel Pipe")**

**10 ×[](/wiki/Steel_Beam "Steel Beam") [Steel Beam](/wiki/Steel_Beam "Steel Beam")**

**Freight Cars** are non-motorized [vehicles](/wiki/Vehicles "Vehicles") that can be attached to [Electric Locomotives](/wiki/Electric_Locomotive "Electric Locomotive") or another Freight Car to form a train. They have a capacity of 32 item slots or 1,600 m3 for fluids and allow for the transportation of resources over [Railways](/wiki/Railway "Railway"). Freight Cars can be loaded and unloaded via [Freight Platforms](/wiki/Freight_Platform "Freight Platform") or [Fluid Freight Platforms](/wiki/Fluid_Freight_Platform "Fluid Freight Platform"). 

## Contents

  * 1 Appearance
  * 2 Weight
  * 3 Train throughput
  * 4 Trivia
  * 5 Current issues
  * 6 See also
  * 7 Gallery
  * 8 History
  * 9 Early game development
  * 10 References



## Appearance

  * If at least one item is loaded, a freight container will be shown. Items can be either loaded manually or with Freight Platforms.
  * If any fluid is loaded, a fluid tank will be shown. Fluids can be only loaded with Fluid Freight Platforms. Much like [Pipeline](/wiki/Pipeline "Pipeline") networks, a single Freight Car can only carry one type of fluid at a time. 
    * When carrying fluids, a flush option will appear similar to Pipelines. Flushing a fluid tank will remove all the fluid from the car, and the tank.
    * Only the selected car will be flushed. Other cars in the train and any Fluid Freight Platform will be unaffected.
  * A single Freight Car cannot carry fluid and items simultaneously.
  * If nothing is loaded, only the undercarriage is shown.



## Weight

An empty Freight Car weighs 30 t[1]. The weight of its payload is determined by the following factors: 

  * If any cargo is loaded at all, the weight increases by 14 t
  * For each full stack loaded, the weight increases by 1.75 t
  * For each 10m3 of fluid, the weight increases by 0.35 t



Therefore, the maximum weight of a Freight Car is 100 t while fully loaded with items or fluid. 

The table below shows the number of Freight Cars a single Locomotive can pull, depending on the incline of the Railway (plus some additional resistances) 

Note that a Locomotive weighs 300 t: 

Data | 1m Ramp  
(2m Double Ramp) | 2m Ramp  
(4m Double Ramp) | 4m Ramp*  
(8 m Double Ramp)*   
---|---|---|---  
Max. weight of Train | 1644 t | 800 t | 580 t   
Max. weight of Freight Cars | 1344 t | 500 t | 280 t   
Max. number of Freight Cars  
(empty) | 44 | 16 | 9   
Max. number of Freight Cars  
(half full) | 18 | 7 | 3   
Max. number of Freight Cars  
(fully loaded) | 13 | 5 | 2.8   
  
(*Note: Railways can't actually be constructed on 4m Ramps. Use these numbers as guideline for really steep inclines instead) 

Explanation: 

As listed on the [Electric Locomotive's section about forces](/wiki/Electric_Locomotive#Weights_and_forces "Electric Locomotive"), Locomotives have a pulling force of 2000 kN. 

Different foundations have a different angle (7.125°, 14.03° and 26.56° for 1m, 2m and 4m Ramps respectively) and so do the tracks placed on them. When a mass is on such a slope, gravity pulls it not just directly down, but also down along the slope. 

The strength of this pull is given by the formula F=m×g×sin(angle) where: 

  * F = The force acting parallel to the incline typically shown in units of Newtons (N). One kilonewton (kN) is equal to 1,000 Newtons or 1kN.
  * m = The mass of the object typically shown in units of kilograms (kg). 1 metric ton equals 1000kg. Example: One Electric Locomotive (300 metric tons) plus five fully loaded Freight Cars (500 metric tons) on a 2m Ramp = 800000kg.
  * g = The acceleration due to gravity on MASSAGE-2(A-B)b, and is 9.80665 meters per second squared (m/s²) _that can be rounded up to 9.81._
  * angle = The angle in degrees of the inclined plane with respect to the horizontal; essentially, the component of the gravitational force pulling the object down the slope.



For a full freight car weighing 100t, this force is **121.6 kN** , **237.8 kN** and **438.6 kN** , depending on the angle. 

If the total sum of these forces exceeds 2000 kN, the Locomotive can no longer accelerate forwards (as the pulling force is completely canceled by this backwards pull.) 

Additionally, trains also experience a few other resistances such as rolling resistance, drag and curve resistance, which all work against the Locomotive. 

## Train throughput

_Main article:_[Tutorial:Train throughput](/wiki/Tutorial:Train_throughput "Tutorial:Train throughput")

## Trivia

  * During the unloading animation, the crane at the (Fluid) Freight Platform will grab the container (tank) from the Freight Car and then drop at the cargo of the Freight Platform.
  * If the Freight Platform does not have enough free space to load/unload all items, a different animation will be played: 
    * When unloading a Freight Car, the container/tank will be hoisted above the Freight Platform cargo. Its door is opened from below with its contents dropped into the Platform cargo. It will then be placed back onto the Freight Car undercarriage.
    * When loading a Freight Car, the Freight Platform crane will pick up the cargo of the platform, hoist it above the Freight Car and load it similarly.
  * If a player is standing on the undercarriage and loads an item, the freight container will spawn and instantly kill the player. If a Freight Platform loads a container over a player, the player will die the same way. However, players can ride the container when it's being unloaded.
  * Unlike motor vehicles, trains do not knock down the player upon contact; instead, the train phases through.
  * While docking, freight platforms performing a loading operation will pause belts and manual interactions, but platforms that do not load or unload anything do not pause. However, all freight cars in the docked train will refuse manual interaction during the docking sequence, regardless of loading.
  * Freight Cars are the only building in the game that can be loaded with _either_ fluids or items. All others are restricted to one or the other, or else take both at once.



## Current issues

  * Dismantling a Freight Car carrying fluid will cause a [dismantle crate](/wiki/Crate "Crate") with the fluid to appear, instead of deleting the fluid much like when a [Pipeline](/wiki/Pipeline "Pipeline") or [Fluid Buffer](/wiki/Fluid_Buffer "Fluid Buffer") is dismantled. The fluid cannot be picked up into the inventory, so the only way to get rid of the crate is to drag the fluid within to the trash slot ([`Ctrl`](/wiki/Controls "Controls")+drag deletes all of the same type).
  * Loading items into an empty Freight Car while standing on the undercarriage will cause the freight container to appear over the [pioneer](/wiki/Pioneer "Pioneer"), causing instant death.



## See also

  * [Electric Locomotive](/wiki/Electric_Locomotive "Electric Locomotive")
  * [Railway](/wiki/Railway "Railway")
  * [Train Station](/wiki/Train_Station "Train Station")
  * [Freight Platform](/wiki/Freight_Platform "Freight Platform")
  * [Fluid Freight Platform](/wiki/Fluid_Freight_Platform "Fluid Freight Platform")



## Gallery

  * [](/wiki/File:Freight_Platform_E3.png "A train with four Freight Cars at Freight Platforms \(old graphic\)")

A train with four Freight Cars at Freight Platforms (old graphic)

  * [](/wiki/File:Train_setup_one_way.png "An arriving Train with two Locomotives and seven empty Freight Cars")

An arriving Train with two Locomotives and seven empty Freight Cars

  * [](/wiki/File:Freight_car_variants.png "Three Freight Cars, one empty, one with a fluid tanker, and one with a cargo container")

Three Freight Cars, one empty, one with a fluid tanker, and one with a cargo container




## History

  * [Patch 1.0](/wiki/Patch_1.0 "Patch 1.0"): 
    * Changed 4 Heavy Modular Frame cost to 5 Modular Frame
    * Added 10 Steel Beam cost
  * [Patch 0.8.2.9](/wiki/Patch_0.8.2.9 "Patch 0.8.2.9"): You can now more easily interact with [Electric Locomotives](/wiki/Electric_Locomotive "Electric Locomotive") and Freight Carts when they are docked on a [Train Station](/wiki/Train_Station "Train Station")
  * [Patch 0.5.0.6](/wiki/Patch_0.5.0.6 "Patch 0.5.0.6"): Improved interaction for Freight Car and automatic doors
  * [Patch 0.5.0.2](/wiki/Patch_0.5.0.2 "Patch 0.5.0.2") _(Released again in[Patch 0.5.0.3](/wiki/Patch_0.5.0.3 "Patch 0.5.0.3"))_: Fix for [Trains](/wiki/Trains "Trains") with carts containing fluids not being able to go up hills
  * [Patch 0.5.0.0](/wiki/Patch_0.5.0.0 "Patch 0.5.0.0"): Freight Cars now have weight based on whether and how much cargo is loaded
  * [Patch 0.3.7](/wiki/Patch_0.3.7 "Patch 0.3.7")
    * Attempt at reducing Freight Car update costs
    * Fixed tick type for Freight Cars
  * [Patch 0.3.4.14](/wiki/Patch_0.3.4.14 "Patch 0.3.4.14")
    * Trains and Freight Cars now snap better to each other at track intersections and turnouts
    * Fluid Freight Cars now display the proper capacity of the buildings in their description
    * Increased storage capacity for Fluid Freight Cars, from 500 to 1600 m3
  * [Patch 0.3.2.0](/wiki/Patch_0.3.2.0 "Patch 0.3.2.0") Fluid Freight Cars now have proper fluid UI
  * [Patch 0.3.1.1](/wiki/Patch_0.3.1.1 "Patch 0.3.1.1") Fluid Freight Cars can now handle 500 m3 of fluid instead of 50 m3
  * [Patch 0.3](/wiki/Patch_0.3 "Patch 0.3"): Now supports fluid containers and allows fluids to be transported
  * [Patch 0.1.16](/wiki/Patch_0.1.16 "Patch 0.1.16"): Are now unlockable in game



## Early game development

Prior to Closed Alpha, in Sprint 23 (week 46) trains were first shown, but there was no information about freight cars other than their availability. 

  * See also: [Game Development - Trains](/wiki/Early_game_development#Trains "Early game development")



## References

  1. ↑ Every single value is taken directly from the game using the dev [Debug Console command `ShowDebug TRAINS`](/wiki/Debug_console#ShowDebug_Parameters "Debug console").



  * [v](/wiki/Template:VehicleNav "Template:VehicleNav")
  * [e](https://satisfactory.wiki.gg/wiki/Template:VehicleNav?action=edit)
  * [h](https://satisfactory.wiki.gg/wiki/Template:VehicleNav?action=history)

[Transportation](/wiki/Vehicles "Vehicles")  
---  
Motor vehicles| [](/wiki/Tractor "Tractor") [Tractor](/wiki/Tractor "Tractor") • [](/wiki/Truck "Truck") [Truck](/wiki/Truck "Truck") • [](/wiki/Explorer "Explorer") [Explorer](/wiki/Explorer "Explorer") • [](/wiki/Factory_Cart "Factory Cart") [Factory Cart](/wiki/Factory_Cart "Factory Cart") • [](/wiki/Golden_Factory_Cart "Golden Factory Cart") [Golden Factory Cart](/wiki/Golden_Factory_Cart "Golden Factory Cart") • [](/wiki/Cyber_Wagon "Cyber Wagon") [Cyber Wagon](/wiki/Cyber_Wagon "Cyber Wagon") • [](/wiki/Truck_Station "Truck Station") [Truck Station](/wiki/Truck_Station "Truck Station") • [](/wiki/Drone_Port "Drone Port") [Drone Port](/wiki/Drone_Port "Drone Port") • [](/wiki/Drone "Drone") [Drone](/wiki/Drone "Drone")  
Rail vehicles| [](/wiki/Electric_Locomotive "Electric Locomotive") [Electric Locomotive](/wiki/Electric_Locomotive "Electric Locomotive") • [](/wiki/Freight_Car "Freight Car") Freight Car • [](/wiki/Train_Station "Train Station") [Train Station](/wiki/Train_Station "Train Station") • [](/wiki/Freight_Platform "Freight Platform") [Freight Platform](/wiki/Freight_Platform "Freight Platform") • [](/wiki/Fluid_Freight_Platform "Fluid Freight Platform") [Fluid Freight Platform](/wiki/Fluid_Freight_Platform "Fluid Freight Platform") • [](/wiki/Empty_Platform "Empty Platform") [Empty Platform](/wiki/Empty_Platform "Empty Platform") • [](/wiki/Empty_Platform_With_Catwalk "Empty Platform With Catwalk") [Empty Platform With Catwalk](/wiki/Empty_Platform_With_Catwalk "Empty Platform With Catwalk") • [](/wiki/Railway "Railway") [Railway](/wiki/Railway "Railway") • [](/wiki/Railroad_Switch_Control "Railroad Switch Control") [Railroad Switch Control](/wiki/Railroad_Switch_Control "Railroad Switch Control") • [](/wiki/Buffer_Stop "Buffer Stop") [Buffer Stop](/wiki/Buffer_Stop "Buffer Stop") • [](/wiki/Block_Signal "Block Signal") [Block Signal](/wiki/Block_Signal "Block Signal") • [](/wiki/Path_Signal "Path Signal") [Path Signal](/wiki/Path_Signal "Path Signal")  
Hypertubes| [](/wiki/Hypertube "Hypertube") [Hypertube](/wiki/Hypertube "Hypertube") • [](/wiki/Hypertube_Entrance "Hypertube Entrance") [Hypertube Entrance](/wiki/Hypertube_Entrance "Hypertube Entrance") • [](/wiki/Hypertube_Support "Hypertube Support") [Hypertube Support](/wiki/Hypertube_Support "Hypertube Support") • [](/wiki/Stackable_Hypertube_Support "Stackable Hypertube Support") [Stackable Hypertube Support](/wiki/Stackable_Hypertube_Support "Stackable Hypertube Support") • [](/wiki/Hypertube_Wall_Hole "Hypertube Wall Hole") [Hypertube Wall Hole](/wiki/Hypertube_Wall_Hole "Hypertube Wall Hole") • [](/wiki/Hypertube_Wall_Support "Hypertube Wall Support") [Hypertube Wall Support](/wiki/Hypertube_Wall_Support "Hypertube Wall Support") • [](/wiki/Hypertube_Floor_Hole "Hypertube Floor Hole") [Hypertube Floor Hole](/wiki/Hypertube_Floor_Hole "Hypertube Floor Hole") • [](/wiki/Hypertube_Junction "Hypertube Junction") [Hypertube Junction](/wiki/Hypertube_Junction "Hypertube Junction") • [](/wiki/Hypertube_Branch "Hypertube Branch") [Hypertube Branch](/wiki/Hypertube_Branch "Hypertube Branch")  
Pioneer transport| [](/wiki/Jump_Pad "Jump Pad") [Jump Pad](/wiki/Jump_Pad "Jump Pad") • [](/wiki/U-Jelly_Landing_Pad "U-Jelly Landing Pad") [U-Jelly Landing Pad](/wiki/U-Jelly_Landing_Pad "U-Jelly Landing Pad") • [](/wiki/Personnel_Elevator "Personnel Elevator") [Personnel Elevator](/wiki/Personnel_Elevator "Personnel Elevator") • [](/wiki/Main_Portal "Main Portal") [Main Portal](/wiki/Main_Portal "Main Portal") • [](/wiki/Satellite_Portal "Satellite Portal") [Satellite Portal](/wiki/Satellite_Portal "Satellite Portal")
  *[v]: View this template
  *[e]: Edit this template
  *[h]: History of this template
  *[his]: his trivia section
