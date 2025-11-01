# Train Station

[](/wiki/File:Cleanup.svg) | **This article may need cleanup to meet quality standards.** Please help [improve this](https://satisfactory.wiki.gg/wiki/Train_Station?action=edit) if you can. The [Discussion page](/wiki/Talk:Train_Station "Talk:Train Station") may contain suggestions.   
---|---  
  
**This article may need cleanup to meet quality standards.**  
Please help [improve this](https://satisfactory.wiki.gg/wiki/Train_Station?action=edit) if you can. The [Discussion page](/wiki/Talk:Train_Station "Talk:Train Station") may contain suggestions.  


## Train Station

[ ](/wiki/File:Train_Station.png "Train Station.png")

_Serves as a hub for Locomotives, which can be set to navigate to and stop at a Train Station.  
You can connect power to a Train Station to power up the trains on the Railway as well as feed power to other stations._

### Unlocked by

[Tier 6](/wiki/Tier_6 "Tier 6") \- Monorail Train Technology

### Class name

Desc_TrainStation_C

## Building

### [Power  
usage](/wiki/Power "Power")

50 MW

## Dimensions

### Width

34 m

### Length

16 m

### Height

20 m

### Area

544 m2

## Ingre­dients

**10 ×[](/wiki/Encased_Industrial_Beam "Encased Industrial Beam") [Encased Industrial Beam](/wiki/Encased_Industrial_Beam "Encased Industrial Beam")**

**50 ×[](/wiki/Plastic "Plastic") [Plastic](/wiki/Plastic "Plastic")**

**50 ×[](/wiki/Concrete "Concrete") [Concrete](/wiki/Concrete "Concrete")**

**200 ×[](/wiki/Wire "Wire") [Wire](/wiki/Wire "Wire")**

[](/wiki/File:Train_stop_dev_blog.png)

[](/wiki/File:Train_stop_dev_blog.png "Enlarge")

A train stopping at a train stop in the vehicle dev blog.

A **Train Station** is a building on the [Railway](/wiki/Railway "Railway") where [trains](/wiki/Train "Train") can be [instructed](/wiki/Vehicle#Automation "Vehicle") to stop and load/unload their contents onto adjacent [Freight Platforms.](/wiki/Freight_Platform "Freight Platform") Each station can be renamed in its UI. 

Train Stations are not constructed over an existing track. It has its own section of track that appears within the station's area. It provides a snapping point for [Freight Platforms](/wiki/Freight_Platform "Freight Platform") and is necessary for them to function. 

## Contents

  * 1 Construction
    * 1.1 Direction
    * 1.2 Bi-directional trains
  * 2 Usage
    * 2.1 Automation
    * 2.2 Stop settings
    * 2.3 Docking
    * 2.4 Power
    * 2.5 Hints
    * 2.6 Station names
  * 3 Train throughput
  * 4 Current issues
  * 5 Trivia
  * 6 See also
  * 7 Gallery
  * 8 History
  * 9 References



## Construction

  * A fully-functional Train Station requires a Train Station, and any number of [Freight Platforms](/wiki/Freight_Platform "Freight Platform"), [Fluid Freight Platforms](/wiki/Fluid_Freight_Platform "Fluid Freight Platform") or [Empty Platforms](/wiki/Empty_Platform "Empty Platform"), which can be placed after the Train Station to load or unload cargo from the train. A multiple-locomotive train only needs one Train station to stop.
  * As Freight Platform (and its fluid variant) must snap to a Train Station or other rail platforms, it is impossible to split a train station into segments: it must be in a continuous straight line, requiring the use of Empty Platforms for spacing. 
    * This makes Train Stations a unique challenge to site, as unlike other large factory buildings, a Train Station's entire footprint (which can easily exceed 100 meters in length) must be flat, with no slopes or layering into multiple floors possible.
  * If a platform is removed from the middle of the train station, the remaining platforms not connected to the train station will not load/unload. It resumes functioning if the platforms are reconnected to a station.
  * Dismantling any part of the station while a train is docking will cause all the train cars to be compressed to the available rail space next to it.
  * The Train Station provides power to all connected platforms.



### Direction

Train Stations are directional, which is indicated by arrows on the platform and the construction hologram. Additionally, the round side of the roof and the side where the name is displayed is where the front of an automatically docked locomotive will be. Trains on autopilot will only stop at the station in the specified direction, passing through when going the opposite direction. 

The attached Freight Platforms can be rotated either way to change which side the conveyor belt or pipe outputs are on. Not all Freight Platforms have to be rotated to the same side for the station to function. 

### Bi-directional trains

A bi-directional train stop is possible by attaching a rear-facing locomotive to the train stopping there, as automated locomotives do not reverse. The train can switch to using the rear facing-locomotive to pilot the train, but only if the front-facing locomotive cannot path to the destination. 

Keep in mind that if there is a way for a bi-directional train to reverse its direction, like a loop in the railroad network somewhere, it can cause the order of cars to be reversed and make the wrong items get unloaded in the wrong stations. Thus, combining bi-directional track designs with looping track designs can cause problems, and arguably single-direction looping networks become more manageable as the networks' size increases. 

The appropriate direction-facing locomotive will stop at the train station selected in its "timetable" (itinerary), but can switch direction when departing said station. Therefore, only a single end station facing away from the track is required for an end stop. Middle stations along the bi-directional line may require two stations each if loading/unloading in both directions is desirable, but otherwise a single stop is also possible. 

## Usage

### Automation

Train Stations give a 100 m pathing penalty to automated trains that pass through the station without stopping in it. This results in trains being able to travel on tracks around the station, rather than through it.[1]

### Stop settings

Individual Train Stations can have Locomotive [Stop Settings](/wiki/Electric_Locomotive#Stop_settings "Electric Locomotive") that determine what happens when trains stop at the station. 

### Docking

  * Trains on autopilot will automatically dock upon arriving at a station. Manually driven trains can be docked by positioning the first locomotive at the station, stopping, and then choosing the "Dock" option in the self-driving menu or pressing [`F`](/wiki/Controls "Controls").
  * If an automated train is passing through a station that it is not set to stop at, it will pass straight through without loading or unloading any items.
  * When a train docks, all freight cars will simultaneously load or unload based on the setting in each attached Freight Platform, _assuming there are items to move and space for them to be moved to_. The load/unload animation and process takes 27.08 seconds.
  * If there is nothing to load/unload, the animation will not be played. The train will instead stop and then immediately proceed, unless the autopilot settings for the train specify that it is to wait at the station for a set amount of time. If the train is docked manually, it will do nothing when the "Dock" option is pressed if there is nothing to load/unload. 
    * There must be a fully empty item slot for a station to perform a partial load/unload. For example, if the station is almost completely full but there's still space for half a stack of items, the freight car will still not be unloaded.
  * No manual interactions with the Freight Platform and Freight Cars are allowed during automatic loading/unloading of the cargo.
  * All belts connected to a freight platform are paused for the 27.08 seconds during loading and unloading. Items will stop entering or exiting the station.



### Power

A Train Station always consumes 50 MW regardless if a Train is docking or not. Attached Freight Platforms draw 50 MW each, but only while loading or unloading. Attached tracks will additionally function as power lines, adding other connected stations to the power network along with anything connected to those stations. 

### Hints

In the train station UI, a total of five hints can appear below the station name. The hint is chosen randomly when the UI is opened. These are: 

  * Please mind the gap between the train and the platform.
  * Be sure to have your [FICSIT](/wiki/FICSIT_Inc. "FICSIT Inc.") badge ready at all times.
  * FICSIT and its affiliates are not responsible for any delays caused by any reason, including but not limited to: [hog](/wiki/Fluffy-tailed_Hog "Fluffy-tailed Hog") attacks, [biomass](/wiki/Biomass "Biomass") on track, oncoming trains, collisions, [nuclear](/wiki/Nuclear_Power_Plant "Nuclear Power Plant") meltdowns or general situational derailment.
  * Have an efficient day!
  * Don't leave any unattended crates on the platform.



### Station names

When placed, train stations will be assigned with one randomly chosen name among the ones listed below (by default no duplicates can occurr). The station names are inspired by real-world station names and villages, and when all names are assigned the following stations are named 'Station N', where N is a number. When the number of stations built exceeds 200, all the stations built afterwards will be named 'Train Simulator'. Train Stations can be renamed at any time. 

  
As of version 1.1.1.4 (Main Branch) the preset station names are **40** : 

[**‘s-Hertogenbosch**](https://en.wikipedia.org/wiki/%27s-Hertogenbosch_railway_station "wikipedia:'s-Hertogenbosch railway station") |  | **[Bengaluru City](https://en.wikipedia.org/wiki/Bengaluru_City_railway_station "wikipedia:Bengaluru City railway station")** |  | **[Edsberg](https://en.wikipedia.org/wiki/Ed_Station "wikipedia:Ed Station")** |  | [**Grisslehamn**](https://en.wikipedia.org/wiki/Grisslehamn "wikipedia:Grisslehamn") |  | **[Ludvika](https://en.wikipedia.org/wiki/Ludvika "wikipedia:Ludvika")** |  | **[Novosibirsk](https://en.wikipedia.org/wiki/Novosibirsk_railway_station "wikipedia:Novosibirsk railway station")** |  | **[Smedjebacken](https://en.wikipedia.org/wiki/Smedjebacken "wikipedia:Smedjebacken")** |  | **[Timmersdala](https://en.wikipedia.org/wiki/Timmersdala "wikipedia:Timmersdala")**  
---|---|---|---|---|---|---|---|---|---|---|---|---|---|---  
**[Aix-en-Provence TGV](https://en.wikipedia.org/wiki/Aix-en-Provence_TGV_station "wikipedia:Aix-en-Provence TGV station")** |  | [**Borås**](https://en.wikipedia.org/wiki/Bor%C3%A5s#Railway "wikipedia:Borås") |  | **[Falun](https://en.wikipedia.org/wiki/Falun "wikipedia:Falun")** |  | [**Hamburg**](https://en.wikipedia.org/wiki/Hamburg_Hauptbahnhof "wikipedia:Hamburg Hauptbahnhof") |  | **[Lund](https://en.wikipedia.org/wiki/Lund_Central_Station "wikipedia:Lund Central Station")** |  | **[Rotterdam](https://en.wikipedia.org/wiki/Rotterdam_Centraal_station "wikipedia:Rotterdam Centraal station")** |  | **[Stångby](https://en.wikipedia.org/wiki/St%C3%A5ngby "wikipedia:Stångby")** |  | [**Venray**](https://en.wikipedia.org/wiki/Venray_railway_station "wikipedia:Venray railway station")  
**[Amsterdam](https://en.wikipedia.org/wiki/Amsterdam_Centraal_station "wikipedia:Amsterdam Centraal station")** |  | **[Borlänge](https://en.wikipedia.org/wiki/Borl%C3%A4nge "wikipedia:Borlänge")** |  | **[Gare](https://en.wikipedia.org/wiki/Gare_du_Nord "wikipedia:Gare du Nord")** |  | **[Krasnoyarsk](https://en.wikipedia.org/wiki/Krasnoyarsk_railway_station "wikipedia:Krasnoyarsk railway station")** |  | **[Milano](https://en.wikipedia.org/wiki/Milano_Centrale_railway_station "wikipedia:Milano Centrale railway station")** |  | **[Samara](https://en.wikipedia.org/wiki/Samara_railway_station "wikipedia:Samara railway station")** |  | **[Stockholm](https://en.wikipedia.org/wiki/Stockholm_Central_Station "wikipedia:Stockholm Central Station")** |  | **[Verkebäcksbron](https://sv.wikipedia.org/wiki/Verkeb%C3%A4cksbron)**  
**[Balakovo](https://en.wikipedia.org/wiki/Balakovo "wikipedia:Balakovo")** |  | [**Breda**](https://en.wikipedia.org/wiki/Breda_railway_station "wikipedia:Breda railway station") |  | **[Goes](https://en.wikipedia.org/wiki/Goes "wikipedia:Goes")** |  | **[Kyiv](https://en.wikipedia.org/wiki/Kyiv-Pasazhyrskyi_railway_station "wikipedia:Kyiv-Pasazhyrskyi railway station")** |  | **[Munroe Falls](https://en.wikipedia.org/wiki/Munroe_Falls,_Ohio "wikipedia:Munroe Falls, Ohio")** |  | **[Saratov](https://en.wikipedia.org/wiki/Saratov "wikipedia:Saratov")** |  | **[Sydney](https://en.wikipedia.org/wiki/Central_railway_station,_Sydney "wikipedia:Central railway station, Sydney")** |  | **[Wuppertal](https://en.wikipedia.org/wiki/Wuppertal_Hauptbahnhof "wikipedia:Wuppertal Hauptbahnhof")**  
**[Balti Jaam](https://en.wikipedia.org/wiki/Tallinn_Baltic_Station "wikipedia:Tallinn Baltic Station")** |  | [**Dordrecht**](https://en.wikipedia.org/wiki/Dordrecht_railway_station "wikipedia:Dordrecht railway station") |  | **[Göteborg](https://en.wikipedia.org/wiki/Gothenburg_Central_Station "wikipedia:Gothenburg Central Station")** |  | **[Lecce](https://en.wikipedia.org/wiki/Lecce_railway_station "wikipedia:Lecce railway station")** |  | **[Norrköping](https://en.wikipedia.org/wiki/Norrk%C3%B6ping_Central_Station "wikipedia:Norrköping Central Station")** |  | [**Skövde**](https://en.wikipedia.org/wiki/Sk%C3%B6vde "wikipedia:Skövde") |  | **[Tilburg](https://en.wikipedia.org/wiki/Tilburg_railway_station "wikipedia:Tilburg railway station")** |  | **[Zeewolde](https://en.wikipedia.org/wiki/Zeewolde "wikipedia:Zeewolde")**  
  
## Train throughput

_Main article:_[Tutorial:Train throughput](/wiki/Tutorial:Train_throughput "Tutorial:Train throughput")

## Current issues

  * Train Stations are always in the "idle" state (even when a train is docking), showing a yellow [Indicator Light](/wiki/Indicator_Light "Indicator Light") and consuming 0.1 MW. Their maximum consumption is still listed as 50 MW on power graphs.



## Trivia

  * In the [E3 trailer](https://www.youtube.com/watch?v=W_lmP8jYVLs), train stations were much closer to [Truck Stations](/wiki/Truck_Station "Truck Station") by appearance. They would be seemingly placed over the existing track, allowing the track to be slightly curved.
  * Some UI elements still feature the old design of trains (before their implementation in Update 2), especially the locomotive.



## See also

  * [](/wiki/Electric_Locomotive "Electric Locomotive") [Electric Locomotive](/wiki/Electric_Locomotive "Electric Locomotive")
  * [](/wiki/Freight_Car "Freight Car") [Freight Car](/wiki/Freight_Car "Freight Car")
  * [](/wiki/Railway "Railway") [Railway](/wiki/Railway "Railway")
  * [](/wiki/Freight_Platform "Freight Platform") [Freight Platform](/wiki/Freight_Platform "Freight Platform")
  * [](/wiki/Empty_Platform "Empty Platform") [Empty Platform](/wiki/Empty_Platform "Empty Platform")



## Gallery

  * [](/wiki/File:Train_station_name.png "Interact with a Train Station and name it for easier identification.")

Interact with a Train Station and name it for easier identification.

  * [](/wiki/File:Train_time_table.png "In the Train Station UI, switch to the timetable tab and set the train schedule.")

In the Train Station UI, switch to the timetable tab and set the train schedule.

  * [](/wiki/File:Freight_depot_setup.png "A train depot with multiple train stations grouped.")

A train depot with multiple train stations grouped.




## History

  * [Patch 1.1.0.4](/wiki/Patch_1.1.0.4 "Patch 1.1.0.4"): Potential fixes for crashes related to Building [Railways](/wiki/Railway "Railway") and Train Stations/[Freight Platforms](/wiki/Freight_Platform "Freight Platform") in [Multiplayer](/wiki/Multiplayer "Multiplayer")
  * [Patch 1.1.0.2](/wiki/Patch_1.1.0.2 "Patch 1.1.0.2"): Fixed train tracks being able to be branched and create [switches](/wiki/Railroad_Switch_Control "Railroad Switch Control") from the end of a Train Station or [Freight Platform](/wiki/Freight_Platform "Freight Platform") which would result in issues
  * [Patch 1.0.1.0](/wiki/Patch_1.0.1.0 "Patch 1.0.1.0"): Fixed white boxes appearing in the compass when Train Stations would be built from [Blueprints](/wiki/Blueprint "Blueprint") in some scenarios
  * [Patch 1.0.0.4](/wiki/Patch_1.0.0.4 "Patch 1.0.0.4"): Fixed an uncommon issue where rebuilding Train Stations in the same spot could freeze the game
  * [Patch 1.0.0.3](/wiki/Patch_1.0.0.3 "Patch 1.0.0.3"): Fixed issue where Train Station names wouldn’t change in [Multiplayer](/wiki/Multiplayer "Multiplayer") until closing and reopening their UI
  * [Patch 1.0](/wiki/Patch_1.0 "Patch 1.0"): Changed cost from 4 Heavy Modular Frame, 8 Computer, 50 Concrete and 25 Cable to 10 Encased Industrial Frame, 50 Plastic, 50 Concrete and 200 Wire
  * [Patch 0.8.2.9](/wiki/Patch_0.8.2.9 "Patch 0.8.2.9"): You can now more easily interact with [Electric Locomotives](/wiki/Electric_Locomotive "Electric Locomotive") and [Freight Carts](/wiki/Freight_Car "Freight Car") when they are docked on a Train Station
  * [Patch 0.8.2.0](/wiki/Patch_0.8.2.0 "Patch 0.8.2.0"): Trains are now sorted in the Train Station UI
  * [Patch 0.7.0.3](/wiki/Patch_0.7.0.3 "Patch 0.7.0.3"): Fixed [train tracks](/wiki/Railway "Railway") not being able to be placed on Train Stations
  * [Patch 0.7.0.2](/wiki/Patch_0.7.0.2 "Patch 0.7.0.2"): Fixed Train Station map not displaying the zoom in/zoom out slider
  * [Patch 0.7.0.1](/wiki/Patch_0.7.0.1 "Patch 0.7.0.1"): Fixed Train Stations showing “No Power” incorrectly
  * [Patch 0.5.2.1](/wiki/Patch_0.5.2.1 "Patch 0.5.2.1")
    * Train Stations cannot be placed inside Path blocks anymore, path signals now give a proper error message if a station is found inside a block.
    * Fixed Path signals placed right after a Train Station being incorrectly reserved by trains going to the Train Station.
    * If the timetable changes and the next Train Station changes, trains should properly re-path now.
    * Fixed timetable getting “Invalid next stop” if the current Train Station was removed when it is also the last Train Station on the list.
    * Current Train Station stop should now properly display for clients in [Multiplayer](/wiki/Multiplayer "Multiplayer") or [Dedicated servers](/wiki/Dedicated_servers "Dedicated servers").
  * [Patch 0.5.1.11](/wiki/Patch_0.5.1.11 "Patch 0.5.1.11"): Fixed [Trains](/wiki/Electric_Locomotive "Electric Locomotive") and Train Stations not showing the correct location on the [Map](/wiki/Map "Map") and [Compass](/wiki/HUD#Compass "HUD")
  * [Patch 0.5.1.4](/wiki/Patch_0.5.1.4 "Patch 0.5.1.4")
    * Fixed a bug where [Trains](/wiki/Electric_Locomotive "Electric Locomotive") docked at a Train Station could reserve [Path Signals](/wiki/Train_Signals "Train Signals") when Saving and Loading
    * Fixed a case where Trains approaching Train Stations with a Path Signal right after the station would reserve the same Path Signal over and over
  * [Patch 0.5.1.3](/wiki/Patch_0.5.1.3 "Patch 0.5.1.3"): Fixed issue where dismantling all the Stations listed in a Train timetable would make the timetable show “Invalid Next Station” until you rebuilt the Train setup
  * [Patch 0.5.0.9](/wiki/Patch_0.5.0.9 "Patch 0.5.0.9"): Fixed a rare crash when accessing the Train Station UI as [Multiplayer](/wiki/Multiplayer "Multiplayer")/[Dedicated Server](/wiki/Dedicated_Server "Dedicated Server") Client
  * [Patch 0.5.0.0](/wiki/Patch_0.5.0.0 "Patch 0.5.0.0"): 
    * Train Station UI has been updated
    * You can now assign some basic logic for what your Trains should do when they stop at a station
    * Train Station Visuals have been updated
  * [Patch 0.3.8.6](/wiki/Patch_0.3.8.6 "Patch 0.3.8.6"): Added support for Extended Latin, Cyrillic, Greek, Chinese, Japanese, and Korean characters in Train Station names
  * Unknown patch between [Patch 0.3.4.0](/wiki/Patch_0.3.4.0 "Patch 0.3.4.0") and [Patch 0.3.7](/wiki/Patch_0.3.7 "Patch 0.3.7"): The station name can now only be so long, preventing it from overflowing the name sign and hovering in mid-air
  * [Patch 0.3.4.16](/wiki/Patch_0.3.4.16 "Patch 0.3.4.16"): Fixed too large Track clearance
  * [Patch 0.3.4.15](/wiki/Patch_0.3.4.15 "Patch 0.3.4.15"): Integrated Station Track should no longer rotate separately from the main building
  * [Patch 0.3.4.14](/wiki/Patch_0.3.4.14 "Patch 0.3.4.14"): Icon updated
  * [Patch 0.3.4.13](/wiki/Patch_0.3.4.13 "Patch 0.3.4.13"): Added a few more details to Train Platform meshes
  * [Patch 0.3.4.12](/wiki/Patch_0.3.4.12 "Patch 0.3.4.12"): Added new meshes
  * [Patch 0.3.4.9](/wiki/Patch_0.3.4.9 "Patch 0.3.4.9"): 
    * Now can be dismantled and rebuilt in the same spot when adjacent to Foundations
    * Fixed clearance so Foundations can be built around the station properly
  * [Patch 0.2.1.17](/wiki/Patch_0.2.1.17 "Patch 0.2.1.17"): 
    * Train AI has changed. Trains now try to slow down to 15 km/h before approaching a station, then come to a full stop once reaching it. Trains are now forcefully stopped no matter their speed if not capable of braking sufficiently
    * Integrated train track of the station is now free to construct
  * [Patch 0.2.1.10](/wiki/Patch_0.2.1.10 "Patch 0.2.1.10"): Fixed small name input bug
  * [Patch 0.2.1.4](/wiki/Patch_0.2.1.4 "Patch 0.2.1.4"): Now appears on the map, LOD updated
  * [Patch 0.2.1.3](/wiki/Patch_0.2.1.3 "Patch 0.2.1.3"): Fixed related crash
  * [Patch 0.1.19](/wiki/Patch_0.1.19 "Patch 0.1.19"): Updated visuals, now shows station name. Added power warnings and support legs
  * [Patch 0.1.17 (101256)](/wiki/Patch_0.1.17 "Patch 0.1.17"): Power graph fixed, UI updated. Foundation 8m x 1m introduced to match platform height
  * [Patch 0.1.16](/wiki/Patch_0.1.16 "Patch 0.1.16"): Are now unlockable in game



## References

  1. ↑ [Satisfactory Q&A Post - How are train paths calculated?](https://questions.satisfactorygame.com/post/6250bd4aca608e080350be1b)



  * [v](/wiki/Template:VehicleNav "Template:VehicleNav")
  * [e](https://satisfactory.wiki.gg/wiki/Template:VehicleNav?action=edit)
  * [h](https://satisfactory.wiki.gg/wiki/Template:VehicleNav?action=history)

[Transportation](/wiki/Vehicles "Vehicles")  
---  
Motor vehicles| [](/wiki/Tractor "Tractor") [Tractor](/wiki/Tractor "Tractor") • [](/wiki/Truck "Truck") [Truck](/wiki/Truck "Truck") • [](/wiki/Explorer "Explorer") [Explorer](/wiki/Explorer "Explorer") • [](/wiki/Factory_Cart "Factory Cart") [Factory Cart](/wiki/Factory_Cart "Factory Cart") • [](/wiki/Golden_Factory_Cart "Golden Factory Cart") [Golden Factory Cart](/wiki/Golden_Factory_Cart "Golden Factory Cart") • [](/wiki/Cyber_Wagon "Cyber Wagon") [Cyber Wagon](/wiki/Cyber_Wagon "Cyber Wagon") • [](/wiki/Truck_Station "Truck Station") [Truck Station](/wiki/Truck_Station "Truck Station") • [](/wiki/Drone_Port "Drone Port") [Drone Port](/wiki/Drone_Port "Drone Port") • [](/wiki/Drone "Drone") [Drone](/wiki/Drone "Drone")  
Rail vehicles| [](/wiki/Electric_Locomotive "Electric Locomotive") [Electric Locomotive](/wiki/Electric_Locomotive "Electric Locomotive") • [](/wiki/Freight_Car "Freight Car") [Freight Car](/wiki/Freight_Car "Freight Car") • [](/wiki/Train_Station "Train Station") Train Station • [](/wiki/Freight_Platform "Freight Platform") [Freight Platform](/wiki/Freight_Platform "Freight Platform") • [](/wiki/Fluid_Freight_Platform "Fluid Freight Platform") [Fluid Freight Platform](/wiki/Fluid_Freight_Platform "Fluid Freight Platform") • [](/wiki/Empty_Platform "Empty Platform") [Empty Platform](/wiki/Empty_Platform "Empty Platform") • [](/wiki/Empty_Platform_With_Catwalk "Empty Platform With Catwalk") [Empty Platform With Catwalk](/wiki/Empty_Platform_With_Catwalk "Empty Platform With Catwalk") • [](/wiki/Railway "Railway") [Railway](/wiki/Railway "Railway") • [](/wiki/Railroad_Switch_Control "Railroad Switch Control") [Railroad Switch Control](/wiki/Railroad_Switch_Control "Railroad Switch Control") • [](/wiki/Buffer_Stop "Buffer Stop") [Buffer Stop](/wiki/Buffer_Stop "Buffer Stop") • [](/wiki/Block_Signal "Block Signal") [Block Signal](/wiki/Block_Signal "Block Signal") • [](/wiki/Path_Signal "Path Signal") [Path Signal](/wiki/Path_Signal "Path Signal")  
Hypertubes| [](/wiki/Hypertube "Hypertube") [Hypertube](/wiki/Hypertube "Hypertube") • [](/wiki/Hypertube_Entrance "Hypertube Entrance") [Hypertube Entrance](/wiki/Hypertube_Entrance "Hypertube Entrance") • [](/wiki/Hypertube_Support "Hypertube Support") [Hypertube Support](/wiki/Hypertube_Support "Hypertube Support") • [](/wiki/Stackable_Hypertube_Support "Stackable Hypertube Support") [Stackable Hypertube Support](/wiki/Stackable_Hypertube_Support "Stackable Hypertube Support") • [](/wiki/Hypertube_Wall_Hole "Hypertube Wall Hole") [Hypertube Wall Hole](/wiki/Hypertube_Wall_Hole "Hypertube Wall Hole") • [](/wiki/Hypertube_Wall_Support "Hypertube Wall Support") [Hypertube Wall Support](/wiki/Hypertube_Wall_Support "Hypertube Wall Support") • [](/wiki/Hypertube_Floor_Hole "Hypertube Floor Hole") [Hypertube Floor Hole](/wiki/Hypertube_Floor_Hole "Hypertube Floor Hole") • [](/wiki/Hypertube_Junction "Hypertube Junction") [Hypertube Junction](/wiki/Hypertube_Junction "Hypertube Junction") • [](/wiki/Hypertube_Branch "Hypertube Branch") [Hypertube Branch](/wiki/Hypertube_Branch "Hypertube Branch")  
Pioneer transport| [](/wiki/Jump_Pad "Jump Pad") [Jump Pad](/wiki/Jump_Pad "Jump Pad") • [](/wiki/U-Jelly_Landing_Pad "U-Jelly Landing Pad") [U-Jelly Landing Pad](/wiki/U-Jelly_Landing_Pad "U-Jelly Landing Pad") • [](/wiki/Personnel_Elevator "Personnel Elevator") [Personnel Elevator](/wiki/Personnel_Elevator "Personnel Elevator") • [](/wiki/Main_Portal "Main Portal") [Main Portal](/wiki/Main_Portal "Main Portal") • [](/wiki/Satellite_Portal "Satellite Portal") [Satellite Portal](/wiki/Satellite_Portal "Satellite Portal")  
  
  * [v](/wiki/Template:BuildingNav "Template:BuildingNav")
  * [e](https://satisfactory.wiki.gg/wiki/Template:BuildingNav?action=edit)
  * [h](https://satisfactory.wiki.gg/wiki/Template:BuildingNav?action=history)

[Buildings](/wiki/Buildings "Buildings")  
---  
Special| [](/wiki/The_HUB "The HUB") [The HUB](/wiki/The_HUB "The HUB") • [](/wiki/MAM "MAM") [MAM](/wiki/MAM "MAM") • [](/wiki/Space_Elevator "Space Elevator") [Space Elevator](/wiki/Space_Elevator "Space Elevator") • [](/wiki/AWESOME_Sink "AWESOME Sink") [AWESOME Sink](/wiki/AWESOME_Sink "AWESOME Sink") • [](/wiki/AWESOME_Shop "AWESOME Shop") [AWESOME Shop](/wiki/AWESOME_Shop "AWESOME Shop") • [](/wiki/Blueprint_Designer "Blueprint Designer") [Blueprint Designer](/wiki/Blueprint_Designer "Blueprint Designer") • [](/wiki/Crafting_Bench "Crafting Bench") [Crafting Bench](/wiki/Crafting_Bench "Crafting Bench") • [](/wiki/Equipment_Workshop "Equipment Workshop") [Equipment Workshop](/wiki/Equipment_Workshop "Equipment Workshop")  
Production| | Extractors| [](/wiki/Miner "Miner") [Miner Mk.1](/wiki/Miner "Miner") ([Mk.2](/wiki/Miner#Mk.2-0 "Miner"), [Mk.3](/wiki/Miner#Mk.3-0 "Miner")) • [](/wiki/Water_Extractor "Water Extractor") [Water Extractor](/wiki/Water_Extractor "Water Extractor") • [](/wiki/Oil_Extractor "Oil Extractor") [Oil Extractor](/wiki/Oil_Extractor "Oil Extractor") • [](/wiki/Resource_Well_Pressurizer "Resource Well Pressurizer") [Resource Well Pressurizer](/wiki/Resource_Well_Pressurizer "Resource Well Pressurizer") ([Extractor](/wiki/Resource_Well_Pressurizer#Extractor "Resource Well Pressurizer"))  
---|---  
Smelters| [](/wiki/Smelter "Smelter") [Smelter](/wiki/Smelter "Smelter") • [](/wiki/Foundry "Foundry") [Foundry](/wiki/Foundry "Foundry")  
Manufacturers| [](/wiki/Constructor "Constructor") [Constructor](/wiki/Constructor "Constructor") • [](/wiki/Assembler "Assembler") [Assembler](/wiki/Assembler "Assembler") • [](/wiki/Manufacturer "Manufacturer") [Manufacturer](/wiki/Manufacturer "Manufacturer") • [](/wiki/Packager "Packager") [Packager](/wiki/Packager "Packager") • [](/wiki/Refinery "Refinery") [Refinery](/wiki/Refinery "Refinery") • [](/wiki/Blender "Blender") [Blender](/wiki/Blender "Blender") • [](/wiki/Particle_Accelerator "Particle Accelerator") [Particle Accelerator](/wiki/Particle_Accelerator "Particle Accelerator") • [](/wiki/Quantum_Encoder "Quantum Encoder") [Quantum Encoder](/wiki/Quantum_Encoder "Quantum Encoder") • [](/wiki/Converter "Converter") [Converter](/wiki/Converter "Converter")  
  
[Power](/wiki/Power "Power")| | Generators| [](/wiki/Biomass_Burner "Biomass Burner") [Biomass Burner](/wiki/Biomass_Burner "Biomass Burner") • [](/wiki/Coal-Powered_Generator "Coal-Powered Generator") [Coal-Powered Generator](/wiki/Coal-Powered_Generator "Coal-Powered Generator") • [](/wiki/Fuel-Powered_Generator "Fuel-Powered Generator") [Fuel-Powered Generator](/wiki/Fuel-Powered_Generator "Fuel-Powered Generator") • [](/wiki/Geothermal_Generator "Geothermal Generator") [Geothermal Generator](/wiki/Geothermal_Generator "Geothermal Generator") • [](/wiki/Nuclear_Power_Plant "Nuclear Power Plant") [Nuclear Power Plant](/wiki/Nuclear_Power_Plant "Nuclear Power Plant") • [](/wiki/Alien_Power_Augmenter "Alien Power Augmenter") [Alien Power Augmenter](/wiki/Alien_Power_Augmenter "Alien Power Augmenter")  
---|---  
Power Grid| [](/wiki/Power_Poles "Power Poles") [Power Poles](/wiki/Power_Poles "Power Poles") • [](/wiki/Wall_Outlets "Wall Outlets") [Wall Outlets](/wiki/Wall_Outlets "Wall Outlets") • [](/wiki/Power_Tower "Power Tower") [Power Tower](/wiki/Power_Tower "Power Tower") • [](/wiki/Power_Line "Power Line") [Power Line](/wiki/Power_Line "Power Line") • [](/wiki/Power_Switch "Power Switch") [Power Switch](/wiki/Power_Switch "Power Switch") • [](/wiki/Priority_Power_Switch "Priority Power Switch") [Priority Power Switch](/wiki/Priority_Power_Switch "Priority Power Switch") • [](/wiki/Power_Storage "Power Storage") [Power Storage](/wiki/Power_Storage "Power Storage")  
  
Logistics| | Conveyors| [](/wiki/Conveyor_Belts "Conveyor Belts") [Conveyor Belts](/wiki/Conveyor_Belts "Conveyor Belts") • [](/wiki/Conveyor_Lift "Conveyor Lift") [Conveyor Lifts](/wiki/Conveyor_Lift "Conveyor Lift") • [](/wiki/Conveyor_Poles "Conveyor Poles") [Conveyor Poles](/wiki/Conveyor_Poles "Conveyor Poles") ([Stackable](/wiki/Conveyor_Poles#Stackable "Conveyor Poles"), [Wall Mount](/wiki/Conveyor_Poles#Mount "Conveyor Poles"), [Ceiling Mount](/wiki/Conveyor_Poles#Ceiling "Conveyor Poles"), {[Wall Hole](/wiki/Conveyor_Poles#Wall_Hole "Conveyor Poles"), [Floor Hole](/wiki/Conveyor_Poles#Floor_Hole "Conveyor Poles")) • [](/wiki/Conveyor_Throughput_Monitor "Conveyor Throughput Monitor") [Conveyor Throughput Monitor](/wiki/Conveyor_Throughput_Monitor "Conveyor Throughput Monitor")  
---|---  
Pipelines| [](/wiki/Pipelines "Pipelines") [Pipelines](/wiki/Pipelines "Pipelines") • [](/wiki/Pipeline_Supports "Pipeline Supports") [Pipeline Supports](/wiki/Pipeline_Supports "Pipeline Supports") ([Stackable](/wiki/Pipeline_Supports#Stackable "Pipeline Supports"), [Wall Support](/wiki/Pipeline_Supports#Wall "Pipeline Supports"), [Wall Hole](/wiki/Pipeline_Supports#Hole "Pipeline Supports"), [Floor Hole](/wiki/Pipeline_Supports#Floor "Pipeline Supports")) • [](/wiki/Pipeline_Junction "Pipeline Junction") [Pipeline Junction](/wiki/Pipeline_Junction "Pipeline Junction") • [](/wiki/Pipeline_Pump "Pipeline Pump") [Pipeline Pumps](/wiki/Pipeline_Pump "Pipeline Pump") • [](/wiki/Valve "Valve") [Valve](/wiki/Valve "Valve")  
Sorting| [](/wiki/Conveyor_Merger "Conveyor Merger") [Conveyor Merger](/wiki/Conveyor_Merger "Conveyor Merger") • [](/wiki/Priority_Merger "Priority Merger") [Priority Merger](/wiki/Priority_Merger "Priority Merger") • [](/wiki/Conveyor_Splitter "Conveyor Splitter") [Conveyor Splitter](/wiki/Conveyor_Splitter "Conveyor Splitter") • [](/wiki/Smart_Splitter "Smart Splitter") [Smart Splitter](/wiki/Smart_Splitter "Smart Splitter") • [](/wiki/Programmable_Splitter "Programmable Splitter") [Programmable Splitter](/wiki/Programmable_Splitter "Programmable Splitter")  
  
Transportation| | [Vehicle Transport](/wiki/Vehicles "Vehicles")| [](/wiki/Tractor "Tractor") [Tractor](/wiki/Tractor "Tractor") • [](/wiki/Truck "Truck") [Truck](/wiki/Truck "Truck") • [](/wiki/Cyber_Wagon "Cyber Wagon") [Cyber Wagon](/wiki/Cyber_Wagon "Cyber Wagon") • [](/wiki/Explorer "Explorer") [Explorer](/wiki/Explorer "Explorer") • [](/wiki/Factory_Cart "Factory Cart") [Factory Cart](/wiki/Factory_Cart "Factory Cart") ([Golden](/wiki/Golden_Factory_Cart "Golden Factory Cart")) • [](/wiki/Truck_Station "Truck Station") [Truck Station](/wiki/Truck_Station "Truck Station") • [](/wiki/Drone_Port "Drone Port") [Drone Port](/wiki/Drone_Port "Drone Port") • [](/wiki/Drone "Drone") [Drone](/wiki/Drone "Drone")  
---|---  
[Railway Transport](/wiki/Trains "Trains")| [](/wiki/Electric_Locomotive "Electric Locomotive") [Electric Locomotive](/wiki/Electric_Locomotive "Electric Locomotive") • [](/wiki/Freight_Car "Freight Car") [Freight Car](/wiki/Freight_Car "Freight Car") • [](/wiki/Train_Station "Train Station") Train Station • [](/wiki/Freight_Platform "Freight Platform") [Freight Platform](/wiki/Freight_Platform "Freight Platform") ([Fluid](/wiki/Freight_Platform#Fluid "Freight Platform")) • [](/wiki/Empty_Platform "Empty Platform") [Empty Platform](/wiki/Empty_Platform "Empty Platform") ([With Catwalk](/wiki/Empty_Platform_With_Catwalk "Empty Platform With Catwalk")) • [](/wiki/Railway "Railway") [Railway](/wiki/Railway "Railway") ([Railroad Switch Control](/wiki/Railroad_Switch_Control "Railroad Switch Control")) • [](/wiki/Buffer_Stop "Buffer Stop") [Buffer Stop](/wiki/Buffer_Stop "Buffer Stop") • [Train Signals](/wiki/Train_Signals "Train Signals") ([](/wiki/Train_Signals#Block "Train Signals") [Block](/wiki/Train_Signals#Block "Train Signals") • [](/wiki/Train_Signals#Path "Train Signals") [Path](/wiki/Train_Signals#Path "Train Signals"))  
Hypertubes| [](/wiki/Hypertube "Hypertube") [Hypertube](/wiki/Hypertube "Hypertube") • [](/wiki/Hypertube_Entrance "Hypertube Entrance") [Hypertube Entrance](/wiki/Hypertube_Entrance "Hypertube Entrance") • [](/wiki/Hypertube_Supports "Hypertube Supports") [Hypertube Supports](/wiki/Hypertube_Supports "Hypertube Supports") ([Stackable](/wiki/Hypertube_Supports#Stackable "Hypertube Supports"), [Wall Support](/wiki/Hypertube_Supports#Wall "Hypertube Supports"), [Wall Hole](/wiki/Hypertube_Supports#Hole "Hypertube Supports"), [Floor Hole](/wiki/Hypertube_Supports#Floor "Hypertube Supports")) • [](/wiki/Hypertube_Junction "Hypertube Junction") [Hypertube Junction](/wiki/Hypertube_Junction "Hypertube Junction") ([Branch](/wiki/Hypertube_Branch "Hypertube Branch"))  
Pioneer Transport| [](/wiki/Jump_Pad "Jump Pad") [Jump Pad](/wiki/Jump_Pad "Jump Pad") • [](/wiki/U-Jelly_Landing_Pad "U-Jelly Landing Pad") [U-Jelly Landing Pad](/wiki/U-Jelly_Landing_Pad "U-Jelly Landing Pad") • [](/wiki/Personnel_Elevator "Personnel Elevator") [Personnel Elevator](/wiki/Personnel_Elevator "Personnel Elevator") • [](/wiki/Portal "Portal") [Portal](/wiki/Portal "Portal") ([Main](/wiki/Main_Portal "Main Portal"), [Satellite](/wiki/Satellite_Portal "Satellite Portal"))  
  
Organization| [](/wiki/Lights "Lights") [Lights](/wiki/Lights "Lights") • [](/wiki/Signs "Signs") [Signs](/wiki/Signs "Signs") • [](/wiki/Crate "Crate") [Crate](/wiki/Crate "Crate") • [](/wiki/Personal_Storage_Box "Personal Storage Box") [Personal Storage Box](/wiki/Personal_Storage_Box "Personal Storage Box") ([Medical](/wiki/Personal_Storage_Box#Medical "Personal Storage Box"), [Hazard](/wiki/Personal_Storage_Box#Hazard "Personal Storage Box")) • [](/wiki/Basic_Shelf_Unit "Basic Shelf Unit") [Basic Shelf Unit](/wiki/Basic_Shelf_Unit "Basic Shelf Unit") • [](/wiki/Storage_Container "Storage Container") [Storage Container](/wiki/Storage_Container "Storage Container") ([Industrial](/wiki/Storage_Container#Industrial "Storage Container")) • [](/wiki/Dimensional_Depot_Uploader "Dimensional Depot Uploader") [Dimensional Depot Uploader](/wiki/Dimensional_Depot_Uploader "Dimensional Depot Uploader") • [](/wiki/Fluid_Buffer "Fluid Buffer") [Fluid Buffer](/wiki/Fluid_Buffer "Fluid Buffer") ([Industrial](/wiki/Fluid_Buffer#Industrial "Fluid Buffer")) • [](/wiki/Lookout_Tower "Lookout Tower") [Lookout Tower](/wiki/Lookout_Tower "Lookout Tower") • [](/wiki/Radar_Tower "Radar Tower") [Radar Tower](/wiki/Radar_Tower "Radar Tower")  
Foundations| [](/wiki/Foundations#Foundations "Foundations") [Foundations](/wiki/Foundations#Foundations "Foundations") • [](/wiki/Foundations#Ramps "Foundations") [Ramps](/wiki/Foundations#Ramps "Foundations") • [](/wiki/Foundations#Inverted_Ramps "Foundations") [Inverted Ramps](/wiki/Foundations#Inverted_Ramps "Foundations") • [](/wiki/Foundations#Quarter-Pipes "Foundations") [Quarter-Pipes](/wiki/Foundations#Quarter-Pipes "Foundations") • [](/wiki/Foundations#Half_Foundations "Foundations") [Half Foundations](/wiki/Foundations#Half_Foundations "Foundations")  
Walls| [](/wiki/Walls#Basic "Walls") [Basic Walls](/wiki/Walls#Basic "Walls") • [](/wiki/Walls#Ramp "Walls") [Ramp Walls](/wiki/Walls#Ramp "Walls") • [](/wiki/Walls#Inverted_Ramp "Walls") [Inverted Ramp Walls](/wiki/Walls#Inverted_Ramp "Walls") • [](/wiki/Walls#Tilted "Walls") [Tilted Walls](/wiki/Walls#Tilted "Walls") • [](/wiki/Walls#Windows "Walls") [Windows](/wiki/Walls#Windows "Walls") • [](/wiki/Walls#Doors "Walls") [Doors](/wiki/Walls#Doors "Walls") • [](/wiki/Walls#Conveyor "Walls") [Conveyor Walls](/wiki/Walls#Conveyor "Walls")  
Architecture| [](/wiki/Frame_Structures "Frame Structures") [Frames](/wiki/Frame_Structures "Frame Structures") • [](/wiki/Roofs "Roofs") [Roofs](/wiki/Roofs "Roofs") • [](/wiki/Beams "Beams") [Beams](/wiki/Beams "Beams") • [](/wiki/Pillars "Pillars") [Pillars](/wiki/Pillars "Pillars") • [](/wiki/Walkways "Walkways") [Walkways](/wiki/Walkways "Walkways") • [](/wiki/Walls "Walls") [Railings](/wiki/Walls "Walls") • [](/wiki/Foundations#Stairs "Foundations") [Stairs](/wiki/Foundations#Stairs "Foundations") • [](/wiki/Ladder "Ladder") [Ladder](/wiki/Ladder "Ladder") • [](/wiki/Large_Fan "Large Fan") [Large Fan](/wiki/Large_Fan "Large Fan") ([Vent](/wiki/Large_Vent "Large Vent"))
  *[v]: View this template
  *[e]: Edit this template
  *[h]: History of this template
  *[his]: his trivia section
