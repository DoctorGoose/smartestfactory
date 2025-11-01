# Patch Closed Alpha 4

Patch notes: **Closed Alpha 4** – Build 94038 – _Bug fixes & game improvements_. This version was released on February 28, 2019. The original post came from the Closed Alpha Discord.[1]  
  
## Contents

  * 1 Intro
  * 2 Features
  * 3 Progression and balancing
  * 4 Bug fixes
  * 5 UI
  * 6 World
  * 7 Optimisation
  * 8 Wildlife
  * 9 Buildings
  * 10 Vehicles
  * 11 Sound
  * 12 Quality of Life
  * 13 Resources
  * 14 Tutorial
  * 15 References



## Intro

Hello there, FICSIT Pioneers! 

We are currently in full bug fixing and game improvement mode, so this patch will get loads of smaller and bigger updates of the current content to you! Also, we are unlocking the last starting area: Northern Forest. 

Something big is coming up next week (and we are VERY excited about it), so we are relying on your feedback more than ever to iron out all the kinks in the game. The more you can play and report to us this weekend, the better it will turn out. 

The patch notes below are a little less detailed than usual due to the amount of smaller updates coming in. Generally, you will see lots of QoL and UI updates, we’ve cracked down on optimising the game more, iterated on the world and did many smaller tweaks to assets and mechanics. 

We'll likely push another update tomorrow and more next week in response to the weekend. 

Hope you enjoy the update and give us all the feedback and bug reports! 

