# Combat

[](/wiki/File:Hog_attacking.jpg)

[](/wiki/File:Hog_attacking.jpg "Enlarge")

An pioneer in combat with a "Fluffy-tailed Hog"

[Pioneers](/wiki/Pioneer "Pioneer") can choose to engage in **combat** with [creatures](/wiki/Category:Fauna "Category:Fauna") found in the [world](/wiki/World "World"), in order to access resources they are nesting on[1] and will need to defend themselves from hostile wildlife while exploring.[1] Creatures will never attack structures built by [pioneers](/wiki/Pioneer "Pioneer"),[2] only targeting the pioneers. The pioneer will die if their [health](/wiki/Health "Health") drops to zero. Dead creatures drop loot on death and leave their corpses on the ground that despawn after a short amount of time if not in sight. 

All creatures except for [Stingers](/wiki/Stinger "Stinger") ignore pioneers riding [vehicles](/wiki/Vehicles "Vehicles"), not even targeting the vehicle. 

## Contents

  * 1 Creature hostility
  * 2 Weapons
  * 3 Creature respawn mechanism
  * 4 Creature teleportation
  * 5 Hostile creatures and plants
  * 6 History
  * 7 References



## Creature hostility

During a session, go to [`Esc`](/wiki/Controls "Controls") menu -> Options (Settings) -> Gameplay -> Creature Hostility, there are 3 options to choose from: 

  * Default: Hostile creature become aggressive when Pioneer enters their line of sight or aggro range
  * Passive: Hostile creature will not attack Pioneer at all, even after bring attacked. Flying Crabs and Spore Flower can still deal damage, however.
  * Retaliate: Hostile creature will fight back after being attacked. When in a group, only those being attacked will fight back.



## Weapons

Pioneers can carry multiple identical loaded weapons so they spend less time reloading in combat by swapping to a loaded weapon after emptying a weapon's magazine. Below is a list of usable weapons and their damage per hit: 

  * [](/wiki/Xeno-Zapper "Xeno-Zapper") [Xeno-Zapper](/wiki/Xeno-Zapper "Xeno-Zapper"): 5
  * [](/wiki/Xeno-Basher "Xeno-Basher") [Xeno-Basher](/wiki/Xeno-Basher "Xeno-Basher"): 9
  * [](/wiki/Rebar_Gun "Rebar Gun") [Rebar Gun](/wiki/Rebar_Gun "Rebar Gun")
    * [](/wiki/Iron_Rebar "Iron Rebar") [Iron Rebar](/wiki/Iron_Rebar "Iron Rebar"): 15
    * [](/wiki/Stun_Rebar "Stun Rebar") [Stun Rebar](/wiki/Stun_Rebar "Stun Rebar"): 5 + 5 seconds stun
    * [](/wiki/Shatter_Rebar "Shatter Rebar") [Shatter Rebar](/wiki/Shatter_Rebar "Shatter Rebar"): 15 x 2
    * [](/wiki/Explosive_Rebar "Explosive Rebar") [Explosive Rebar](/wiki/Explosive_Rebar "Explosive Rebar"): 50 explosion
  * [](/wiki/Rifle "Rifle") [Rifle](/wiki/Rifle "Rifle")
    * [](/wiki/Rifle_Ammo "Rifle Ammo") [Rifle Ammo](/wiki/Rifle_Ammo "Rifle Ammo"): 5 hitscan
    * [](/wiki/Homing_Rifle_Ammo "Homing Rifle Ammo") [Homing Rifle Ammo](/wiki/Homing_Rifle_Ammo "Homing Rifle Ammo"): 3 + homing effect
    * [](/wiki/Turbo_Rifle_Ammo "Turbo Rifle Ammo") [Turbo Rifle Ammo](/wiki/Turbo_Rifle_Ammo "Turbo Rifle Ammo"): 4 hitscan + high fire rate
  * [](/wiki/Nobelisk_Detonator "Nobelisk Detonator") [Nobelisk Detonator](/wiki/Nobelisk_Detonator "Nobelisk Detonator")
    * [](/wiki/Nobelisk "Nobelisk") [Nobelisk](/wiki/Nobelisk "Nobelisk"): 50 explosion
    * [](/wiki/Gas_Nobelisk "Gas Nobelisk") [Gas Nobelisk](/wiki/Gas_Nobelisk "Gas Nobelisk"): 5 poison per second x 30 sec
    * [](/wiki/Pulse_Nobelisk "Pulse Nobelisk") [Pulse Nobelisk](/wiki/Pulse_Nobelisk "Pulse Nobelisk"): 5 explosion + knockback
    * [](/wiki/Cluster_Nobelisk "Cluster Nobelisk") [Cluster Nobelisk](/wiki/Cluster_Nobelisk "Cluster Nobelisk"): 50 explosion + 5 x 25 secondary explosions
    * [](/wiki/Nuke_Nobelisk "Nuke Nobelisk") [Nuke Nobelisk](/wiki/Nuke_Nobelisk "Nuke Nobelisk"): 150 explosion + radiation x 30 sec



