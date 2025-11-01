# Patch 0.8.3.0

[](/wiki/File:Update8_Sign_Logo.png)  
  
Patch Notes: Early Access – **v0.8.3.0** – Build 264901. This patch was released on 14 November 2023. It is the last patch of Update 8 development, bringing its features to the stable branch. 

The original post can be viewed on Satisfactory's [official website](https://www.satisfactorygame.com/updates/update-8), as well as [Discord](https://discord.com/channels/370472939054956546/557603412565426196/1174019038976954480), [Reddit](https://www.reddit.com/r/SatisfactoryGame/comments/17v5fno), and [Steam](https://store.steampowered.com/news/app/526870/view/3809543111554233637). 

## Contents

  * 1 Intro
    * 1.1 Upgrading to Unreal Engine 5
    * 1.2 World partitioning
    * 1.3 Vehicle physics & sound overhaul
    * 1.4 Enhanced Input System
    * 1.5 Upscaling (DLSS, XeSS, FSR)
    * 1.6 Anti-aliasing (TSR & FXAA)
    * 1.7 Nanite
    * 1.8 Lumen
    * 1.9 Blueprint improvements
    * 1.10 Dismantling
    * 1.11 Building
    * 1.12 Nudging
    * 1.13 Changes to the world
    * 1.14 Visuals
    * 1.15 Gameplay
    * 1.16 Atmosphere
    * 1.17 Advanced Game Settings
    * 1.18 Priority Power Switch & Power Tower
    * 1.19 Quality of life and other improvements
    * 1.20 Destructible Gas Pillars
    * 1.21 Jetpack fuels
    * 1.22 Parachute
    * 1.23 Conveyor and Pipe building
    * 1.24 Dismantle Filter
  * 2 Patch Notes
    * 2.1 Engine
    * 2.2 Online integration / EOS
    * 2.3 Upscaling / visuals
    * 2.4 Auto detect settings
    * 2.5 Factory
    * 2.6 Advanced Game Settings
    * 2.7 Equipment
    * 2.8 Creatures
    * 2.9 Vehicles
    * 2.10 World
    * 2.11 Audio
    * 2.12 Quality of Life
    * 2.13 Modding
    * 2.14 Localisation
    * 2.15 Balancing
    * 2.16 Inventory
    * 2.17 UI
    * 2.18 Player character
    * 2.19 Systems
    * 2.20 Optimization
    * 2.21 Bug fixes
  * 3 Known issues



## Intro

Hi Pioneers! 

Today Update 8 is now available on the Early Access version of Satisfactory for everyone to try out and have fun with it! This update showcases the combined efforts of the studio over more than a year worth of work with both Unreal Engine 5 and Update 8 as a whole, so there are a LOT of changes that have happened since Update 7 released on Early Access. 

We’ve spent the last few months trying our best to stabilize as much as we can so you all can have a good experience when Update 8 releases on Early Access, with that being said, It never hurts to BACK UP YOUR SAVES 🙂 

If you are experiencing issues, want to give us some feedback, or just post any cool ideas you might have, please let us know over at our QA/Questions Site: <https://questions.satisfactorygame.com/> We always enjoy reading all your comments after a big update like this. 

Our community manager Snutt has prepared a new video for you all which goes over what’s new in Update 8 so be sure to check it out <https://youtu.be/BIZieuScBmE>

If you have been following along through Experimental, everything in this patch notes will be already known to you, as this build has little or no changes from the latest Experimental from last week, but you can still give them a look as there might be a new thing or two you didn’t know about 

However, If you haven’t been keeping up with the patch releases at all, there are a LOT of new things to go through, so grab a snack/drink and let’s get started. 

### Upgrading to Unreal Engine 5

With this come many reworks and updates of systems that should improve aspects of the game, We’ve put a lot of effort into stabilising the game and performance before the Early Access release, but there might very well be things that we’ve missed. 

So again please back up your saves and let us know about any differences that you encounter while playing Update 8. 

Jace talked about the upgrade in depth in one of our earliest Update 8 videos check it out for more info! <https://youtu.be/dY__x2dq7Sk>

### World partitioning

With world partitioning in UE5 the level streaming should be much more flexible compared to the tile-based system we used before, reducing hitches that you will have encountered where these tiles used to intersect. 

### Vehicle physics & sound overhaul

With UE5 comes an all-new physics simulation called Chaos, we’ve reworked our vehicles to use this instead of our previous implementation. The manual driving of vehicles has been redone and we made improvements in feel and usage of the different vehicles. 

