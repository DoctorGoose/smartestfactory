# Radiation

[](/wiki/File:Radiation.png)  
  
[](/wiki/File:Radiation.png "Enlarge")

Radiation intensity appears on screen when under the effects of radiation, due to being near a radioactive source.

**Radiation** refers to the effects of radioactive items and objects in the game, which cause [damage](/wiki/Damage "Damage") to the [pioneer](/wiki/Pioneer "Pioneer") unless a [Hazmat Suit](/wiki/Hazmat_Suit "Hazmat Suit") is worn. While radiation is in effect, the screen will become slightly distorted, [Geiger counter](https://en.wikipedia.org/wiki/Geiger_counter "wikipedia:Geiger counter") noises will be heard and a radiation intensity bar will appear in the upper part of the screen. 

Radiation effects are caused by being in proximity to radioactive sources. Radiation does not linger (except due to bugs). 

## Contents

  * 1 Radioactive sources
  * 2 Radiation levels
  * 3 Protection
  * 4 Tips
  * 5 Current issues
  * 6 History
  * 7 References



## Radioactive sources

Each radioactive source has a `ItemDecay` value, which determines how strongly it emits radiation: 

Item | ItemDecay | Stack ItemDecay   
---|---|---  
Uranium [Resource Node](/wiki/Resource_Node "Resource Node") | 10000 | 10000   
Uranium resource [deposit](/wiki/Deposit "Deposit") | 15 × Uranium contained (usually 54~66) | ~900 (varies)   
[](/wiki/Uranium "Uranium") [Uranium](/wiki/Uranium "Uranium") | 15 | 1500   
[](/wiki/Encased_Uranium_Cell "Encased Uranium Cell") [Encased Uranium Cell](/wiki/Encased_Uranium_Cell "Encased Uranium Cell") | 0.5 | 100   
[](/wiki/Uranium_Fuel_Rod "Uranium Fuel Rod") [Uranium Fuel Rod](/wiki/Uranium_Fuel_Rod "Uranium Fuel Rod") | 50 | 2500   
[](/wiki/Uranium_Waste "Uranium Waste") [Uranium Waste](/wiki/Uranium_Waste "Uranium Waste") | 10 | 5000   
[](/wiki/Non-Fissile_Uranium "Non-Fissile Uranium") [Non-Fissile Uranium](/wiki/Non-Fissile_Uranium "Non-Fissile Uranium") | 0.75 | 375   
[](/wiki/Plutonium_Pellet "Plutonium Pellet") [Plutonium Pellet](/wiki/Plutonium_Pellet "Plutonium Pellet") | 20 | 2000   
[](/wiki/Encased_Plutonium_Cell "Encased Plutonium Cell") [Encased Plutonium Cell](/wiki/Encased_Plutonium_Cell "Encased Plutonium Cell") | 120 | 24000   
[](/wiki/Plutonium_Fuel_Rod "Plutonium Fuel Rod") [Plutonium Fuel Rod](/wiki/Plutonium_Fuel_Rod "Plutonium Fuel Rod") | 250 | 12500   
[](/wiki/Plutonium_Waste "Plutonium Waste") [Plutonium Waste](/wiki/Plutonium_Waste "Plutonium Waste") | 200 | 100000   
[](/wiki/Ficsonium "Ficsonium") [Ficsonium](/wiki/Ficsonium "Ficsonium") | 250 | 25000   
[](/wiki/Ficsonium_Fuel_Rod "Ficsonium Fuel Rod") [Ficsonium Fuel Rod](/wiki/Ficsonium_Fuel_Rod "Ficsonium Fuel Rod") | 1000 | 50000   
  
Due to having both a very high ItemDecay value _and_ a [stack](/wiki/Stack "Stack") size of 500, Plutonium Waste has the highest density of radiation per inventory slot. 

All sources of radiation glow in the dark. 

## Radiation levels

The formula for calculating the radiation level (intensity) is: ItemCount×ItemDecay×e−x/RadiationFallOffDistance4πx2

Where: 

  * ItemCount = Number of items. So 2 stacks of Uranium counted as 200.
  * ItemDecay: Refer to the table above.
  * e≈2.71828 _(Constant[Euler's number](https://en.wikipedia.org/wiki/E_\(mathematical_constant\)))_
  * RadiationFallOffDistance=80 _(Constant)_
  * x = Distance between the player and the item, in meters



Radiation intensity for multiple radioactive sources, such as items in different containers, are summed scalar in 3D. After the summation, the intensity level is then capped between 0.2 (0.44% radiation damage) and 45 (100% radiation damage). A pioneer will not receive any [damage](/wiki/Damage "Damage") below 0.2 intensity. Beyond 45, the radiation damage is capped, which at this intensity, kills the pioneer in 5 seconds or consumes the [Iodine Infused Filter](/wiki/Iodine_Infused_Filter "Iodine Infused Filter") at a maximum rate of 1 per 12 seconds. In-between, the filter lasts proportionally longer as the radiation intensity decreases. The radiation intensity bar in the game screen is capped at 26.7% radiation damage. 

Items closer than 0.5 meters or in the inventory are counted as x = 0.5 meters. 

The calculation applies to all radiation sources: 

  * [Resource nodes](/wiki/Resource_node "Resource node") and [resource deposits](/wiki/Resource_deposit "Resource deposit")
  * Items on [Conveyor Belts](/wiki/Conveyor_Belts "Conveyor Belts") or the ground
  * Items in buildings with any inventory slots, such as: 
    * [Miners](/wiki/Miner "Miner")
    * Production buildings
    * [Storage Containers](/wiki/Storage_Container "Storage Container"), [Industrial Storage Containers](/wiki/Industrial_Storage_Container "Industrial Storage Container") or [Personal Storage Boxs](/wiki/Personal_Storage_Box "Personal Storage Box"),
  * Items carried in the player [inventory](/wiki/Inventory "Inventory") or a [Lizard Doggo](/wiki/Lizard_Doggo "Lizard Doggo")
  * [Death and dismantle crates](/wiki/Crate "Crate")



Radiation effects apply only to [pioneers](/wiki/Pioneer "Pioneer"). Other creatures, including Lizard Doggos carrying a radioactive item, are immune. 

## Protection

In [Tier 7](/wiki/Tier_7 "Tier 7"), a [Hazmat Suit](/wiki/Hazmat_Suit "Hazmat Suit") can be unlocked via its respective milestone. Having the suit with [Iodine Infused Filters](/wiki/Hazmat_Suit#Iodine_Infused_Filter-0 "Hazmat Suit") on will protect the pioneer from Radiation damage. As the suit requires [Alclad Aluminum Sheets](/wiki/Alclad_Aluminum_Sheet "Alclad Aluminum Sheet") to craft, it is required to complete the Bauxite Refinement milestone first. 

Entering any [vehicle](/wiki/Vehicle "Vehicle") also stops the pioneer from taking radiation damage. 

Foundations, walls, terrain and water do not reduce radiation levels by any means. 

## Tips

  * Be careful when hand-mining Uranium deposits, as Uranium in the inventory can kill the [pioneer](/wiki/Pioneer "Pioneer") quickly.[1]
  * Any Uranium Ore in the Inventory can be dragged to the inventory trash slot which will stop any radiation. However, Uranium Waste and its products, excluding Plutonium Fuel Rods, but including Plutonium Waste, cannot be discarded using the inventory trash slot.
  * Area radiation is often calculated when a save is loaded, which leads to a bug where mining [Uranium](/wiki/Uranium "Uranium") [deposits](/wiki/Deposit "Deposit") will not clear the area of radiation. In order to clear the radiation level of an area, clear the Uranium deposits, save the game (after clearing the inventory), and reload the save. This will recalculate the radiation level of the area, clearing the area of radiation if there are no radiation sources remaining nearby.
  * If using the [Dimensional Depot Uploader](/wiki/Dimensional_Depot_Uploader "Dimensional Depot Uploader") and have access to the Dimensional Depot you can send any radioactive part from your [Inventory](/wiki/Inventory "Inventory") to the Dimensional Depot which will stop all radiation.[2]



## Current issues

  * Sorting the [inventory](/wiki/Inventory "Inventory") or a [Storage Container](/wiki/Storage_Container "Storage Container") will cause the radiation to persist even after radioactive items are removed. This lasts until the game is reloaded (or the Storage Container is [dismantled](/wiki/Dismantle "Dismantle")).
  * Radiation of [Uranium](/wiki/Uranium "Uranium") [deposits](/wiki/Deposit "Deposit") will persist until the save is reloaded, even after a deposit is completely destroyed.



## History

[](/wiki/File:Icon-boilerplate.png) | The history section is incomplete in this article. Please help [expanding it](https://satisfactory.wiki.gg/wiki/Radiation?action=edit) if you can. Information can be gathered from [patch notes](/wiki/Category:Patch_notes "Category:Patch notes").   
---|---  
  
  * [Patch 0.4.0.11](/wiki/Patch_0.4.0.11 "Patch 0.4.0.11"): Updated radiation levels to fit new item production rates.
  * [Patch 0.4.0.0](/wiki/Patch_0.4.0.0 "Patch 0.4.0.0"): Tweaked the radiation decay value for [Uranium Waste](/wiki/Uranium_Waste "Uranium Waste")



## References

  1. ↑ [Reddit - Radiation? How do I protect myself from it?](https://www.reddit.com/r/SatisfactoryGame/comments/b628ck/radiation_how_do_i_protect_myself_from_it/)
  2. ↑ [Reddit - PSA: Radiation doesn't seem to cross the dimensional barrier once uploaded](https://www.reddit.com/r/SatisfactoryGame/comments/1ggh0q4/psa_radiation_doesnt_seem_to_cross_the/)



  * [v](/wiki/Template:PioneerNav "Template:PioneerNav")
  * [e](https://satisfactory.wiki.gg/wiki/Template:PioneerNav?action=edit)
  * [h](https://satisfactory.wiki.gg/wiki/Template:PioneerNav?action=history)

[Satisfactory](/wiki/Satisfactory "Satisfactory") game mechanics  
---  
Player abilities| [Codex](/wiki/Codex "Codex") • [Resource Scanner](/wiki/Resource_Scanner "Resource Scanner") • [Build Gun](/wiki/Build_Gun "Build Gun") • [Inventory](/wiki/Inventory "Inventory") • [Health](/wiki/Health "Health") • [Combat](/wiki/Combat "Combat") • [Movement](/wiki/Movement "Movement") • [Flashlight](/wiki/Flashlight "Flashlight") • [HUD](/wiki/HUD "HUD") • [Crate](/wiki/Crate "Crate") • [To-Do List](/wiki/To-Do_List "To-Do List")  
Unlockable abilities| [Recipes](/wiki/Recipes "Recipes") • [Power](/wiki/Power "Power") • [Overclocking/Underclocking](/wiki/Clock_speed "Clock speed") • [Production amplifier](/wiki/Production_amplifier "Production amplifier") • [Customizer](/wiki/Customizer "Customizer") • [Map](/wiki/Map "Map") • [Productivity Display](/wiki/Productivity_Display "Productivity Display") • [Head lift](/wiki/Head_lift "Head lift") • [Blueprints](/wiki/Blueprints "Blueprints") • [Fuels](/wiki/Category:Fuels "Category:Fuels") • [FICSIT Productive Packer Deluxe](/wiki/FICSIT_Productive_Packer_Deluxe "FICSIT Productive Packer Deluxe")  
Progression| [Story](/wiki/Story "Story") • [Drop-pod](/wiki/Drop-pod "Drop-pod") • [Onboarding (In-game tutorial)](/wiki/Onboarding "Onboarding") • [Milestones](/wiki/Milestones "Milestones") • [MAM](/wiki/MAM "MAM") • [Alternate recipes](/wiki/Hard_Drive#Alternate_recipes "Hard Drive") • [Space Elevator](/wiki/Space_Elevator "Space Elevator") • [AWESOME Sink](/wiki/AWESOME_Sink "AWESOME Sink") • [AWESOME Shop](/wiki/AWESOME_Shop "AWESOME Shop")  
Seasonal events| [April Fools' Day](/wiki/April_Fools%27_Day "April Fools' Day") • [Anniversary](/wiki/Anniversary "Anniversary") • [FICSMAS](/wiki/FICSMAS "FICSMAS")  
Environment| [World](/wiki/World "World") • [Resource Node](/wiki/Resource_Node "Resource Node") • [Resource Well](/wiki/Resource_Well "Resource Well") • [Resource renewability](/wiki/Resource_renewability "Resource renewability") • [Crash Site](/wiki/Crash_Site "Crash Site") • Radiation • [Poison Gas](/wiki/Poison_Gas "Poison Gas") • [Cracked boulder](/wiki/Cracked_boulder "Cracked boulder") • [Cave](/wiki/Cave "Cave")  
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
