# Patch 0.8.2.0

Patch Notes: Early Access (EXPERIMENTAL) – **v0.8.2.0** – Build 259435. This patch was released on 16 October 2023.   
  
The original post can be viewed on Satisfactory's [Discord](https://discord.com/channels/370472939054956546/557603412565426196/1163472883578843257), [Reddit](https://www.reddit.com/r/SatisfactoryGame/comments/179699f), and [Steam](https://store.steampowered.com/news/app/526870/view/6506070938937664096). 

## Contents

  * 1 Intro
  * 2 New
  * 3 QoL
  * 4 Optimisation
  * 5 Bug fixes
  * 6 UI
  * 7 Audio
  * 8 Localisation
  * 9 Known issues



## Intro

Hi Pioneers! 

Here’s a pretty big patch with a lot of QOL, optimizations across the board, bug fixes, reworks of many features both big and small, Including an entire rework of our Online Integration, Epic Online Services (EOS) update for crossplay and even another Engine Upgrade to 5.2.1 

Big disclaimer, from a technical standpoint this is a BIG Update, so please BACK UP YOUR SAVES before trying it, we don’t want to see anyone lose their saves due to unexpected behavior, so please back them all up 

With big updates like this, there might be a lot of unexpected issues showing up so if you’re experiencing any please let us know over at our QA Site: <https://questions.satisfactorygame.com/> We will look into them ASAP! 

Thank you for enjoying our game as always, See you again soon <3 