With this we also reworked all vehicle sounds, eliminating many issues and overall improving quality and consistency. 

### Enhanced Input System

A new system we switched to with Unreal Engine 5 is the Enhanced Input system. With this we implemented contextual key bindings in the options, allowing for much more granularity and control over your control scheme across different contexts like the build mode, driving vehicles, using equipment, etc. 

### Upscaling (DLSS, XeSS, FSR)

Added several upscalers for any hardware that supports them. 

### Anti-aliasing (TSR & FXAA)

We added a lightweight anti-aliasing method known as FXAA (Fast approximate anti-aliasing) which allows for better performance on lower end machines or for people that don’t like the effect that the previous default anti-aliasing technique had. 

We also support TSR (Temporal Super Resolution) which is Epic’s implementation of upscaling technology combined with anti-aliasing. For user experience we added several presets: Performance, Balanced, Quality & Insanity. 

### Nanite

With Unreal Engine 5 comes Nanite, a new way of rendering complex meshes allowing for high visual quality. Due to complications we only decided to convert a part of our content to Nanite. Rocks, Cliffs and Conveyor items will be using Nanite for the time being. 

### Lumen

Lumen is a Global Illumination system that improves lighting and reflections. This new rendering feature will make the world and factory more grounded which can result in more intense & realistic scenes. 

We decided to have Lumen disabled by default even on the ultra-preset due to its high demand on the hardware. There are several scalability options to make Lumen perform well on most hardware. 

When using Lumen, we recommend running with an up-scaler enabled on the “Performance” preset and Lumen on Medium or High due to the minimum quality difference. 

### Blueprint improvements

There were a number of improvements you’ve requested and that we still wanted to make, which should significantly improve using them 

Jace talks a about the new features coming to Blueprints in this video: <https://youtu.be/ZDN_b6TX5gg>

### Dismantling

We’ve added a Blueprint dismantle mode that you can toggle with ‘R’ by default while in the regular dismantle mode. With this you can dismantle an entire Blueprint at once! 

### Building

Blueprints now have a directional indicator in their hologram making it easier to place them in the correct rotation. We also implemented Quick Switch for Blueprints, allowing you to quickly toggle through Blueprints by pressing or holding ‘E’, without leaving the build mode. 

### Nudging

We’ve also added a Nudge Mode for all buildables and Blueprints! Pressing the H key will lock the current hologram in place, so you can move around freely to check its placement from different directions. From there you are then able to nudge the hologram around to adjust the placement by using the arrow keys before building it. You can also hold CTRL when Nudging to move the building in half steps for easier fine tuning. 

### Changes to the world

We didn’t make any changes to resource nodes this time around and any terrain changes we’ve done are minor, so your factories should be safe 

To get an overview on what’s changed you can watch this video covering it in more detail: <https://youtu.be/6X4jqMUtCwI>

### Visuals

Titan Forest and Red Jungle have received the most significant overhaul for their foliage, visual and sound effects, as well as lighting. 

Many areas have received more polish, those being the Abyss Cliffs, Rocky Desert, Grass Fields, Northern Forest, Dune Desert, Eastern Dune Forest, Spire Coast, and some of the caves as well. 

We also updated and improved the vista around the world, which has a huge impact on the look and feel of the areas at the edge on the map. With this one we are not fully done yet, but it is certainly an upgrade, and are excited for you to see the direction it is taking. 

### Gameplay

We are adding two new variants to the Hogs: The Cliff Hog and Nuclear Hog! They are the most menacing members of their family, defending their territory with devastating charges, and in case of the Nuclear Hog, also radiation. 

We’ve also polished and updated placements of creatures, hazards, and collectables in many areas of the world, Such as Titan Forest, Red Jungle, Spire Coast, Grass Fields, Northern Forest, Dune Desert, Eastern Dune Forest, Crater Lakes, Western Beaches, Abyss Cliffs, Coin Tree Forest and most of their sub areas. 

### Atmosphere

In terms of lighting, we’ve done full passes over all starting areas; Grass Fields, Rocky Desert, Northern Forest and Dune Desert, the Titan Forest, Red Jungle and Spire Coast to elevate their look and feel further and fix existing issues. 

You can find all the details in the patch notes below! 

### Advanced Game Settings

We are adding a number of settings that will allow you to customise your experience quite heavily. These Advanced Game Settings can alter the experience drastically, you can either enable them when creating a new game or when loading a save from the main menu. 

There is a full list of all new settings in the detailed patch notes below, but they include things such as Flight Mode, No Build Cost, Set Starting Tier, and No Stinger Mode fully removing the spidery Stinger enemy from the game. 

