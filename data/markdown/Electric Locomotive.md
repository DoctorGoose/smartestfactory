# Electric Locomotive

## Electric Locomotive

[ ](/wiki/File:Electric_Locomotive.png "Electric Locomotive.png")

_Moves Freight Cars from station to station.  
Requires between 25-110 MW of power to move.   
Must be built on a Railway.  
Nicknamed 'Leif' by FICSIT pioneers because of its reliability._

### Unlocked by

[Tier 6](/wiki/Tier_6 "Tier 6") \- Monorail Train Technology

### Class name

Desc_Locomotive_C

## Vehicle

### Max speed

120 km/h

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

**10 ×[](/wiki/Motor "Motor") [Motor](/wiki/Motor "Motor")**

**20 ×[](/wiki/Steel_Pipe "Steel Pipe") [Steel Pipe](/wiki/Steel_Pipe "Steel Pipe")**

**20 ×[](/wiki/Rubber "Rubber") [Rubber](/wiki/Rubber "Rubber")**

**50 ×[](/wiki/Wire "Wire") [Wire](/wiki/Wire "Wire")**

The **Electric Locomotive** is a [vehicle](/wiki/Vehicle "Vehicle") used to transport cargo and [pioneers](/wiki/Pioneer "Pioneer") along the [Railway](/wiki/Railway "Railway"). Connected [Freight Cars](/wiki/Freight_Car "Freight Car") can be loaded or unloaded via [Freight Platforms](/wiki/Freight_Platform "Freight Platform"). The Electric Locomotive can be [automated](/wiki/Vehicle#Automation "Vehicle"), by setting a list of [Train Stations](/wiki/Train_Station "Train Station") for it to stop at. 

Multiple cargo freight cars and locomotives can be chained together to form a single train. The Locomotive is currently the fastest ground vehicle in-game, allowing for efficient long-range resource transportation. Aerial [Drones](/wiki/Drone "Drone"), unlocked at [Tier 8](/wiki/Tier_8 "Tier 8"), are twice as fast, but have their own set of advantages and disadvantages. 

## Contents

  * 1 Power consumption
  * 2 Construction
  * 3 Usage
    * 3.1 Locomotive UI
    * 3.2 Timetable
    * 3.3 Stop settings
    * 3.4 Driving
      * 3.4.1 Braking
      * 3.4.2 Speed
    * 3.5 Automation
      * 3.5.1 Pathfinding
    * 3.6 Collision
    * 3.7 Use of buffer stops
    * 3.8 Rerailing derailed trains
  * 4 Train length
  * 5 Weights and forces
  * 6 Train throughput
  * 7 Achievements
  * 8 Trivia
  * 9 Current issues
  * 10 See also
  * 11 Gallery
  * 12 History
  * 13 Early game development
  * 14 References



## Power consumption

The Electric Locomotive requires a minimum of 25 MW to operate at all times, even when it is not moving. It may draw up to 110 MW when accelerating, with the exact amount depending on how much "strain" it is under. For example, it will use more power when climbing a hill than on a level track. Likewise, it will automatically dial back the power consumption when under less strain, dropping to its minimum 25 MW when going downhill. A locomotive cannot accelerate unless the railway is powered, but it can always use its brakes. 

Note that the power consumption shown in the HUD is the sum of every locomotive's consumption on that train. A train with four locomotives may thus show 100 - 440 MW. 

By holding the key opposite of current travel direction ([`S`](/wiki/Controls "Controls") or [`W`](/wiki/Controls "Controls")) , the Locomotive will use the regenerative brake. The regenerative brake will, depending on the current speed of the locomotive, generate up to 33 MW. By subtracting the base demand of 25 MW, this results in a net power gain of up to 8 MW. 

## Construction

A locomotive can only be constructed on a railway. The face with the wind shield and cab is the front, and the side with six motors is the rear. 

The orientation of manually driven trains generally doesn't matter; they can drive in either direction at maximum velocity. 

The auto-pilot can only take control of locomotives at either end of a train and only if it is facing forwards (meaning the front of the locomotive is facing away from the rest of the train). 

In both manual and auto-pilot mode, the orientation or position of a locomotive within a train does not affect how much force it applies. Locomotives in the middle or at the end of a train also help with pushing or pulling freight cars, even when facing different directions. 

Locomotives (and Freight Cars) automatically engage their brakes without a driver in manual mode. This means they can be built on a slope without risk of rolling down. 

To add more locomotives or freight cars to a train, simply aim at the railway in front of or behind the train and the hologram will usually snap in place. Sometimes the hologram will not look like it is snapping, but building the locomotive or car will still connect it to the rest of the train if it is close enough that it _should_ snap. Dismantling cars in the middle of a train will split the train with no way to merge it back together, meaning the entire train must be rebuilt. Locomotives and cars can be added even when the train is moving, but in multiplayer sessions, this can only be done by the session's host. 

Locomotives or freight cars cannot be dismantled while moving or on an automatic schedule - only when completely stationary and with disabled auto-pilot. However, the railway beneath can still be dismantled, and the train will abruptly halt and remain floating in the air. 

## Usage

### Locomotive UI

Interacting with any Locomotive by pressing the [`E`](/wiki/Controls "Controls") key followed by the [`Q`](/wiki/Controls "Controls") key will provide access to the UI. 

You can name the Locomotive (Train) anything you want, edit the Timetable and even start the auto-pilot (self drive). 

### Timetable

Accessing the Locomotive UI will provide access to the Timetable UI for _the entire Train_. 

The Timetable includes a Map, and you can use "drag-and-drop" to set up the Timetable by dragging available Train Station right, or hover over the "+" on any available Train Station and clicking using [](/wiki/File:Keyboard_White_Mouse_Left.png "Left"). [1]

The current Timetable provides a way to adjust the settings for when trains stop at a [Train Station](/wiki/Train_Station "Train Station"). 

IMPORTANT: The Timetable must be **saved** in order for changes to take effect. 

  * [](/wiki/File:Train_Station_UI_0.png "Example of Locomotive UI showing access to Timetable UI")

Example of Locomotive UI showing access to Timetable UI

  * [](/wiki/File:Train_Station_UI_1.png "Example of Train Station Timetable UI showing drag of Train Station to Timetable")

Example of Train Station Timetable UI showing drag of Train Station to Timetable

  * [](/wiki/File:Train_Station_UI_2.png "Example of Train Station Timetable UI showing selection of Stop Settings for that Train Station")

Example of Train Station Timetable UI showing selection of Stop Settings for _that Train Station_




### Stop settings

In the Timetable UI, in the **Current Time Table** column, for a desired Train Station, you click on Gear Cog ⚙️ (on the right), which opens a new UI to allow adjusting the Stop Settings for a particular Train Station. [2]

You can, depending on individual [Freight Platform](/wiki/Freight_Platform "Freight Platform") Settings of either LOAD or UNLOAD, choose to Load / Unload everything, or Load/Unload particular Item(s) only, or do nothing at all. 

Additionally you can set an amount of time (in seconds) for the Train to WAIT before proceeding. 

The Stop Settings are **Per Train / Per Station** and _different Trains_ can have different Stop Settings. 

**⭑ IMPORTANT:** The Stop Settings AND the Timetable must be **saved** in order for Stop Settings changes to take effect. 

  * [](/wiki/File:Train_Station_UI_3.png "Example of Train Station Stop Settings UI showing default settings")

Example of Train Station Stop Settings UI showing default settings

  * [](/wiki/File:Train_Station_UI_4.png "Example of Train Station Stop Settings UI showing Load Only example")

Example of Train Station Stop Settings UI showing Load Only example

  * [](/wiki/File:Train_Station_UI_5.png "Example of Train Station Stop Settings UI showing Locomotive should stay until AI Limiters and Aluminum Ingots are fully loaded AND wait for 15 seconds")

Example of Train Station Stop Settings UI showing Locomotive should stay until AI Limiters and Aluminum Ingots are fully loaded AND wait for 15 seconds




### Driving

Interacting with any Locomotive with self-drive disabled, using the [`E`](/wiki/Controls "Controls") key, will allow you to enter it. Only Locomotives with disabled auto-pilot can be manually driven. 

While manually driving a Locomotive, pressing the [`Q`](/wiki/Controls "Controls") key will open the Timetable UI (see above). 

Holding the [`W`](/wiki/Controls "Controls") (forward) or [`S`](/wiki/Controls "Controls") (backward) directional key, the Locomotive will start applying force, slowly increasing the power consumption until that force is enough to overcome friction and the train begins to accelerate in that direction. 

The brakes release _as soon as the locomotive starts applying force_ . This means that if the train is on a hill, it will begin rolling backwards until the Locomotives pull power up enough to pull the train up the hill. 

#### Braking

  * Trains have two different braking systems: 
    * Pressing the directional key in the opposite direction ([`S`](/wiki/Controls "Controls") or [`W`](/wiki/Controls "Controls")) of travel will engage the regenerative electric brakes. A flashing UI element stating "BRAKE" will appear and the train will start dialing back power usage (and even start generating power at higher velocities). These brakes have a braking force of _600 kN_ above 80km/h and _2000 kN_ below 80 km/h.
    * Pressing the handbrake key ([`Space`](/wiki/Controls "Controls")) will engage the air brakes. They are loud and engage multiple moving parts across the train (like the air flaps and brake pads). Braking at high velocities for long enough will cause the wheels of freight cars to glow red. These brakes have a fixed braking force of _900 kN_ , regardless of train velocity.



Either brake system can be engaged separately or both can be engaged together for maximum stopping power. When driving manually, releasing the brakes will cause the train to start rolling. Exiting the train will automatically engage the brakes, and it will try to stop from rolling. It will keep braking until it receives player input again or auto-pilot is engaged and active.

[](/wiki/File:Train_speed_test.png)

[](/wiki/File:Train_speed_test.png "Enlarge")

Using a tower of [4m double ramps](/wiki/Double_Ramp_8m_x_4m "Double Ramp 8m x 4m") approximately 2400m tall, a train can reach ludicrous speed.

#### Speed

Under its own power, a Locomotive's top speed is approximately 120 km/h on a flat railway. 

Its top speed is slower when climbing a steep incline, but should always be capable of reaching at least 54 km/h so long as the train is not too heavy for the locomotives. 

When rolling downhill, it can rapidly accelerate well beyond its top speed, nearly 500 km/h given a long enough hill (see image). 

### Automation

Interacting with any Locomotive in a train using the [`E`](/wiki/Controls "Controls") key will allow you to toggle on / off the auto-pilot for the entire train. 

**Train Stations will only accept trains from one direction** , but a train can depart in either direction. 

If a train does not begin moving once a route is set, the rail may not be properly connected, have no power or the route to the next stop may be invalid (due to signals or a Train Station facing the wrong direction) 

Automated trains try to not exceed 200 km/h and will brake if they do. As they approach a station on their schedule they will slowly decelerate. If a train is unable to slow down in time as it approaches a station, it will simply come to a standstill by the time it arrives. 

All connected locomotives and freight cars are treated as a single train and share the same train schedule. 

Train schedules with only one station will not loop - once the train has stopped at the station, it will not move and complain of an "invalid path". 

At least two stations are required to make a train loop. 

#### Pathfinding

Pathfinding is done by each Locomotive on a per train basis. 

Individual [Train Signals](/wiki/Train_Signals "Train Signals") cannot change the paths trains have chosen, they can only tell the trains when they can proceed on their path or when they have to wait. However [Train Signals](/wiki/Train_Signals "Train Signals") can be used to build a one way train railway path, which then prevents the train to take this path in the wrong direction. 

A train always tries to find the shortest path to the next stop. If two paths are equal in length, the one with lower rail parts is selected. If the paths are still equal, the rail crossing decides which path is taken. Giving priority to left over middle over right path. 

The order in which the rails have been build, does not matter. The number and type of [Train Signals](/wiki/Train_Signals "Train Signals") present on the rail, does not matter. 

There is a special case when the train path passes through a [Train Station](/wiki/Train_Station "Train Station"), [Freight Platform](/wiki/Freight_Platform "Freight Platform") or [Empty Platform](/wiki/Empty_Platform "Empty Platform") that is not on the train's schedule. In this case: 

  * The number of rail parts for this path is set to 0.
  * For each [Train Station](/wiki/Train_Station "Train Station") facing the trains moving direction, a extra 100m is added to the path length.[3]



### Collision

Trains will collide (and derail at higher velocities) if their train hit-boxes clip one another. [4]

Currently, trains can only collide with other trains. When there is a collision Pioneers will be notified by a sound in the HUD and a marker on the Compass and Map showing where the Train had derailed. 

Trains will pass freely through everything else, including natural terrain, player-built structures, and even the player themselves, doing no [damage](/wiki/Damage "Damage") and losing no momentum. The sides of the train do have collision boxes, but only to prevent the pioneer from clipping through the sides. A train can not collide with itself: large trains are still able to use turnarounds which can cause the front of the train to intersect the rear without issue. 

Trains can collide with wheeled vehicles, such as [trucks](/wiki/Truck "Truck"). The train will not slow down, derail, or otherwise be effected. The hit vehicle however will be pushed, dragged, or punted depending on where its hit, how fast its hit, and the surrounding environment. Wheeled vehicles on autopilot will shortly correct back on their paths. 

### Use of buffer stops

As of [Version 1.1](/wiki/Patch_1.1.0.0 "Patch 1.1.0.0"), the use of the [Buffer Stop](/wiki/Buffer_Stop "Buffer Stop") attachment for [Railways](/wiki/Railway "Railway") and/or [Train Stations](/wiki/Train_Station "Train Station") _(that you intend to manually drive through )_ is required to prevent manually-driven trains from derailing by reaching the end of the railway. 

Manually-driven trains that run off end of railway will have to be interacted with in order to get it back on the rail, similar to how train collisions work. 

### Rerailing derailed trains

The Pioneer can rerail derailed trains [5][6] by walking up to any derailed part of the Train and pressing the [`E`](/wiki/Controls "Controls") key to rerail the Train, which will return it to the point on the railway where it originally collided. There will also be a **yellow hologram** that you can interact with using the [`E`](/wiki/Controls "Controls") Key method, should the Train wreck be inaccessible.[7]

  * [](/wiki/File:Derailed_Train_Repair.png "Update 5 - Example of repairing derailed train")

Update 5 - Example of repairing derailed train

  * [](/wiki/File:Train_Rerail_Holograms.png "Update 5 - Example of yellow train holograms at crash site")

Update 5 - Example of yellow train holograms at crash site




## Train length

A single locomotive can pull approximately 100 freight cars on a perfectly flat rail, granted that they are empty. (_See section on Weight and Forces_ _below_) 

However, even a slight incline will cause the weight of 100 cars to quickly overcome the locomotive and it will begin to roll backward. Using natural hills or building a mixture of 2m and 4m ramps, it is possible to achieve the steepest possible incline (see [](/wiki/Railway "Railway") [Railway](/wiki/Railway "Railway") for more details), but a chain of 2-meter ramps or [Double Ramps](/wiki/Double_Ramp_8m_x_2m "Double Ramp 8m x 2m") is the steepest incline that can support a railway and can be quickly and easily built.  
Due to freight cars having variable weight depending on how full they are, the number of locomotives needed varies. The steepness of the tracks also affects this. 

For Locomotive-to-Freight Car ratio, see the table on [Freight Car - Weight](/wiki/Freight_Car#Weight "Freight Car"). 

## Weights and forces

Locomotives weigh _300 t_[8]. At maximum strain, they use 110 MW and apply a force of **_2000 kN_**. The train's total weight influences acceleration. A train with one locomotive and a total weight of 2000 tons (17 full freight cars + locomotive) will accelerate at roughly 2000 kN2000 t=1 m/s2 . This means that it will reach 36 km/h after 10 seconds or 50 m. Above 60 km/h, the train will dial back the force gradually, so the total time to reach maximum speed is greater than expected. The total force applied is the sum of force from locomotives and negative slope force _minus all resistances_. 

The air brake applies a braking force of _900 kN_ (_200 kN_ on freight cars), while the regenerative brake applies a braking force of _600 kN_ above 80 km/h and _2000 kN_ below. A train's braking force is the sum of all brakes combined. 

_Brakes always oppose movement forces_ (like incline forces and the locomotive's force, as well as the train's inertia). 

Resistances influence how fast trains can go and how big they can be. Every single freight car and locomotive in a train is affected by these forces individually. Namely, these forces are: 

  * **Drag** : Also known as air resistance, this force increases the faster the train goes. It increases by the square of velocity. The Locomotive at the front will experience roughly __15 kN_ at 120 km/h;_ for every Freight Car this increases by about __5.4 kN_._
  * **Roll Resistance** : This is the friction of the wheels. For Locomotives, it is a static _4.4 kN_. For Freight Cars, it ranges from _0.4 kN_ to _1.5 kN_ , increasing with the total weight of the car.
  * **Incline Force** : This is the force experienced when on a slope. It pulls the train backwards, and is equal to total weight×9.81×sin⁡(angle). If the train is moving downhill, this force is negative and is added to locomotive force (see [Freight Car#Weight](/wiki/Freight_Car#Weight "Freight Car") for details).
  * **Curve Resistance** : As trains take curves, they experience an additional rolling resistance. This one depends on the curve radius and train velocity. It can be approximated as: 0.4×weight×velocityradius . Note that for freight cars, only their payload is accounted for. The curve radius is measured from the middle of the tracks. A quarter circle curve on 3x3 foundations has radius 22 m, a 6x6 curve has radius 46. Larger curves have smaller curve resistances.



An empty Freight Car weights _30 t_ , while a full one weights _100 t_ (the payload is 70 t, composed of the 14 t for the container and 1.75 t for each full stack). 

## Train throughput

_Main article:_[Tutorial:Train throughput](/wiki/Tutorial:Train_throughput "Tutorial:Train throughput")

## Achievements

[](/wiki/Achievements "Achievements")**[All aboard!](/wiki/Achievements#All_aboard! "Achievements")** •  _"Set up a train schedule."_

[](/wiki/Achievements "Achievements")**[Too fast, Too factory](/wiki/Achievements#Too_fast,_Too_factory "Achievements")** •  _"Move faster than 140 km/h."_

## Trivia

  * When using the horn (by pressing the left mouse button), there is a very slight chance that a steam locomotive whistle would be heard[9] instead of the normal horn. This was removed in [Patch 0.5.0.0](/wiki/Patch_0.5.0.0 "Patch 0.5.0.0") and reintroduced in [Patch 1.1.1.0](/wiki/Patch_1.1.1.0 "Patch 1.1.1.0").
  * Unlike wheeled vehicles, automated trains continue to function when submerged underwater. Manually driven trains, however, will disembark the pioneer upon entering the water.
  * Pioneers inside a train are immune to [Poison Gas](/wiki/Poison_Gas "Poison Gas") and [Radiation](/wiki/Radiation "Radiation") damage.
  * The train leans slightly when turning.
  * The general design of the locomotive appears to be an [EMD F40PH Diesel Locomotive](https://en.wikipedia.org/wiki/EMD_F40PH "wikipedia:EMD F40PH")



  


## Current issues

  * Sometimes after exiting a train, the [build menu](/wiki/Build_Gun "Build Gun") is locked. The issue can be resolved by pressing P twice, saving and loading the game, or by entering and exiting a Hyper Tube. 
    * This can be caused if the train rides through a body of water
  * If two Train Stations are built without a gap separating the two station structures (such as a Train Station, Freight Platform, Train Station, Freight Platform setup) and two trains stop one in each station, both trains will get stuck in docking until the game is reloaded.



## See also

  * [](/wiki/Freight_Car "Freight Car") [Freight Car](/wiki/Freight_Car "Freight Car")
  * [](/wiki/Railway "Railway") [Railway](/wiki/Railway "Railway")
  * [](/wiki/Train_Station "Train Station") [Train Station](/wiki/Train_Station "Train Station")
  * [](/wiki/Freight_Platform "Freight Platform") [Freight Platform](/wiki/Freight_Platform "Freight Platform")
  * [](/wiki/Empty_Platform "Empty Platform") [Empty Platform](/wiki/Empty_Platform "Empty Platform")



## Gallery

  * [](/wiki/File:Electric_Locomotive_%26_Freight_Car,_Parked.png "The Electric Locomotive with a single loaded Freight Car, as it appears in-game.")

The Electric Locomotive with a single loaded [Freight Car](/wiki/Freight_Car "Freight Car"), as it appears in-game.

  * [](/wiki/File:Electric_Train_Overpass.png "A Two-way train with three Freight Cars on elevated Railway. Notice both Locomotives are facing opposite ends.")

A Two-way train with three [Freight Cars](/wiki/Freight_Car "Freight Car") on elevated [Railway](/wiki/Railway "Railway"). Notice both Locomotives are facing opposite ends.

  * [](/wiki/File:Train_on_elevated_Railway.png "A longer one-way train on an elevated Railway. Notice both locomotives are facing the same way.")

A longer one-way train on an elevated Railway. Notice both locomotives are facing the same way.

  * [](/wiki/File:Train_timing_tutorial.png "A diagrammatic representation of timing multiple trains on the same schedule.")

A diagrammatic representation of timing multiple trains on the same schedule.

  * [](/wiki/File:Bi-Directional_Rail_System_Design_1.webp "A diagram of a rail system using bi-directional rails, showing a Train Signal setup.")

A diagram of a rail system using bi-directional rails, showing a Train Signal setup.

  * [](/wiki/File:Freight_Platform_E3.png "A docked train with crane-fed platforms seen in the E3 trailer \(old visual\).")

A docked train with crane-fed platforms seen in the E3 trailer (old visual).

  * [](/wiki/File:Train_screenshot_old.jpg "An earlier design of the locomotive and cars before the Trains and Nuclear update.")

An earlier design of the locomotive and cars before the Trains and Nuclear update.

  * [](/wiki/File:Train_on_railway_dev_blog.png "Train revealed in dev-blog.")

Train revealed in dev-blog.

  * [](/wiki/File:The_old_look_of_the_train_up_close_before_it_was_properly_implemented..png "The old look of the train up-close before it was properly implemented in the EA release.")

The old look of the train up-close before it was properly implemented in the EA release.

  * An Electric Locomotive's train horn, followed by the whistle easter egg.




## History

  * [Patch 1.1.0.2](/wiki/Patch_1.1.0.2 "Patch 1.1.0.2"): Fixed Train collision notice audio not playing
  * [Patch 1.0.0.4](/wiki/Patch_1.0.0.4 "Patch 1.0.0.4")
    * Fixed Trains rolling away in [Multiplayer](/wiki/Multiplayer "Multiplayer") if entered from a steep slope
    * Added a prompt to warn about unsaved changes in Timetables for Trains when closing the menu
  * [Patch 1.0](/wiki/Patch_1.0 "Patch 1.0"): 
    * Changed Heavy Modular Frame cost to Modular Frame
    * Changed Steel Pipe cost from 15 to 20
    * Changed 5 Computer cost to 20 Rubber
    * Added 50 Wire cost
    * Train replication rework was done. Should now be a lot better to drive around when playing in [Multiplayer](/wiki/Multiplayer "Multiplayer"), as well as watching them be self-driven there should be a significant decrease of rubber-banding overall thanks to all the improvements.
  * [Patch 0.8.3.1](/wiki/Patch_0.8.3.1 "Patch 0.8.3.1"): [Invert Look](/wiki/Settings#Controls "Settings") option now also works on [Vehicles](/wiki/Vehicles "Vehicles") and Trains
  * [Patch 0.8.2.9](/wiki/Patch_0.8.2.9 "Patch 0.8.2.9"): You can now more easily interact with Electric Locomotives and [Freight Carts](/wiki/Freight_Car "Freight Car") when they are docked on a [Train Station](/wiki/Train_Station "Train Station")
  * [Patch 0.8.2.0](/wiki/Patch_0.8.2.0 "Patch 0.8.2.0"): Locomotives should now start to brake when self driving is disabled
  * [Patch 0.8.1.0](/wiki/Patch_0.8.1.0 "Patch 0.8.1.0"): Fixed a [Train](/wiki/Train "Train") pathing issue related to duplicates in the pathfinding results. This would make it so trains would sometimes take the wrong turn at the first switch out of a [station](/wiki/Train_Station "Train Station").
  * [Patch 0.8.0.5](/wiki/Patch_0.8.0.5 "Patch 0.8.0.5"): Fixed being able to exit Locomotives while having the Train Menu UI open
  * [Patch 0.8.0.1](/wiki/Patch_0.8.0.1 "Patch 0.8.0.1"): The train scheduler has been reverted back to a stable version, some work in progress accidentally got into update 8. This caused problems in some path signal setups. Problems such as allowing a train to enter a path block without the exit being clear.
  * [Patch 0.8.0.0](/wiki/Patch_0.8.0.0 "Patch 0.8.0.0"): Fixed so trains do not have to wait 2 seconds for pathfinding (a cooldown) when loading a save. This fixed a case where a train could take a wrong turn on load if it was close enough to a switch.
  * [Patch 0.7.0.3](/wiki/Patch_0.7.0.3 "Patch 0.7.0.3")
    * Train lights should now update correctly when a train loses power
    * Train lights should now restore properly to the correct location after derailment
  * [Patch 0.6.0.10](/wiki/Patch_0.6.0.10 "Patch 0.6.0.10"): Added Lights to Electric Locomotive. Lights now actually emit light, similar to motor vehicles
  * [Patch 0.6.0.0](/wiki/Patch_0.6.0.0 "Patch 0.6.0.0"): Removed Beacon cost
  * [Patch 0.5.1.11](/wiki/Patch_0.5.1.11 "Patch 0.5.1.11")
    * Fixed some issues where automated Trains could get completely stuck (“deadlock”)
    * Fixed re-rail holograms for Trains sometimes disappearing
    * Fixed Trains and [Train Stations](/wiki/Train_Station "Train Station") not showing the correct location on the [Map](/wiki/Map "Map") and [Compass](/wiki/HUD#Compass "HUD")
  * [Patch 0.5.1.7](/wiki/Patch_0.5.1.7 "Patch 0.5.1.7")
    * Train UI now opens with [`Q`](/wiki/Controls "Controls") key by default
    * Fixed [Freight Cars](/wiki/Freight_Platform "Freight Platform") failing to load/unload correctly with the rule set to Fully Load/Unload which lead to them getting stuck in docking until force cancelled
    * Fixed [Multiplayer](/wiki/Multiplayer "Multiplayer") and [Dedicated servers](/wiki/Dedicated_servers "Dedicated servers") Clients not being able to cancel the docking sequence
  * [Patch 0.5.1.4](/wiki/Patch_0.5.1.4 "Patch 0.5.1.4")
    * Fixed a bug where Trains docked at a [Train Station](/wiki/Train_Station "Train Station") could reserve [Path Signals](/wiki/Train_Signals "Train Signals") when Saving and Loading
    * Fixed a case where Trains approaching Train Stations with a Path Signal right after the station would reserve the same Path Signal over and over
  * [Patch 0.5.1.1](/wiki/Patch_0.5.1.1 "Patch 0.5.1.1"): Fixed a bug where Trains colliding at low speed could spam particle effects, leading to poor performance and could cause the game to crash in some cases
  * [Patch 0.5.0.14](/wiki/Patch_0.5.0.14 "Patch 0.5.0.14"): Added some preventions for Trains falling out of the world when derailing
  * [Patch 0.5.0.12](/wiki/Patch_0.5.0.12 "Patch 0.5.0.12"): Holograms will be shown on top of [Railways](/wiki/Railway "Railway") so Train can be more easily re-railed when a derailing occurs and all the Trains/Carts are at least 50m away from the track
  * [Patch 0.5.0.8](/wiki/Patch_0.5.0.8 "Patch 0.5.0.8")
    * Fixed Self Driving Trains being slow when a [Multiplayer](/wiki/Multiplayer "Multiplayer") / [Dedicated Servers](/wiki/Dedicated_Servers "Dedicated Servers") Client was traveling in them
    * Fixed Train Honk not being rebindable and setting Left Mouse Button to Move Forward making the Train always honk
  * [Patch 0.5.0.6](/wiki/Patch_0.5.0.6 "Patch 0.5.0.6"): Fixed some scenarios where Trains waiting at a signal could sometimes have a collision with a Train passing by on a parallel track
  * [Patch 0.5.0.5](/wiki/Patch_0.5.0.5 "Patch 0.5.0.5"): Fixed a bug that would cause Trains to get stuck in docking forever resulting in bad performance in affected saves
  * [Patch 0.5.0.4](/wiki/Patch_0.5.0.4 "Patch 0.5.0.4")
    * Fix for the Train payload being reset on load and staying like that until the next time the train is loaded
    * Temporary fix for Trains getting stuck in Docking State, Docking animations might not work until a proper fix is applied
  * [Patch 0.5.0.2](/wiki/Patch_0.5.0.2 "Patch 0.5.0.2") _(Released again in[Patch 0.5.0.3](/wiki/Patch_0.5.0.3 "Patch 0.5.0.3"))_
    * Fixed “Press _ to dock” message getting stuck when exiting the Electric Locomotive
    * Fixed being unable to close the Locomotive Menu with [`V`](/wiki/Controls "Controls")
    * Fix for Trains with [carts containing fluids](/wiki/Freight_Car "Freight Car") not being able to go up hills
  * [Patch 0.5.0.0](/wiki/Patch_0.5.0.0 "Patch 0.5.0.0")
    * You can now press [`A`](/wiki/Controls "Controls") or [`D`](/wiki/Controls "Controls") to choose between [rails](/wiki/Railway "Railway") on an intersection while driving a Locomotive.
    * Trains will now collide with each other and can be re-railed by pressing [`E`](/wiki/Controls "Controls")
      * Trains can't collide with motor vehicles, buildings or terrain, only other trains
    * Timetables have been reworked
    * Timetable UI has been reworked, with the addition of Stop Settings
    * Now listen to Train Signals
    * A list of keybinds is now shown while driving
    * Intersections can now be switched remotely while driving
    * Now can be painted from the Customizer
    * **Undocumented Change** \- Removed Steam Whistle easter egg.
  * [Patch 0.3.6.8](/wiki/Patch_0.3.6.8 "Patch 0.3.6.8"): Fixed tick type for Electric Locomotives
  * [Patch 0.3.4.13](/wiki/Patch_0.3.4.13 "Patch 0.3.4.13"): The Trains handbrake animation will no longer end up in a spamming loop
  * [Patch 0.3.4.9](/wiki/Patch_0.3.4.9 "Patch 0.3.4.9"): Client players can now interact with Trains when the host is far away
  * [Patch 0.2.1.20](/wiki/Patch_0.2.1.20 "Patch 0.2.1.20"): Fixed Trains not receiving power on loading a game
  * [Patch 0.2.1.17](/wiki/Patch_0.2.1.17 "Patch 0.2.1.17"): Trains now auto release the brake if you jump in and apply throttle (W or S).
  * [Patch 0.2.1.16](/wiki/Patch_0.2.1.16 "Patch 0.2.1.16"): 
    * Bugfix: Trains will no longer be stuck in docking due to multiple linked stations.
    * Bugfix: Update the master locomotive for player driven train during load.
    * Bugfix: Entering a train no longer auto releases the brakes, needs manual release with space.
  * [Patch 0.2.1.15](/wiki/Patch_0.2.1.15 "Patch 0.2.1.15"): 
    * When a bidirectional train "reverses" it will now brake correctly.
    * Appending an AI controlled train doesn’t make the AI lose control over the train anymore.
    * Unmanned trains (not driven by player or AI) now automatically apply their brakes.
  * [Patch 0.2.1.14](/wiki/Patch_0.2.1.14 "Patch 0.2.1.14"): 
    * Manual docking would sometimes crash, the crash is avoided but it's likely that the train won't dock if this case occurs.
    * Crashfix: Trains sometimes crash on client or when exiting the game.
    * The reverser would be incorrectly updated for bidirectional trains causing them to not be driveable in one of the directions. This affected both player and AI.
  * [Patch 0.2.1.13](/wiki/Patch_0.2.1.13 "Patch 0.2.1.13"): 
    * You can have the AI enabled while being inside the train.
    * Self driving calculations improved for better brake prediction; this shortens the brake distances and fixes some problems going uphill or downhill.
    * Sound no longer plays when the train is not close to a player.
    * Only one AI per train; fixes the edge case where 2 AI's would try to drive the same train.
    * Trains sometimes run too fast and miss the station. This made them unreliable; now the AI brakes better and the station catches the train.
    * If a train is split in half at a switch the train is repositioned back together.
    * Fixed case where player character could get destroyed while driving a train near water.
    * Cannot use build gun after being inside a train near water.
    * Trains now save their velocity so they keep moving when loaded.
  * [Patch 0.2.1.11](/wiki/Patch_0.2.1.11 "Patch 0.2.1.11"): 
    * Train names should now be saved correctly (also for clients)
    * Trains should now be properly shown on the Compass
  * [Patch 0.2.1.3](/wiki/Patch_0.2.1.3 "Patch 0.2.1.3"): Train particle effects that build up over time and result in decreased performance now get removed properly.
  * [Patch 0.2.1.1](/wiki/Patch_0.2.1.1 "Patch 0.2.1.1"): Added sound for steam when stopping
  * [Patch 0.1.20](/wiki/Patch_0.1.20 "Patch 0.1.20"): 
    * Power consumption increased. From 15 -> 25 and max 80 -> 110
    * Fixed the bug that caused the train to abort the docking sequence prematurely
    * Fix for when 2 people try to dock the same train
    * Trains with multiple locomotives should dock properly now
    * Trains now lean in curves
  * [Patch 0.1.19](/wiki/Patch_0.1.19 "Patch 0.1.19"): 
    * Power warnings for Trains
    * Client can now kind of drive Locomotives
  * [Patch 0.1.17 build 101353](/wiki/Patch_0.1.17_build_101353 "Patch 0.1.17 build 101353"): 
    * Added docking notification while driving a train
    * Train AI no longer gets stuck when railroad is removed ahead
    * Trains can now dock in reverse
    * General improvements to the self-driving AI
    * Updated some of the Train UI
  * [Patch 0.1.17](/wiki/Patch_0.1.17 "Patch 0.1.17"): Trains should no longer get stuck if they don’t have any valid Freight Platforms
  * [Patch 0.1.16](/wiki/Patch_0.1.16 "Patch 0.1.16"): Introduced



## Early game development

Prior to Closed Alpha, in Sprint 23 (week 46) trains were first shown, to include an early extremely basic version of the Electric Locomotive. 

  * See also: [Game Development - Trains](/wiki/Early_game_development#Trains "Early game development")



## References

  1. ↑ [YouTube - Update 5 Trains Collisions, Signals, New "Stop Settings" & more - Train Timetable UI Changes](https://www.youtube.com/watch?v=CskxkIepX6Y&t=889s)
  2. ↑ [YouTube - Update 5 Trains Collisions, Signals, New "Stop Settings" & more - New "Stop Settings" Feature](https://youtu.be/CskxkIepX6Y?t=911s)
  3. ↑ [Satisfactory Q&A Post - How are train paths calculated?](https://questions.satisfactorygame.com/post/6250bd4aca608e080350be1b)
  4. ↑ [YouTube - Update 5 Trains Collisions, Signals, New "Stop Settings" & more - Train Collisions](https://youtu.be/CskxkIepX6Y?t=163s)
  5. ↑ [YouTube - Update 5 Trains Collisions, Signals, New "Stop Settings" & more - Repairing de-railed trains (General)](https://youtu.be/CskxkIepX6Y?t=202s)
  6. ↑ [YouTube - Update 5 Trains Collisions, Signals, New "Stop Settings" & more - Repairing derailed trains (Steps)](https://youtu.be/CskxkIepX6Y?t=240s)
  7. ↑ [YouTube - Update 5 Trains Collisions, Signals, New "Stop Settings" & more - Repairing de-railed trains (Inaccessible)](https://youtu.be/CskxkIepX6Y?t=285s)
  8. ↑ Every single value is taken directly from the game using the dev [Debug Console command `ShowDebug TRAINS`](/wiki/Debug_console#ShowDebug_Parameters "Debug console").
  9. ↑ [YouTube - Satisfactory train steam whistle sound](https://www.youtube.com/watch?v=yMwMj7e6DEc)



  * [v](/wiki/Template:VehicleNav "Template:VehicleNav")
  * [e](https://satisfactory.wiki.gg/wiki/Template:VehicleNav?action=edit)
  * [h](https://satisfactory.wiki.gg/wiki/Template:VehicleNav?action=history)

[Transportation](/wiki/Vehicles "Vehicles")  
---  
Motor vehicles| [](/wiki/Tractor "Tractor") [Tractor](/wiki/Tractor "Tractor") • [](/wiki/Truck "Truck") [Truck](/wiki/Truck "Truck") • [](/wiki/Explorer "Explorer") [Explorer](/wiki/Explorer "Explorer") • [](/wiki/Factory_Cart "Factory Cart") [Factory Cart](/wiki/Factory_Cart "Factory Cart") • [](/wiki/Golden_Factory_Cart "Golden Factory Cart") [Golden Factory Cart](/wiki/Golden_Factory_Cart "Golden Factory Cart") • [](/wiki/Cyber_Wagon "Cyber Wagon") [Cyber Wagon](/wiki/Cyber_Wagon "Cyber Wagon") • [](/wiki/Truck_Station "Truck Station") [Truck Station](/wiki/Truck_Station "Truck Station") • [](/wiki/Drone_Port "Drone Port") [Drone Port](/wiki/Drone_Port "Drone Port") • [](/wiki/Drone "Drone") [Drone](/wiki/Drone "Drone")  
Rail vehicles| [](/wiki/Electric_Locomotive "Electric Locomotive") Electric Locomotive • [](/wiki/Freight_Car "Freight Car") [Freight Car](/wiki/Freight_Car "Freight Car") • [](/wiki/Train_Station "Train Station") [Train Station](/wiki/Train_Station "Train Station") • [](/wiki/Freight_Platform "Freight Platform") [Freight Platform](/wiki/Freight_Platform "Freight Platform") • [](/wiki/Fluid_Freight_Platform "Fluid Freight Platform") [Fluid Freight Platform](/wiki/Fluid_Freight_Platform "Fluid Freight Platform") • [](/wiki/Empty_Platform "Empty Platform") [Empty Platform](/wiki/Empty_Platform "Empty Platform") • [](/wiki/Empty_Platform_With_Catwalk "Empty Platform With Catwalk") [Empty Platform With Catwalk](/wiki/Empty_Platform_With_Catwalk "Empty Platform With Catwalk") • [](/wiki/Railway "Railway") [Railway](/wiki/Railway "Railway") • [](/wiki/Railroad_Switch_Control "Railroad Switch Control") [Railroad Switch Control](/wiki/Railroad_Switch_Control "Railroad Switch Control") • [](/wiki/Buffer_Stop "Buffer Stop") [Buffer Stop](/wiki/Buffer_Stop "Buffer Stop") • [](/wiki/Block_Signal "Block Signal") [Block Signal](/wiki/Block_Signal "Block Signal") • [](/wiki/Path_Signal "Path Signal") [Path Signal](/wiki/Path_Signal "Path Signal")  
Hypertubes| [](/wiki/Hypertube "Hypertube") [Hypertube](/wiki/Hypertube "Hypertube") • [](/wiki/Hypertube_Entrance "Hypertube Entrance") [Hypertube Entrance](/wiki/Hypertube_Entrance "Hypertube Entrance") • [](/wiki/Hypertube_Support "Hypertube Support") [Hypertube Support](/wiki/Hypertube_Support "Hypertube Support") • [](/wiki/Stackable_Hypertube_Support "Stackable Hypertube Support") [Stackable Hypertube Support](/wiki/Stackable_Hypertube_Support "Stackable Hypertube Support") • [](/wiki/Hypertube_Wall_Hole "Hypertube Wall Hole") [Hypertube Wall Hole](/wiki/Hypertube_Wall_Hole "Hypertube Wall Hole") • [](/wiki/Hypertube_Wall_Support "Hypertube Wall Support") [Hypertube Wall Support](/wiki/Hypertube_Wall_Support "Hypertube Wall Support") • [](/wiki/Hypertube_Floor_Hole "Hypertube Floor Hole") [Hypertube Floor Hole](/wiki/Hypertube_Floor_Hole "Hypertube Floor Hole") • [](/wiki/Hypertube_Junction "Hypertube Junction") [Hypertube Junction](/wiki/Hypertube_Junction "Hypertube Junction") • [](/wiki/Hypertube_Branch "Hypertube Branch") [Hypertube Branch](/wiki/Hypertube_Branch "Hypertube Branch")  
Pioneer transport| [](/wiki/Jump_Pad "Jump Pad") [Jump Pad](/wiki/Jump_Pad "Jump Pad") • [](/wiki/U-Jelly_Landing_Pad "U-Jelly Landing Pad") [U-Jelly Landing Pad](/wiki/U-Jelly_Landing_Pad "U-Jelly Landing Pad") • [](/wiki/Personnel_Elevator "Personnel Elevator") [Personnel Elevator](/wiki/Personnel_Elevator "Personnel Elevator") • [](/wiki/Main_Portal "Main Portal") [Main Portal](/wiki/Main_Portal "Main Portal") • [](/wiki/Satellite_Portal "Satellite Portal") [Satellite Portal](/wiki/Satellite_Portal "Satellite Portal")
  *[v]: View this template
  *[e]: Edit this template
  *[h]: History of this template
  *[his]: his trivia section
