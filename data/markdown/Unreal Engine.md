# Unreal Engine

[](/wiki/File:Cleanup.svg) | **This article may need cleanup to meet quality standards.** Please help [improve this](https://satisfactory.wiki.gg/wiki/Unreal_Engine?action=edit) if you can. The [Discussion page](/wiki/Talk:Unreal_Engine?action=edit&redlink=1 "Talk:Unreal Engine \(page does not exist\)") may contain suggestions.  
Reason: "_Wording and casing_ "   
---|---  
  
**This article may need cleanup to meet quality standards.**  
Please help [improve this](https://satisfactory.wiki.gg/wiki/Unreal_Engine?action=edit) if you can. The [Discussion page](/wiki/Talk:Unreal_Engine?action=edit&redlink=1 "Talk:Unreal Engine \(page does not exist\)") may contain suggestions.  
Reason: "_Wording and casing_ "

_Satisfactory_ is developed in **Unreal Engine** , which comprises a series of 3D computer graphics game engines developed by Epic Games. 

Development started with version 4.16–4.18 in the Closed Alpha.[1] The game stayed on Unreal Engine 4 up until [Patch 0.8.0.0](/wiki/Patch_0.8.0.0 "Patch 0.8.0.0"), when it was ported to Unreal Engine 5. 

## Contents

  * 1 Unreal Engine features
    * 1.1 Nanite
      * 1.1.1 Usage
      * 1.1.2 Examples
    * 1.2 Global Illumination (Lumen)
      * 1.2.1 Usage
      * 1.2.2 Examples
    * 1.3 Virtual Shadow Maps (VSM)
    * 1.4 World Partitioning System (WPS)
      * 1.4.1 Usage
    * 1.5 Temporal Super Resolution (TSR)
    * 1.6 Fast Approximate Anti-Aliasing (FXAA)
    * 1.7 Nvidia DLSS, Intel ExSS, AMD FSR
    * 1.8 Chaos Physics System
      * 1.8.1 Usage
    * 1.9 Enhanced Input System (EIS)
    * 1.10 Game audio
  * 2 Unreal Engine UObject Limit
    * 2.1 Abstract Instances
    * 2.2 Lightweight Actors
    * 2.3 UObject Game Crash
    * 2.4 UObject Limit Increase
  * 3 Engine usage history
  * 4 Trivia
  * 5 Current issues
  * 6 See also
  * 7 Gallery
  * 8 History
  * 9 References
    * 9.1 Unreal Engine Chaos Physics
    * 9.2 Unreal Engine Documentation



## Unreal Engine features

### Nanite

The word Nanite is derived from the prefix "Nano" meaning one-billionth, referring to the fact that Unreal Engine Version 5 can handle polygons in the billions[2] versus polygons in the millions using Unreal Engine 4.xx. 

The formal name for Nanite is **Nanite Virtualized Geometry**[Doc 1] which comes with the following benefits: 

  * Multiple orders of magnitude increase in geometry complexity, higher triangle and objects counts than has been possible before in real-time
  * Frame budgets are no longer constrained by polycounts, draw calls, and mesh memory usage
  * Now possible to directly import film-quality source arts, such as ZBrush sculpts and photogrammetry scans
  * Use high-poly detailing rather than baking detail into normal map textures
  * Level of Detail (LOD) is automatically handled and no longer requires manual setup for individual mesh's LODs
  * Loss of quality is rare or non-existent, especially with LOD transitions



#### Usage

Nanite in Satisfactory is currently mainly used on Rocks, Cliffs items _(see Examples below)._[3]

While possible in Unreal Engine 5, Nanite won't mostly be used on foliage, but IS USED in Satisfactory on "Static Foliage" like the Titan Trees in the [Titan Forest Biome](/wiki/World#Titan_Forest "World") _(see Examples below)._[4]

Nanite on "factory elements" is currently NOT being used but may be added later. 

#### Examples

The first 4 images are "paired" and can be toggled back and forth to see the changes. 

  * [](/wiki/File:Comparison_4_-_Dune_Desert_-_U7.png "Dune Desert Biome of Patch 0.7.1.1 using UE 4.26.2 \(Nanite not used\)")

Dune Desert Biome of [Patch 0.7.1.1](/wiki/Patch_0.7.1.1 "Patch 0.7.1.1") using UE 4.26.2 (Nanite not used)

  * [](/wiki/File:Comparison_4_-_Dune_Desert_-_U8.png "Dune Desert Biome as of Patch 0.8.0.0 using UE 5.1.1 \(Nanite used\)")

Dune Desert Biome as of [Patch 0.8.0.0](/wiki/Patch_0.8.0.0 "Patch 0.8.0.0") using UE 5.1.1 (Nanite used)

  * [](/wiki/File:Nanite_-_Dune_Desert_Biome_1.png "Dune Desert Biome - Use of Nanite \(In-Game\) using UE 5.1.1 \(Example 1\)")

Dune Desert Biome - Use of Nanite (In-Game) using UE 5.1.1 (Example 1)

  * [](/wiki/File:Nanite_-_Dune_Desert_Biome_2.png "Dune Desert Biome - Use of Nanite \(UE Editor\) using UE 5.1.1 \(Example 2\)")

Dune Desert Biome - Use of Nanite (UE Editor) using UE 5.1.1 (Example 2)

  * [](/wiki/File:Nanite_-_Titan_Forest_1.png "Titan Forest Biome - Use of Nanite on Static Foliage \(UE Editor\) using UE 5.1.1 \(Example 1\)")

Titan Forest Biome - Use of Nanite on Static Foliage (UE Editor) using UE 5.1.1 (Example 1)

  * [](/wiki/File:Nanite_-_Titan_Forest_2.png "Titan Forest Biome - Use of Nanite on Static Foliage \(UE Editor\) using UE 5.1.1 \(Example 2\)")

Titan Forest Biome - Use of Nanite on Static Foliage (UE Editor) using UE 5.1.1 (Example 2)




### Global Illumination (Lumen)

The word Lumen is derived from the word "Illuminate" meaning make (something) visible or bright by shining light on it; light up. 

The formal name for Lumen is **Lumen Global Illumination and Reflections**[Doc 2] which comes with the following benefits: 

  * Ability to render in a lower resolution and upscale to a higher display resolution in order to increase performance (FPS).
  * Ability to push render computations to supported GPU's freeing up the CPU for other things.



#### Usage

Lumen in Satisfactory **is not officially supported** , and by default is turned off[5], but can be optionally turned on by the Player in [Settings](/wiki/Settings "Settings"). 

Lumen in Satisfactory currently uses the Software Raytracing Method and as such will run on your CPU (not the GPU)[6] which is why it is turned off by default. 

Currently there are no plans to spend much time making the game optimized to work with Lumen. **The game will run better without Lumen than with Lumen turned on.**

The use of Lumen away from factories, out in the world, often doesn't result in significant differences between having it turned off or turned on as compared to the use of Lumen near or within factories where the difference between Lumen being off versus being on is significant _(see Examples below)._

In [Patch 0.8.0.0](/wiki/Patch_0.8.0.0 "Patch 0.8.0.0") through [Patch 0.8.1.0](/wiki/Patch_0.8.1.0 "Patch 0.8.1.0") the use of Lumen within factories appeared very dark depending on available lighting. As of [Patch 0.8.1.1](/wiki/Patch_0.8.1.1 "Patch 0.8.1.1") Lumen was improved resulting in more illuminated and natural factory interiors _(see Examples below)._

#### Examples

The following example images are "paired" and can be toggled back and forth to see the changes. 

1\. Outside away from factories example uses of Lumen in Satisfactory: 

  * [](/wiki/File:Lumen_Test_1_-_Off.png "Western Dune Forest Biome as of Patch 0.8.0.0 using UE 5.1.1 \(Lumen Off\)")

Western Dune Forest Biome as of [Patch 0.8.0.0](/wiki/Patch_0.8.0.0 "Patch 0.8.0.0") using UE 5.1.1 (Lumen Off)

  * [](/wiki/File:Lumen_Test_1_-_On.png "Western Dune Forest Biome as of Patch 0.8.0.0 using UE 5.1.1 \(Lumen On\)")

Western Dune Forest Biome as of [Patch 0.8.0.0](/wiki/Patch_0.8.0.0 "Patch 0.8.0.0") using UE 5.1.1 (Lumen On)

  * [](/wiki/File:Lumen_Test_2_-_Off.png "Eastern Dune Forest Biome as of Patch 0.8.0.0 using UE 5.1.1 \(Lumen Off\)")

Eastern Dune Forest Biome as of [Patch 0.8.0.0](/wiki/Patch_0.8.0.0 "Patch 0.8.0.0") using UE 5.1.1 (Lumen Off)

  * [](/wiki/File:Lumen_Test_2_-_On.png "Eastern Dune Forest Biome as of Patch 0.8.0.0 using UE 5.1.1 \(Lumen On\)")

Eastern Dune Forest Biome as of [Patch 0.8.0.0](/wiki/Patch_0.8.0.0 "Patch 0.8.0.0") using UE 5.1.1 (Lumen On)

  * [](/wiki/File:Lumen_Test_3_-_Off.png "Southern Forest Biome at night as of Patch 0.8.0.0 using UE 5.1.1 \(Lumen Off\)")

Southern Forest Biome at night as of [Patch 0.8.0.0](/wiki/Patch_0.8.0.0 "Patch 0.8.0.0") using UE 5.1.1 (Lumen Off)

  * [](/wiki/File:Lumen_Test_3_-_On.png "Southern Forest Biome at night as of Patch 0.8.0.0 using UE 5.1.1 \(Lumen On\)")

Southern Forest Biome at night as of [Patch 0.8.0.0](/wiki/Patch_0.8.0.0 "Patch 0.8.0.0") using UE 5.1.1 (Lumen On)

  * [](/wiki/File:Lumen_Test_4_-_Off.png "Grass Fields Biome as of Patch 0.8.0.0 using UE 5.1.1 \(Lumen Off\)")

Grass Fields Biome as of [Patch 0.8.0.0](/wiki/Patch_0.8.0.0 "Patch 0.8.0.0") using UE 5.1.1 (Lumen Off)

  * [](/wiki/File:Lumen_Test_4_-_On.png "Grass Fields Biome as of Patch 0.8.0.0 using UE 5.1.1 \(Lumen On\)")

Grass Fields Biome as of [Patch 0.8.0.0](/wiki/Patch_0.8.0.0 "Patch 0.8.0.0") using UE 5.1.1 (Lumen On)




2\. Near or within factories example uses of Lumen in Satisfactory: 

  * [](/wiki/File:Lumen_Test_5_-_Off.png "Example 1 - Inside Factory as of Patch 0.8.0.0 using UE 5.1.1 \(Lumen Off\)")

Example 1 - Inside Factory as of [Patch 0.8.0.0](/wiki/Patch_0.8.0.0 "Patch 0.8.0.0") using UE 5.1.1 (Lumen Off)

  * [](/wiki/File:Lumen_Test_5_-_On.png "Example 1 - Inside Factory as of Patch 0.8.0.0 using UE 5.1.1 \(Lumen On\)")

Example 1 - Inside Factory as of [Patch 0.8.0.0](/wiki/Patch_0.8.0.0 "Patch 0.8.0.0") using UE 5.1.1 (Lumen On)

  * [](/wiki/File:Lumen_Test_6_-_Off.png "Example 2 - Inside Factory as of Patch 0.8.0.0 using UE 5.1.1 \(Lumen Off\)")

Example 2 - Inside Factory as of [Patch 0.8.0.0](/wiki/Patch_0.8.0.0 "Patch 0.8.0.0") using UE 5.1.1 (Lumen Off)

  * [](/wiki/File:Lumen_Test_6_-_On.png "Example 2 - Inside Factory as of Patch 0.8.0.0 using UE 5.1.1 \(Lumen On\)")

Example 2 - Inside Factory as of [Patch 0.8.0.0](/wiki/Patch_0.8.0.0 "Patch 0.8.0.0") using UE 5.1.1 (Lumen On)

  * [](/wiki/File:Lumen_-_Patch_0810.png "Lumen Example - Inside Factory as of Patch 0.8.1.0 using UE 5.1.1 \(Lumen On\)")

Lumen Example - Inside Factory as of [Patch 0.8.1.0](/wiki/Patch_0.8.1.0 "Patch 0.8.1.0") using UE 5.1.1 (Lumen On)

  * [](/wiki/File:Lumen_-_Patch_0811.png "Lumen Example - Inside Factory as of Patch 0.8.1.1 using UE 5.1.1 \(Lumen On\)")

Lumen Example - Inside Factory as of [Patch 0.8.1.1](/wiki/Patch_0.8.1.1 "Patch 0.8.1.1") using UE 5.1.1 (Lumen On)




### Virtual Shadow Maps (VSM)

Virtual Shadow Maps (VSM) as of Unreal Engine 5.3 are now considered production ready. Despite that, there are no plans to included it in the game. Perhaps in the future it will be.[7][8]

### World Partitioning System (WPS)

In Unreal Engine 4.xx Satisfactory game used a World Grid System (WGS), comprised of 7 by 6 "tiles". There was a known "lag issue" with the WGS that occurs when the Pioneer approached the boundary of a "map tile" due to the Game having to load in the "all assets" of the next "map tile".[9]

Starting in Unreal Engine 5, the Satisfactory game began using the World Partitioning System (WPS)[Doc 3][10] which is a vast improvement over the old Level Streaming System used prior and eliminated the need to tie Actors[Doc 4] (individual "objects") to an individual tile. 

#### Usage

The WPS removed the previous need to divide large levels into sublevels by storing the world in a single persistent level separated into grid cells, and provides the game with an automatic streaming system to load and unload those cells based on distance from a streaming source. 

Since Actors (individual "objects") are not tied to a specific "map tile", but instead tied to a "grid coordinate / location", CSS now has the ability to break up the Map into smaller chunks thereby reducing Game Lag at "world map chuck borders" and ability to find the most efficient "tile / chunk size".[11]

There may be a game setting added in the future which will enable Players to reduce the size of "Map Chunks" as a way to improve game performance even further. 

### Temporal Super Resolution (TSR)

Temporal Super Resolution (TSR)[Doc 5] will enable lower resolutions appear crisp at higher resolutions with no loss in quality[12] which is similar to Nvidia DLSS and AMD FSR. 

Using TSR provides the ability to rendered frames approach the quality of native 4K with input resolutions as low as 1080p. 

Players using TSR will be able to offload rendering to their GPU versus using the CPU to do the rendering calculations. 

### Fast Approximate Anti-Aliasing (FXAA)

Fast Approximate Anti-Aliasing (FXAA)[Doc 6] is a spatial-only anti-aliasing technique that is a post-processing effect that uses a high contrast filter to find edges and smooth them by blending (dithering) between the pixel edges. As the name suggests for this technique, it is fast to render and well-suited for low-end devices and desktops. 

FXAA will be an option for Players to use if they can't effectively use TSR.[13]

### Nvidia DLSS, Intel ExSS, AMD FSR

Satisfactory game [Patch 0.8.1.0](/wiki/Patch_0.8.1.0 "Patch 0.8.1.0") added additional upscaling support[14] for Nvidia Deep Learning Super Sampling (DLSS) Technology[Doc 7] (Version 1, 2, and 3), and Intel® Arc™ Xe Super Sampling (XeSS)[Doc 8]. 

AMD FidelityFX™ Super Resolution (FSR)[Doc 9] was added in [Patch 0.8.2.4](/wiki/Patch_0.8.2.4 "Patch 0.8.2.4") as planned.[15]

Players using Nvidia DLSS, Intel ExSS, AMD FSR will be able to offload rendering to their GPU versus using the CPU to do the rendering calculations. 

### Chaos Physics System

In Unreal Engine 5 the Satisfactory moved to the **Chaos Physics System**[Doc 10] which was a quantum improvement over the **PhysX System** used in Unreal Engine 4.xx. 

While the Chaos Physics System is used for all physic simulations in the game, the main area it is being used is in the **Vehicle Physics System** which was completely overhauled.[Chaos 1]

#### Usage

[Motor Vehicles](/wiki/Vehicles#Motor_vehicles "Vehicles") now act / perform different than they did in Unreal Engine 4.xx. 

The use of UE 5 Chaos Physics has eliminated the Vehicle Bouncing Issue on Foundations but there may be some slight issue on ramps that will be fixed at some point.[Chaos 2]

Motor Vehicles top speed and handling have changed.[Chaos 3]

  * [Tractor](/wiki/Tractor "Tractor") (aka "Suger Cube") is a bit faster.
  * [Trucks](/wiki/Truck "Truck") feel more "heavy" and less "bouncy".
  * [Explorer](/wiki/Explorer "Explorer") feels more "zippy".
  * [Factory Cart](/wiki/Factory_Cart "Factory Cart") is less prone to flipping over but still by design only works well on Foundations.



The use of the Vehicle Hand Break [`Space`](/wiki/Controls "Controls") now shows real "force" when braking in Vehicles.[Chaos 4]

Vehicle Air Control was removed since this ability was not used a lot.[Chaos 5] Those whom want it back should posted that on the [Satisfactory Q&A Website](https://questions.satisfactorygame.com/search?sort=1). 

[Trains](/wiki/Train "Train") did not see any physic changes as the result of the Upgrade to Unreal Engine 5.[Chaos 6]

### Enhanced Input System (EIS)

With Unreal Engine 5 the Satisfactory game began using the **Enhanced Input System (EIS)**.[Doc 11]

The Enhanced Input System improved how keybinding works depending on what is happening in the game, and eliminate current "input bugs" like constant up flying when using the [Hover Pack](/wiki/Hover_Pack "Hover Pack").[16]

### Game audio

With Unreal Engine 5 there is the ability to use **MetaSounds**[Doc 12] high-performance audio system. **Satisfactory game won't use it.** Game will continue to use [Wwise](https://www.audiokinetic.com/en/products/wwise/) for all sound / audio related production.[17]

In Unreal Engine 5 the [Motor Vehicles](/wiki/Vehicles#Motor_vehicles "Vehicles") in Satisfactory have new sounds. When Vehicles are being driven, their sounds will be more natural _based upon what is happening_. When not driving a Vehicle, the sounds the Pioneer hears are simpler for optimization purposes.[Chaos 7]

[Version 1.1](/wiki/Patch_1.1.0.0 "Patch 1.1.0.0") added several audio improvements: 

  * **Dynamic Occlusion System:** Factory sounds will now be occluded and muffled if they are behind walls or other obstacles (like foundations). Different buildings will also change the way the sounds occlude, for example, glass or metal.
  * **Audio Indoor Detection System:** Factory and player sounds will now behave differently if the player is indoors, The HUB now has a unique audio setup as well
  * **Local Acoustic Context:** Player related sounds will now change dynamically depending on your surroundings for example high ceilings, tight corridors or inside caves.
  * **Voice Chat Attenuation:** Voice has different strength levels adjustable in [Settings](/wiki/Settings "Settings"). Attenuation now uses mid-side stereo positioning rather than just ducking specific frequencies



## Unreal Engine UObject Limit

The **Unreal Engine UObject Limit** is a limit of UObjects[Doc 13] which can be loaded in the game. 

The default limit set in the Unreal Engine is **2,162,688 UObjects**. The UObject limit is imposed from Unreal Engine's memory management implementation[18] and refers to data objects, not in-game objects. This default limit was not changed in Unreal Engine Version 5.[19]

For Satisfactory game development, the UObject limit has been **increased in the editor** but not for built games used by Players.[20]

### Abstract Instances

In [Update 7](/wiki/Patch_0.7.0.0 "Patch 0.7.0.0") Satisfactory began using _Abstract Instances_ that reduced the number of UObjects used per "object". For example, in the Update 6 or earlier a Foundation would have used 3 UObjects, however in Update 7/8 a Foundation used only 1 UObject.[21] In Version 1.0 _(and after)_ Foundations and other _Lightweight Actors_ used 0 UObjects, but the use of Abstract Instances remained for other _Heavy Actors_ which are buildable's that __produce items, or are interacted with by the Player__. 

### Lightweight Actors

In [Version 1.0](/wiki/Patch_1.0 "Patch 1.0") Satisfactory began using _Lightweight Actors_[22] to further improve performance and reduce UObject usage. Buildable's that __don't produce items, nor are interacted with by the Player__ , are now implemented as data-only Lightweight Actors, sometimes called **Data Only Objects**. Common examples of Data Only Objects are [Foundations](/wiki/Foundations "Foundations"), [Walls](/wiki/Walls "Walls"), [Roofs](/wiki/Roofs "Roofs"), [Fences](/wiki/Walls#Other "Walls"), [Walkways](/wiki/Walkways "Walkways"), etc. Notable benefits include: 

  * Game Saves created prior to Version 1.0 will convert as needed former _Heavy Actors_ to Lightweight Actors making them Data Only Objects[23], and the game will render them based on that "lightweight data", resulting in a decrease in use of Unreal Engine UObjects by _that Game Save_.
  * Lightweight Actors have 0 UObjects[24] as they are rendered directly from the building position and customization data without going through the UObject system.
  * Data Only Objects will only store crucial information, like location, graphic mesh, customization data _(colors, materials, etc.)_ , and the recipe used to build them. This lightweight data is stored in a centralized location in memory, reducing game save/load times and save file size.
  * As a result of the use of Lightweight Actors, [Multiplayer](/wiki/Multiplayer "Multiplayer") clients can join faster due to the reduced amount of data needed to be transferred from host to client.



### UObject Game Crash

When creating a huge factory _(in a sense of 2000+ hours spent on a single save)_ , it is possible that the game will begin crashing with the following crash: 

`Assertion failed: Index >= 0 && Index < MaxElements Fatal error: [File:C:\BuildAgent2\work\b731a33f2a691e17\UE4\Engine\Source\Runtime\CoreUObject\Private\UObject\UObjectArray.cpp] [Line: 534] Maximum number of UObjects (2162688) exceeded when trying to add 1 object(s), make sure you update MaxObjectsInGame/MaxObjectsInEditor/MaxObjectsInProgram in project settings.`

Keep in mind that _this crash only occurs to a minuscule percentage of players, and should not be worried about_ unless one knowingly creates a map-wide factory. Raising the UObject limit leads to potential instability and it would therefore be counterproductive to change the limit, unless the game begins crashing with the aforementioned crash. 

### UObject Limit Increase

**NOTE: Changing the UObject Limit is NOT supported by Coffee Stain Studios.**[25]

The UObject Limit can be increased by appending the following at the bottom of the _Engine.ini_ file, found at `%LOCALAPPDATA%\FactoryGame\Saved\Config\Windows\Engine.ini`: 
    
    
     [/Script/Engine.GarbageCollectionSettings]
     gc.MaxObjectsInEditor=100000000
     gc.MaxObjectsInGame=100000000

Please note that it is imperative that you **back up your save files regularly if you chose to do this** as it can lead to save file corruption and various other issues in the game.[26]

If you experience the UObject crash after making the above changes to 'Engine.ini', the Epic Games platform may be overriding your project settings with its own, accessible (by default) in `C:\Program Files (x86)\Epic Games\UE_5.1\Engine\Config\BaseEngine.ini`. 

Find (Ctrl+F) the `GarbageCollectionSettings` within BaseEngine.ini and increase the entity limit as above. 

## Engine usage history

Version  | Introduced  | Date  | Remarks   
---|---|---|---  
4.16–4.18[Doc 14] | Pre-Closed Alpha  | 17 July 2017  | _Possibly used_[27]  
4.20[Doc 15] | [Patch 2018-10-17](/wiki/Patch_2018-10-17 "Patch 2018-10-17") | 17 October 2018  | Upgraded   
4.25[Doc 16] | [Patch 0.3.8.0](/wiki/Patch_0.3.8.0 "Patch 0.3.8.0") | 19 January 2021  | Upgraded   
4.25–4.26[Doc 17] | [Patch 0.3.8.7](/wiki/Patch_0.3.8.7 "Patch 0.3.8.7") | 11 February 2021  | Cherry picked Instance mesh optimization from Unreal Engine 4.26 upgrade to use in game.   
4.26[Doc 17] | [Patch 0.4.3.0](/wiki/Patch_0.4.3.0 "Patch 0.4.3.0") | 21 September 2021  | Upgraded   
4.26.2[Doc 17] | [Patch 0.5.1.11](/wiki/Patch_0.5.1.11 "Patch 0.5.1.11") | 22 February 2022  | Upgraded   
5.1.1  | [Patch 0.8.0.0](/wiki/Patch_0.8.0.0 "Patch 0.8.0.0") | 13 June 2023  | Upgraded[28]  
5.2.1  | [Patch 0.8.2.0](/wiki/Patch_0.8.2.0 "Patch 0.8.2.0") | 16 October 2023  | Upgraded[29]  
5.3.0  | [Version 1.0](/wiki/Patch_1.0 "Patch 1.0") | 10 September 2024  | Upgraded. Also used in Closed Beta[30].   
  
## Trivia

  * The World Partitioning System (WPS) was one of the main reasons that Satisfactory was upgraded to Unreal Engine 5.[31]
  * Virtual Shadow Maps (VSM) was developed by Snutt's professor and invented while he was in University studying Computer Graphics.[32]



## Current issues

  * There are some known issues with Unreal Engine 5. 
    * There is major performance loss when running out of VRAM
    * TSR can cause visual issues with conveyor belts, you can try using the following console command to alleviate the issues, but this will reduce AntiAliasing quality 
      * `r.TSR.ShadingRejection.Flickering 0`
    * Random Physic bugs might be seen that will be addressed at some point[Chaos 8]



## See also

  * [Settings](/wiki/Settings "Settings")



## Gallery

The following images are paired together and can be toggled back and forth to see differences. 

  * [](/wiki/File:Comparison_1_-_Grass_Fields_Biome_-_U7.png "Grass Fields Biome as of Patch 0.7.1.1 using UE 4.26.2.")

Grass Fields Biome as of [Patch 0.7.1.1](/wiki/Patch_0.7.1.1 "Patch 0.7.1.1") using UE 4.26.2.

  * [](/wiki/File:Comparison_1_-_Grass_Fields_Biome_-_U8.png "Grass Fields Biome as of Patch 0.8.0.0 using UE 5.1.1.")

Grass Fields Biome as of [Patch 0.8.0.0](/wiki/Patch_0.8.0.0 "Patch 0.8.0.0") using UE 5.1.1.

  * [](/wiki/File:Comparison_2_-_Northern_Forest_-_U7.png "Northern Forest Biome as of Patch 0.7.1.1 using UE 4.26.2. \(Example 1\)")

Northern Forest Biome as of [Patch 0.7.1.1](/wiki/Patch_0.7.1.1 "Patch 0.7.1.1") using UE 4.26.2. (Example 1)

  * [](/wiki/File:Comparison_2_-_Northern_Forest_-_U8.png "Northern Forest Biome as of Patch 0.8.0.0 using UE 5.1.1. \(Example 1\)")

Northern Forest Biome as of [Patch 0.8.0.0](/wiki/Patch_0.8.0.0 "Patch 0.8.0.0") using UE 5.1.1. (Example 1)

  * [](/wiki/File:Comparison_3_-_Northern_Forest_-_U7.png "Northern Forest Biome as of Patch 0.7.1.1 using UE 4.26.2. \(Example 2\)")

Northern Forest Biome as of [Patch 0.7.1.1](/wiki/Patch_0.7.1.1 "Patch 0.7.1.1") using UE 4.26.2. (Example 2)

  * [](/wiki/File:Comparison_3_-_Northern_Forest_-_U8.png "Northern Forest Biome as of Patch 0.8.0.0 using UE 5.1.1. \(Example 2\)")

Northern Forest Biome as of [Patch 0.8.0.0](/wiki/Patch_0.8.0.0 "Patch 0.8.0.0") using UE 5.1.1. (Example 2)

  * [](/wiki/File:Comparison_4_-_Dune_Desert_-_U7.png "Dune Desert Biome of Patch 0.7.1.1 using UE 4.26.2.")

Dune Desert Biome of [Patch 0.7.1.1](/wiki/Patch_0.7.1.1 "Patch 0.7.1.1") using UE 4.26.2.

  * [](/wiki/File:Comparison_4_-_Dune_Desert_-_U8.png "Dune Desert Biome as of Patch 0.8.0.0 using UE 5.1.1.")

Dune Desert Biome as of [Patch 0.8.0.0](/wiki/Patch_0.8.0.0 "Patch 0.8.0.0") using UE 5.1.1.

  * [](/wiki/File:Comparison_5_-_Spire_Coast_-_U7.png "Spire Coast Biome as of Patch 0.7.1.1 using UE 4.26.2.")

Spire Coast Biome as of [Patch 0.7.1.1](/wiki/Patch_0.7.1.1 "Patch 0.7.1.1") using UE 4.26.2.

  * [](/wiki/File:Comparison_5_-_Spire_Coast_-_U8.png "Spire Coast Biome as of Patch 0.8.0.0 using UE 5.1.1.")

Spire Coast Biome as of [Patch 0.8.0.0](/wiki/Patch_0.8.0.0 "Patch 0.8.0.0") using UE 5.1.1.




## History

  * [Patch 1.1.1.4](/wiki/Patch_1.1.1.4 "Patch 1.1.1.4"): Fixed Surround sound not working properly since 1.1
  * [Patch 1.1.0.5](/wiki/Patch_1.1.0.5 "Patch 1.1.0.5"): Potential crash fix for Shader related issue when closing the game
  * [Patch 1.1.0.3](/wiki/Patch_1.1.0.3 "Patch 1.1.0.3"): Fixed a memory leak that would lead to an Object Limit related crash when playing for prolonged amounts of time
  * [Patch 1.1.0.0](/wiki/Patch_1.1.0.0 "Patch 1.1.0.0")
  * Several audio improvements were made: 
    * Factory sounds will now be occluded and muffled if they are behind walls or other obstacles (like foundations). Different buildings will also change the way the sounds occlude, for example, glass or metal.
    * Factory and player sounds will now behave differently if the player is indoors, The HUB now has a unique audio setup as well
    * Player related sounds will now change dynamically depending on your surroundings for example high ceilings, tight corridors or inside caves.
    * Voice has different strength levels adjustable in [Settings](/wiki/Settings "Settings"). Attenuation now uses mid-side stereo positioning rather than just ducking specific frequencies
  * [Patch 1.0.1.5](/wiki/Patch_1.0.1.5 "Patch 1.0.1.5")
    * Fixed an issue where lightweight buildable's could be seen but not interacted with, either by walking through them or by dismantling them but not actually being able to remove them until restarting a [Dedicated Servers](/wiki/Dedicated_Servers "Dedicated Servers") or rejoining a [Multiplayer](/wiki/Multiplayer "Multiplayer") Session 
      * This was most commonly seen with Foundations and Walls, but could also affect other buildable's like Road Barriers, Catwalk Walkways, etc.
    * Fixed an issue where Lightweight buildable's would fail to sample (MMB) in Dedicated Servers or Multiplayer sessions
  * [Patch 1.0.1.0](/wiki/Patch_1.0.1.0 "Patch 1.0.1.0")
    * Fixed crash on shutdown related to WWise
    * Fixed performance issues in huge factories related to Wwise voice starvation
  * [Patch 1.0.0.5](/wiki/Patch_1.0.0.5 "Patch 1.0.0.5"): Optimized the Lightweight Subsystem, this improves a bug where hovering over big [blueprint](/wiki/Blueprint "Blueprint") holograms over existing buildables would drastically lower performance until the hologram was closed
  * [Patch 0.8.3.1](/wiki/Patch_0.8.3.1 "Patch 0.8.3.1"): Potential fix to a crash related to ItemRegrow subsystem
  * [Patch 0.8.2.9](/wiki/Patch_0.8.2.9 "Patch 0.8.2.9"): Some improvements to [Pipe](/wiki/Pipe "Pipe") SFX causing hitches/stuttering in factories with a lot of [Refineries](/wiki/Refinery "Refinery")/[Blenders](/wiki/Blender "Blender") built
  * [Patch 0.8.2.6](/wiki/Patch_0.8.2.6 "Patch 0.8.2.6")
    * Applied a series of patches to the rendered recommended by AMD that should improve [FSR](/wiki/Settings#Video "Settings") Performance
    * Tweaked scalability for better eye adaptation on lower quality
  * [Patch 0.8.2.4](/wiki/Patch_0.8.2.4 "Patch 0.8.2.4")
    * Added AMD FidelityFX™ Super Resolution (FSR) 2 
      * It can now be selected under Options > Video > Upscaling Method
  * [Patch 0.8.2.0](/wiki/Patch_0.8.2.0 "Patch 0.8.2.0")
    * Unreal Engine Upgraded to 5.2.1
    * Parallelized post processing blending.
    * Chaos memory optimizations
    * Texture memory optimizations
    * Mesh memory optimizations
    * Enabled virtual textures for HLODs
    * Updated HLODs to use virtual textures.
    * Enabled PSO caching
    * Removed legacy assets
    * Fixed an Audio issue leading to performance hitches in factories with [Blenders](/wiki/Blender "Blender") and [Refineries](/wiki/Refinery "Refinery"), including audio optimizations for the Refinery
    * Replaced some audio files for the [Tractor](/wiki/Tractor "Tractor") and [Truck](/wiki/Truck "Truck")
    * Tweaks and adjustments for Tractor and Truck audio
  * [Patch 0.8.1.3](/wiki/Patch_0.8.1.3 "Patch 0.8.1.3")
    * Updated XeSS to 1.2
    * Changed so screen percentage presets for XeSS match DLSS and TSR presets
    * Unlocked Screen Percentage for XeSS
    * Moved the Screen Percentage setting to be under Upscaling Preset
    * Fixed Screen Percentage setting not saving properly
  * [Patch 0.8.1.1](/wiki/Patch_0.8.1.1 "Patch 0.8.1.1"): Undocumented Change - Improvements to use of Lumen Global Illumination
  * [Patch 0.8.1.0](/wiki/Patch_0.8.1.0 "Patch 0.8.1.0")
    * Added Nvidia DLSS as a selectable Upscaling method
    * Added Intel XeSS as a selectable Upscaling method
    * Added Upscaling method settings 
      * You can select between TSR, DLSS or XeSS under this drop down when your hardware supports it
    * Fixed Lumen for buildable [lights](/wiki/Lights "Lights"). Fixed apply customization data to also apply extra data. 
      * You will need to reload your save if Lumen was not enabled in order for this to work
    * Added Lumen boost to materials
    * Enabled Skip draw when shader isn't done compiling, this should help reduce rendering hitches
    * Disabled overlap caching to reduce consistent chaos performance loss.
    * General Chaos memory optimizations
    * Optimized physic scene handling for foliage, should reduce hitches.
  * [Patch 0.8.0.3](/wiki/Patch_0.8.0.3 "Patch 0.8.0.3")
    * Some ambience tweaks to Red Jungle sound effects
    * Some ambience tweaks to Spire Coast sound effects
    * Changed the audio for the waterfalls in Dune Desert Canyon
    * General tweaks to waterfall sound effects
  * [Patch 0.8.0.2](/wiki/Patch_0.8.0.2 "Patch 0.8.0.2")
    * Resolved issues where signs ticked when not needed, This should improve GPU bandwidth and improve CPU performance in saves with a big quantity of Signs built
    * Cleaned up major log spam that affected loading
  * [Patch 0.8.0.1](/wiki/Patch_0.8.0.1 "Patch 0.8.0.1")
    * Removed "Cinematic" Global Illumination preset due to the fact that VRAM does not get flushed correctly, which would lead to severe performance loss until the game is restarted.
    * Renamed TSR "Insanity" Preset to "No downscaling" and added Tooltips clarifying their purpose 
      * Performance (Performance over quality, Some rendering artifacts)
      * Balanced (Performance and quality focused)
      * Quality (Quality Focused)
      * No Downscaling (Only Anti aliasing, not recommended!)
  * [Patch 0.8.0.0](/wiki/Patch_0.8.0.0 "Patch 0.8.0.0")
    * Upgraded Unreal Engine to Version 5 
      * Introduced World Partitioning System (WPS) for streaming parts of the world in and out
      * Introduced physics simulation system called Chaos and reworked vehicles to use this instead of previous physics simulation system
      * Introduced Enhanced Input system and implemented contextual key bindings in the options, allowing for much more granularity and control over your control scheme across different contexts like the build mode, driving vehicles, using equipment, etc.
      * Introduced Anti-aliasing (TSR & FXAA) 
        * Setup content to work with TSR (Temporal Super Resolution) which is Epic’s implementation of upscaling technology combined with anti-aliasing. Added several presets: Performance, Balanced, Quality & Insanity.
        * Added a lightweight anti-aliasing method known as FXAA (Fast approximate anti-aliasing) which would allow for better performance on lower end machines or for people that don’t like the effect that the previous default anti-aliasing technique had.
      * Introduced Nanite, a new way of rendering complex meshes allowing for high visual quality. Due to complications we only decided to convert a part of our content to Nanite. Rocks, Cliffs and Conveyor items will be using Nanite for the time being.
      * Introduced Lumen, a Global Illumination system that improves lighting and reflections. This new rendering feature will make the world and factory more grounded which can result in more intense & realistic scenes. 
        * Lumen disabled by default even on the ultra-preset due to its high demand on the hardware. There are several scalability options to make Lumen perform well on most hardware.
        * When using Lumen, it is recommend running with TSR enabled on the “Performance” preset and Lumen on Medium or High due to the minimum quality difference. Next to that if you want the high-quality bounce light but not the reflections you can disable the Lumen Reflections in the video settings.
    * Converted to World Partitioning (Work in progress)
    * Deprecated World composition implementation
    * Added streaming scalability for foliage streaming cells 
      * Foliage cells can now be loaded from different ranges 
        * Near, Default, Far, Cinematic
    * Added TSR 
      * Added TSR Presets: 
        * Performance (60% Screen percentage)
        * Balanced (75% Screen percentage)
        * Quality (90% Screen percentage)
        * Insanity (100% Screen percentage)
    * Added Lumen
    * Added Lumen Scalability
    * Added Lumen Reflections Scalability
    * Improved DirectX12 Stability
    * Improved Vulkan Stability
    * Deprecated/Soft Removed DirectX 11 
      * Note you can still run on DirectX 11 but without Nanite or Lumen. We cannot promise the same quality as on DirectX 12 or Vulkan.
  * [Patch 0.7.0.0](/wiki/Patch_0.7.0.0 "Patch 0.7.0.0") through [Patch 0.7.1.1](/wiki/Patch_0.7.1.1 "Patch 0.7.1.1"): Undocumented Change - At some point in Update 7 game began using "Abstract Incidences" that reduced the number of UObjects used per "Object" like a Constructor.[21][33]
  * [Patch 0.6.1.2](/wiki/Patch_0.6.1.2 "Patch 0.6.1.2")
    * Added new ambient audio for [Spire Coast](/wiki/Spire_Coast "Spire Coast")
    * Reduced the fog glow at night in [Grass Fields](/wiki/Grass_Fields "Grass Fields")
  * [Patch 0.6.0.14](/wiki/Patch_0.6.0.14 "Patch 0.6.0.14")
    * New [Alpha Hog](/wiki/Alpha_Hog "Alpha Hog") and [Spitter](/wiki/Spitter "Spitter") Sounds
    * Improved the lighting in [Grass Fields](/wiki/Grass_Fields "Grass Fields") during the night, also increased blend distance to improve differences in fog heights
  * [Patch 0.6.0.10](/wiki/Patch_0.6.0.10 "Patch 0.6.0.10")
    * Reworks to ambient audio in [Spire Coast](/wiki/Spire_Coast "Spire Coast")
    * New [Gas](/wiki/Gas_Nobelisk "Gas Nobelisk") and [Pulse Nobelisk](/wiki/Pulse_Nobelisk "Pulse Nobelisk") equip sounds
    * Added Nobelisk equip effects for gas and shockwave
    * Remade all the Rain SFX and added new assets for distant thunder
    * Fixed issue where not all foundation materials were affected by rain
  * [Patch 0.6.0.0](/wiki/Patch_0.6.0.0 "Patch 0.6.0.0")
    * Added dynamic clouds and rainy weather
    * Updated night sky visuals
    * Updated lighting and fog in: 
      * Spire Coast Biome
      * Swamp Biome
      * Northern Forest Biome
      * Dune Desert Biome
      * Grass Fields Biome
    * Added new music in Swamp Biome
    * Tweaked Western Dune Forest ambient sounds
    * Reworked [Chainsaw](/wiki/Chainsaw "Chainsaw") audio
    * Reworked [Rifle](/wiki/Rifle "Rifle") audio
    * Added sound effect when collecting [Power Slugs](/wiki/Power_Slug "Power Slug")
    * Overhauled the Foliage System
    * Implemented Sublevel Saving
    * Parallelized fluid system
  * [Patch 0.5.1.11](/wiki/Patch_0.5.1.11 "Patch 0.5.1.11")
    * Upgraded to Unreal Engine 4.26.2
    * Fixed a crash when exiting the game when using [Vulkan](/wiki/Settings "Settings") as a renderer
  * [Patch 0.5.1.2](/wiki/Patch_0.5.1.2 "Patch 0.5.1.2")
    * Made it so when a game running on DX12 detects an incompatible Intel graphics card it will set the renderer to DX11 instead, this is to solve crashes on Start-up or Loading due to DX12 incompatibility.
    * If you are on an Intel GPU and you’re running the game completely fine in DX12, you can still force it by adding the following launch options: 
      * `-d3d12`
      * `-DX12`
  * [Patch 0.5.0.10](/wiki/Patch_0.5.0.10 "Patch 0.5.0.10"): Made DX12 the default graphics renderer. When not supported the game should still default to DX11. [Options Menu](/wiki/Settings#Video "Settings") might show DX12 as selected even though DX11 is the one active in these cases. (Known Bug)
  * [Patch 0.5.0.9](/wiki/Patch_0.5.0.9 "Patch 0.5.0.9"): Potential fix for a [Multiplayer](/wiki/Multiplayer "Multiplayer") / [Dedicated servers](/wiki/Dedicated_servers "Dedicated servers") crash related to Unreal Engine tireconfig deletion
  * [Patch 0.5.0.6](/wiki/Patch_0.5.0.6 "Patch 0.5.0.6")
    * Adjusted sky light
    * Adjusted clouds
    * Adjusted post processing
  * [Patch 0.5.0.4](/wiki/Patch_0.5.0.4 "Patch 0.5.0.4"): Potential fix for a Crash related to Instance Bucket
  * [Patch 0.5.0.3](/wiki/Patch_0.5.0.3 "Patch 0.5.0.3"): Fixed Epic Online Services (EOS) related crash when loading or starting a new game
  * [Patch 0.5.0.2](/wiki/Patch_0.5.0.2 "Patch 0.5.0.2"): Rolled back latest Epic Online Services (EOS) plugin to the previous version, this should solve all sorts of messages people are seeing when starting up the game, shouldn’t create any new issues
  * [Patch 0.5.0.0](/wiki/Patch_0.5.0.0 "Patch 0.5.0.0")
    * Added 8 music tracks to the Factory playlist (only plays around factory buildings) 
      * 5 new intermission tracks (around 2 minutes each)
      * 3 new full-length tracks (7-8 minutes each)
    * DX12 now available again as experimental renderer in the options menu
    * Vulkan now available again as experimental renderer in the options menu
    * Updates to a lot of LODs
    * All walls and foundations are now more optimized
    * Conveyor renderer optimizations
    * Factory tick optimizations
  * [Patch 0.4.3.0](/wiki/Patch_0.4.3.0 "Patch 0.4.3.0")
    * Upgraded to Unreal Engine 4.26
    * DX12 now available as renderer in the options menu
    * Vulkan now available as renderer in the options menu
  * [Patch 0.3.8.7](/wiki/Patch_0.3.8.7 "Patch 0.3.8.7"): Cherry picked Instance mesh optimization from unreal engine 4.26 upgrade
  * [Patch 0.3.8.0](/wiki/Patch_0.3.8.0 "Patch 0.3.8.0"): Updated to Unreal Engine version 4.25
  * [Patch 2018-10-17](/wiki/Patch_2018-10-17 "Patch 2018-10-17"): Updated to the latest Unreal Version _(not specified but presumed Version 4.20)_ which has set us back some in performance. However, in the coming weeks we will get back some of our custom features as well as additional features now possible with latest Unreal version.
  * [Patch 2018-10-11](/wiki/Patch_2018-10-11 "Patch 2018-10-11"): Made Available _(Version 4.16 through 4.19)_



## References

  1. ↑ [YouTube - Pre-alpha Satisfactory Tutorial (August 2017)](https://www.youtube.com/watch?v=ZW0OOikcWN0&t=39s)
  2. ↑ [YouTube - We're upgrading to UNREAL ENGINE 5 - Nanite General Info](https://www.youtube.com/watch?v=dY__x2dq7Sk&t=306s)
  3. ↑ [YouTube - We're upgrading to UNREAL ENGINE 5 - Nanite Game Usage](https://www.youtube.com/watch?v=dY__x2dq7Sk-2&t=407s)
  4. ↑ [YouTube - World Changes with Hannah - Nanite Discussion](https://www.youtube.com/watch?v=5NBgetrxtpw&t=1054s)
  5. ↑ [YouTube - We're upgrading to UNREAL ENGINE 5 - Lumen Game Usage](https://www.youtube.com/watch?v=dY__x2dq7Sk-2&t=436s)
  6. ↑ [YouTube - March 28th, 2023 Livestream on Twitch - Lumen on / off](https://www.youtube.com/watch?v=oLl9SZht-bE&t=1798s)
  7. ↑ [YouTube - We're upgrading to UNREAL ENGINE 5 - Virtual Shadow Maps (VSM)](https://www.youtube.com/watch?v=dY__x2dq7Sk&t=374s)
  8. ↑ [YouTube - April 2nd, 2024 Livestream - Q&A: Since Virtual Shadow Maps are production-ready in 5.3, has your position changed?](https://www.youtube.com/watch?v=I1mbAHhkIfE)
  9. ↑ [YouTube - We're upgrading to UNREAL ENGINE 5 - UE 4 World Grid System (WGS)](https://www.youtube.com/watch?v=dY__x2dq7Sk&t=528s)
  10. ↑ [YouTube - December 12th, 2023 Livestream - Q&A: World Partitioning System, how does that correspond to the Map?](https://www.youtube.com/watch?v=zVI14aHkv3o)
  11. ↑ [YouTube - We're upgrading to UNREAL ENGINE 5 - World Partitioning System (WPS) Usage](https://www.youtube.com/watch?v=dY__x2dq7Sk&t=609s)
  12. ↑ [YouTube - We're upgrading to UNREAL ENGINE 5 - Temporal Super Resolution (TSR)](https://www.youtube.com/watch?v=dY__x2dq7Sk-2&t=824s)
  13. ↑ [YouTube - We're upgrading to UNREAL ENGINE 5 - Fast Approximate Anti-Aliasing (FXAA)](https://www.youtube.com/watch?v=dY__x2dq7Sk-2&t=890s)
  14. ↑ [YouTube - August 22nd, 2023 Livestream on Twitch - DLSS and XESS](https://www.youtube.com/watch?v=eGZh3zRXKQE&t=790s)
  15. ↑ [YouTube - August 22nd, 2023 Livestream on Twitch - FSR](https://www.youtube.com/watch?v=eGZh3zRXKQE&t=857s)
  16. ↑ [YouTube - We're upgrading to UNREAL ENGINE 5 - Enhanced Input System (EIS)](https://www.youtube.com/watch?v=dY__x2dq7Sk&t=1193s)
  17. ↑ [YouTube - We're upgrading to UNREAL ENGINE 5 - Audio Improvements](https://www.youtube.com/watch?v=dY__x2dq7Sk&t=1250s)
  18. ↑ [YouTube - November 20th, 2020 Livestream on Twitch - Snutt & Jace Talk: Unreal Engine Object Limit - Limit Set By](https://www.youtube.com/watch?v=bk2ojhuil-g&t=19s)
  19. ↑ [YouTube - We're upgrading to UNREAL ENGINE 5 - Q&A: Has The UObject Build Limit Increased in UE 5?](https://www.youtube.com/watch?v=dY__x2dq7Sk&t=1762s)
  20. ↑ [Reddit - General Questions - Former CSS Community Manager Snutt Treptow comment about UObject Limit](https://www.reddit.com/r/SatisfactoryGame/comments/1444nwp/general_questions/)
  21. ↑ 21.0 21.1 [YouTube - We're upgrading to UNREAL ENGINE 5 - Use of Abstract Incidences](https://www.youtube.com/watch?v=dY__x2dq7Sk&t=1855s)
  22. ↑ [YouTube - Optimization Coming in 1.0! - Lightweight Actors](https://youtu.be/yIKjR5jVv9Y?t=373)
  23. ↑ [YouTube - May 7th, 2025 Livestream - Q&A: Does the announced Belt optimization impact the in-game Object Limit?](https://www.youtube.com/watch?v=7n2x5yZJZvQ)
  24. ↑ [Modding Discord - Message from developer Archengius on June 12th, 2025](https://discord.com/channels/555424930502541343/555505343031934979/1382638128547758150)
  25. ↑ [YouTube - November 20th, 2020 Livestream on Twitch - Snutt & Jace Talk: Unreal Engine Object Limit - Increase Support](https://www.youtube.com/watch?v=bk2ojhuil-g&t=25s)
  26. ↑ [YouTube - November 20th, 2020 Livestream on Twitch - Snutt & Jace Talk: Unreal Engine Object Limit - Increase Issues](https://www.youtube.com/watch?v=bk2ojhuil-g&t=121s)
  27. ↑ [Pre-alpha Satisfactory Tutorial (August 2017) Screenshot](https://satisfactory.wiki.gg/wiki/Game_menus#/media/File:Main_Menu_Pre-Alpha.png)
  28. ↑ [YouTube - We're upgrading to UNREAL ENGINE 5 - Q&A: What Version Of UE 5 Is Game Using?](https://www.youtube.com/watch?v=dY__x2dq7Sk&t=2120s)
  29. ↑ [YouTube - Where's Update 8? - Game Is Getting Upgrade to Unreal Engine 5.2](https://www.youtube.com/watch?v=RIZS_qyiLH4&t=105s)
  30. ↑ [YouTube - February 6, 2024 Livestream - Q&A: Will Mods work for closed beta?](https://www.youtube.com/watch?v=HXQkWaFH-TU)
  31. ↑ [YouTube - March 28th, 2023 Livestream on Twitch - World Partitioning System](https://www.youtube.com/watch?v=oLl9SZht-bE&t=2568s)
  32. ↑ [YouTube - September 19th, 2023 Livestream on Twitch - Snutt Talk: Shadow Rendering Techniques](https://www.youtube.com/watch?v=z0gVOREXHGs&t=97s)
  33. ↑ [Reddit Post - General Questions - Reply Comment by CSS Community Manager Snutt Treptow](https://www.reddit.com/r/SatisfactoryGame/comments/1444nwp/comment/jndl1ie/?utm_source=reddit&utm_medium=web2x&context=3)



### Unreal Engine Chaos Physics

  1. ↑ [YouTube - We're upgrading to UNREAL ENGINE 5 - Vehicle Physics Overhaul - General](https://www.youtube.com/watch?v=dY__x2dq7Sk&t=922s)
  2. ↑ [YouTube - We're upgrading to UNREAL ENGINE 5 - Vehicle Physics Overhaul - Vehicle Issues](https://www.youtube.com/watch?v=dY__x2dq7Sk&t=1012s)
  3. ↑ [YouTube - We're upgrading to UNREAL ENGINE 5 - Vehicle Physics Overhaul - Vehicle Changes](https://www.youtube.com/watch?v=dY__x2dq7Sk&t=1062s)
  4. ↑ [YouTube - We're upgrading to UNREAL ENGINE 5 - Vehicle Physics Overhaul - Vehicle Breaking](https://www.youtube.com/watch?v=dY__x2dq7Sk&t=1115s)
  5. ↑ [YouTube - We're upgrading to UNREAL ENGINE 5 - Vehicle Physics Overhaul - Vehicle Air Control Removed](https://www.youtube.com/watch?v=dY__x2dq7Sk&t=1130s)
  6. ↑ [YouTube - We're upgrading to UNREAL ENGINE 5 - Vehicle Physics Overhaul - Trains](https://www.youtube.com/watch?v=dY__x2dq7Sk&t=1190s)
  7. ↑ [YouTube - We're upgrading to UNREAL ENGINE 5 - Vehicle Physics Overhaul - Sounds](https://www.youtube.com/watch?v=dY__x2dq7Sk&t=1157s)
  8. ↑ [YouTube - We're upgrading to UNREAL ENGINE 5 - Chaos Physic Issues](https://www.youtube.com/watch?v=dY__x2dq7Sk&t=1044s)



### Unreal Engine Documentation

  1. ↑ [Unreal Engine 5 - Nanite Virtualized Geometry](https://docs.unrealengine.com/5.0/en-US/nanite-virtualized-geometry-in-unreal-engine/)
  2. ↑ [Unreal Engine 5 - Lumen Global Illumination and Reflections](https://docs.unrealengine.com/5.0/en-US/lumen-global-illumination-and-reflections-in-unreal-engine/)
  3. ↑ [Unreal Engine 5 - World Partitioning System (WPS)](https://docs.unrealengine.com/5.1/en-US/world-partition-in-unreal-engine/)
  4. ↑ [Unreal Engine 5 - Actors Explained](https://docs.unrealengine.com/4.26/en-US/ProgrammingAndScripting/ProgrammingWithCPP/UnrealArchitecture/Actors/)
  5. ↑ [Unreal Engine 5 - Temporal Super Resolution](https://docs.unrealengine.com/5.2/en-US/temporal-super-resolution-in-unreal-engine/)
  6. ↑ [Unreal Engine 5 - Anti-Aliasing and Upscaling](https://docs.unrealengine.com/5.2/en-US/anti-aliasing-and-upscaling-in-unreal-engine/)
  7. ↑ [Nvidia Deep Learning Super Sampling (DLSS)](https://www.nvidia.com/en-us/geforce/technologies/dlss/)
  8. ↑ [XeSS Super Sampling (ExSS)](https://www.intel.com/content/www/us/en/products/docs/discrete-gpus/arc/technology/xess.html)
  9. ↑ [AMD FidelityFX™ Super Resolution (FSR)](https://www.amd.com/en/technologies/fidelityfx-super-resolution)
  10. ↑ [Unreal Engine 5 - Chaos Physics](https://docs.unrealengine.com/4.26/en-US/InteractiveExperiences/Physics/ChaosPhysics/)
  11. ↑ [Unreal Engine - Enhanced Input System (EIS)](https://docs.unrealengine.com/5.0/en-US/enhanced-input-in-unreal-engine/)
  12. ↑ [Unreal Engine - MetaSounds](https://docs.unrealengine.com/5.0/en-US/metasounds-the-next-generation-sound-sources-in-unreal-engine/)
  13. ↑ [Unreal Engine - UObject](https://docs.unrealengine.com/en-US/API/Runtime/CoreUObject/UObject/UObject/index.html)
  14. ↑ [Unreal Engine 4.16 Released!](https://www.unrealengine.com/en-US/blog/unreal-engine-4-16-released)
  15. ↑ [Unreal Engine 4.20 Released!](https://www.unrealengine.com/en-US/blog/unreal-engine-4-20-released)
  16. ↑ [Unreal Engine 4.25 Released!](https://www.unrealengine.com/en-US/blog/unreal-engine-4-25-released)
  17. ↑ 17.0 17.1 17.2 [Unreal Engine 4.26 Released!](https://www.unrealengine.com/en-US/blog/unreal-engine-4-26-released)



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
Technical| [Console release](/wiki/Console_release "Console release") • [Debug console](/wiki/Debug_console "Debug console") • [Launch arguments](/wiki/Launch_arguments "Launch arguments") • [Save files](/wiki/Save_files "Save files") • [System requirements](/wiki/System_requirements "System requirements") • [Units](/wiki/Units "Units") • Unreal Engine  
Guides and tutorials| | Basics| [Walkthrough/How to play](/wiki/Tutorial:How_to_play "Tutorial:How to play") • [New Pioneer Guide](/wiki/Tutorial:New_Pioneer_Guide "Tutorial:New Pioneer Guide") • [Production line basics](/wiki/Tutorial:Production_line "Tutorial:Production line") • [Advanced production line tips](/wiki/Tutorial:Production_line_design_tips "Tutorial:Production line design tips") • [Picking an alternate recipe](/wiki/Tutorial:Picking_an_alternate_recipe "Tutorial:Picking an alternate recipe") • [Independency](/wiki/Tutorial:Independency "Tutorial:Independency") • [Aluminum Ingot production](/wiki/Tutorial:Setting_up_Aluminum_Ingot_production "Tutorial:Setting up Aluminum Ingot production")  
---|---  
Logistics| [Manifold](/wiki/Manifold "Manifold") • [Balancer](/wiki/Balancer "Balancer") • [Pipeline manifold](/wiki/Pipeline_manifold "Pipeline manifold") • [Prime Splitter Arrays](/wiki/Tutorial:Prime_splitter_arrays "Tutorial:Prime splitter arrays") • [Trains](/wiki/Tutorial:Trains "Tutorial:Trains") • [Train throughput](/wiki/Tutorial:Train_throughput "Tutorial:Train throughput")  
Dedicated servers| [Dedicated servers](/wiki/Dedicated_servers "Dedicated servers") • [Running as a Service](/wiki/Dedicated_servers/Running_as_a_Service "Dedicated servers/Running as a Service") • [Configuration files](/wiki/Dedicated_servers/Configuration_files "Dedicated servers/Configuration files") • [Automatic updates](/wiki/Dedicated_servers/Automatic_updates "Dedicated servers/Automatic updates") • [HTTPS API](/wiki/Dedicated_servers/HTTPS_API "Dedicated servers/HTTPS API") • [Lightweight Query API](/wiki/Dedicated_servers/Lightweight_Query_API "Dedicated servers/Lightweight Query API")  
Other| [Hypertube cannon](/wiki/Tutorial:Hypertube_cannon "Tutorial:Hypertube cannon") • [Hypertube brake](/wiki/Tutorial:Hypertube_brake "Tutorial:Hypertube brake") • [Steam Deck & Controller setup](/wiki/Tutorial:Controller_setup "Tutorial:Controller setup") • [Extracting UI icons](/wiki/Tutorial:Extracting_UI_icons "Tutorial:Extracting UI icons")
  *[v]: View this template
  *[e]: Edit this template
  *[h]: History of this template
  *[his]: his trivia section
