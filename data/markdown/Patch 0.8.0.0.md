# Patch 0.8.0.0

[](/wiki/File:Update8_Sign_Logo.png)  
  
Patch Notes: Early Access (EXPERIMENTAL) – **v0.8.0.0** – Build 238433. This patch was released on 13 June 2023. It is the first patch of Update 8 development. 

The original post can be viewed on Satisfactory's [official website](https://www.satisfactorygame.com/updates/update-8), as well as [Discord](https://discord.com/channels/370472939054956546/557603412565426196/1118193735218507828), [Reddit](https://www.reddit.com/r/SatisfactoryGame/comments/148heqg), and [Steam](https://store.steampowered.com/news/app/526870/view/3690183765419759383). 

## Contents

  * 1 Intro
    * 1.1 Upgrading to Unreal Engine 5
      * 1.1.1 World partitioning
      * 1.1.2 Vehicle physics & sound overhaul
      * 1.1.3 Enhanced Input System
      * 1.1.4 Anti-aliasing (TSR & FXAA)
      * 1.1.5 Nanite
      * 1.1.6 Lumen
    * 1.2 Blueprint improvements
      * 1.2.1 Dismantling
      * 1.2.2 Building
    * 1.3 Changes to the world
      * 1.3.1 Visuals
      * 1.3.2 Gameplay
      * 1.3.3 Atmosphere
    * 1.4 Advanced Game Settings
    * 1.5 Priority Power Switch & Power Tower
    * 1.6 Quality of life and other improvements
      * 1.6.1 Destructible Gas Pillars
      * 1.6.2 Jetpack fuels
      * 1.6.3 Parachute
      * 1.6.4 Dismantle Filter
  * 2 Patch notes
    * 2.1 Factory
    * 2.2 Advanced Game Settings
    * 2.3 Equipment
    * 2.4 Creatures
    * 2.5 Vehicles
    * 2.6 World
    * 2.7 Quality of Life
    * 2.8 Balancing
    * 2.9 UI
    * 2.10 Player character
    * 2.11 Systems
    * 2.12 Optimization
    * 2.13 Bug fixes
    * 2.14 Known issues
  * 3 Media
    * 3.1 Videos



## Intro

Hi Pioneers! Since you’re reading this, Update 8 is now out on Experimental for you all to try and let us know what you think. We’ve put in great effort to stabilise the game before it gets out to you, but with a major engine upgrade there are always extra chances for issues to occur. So, while you hopefully enjoy all the new goodies, keep an eye out for bugs and problems and most importantly: BACK UP YOUR SAVES! Better to be safe than sorry with this one. Now let’s move on to content. 

Oh boy, did we say this was a smaller update again? Well, it seems we’ve overshot the target a little bit and are now looking at a big package of additions, changes, and quality of life improvements coming out with Update 8! 

There are two new buildings joining the line-up, the Power Tower, and Priority Power Switch. The Titan Forest has gotten a new look, we’ve done updates to atmosphere and lighting, and worked on polishing many other biomes in terms of gameplay and/or visuals. Advanced Game Settings are coming to the game, allowing you to experiment and enjoy Satisfactory with less restrictions than before – if you wish. Blueprints have gotten some major improvements in how you can build with them, and we’ve added several other improvements that we’ll describe in more detail below. We also reworked a number of our systems in conjunction with the engine upgrade to make things run more smoothly for you. 

Find things you love? Things you hate? Tell us about any bugs, issues, and feedback you have on our Questions Site: <https://questions.satisfactorygame.com/>

We’ve hit some roadblocks on the way to this release, but we’re very excited to have you finally play it. Hope you all have a great time, be safe, and best wishes from the team! ❤️ 

### Upgrading to Unreal Engine 5

The bulk of our work on Update 8 has been the engine upgrade. With this come many reworks and updates of systems that should improve aspects of the game, but it all being new also means that new issues can be hiding in lots of places as well. We’ve put a lot of effort into stabilising the game and performance before Experimental release, but there has been lots of ground to cover and this combined with the fact that you all are playing on a vast array of differing hardware means there might very well be things that we’ve missed. So again, come our usual reminders: please back up your saves beforehand and let us know about any differences that you encounter, good or bad, while playing Update 8. 

Below are the most relevant details on what this engine upgrade means for Satisfactory, but if you’ve got some time on your hands Jace talked about the upgrade in depth in one of our earliest Update 8 related videos: <https://youtu.be/dY__x2dq7Sk>

#### World partitioning

This is the new system in Unreal Engine 5 for streaming parts of the world in and out, and we’ve switched to it entirely. The base line for you is that with world partitioning the level streaming should be much more flexible compared to the tile-based system we used before, reducing hitches that you will have encountered at specific parts of the world where these tiles used to intersect. 

#### Vehicle physics & sound overhaul

With UE5 comes an all-new physics simulation called Chaos, and we’ve reworked our vehicles to use this instead of our previous implementation. There should be little to no changes when it comes to vehicle automation, but the manual driving of vehicles has been redone and we made improvements in feel and usage of the different vehicles. From our own tests we feel it is an upgrade overall, but we are curious to hear what you think after playing with them! 

With this we also reworked all vehicle sounds, eliminating many issues we couldn’t easily resolve in our old implementation, overall improving quality and consistency. 

#### Enhanced Input System

Another new system that we switched to with Unreal Engine 5 is the Enhanced Input system. With this we implemented contextual key bindings in the options, allowing for much more granularity and control over your control scheme across different contexts like the build mode, driving vehicles, using equipment, etc. 

Using the Enhanced Input system has also made it easier for us to fix bugs related to inputs. While the migration to the new system created some short-term issues, we have done an extensive pass to ensure all inputs work as intended. But there is always the possibility that you run into an issue that we have missed, in which case you can let us know on our questions site. 

#### Anti-aliasing (TSR & FXAA)

For scalability options we added a lightweight anti-aliasing method known as FXAA (Fast approximate anti-aliasing) which would allow for better performance on lower end machines or for people that don’t like the effect that the previous default anti-aliasing technique had. 

Next to that we setup our content to work with TSR (Temporal Super Resolution) which is Epic’s implementation of upscaling technology combined with anti-aliasing. For user experience we added several presets: Performance, Balanced, Quality & Insanity. 

Note, this doesn’t mean we won't support other Upscaling technologies in the future. 

#### Nanite

With Unreal Engine 5 comes Nanite, a new way of rendering complex meshes allowing for high visual quality. Due to complications we only decided to convert a part of our content to Nanite. Rocks, Cliffs and Conveyor items will be using Nanite for the time being. 

#### Lumen

Lumen is a Global Illumination system that improves lighting and reflections. This new rendering feature will make the world and factory more grounded which can result in more intense & realistic scenes. 

We decided to have Lumen disabled by default even on the ultra-preset due to its high demand on the hardware. There are several scalability options to make Lumen perform well on most hardware. 

When using Lumen, we recommend running with TSR enabled on the “Performance” preset and Lumen on Medium or High due to the minimum quality difference. Next to that if you want the high-quality bounce light but not the reflections you can disable the Lumen Reflections in the video settings. 

### Blueprint improvements