Here is our video covering all of this in detail: <https://youtu.be/T2lOiHtygVM>

### Priority Power Switch & Power Tower

You can watch Jace talk about them in this video: <https://youtu.be/v4mbNy3gt7c>

The Priority Power Switch allows you to organise sections of your power grid into different priorities. So, if your power would fail the Priority Power Switches turn off in order of their set priority, shutting of the parts of your factory gated behind them until there is enough power available for the remainder of your grid to keep running. 

They can also be switched off and on remotely from any other Priority Power Switch, allowing you to remotely control which parts of your factory are running. 

The Power Tower is a large building allowing you to connect power lines over longer distances. It comes in two versions, one with a ladder and platform that make them and excellent combination with the Zipline, and one version without for a cleaner look. 

### Quality of life and other improvements

You can check out this video we made on all these other improvements coming with Update 8: <https://youtu.be/9jDBEpAlS2s>

And check out the written section for Quality of life in the patch notes further below, it contains many new improvements that came alongside Update 8 Experimental, so they are not featured in the videos above, but should be very welcome additions! 

### Destructible Gas Pillars

With Update 8 you’ll be able to blow up Gas Pillars using the Nobelisk! We’ve been wanting to add this for a while, and it is finally in the game. After unlocking Nobelisks you won’t have to worry anymore about odd Gas Pillars disrupting how you can build your factories. 

### Jetpack fuels

The Jetpack can now use a selection of fuels with different burn rates and acceleration. Thanks to this the Jetpack can be used before automating fuel with Solid Biofuel, and in the late game you can even use Turbofuel which has unparalleled acceleration. 

### Parachute

This feature has received some changes to make it a viable tool in the early to mid-game. For one, the Parachute no longer gets consumed when used, so you can now make one and use it for as long as you want. 

It now has a standard and sprint speed which match the Bladerunner speeds. Of course, it also retains its signature function of preventing fall damage in any dicey situations you might find yourself in. 

### Conveyor and Pipe building

You now have an automatic starting pole if you don’t start building from an existing connection such as a pole or input/output. This means that when selecting to build a Conveyor or Pipe you can put down a pole with your first click and drag the Conveyor/Pipe out from there as usual! 

Before it was sometimes impossible to build a pole because its initial starting position was invalid, even if you would be able to make it a valid placement after adjusting the height of the pole. We have now moved this validity check to the final placement of the pole to fix this. 

### Dismantle Filter

We’ve added a filter to the Dismantle Mode where you can hover over a specific type of building and select it to your dismantle filter. While remaining in Dismantle Mode you will only highlight the selected type of building for dismantling, making it much easier to dismantle specific parts of your factory while avoiding removing the other parts you want to keep by accident. 

You can switch the filter freely while dismantling, and it works with both the new Blueprint Dismantle Mode and Mass Dismantle! 

## Patch Notes

### [Engine](/wiki/Unreal_Engine "Unreal Engine")

  * Unreal Engine Upgraded to 5.2.1



### Online integration / EOS

  * Online Integration has been reworked, some parts of it will still change (WIP)