## New

  * [Unreal Engine](/wiki/Unreal_Engine "Unreal Engine") Upgraded to 5.2.1
  * Online Integration has been reworked (Work In Progress) 
    * This is still WIP and we will be patching it up through the next few weeks
    * Most of the UI for [Multiplayer](/wiki/Multiplayer "Multiplayer") related menus has been redone (Some of it is still WIP and will be updated in the future)
    * Epic Online Services have also been updated (Enables cross-play between Steam and Epic and friend list visibility)
    * [Account unlinking](/wiki/Settings#Online_\(main_menu_only\) "Settings") is WIP, so if you need to unlink your accounts and are running into issues doing so this can be done on the “Default” Early Access Branch (Not on Experimental)


  * [Auto Detect Settings](/wiki/Settings#General_2 "Settings") (Experimental) 
    * When starting the game, your video settings should now be automatically detected and set up to recommended Video settings for your system
    * If you’ve never changed a setting before, a new default will be applied to it
    * If you manually change an option, it will not be overwritten automatically on startup, but you can still manually force ALL settings be autodetected by clicking on the “Auto Detect Settings” button in the options menu in the Video section



## QoL

  * [Blueprints](/wiki/Blueprint "Blueprint")
    * You can now sample blueprints from dismantle mode
    * Pillars can partially intersect the edges of the [blueprint designer](/wiki/Blueprint_Designer "Blueprint Designer") again
  * [Hotbar](/wiki/HUD#Hotbar "HUD")
    * Hotbar system has been reworked
    * Added a way to save the current hologram into the hotbar by pressing [`Alt`](/wiki/Controls "Controls")+Shortcut key combination
    * You can now swap the Hotbar scroll direction in the “Controls” menu in the [Options menu](/wiki/Settings "Settings") (Clockwise and Counterclockwise)
  * [Conveyor Lifts](/wiki/Conveyor_Lifts "Conveyor Lifts")
    * Quick Switch [`E`](/wiki/Controls "Controls") is now supported when building them
    * Can now be Nudged
  * [Nudging](/wiki/Controls#Default_keybindings "Controls") (Arrow Keys) 
    * Holding [`Ctrl`](/wiki/Controls "Controls") when Nudging will now nudge in half steps
    * Fixed so Wall Mounted Flood Light Nudging is Vertical
  * [Zipline](/wiki/Zipline "Zipline")
    * Increased Zipline sprint acceleration. It should be easier to tell that sprint mode is turned on now due to the more direct change in speed
    * Zipline path selection now works vertically too
    * Additional improvements to try and mitigate cases where you get disconnected from ziplining when ziplining on an incline
  * [Power Tower](/wiki/Power_Tower "Power Tower")/[Power Poles](/wiki/Power_Poles "Power Poles")
    * Changed power poles and power towers to use gradual rotation (45 degrees on foundations)
    * Holding [`Ctrl`](/wiki/Controls "Controls") when building a wire off another wire now aligns the new Pole to the original one
    * Building a Power Tower off a wire from a Power Pole now correctly increases the build range for the Power Tower
  * [Hypertubes](/wiki/Hypertube "Hypertube")
    * Implemented network correction and smoothing for remote players moving in Hypertubes, This should make the movement inside hypertubes much smoother and prevent any kind of desync, this is also enabled for [Multiplayer](/wiki/Multiplayer "Multiplayer") and [Dedicated Servers](/wiki/Dedicated_Servers "Dedicated Servers") Clients
    * Fixed character getting too much acceleration when braking while going downhill
    * Fixed [hypertube attachments](/wiki/Hypertube_Supports "Hypertube Supports") incorrectly building when attaching them in a section of a hypertube
    * [Hypertube Entrances](/wiki/Hypertube_Entrance "Hypertube Entrance") can now be nudged
    * Hypertube entrances now work correctly when they are built directly on top of a floor hole
  * Input System 
    * Added an “Auto release sprint” [option](/wiki/Settings#Controls "Settings") when Hold to sprint is off, this option is off by default. This makes it so whenever your movement stops, the [`⇧ Left Shift`](/wiki/Controls "Controls") key is automatically released so you have to press it again to start sprinting
  * [Resource Miner](/wiki/Controls#Default_keybindings "Controls") (Hand Mining) 
    * Can now be Tap [`E`](/wiki/Controls "Controls") to Mine (Toggle) or Hold [`E`](/wiki/Controls "Controls") to Mine, depending on how long the button is held
    * Fixed a couple of issues with mining lingering around when walking away from the node
  * [Signs](/wiki/Signs "Signs")
    * Improved snapping for signs, they can now snap to foundation sides and ceilings and can be rotated more freely.
    * Changed signs to use the same snapping logic for walls and foundations
  * [Power Switch](/wiki/Power_Switch "Power Switch") and [Priority Power Switch](/wiki/Priority_Power_Switch "Priority Power Switch")
    * Both should now have gradual 45 degree rotation on foundations
    * Power Switches can now be upgraded to Priority Power Switches and vice versa
    * Added buttons for turning entire priority groups on and off in the Priority Power Switch
  * [Build Gun / Dismantle Gun](/wiki/Build_Gun "Build Gun")
    * When trying to dismantle invalid buildables they will now redirect to the valid dismantlable (I.E. Like the Integrated train tracks or the Sub Buildings of the Hub, they will now dismantle the Train Station and the entire Hub respectively)
  * [Splitters](/wiki/Splitter "Splitter")/[Mergers](/wiki/Merger "Merger")
    * Can now be upgraded to [Smart](/wiki/Smart_Splitter "Smart Splitter") or [Programmable](/wiki/Programmable_Splitter "Programmable Splitter") versions
    * Can also be upgraded to each other (Splitter to Merger and vice-versa) as long as only the main input and output is connected



## Optimisation

  * Parallelized post processing blending.
  * [Chaos memory](/wiki/Unreal_Engine "Unreal Engine") optimizations
  * Texture memory optimizations
  * Mesh memory optimizations
  * Enabled virtual textures for HLODs
  * Updated HLODs to use virtual textures.
  * Enabled PSO caching
  * Removed legacy assets



## Bug fixes

  * Fixed a bug where [drones](/wiki/Drone "Drone") would sometimes consume batteries multiple times when starting a new trip, especially when the player is far away
  * Refactored [player mapping](/wiki/Pioneer "Pioneer") contexts, reordered player mapping context priorities, so we have a clear hierarchy. This should potentially fix issues where certain actions like detonating Nobelisks cannot be done.
  * Fixed so quick switching [`E`](/wiki/Controls "Controls") a [conveyor](/wiki/Conveyor_Belt "Conveyor Belt")/[pipe](/wiki/Pipeline "Pipeline") doesn’t reset the hologram anymore.
  * Fixed bug where quick switching Pipeline and Conveyor holograms would reset pole rotation on the second build step
  * Fixed a rare UI crash
  * Fixed a bug where it was possible to accidentally delete items by [splitting](/wiki/Inventory "Inventory") them
  * Potential fix for bug where item stacks can not be split in the inventory for Client
  * Refactored [wire](/wiki/Power_Line "Power Line") splitting so it works with power towers
  * Fixed bug where build effects for wires never got cleaned up
  * Fixed so wire build effect works again
  * Fixed so poles created from wires copy the rotation of the pole you drag from
  * Fixed issue where changing materials ([Customizer](/wiki/Customizer "Customizer")) in the Quick Switch menu would stop working after the first time
  * Potential crash fix for an Input System related crash
  * Reworked [Object Scanner](/wiki/Object_Scanner "Object Scanner"), should now work correctly in Multiplayer, fixed multiple visual bugs
  * Fixed Clients not continuing to have [Flight Mode](/wiki/Advanced_Game_Settings#Gameplay "Advanced Game Settings") enabled after logging in and out of a session
  * Fixed [Bacon Agaric](/wiki/Bacon_Agaric "Bacon Agaric") not displaying properly when using a [Field of View (FOV)](/wiki/Settings#Camera_2 "Settings") other than 90
  * Fixed [Hover Pack](/wiki/Hover_Pack "Hover Pack") not displaying properly when using a Field of View (FOV) when loading into a save where the Hover Pack was already equipped
  * Fixed [Gas Mask](/wiki/Gas_Mask "Gas Mask") not displaying properly when using a Field of View (FOV) other than 90
  * Refactored the way [vehicles](/wiki/Vehicles "Vehicles") are outlined
  * Removed knockback when the player has Flight Mode enabled
  * [Flight Mode](/wiki/Advanced_Game_Settings "Advanced Game Settings") is no longer turned off when you use Turbo Bass with the [Boombox](/wiki/Boombox "Boombox") while it is enabled
  * Fixed [Hyper Tube Floor Holes](/wiki/Hypertube_Supports#Types "Hypertube Supports") appearing visually distorted
  * Fixed [railroad track signal visualization](/wiki/Train_Signals "Train Signals")
  * Fixed trajectory visualization for the [jump pads](/wiki/Jump_Pad "Jump Pad")
  * Fixed outlines displaying incorrectly on [Beams](/wiki/Beams "Beams")
  * Fixed [Ping](/wiki/Ping "Ping") indicator occasionally pinging the player
  * Fixed Resource Miner having an incorrect animation in [Multiplayer](/wiki/Multiplayer "Multiplayer") or when Holstering
  * Fixed [Chainsaw](/wiki/Chainsaw "Chainsaw"), [Xeno Basher](/wiki/Xeno-Basher "Xeno-Basher") and [Xeno Zapper](/wiki/Xeno-Zapper "Xeno-Zapper") displaying and behaving incorrectly in Multiplayer
  * Refactored the Gas Mask, fixing a lot of bugs with it
  * Refactored the [Flying Crab](/wiki/Flying_Crab "Flying Crab")
  * Fixed a bug where the [Blade Runners](/wiki/Blade_Runners "Blade Runners") would not work until after you jumped once after equipping them
  * Fixed bug where player can fall through world as a ragdoll when falling to far, It's still possible to clip through the world when traveling really fast as a ragdoll, but it's much more difficult and won't happen under normal circumstances.
  * Pipes having incorrect visuals when built in certain scenarios should now be fixed
  * Camera should not now rubber band as much when driving vehicles as it is now allowed to clip through various objects
  * Vehicle engines will now shut down when the vehicle is submerged in water
  * Fix head bobbing not working, and head bobbing scale option not affecting anything
  * Fixed so players don't get registered as an "aggressor" when dealing damage to a creature in passive mode. (Creature won’t immediately attack when changing from passive to retaliate)
  * Fixed being able to sample buildings when you shouldn’t (i.e. Inside a Hypertube)
  * Fixed Full Screen setting being reversed when pressing apply after restarting the game
  * Fixed players being unable to enter a vehicle if another player was interacting with the inventory of the vehicle
  * Fixed sliding not ending when entering vehicles
  * Fixed a specific [Copper Node](/wiki/Resource_node "Resource node") producing [Limestone](/wiki/Limestone "Limestone") if the miner was placed prior to Update 8
  * Removed a duplicate coal node
  * Improved visual quality of the [Blue Palm billboards](/wiki/World "World") when looking at them from very far away
  * Improved Beam Support to [Pillar](/wiki/Pillars "Pillars") snapping
  * Fixed [Nobelisk](/wiki/Nobelisk "Nobelisk") smoke not displaying properly
  * Fixed a specific case where aiming the Hypertube Floor Hole would flash the screen white
  * [Locomotives](/wiki/Electric_Locomotive "Electric Locomotive") should now start to brake when self driving is disabled
  * Fixed [MAM](/wiki/MAM "MAM") nodes showing up as unlockable when the tree itself is not unlocked when No Cost Advanced Game Setting is enabled
  * Fixed [Tractor](/wiki/Tractor "Tractor") headlights breaking when opening its inventory
  * Fixed Jumping off a zipline canceling the Zipline input if it's still held, now holding it will continue the input as it should



## UI

  * Updated [Map](/wiki/Map "Map") Render
  * Fixed multiple [Jetpack](/wiki/Jetpack "Jetpack") UI bugs
  * Fixed Game Phase Numbers and Naming in the [Advanced Game Settings](/wiki/Advanced_Game_Settings "Advanced Game Settings") menu
  * Renamed “Rotate Hologram” Keybinds into “Rotate Hologram Right” and “Rotate Hologram Left” so they no longer share the same name
  * Renamed “Nudge Up” and “Nudge Down” to “Nudge Forward” and “Nudge Backward”
  * Fixed Object Scanner UI disappearing when hopping in and out of vehicles
  * Fixed Object Scanner UI not showing the Object Name
  * Updated Storage UI so that [industrial storage boxes](/wiki/Industrial_Storage_Container "Industrial Storage Container") no longer use a scroll bar when using small inventory slots
  * Fixed issue where keyboard input was lost after manually entering text when [Overclocking](/wiki/Clock_speed "Clock speed")
  * Fixed a bug where you would have to click on the Gameplay sub-menu in the Options Menu twice
  * Trains are now sorted in the [Train Station](/wiki/Train_Station "Train Station") UI
  * Fixed an issue where [drag and drop](/wiki/Controls "Controls") wouldn’t be cancelled when opening up a different menu
  * Fixed issue where mouse would be lost if clicking the chat window by closing the window if the player clicks outside the text input box. If you close it by doing that you'll have to hit enter twice to open it again.
  * News Feed in the [Main Menu](/wiki/Game_menus "Game menus") should now be easier to read
  * Items in the Options Menu setting have been re-arranged in various menus, most noticeably in the Video menu



## Audio

  * Fixed an Audio issue leading to performance hitches in factories with [Blenders](/wiki/Blender "Blender") and [Refineries](/wiki/Refinery "Refinery"), including audio optimizations for the Refinery
  * Replaced some audio files for the [Tractor](/wiki/Tractor "Tractor") and [Truck](/wiki/Truck "Truck")
  * Tweaks and adjustments for Tractor and Truck audio



## Localisation

  * Fixed hundreds of typos across English (US) and English (UK)
  * Fixed Japanese and Traditional Han characters display, and added Devangari and Bengali support as well
  * Updated all languages with the latest translations
  * Updated language completion rates
  * Updated community translators in the credits



## Known issues

  * A reminder for people who have been having issues with unexpected crashes on startup or weird behavior with the game, in that case please try to verify your game files.  
You can do this on Steam by Right Clicking the game in your Library > Properties > Local Files > Verify integrity of game files...  
And on Epic by clicking on the three dots ("...") next to the title or at the right side, depending on your selected library view > Verify  
This may or may not redownload a large amount of files which might take a while depending on your internet connection or hard drive speeds so be wary of that.
  * If you are using mods, they might need to be updated or uninstalled after updating so please keep this in mind too.
  * The first time booting the game will be very slow, but that should not continue to happen after the first boot
  * Game can hang on quit
  * There is major performance loss when running out of VRAM
  * Factory Animation tick reductions can be slightly too aggressive
  * TSR can cause visual issues with conveyor belts, you can try using the following console command to alleviate the issues, but this will reduce AntiAliasing quality 
    * r.TSR.ShadingRejection.Flickering 0



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
Experimental Update 8| [0.8.0.0](/wiki/Patch_0.8.0.0 "Patch 0.8.0.0") • [0.8.0.1](/wiki/Patch_0.8.0.1 "Patch 0.8.0.1") • [0.8.0.2](/wiki/Patch_0.8.0.2 "Patch 0.8.0.2") • [0.8.0.3](/wiki/Patch_0.8.0.3 "Patch 0.8.0.3") • [0.8.0.4](/wiki/Patch_0.8.0.4 "Patch 0.8.0.4") • [0.8.0.5](/wiki/Patch_0.8.0.5 "Patch 0.8.0.5") • [0.8.1.0](/wiki/Patch_0.8.1.0 "Patch 0.8.1.0") • [0.8.1.1](/wiki/Patch_0.8.1.1 "Patch 0.8.1.1") • [0.8.1.2](/wiki/Patch_0.8.1.2 "Patch 0.8.1.2") • [0.8.1.3](/wiki/Patch_0.8.1.3 "Patch 0.8.1.3") • 0.8.2.0 • [0.8.2.1](/wiki/Patch_0.8.2.1 "Patch 0.8.2.1") • [0.8.2.2](/wiki/Patch_0.8.2.2 "Patch 0.8.2.2") • [0.8.2.3](/wiki/Patch_0.8.2.3 "Patch 0.8.2.3") • [0.8.2.4](/wiki/Patch_0.8.2.4 "Patch 0.8.2.4") • [0.8.2.5](/wiki/Patch_0.8.2.5 "Patch 0.8.2.5") • [0.8.2.6](/wiki/Patch_0.8.2.6 "Patch 0.8.2.6") • [0.8.2.7](/wiki/Patch_0.8.2.7 "Patch 0.8.2.7") • [0.8.2.8](/wiki/Patch_0.8.2.8 "Patch 0.8.2.8") • [0.8.2.9](/wiki/Patch_0.8.2.9 "Patch 0.8.2.9") • [0.8.3.1](/wiki/Patch_0.8.3.1 "Patch 0.8.3.1")  
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