## Creature respawn mechanism

[](/wiki/File:Map_\(Creature_Spawns\).jpg)

[](/wiki/File:Map_\(Creature_Spawns\).jpg "Enlarge")

A map of all creatures which spawn in the world.

All creatures (fauna) have the ability to respawn. The Pioneer has no control over passive and non-interactable creatures respawning, but can control where and how hostile creatures will respawn as a result of improved logic.[3]

  * There are spawn points for hostile creatures such as [Hogs](/wiki/Hog "Hog") and [Spitters](/wiki/Spitter "Spitter") scattered around the map, particularly near by [Resource Nodes](/wiki/Resource_Node "Resource Node") or collectibles.
  * In the Creature Spawning System[4] each Buildable is given a **value** , and if the sum total of all the _Buildable values_ in a given location reach a **threshold amount** then nearby spawners will be disabled. For example, a single Miner is capable of disabling nearby spawners but a single Foundation is not. 
    * The new Creature Spawning System is believed to have kept the same "effect radius"[5] that was updated in [Update 6](/wiki/Patch_0.6.0.12 "Patch 0.6.0.12") where spawners are disabled within 150 meters of powered buildings, and within a smaller radius for foundations.
  * Creatures won't respawn near places which are intended to be a factory space and have for example large [Foundation](/wiki/Foundations "Foundations") platforms, or functional Buildings like [Miners](/wiki/Miner "Miner"), [Manufacturers](/wiki/Manufacturer "Manufacturer"), [Generators](/wiki/Power#Power_generators "Power"), etc.
  * Creatures will respawn near smaller infrastructure like [Pipelines](/wiki/Pipelines "Pipelines"), [Power Lines](/wiki/Power_Line "Power Line"), [Conveyor Belts](/wiki/Conveyor_Belts "Conveyor Belts"), [Hypertubes](/wiki/Hypertube "Hypertube"), and Foundation "Roads" between distant factories, etc.
  * If creatures were killed, they will attempt to respawn within three game days, and only if the pioneer is not within 150 meters of the spawn point.
  * At the start of the game, (or upon game updates/balancing) the hostile creatures will be present around their spawn point by default.



To prevent hostile creature respawn, the following must be fulfilled: 

  * There is at least one powered player-built building within a 150 meter radius (or Foundations which have a smaller radius)[6] around the hostile spawn point. 
    * This excludes all smaller infrastructure as mentioned above.
  * The existing creatures around their spawn point, if present, must be killed first.
  * The creatures with their spawn point only active at night, must wait to be spawned at least once then be killed, even if all the above criteria are fulfilled before the first night.



## Creature teleportation

  * If a hostile creature moves too far away from its spawn point, it will be automatically teleported back to it, provided the player is not near the spawn point (~ 80 m). For example, if the pioneer attempts to lure a stinger to fall off an edge, or move out of a cave, the stinger will be teleported back to its spawn point. Same applies to most other creatures except [Hogs](/wiki/Hog "Hog").
  * A creature's HP resets back to full-health after it is teleported back to its spawn point.