## Features

  * Added [Photo Mode](/wiki/Photo_Mode "Photo Mode") (P-key while playing)
  * [Hard Drives](/wiki/Hard_Drive "Hard Drive") are now researchable and give alternate recipes
  * [Northern Forest](/wiki/World#Starting_areas "World") starting area is now unlocked



## Progression and balancing

  * Removed click to craft and made hold to craft significantly faster
  * Adjusted [belt](/wiki/Conveyor_Belt "Conveyor Belt") speeds after Conveyor Belt Mk.1 and adjusted recipe balancing accordingly
  * Increased most [research](/wiki/Research "Research") times
  * [The Hub](/wiki/The_Hub "The Hub") now costs and yields a single item “[Hub Parts](/wiki/HUB_Parts "HUB Parts")”
  * Adjusted [tutorial](/wiki/Tutorial "Tutorial") texts
  * Reduced some cooldowns after exploration based [milestones](/wiki/Milestone "Milestone")
  * Renamed Stone to [Limestone](/wiki/Limestone "Limestone")
  * Renamed Workshop to [Equipment Workshop](/wiki/Equipment_Workshop "Equipment Workshop")
  * Removed [vines](/wiki/Vines "Vines") from the game
  * Removed ability to skip tutorial steps
  * Disabled some interactions until specific tutorial steps are completed



## Bug fixes

  * Variety of crash fixes
  * Fixed that old saves don't get milestones that were added later in development
  * Improved client position desyncing while driving vehicles (but you might still experience lag)
  * Fixed [Small Spitter](/wiki/Spitter "Spitter") line of sight issue
  * Fixed issue with [Truck Station](/wiki/Truck_Station "Truck Station") collision
  * Fixed [Coal Generator](/wiki/Coal_Generator "Coal Generator") grid alignment issues
  * Fixed broken [caves](/wiki/Cave "Cave")
  * Spitter projectiles on client are now rotated correctly and travel smoother
  * Fixed a variety of spelling issues
  * Fixed most UI focus issues resulting in inconsistent closing behaviour (Esc not working, for example)
  * [Manual craft](/wiki/Craft_Bench "Craft Bench") button now disables when the player is unable to craft the selected item
  * Made it easier to spot and pick up the [Xeno-Zapper](/wiki/Xeno-Zapper "Xeno-Zapper") after dropping it to the ground
  * Fixed some issues with the [Space Whale/Tick/Giraffe](/wiki/Space_Giraffe-Tick-Penguin-Whale_Thing "Space Giraffe-Tick-Penguin-Whale Thing") where it tried to take paths it cannot actually reach
  * Added meshes for dropped version of [Portable Miner](/wiki/Portable_Miner "Portable Miner") and [Beacon](/wiki/Beacon "Beacon")
  * Fixed that after death the player icon (not death marker) appears on the [compass](/wiki/Compass "Compass")
  * Fixed that players could select multiple items in the Craft Bench
  * Snapping [Walls](/wiki/Walls "Walls") to each other and to [Foundation](/wiki/Foundation "Foundation") works as intended again
  * AND MANY MORE!



## UI

  * Big icon improvement update
  * New Main Menu and Escape Menu style
  * Added tooltips for [Build Mode](/wiki/Construction_Tool "Construction Tool"), Dismantle Mode, Build Menu, [Inventory](/wiki/Inventory "Inventory"), Craft Bench
  * Adjusted narrative messages to dark UI
  * Added the [Drop Pod](/wiki/Drop-pod "Drop-pod") that the players start the game in to the compass
  * Improved send/receive UI in the Truck Station
  * Added load/unload information on the [Vehicle](/wiki/Vehicle "Vehicle") HUD
  * Implemented a new respawn and loading screen
  * Moved the tutorial tips to centre left on the HUD
  * Ingame “Give Feedback” is now only for Level Feedback
  * Standardised the interact prompt for machines, pick-ups, etc.
  * All look-at-descriptions have unified texts now
  * Newly unlocked building are now highlighted in the Build Menu
  * Increased drop areas for items in inventory, manufacturing menus, fuel slots, overclocking, etc.
  * Clarification pass on Hub Milestone Menu elements
  * Changed Hub Upgrade icon in the Hub Menu
  * Improved feedback for hold-to-craft in the Craft Bench Menu
  * Updated Current Milestone on HUD to be in line with style changes
  * Added invite notification in Main Menu
  * New colours for player [pings](/wiki/Ping "Ping")/chat/compass icons
  * Made [MAM](/wiki/MAM "MAM") input slot more obvious
  * Added icons for [Enemies](/wiki/Combat "Combat") & [Crash Sites](/wiki/Wreckage "Wreckage") on the Object Scanner
  * NAT-type is now displayed in the Main and Escape Menu



## World

  * Implemented gameplay improvements across most areas
  * Added [Vine ladders](/wiki/Vine_ladder "Vine ladder") in the world
  * Red Bamboo Fields area visual first pass (plateau north of Grass Fields)
  * Red Jungle area visual first pass (plateau north of Grass Fields)
  * Crater area level design implementation (oil area east of Grass Fields)
  * Spire Coast area level design implementation (north of Northern Forest)
  * Added and tweaked ambient sounds all over the world
  * Improved and added billboards and LODs on trees and foliage
  * Improved fog across the world
  * Improved the world vista visuals
  * Improved the world perimeter visuals
  * Implemented world tile LODs
  * Improved cave visuals
  * Implemented better long distance grass
  * Improved moon intensity
  * Tweaked night time to be darker and generally look better
  * Added kill volumes for leaving the playable area
  * Added more colour variation on foliage in Grass Fields



## Optimisation

  * Significance Manager improvements
  * More and better factory instancing



## Wildlife

  * Improved [Hog](/wiki/Hog "Hog") aggro and panic behaviour
  * Added a Hog group behaviour
  * Adjusted colours of the Spitter variations
  * Tweaks to Spitter behaviours
  * Increased freedom of movement for all [Stingers](/wiki/Stinger "Stinger") (spider-like creatures)
  * Tweaked Space Giraffe/Tick/Whale movement and health
  * Reworked [Alpha Hog](/wiki/Alpha_Hog "Alpha Hog") behaviour
  * Adjusted colours of the Alpha hog



## Buildings

  * Improved the [Oil Pump](/wiki/Oil_Pump "Oil Pump")
  * Added sounds for the [Assembler](/wiki/Assembler "Assembler")
  * Updated Hub interior materials
  * Moved the power connections of the [Hub Biomass Burners](/wiki/The_HUB#Attached_Biomass_Burners "The HUB")



## Vehicles

  * Reworked drifting functionality (now functions correctly down to 20fps)
  * Vehicles can now destroy foliage they drive over
  * Improved [self-driving vehicles](/wiki/Vehicles#Automation "Vehicles")



## Sound

  * Updated music files and added new intermission tracks
  * Added sound for crash site UI
  * Added sound to the [Space Elevator](/wiki/Space_Elevator "Space Elevator") UI



## Quality of Life

  * Increased the collision of [Power Lines](/wiki/Power_Line "Power Line") to make it easier to dismantle them
  * Made closing menus more consistent. Now they should close with the button used to open it, Escape or by clicking the close button on the window.
  * Using the snapping while building now snaps to the nearest guideline point rather than to the nearest building
  * Pressing RMB in dismantle mode now exits dismantle mode and doesn't lead to the build menu
  * Build Mode now shows info on what specific ingredients the player is missing
  * Added ability to rotate [Storages](/wiki/Storage_Container "Storage Container") when stacking (but we might have broken rotating storages when not stacked? Whoopsie!)



## Resources

  * Mesh updates: [Circuit Board](/wiki/Circuit_Board "Circuit Board"), [Computer](/wiki/Computer "Computer"), [Oil](/wiki/Crude_Oil "Crude Oil"), [Plastic](/wiki/Plastic "Plastic"), [Crude Oil](/wiki/Crude_Oil "Crude Oil")



## Tutorial

  * Spaced out the unlock and progression message flow and effects to be less overwhelming



## References

  1. ↑ [Closed Alpha Discord patch notes dump](https://cdn.discordapp.com/attachments/464495516433121281/808312817274978304/Satisfactory_closed_alpha_patch_notes.txt)



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
Closed Alpha| [Early game development](/wiki/Early_game_development "Early game development") • [2018-10-11](/wiki/Patch_2018-10-11 "Patch 2018-10-11") • [2018-10-17](/wiki/Patch_2018-10-17 "Patch 2018-10-17") • [2018-10-19](/wiki/Patch_2018-10-19 "Patch 2018-10-19") • [2018-10-27](/wiki/Patch_2018-10-27 "Patch 2018-10-27") • [2](/wiki/Patch_Closed_Alpha_2 "Patch Closed Alpha 2") • [2.1](/wiki/Patch_Closed_Alpha_2.1 "Patch Closed Alpha 2.1") • [3](/wiki/Patch_Closed_Alpha_3 "Patch Closed Alpha 3") • [3.1](/wiki/Patch_Closed_Alpha_3.1 "Patch Closed Alpha 3.1") • [3.2](/wiki/Patch_Closed_Alpha_3.2 "Patch Closed Alpha 3.2") • 4 • [4.1](/wiki/Patch_Closed_Alpha_4.1 "Patch Closed Alpha 4.1") • [Alpha Test Weekend](/wiki/Alpha_Test_Weekend "Alpha Test Weekend") • [5](/wiki/Patch_Closed_Alpha_5 "Patch Closed Alpha 5") • [5.1](/wiki/Patch_Closed_Alpha_5.1 "Patch Closed Alpha 5.1") • [5.3](/wiki/Patch_Closed_Alpha_5.3 "Patch Closed Alpha 5.3")
  *[v]: View this template
  *[e]: Edit this template
  *[h]: History of this template
  *[his]: his trivia section