The main feature of our last update is getting some additional love in this one as well. These were a number of improvements you’ve requested and that we still wanted to make, which should significantly improve using Blueprints in Satisfactory. Since a lot changed here, we are closing the old posts on our Questions Site and are curious for you all to submit some fresh feedback after playing with all these changes. Jace talks a little about this, and mostly about the new features coming to Blueprints in this video: <https://youtu.be/ZDN_b6TX5gg>

#### Dismantling

Before Update 8 Blueprints were very tedious to dismantle after being placed. Now we’ve added a Blueprint dismantle mode that you can toggle with ‘R’ by default while in the regular dismantle mode. With this you can dismantle an entire Blueprint at once, significantly reducing the effort to get rid of Blueprints that are misplaced or no longer useful! 

#### Building

To improve building with Blueprints we’ve added several useful features. Blueprints now have a directional indicator in their hologram making it easier to place them in the correct rotation. We also implemented Quick Switch for Blueprints, a feature we’ve already had for regular buildables, allowing you to quickly toggle through Blueprints in the same sub-category by pressing or holding ‘E’, without leaving the build mode. 

We’ve also added a Nudge Mode for all buildables! Using it will lock the current hologram in place, so you can move around freely to check its placement from different directions. From there you are then able to nudge the hologram around to adjust the placement, if necessary, before building it. While this feature is available for all buildables, it is particularly useful for Blueprints and other large buildings. 

### Changes to the world

We didn’t make any changes to Resource Nodes this time around and any terrain changes we’ve done are minor, so your factories should be safe. In Update 8 we instead polished a number of areas in terms of visuals, atmosphere, and gameplay elements. Lots of work has gone into all of this, so to get an overview on what’s changed you can read the next parts below and/or look at this video covering it in a little more detail: <https://youtu.be/6X4jqMUtCwI>

#### Visuals

Titan Forest and Red Jungle have received the most significant overhaul for their foliage, visual and sound effects, as well as lighting. 

Many areas have received more polish, those being the Abyss Cliffs, Rocky Desert, Eastern Dune Forest, Spire Coast, and some of the caves as well. 

We also updated and improved the vista around the world, which has a huge impact on the look and feel of the areas at the edge on the map. With this one we are not fully done yet, but it is certainly an upgrade, and are excited for you to see the direction it is taking. 

#### Gameplay

In terms of gameplay in the world, we are adding two new variants to the Hogs: The Cliff Hog and Nuclear Hog! They are the most menacing members of their family, defending their territory with devastating charges, and in case of the Nuclear Hog, also radiation. 

We’ve also polished and updated placements of creatures, hazards, and collectables in many areas of the world, Such as Titan Forest, Red Jungle, Spire Coast, Grass Fields, Crater Lakes, Western Beaches, Abyss Cliffs, Coin Tree Forest, Dune Desert, Northern Forest and most of their sub areas. 

We also did a preliminary pass of Bamboo Fields and Rocky Desert as well to prepare them for Experimental Release, though there may still be changes on them in the future. 

#### Atmosphere

It was time for us to take a look at lighting and sound in the world, both with the upgrade to Unreal Engine 5 and just in general to polish things up and get rid of lingering issues. In terms of lighting, we’ve done full passes over all starting areas; Grass Fields, Rocky Desert, Northern Forest and Dune Desert, the Titan Forest, Red Jungle and Spire Coast to elevate their look and feel further and fix existing issues. 

When it comes to sound improvements and clean-up in the world, we’ve passed all the same areas and several more. You can find all the details in the patch notes below! 

### Advanced Game Settings

We are adding a number of settings that will allow you to customise your experience quite heavily when it comes to removing restrictions inherent to Satisfactory. These Advanced Game Settings can alter the experience drastically, so you can either enable them when creating a new game or when converting your existing save to using these settings when loading a save from the main menu. 

There is a full list of all new settings in the detailed patch notes below, but they include things such as Flight Mode making traversal and building freely a non-issue, No Build Cost which means buildables no longer need the required items to be built, Set Starting Tier allowing you to start a new game with everything up to that point unlocked and some resources to get started quickly, and No Stinger Mode fully removing the spidery Stinger enemy from the game. 

Many of these settings change restrictions that are part of what makes Satisfactory what it is, but we also know that people find their fun in games in different ways, and we wanted to give you the option to experiment with that and find out how you enjoy Satisfactory the most. 

Here is our video covering all of this in detail: <https://youtu.be/T2lOiHtygVM>

### Priority Power Switch & Power Tower

Both of these features can make a significant change in how you set up your power grid. We’ve got a summary for what they can do below, or you can watch Jace talk about them in this video: <https://youtu.be/v4mbNy3gt7c>

The Priority Power Switch allows you to organise sections of your power grid into different priorities. So, if your power would fail, the Priority Power Switches turn off in order of their set priority, shutting of the parts of your factory gated behind them until there is enough power available for the remainder of your grid to keep running. 

While they are great to prevent full power outages, they can also be switched off and on remotely from any other Priority Power Switch, allowing you to remotely control which parts of your factory are running. 

The Power Tower is a large building allowing you to connect power lines over longer distances. It comes in two versions, one with a ladder and platform that make them and excellent combination with the Zipline, and one version without for a cleaner look. 

### Quality of life and other improvements

It wouldn’t be our usual updates if there weren’t several miscellaneous improvements to features and quality of life for Satisfactory included in the Update, so let’s take a quick look at these as well! 

#### Destructible Gas Pillars

With Update 8 you’ll be able to blow up Gas Pillars using the Nobelisk! We’ve been wanting to add this for a while, and it is finally in the game. After unlocking Nobelisks you won’t have to worry anymore about odd Gas Pillars disrupting how you can build your factories. 

#### Jetpack fuels

The Jetpack can now use a selection of fuels with different burn rates and acceleration. Thanks to this the Jetpack can be used before automating fuel with Solid Biofuel, and in the late game you can even use Turbofuel which has unparalleled acceleration. 

#### Parachute

This feature has received some changes to make it a viable tool in the early to mid-game. For one, the Parachute no longer gets consumed when used, so you can now make one and use it for as long as you want. 

It now has a standard and sprint speed, which match the Bladerunner speeds, and we balanced it to be an excellent tool for making longer jumps while exploring and traversing your factory. Of course, it also retains its signature function of preventing fall damage in any dicey situations you might find yourself in. 

#### Dismantle Filter

We’ve added a filter to the Dismantle Mode where you can hover over a specific type of building, such as a Constructor, and select it to your dismantle filter. While remaining in Dismantle Mode you will only highlight the selected type of building for dismantling, making it much easier to dismantle specific parts of your factory while avoiding removing the other parts you want to keep by accident, such as Foundations. 

You can switch the filter freely while dismantling, and it works with both the new Blueprint Dismantle Mode and Mass Dismantle! 

If you want to see these changes in action before trying them out yourself, you can check out this video we made: <https://youtu.be/9jDBEpAlS2s>

## Patch notes

### Factory

  * Added the [Power Tower](/wiki/Power_Tower "Power Tower") and [Power Tower Platform](/wiki/Power_Tower_Platform "Power Tower Platform")
    * Unlocked in [Tier 4](/wiki/Tier_4 "Tier 4"): Expanded Power Infrastructure
  * Added the [Priority Power Switch](/wiki/Priority_Power_Switch "Priority Power Switch")
    * Unlocked in [MAM: Caterium](/wiki/Caterium_Research "Caterium Research")