## Hostile creatures and plants

_Main article:_[Creatures](/wiki/Creatures "Creatures")

## History

  * [Patch 0.6.0.12](/wiki/Patch_0.6.0.12 "Patch 0.6.0.12"): 
    * Creature Changes 
      * Adjustments to the Spitter VFX, Animations, AI and Attacks
      * Adjustments to Hog and Alpha Hogs Physics, AI and Attacks
    * Balancing 
      * Reduced the size of the radius for Factory buildings preventing creatures from respawning
  * [Patch 0.6.0.5](/wiki/Patch_0.6.0.5 "Patch 0.6.0.5"): 
    * Creature Changes 
      * Spawner rework, Initial creature respawn has been reset for all creatures across the world
      * Reduced the distance check for despawning when considered near to a base
      * Power Poles, Hypertubes, Conveyor Belts, Pipes and their related attachments should no longer be considered a base, therefore should not despawn any creatures when built by themselves
  * [Patch 2018-10-17](/wiki/Patch_2018-10-17 "Patch 2018-10-17"): Introduced



## References

  1. ↑ 1.0 1.1 [YouTube - Developer Highlight - Game Design](https://www.youtube.com/watch?v=vUW3pockA5Y&t=99)
  2. ↑ [YouTube - Satisfactory gameplay, campaign length, enemies | E3 2018](https://www.youtube.com/watch?v=_lS1GNl0dGAt=189)
  3. ↑ [YouTube - Where's Update 8? - Creature Spawning System Rewritten](https://youtu.be/RIZS_qyiLH4?t=210)
  4. ↑ [YouTube - Where's Update 8? - Creature Spawning System - How It Works](https://www.youtube.com/watch?v=RIZS_qyiLH4&t=269s)
  5. ↑ [YouTube - September 6th, 2022 Livestream - Fixes and Changes to Creatures](https://www.youtube.com/watch?v=hRN17cFJeRc&t=906s)
  6. ↑ [YouTube - Update 6 Fixes and Changes to Creatures (September 6th, 2022 Livestream on Twitch)](https://youtu.be/hRN17cFJeRc?t=906)



  * [v](/wiki/Template:PioneerNav "Template:PioneerNav")
  * [e](https://satisfactory.wiki.gg/wiki/Template:PioneerNav?action=edit)
  * [h](https://satisfactory.wiki.gg/wiki/Template:PioneerNav?action=history)

[Satisfactory](/wiki/Satisfactory "Satisfactory") game mechanics  
---  
Player abilities| [Codex](/wiki/Codex "Codex") • [Resource Scanner](/wiki/Resource_Scanner "Resource Scanner") • [Build Gun](/wiki/Build_Gun "Build Gun") • [Inventory](/wiki/Inventory "Inventory") • [Health](/wiki/Health "Health") • Combat • [Movement](/wiki/Movement "Movement") • [Flashlight](/wiki/Flashlight "Flashlight") • [HUD](/wiki/HUD "HUD") • [Crate](/wiki/Crate "Crate") • [To-Do List](/wiki/To-Do_List "To-Do List")  
Unlockable abilities| [Recipes](/wiki/Recipes "Recipes") • [Power](/wiki/Power "Power") • [Overclocking/Underclocking](/wiki/Clock_speed "Clock speed") • [Production amplifier](/wiki/Production_amplifier "Production amplifier") • [Customizer](/wiki/Customizer "Customizer") • [Map](/wiki/Map "Map") • [Productivity Display](/wiki/Productivity_Display "Productivity Display") • [Head lift](/wiki/Head_lift "Head lift") • [Blueprints](/wiki/Blueprints "Blueprints") • [Fuels](/wiki/Category:Fuels "Category:Fuels") • [FICSIT Productive Packer Deluxe](/wiki/FICSIT_Productive_Packer_Deluxe "FICSIT Productive Packer Deluxe")  
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