### [Upscaling / visuals](/wiki/Unreal_Engine#Nvidia_DLSS,_Intel_ExSS,_AMD_FSR "Unreal Engine")

  * Added Nvidia DLSS as a selectable Upscaling method
  * Added Intel XeSS 1.2 as a selectable Upscaling method
  * Added FSR 2
  * Added Upscaling method [settings](/wiki/Settings#Video "Settings")
    * You can select between TSR, DLSS or XeSS under this drop down when your hardware supports it



### [Auto detect settings](/wiki/Settings#Video "Settings")

  * Auto Detect Settings (Experimental) 
    * When starting the game, your video settings should now be automatically detected and set up to recommended Video settings for your system
    * If you’ve never changed a setting before, a new default might be applied to it
    * If you manually change an option, it will not be overwritten automatically on startup, but you can still manually force ALL settings be autodetected by clicking on the “Auto Detect Settings” button in the options menu in the Video section



### Factory

  * Added the [Power Tower](/wiki/Power_Tower "Power Tower") and Power Tower Platform 
    * Unlocked in Tier 4: Expanded Power Infrastructure
    * Has gradual 45 degree rotation on foundations
  * Added the [Priority Power Switch](/wiki/Priority_Power_Switch "Priority Power Switch")
    * Unlocked in MAM: Caterium
    * Has gradual 45 degree rotation on foundations
    * Power Switches can be upgraded to Priority Power Switches and vice versa
    * There are buttons for turning entire priority groups on and off in the Priority Power Switch



### [Advanced Game Settings](/wiki/Advanced_Game_Settings "Advanced Game Settings")

  * Added several Advanced Game Settings that can be enabled when starting a new game or loading a save from the main menu: 
    * Flight mode: Player can fly
    * God mode: Player takes no damage (will still die from leaving the map)
    * Give items: Player can add items to their inventory
    * No build cost: Buildables cost nothing to build
    * No unlock cost: Unlocks cost nothing to unlock
    * Unlock alternative recipes instantly: Alternate recipes unlock as soon as all requirements are met (removes need for Hard Drives)
    * No power: Buildings don’t consume power
    * Set starting tier: The session will start at the selected Tier and players will receive a starting set of items
    * Set game phase: Unlocks all phases before
    * Unlock all Tiers/MAM/Shop/Phases: Unlocks everything in the selected progression branch
    * Respawn settings: Player can set what they keep on them when respawning (everything, only equipped items, nothing)
    * Disable arachnid creatures: Disables the spawning of Stingers in the session



### Equipment

  * [Jetpack](/wiki/Jetpack#Fuel "Jetpack")
    * Added support for using different fuel types in the Jetpack 
      * Solid Biofuel
      * Liquid Biofuel
      * Fuel
      * Turbo Fuel
    * Jetpack can now refuel while the player is on a Zipline
  * [Parachute](/wiki/Parachute "Parachute")
    * The Parachute is no longer consumed after usage and the stack size is now 1, making it function the same as other back slot equipment, such as the Jetpack
    * Added a Sprint Mode to the Parachute, allowing for slow and fast movement
    * Increased the maximum speed and descending speed, allowing for improved gliding
  * [Zipline](/wiki/Zipline "Zipline")
    * The Zipline now automatically connects to the next Power Line while ziplining on Power Towers and ceiling connections 
      * This will not work if the angle between the Power Lines exceeds 60 degrees
      * If the Zipline can move along more than one Power Line the direction can be controlled by looking at the desired direction or by holding the directional movement input
    * Reduced maximum Zipline Sprint Speed to 100 km/h (due to the previous maximum speed being too high for the world loading)
    * Increased the Zipline Sprint acceleration to be nearly instant
    * The Zipline can now be toggled on/off by pressing the secondary equipment input (RMB by default), which allows ziplining without needing to hold down the primary equipment input (LMB by default)
  * Weapons 
    * Fire rate and damage balancing done to the [Homing Rifle ammo](/wiki/Rifle#Homing_Ammo-0 "Rifle")
    * Weapon spread and damage balancing done to the [Turbo Rifle ammo](/wiki/Rifle#Turbo_Ammo-0 "Rifle")
    * Minor damage reductions on the [Rebar Gun](/wiki/Rebar_Gun "Rebar Gun") Iron, Stun, and Explosive Rebar ammo



### Creatures

  * [Cliff Hog](/wiki/Cliff_Hog "Cliff Hog")
    * Higher health, damage, size, and speed relative to the Alpha Hog
    * Basic Hog Charge attack, with increased speed and damage
    * New Rock Throw attack, which launches a rock at a distant or unreachable target
    * New Plow Charge attack, which continually pushes and deals damage to the target
  * [Nuclear Hog](/wiki/Cliff_Hog#Nuclear_Hog-0 "Cliff Hog")
    * Higher health, damage, size, and speed relative to the Cliff Hog
    * Basic Hog Charge attack, with increased speed and damage
    * New Rock Throw attack, which launches a rock at a distant or unreachable target
    * New Plow Charge attack, which continually pushes and deals damage to the target
    * Passive Radiation Damage area of effect
  * Creature health and damage balancing 
    * Reduced the health of Small Desert and Aquatic [Spitters](/wiki/Spitter#Variants "Spitter") from 30 to 20
    * Increased health of [Alpha Forest Spitter](/wiki/Alpha_Spitter#Variants "Alpha Spitter") from 60 to 80



### [Vehicles](/wiki/Vehicles "Vehicles")

  * Moved vehicle physics to using [Chaos](/wiki/Unreal_Engine#Chaos_Physics_System "Unreal Engine")
  * Overhauled all vehicle sounds
  * Improved the manual driving of all vehicles
  * Reworked all vehicle trunks visually simplifying the animation and adding a new sound
  * Added functionality for vehicles to deal damage to creatures by hitting them 
    * Damage dealt is relative to vehicle speed and size



### [World](/wiki/World "World")

  * Gas Pillars can now be destroyed by explosives such as the Nobelisk
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
  * Fixed collision being missing in some Coral



### [Audio](/wiki/Unreal_Engine#Game_audio "Unreal Engine")

  * Some ambience tweaks to Red Jungle sound effects
  * Some ambience tweaks to Spire Coast sound effects
  * Changed the audio for the waterfalls in Dune Desert Canyon
  * General tweaks to waterfall sound effects



### Quality of Life

  * [Nudging](/wiki/Controls#Default_keybindings "Controls")
    * Added the ability to lock a hologram in place with ‘H’ by default while in Build Mode, allowing players to inspect the placement before building
    * Added the ability to nudge a locked hologram with the arrow keys by default, allowing players to adjust the placement before building
    * Holding CTRL when Nudging will now nudge in half steps


  * [Blueprints](/wiki/Blueprint_Designer "Blueprint Designer")
    * Added a directional indicator to the Blueprint hologram
    * Added a Blueprints Dismantle Mode that can be switched on in the regular Dismantle Mode, allowing an entire Blueprint to be dismantled at once
    * Added Quick Switch functionality to Blueprints, allowing the player to quickly switch between Blueprints in the same sub-category
    * Added Sample functionality to Blueprints (can only be sampled when in Blueprint Dismantle Mode)
    * Added a Dismantle Filter to the Dismantle Mode, allowing the player to select a specific buildable to dismantle and ignore all other buildables
    * Pillars can partially intersect the edges of the blueprint designer again


  * [Hotbar](/wiki/HUD#Hotbar "HUD")
    * Hotbar system has been reworked
    * Added a way to save the current hologram into the hotbar by pressing ALT+Shortcut key combination
    * You can now swap the Hotbar scroll direction in the “Controls” menu in the Options menu (Clockwise and Counterclockwise)


  * [Conveyor Lifts](/wiki/Conveyor_Lifts "Conveyor Lifts")
    * Quick Switch is now supported when building them
    * Added automatic placement of a Conveyor or Pipe pole when not building a Belt or Pipe from an existing connection point
    * Changed the Quick Switching of Conveyor Belt, Lift, and Pipe Mk.’s to no longer revert back to the first placement step
    * Moved validation check for building Conveyors and Pipes to final placement step


  * [Zipline](/wiki/Zipline "Zipline")
    * Increased Zipline sprint acceleration. It should be easier to tell that sprint mode is turned on now due to the more direct change in speed
    * Zipline path selection now works vertically too
    * Additional improvements to try and mitigate cases where you get disconnected from ziplining when ziplining on an incline


  * [Power Lines](/wiki/Power_Line "Power Line")
    * Made the automatic power connections when building Power Lines context sensitive, copying the same type of pole the Power Line was initially connected to
    * Holding CTRL when building a wire off another wire now aligns the new Pole to the original one


  * [Splitters](/wiki/Conveyor_Splitter "Conveyor Splitter")/[Mergers](/wiki/Conveyor_Merger "Conveyor Merger")
    * Added the option to upgrade Splitters (regular, Smart, Programmable) by holding CTRL (default input) while aiming any Splitter variant hologram at any other already build Splitter variant
    * Can also be upgraded to each other (Splitter to Merger and viceversa) as long as only the main input and output is connected


  * [Hypertubes](/wiki/Hypertube "Hypertube")
    * Implemented network correction and smoothing for remote players moving in Hypertubes, This should make the movement inside hypertubes much smoother and prevent any kind of desync, this is also enabled for Clients
    * Fixed character getting too much acceleration when braking while going downhill
    * Fixed hypertube attachments incorrectly building when attaching them in a section of a hypertube
    * Hypertube Entrances can now be nudged
    * Hypertube entrances now work correctly when they are built directly on top of a floor hole


  * Input System 
    * Added an “Auto release sprint” [option](/wiki/Settings#Controls "Settings") when Hold to sprint is off, this option is off by default. This makes it so whenever your movement stops, the sprint key is automatically released so you have to press it again to start sprinting


  * [Hand Miner](/wiki/Controls#Default_keybindings "Controls")
    * Can now be Tap E to Mine (Toggle) or Hold E to Mine, depending on how long the button is held
    * Fixed a couple of issues with mining lingering around when walking away from the node


  * [Signs](/wiki/Signs "Signs")
    * Improved snapping for signs, they can now snap to foundation sides and ceilings and can be rotated more freely.
    * Changed signs to use the same snapping logic for walls and foundations
    * Removed restrictions for snapping signs to pillars, they can now snap to any side at any time
    * When snapping a sign to a foundation, ceiling or floor, you can now hold CTRL to lay the sign down flat, otherwise it will use the pole support


  * [Build Gun / Dismantle Gun](/wiki/Build_Gun "Build Gun")
    * When trying to dismantle invalid buildables they will now redirect to the valid dismantlable (I.E. Like the Integrated train tracks or the Sub Buildings of the Hub, they will now dismantle the Train Station and the entire Hub respectively)
    * The Build Gun now remembers its last used dismantle mode, such as blueprint dismantle, so you no longer need to switch to it every time the Build Gun is brought up



### Modding

  * Included .usmap file into the Community Resources



### Localisation

  * Updated all languages with the latest translations
  * Updated language completion rates
  * Updated community translators in the credits



### Balancing

  * Changed the Parachute recipe to only produce 1 at a time and increased the cost of a single Parachute
  * Removed the option to purchase Parachutes from the AWESOME Shop now that it is no longer a consumable item
  * Added a new [milestone](/wiki/Milestones#Tier_4 "Milestones") to Tier 4: ‘Expanded Power Infrastructure’ 
    * Moved the Power Storage unlock to Tier 4: Expanded Power Infrastructure
    * Added the Power Tower and Power Tower Platform to Tier 4: Expanded Power Infrastructure
  * Renamed the Tier 6 milestone ‘Expanded Power Infrastructure’ to ‘Logistics Mk.4’
  * Moved the location of the [Power Poles](/wiki/Power_Poles "Power Poles") Mk.3 unlock in the [MAM: Caterium](/wiki/MAM#Caterium "MAM") research tree 
    * Reduced the High-Speed Connector cost of the Power Poles Mk.3 research from 100 to 50
  * Added the Priority Power Switch unlock to the MAM: Caterium research tree



### [Inventory](/wiki/Inventory "Inventory")

  * Somersloops and Mercer Spheres can no longer be deleted from the inventory



### UI

  * Updated UI to work with the new UE5 Input System
  * Re-worked the [options menus](/wiki/Settings "Settings") and [key binding menu](/wiki/Settings#Keybindings "Settings")
  * Added a search bar in the options and key binding menu
  * Re-worked the [main menu](/wiki/Game_menus#Main_menu "Game menus") and new game menu
  * Reworked the [multiplayer](/wiki/Multiplayer "Multiplayer") menus (WIP)
  * Added functionality to change the preferred fuel of equipped Jetpack in inventory window
  * Improved UI memory usage
  * Added Dark Mode for the [A.W.E.S.O.M.E. Shop](/wiki/AWESOME_Shop "AWESOME Shop")
  * Rewrote descriptions for video and graphical settings to be clearer to understand
  * Added a button to the new Wiki to the Social Media buttons in the main menu and rearranged the buttons
  * Made the [Experimental Label](/wiki/HUD#Game_version "HUD") bit more transparent and less bright red to help prevent OLED Burn-in



### [Player character](/wiki/Pioneer "Pioneer")

  * The player character now respawns with the equipment that was equipped on death still equipped
  * Reworked and improved the player character footstep sounds



### Systems

  * Overhauled the foliage system to be compatible with Unreal Engine 5
  * Some adjustments in the power system, no changes should be noticeable during play
  * Migrated all inputs to the new Enhanced Input System



### Optimization

  * Optimized the [save system](/wiki/Save_files "Save files") to decrease saving time on larger saves by roughly 80-90%
  * Optimized significance manager
  * Converted to World Partitioning
  * Added streaming scalability for foliage streaming cells 
    * Foliage cells can now be loaded from different ranges 
      * Near, Default, Far, Cinematic
  * Optimized Signs 
    * Signs will now share when same configuration is found
    * Emissive only signs are handled in a more performant way
  * Improved conveyor rendering system to make use of Nanite
  * Added TSR 
    * Added TSR Presets: 
      * Performance (60% Screen percentage)
      * Balanced (75% Screen percentage)
      * Quality (90% Screen percentage)
      * Insanity (100% Screen percentage)
  * Added Lumen 
    * Added Lumen Scalability
  * Deprecated/Soft Removed DirectX 11 
    * Note you can still run on DirectX 11 but without Nanite or Lumen.  
We cannot promise the same quality as on DirectX 12 or Vulkan.
  * Minor optimizations for the Conveyor system
  * Resolved issues where signs ticked when not needed, This should improve GPU bandwidth and improve CPU performance in saves with a big quantity of Signs built
  * Enabled Skip draw when shader isn't done compiling, this should help reduce rendering hitches
  * Disabled overlap caching to reduce consistent chaos performance loss.
  * General Chaos memory optimizations
  * Optimized physic scene handling for foliage, reduces hitches when level streaming.
  * Optimized logic to determine if an entity is near a factory.
  * Refactored sign system for optimal performance. 
    * Improved consistency with backgrounds between signs sizes.
  * Parallelized post processing blending.
  * Chaos memory optimizations
  * Texture memory optimizations
  * Mesh memory optimizations
  * Enabled virtual textures for HLODs
  * Updated HLODs to use virtual textures.
  * Enabled PSO caching
  * Removed legacy assets



### Bug fixes

  * Fixed a potential bug with [drone](/wiki/Drone "Drone") queue processing
  * Fixed shadow flickering
  * Fixed so trains do not have to wait 2 seconds for pathfinding (a cooldown) when loading a save. This fixed a case where a train could take a wrong turn on load if it was close enough to a switch.
  * Fixed FOV scaling issues for equipment, now it should properly update without having to unequip and re-equip the equipment
  * Fixed the parachute visuals on conveyor belts or when dropped
  * Fixed a bug where drones would sometimes consume batteries multiple times when starting a new trip, especially when the player is far away
  * Fixed Jetpack (Spacebar) Getting stuck
  * You can now more easily pick up items dropped in [resource nodes](/wiki/Resource_Node "Resource Node")
  * Potential fix for foliage not being removed when playing as Client in both regular [Multiplayer](/wiki/Multiplayer "Multiplayer") and [Dedicated Server](/wiki/Dedicated_servers "Dedicated servers")
  * You can now more easily interact with Electric Locomotives and Freight Carts when they are docked on a [Train Station](/wiki/Train_Station "Train Station")
  * Some improvements to Pipe SFX causing hitches/stuttering in factories with a lot of Refineries/Blenders built



## Known issues

  * A reminder for people who have been having issues with unexpected crashes on startup or weird behaviour with the game, in that case please try to verify your game files.   
You can do this on Steam by Right Clicking the game in your Library > Properties > Local Files > Verify integrity of game files...   
And on Epic by clicking on the three dots (“...”) next to the title or at the right side, depending on your selected library view > Manage > Verify Files > Verify   
This may or may not redownload a large amount of files which might take a while depending on your internet connection or hard drive speeds so be wary of that.
  * If you are using mods, they might need to be updated or uninstalled after updating so please keep this in mind too.
  * The first time booting the game will be very slow, but that should not continue to happen after the first boot
  * Factory Animation tick reductions can be slightly too aggressive
  * Some players with extremely big factories might experience hitches/stuttering related to Pipes, a workaround if you're experiencing this is to build longer continuous pipes instead of multiple segments as building more segments increases the likelihood for this to happen. 
    * Another potential workaround for the more extreme cases of this is to launch the game with the -NoAudio/-NoSound command or have factory Audio set to zero in the options menu
  * TSR can cause visual issues with conveyor belts, you can try using the following console command to alleviate the issues, but this will reduce AntiAliasing quality 
    * `r.TSR.ShadingRejection.Flickering 0`
  * **ADDED:** Game can hang on quit
  * **ADDED:** There is major performance loss when running out of VRAM



  * [v](/wiki/Template:PatchesNav "Template:PatchesNav")
  * [e](https://satisfactory.wiki.gg/wiki/Template:PatchesNav?action=edit)
  * [h](https://satisfactory.wiki.gg/wiki/Template:PatchesNav?action=history)

[Patches](/wiki/Category:Patch_notes "Category:Patch notes")  
---  
1.1| [1.1.1.0](/wiki/Patch_1.1.1.0 "Patch 1.1.1.0") • [1.1.1.1](/wiki/Patch_1.1.1.1 "Patch 1.1.1.1") • [1.1.1.2](/wiki/Patch_1.1.1.2 "Patch 1.1.1.2") • [1.1.1.3](/wiki/Patch_1.1.1.3 "Patch 1.1.1.3") • [1.1.1.4](/wiki/Patch_1.1.1.4 "Patch 1.1.1.4")  
Experimental 1.1| [1.1.0.0](/wiki/Patch_1.1.0.0 "Patch 1.1.0.0") • [1.1.0.1](/wiki/Patch_1.1.0.1 "Patch 1.1.0.1") • [1.1.0.2](/wiki/Patch_1.1.0.2 "Patch 1.1.0.2") • [1.1.0.3](/wiki/Patch_1.1.0.3 "Patch 1.1.0.3") • [1.1.0.4](/wiki/Patch_1.1.0.4 "Patch 1.1.0.4") • [1.1.0.5](/wiki/Patch_1.1.0.5 "Patch 1.1.0.5") • [1.1.0.6](/wiki/Patch_1.1.0.6 "Patch 1.1.0.6") • [1.1.1.5](/wiki/Patch_1.1.1.5 "Patch 1.1.1.5") • [1.1.1.6](/wiki/Patch_1.1.1.6 "Patch 1.1.1.6")  
1.0| [1.0](/wiki/Patch_1.0 "Patch 1.0") • [1.0.0.1](/wiki/Patch_1.0.0.1 "Patch 1.0.0.1") • [1.0.0.2](/wiki/Patch_1.0.0.2 "Patch 1.0.0.2") • [1.0.0.3](/wiki/Patch_1.0.0.3 "Patch 1.0.0.3") • [1.0.0.4](/wiki/Patch_1.0.0.4 "Patch 1.0.0.4") • [1.0.0.5](/wiki/Patch_1.0.0.5 "Patch 1.0.0.5") • [1.0.0.6](/wiki/Patch_1.0.0.6 "Patch 1.0.0.6") • [1.0.0.7](/wiki/Patch_1.0.0.7 "Patch 1.0.0.7") • [1.0.1.0](/wiki/Patch_1.0.1.0 "Patch 1.0.1.0") • [1.0.1.1](/wiki/Patch_1.0.1.1 "Patch 1.0.1.1") • [1.0.1.2](/wiki/Patch_1.0.1.2 "Patch 1.0.1.2") • [1.0.1.3](/wiki/Patch_1.0.1.3 "Patch 1.0.1.3") • [1.0.1.4](/wiki/Patch_1.0.1.4 "Patch 1.0.1.4")  
Experimental 1.0| [1.0.1.5](/wiki/Patch_1.0.1.5 "Patch 1.0.1.5") • [1.0.1.6](/wiki/Patch_1.0.1.6 "Patch 1.0.1.6")  
Update 8| 0.8.3.0 • [0.8.3.2](/wiki/Patch_0.8.3.2 "Patch 0.8.3.2") • [0.8.3.3](/wiki/Patch_0.8.3.3 "Patch 0.8.3.3")  
Experimental Update 8| [0.8.0.0](/wiki/Patch_0.8.0.0 "Patch 0.8.0.0") • [0.8.0.1](/wiki/Patch_0.8.0.1 "Patch 0.8.0.1") • [0.8.0.2](/wiki/Patch_0.8.0.2 "Patch 0.8.0.2") • [0.8.0.3](/wiki/Patch_0.8.0.3 "Patch 0.8.0.3") • [0.8.0.4](/wiki/Patch_0.8.0.4 "Patch 0.8.0.4") • [0.8.0.5](/wiki/Patch_0.8.0.5 "Patch 0.8.0.5") • [0.8.1.0](/wiki/Patch_0.8.1.0 "Patch 0.8.1.0") • [0.8.1.1](/wiki/Patch_0.8.1.1 "Patch 0.8.1.1") • [0.8.1.2](/wiki/Patch_0.8.1.2 "Patch 0.8.1.2") • [0.8.1.3](/wiki/Patch_0.8.1.3 "Patch 0.8.1.3") • [0.8.2.0](/wiki/Patch_0.8.2.0 "Patch 0.8.2.0") • [0.8.2.1](/wiki/Patch_0.8.2.1 "Patch 0.8.2.1") • [0.8.2.2](/wiki/Patch_0.8.2.2 "Patch 0.8.2.2") • [0.8.2.3](/wiki/Patch_0.8.2.3 "Patch 0.8.2.3") • [0.8.2.4](/wiki/Patch_0.8.2.4 "Patch 0.8.2.4") • [0.8.2.5](/wiki/Patch_0.8.2.5 "Patch 0.8.2.5") • [0.8.2.6](/wiki/Patch_0.8.2.6 "Patch 0.8.2.6") • [0.8.2.7](/wiki/Patch_0.8.2.7 "Patch 0.8.2.7") • [0.8.2.8](/wiki/Patch_0.8.2.8 "Patch 0.8.2.8") • [0.8.2.9](/wiki/Patch_0.8.2.9 "Patch 0.8.2.9") • [0.8.3.1](/wiki/Patch_0.8.3.1 "Patch 0.8.3.1")  
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