### Advanced Game Settings

  * Added several [Advanced Game Settings](/wiki/Advanced_Game_Settings "Advanced Game Settings") that can be enabled when starting a new game or loading a save from the main menu: 
    * Flight mode: Player can fly
    * God mode: Player takes no [damage](/wiki/Damage "Damage") (will still die from leaving the map)
    * Give items: Player can add items to their inventory
    * No build cost: Buildables cost nothing to build
    * No unlock cost: Unlocks cost nothing to unlock
    * Unlock alternative recipes instantly: [Alternate recipes](/wiki/Alternate_recipes "Alternate recipes") unlock as soon as all requirements are met (removes need for Hard Drives)
    * No power: Buildings don’t consume power
    * Set starting tier: The session will start at the selected Tier and players will receive a starting set of items
    * Set game phase: Unlocks all phases before
    * Unlock all Tiers/MAM/Shop/Phases: Unlocks everything in the selected progression branch
    * Respawn settings: Player can set what they keep on them when respawning (everything, only equipped items, nothing)
    * Disable arachnid creatures: Disables the spawning of [Stingers](/wiki/Stinger "Stinger") in the session



### Equipment

  * Added support for using different [fuel](/wiki/Fuels "Fuels") types in the [Jetpack](/wiki/Jetpack "Jetpack")
    * [Solid Biofuel](/wiki/Solid_Biofuel "Solid Biofuel")
    * [Liquid Biofuel](/wiki/Packaged_Liquid_Biofuel "Packaged Liquid Biofuel")
    * [Fuel](/wiki/Packaged_Fuel "Packaged Fuel")
    * [Turbo Fuel](/wiki/Packaged_Turbofuel "Packaged Turbofuel")
  * Jetpack can now refuel while the player is on a [Zipline](/wiki/Zipline "Zipline")
  * [Parachute](/wiki/Parachute "Parachute") changes 
    * The Parachute is no longer consumed after usage and the stack size is now 1, making it function the same as other back slot equipment, such as the Jetpack
    * Added a Sprint Mode to the Parachute, allowing for slow and fast movement
    * Increased the maximum speed and descending speed, allowing for improved gliding
  * [Zipline](/wiki/Zipline "Zipline") changes 
    * The Zipline now automatically connects to the next [Power Line](/wiki/Power_Line "Power Line") while ziplining on [Power Towers](/wiki/Power_Tower "Power Tower") and [ceiling connections](/wiki/Wall_Outlet "Wall Outlet")
      * This will not work if the angle between the Power Lines exceeds 60 degrees
      * If the Zipline can move along more than one Power Line the direction can be controlled by looking at the desired direction or by holding the directional movement input
    * Reduced maximum Zipline Sprint Speed to 100 km/h (due to the previous maximum speed being too high for the world loading)
    * Increased the Zipline Sprint acceleration to be nearly instant
    * The Zipline can now be toggled on/off by pressing the secondary equipment input (RMB by default), which allows ziplining without needing to hold down the primary equipment input (LMB by default)
  * Weapon balancing 
    * Fire rate and damage balancing done to the [Homing Rifle ammo](/wiki/Homing_Rifle_Ammo "Homing Rifle Ammo")
    * Weapon spread and damage balancing done to the [Turbo Rifle ammo](/wiki/Turbo_Rifle_Ammo "Turbo Rifle Ammo")
    * Minor damage reductions on [Iron, Stun, and Explosive Rebar ammo](/wiki/Rebar_Gun "Rebar Gun")



### Creatures

  * Added [Cliff Hog](/wiki/Cliff_Hog "Cliff Hog")
    * Higher health, damage, size, and speed relative to the [Alpha Hog](/wiki/Alpha_Hog "Alpha Hog")
    * Basic Hog Charge attack, with increased speed and damage
    * New Rock Throw attack, which launches a rock at a distant or unreachable target
    * New Plow Charge attack, which continually pushes and deals damage to the target
  * Added [Nuclear Hog](/wiki/Nuclear_Hog "Nuclear Hog")
    * Higher health, damage, size, and speed relative to the Cliff Hog
    * Basic Hog Charge attack, with increased speed and damage
    * New Rock Throw attack, which launches a rock at a distant or unreachable target
    * New Plow Charge attack, which continually pushes and deals damage to the target
    * Passive [Radiation](/wiki/Radiation "Radiation") Damage area of effect
  * Creature health and damage balancing 
    * Reduced the health of [Small Desert and Aquatic Spitters](/wiki/Spitter "Spitter") from 30 to 20
    * Increased health of [Alpha Forest Spitter](/wiki/Alpha_Spitter "Alpha Spitter") from 60 to 80



### Vehicles

  * Moved [vehicle](/wiki/Vehicles "Vehicles") physics to using Chaos
  * Overhauled all vehicle sounds
  * Improved the manual driving of all vehicles
  * Reworked all vehicle trunks visually simplifying the animation and adding a new sound
  * Added functionality for vehicles to deal damage to creatures by hitting them
  * Damage dealt is relative to vehicle speed and size



### World

  * [Gas Pillars](/wiki/Gas_Pillar "Gas Pillar") can now be destroyed by explosives such as the Nobelisk
  * Titan Forest 
    * Major overhaul of the area and foliage
    * Updated creature, hazard, and reward placements
    * Improved lighting and atmosphere in the area
    * Improved sound in the area
  * Red Jungle 
    * Major overhaul of the area and foliage
    * Updated creature, hazard, and reward placements
    * Improved lighting and atmosphere in the area
    * Improved sound in the area
  * Rocky Desert 
    * Polished foliage assets and placement
    * Minor tweaks to creature, hazard, and rewards, but there are more changes we intend to make in the future
    * Improved lighting and atmosphere in the area
    * Improved sound in the area
  * Grass Fields 
    * Polished foliage assets and placement, also for the Grass Crater and Snake Tree Forest Sub biomes
    * Updated creature, hazard, and reward placements
    * Improved lighting and atmosphere in the area
    * Improved sound in the area
  * Northern Forest 
    * Updated creature, hazard, and reward placements
    * Improved lighting and atmosphere in the area
    * Improved sound in the area
  * Dune Desert 
    * Updated creature, hazard, and reward placements
    * Improved lighting and atmosphere in the area
    * Improved sound in the area
  * Abyss Cliffs 
    * Polished foliage placement and replaced old assets
    * Added creature, hazard, and reward placements
    * Preliminary sound improvements in the area
  * Eastern Dune Forest 
    * Polished foliage placement, landscape painting, and the Coin Forest sub biome
    * Minor tweaks to creature, hazard, and rewards, but there are more changes we intend to make in the future
    * Preliminary sound improvements in the area
  * Crater Lakes 
    * Updated creature, hazard, and reward placements
    * Preliminary sound improvements in the area
  * Western Beaches 
    * Updated creature, hazard, and reward placements
    * Preliminary sound improvements in the area
  * Spire Coast 
    * Updated creature, hazard, and reward placements
    * Overhauled lighting and atmosphere in the area
    * Overhauled sound in the area
  * Bamboo Fields 
    * Some changes to foliage have been made, but there are more changes we intend to make later to fix any remaining issues
    * Improved sound in the area
    * Added the new prototype of the world perimeter, which we will continue working on in the future
    * Overhauled the look and gameplay of several caves



