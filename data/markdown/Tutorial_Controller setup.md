# Tutorial:Controller setup

[](/wiki/File:Stub.svg "Outdated") | _This article is[outdated](/wiki/Category:Outdated "Category:Outdated"). You can help Satisfactory Wiki by [updating it](https://satisfactory.wiki.gg/wiki/Tutorial:Controller_setup?action=edit)._  
---|---  
  
_This article is[outdated](/wiki/Category:Outdated "Category:Outdated"). You can help Satisfactory Wiki by [updating it](https://satisfactory.wiki.gg/wiki/Tutorial:Controller_setup?action=edit)._  
  


As of [Version 1.1](/wiki/Patch_1.1.0.0 "Patch 1.1.0.0") official controller support became available for both Xbox and DualSense™ controllers. _The following information was made for Version 1.0 and earlier and will need revision as needed._

This page walks through the steps of **setting up controller layouts** for the controllers commonly used while playing _Satisfactory_. 

Satisfactory used to have unofficial partial controller support using legacy leftover inputs from default Unreal Engine 4. That functionality was removed in [Update 8](/wiki/Patch_0.8.0.5#UI "Patch 0.8.0.5"), as a result of the upgrade to Unreal Engine 5. The goal was to allow players to remap controls using third-party software in order to create their own custom controller layouts.[1]

It was announced during Satisfactory Version 1.0 Release livestream that along with the [console release](/wiki/Console_release "Console release") that the game will finally get official controller support for both consoles and PC.[2][3][4]

Release of game to Consoles is currently slated for **early 2025** _(but no specific date yet)_ and Coffee Stain Studios is considering doing an Experimental Branch for Controller Support on PC _(but no decision has been made yet)_.[5][6]

## Contents

  * 1 Steam Deck
    * 1.1 Guide
    * 1.2 Layout configurations
    * 1.3 Manual setup
      * 1.3.1 Steam settings
      * 1.3.2 Game settings
    * 1.4 Save File Location
      * 1.4.1 Save Files
      * 1.4.2 Blueprints
  * 2 Xbox
    * 2.1 Guide
    * 2.2 Layout configurations
    * 2.3 Manual setup
      * 2.3.1 Steam settings
      * 2.3.2 Game settings
  * 3 See also
  * 4 History
  * 5 References



## Steam Deck

Satisfactory was confirmed to work on the [Steam Deck™](https://store.steampowered.com/steamdeck) during the Update 5 Countdown Stream which shows the CSS Developers using the Steam Deck.[7]

Since then players have created custom controller layouts for the Steam Deck (see below). 

### Guide

See [Steam Deck Controller Guide - A Visual Introduction](https://steamcommunity.com/sharedfiles/filedetails/?id=2804823261)

### Layout configurations

There are multiple community supported layout configurations for the Steam Deck with the following created by Reddit Member u/punkgeek being popular.[8]. 

Configuration Name  | Notes   
---|---  
satisfactory-deck v6.0.1-SD  | Default Game Controls  
For direct access, in desktop-mode, open this link: **steam://controllerconfig/526870/3407115505**  
satisfactory-deck v5.4-PS4  | Bluetooth PS4/PS5 layout   
  
  * To pick these layouts you might need to press the Y button to "Show all layouts" _(see Screenshot 1)_ and then scroll down as needed.


  * [](/wiki/File:Layout_picker.png "Screenshot 1")

Screenshot 1



  * After picking your appropriate controller layout for your selected controller it should look approximately like Screenshot 2.


  * [](/wiki/File:Controller_picker.png "Screenshot 2")

Screenshot 2



  * After switching to either satisfactory-deck SD or PS4 _(as appropriate for your current controller)_ , the button assignments should look like Screenshot 3. You can see the current button assignments at any time by pressing the Steam button.


  * [](/wiki/File:Dualshock_controller.png "Screenshot 3")

Screenshot 3




### Manual setup

#### Steam settings

  * Change the proton version from the default to "Proton Experimental" - this fixes mouse cursor behavior when in text edit boxes (as of 10/21/24).
  * Change display resolution from "default" to 1980x1080. This makes things look better if you are using the external monitor output (rather than upscaling from the LCD resolution)
  * Use the 'per game profile' option and set "TDP limit" somewhere between 7 and 9 watts. **This is very important**. 
    * Satisfactory has some thread that spins _(unrelated to the required FPS render rate)_. If you don't set this limit it will suck an enormous amount of battery (for no benefit). In the late game with big factories you might need to increase this if you see your FPS begin to fall. Basically - just slide TDP slider down until you see FPS fall below 30 then bump it up a bit.



#### Game settings

  * Set all Video Settings to Low with the exception of the following.
  * In [Video > Display](/wiki/Settings#Display "Settings"): 
    * Set **Graphics API** to DX12 _(Vulkan is the 'native' Steam Deck API but the Satsifactory Vulkan port very rarely has draw errors and the DX12 performance is just fine on Steam Deck)._
    * Set **Fullscreen** to "Windowed Fullscreen" (not Fullscreen). This will allow the steamdeck to automatically change the game resolution when you undock from the TV to go handheld and vice versa.
    * Set **Max FPS** to 60
  * In [Video > Performance & Graphics Quality](/wiki/Settings#Performance_&_Graphics_Quality "Settings"): 
    * Set **Texture Quality** to High.
    * Set **Foliage Load Distance** to Default. (Note: in the very late game you _might_ want to lower this to Near - which helps FPS a lot, but looks poor IMO)
    * Set **Foliage Quality** to Medium.
    * Set **View Distance** to Medium or Far. (If you are setting your TDP limit very low you might need to use Medium to keep 30 fps, but Far looks better - so if you don't mind the battery draw go for that)
    * Turn off **Motion Blur**.
  * In [Video > Advanced](/wiki/Settings#Advanced "Settings"): 
    * Change **Upscaling Method** to Temporal Super Resolution (TSR) or AMD FidelityFX™ Super Resolution (FSR). 
      * NOTE 1: Testing has shown that TSR looks better then FSR and essentially has the same FPS game performance.
      * NOTE 2: The GPU in the Steam Deck is an AMD GPU so choosing Nvidia Deep Learning Super Sampling (DLSS) or Intel Xe Super Sampling (XeSS) will effectively disable upscaling.
      * All upscaling techniques can introduce slight draw artifacts - particularly for conveyor belt items. If this bothers you, increase the quality from Performance to Balanced or Quality.
    * Change **TSR Preset** to "Performance" or "Balanced" mode _(your choice on how much you value FPS vs appearance)._
  * In [User Interface](/wiki/Settings#User_Interface "Settings"): 
    * Set **HUD Scaling** to 1.1 _(to make text easier to read)_



### Save File Location

The Steam Deck save file location is similar to that for PC but for clarity here are the file paths for both Save Files and Blueprints:[9][10]

#### Save Files

`/home/deck/.steam/root/steamapps/compatdata/526870/pfx/dosdevices/c:/users/steamuser/AppData/Local/FactoryGame/Saved/SaveGames/{YOUR ID}/`

#### Blueprints

`/home/deck/.steam/root/steamapps/compatdata/526870/pfx/dosdevices/c:/users/steamuser/AppData/Local/FactoryGame/Saved/SaveGames/blueprints/`

## Xbox

Satisfactory can played using an [Xbox Wireless Controller](https://www.xbox.com/en-US/accessories/controllers/xbox-wireless-controller) instead of a keyboard or mouse. 

### Guide

See [How To Connect Xbox Wireless Controller to PC](https://support.xbox.com/en-US/help/hardware-network/controller/connect-xbox-wireless-controller-to-pc)

### Layout configurations

There are multiple layout configurations for the Xbox Wireless Controller with the following created by Reddit Member u/Specialist_Tone3879 for those interested.[11]

Configuration Name  | Notes   
---|---  
Update 8  | Default Game Controls   
  
See also [How To Configure an Xbox Wireless Controller](https://support.xbox.com/en-US/help/hardware-network/controller/customize-wireless-controller-with-accessories-app)

### Manual setup

Make sure your controller is on and properly connected to access all the following steps. View the related screenshots below for reference. 

#### Steam settings

  * Enter Steam Settings and go to the controller tab, there you will find enable Steam input for Xbox controllers - Enable this _(see Screenshot 1)_.


  * [](/wiki/File:Xbox_Controller_Setup_1.png "Screenshot 1")

Screenshot 1



  * Next head to your game library and on the tabs below the play button to the far right you will see controller layout. Click on the tab and then it will bring you to a controller setting screen _(see Screenshot 2)_.
  * You can download this controller layout by clicking "Your current layout" and head over to the search tab and search for "Update 8" it will show up. Or you can set up your own controller layout by hitting the "Edit Layout Tab".


  * [](/wiki/File:Xbox_Controller_Setup_2.png "Screenshot 2")

Screenshot 2




#### Game settings

  * View some of the basic game settings to help with setting up your own controller _(see Screenshot 3)_.


  * [](/wiki/File:Xbox_Controller_Setup_3.png "Screenshot 3")

Screenshot 3




## See also

  * [Controls](/wiki/Controls "Controls")
  * [Settings](/wiki/Settings "Settings")



## History

  * [Patch 0.8.0.5](/wiki/Patch_0.8.0.5 "Patch 0.8.0.5") Removed the legacy option for “Enable Gamepad Input” from the “Controls” submenu and removed leftover keybinds
  * [Patch 2018-10-17](/wiki/Patch_2018-10-17 "Patch 2018-10-17"): Unofficial partial controller support introduced



## References

  1. ↑ [YouTube - Update 8 Known Issues and State of FICSMAS - Controller Support](https://www.youtube.com/watch?v=UW1uFElp7ZE&t=397s)
  2. ↑ [YouTube - October 17th, 2023 Livestream - Q&A: Will there ever be full Controller Support?](https://www.youtube.com/watch?v=BgOj_3AhC7Q)
  3. ↑ [YouTube - Satisfactory 1.0 Launch Trailer - Satisfactory Coming To Consoles](https://www.youtube.com/watch?v=Jt4XOPiPJHs&t=133s)
  4. ↑ [YouTube - Satisfactory 1.0 Release Stream! - Official Controller Support Coming](https://www.youtube.com/watch?v=1GH5SZkrv2M&t=11387s)
  5. ↑ [YouTube - October 8th, 2024 - The Spill - Developer Explainers - Console Release](https://www.youtube.com/watch?v=T1HN4m32nr4&t=12019s)
  6. ↑ [YouTube - October 8th, 2024 - The Spill - Developer Explainers - Official Controller Support](https://www.youtube.com/watch?v=T1HN4m32nr4&t=12103s)
  7. ↑ [YouTube - Satisfactory UPDATE 5 Experimental Release Countdown](https://www.youtube.com/embed/Rumqu_lyapg?autoplay=1&start=1426&end=1588)
  8. ↑ [Reddit - Running Satisfactory on Steam Deck (an Updated Guide)](https://www.reddit.com/r/SatisfactoryGame/comments/1clp3yd/running_satisfactory_on_steam_deck_an_updated/)
  9. ↑ [Reddit - Finding save file on Steam Deck?](https://www.reddit.com/r/SatisfactoryGame/comments/1iyu8qr/finding_save_file_on_steam_deck/)
  10. ↑ [Reddit - Satisfactory blueprint and saved game location on Steam Deck](https://www.reddit.com/r/satisfactory/comments/176g5dr/satisfactory_blueprint_and_saved_game_location_on/)
  11. ↑ [Reddit - Update 8 Controller Layout](https://www.reddit.com/r/SatisfactoryGame/comments/17v9nor/update_8_controller_layout/)



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
Technical| [Console release](/wiki/Console_release "Console release") • [Debug console](/wiki/Debug_console "Debug console") • [Launch arguments](/wiki/Launch_arguments "Launch arguments") • [Save files](/wiki/Save_files "Save files") • [System requirements](/wiki/System_requirements "System requirements") • [Units](/wiki/Units "Units") • [Unreal Engine](/wiki/Unreal_Engine "Unreal Engine")  
Guides and tutorials| | Basics| [Walkthrough/How to play](/wiki/Tutorial:How_to_play "Tutorial:How to play") • [New Pioneer Guide](/wiki/Tutorial:New_Pioneer_Guide "Tutorial:New Pioneer Guide") • [Production line basics](/wiki/Tutorial:Production_line "Tutorial:Production line") • [Advanced production line tips](/wiki/Tutorial:Production_line_design_tips "Tutorial:Production line design tips") • [Picking an alternate recipe](/wiki/Tutorial:Picking_an_alternate_recipe "Tutorial:Picking an alternate recipe") • [Independency](/wiki/Tutorial:Independency "Tutorial:Independency") • [Aluminum Ingot production](/wiki/Tutorial:Setting_up_Aluminum_Ingot_production "Tutorial:Setting up Aluminum Ingot production")  
---|---  
Logistics| [Manifold](/wiki/Manifold "Manifold") • [Balancer](/wiki/Balancer "Balancer") • [Pipeline manifold](/wiki/Pipeline_manifold "Pipeline manifold") • [Prime Splitter Arrays](/wiki/Tutorial:Prime_splitter_arrays "Tutorial:Prime splitter arrays") • [Trains](/wiki/Tutorial:Trains "Tutorial:Trains") • [Train throughput](/wiki/Tutorial:Train_throughput "Tutorial:Train throughput")  
Dedicated servers| [Dedicated servers](/wiki/Dedicated_servers "Dedicated servers") • [Running as a Service](/wiki/Dedicated_servers/Running_as_a_Service "Dedicated servers/Running as a Service") • [Configuration files](/wiki/Dedicated_servers/Configuration_files "Dedicated servers/Configuration files") • [Automatic updates](/wiki/Dedicated_servers/Automatic_updates "Dedicated servers/Automatic updates") • [HTTPS API](/wiki/Dedicated_servers/HTTPS_API "Dedicated servers/HTTPS API") • [Lightweight Query API](/wiki/Dedicated_servers/Lightweight_Query_API "Dedicated servers/Lightweight Query API")  
Other| [Hypertube cannon](/wiki/Tutorial:Hypertube_cannon "Tutorial:Hypertube cannon") • [Hypertube brake](/wiki/Tutorial:Hypertube_brake "Tutorial:Hypertube brake") • Steam Deck & Controller setup • [Extracting UI icons](/wiki/Tutorial:Extracting_UI_icons "Tutorial:Extracting UI icons")
  *[v]: View this template
  *[e]: Edit this template
  *[h]: History of this template
  *[his]: his trivia section