### Quality of Life

  * Added the ability to lock a hologram in place with [`H`](/wiki/Controls "Controls") by default while in Build Mode, allowing players to inspect the placement before building
  * Added the ability to nudge a locked hologram with the arrow keys by default, allowing players to adjust the placement before building
  * Added a directional indicator to the [Blueprint](/wiki/Blueprint "Blueprint") hologram
  * Added a Blueprints Dismantle Mode that can be switched on in the regular Dismantle Mode, allowing an entire Blueprint to be dismantled at once
  * Added Quick Switch functionality to Blueprints, allowing the player to quickly switch between Blueprints in the same sub-category
  * Added Sample functionality to Blueprints (can only be sampled when in Blueprint Dismantle Mode)
  * Added a Dismantle Filter to the Dismantle Mode, allowing the player to select a specific buildable to dismantle and ignore all other buildables
  * Added automatic placement of a [Conveyor](/wiki/Conveyor_Poles "Conveyor Poles") or [Pipe pole](/wiki/Pipeline_Supports "Pipeline Supports") when not building a [Belt](/wiki/Conveyor_Belt "Conveyor Belt") or [Pipe](/wiki/Pipeline "Pipeline") from an existing connection point
  * Changed the Quick Switching of Conveyor Belt, Lift, and Pipe Mk.’s to no longer revert back to the first placement step
  * Moved validation check for building Conveyors and Pipes to final placement step
  * [Somersloops](/wiki/Somersloop "Somersloop") and [Mercer Spheres](/wiki/Mercer_Sphere "Mercer Sphere") can no longer be deleted in the inventory
  * Made the automatic power connections when building Power Lines context sensitive, copying the same type of pole the Power Line was initially connected to
  * Added the option to upgrade [Splitters](/wiki/Splitter "Splitter") (regular, [Smart](/wiki/Smart_Splitter "Smart Splitter"), [Programmable](/wiki/Programmable_Splitter "Programmable Splitter")) by holding [`Ctrl`](/wiki/Controls "Controls") (default input) while aiming any Splitter variant hologram at any other already build Splitter variant



### Balancing

  * Changed the [Parachute](/wiki/Parachute "Parachute") recipe to only produce 1 at a time and increased the cost of a single Parachute
  * Removed the option to purchase Parachutes from the [AWESOME Shop](/wiki/AWESOME_Shop "AWESOME Shop")
  * Added a new milestone to [Tier 4](/wiki/Tier_4 "Tier 4"): ‘Expanded Power Infrastructure’
  * Moved the [Power Storage](/wiki/Power_Storage "Power Storage") unlock to Tier 4: Expanded Power Infrastructure
  * Added the [Power Tower](/wiki/Power_Tower "Power Tower") and [Power Tower Platform](/wiki/Power_Tower_Platform "Power Tower Platform") to Tier 4: Expanded Power Infrastructure
  * Renamed the [Tier 6](/wiki/Tier_6 "Tier 6") milestone ‘Expanded Power Infrastructure’ to ‘Logistics Mk.4’
  * Moved the location of the [Power Poles Mk.3](/wiki/Power_Pole_Mk.3 "Power Pole Mk.3") unlock in the MAM: Caterium research tree
  * Reduced the [High-Speed Connector](/wiki/High-Speed_Connector "High-Speed Connector") cost of the Power Poles Mk.3 research from 100 to 50
  * Added the [Priority Power Switch](/wiki/Priority_Power_Switch "Priority Power Switch") unlock to the [MAM: Caterium](/wiki/Caterium_Research "Caterium Research") research tree



### UI

  * Updated UI to work with the new UE5 Input System
  * Re-worked the [options](/wiki/Settings "Settings") menus and key binding menu
  * Added a search bar in the options and key binding menu
  * Re-worked the main menu and new game menu
  * Added functionality to change the preferred fuel of equipped Jetpack in inventory window
  * Improved UI memory usage
  * Added UI for selecting Dismantle Modes
  * Added Dark Mode for the [A.W.E.S.O.M.E. Shop](/wiki/AWESOME_Shop "AWESOME Shop")
  * Added Quick Switch functionality to Blueprints
  * Rewrote descriptions for video and graphical settings to be clearer to understand
  * Updated the credits :D



### Player character

  * The [player character](/wiki/Pioneer "Pioneer") now respawns with the equipment that was equipped on death still equipped
  * Reworked and improved the player character footstep sounds



### Systems

  * Overhauled the foliage system to be compatible with Unreal Engine 5
  * Some adjustments in the power system, no changes should be noticeable during play
  * Migrated all inputs to the new Enhanced Input System



### Optimization

  * Optimized the [save](/wiki/Save_file "Save file") system to decrease saving time on larger saves by roughly 80-90%
  * Optimized significance manager to be ISPC accelerated
  * Converted to World Partitioning (Work in progress)
  * Deprecated World composition implementation
  * Added streaming scalability for foliage streaming cells 
    * Foliage cells can now be loaded from different ranges 
      * Near, Default, Far, Cinematic
  * Optimized Signs 
    * Signs will now share when same configuration is found
    * Emissive only signs are handled in a more performant way
  * Re-implemented conveyor rendering system to work well with Nanite
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
  * Minor optimizations for the Conveyor tick



### Bug fixes

  * Fixed a potential bug with [drone](/wiki/Drone "Drone") queue processing
  * Fixed shadow flickering
  * Fixed so [trains](/wiki/Train "Train") do not have to wait 2 seconds for pathfinding (a cooldown) when loading a save. This fixed a case where a train could take a wrong turn on load if it was close enough to a switch.



### Known issues

  * The first time booting the game will be very slow, but that should not continue to happen after the first boot
  * Game can hang on quit
  * Performance loss when running out of VRAM
  * Lights don’t behave correctly in Lumen compared with Signs
  * Factory Animation tick reductions can be slightly too aggressive
  * TSR can cause visual issues with conveyor belts, you can try using the following console command to alleviate the issues, but this will reduce AntiAliasing quality
  * r.TSR.ShadingRejection.Flickering 0



## Media

### Videos

Load video

YouTube

YouTube might collect personal data. [Privacy Policy](https://www.youtube.com/howyoutubeworks/user-settings/privacy/)

ContinueDismiss

Patch Notes

Load video

YouTube

YouTube might collect personal data. [Privacy Policy](https://www.youtube.com/howyoutubeworks/user-settings/privacy/)

ContinueDismiss

Launch Stream

Load video

YouTube

YouTube might collect personal data. [Privacy Policy](https://www.youtube.com/howyoutubeworks/user-settings/privacy/)

ContinueDismiss

Unreal Engine 5

  * [v](/wiki/Template:PatchesNav "Template:PatchesNav")
  * [e](https://satisfactory.wiki.gg/wiki/Template:PatchesNav?action=edit)
  * [h](https://satisfactory.wiki.gg/wiki/Template:PatchesNav?action=history)

[Patches](/wiki/Category:Patch_notes "Category:Patch notes")  
---  
1.1| [1.1.1.0](/wiki/Patch_1.1.1.0 "Patch 1.1.1.0") • [1.1.1.1](/wiki/Patch_1.1.1.1 "Patch 1.1.1.1") • [1.1.1.2](/wiki/Patch_1.1.1.2 "Patch 1.1.1.2") • [1.1.1.3](/wiki/Patch_1.1.1.3 "Patch 1.1.1.3") • [1.1.1.4](/wiki/Patch_1.1.1.4 "Patch 1.1.1.4")  
Experimental 1.1| [1.1.0.0](/wiki/Patch_1.1.0.0 "Patch 1.1.0.0") • [1.1.0.1](/wiki/Patch_1.1.0.1 "Patch 1.1.0.1") • [1.1.0.2](/wiki/Patch_1.1.0.2 "Patch 1.1.0.2") • [1.1.0.3](/wiki/Patch_1.1.0.3 "Patch 1.1.0.3") • [1.1.0.4](/wiki/Patch_1.1.0.4 "Patch 1.1.0.4") • [1.1.0.5](/wiki/Patch_1.1.0.5 "Patch 1.1.0.5") • [1.1.0.6](/wiki/Patch_1.1.0.6 "Patch 1.1.0.6") • [1.1.1.5](/wiki/Patch_1.1.1.5 "Patch 1.1.1.5") • [1.1.1.6](/wiki/Patch_1.1.1.6 "Patch 1.1.1.6")  
1.0| [1.0](/wiki/Patch_1.0 "Patch 1.0") • [1.0.0.1](/wiki/Patch_1.0.0.1 "Patch 1.0.0.1") • [1.0.0.2](/wiki/Patch_1.0.0.2 "Patch 1.0.0.2") • [1.0.0.3](/wiki/Patch_1.0.0.3 "Patch 1.0.0.3") • [1.0.0.4](/wiki/Patch_1.0.0.4 "Patch 1.0.0.4") • [1.0.0.5](/wiki/Patch_1.0.0.5 "Patch 1.0.0.5") • [1.0.0.6](/wiki/Patch_1.0.0.6 "Patch 1.0.0.6") • [1.0.0.7](/wiki/Patch_1.0.0.7 "Patch 1.0.0.7") • [1.0.1.0](/wiki/Patch_1.0.1.0 "Patch 1.0.1.0") • [1.0.1.1](/wiki/Patch_1.0.1.1 "Patch 1.0.1.1") • [1.0.1.2](/wiki/Patch_1.0.1.2 "Patch 1.0.1.2") • [1.0.1.3](/wiki/Patch_1.0.1.3 "Patch 1.0.1.3") • [1.0.1.4](/wiki/Patch_1.0.1.4 "Patch 1.0.1.4")  
Experimental 1.0| [1.0.1.5](/wiki/Patch_1.0.1.5 "Patch 1.0.1.5") • [1.0.1.6](/wiki/Patch_1.0.1.6 "Patch 1.0.1.6")  
Update 8| [0.8.3.0](/wiki/Patch_0.8.3.0 "Patch 0.8.3.0") • [0.8.3.2](/wiki/Patch_0.8.3.2 "Patch 0.8.3.2") • [0.8.3.3](/wiki/Patch_0.8.3.3 "Patch 0.8.3.3")  
Experimental Update 8| 0.8.0.0 • [0.8.0.1](/wiki/Patch_0.8.0.1 "Patch 0.8.0.1") • [0.8.0.2](/wiki/Patch_0.8.0.2 "Patch 0.8.0.2") • [0.8.0.3](/wiki/Patch_0.8.0.3 "Patch 0.8.0.3") • [0.8.0.4](/wiki/Patch_0.8.0.4 "Patch 0.8.0.4") • [0.8.0.5](/wiki/Patch_0.8.0.5 "Patch 0.8.0.5") • [0.8.1.0](/wiki/Patch_0.8.1.0 "Patch 0.8.1.0") • [0.8.1.1](/wiki/Patch_0.8.1.1 "Patch 0.8.1.1") • [0.8.1.2](/wiki/Patch_0.8.1.2 "Patch 0.8.1.2") • [0.8.1.3](/wiki/Patch_0.8.1.3 "Patch 0.8.1.3") • [0.8.2.0](/wiki/Patch_0.8.2.0 "Patch 0.8.2.0") • [0.8.2.1](/wiki/Patch_0.8.2.1 "Patch 0.8.2.1") • [0.8.2.2](/wiki/Patch_0.8.2.2 "Patch 0.8.2.2") • [0.8.2.3](/wiki/Patch_0.8.2.3 "Patch 0.8.2.3") • [0.8.2.4](/wiki/Patch_0.8.2.4 "Patch 0.8.2.4") • [0.8.2.5](/wiki/Patch_0.8.2.5 "Patch 0.8.2.5") • [0.8.2.6](/wiki/Patch_0.8.2.6 "Patch 0.8.2.6") • [0.8.2.7](/wiki/Patch_0.8.2.7 "Patch 0.8.2.7") • [0.8.2.8](/wiki/Patch_0.8.2.8 "Patch 0.8.2.8") • [0.8.2.9](/wiki/Patch_0.8.2.9 "Patch 0.8.2.9") • [0.8.3.1](/wiki/Patch_0.8.3.1 "Patch 0.8.3.1")  
Update 7| [0.7.0.8](/wiki/Patch_0.7.0.8 "Patch 0.7.0.8") • [0.7.1.1](/wiki/Patch_0.7.1.1 "Patch 0.7.1.1")  
Experimental Update 7| [0.7.0.0](/wiki/Patch_0.7.0.0 "Patch 0.7.0.0") • [0.7.0.1](/wiki/Patch_0.7.0.1 "Patch 0.7.0.1") • [0.7.0.2](/wiki/Patch_0.7.0.2 "Patch 0.7.0.2") • [0.7.0.3](/wiki/Patch_0.7.0.3 "Patch 0.7.0.3") • [0.7.0.4](/wiki/Patch_0.7.0.4 "Patch 0.7.0.4") • [0.7.0.5](/wiki/Patch_0.7.0.5 "Patch 0.7.0.5") • [0.7.0.6](/wiki/Patch_0.7.0.6 "Patch 0.7.0.6") • [0.7.0.7](/wiki/Patch_0.7.0.7 "Patch 0.7.0.7") • [0.7.0.8 (Experimental)](/wiki/Patch_0.7.0.8_\(Experimental\) "Patch 0.7.0.8 \(Experimental\)")  
Update 6| [0.6.1.0](/wiki/Patch_0.6.1.0 "Patch 0.6.1.0") • [0.6.1.1](/wiki/Patch_0.6.1.1 "Patch 0.6.1.1") • [0.6.1.2](/wiki/Patch_0.6.1.2 "Patch 0.6.1.2") • [0.6.1.3](/wiki/Patch_0.6.1.3 "Patch 0.6.1.3") • [0.6.1.4](/wiki/Patch_0.6.1.4 "Patch 0.6.1.4") • [0.6.1.5](/wiki/Patch_0.6.1.5 "Patch 0.6.1.5")  
Experimental Update 6| [0.6.0.0](/wiki/Patch_0.6.0.0 "Patch 0.6.0.0") • [0.6.0.1](/wiki/Patch_0.6.0.1 "Patch 0.6.0.1") • [0.6.0.2](/wiki/Patch_0.6.0.2 "Patch 0.6.0.2") • [0.6.0.3](/wiki/Patch_0.6.0.3 "Patch 0.6.0.3") • [0.6.0.4](/wiki/Patch_0.6.0.4 "Patch 0.6.0.4") • [0.6.0.5](/wiki/Patch_0.6.0.5 "Patch 0.6.0.5") • [0.6.0.6](/wiki/Patch_0.6.0.6 "Patch 0.6.0.6") • [0.6.0.7](/wiki/Patch_0.6.0.7 "Patch 0.6.0.7") • [0.6.0.8](/wiki/Patch_0.6.0.8 "Patch 0.6.0.8") • [0.6.0.9](/wiki/Patch_0.6.0.9 "Patch 0.6.0.9") • [0.6.0.10](/wiki/Patch_0.6.0.10 "Patch 0.6.0.10") • [0.6.0.11](/wiki/Patch_0.6.0.11 "Patch 0.6.0.11") • [0.6.0.12](/wiki/Patch_0.6.0.12 "Patch 0.6.0.12") • [0.6.0.13](/wiki/Patch_0.6.0.13 "Patch 0.6.0.13") • [0.6.0.14](/wiki/Patch_0.6.0.14 "Patch 0.6.0.14") • [0.6.0.15](/wiki/Patch_0.6.0.15 "Patch 0.6.0.15")  
Update 5| [0.5.1.0](/wiki/Patch_0.5.1.0 "Patch 0.5.1.0") • [0.5.1.1](/wiki/Patch_0.5.1.1 "Patch 0.5.1.1") • [0.5.1.3](/wiki/Patch_0.5.1.3 "Patch 0.5.1.3") • [0.5.1.4](/wiki/Patch_0.5.1.4 "Patch 0.5.1.4") • [0.5.1.5](/wiki/Patch_0.5.1.5 "Patch 0.5.1.5") • [0.5.1.7](/wiki/Patch_0.5.1.7 "Patch 0.5.1.7") • [0.5.1.8](/wiki/Patch_0.5.1.8 "Patch 0.5.1.8") • [0.5.1.10](/wiki/Patch_0.5.1.10 "Patch 0.5.1.10") • [0.5.2.0](/wiki/Patch_0.5.2.0 "Patch 0.5.2.0") • [0.5.2.1](/wiki/Patch_0.5.2.1 "Patch 0.5.2.1")  
Experimental Update 5| [0.5.0.0](/wiki/Patch_0.5.0.0 "Patch 0.5.0.0") • [0.5.0.1](/wiki/Patch_0.5.0.1 "Patch 0.5.0.1") • [0.5.0.2](/wiki/Patch_0.5.0.2 "Patch 0.5.0.2") • [0.5.0.3](/wiki/Patch_0.5.0.3 "Patch 0.5.0.3") • [0.5.0.4](/wiki/Patch_0.5.0.4 "Patch 0.5.0.4") • [0.5.0.5](/wiki/Patch_0.5.0.5 "Patch 0.5.0.5") • [0.5.0.6](/wiki/Patch_0.5.0.6 "Patch 0.5.0.6") • [0.5.0.7](/wiki/Patch_0.5.0.7 "Patch 0.5.0.7") • [0.5.0.8](/wiki/Patch_0.5.0.8 "Patch 0.5.0.8") • [0.5.0.9](/wiki/Patch_0.5.0.9 "Patch 0.5.0.9") • [0.5.0.10](/wiki/Patch_0.5.0.10 "Patch 0.5.0.10") • [0.5.0.11](/wiki/Patch_0.5.0.11 "Patch 0.5.0.11") • [0.5.0.12](/wiki/Patch_0.5.0.12 "Patch 0.5.0.12") • [0.5.0.13](/wiki/Patch_0.5.0.13 "Patch 0.5.0.13") • [0.5.0.14](/wiki/Patch_0.5.0.14 "Patch 0.5.0.14") • [0.5.1.2](/wiki/Patch_0.5.1.2 "Patch 0.5.1.2") • [0.5.1.6](/wiki/Patch_0.5.1.6 "Patch 0.5.1.6") • [0.5.1.9](/wiki/Patch_0.5.1.9 "Patch 0.5.1.9") • [0.5.1.11](/wiki/Patch_0.5.1.11 "Patch 0.5.1.11") • [0.5.1.12](/wiki/Patch_0.5.1.12 "Patch 0.5.1.12") • [0.5.1.13](/wiki/Patch_0.5.1.13 "Patch 0.5.1.13")  
Update 4| [0.4.1.0](/wiki/Patch_0.4.1.0 "Patch 0.4.1.0") • [0.4.1.1](/wiki/Patch_0.4.1.1 "Patch 0.4.1.1") • [0.4.2.0](/wiki/Patch_0.4.2.0 "Patch 0.4.2.0") • [0.4.2.2](/wiki/Patch_0.4.2.2 "Patch 0.4.2.2") • [0.4.2.5](/wiki/Patch_0.4.2.5 "Patch 0.4.2.5") • [0.4.2.7](/wiki/Patch_0.4.2.7 "Patch 0.4.2.7") • [0.4.2.9](/wiki/Patch_0.4.2.9 "Patch 0.4.2.9") • [0.4.2.11](/wiki/Patch_0.4.2.11 "Patch 0.4.2.11")  
Experimental Update 4| [0.4.0.0](/wiki/Patch_0.4.0.0 "Patch 0.4.0.0") • [0.4.0.1](/wiki/Patch_0.4.0.1 "Patch 0.4.0.1") • [0.4.0.2](/wiki/Patch_0.4.0.2 "Patch 0.4.0.2") • [0.4.0.3](/wiki/Patch_0.4.0.3 "Patch 0.4.0.3") • [0.4.0.4](/wiki/Patch_0.4.0.4 "Patch 0.4.0.4") • [0.4.0.5](/wiki/Patch_0.4.0.5 "Patch 0.4.0.5") • [0.4.0.6](/wiki/Patch_0.4.0.6 "Patch 0.4.0.6") • [0.4.0.7](/wiki/Patch_0.4.0.7 "Patch 0.4.0.7") • [0.4.0.8](/wiki/Patch_0.4.0.8 "Patch 0.4.0.8") • [0.4.0.9](/wiki/Patch_0.4.0.9 "Patch 0.4.0.9") • [0.4.0.10](/wiki/Patch_0.4.0.10 "Patch 0.4.0.10") • [0.4.0.11](/wiki/Patch_0.4.0.11 "Patch 0.4.0.11") • [0.4.0.12](/wiki/Patch_0.4.0.12 "Patch 0.4.0.12") • [0.4.2.1](/wiki/Patch_0.4.2.1 "Patch 0.4.2.1") • [0.4.2.2 (Experimental)](/wiki/Patch_0.4.2.2_\(Experimental\) "Patch 0.4.2.2 \(Experimental\)") • [0.4.2.3](/wiki/Patch_0.4.2.3 "Patch 0.4.2.3") • [0.4.2.4](/wiki/Patch_0.4.2.4 "Patch 0.4.2.4") • [0.4.2.6](/wiki/Patch_0.4.2.6 "Patch 0.4.2.6") • [0.4.2.8](/wiki/Patch_0.4.2.8 "Patch 0.4.2.8") • [0.4.2.10](/wiki/Patch_0.4.2.10 "Patch 0.4.2.10") • [0.4.3.0](/wiki/Patch_0.4.3.0 "Patch 0.4.3.0") • [0.4.3.1](/wiki/Patch_0.4.3.1 "Patch 0.4.3.1")  
Update 3  
& Steam Release| [0.3.3.3](/wiki/Patch_0.3.3.3 "Patch 0.3.3.3") • [0.3.3.4](/wiki/Patch_0.3.3.4 "Patch 0.3.3.4") • [0.3.3.5](/wiki/Patch_0.3.3.5 "Patch 0.3.3.5") • [0.3.3.6](/wiki/Patch_0.3.3.6 "Patch 0.3.3.6") • [0.3.4.14](/wiki/Patch_0.3.4.14 "Patch 0.3.4.14") • [0.3.4.15](/wiki/Patch_0.3.4.15 "Patch 0.3.4.15") • [0.3.4.16](/wiki/Patch_0.3.4.16 "Patch 0.3.4.16") • [0.3.5](/wiki/Patch_0.3.5 "Patch 0.3.5") • [0.3.5.1](/wiki/Patch_0.3.5.1 "Patch 0.3.5.1") • [0.3.5.2](/wiki/Patch_0.3.5.2 "Patch 0.3.5.2") • [0.3.5.3](/wiki/Patch_0.3.5.3 "Patch 0.3.5.3") • [0.3.5.4](/wiki/Patch_0.3.5.4 "Patch 0.3.5.4") • [0.3.5.6](/wiki/Patch_0.3.5.6 "Patch 0.3.5.6") • [0.3.6.5](/wiki/Patch_0.3.6.5 "Patch 0.3.6.5") • [0.3.7](/wiki/Patch_0.3.7 "Patch 0.3.7") • [0.3.7.1](/wiki/Patch_0.3.7.1 "Patch 0.3.7.1") • [0.3.7.2](/wiki/Patch_0.3.7.2 "Patch 0.3.7.2") • [0.3.7.3](/wiki/Patch_0.3.7.3 "Patch 0.3.7.3") • [0.3.7.4](/wiki/Patch_0.3.7.4 "Patch 0.3.7.4") • [0.3.7.5](/wiki/Patch_0.3.7.5 "Patch 0.3.7.5") • [0.3.7.6](/wiki/Patch_0.3.7.6 "Patch 0.3.7.6") • [0.3.7.7](/wiki/Patch_0.3.7.7 "Patch 0.3.7.7")  
Experimental Update 3  
& Steam Release| [0.3](/wiki/Patch_0.3 "Patch 0.3") • [0.3.0.1](/wiki/Patch_0.3.0.1 "Patch 0.3.0.1") • [0.3.0.2](/wiki/Patch_0.3.0.2 "Patch 0.3.0.2") • [0.3.1.0](/wiki/Patch_0.3.1.0 "Patch 0.3.1.0") • [0.3.1.1](/wiki/Patch_0.3.1.1 "Patch 0.3.1.1") • [0.3.1.2](/wiki/Patch_0.3.1.2 "Patch 0.3.1.2") • [0.3.2.0](/wiki/Patch_0.3.2.0 "Patch 0.3.2.0") • [0.3.2.1](/wiki/Patch_0.3.2.1 "Patch 0.3.2.1") • [0.3.2.2](/wiki/Patch_0.3.2.2 "Patch 0.3.2.2") • [0.3.3.0](/wiki/Patch_0.3.3.0 "Patch 0.3.3.0") • [0.3.3.1](/wiki/Patch_0.3.3.1 "Patch 0.3.3.1") • [0.3.3.2](/wiki/Patch_0.3.3.2 "Patch 0.3.3.2") • [0.3.3.4](/wiki/Patch_0.3.3.4 "Patch 0.3.3.4") • [0.3.3.5](/wiki/Patch_0.3.3.5 "Patch 0.3.3.5") • [0.3.4.0](/wiki/Patch_0.3.4.0 "Patch 0.3.4.0") • [0.3.4.1](/wiki/Patch_0.3.4.1 "Patch 0.3.4.1") • [0.3.4.2](/wiki/Patch_0.3.4.2 "Patch 0.3.4.2") • [0.3.4.3](/wiki/Patch_0.3.4.3 "Patch 0.3.4.3") • [0.3.4.4](/wiki/Patch_0.3.4.4 "Patch 0.3.4.4") • [0.3.4.5](/wiki/Patch_0.3.4.5 "Patch 0.3.4.5") • [0.3.4.6](/wiki/Patch_0.3.4.6 "Patch 0.3.4.6") • [0.3.4.7](/wiki/Patch_0.3.4.7 "Patch 0.3.4.7") • [0.3.4.8](/wiki/Patch_0.3.4.8 "Patch 0.3.4.8") • [0.3.4.9](/wiki/Patch_0.3.4.9 "Patch 0.3.4.9") • [0.3.4.10](/wiki/Patch_0.3.4.10 "Patch 0.3.4.10") • [0.3.4.11](/wiki/Patch_0.3.4.11 "Patch 0.3.4.11") • [0.3.4.12](/wiki/Patch_0.3.4.12 "Patch 0.3.4.12") • [0.3.4.13](/wiki/Patch_0.3.4.13 "Patch 0.3.4.13") • [0.3.5.5](/wiki/Patch_0.3.5.5 "Patch 0.3.5.5") • [0.3.6](/wiki/Patch_0.3.6 "Patch 0.3.6") • [0.3.6.1](/wiki/Patch_0.3.6.1 "Patch 0.3.6.1") • [0.3.6.2](/wiki/Patch_0.3.6.2 "Patch 0.3.6.2") • [0.3.6.3](/wiki/Patch_0.3.6.3 "Patch 0.3.6.3") • [0.3.6.4](/wiki/Patch_0.3.6.4 "Patch 0.3.6.4") • [0.3.6.6](/wiki/Patch_0.3.6.6 "Patch 0.3.6.6") • [0.3.6.7](/wiki/Patch_0.3.6.7 "Patch 0.3.6.7") • [0.3.6.8](/wiki/Patch_0.3.6.8 "Patch 0.3.6.8") • [0.3.6.9](/wiki/Patch_0.3.6.9 "Patch 0.3.6.9") • [0.3.6.10](/wiki/Patch_0.3.6.10 "Patch 0.3.6.10") • [0.3.6.11](/wiki/Patch_0.3.6.11 "Patch 0.3.6.11") • [0.3.6.12](/wiki/Patch_0.3.6.12 "Patch 0.3.6.12") • [0.3.6.13](/wiki/Patch_0.3.6.13 "Patch 0.3.6.13") • [0.3.8.0](/wiki/Patch_0.3.8.0 "Patch 0.3.8.0") • [0.3.8.1](/wiki/Patch_0.3.8.1 "Patch 0.3.8.1") • [0.3.8.2](/wiki/Patch_0.3.8.2 "Patch 0.3.8.2") • [0.3.8.3](/wiki/Patch_0.3.8.3 "Patch 0.3.8.3") • [0.3.8.4](/wiki/Patch_0.3.8.4 "Patch 0.3.8.4") • [0.3.8.5](/wiki/Patch_0.3.8.5 "Patch 0.3.8.5") • [0.3.8.6](/wiki/Patch_0.3.8.6 "Patch 0.3.8.6") • [0.3.8.7](/wiki/Patch_0.3.8.7 "Patch 0.3.8.7") • [0.3.8.8](/wiki/Patch_0.3.8.8 "Patch 0.3.8.8") • [0.3.8.9](/wiki/Patch_0.3.8.9 "Patch 0.3.8.9") • [0.3.8.10](/wiki/Patch_0.3.8.10 "Patch 0.3.8.10") • [0.3.8.11](/wiki/Patch_0.3.8.11 "Patch 0.3.8.11")  
Update 2| [0.2.1](/wiki/Patch_0.2.1 "Patch 0.2.1") • [0.2.1.1](/wiki/Patch_0.2.1.1 "Patch 0.2.1.1") • [0.2.1.2](/wiki/Patch_0.2.1.2 "Patch 0.2.1.2") • [0.2.1.3](/wiki/Patch_0.2.1.3 "Patch 0.2.1.3") • [ 0.2.1.4](/wiki/Patch_0.2.1.4 "Patch 0.2.1.4") • [ 0.2.1.5](/wiki/Patch_0.2.1.5 "Patch 0.2.1.5") • [0.2.1.7](/wiki/Patch_0.2.1.7 "Patch 0.2.1.7") • [0.2.1.10](/wiki/Patch_0.2.1.10 "Patch 0.2.1.10") • [0.2.1.12](/wiki/Patch_0.2.1.12 "Patch 0.2.1.12") • [0.2.1.17](/wiki/Patch_0.2.1.17 "Patch 0.2.1.17") • [0.2.1.18](/wiki/Patch_0.2.1.18 "Patch 0.2.1.18")  
Experimental Update 2| [0.1.14](/wiki/Patch_0.1.14 "Patch 0.1.14") • [0.1.15](/wiki/Patch_0.1.15 "Patch 0.1.15") • [0.1.16](/wiki/Patch_0.1.16 "Patch 0.1.16") • [0.1.17 (101256)](/wiki/Patch_0.1.17 "Patch 0.1.17") • [0.1.17 (101353)](/wiki/Patch_0.1.17_build_101353 "Patch 0.1.17 build 101353") • [0.1.19](/wiki/Patch_0.1.19 "Patch 0.1.19") • [0.1.20](/wiki/Patch_0.1.20 "Patch 0.1.20") • [0.2.1.6](/wiki/Patch_0.2.1.6 "Patch 0.2.1.6") • [0.2.1.7 (Experimental)](/wiki/Patch_0.2.1.7_\(Experimental\) "Patch 0.2.1.7 \(Experimental\)") • [0.2.1.8](/wiki/Patch_0.2.1.8 "Patch 0.2.1.8") • [0.2.1.9](/wiki/Patch_0.2.1.9 "Patch 0.2.1.9") • [0.2.1.11](/wiki/Patch_0.2.1.11 "Patch 0.2.1.11") • [0.2.1.12 (Experimental)](/wiki/Patch_0.2.1.12_\(Experimental\) "Patch 0.2.1.12 \(Experimental\)") • [0.2.1.13](/wiki/Patch_0.2.1.13 "Patch 0.2.1.13") • [0.2.1.14](/wiki/Patch_0.2.1.14 "Patch 0.2.1.14") • [0.2.1.15](/wiki/Patch_0.2.1.15 "Patch 0.2.1.15") • [0.2.1.16](/wiki/Patch_0.2.1.16 "Patch 0.2.1.16") • [0.2.1.17 (Experimental)](/wiki/Patch_0.2.1.17_\(Experimental\) "Patch 0.2.1.17 \(Experimental\)") • [0.2.1.19](/wiki/Patch_0.2.1.19 "Patch 0.2.1.19") • [0.2.1.20](/wiki/Patch_0.2.1.20 "Patch 0.2.1.20")  
Update 1| [0.1.11](/wiki/Patch_0.1.11 "Patch 0.1.11") • [0.1.12](/wiki/Patch_0.1.12 "Patch 0.1.12") • [0.1.13](/wiki/Patch_0.1.13 "Patch 0.1.13")  
Experimental Update 1| [0.1.5](/wiki/Patch_0.1.5 "Patch 0.1.5") • [0.1.6 (98394)](/wiki/Patch_0.1.6_build_98394 "Patch 0.1.6 build 98394") • [0.1.6 (98445)](/wiki/Patch_0.1.6_build_98445 "Patch 0.1.6 build 98445") • [0.1.7](/wiki/Patch_0.1.7 "Patch 0.1.7") • [0.1.8](/wiki/Patch_0.1.8 "Patch 0.1.8") • [0.1.9](/wiki/Patch_0.1.9 "Patch 0.1.9") • [0.1.10](/wiki/Patch_0.1.10 "Patch 0.1.10")  
Early Access Release| [0.1](/wiki/Patch_0.1 "Patch 0.1") • [0.101](/wiki/Patch_0.101 "Patch 0.101") • [0.102](/wiki/Patch_0.102 "Patch 0.102") • [0.103](/wiki/Patch_0.103 "Patch 0.103") • [0.104](/wiki/Patch_0.104 "Patch 0.104")  
Closed Alpha| [Early game development](/wiki/Early_game_development "Early game development") • [2018-10-11](/wiki/Patch_2018-10-11 "Patch 2018-10-11") • [2018-10-17](/wiki/Patch_2018-10-17 "Patch 2018-10-17") • [2018-10-19](/wiki/Patch_2018-10-19 "Patch 2018-10-19") • [2018-10-27](/wiki/Patch_2018-10-27 "Patch 2018-10-27") • [2](/wiki/Patch_Closed_Alpha_2 "Patch Closed Alpha 2") • [2.1](/wiki/Patch_Closed_Alpha_2.1 "Patch Closed Alpha 2.1") • [3](/wiki/Patch_Closed_Alpha_3 "Patch Closed Alpha 3") • [3.1](/wiki/Patch_Closed_Alpha_3.1 "Patch Closed Alpha 3.1") • [3.2](/wiki/Patch_Closed_Alpha_3.2 "Patch Closed Alpha 3.2") • [4](/wiki/Patch_Closed_Alpha_4 "Patch Closed Alpha 4") • [4.1](/wiki/Patch_Closed_Alpha_4.1 "Patch Closed Alpha 4.1") • [Alpha Test Weekend](/wiki/Alpha_Test_Weekend "Alpha Test Weekend") • [5](/wiki/Patch_Closed_Alpha_5 "Patch Closed Alpha 5") • [5.1](/wiki/Patch_Closed_Alpha_5.1 "Patch Closed Alpha 5.1") • [5.3](/wiki/Patch_Closed_Alpha_5.3 "Patch Closed Alpha 5.3")
  *[v]: View this template
  *[e]: Edit this template
  *[h]: History of this template
  *[his]: his trivia section
