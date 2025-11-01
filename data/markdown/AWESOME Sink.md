# AWESOME Sink

“  | _Go that extra kilometer, go AWESOME._ | „   
---|---|---  
| ~ **[ADA](/wiki/ADA "ADA")** |   
  
## AWESOME Sink

[ ](/wiki/File:AWESOME_Sink.png "AWESOME Sink.png")

_Got excess resources? Fear not, for FICSIT does not waste! The newly developed AWESOME Sink turns any and all useful parts into research data just as fast as you can supply them!  
Participating pioneers will be compensated with Coupons that can be spent at the AWESOME Shop._

### Unlocked by

[Tier 2](/wiki/Tier_2 "Tier 2") \- Resource Sink Bonus Program

### Class name

Desc_ResourceSink_C

## Building

### [Power  
usage](/wiki/Power "Power")

30 MW

### [Overclock­able](/wiki/Clock_speed "Clock speed")

No

### Conveyor  
inputs

1

## Dimensions

### Width

16 m

### Length

13 m

### Height

24 m

### Area

208 m2

## Ingre­dients

**15 ×[](/wiki/Reinforced_Iron_Plate "Reinforced Iron Plate") [Reinforced Iron Plate](/wiki/Reinforced_Iron_Plate "Reinforced Iron Plate")**

**30 ×[](/wiki/Cable "Cable") [Cable](/wiki/Cable "Cable")**

**45 ×[](/wiki/Concrete "Concrete") [Concrete](/wiki/Concrete "Concrete")**

The **AWESOME Sink** is a special [building](/wiki/Building "Building") that produces [](/wiki/FICSIT_Coupon "FICSIT Coupon") [FICSIT Coupons](/wiki/FICSIT_Coupon "FICSIT Coupon") for use in the [AWESOME Shop](/wiki/AWESOME_Shop "AWESOME Shop") by destroying items inserted into it and converting them into points based on their value or complexity. These points are used to print the aforementioned Coupons, with each successive Coupon requiring more points according to a mathematical formula. In addition to normal items, [Alien DNA Capsules](/wiki/Alien_DNA_Capsule "Alien DNA Capsule") can also be sunk and their AWESOME Points are counted separately. 

The Sink can consume as many parts as the connected conveyor can supply, therefore its maximum capacity is 1,200/min using a [Conveyor Belt Mk.6](/wiki/Conveyor_Belt_Mk.6 "Conveyor Belt Mk.6") or [Conveyor Lift Mk.6](/wiki/Conveyor_Lift_Mk.6 "Conveyor Lift Mk.6"). 

Multiple Sinks can be constructed. Accumulated points will be shared between all Sinks, and Coupons can be printed from any of them. If all Sinks are deconstructed, the amount of points and accumulated Coupons is not lost. 

AWESOME is an acronym, which stands for "Anti-Waste Effort for Stress-Testing of Materials on Exoplanets". 

## Contents

  * 1 Items not allowed to sink
  * 2 Coupon cost
    * 2.1 Coupon cost from Alien DNA Capsules
    * 2.2 Printing
  * 3 Points generated per item
  * 4 Recipe point improvement ratios
  * 5 Tips
    * 5.1 Farming points
  * 6 Achievements
  * 7 Trivia
  * 8 See also
  * 9 Gallery
  * 10 History
  * 11 References



## Items not allowed to sink

Some items cannot be fed into the AWESOME Sink and will clog the input. If that happens, it is advised to pick up these items or reconstruct the input belt to allow other items to be sunk. 

  * Consumables such as [Beryl Nuts](/wiki/Beryl_Nut "Beryl Nut"), [Bacon Agarics](/wiki/Bacon_Agaric "Bacon Agaric"), and [Paleberries](/wiki/Paleberries "Paleberries") (does not apply to [Medicinal Inhalers](/wiki/Medicinal_Inhaler "Medicinal Inhaler"))
  * Special items such as [Power Slugs](/wiki/Power_Slug "Power Slug"), [Power Shards](/wiki/Power_Shard "Power Shard"), [Hard Drives](/wiki/Hard_Drive "Hard Drive"), [Mercer Spheres](/wiki/Mercer_Sphere "Mercer Sphere") and [Somersloops](/wiki/Somersloop "Somersloop")
  * [Alien Remains](/wiki/Alien_Remains "Alien Remains") and [Alien Protein](/wiki/Alien_Protein "Alien Protein")
  * [Uranium Waste](/wiki/Uranium_Waste "Uranium Waste") and every derived item with [Plutonium Fuel Rods](/wiki/Plutonium_Fuel_Rod "Plutonium Fuel Rod") being the only exception; a warning that [radioactive](/wiki/Radioactive "Radioactive") items are not allowed for contaminating the results will be shown
  * [Quantum Computers](/wiki/Quantum_Computer "Quantum Computer") as they are now unobtainable



## Coupon cost

Coupons increase in point cost as more are acquired, until the 2,998th coupon. The first three coupons cost 500 points. After that, the cost for the n-th coupon (through 3,000) is calculated as `250 * (ceil(n/3)-1)2 + 1000` or `250*POWER((CEILING.MATH(N/3)-1),2)+1000`. Once the 2,998th coupon is reached, every subsequent coupon will cost 249,501,250 points. Until that point, when the current cost of a coupon is known, then the number of coupons that have been printed is `(sqrt((cost-1000)/250)+1)*3`. 

In mathematical terms, the cost of the _n_ -th coupon (through coupon 3,000) is given by: 

    cost(n)=250×(⌈n3⌉−1)2+1000

Coupons starting with 3,001 will share the cost of coupons 2,998-3,000. 

Given the current cost _c_ of a coupon, for _c_ below 249,501,250, the number of coupons that have been printed is between 

    3×c−1000250
    and
    3×c−1000250+2
    (inclusive)

The cumulative cost for printing the first _n_ coupons (through 3,000), if _n_ is a multiple of 3, is given by: 

    C(n)=25027n3−1253n2+31253n−1500

It takes 1,895 Coupons to purchase every non-producible item in the AWESOME Shop, which would require 125,721,388,500 AWESOME points. This would take about 11 hours and 23 minutes at the current [theoretical max awesome points per minute](/wiki/AWESOME_Sink/Theoretical_maximum_of_points "AWESOME Sink/Theoretical maximum of points") of 184,168,000 (see § Farming Points). However, it only takes 347 Coupons to unlock every non-repeatable purchase, which equates to 382,231,750 AWESOME points, or 20,242 Alien DNA capsules if earned purely with one or the other (mixing both sources is more efficient). 

Patch notes and in-game dialogue suggest further items will be added to the AWESOME shop in future releases. 

Group | n-th Coupon | Cost | Cumulative cost   
---|---|---|---  
0 | 1-3 | 500 | 1,500   
1 | 4-6 | 1,250 | 5,250   
2 | 7-9 | 2,000 | 11,250   
3 | 10-12 | 3,250 | 21,000   
4 | 13-15 | 5,000 | 36,000   
5 | 16-18 | 7,250 | 57,750   
6 | 19-21 | 10,000 | 87,750   
7 | 22-24 | 13,250 | 127,500   
8 | 25-27 | 17,000 | 178,500   
9 | 28-30 | 21,250 | 242,250   
... | ... | ... | ...   
29 | 88-90 | 211,250 | 6,504,750   
... | ... | ... | ...   
332 | 997-999 | 27,557,000 | 9,190,965,000   
n (n = 0, 1, 2, ..., 999) | 3n + 1 to 3n + 3 | 250n2 \+ 1000 | 250n3 \+ 375n2 \+ 3125n + 1500   
_n/a_ | c (c = 3001, 3002, ...) | 249,501,250 | 249,628,123,500 + 249,501,250(c-3000)   
  
### Coupon cost from Alien DNA Capsules

[Alien DNA Capsules](/wiki/Alien_DNA_Capsule "Alien DNA Capsule") have a separate point counter. Unlike the standard coupon cost, it increases linearly by 1000 points for each group of coupons. 

In mathematical terms, the cost of the _n_ -th coupon is given by: 

    cost(n)=1000×⌈n3⌉

And the cumulative cost of the first _n_ coupons is given by: 

    ccost(n)=(⌊n3⌋+1)×(1000×n−1500×⌊n3⌋)

The table below shows the points required per coupon when sinking Alien DNA Capsules, which are worth 1000 points each. 

Group | n-th Coupon | Cost | Cumulative cost   
---|---|---|---  
1 | 1-3 | 1,000 | 3,000   
2 | 4-6 | 2,000 | 9,000   
3 | 7-9 | 3,000 | 18,000   
4 | 10-12 | 4,000 | 30,000   
5 | 13-15 | 5,000 | 45,000   
6 | 16-18 | 6,000 | 63,000   
n (n = 1, 2, ...) | 3n - 2 to 3n | 1000n | 1500n2 \+ 1500n   
  
### Printing

Once sufficient points are accumulated to print at least one Coupon, the option to print it is made available. Printing coupons does not require the AWESOME Sink to be powered. As the 'Print' button is pressed, an animation is played, where a Coupon comes out of the slot with the actual Coupon items. These coupons may be retrieved by dragging them into the inventory or using ([`⇧ Shift`](/wiki/Controls "Controls") \+ [](/wiki/File:Keyboard_White_Mouse_Left.png "Left")). Coupons have a stack size of 500, so if the amount of accumulated coupons exceeds 500, the remaining coupons will remain in the Sink, and they can be printed out next time. 

If coupons are printed but not taken out and the UI of the Sink is closed, those coupons can be re-printed the next time the AWESOME Sink UI is opened. 

It's also possible to put Coupons back into the Sink using this mechanic by printing Coupons and instead of taking any, moving Coupons in the inventory into the Sink slot. This is only possible if at least one Coupon can be printed and the sum of Coupons in the Sink and the inventory does not exceed 500 (if it does, less than a full stack or no Coupons can be inserted back). 

[](/wiki/File:New_Awesome_Sink_UI.png)

[](/wiki/File:New_Awesome_Sink_UI.png "Enlarge")

The UI of an AWESOME Sink.

## Points generated per item

Points | Items   
---|---  
Cannot be sunk | [](/wiki/Alien_Protein "Alien Protein") [Alien Protein](/wiki/Alien_Protein "Alien Protein"), [](/wiki/Bacon_Agaric "Bacon Agaric") [Bacon Agaric](/wiki/Bacon_Agaric "Bacon Agaric"), [](/wiki/Beryl_Nut "Beryl Nut") [Beryl Nut](/wiki/Beryl_Nut "Beryl Nut"), [](/wiki/Blue_Power_Slug "Blue Power Slug") [Blue Power Slug](/wiki/Blue_Power_Slug "Blue Power Slug"), [](/wiki/Encased_Plutonium_Cell "Encased Plutonium Cell") [Encased Plutonium Cell](/wiki/Encased_Plutonium_Cell "Encased Plutonium Cell"), [](/wiki/FICSIT_Coupon "FICSIT Coupon") [FICSIT Coupon](/wiki/FICSIT_Coupon "FICSIT Coupon"), [](/wiki/Ficsonium_Fuel_Rod "Ficsonium Fuel Rod") [Ficsonium Fuel Rod](/wiki/Ficsonium_Fuel_Rod "Ficsonium Fuel Rod"), [](/wiki/Ficsonium "Ficsonium") [Ficsonium](/wiki/Ficsonium "Ficsonium"), [](/wiki/Hatcher_Remains "Hatcher Remains") [Hatcher Remains](/wiki/Hatcher_Remains "Hatcher Remains"), [](/wiki/Hog_Remains "Hog Remains") [Hog Remains](/wiki/Hog_Remains "Hog Remains"), [](/wiki/Mercer_Sphere "Mercer Sphere") [Mercer Sphere](/wiki/Mercer_Sphere "Mercer Sphere"), [](/wiki/Non-Fissile_Uranium "Non-Fissile Uranium") [Non-Fissile Uranium](/wiki/Non-Fissile_Uranium "Non-Fissile Uranium"), [](/wiki/Paleberry "Paleberry") [Paleberry](/wiki/Paleberry "Paleberry"), [](/wiki/Plutonium_Pellet "Plutonium Pellet") [Plutonium Pellet](/wiki/Plutonium_Pellet "Plutonium Pellet"), [](/wiki/Plutonium_Waste "Plutonium Waste") [Plutonium Waste](/wiki/Plutonium_Waste "Plutonium Waste"), [](/wiki/Power_Shard "Power Shard") [Power Shard](/wiki/Power_Shard "Power Shard"), [](/wiki/Purple_Power_Slug "Purple Power Slug") [Purple Power Slug](/wiki/Purple_Power_Slug "Purple Power Slug"), [](/wiki/Somersloop "Somersloop") [Somersloop](/wiki/Somersloop "Somersloop"), [](/wiki/Spitter_Remains "Spitter Remains") [Spitter Remains](/wiki/Spitter_Remains "Spitter Remains"), [](/wiki/Stinger_Remains "Stinger Remains") [Stinger Remains](/wiki/Stinger_Remains "Stinger Remains"), [](/wiki/Uranium_Waste "Uranium Waste") [Uranium Waste](/wiki/Uranium_Waste "Uranium Waste"), [](/wiki/Yellow_Power_Slug "Yellow Power Slug") [Yellow Power Slug](/wiki/Yellow_Power_Slug "Yellow Power Slug")  
1 | [](/wiki/Blue_FICSMAS_Ornament "Blue FICSMAS Ornament") [Blue FICSMAS Ornament](/wiki/Blue_FICSMAS_Ornament "Blue FICSMAS Ornament"), [](/wiki/FICSIT_Coupon "FICSIT Coupon") [FICSIT Coupon](/wiki/FICSIT_Coupon "FICSIT Coupon"), [](/wiki/FICSMAS_Gift "FICSMAS Gift") [FICSMAS Gift](/wiki/FICSMAS_Gift "FICSMAS Gift"), [](/wiki/Iron_Ore "Iron Ore") [Iron Ore](/wiki/Iron_Ore "Iron Ore")  
2 | [](/wiki/FICSMAS_Tree_Branch "FICSMAS Tree Branch") [FICSMAS Tree Branch](/wiki/FICSMAS_Tree_Branch "FICSMAS Tree Branch"), [](/wiki/Iron_Ingot "Iron Ingot") [Iron Ingot](/wiki/Iron_Ingot "Iron Ingot"), [](/wiki/Limestone "Limestone") [Limestone](/wiki/Limestone "Limestone"), [](/wiki/Red_FICSMAS_Ornament "Red FICSMAS Ornament") [Red FICSMAS Ornament](/wiki/Red_FICSMAS_Ornament "Red FICSMAS Ornament"), [](/wiki/Screws "Screws") [Screws](/wiki/Screws "Screws")  
3 | [](/wiki/Coal "Coal") [Coal](/wiki/Coal "Coal"), [](/wiki/Copper_Ore "Copper Ore") [Copper Ore](/wiki/Copper_Ore "Copper Ore"), [](/wiki/Leaves "Leaves") [Leaves](/wiki/Leaves "Leaves")  
4 | [](/wiki/FICSMAS_Bow "FICSMAS Bow") [FICSMAS Bow](/wiki/FICSMAS_Bow "FICSMAS Bow"), [](/wiki/Iron_Rod "Iron Rod") [Iron Rod](/wiki/Iron_Rod "Iron Rod")  
5 | [](/wiki/FICSMAS_Actual_Snow "FICSMAS Actual Snow") [FICSMAS Actual Snow](/wiki/FICSMAS_Actual_Snow?action=edit&redlink=1 "FICSMAS Actual Snow \(page does not exist\)")  
6 | [](/wiki/Candy_Cane "Candy Cane") [Candy Cane](/wiki/Candy_Cane "Candy Cane"), [](/wiki/Copper_Ingot "Copper Ingot") [Copper Ingot](/wiki/Copper_Ingot "Copper Ingot"), [](/wiki/Iron_Plate "Iron Plate") [Iron Plate](/wiki/Iron_Plate "Iron Plate"), [](/wiki/Wire "Wire") [Wire](/wiki/Wire "Wire")  
7 | [](/wiki/Caterium_Ore "Caterium Ore") [Caterium Ore](/wiki/Caterium_Ore "Caterium Ore")  
8 | [](/wiki/Bauxite "Bauxite") [Bauxite](/wiki/Bauxite "Bauxite"), [](/wiki/Iron_Rebar "Iron Rebar") [Iron Rebar](/wiki/Iron_Rebar "Iron Rebar"), [](/wiki/Steel_Ingot "Steel Ingot") [Steel Ingot](/wiki/Steel_Ingot "Steel Ingot")  
10 | [](/wiki/Mycelia "Mycelia") [Mycelia](/wiki/Mycelia "Mycelia")  
11 | [](/wiki/Sulfur "Sulfur") [Sulfur](/wiki/Sulfur "Sulfur")  
12 | [](/wiki/Biomass "Biomass") [Biomass](/wiki/Biomass "Biomass"), [](/wiki/Concrete "Concrete") [Concrete](/wiki/Concrete "Concrete"), [](/wiki/Polymer_Resin "Polymer Resin") [Polymer Resin](/wiki/Polymer_Resin "Polymer Resin")  
14 | [](/wiki/Black_Powder "Black Powder") [Black Powder](/wiki/Black_Powder "Black Powder")  
15 | [](/wiki/Raw_Quartz "Raw Quartz") [Raw Quartz](/wiki/Raw_Quartz "Raw Quartz")  
17 | [](/wiki/Quickwire "Quickwire") [Quickwire](/wiki/Quickwire "Quickwire")  
18 | [](/wiki/Iron_FICSMAS_Ornament "Iron FICSMAS Ornament") [Iron FICSMAS Ornament](/wiki/Iron_FICSMAS_Ornament "Iron FICSMAS Ornament")  
20 | [](/wiki/Petroleum_Coke "Petroleum Coke") [Petroleum Coke](/wiki/Petroleum_Coke "Petroleum Coke"), [](/wiki/SAM "SAM") [SAM](/wiki/SAM "SAM"), [](/wiki/Silica "Silica") [Silica](/wiki/Silica "Silica")  
24 | [](/wiki/Cable "Cable") [Cable](/wiki/Cable "Cable"), [](/wiki/Copper_Sheet "Copper Sheet") [Copper Sheet](/wiki/Copper_Sheet "Copper Sheet"), [](/wiki/Steel_Pipe "Steel Pipe") [Steel Pipe](/wiki/Steel_Pipe "Steel Pipe")  
25 | [](/wiki/Rifle_Ammo "Rifle Ammo") [Rifle Ammo](/wiki/Rifle_Ammo "Rifle Ammo")  
27 | [](/wiki/Aluminum_Scrap "Aluminum Scrap") [Aluminum Scrap](/wiki/Aluminum_Scrap "Aluminum Scrap")  
28 | [](/wiki/Compacted_Coal "Compacted Coal") [Compacted Coal](/wiki/Compacted_Coal "Compacted Coal")  
30 | [](/wiki/Snowball "Snowball") [Snowball](/wiki/Snowball "Snowball"), [](/wiki/Wood "Wood") [Wood](/wiki/Wood "Wood")  
32 | [](/wiki/Copper_FICSMAS_Ornament "Copper FICSMAS Ornament") [Copper FICSMAS Ornament](/wiki/Copper_FICSMAS_Ornament "Copper FICSMAS Ornament"), [](/wiki/Sparkly_Fireworks "Sparkly Fireworks") [Sparkly Fireworks](/wiki/Sparkly_Fireworks "Sparkly Fireworks")  
35 | [](/wiki/Uranium "Uranium") [Uranium](/wiki/Uranium "Uranium")  
40 | [](/wiki/Fancy_Fireworks "Fancy Fireworks") [Fancy Fireworks](/wiki/Fancy_Fireworks "Fancy Fireworks")  
42 | [](/wiki/Caterium_Ingot "Caterium Ingot") [Caterium Ingot](/wiki/Caterium_Ingot "Caterium Ingot")  
48 | [](/wiki/Solid_Biofuel "Solid Biofuel") [Solid Biofuel](/wiki/Solid_Biofuel "Solid Biofuel")  
50 | [](/wiki/Quartz_Crystal "Quartz Crystal") [Quartz Crystal](/wiki/Quartz_Crystal "Quartz Crystal")  
56 | [](/wiki/Portable_Miner "Portable Miner") [Portable Miner](/wiki/Portable_Miner "Portable Miner")  
58 | [](/wiki/Smokeless_Powder "Smokeless Powder") [Smokeless Powder](/wiki/Smokeless_Powder "Smokeless Powder")  
60 | [](/wiki/Empty_Canister "Empty Canister") [Empty Canister](/wiki/Empty_Canister "Empty Canister"), [](/wiki/Rubber "Rubber") [Rubber](/wiki/Rubber "Rubber"), [](/wiki/Sweet_Fireworks "Sweet Fireworks") [Sweet Fireworks](/wiki/Sweet_Fireworks "Sweet Fireworks")  
64 | [](/wiki/Steel_Beam "Steel Beam") [Steel Beam](/wiki/Steel_Beam "Steel Beam")  
72 | [](/wiki/Copper_Powder "Copper Powder") [Copper Powder](/wiki/Copper_Powder "Copper Powder")  
75 | [](/wiki/Plastic "Plastic") [Plastic](/wiki/Plastic "Plastic")  
84 | [](/wiki/%27Employee_of_the_Planet%27_Cup "'Employee of the Planet' Cup") ['Employee of the Planet' Cup](/wiki/%27Employee_of_the_Planet%27_Cup "'Employee of the Planet' Cup"), [](/wiki/Cup "Cup") [Cup](/wiki/Cup "Cup")  
100 | [](/wiki/FICSMAS_Ornament_Bundle "FICSMAS Ornament Bundle") [FICSMAS Ornament Bundle](/wiki/FICSMAS_Ornament_Bundle "FICSMAS Ornament Bundle")  
120 | [](/wiki/Reinforced_Iron_Plate "Reinforced Iron Plate") [Reinforced Iron Plate](/wiki/Reinforced_Iron_Plate "Reinforced Iron Plate"), [](/wiki/Turbo_Rifle_Ammo "Turbo Rifle Ammo") [Turbo Rifle Ammo](/wiki/Turbo_Rifle_Ammo "Turbo Rifle Ammo")  
125 | [](/wiki/Medicinal_Inhaler "Medicinal Inhaler") [Medicinal Inhaler](/wiki/Medicinal_Inhaler "Medicinal Inhaler")  
130 | [](/wiki/Packaged_Water "Packaged Water") [Packaged Water](/wiki/Packaged_Water "Packaged Water")  
131 | [](/wiki/Aluminum_Ingot "Aluminum Ingot") [Aluminum Ingot](/wiki/Aluminum_Ingot "Aluminum Ingot")  
140 | [](/wiki/Fabric "Fabric") [Fabric](/wiki/Fabric "Fabric"), [](/wiki/Rotor "Rotor") [Rotor](/wiki/Rotor "Rotor")  
147 | [](/wiki/Encased_Uranium_Cell "Encased Uranium Cell") [Encased Uranium Cell](/wiki/Encased_Uranium_Cell "Encased Uranium Cell")  
152 | [](/wiki/Nobelisk "Nobelisk") [Nobelisk](/wiki/Nobelisk "Nobelisk"), [](/wiki/Packaged_Sulfuric_Acid "Packaged Sulfuric Acid") [Packaged Sulfuric Acid](/wiki/Packaged_Sulfuric_Acid "Packaged Sulfuric Acid")  
160 | [](/wiki/Packaged_Alumina_Solution "Packaged Alumina Solution") [Packaged Alumina Solution](/wiki/Packaged_Alumina_Solution "Packaged Alumina Solution"), [](/wiki/Reanimated_SAM "Reanimated SAM") [Reanimated SAM](/wiki/Reanimated_SAM "Reanimated SAM")  
170 | [](/wiki/Empty_Fluid_Tank "Empty Fluid Tank") [Empty Fluid Tank](/wiki/Empty_Fluid_Tank "Empty Fluid Tank")  
180 | [](/wiki/Packaged_Heavy_Oil_Residue "Packaged Heavy Oil Residue") [Packaged Heavy Oil Residue](/wiki/Packaged_Heavy_Oil_Residue "Packaged Heavy Oil Residue"), [](/wiki/Packaged_Oil "Packaged Oil") [Packaged Oil](/wiki/Packaged_Oil "Packaged Oil")  
186 | [](/wiki/Stun_Rebar "Stun Rebar") [Stun Rebar](/wiki/Stun_Rebar "Stun Rebar")  
210 | [](/wiki/Alien_Power_Matrix "Alien Power Matrix") [Alien Power Matrix](/wiki/Alien_Power_Matrix "Alien Power Matrix")  
240 | [](/wiki/Diamonds "Diamonds") [Diamonds](/wiki/Diamonds "Diamonds"), [](/wiki/Stator "Stator") [Stator](/wiki/Stator "Stator")  
266 | [](/wiki/Alclad_Aluminum_Sheet "Alclad Aluminum Sheet") [Alclad Aluminum Sheet](/wiki/Alclad_Aluminum_Sheet "Alclad Aluminum Sheet")  
270 | [](/wiki/Packaged_Fuel "Packaged Fuel") [Packaged Fuel](/wiki/Packaged_Fuel "Packaged Fuel")  
312 | [](/wiki/Packaged_Nitrogen_Gas "Packaged Nitrogen Gas") [Packaged Nitrogen Gas](/wiki/Packaged_Nitrogen_Gas "Packaged Nitrogen Gas")  
332 | [](/wiki/Shatter_Rebar "Shatter Rebar") [Shatter Rebar](/wiki/Shatter_Rebar "Shatter Rebar")  
360 | [](/wiki/Explosive_Rebar "Explosive Rebar") [Explosive Rebar](/wiki/Explosive_Rebar "Explosive Rebar")  
370 | [](/wiki/Packaged_Liquid_Biofuel "Packaged Liquid Biofuel") [Packaged Liquid Biofuel](/wiki/Packaged_Liquid_Biofuel "Packaged Liquid Biofuel")  
393 | [](/wiki/Aluminum_Casing "Aluminum Casing") [Aluminum Casing](/wiki/Aluminum_Casing "Aluminum Casing")  
408 | [](/wiki/Modular_Frame "Modular Frame") [Modular Frame](/wiki/Modular_Frame "Modular Frame")  
412 | [](/wiki/Packaged_Nitric_Acid "Packaged Nitric Acid") [Packaged Nitric Acid](/wiki/Packaged_Nitric_Acid "Packaged Nitric Acid")  
465 | [](/wiki/Battery "Battery") [Battery](/wiki/Battery "Battery")  
520 | [](/wiki/Smart_Plating "Smart Plating") [Smart Plating](/wiki/Smart_Plating "Smart Plating")  
528 | [](/wiki/Encased_Industrial_Beam "Encased Industrial Beam") [Encased Industrial Beam](/wiki/Encased_Industrial_Beam "Encased Industrial Beam")  
544 | [](/wiki/Gas_Nobelisk "Gas Nobelisk") [Gas Nobelisk](/wiki/Gas_Nobelisk "Gas Nobelisk")  
570 | [](/wiki/Packaged_Turbofuel "Packaged Turbofuel") [Packaged Turbofuel](/wiki/Packaged_Turbofuel "Packaged Turbofuel")  
608 | [](/wiki/Gas_Filter "Gas Filter") [Gas Filter](/wiki/Gas_Filter "Gas Filter")  
630 | [](/wiki/FICSMAS_Wreath "FICSMAS Wreath") [FICSMAS Wreath](/wiki/FICSMAS_Wreath "FICSMAS Wreath")  
696 | [](/wiki/Circuit_Board "Circuit Board") [Circuit Board](/wiki/Circuit_Board "Circuit Board")  
855 | [](/wiki/Homing_Rifle_Ammo "Homing Rifle Ammo") [Homing Rifle Ammo](/wiki/Homing_Rifle_Ammo "Homing Rifle Ammo")  
920 | [](/wiki/AI_Limiter "AI Limiter") [AI Limiter](/wiki/AI_Limiter "AI Limiter")  
960 | [](/wiki/Time_Crystal "Time Crystal") [Time Crystal](/wiki/Time_Crystal "Time Crystal")  
1,028 | [](/wiki/Packaged_Rocket_Fuel "Packaged Rocket Fuel") [Packaged Rocket Fuel](/wiki/Packaged_Rocket_Fuel "Packaged Rocket Fuel")  
1,176 | [](/wiki/Versatile_Framework "Versatile Framework") [Versatile Framework](/wiki/Versatile_Framework "Versatile Framework")  
1,291 | [](/wiki/Ficsite_Trigon "Ficsite Trigon") [Ficsite Trigon](/wiki/Ficsite_Trigon "Ficsite Trigon")  
1,376 | [](/wiki/Cluster_Nobelisk "Cluster Nobelisk") [Cluster Nobelisk](/wiki/Cluster_Nobelisk "Cluster Nobelisk")  
1,400 | [](/wiki/Object_Scanner "Object Scanner") [Object Scanner](/wiki/Object_Scanner "Object Scanner")  
1,440 | [](/wiki/Automated_Wiring "Automated Wiring") [Automated Wiring](/wiki/Automated_Wiring "Automated Wiring")  
1,520 | [](/wiki/Motor "Motor") [Motor](/wiki/Motor "Motor")  
1,533 | [](/wiki/Pulse_Nobelisk "Pulse Nobelisk") [Pulse Nobelisk](/wiki/Pulse_Nobelisk "Pulse Nobelisk")  
1,552 | [](/wiki/Factory_Cart%E2%84%A2 "Factory Cart™") [Factory Cart™](/wiki/Factory_Cart%E2%84%A2 "Factory Cart™")  
1,780 | [](/wiki/Dark_Matter_Crystal "Dark Matter Crystal") [Dark Matter Crystal](/wiki/Dark_Matter_Crystal "Dark Matter Crystal")  
1,852 | [](/wiki/Golden_Factory_Cart%E2%84%A2 "Golden Factory Cart™") [Golden Factory Cart™](/wiki/Golden_Factory_Cart%E2%84%A2 "Golden Factory Cart™")  
1,880 | [](/wiki/Xeno-Zapper "Xeno-Zapper") [Xeno-Zapper](/wiki/Xeno-Zapper "Xeno-Zapper")  
1,936 | [](/wiki/Ficsite_Ingot "Ficsite Ingot") [Ficsite Ingot](/wiki/Ficsite_Ingot "Ficsite Ingot")  
1,968 | [](/wiki/Rebar_Gun "Rebar Gun") [Rebar Gun](/wiki/Rebar_Gun "Rebar Gun"), [](/wiki/SAM_Fluctuator "SAM Fluctuator") [SAM Fluctuator](/wiki/SAM_Fluctuator "SAM Fluctuator")  
2,274 | [](/wiki/Iodine-Infused_Filter "Iodine-Infused Filter") [Iodine-Infused Filter](/wiki/Iodine-Infused_Filter "Iodine-Infused Filter")  
2,560 | [](/wiki/Electromagnetic_Control_Rod "Electromagnetic Control Rod") [Electromagnetic Control Rod](/wiki/Electromagnetic_Control_Rod "Electromagnetic Control Rod")  
2,760 | [](/wiki/Chainsaw "Chainsaw") [Chainsaw](/wiki/Chainsaw "Chainsaw")  
2,804 | [](/wiki/Heat_Sink "Heat Sink") [Heat Sink](/wiki/Heat_Sink "Heat Sink")  
3,072 | [](/wiki/Crystal_Oscillator "Crystal Oscillator") [Crystal Oscillator](/wiki/Crystal_Oscillator "Crystal Oscillator")  
3,776 | [](/wiki/High-Speed_Connector "High-Speed Connector") [High-Speed Connector](/wiki/High-Speed_Connector "High-Speed Connector")  
4,088 | [](/wiki/Blade_Runners "Blade Runners") [Blade Runners](/wiki/Blade_Runners "Blade Runners")  
5,246 | [](/wiki/Packaged_Ionized_Fuel "Packaged Ionized Fuel") [Packaged Ionized Fuel](/wiki/Packaged_Ionized_Fuel "Packaged Ionized Fuel")  
5,284 | [](/wiki/Zipline "Zipline") [Zipline](/wiki/Zipline "Zipline")  
6,080 | [](/wiki/Parachute "Parachute") [Parachute](/wiki/Parachute "Parachute")  
6,480 | [](/wiki/Nobelisk_Detonator "Nobelisk Detonator") [Nobelisk Detonator](/wiki/Nobelisk_Detonator "Nobelisk Detonator")  
6,540 | [](/wiki/FICSMAS_Wonder_Star "FICSMAS Wonder Star") [FICSMAS Wonder Star](/wiki/FICSMAS_Wonder_Star "FICSMAS Wonder Star")  
7,850 | [](/wiki/Candy_Cane_Basher "Candy Cane Basher") [Candy Cane Basher](/wiki/Candy_Cane_Basher "Candy Cane Basher")  
8,352 | [](/wiki/Computer "Computer") [Computer](/wiki/Computer "Computer")  
9,480 | [](/wiki/Rifle "Rifle") [Rifle](/wiki/Rifle "Rifle")  
9,960 | [](/wiki/Modular_Engine "Modular Engine") [Modular Engine](/wiki/Modular_Engine "Modular Engine")  
10,800 | [](/wiki/Heavy_Modular_Frame "Heavy Modular Frame") [Heavy Modular Frame](/wiki/Heavy_Modular_Frame "Heavy Modular Frame")  
11,000 | [](/wiki/Magnetic_Field_Generator "Magnetic Field Generator") [Magnetic Field Generator](/wiki/Magnetic_Field_Generator "Magnetic Field Generator")  
12,006 | [](/wiki/Cooling_System "Cooling System") [Cooling System](/wiki/Cooling_System "Cooling System")  
14,960 | [](/wiki/Gas_Mask "Gas Mask") [Gas Mask](/wiki/Gas_Mask "Gas Mask")  
16,580 | [](/wiki/Jetpack "Jetpack") [Jetpack](/wiki/Jetpack "Jetpack")  
17,800 | [](/wiki/Xeno-Basher "Xeno-Basher") [Xeno-Basher](/wiki/Xeno-Basher "Xeno-Basher")  
19,600 | [](/wiki/Nuke_Nobelisk "Nuke Nobelisk") [Nuke Nobelisk](/wiki/Nuke_Nobelisk "Nuke Nobelisk")  
32,352 | [](/wiki/Radio_Control_Unit "Radio Control Unit") [Radio Control Unit](/wiki/Radio_Control_Unit "Radio Control Unit")  
37,292 | [](/wiki/Superposition_Oscillator "Superposition Oscillator") [Superposition Oscillator](/wiki/Superposition_Oscillator "Superposition Oscillator")  
43,468 | [](/wiki/Uranium_Fuel_Rod "Uranium Fuel Rod") [Uranium Fuel Rod](/wiki/Uranium_Fuel_Rod "Uranium Fuel Rod")  
54,100 | [](/wiki/Hazmat_Suit "Hazmat Suit") [Hazmat Suit](/wiki/Hazmat_Suit "Hazmat Suit")  
62,840 | [](/wiki/Fused_Modular_Frame "Fused Modular Frame") [Fused Modular Frame](/wiki/Fused_Modular_Frame "Fused Modular Frame")  
76,368 | [](/wiki/Adaptive_Control_Unit "Adaptive Control Unit") [Adaptive Control Unit](/wiki/Adaptive_Control_Unit "Adaptive Control Unit")  
97,352 | [](/wiki/Supercomputer "Supercomputer") [Supercomputer](/wiki/Supercomputer "Supercomputer")  
114,675 | [](/wiki/Singularity_Cell "Singularity Cell") [Singularity Cell](/wiki/Singularity_Cell "Singularity Cell")  
153,184 | [](/wiki/Plutonium_Fuel_Rod "Plutonium Fuel Rod") [Plutonium Fuel Rod](/wiki/Plutonium_Fuel_Rod "Plutonium Fuel Rod")  
240,496 | [](/wiki/Turbo_Motor "Turbo Motor") [Turbo Motor](/wiki/Turbo_Motor "Turbo Motor")  
248,034 | [](/wiki/Neural-Quantum_Processor "Neural-Quantum Processor") [Neural-Quantum Processor](/wiki/Neural-Quantum_Processor "Neural-Quantum Processor")  
255,088 | [](/wiki/Pressure_Conversion_Cube "Pressure Conversion Cube") [Pressure Conversion Cube](/wiki/Pressure_Conversion_Cube "Pressure Conversion Cube")  
265,632 | [](/wiki/Hoverpack "Hoverpack") [Hoverpack](/wiki/Hoverpack "Hoverpack")  
301,778 | [](/wiki/Biochemical_Sculptor "Biochemical Sculptor") [Biochemical Sculptor](/wiki/Biochemical_Sculptor "Biochemical Sculptor")  
500,176 | [](/wiki/Assembly_Director_System "Assembly Director System") [Assembly Director System](/wiki/Assembly_Director_System "Assembly Director System")  
538,976 | [](/wiki/Nuclear_Pasta "Nuclear Pasta") [Nuclear Pasta](/wiki/Nuclear_Pasta "Nuclear Pasta")  
597,652 | [](/wiki/AI_Expansion_Server "AI Expansion Server") [AI Expansion Server](/wiki/AI_Expansion_Server "AI Expansion Server")  
728,508 | [](/wiki/Thermal_Propulsion_Rocket "Thermal Propulsion Rocket") [Thermal Propulsion Rocket](/wiki/Thermal_Propulsion_Rocket "Thermal Propulsion Rocket")  
2,895,334 | [](/wiki/Ballistic_Warp_Drive "Ballistic Warp Drive") [Ballistic Warp Drive](/wiki/Ballistic_Warp_Drive "Ballistic Warp Drive")  
  
_This table is compiled via[Module:AwesomeSinkPoints](/wiki/Module:AwesomeSinkPoints "Module:AwesomeSinkPoints")._

The first time a FICSIT Coupon is inserted, the [Cyber Wagon](/wiki/Cyber_Wagon "Cyber Wagon") is made available for purchase in the AWESOME Shop, and the point is not awarded. The first (and only possible) time an ['Employee of the Planet' Cup](/wiki/%27Employee_of_the_Planet%27_Cup "'Employee of the Planet' Cup") is inserted, the [Golden Factory Cart](/wiki/Golden_Factory_Cart "Golden Factory Cart") is made available for purchase in the AWESOME Shop. 

  
Items listed as "cannot be sunk" will clog the input. 

Alien DNA Capsules have a separate point counter, see § Coupon cost from Alien DNA Capsule

## Recipe point improvement ratios

As mentioned earlier, recipes usually yield more points than their ingredients. However, the point increase when using alternate recipes varies widely; the output from most recipes is worth between 1.5 and 2.5 times as many points as the combined input, but exceptions exist in both directions (as alts use either cheaper or more expensive ingredients, which affects how effective using the alt is point-wise). 

Eight alternate recipes actually provide less points than all of their ingredients combined: [Compacted Steel Ingot](/wiki/Steel_Ingot "Steel Ingot"), [Coke Steel Ingot](/wiki/Steel_Ingot "Steel Ingot"), [Rubber Concrete](/wiki/Concrete "Concrete"), [Steel Coated Plate](/wiki/Iron_Plate "Iron Plate"), [Coated Iron Plate](/wiki/Iron_Plate "Iron Plate"), [Caterium Wire](/wiki/Wire "Wire"), [Plutonium Fuel Unit](/wiki/Plutonium_Fuel_Rod "Plutonium Fuel Rod") and [Automated Miner](/wiki/Miner#Portable_Miner "Miner"). 

Note: In the case of Plutonium Fuel Unit not all the components can be sunk, but the sink value of the [Pressure Conversion Cube](/wiki/Pressure_Conversion_Cube "Pressure Conversion Cube") exceeds that of the Plutonium Fuel Rod. 

The most "profitable" recipe as of [Patch 0.3.3.0](/wiki/Patch_0.3.3.0 "Patch 0.3.3.0") is [Silicon Circuit Board](/wiki/Circuit_Board "Circuit Board"), which generates items worth 7.19 as many points as the input items. Meanwhile, the [Alien Power Matrix](/wiki/Alien_Power_Matrix "Alien Power Matrix") is one of (?) the least profitable items, generating items worth 0.0017 as many points as its input items. 

## Tips

  * Other than farming points for [Coupons](/wiki/Coupon "Coupon"), the AWESOME Sink is very useful to get rid of solid by-products, which is quite useful for any setup involving [Refineries](/wiki/Refineries "Refineries"). Connect a [Smart Splitter](/wiki/Smart_Splitter "Smart Splitter") with an Overflow setting, with the Sink connected to the overflow output. An AWESOME Sink is also useful for forcing the factory to run 100% of the time as the output item will never have a chance to back up, with the cost of increased [power](/wiki/Power "Power") demand. 
    * _Further reading:[Smart Splitter](/wiki/Smart_Splitter "Smart Splitter")_
  * The AWESOME Sink does not consume power if it is not doing any work, much like other buildings.



### Farming points

Some items can be used to effectively get lots of points for comparatively little effort: 

  * [Concrete](/wiki/Concrete "Concrete"): Only requires one step to manufacture from [limestone](/wiki/Limestone "Limestone"), but generates decent points for low energy costs.
  * [Cables](/wiki/Cable "Cable"): Can be automated almost immediately and generate a decent amount of points for early game.
  * [Raw Quartz](/wiki/Raw_Quartz "Raw Quartz"): If a Resource Node is found early, lots of points can be generated with minimal effort. 
    * Converting them to [Quartz Crystals](/wiki/Quartz_Crystal "Quartz Crystal") once possible doubles point yield.
    * Converting them to [Silica](/wiki/Silica "Silica") more than doubles point yield.
  * [Uranium](/wiki/Uranium "Uranium"): If the player is willing to accept risk of death from enemies as well as radiation, the Uranium ore itself can be sunk at any stage in the game for a lot of points due to its high base value and lack of a need to process it.
  * [SAM](/wiki/SAM "SAM") and [Reanimated SAM](/wiki/Reanimated_SAM "Reanimated SAM"): These are easy to automate if a resource node is located, and are not needed in large quantities until the late game.
  * [Object Scanner](/wiki/Object_Scanner "Object Scanner"), [Blade Runners](/wiki/Blade_Runners "Blade Runners"), and [Xeno-Basher](/wiki/Xeno-Basher "Xeno-Basher") give a lot of points early on, but can't be automated.
  * [Quickwire](/wiki/Quickwire "Quickwire"): Given how much can be manufactured from a single Caterium node, sinking surplus can be effective.
  * [AI Limiter](/wiki/AI_Limiter "AI Limiter"): Similar to Quickwire, but considerably more effective.
  * [Alien DNA Capsule](/wiki/Alien_DNA_Capsule "Alien DNA Capsule"): If you use a [Somersloop](/wiki/Somersloop "Somersloop") for both steps of processing, it would take near 35 full containers of [Alien Remains](/wiki/Alien_Remains "Alien Remains") to afford the 1,000 tickets for [Golden Nut](/wiki/Golden_Nut "Golden Nut") for the Achievement. But your first container of remains will net you 168 tickets.
  * Excess Space Elevator parts: Have no use if not demanded by the [Space Elevator](/wiki/Space_Elevator "Space Elevator").
  * Items scattered around [Crash Sites](/wiki/Crash_Site "Crash Site"): Some crash sites have high-point items such as [Turbo Motors](/wiki/Turbo_Motor "Turbo Motor") or [Heavy Modular Frames](/wiki/Heavy_Modular_Frame "Heavy Modular Frame") scattered around them. If these are collected and sunk, they can give many tickets in the early game.
  * The absolute best items to sink are: 
    * [Ballistic Warp Drive](/wiki/Ballistic_Warp_Drive "Ballistic Warp Drive"): Being the most expensive item, it benefits greatly from [Somersloop](/wiki/Somersloop "Somersloop") boosting.
    * [AI Expansion Server](/wiki/AI_Expansion_Server "AI Expansion Server"): The most resource-efficient item. After you run out of Somersloops, this becomes the most efficient item to sink.
    * [Assembly Director System](/wiki/Assembly_Director_System "Assembly Director System"): The first two items require SAM and you deplete SAM before other resources. This becomes the best item to sink after that, and it was the best item to sink in update 8 and before


  * The maximum amount of points per minute that can be generated in 1.0 while using all available resources and energy is 
    * 511,613,703 if underclocking almost all buildings to 1% (except miners, power production, and [Somersloop](/wiki/Somersloop "Somersloop")-boosted buildings)
    * 480,345,879 if using default clock speed for most of the buildings
    * 463,281,456 if boosting all buildings to 250%
  * This requires some combinations of Ballistic Warp Drive,s AI Expansion Servers, Assembly Director Systems and [Plutonium Fuel Rods](/wiki/Plutonium_Fuel_Rod "Plutonium Fuel Rod"). More information can be found here: [/Theoretical maximum of points](/wiki/AWESOME_Sink/Theoretical_maximum_of_points "AWESOME Sink/Theoretical maximum of points")



## Achievements

[](/wiki/Achievements "Achievements")**[Now where to spend it...](/wiki/Achievements#Now_where_to_spend_it... "Achievements")** •  _"Print out your first Coupon."_

## Trivia

  * The maximum amount of points per minute the chart will display is 2,147,483,648, the signed 32-bit integer limit plus one. This is only a visual limit. Since points come in on a per item basis and not all at once it will not affect the actual amount of points the player gets.[1]
  * An early concept for the Sink had considered using the [Space Elevator](/wiki/Space_Elevator "Space Elevator") for sinking items, but this was discarded due to concerns about getting all the resources to one central location.[2]
  * It takes about 2.31  [MJ](/wiki/MJ "MJ") to sink a single item, assuming a Mk.5 [Conveyor Belt](/wiki/Belt "Belt") is used and it is saturated with items. 
    * For lower tier belts (from Mk.1 to Mk.4), the energy spent for sinking is 3.75 MJ, 6.67 MJ, 15 MJ and 30 MJ respectively. Thus, it is least efficient to sink items with Mk.1 belts.
  * For the Sink to run constantly there should be no gap of items in the input larger than 1/30 the speed of the belt feeding the Sink. 
    * For a Mk.1 belt, that's a gap of 2 items; the lowest evenly spaced rate that does this is 20 items per minute.



## See also

  * [](/wiki/FICSIT_Coupon "FICSIT Coupon") [FICSIT Coupon](/wiki/FICSIT_Coupon "FICSIT Coupon")
  * [](/wiki/AWESOME_Shop "AWESOME Shop") [AWESOME Shop](/wiki/AWESOME_Shop "AWESOME Shop")
  * [](/wiki/Smart_Splitter "Smart Splitter") [Smart Splitter](/wiki/Smart_Splitter "Smart Splitter")



## Gallery

  * [](/wiki/File:Priority_Splitter_Packaged_Fuel.png "Using AWESOME Sink to remove excess Packaged Fuel to prevent Refineries from clogging up.")

Using AWESOME Sink to remove excess [Packaged Fuel](/wiki/Packaged_Fuel "Packaged Fuel") to prevent [Refineries](/wiki/Refineries "Refineries") from clogging up.

  * [](/wiki/File:Max_Points_Per_Minute.jpg "Maximum amount of points per minute.")

Maximum amount of points per minute.




## History

  * [Patch 1.0](/wiki/Patch_1.0 "Patch 1.0"): Point values for some items were changed and re-balanced
  * [Patch 0.7.0.1](/wiki/Patch_0.7.0.1 "Patch 0.7.0.1"): Fixed a crash for Clients when placing a Blueprint that has the AWESOME Sink
  * [Patch 0.7.0.0](/wiki/Patch_0.7.0.0 "Patch 0.7.0.0"): Added a separate point counter for [Alien DNA Capsules](/wiki/Alien_DNA_Capsule "Alien DNA Capsule")
  * [Patch 0.7.0.6](/wiki/Patch_0.7.0.6 "Patch 0.7.0.6"): Fixed the Print Coupon button flickering briefly when opening the AWESOME Sink
  * [Patch 0.6.0.3](/wiki/Patch_0.6.0.3 "Patch 0.6.0.3"): Recalculated AWESOME Sink point values and made the new parts sinkable
  * [Patch 0.5.1.7](/wiki/Patch_0.5.1.7 "Patch 0.5.1.7"): Fixed bug where right clicking coupons while picking them up from the AWESOME Sink would result in losing half of them
  * [Patch 0.5.0.2](/wiki/Patch_0.5.0.2 "Patch 0.5.0.2") _(Released again in[Patch 0.5.0.3](/wiki/Patch_0.5.0.3 "Patch 0.5.0.3"))_: Fixed some shader bugs in the AWESOME Sink UI
  * [Patch 0.4.0.0](/wiki/Patch_0.4.0.0 "Patch 0.4.0.0"): Points for Tier 7 and 8 items were rebalanced
  * [Patch 0.3.7.7](/wiki/Patch_0.3.7.7 "Patch 0.3.7.7"): [FICSMAS](/wiki/FICSMAS "FICSMAS") items can now be sunk for 1 point each
  * [Patch 0.3.4.14](/wiki/Patch_0.3.4.14 "Patch 0.3.4.14"): Now capable of processing more than 600 items per minute
  * [Patch 0.3.3.0](/wiki/Patch_0.3.3.0#Balancing "Patch 0.3.3.0"): Point values for all items were changed and re-balanced, generally reducing the amount of generated points. Most Equipment items gained point values.
  * [Patch 0.3](/wiki/Patch_0.3#New_content "Patch 0.3"): Introduced

Points generated per item prior to Patch 0.3.3.0   
---  
Points | Items   
1 | [Coupon](/wiki/Coupon "Coupon")  
1 | [Copper Ore](/wiki/Copper_Ore "Copper Ore"), [Iron Ore](/wiki/Iron_Ore "Iron Ore"), [Bauxite](/wiki/Bauxite "Bauxite"), [Empty Canister](/wiki/Empty_Canister "Empty Canister"), [Packaged Turbofuel](/wiki/Packaged_Turbofuel "Packaged Turbofuel"), [Compacted Coal](/wiki/Compacted_Coal "Compacted Coal"), [Packaged Liquid Biofuel](/wiki/Packaged_Liquid_Biofuel "Packaged Liquid Biofuel")  
2 | [Limestone](/wiki/Limestone "Limestone"), [Coal](/wiki/Coal "Coal"), [Iron Ingot](/wiki/Iron_Ingot "Iron Ingot"), [Copper Ingot](/wiki/Copper_Ingot "Copper Ingot"), [Screw](/wiki/Screw "Screw"), [Wire](/wiki/Wire "Wire")  
3 | [Leaves](/wiki/Leaves "Leaves")  
4 | [Iron Rod](/wiki/Iron_Rod "Iron Rod")  
5 | [Caterium Ore](/wiki/Caterium_Ore "Caterium Ore")  
6 | [Iron Plate](/wiki/Iron_Plate "Iron Plate"), [Packaged Fuel](/wiki/Packaged_Fuel "Packaged Fuel")  
8 | [Cable](/wiki/Cable "Cable"), [Copper Sheet](/wiki/Copper_Sheet "Copper Sheet"), [Spiked Rebar](/wiki/Spiked_Rebar "Spiked Rebar")  
9 | [Steel Ingot](/wiki/Steel_Ingot "Steel Ingot")  
10  | [Flower Petals](/wiki/Flower_Petals "Flower Petals"), [Biomass](/wiki/Biomass "Biomass"), [Color Cartridge](/wiki/Color_Cartridge "Color Cartridge")  
12  | [Silica](/wiki/Silica "Silica"), [Concrete](/wiki/Concrete "Concrete"), [Quickwire](/wiki/Quickwire "Quickwire")  
15  | [Raw Quartz](/wiki/Raw_Quartz "Raw Quartz"), [Mycelia](/wiki/Mycelia "Mycelia")  
18  | [Packaged Oil](/wiki/Packaged_Oil "Packaged Oil")  
20  | [Sulfur](/wiki/Sulfur "Sulfur"), [Packaged Water](/wiki/Packaged_Water "Packaged Water")  
21  | [Aluminum Scrap](/wiki/Aluminum_Scrap "Aluminum Scrap")  
25  | [Wood](/wiki/Wood "Wood")  
27  | [Steel Pipe](/wiki/Steel_Pipe "Steel Pipe")  
30  | [Petroleum Coke](/wiki/Petroleum_Coke "Petroleum Coke"), [Caterium Ingot](/wiki/Caterium_Ingot "Caterium Ingot")  
40  | [Solid Biofuel](/wiki/Solid_Biofuel "Solid Biofuel")  
50 | [Uranium](/wiki/Uranium "Uranium"), [Quartz Crystal](/wiki/Quartz_Crystal "Quartz Crystal"), [Polymer Resin](/wiki/Polymer_Resin "Polymer Resin")  
72  | [Steel Beam](/wiki/Steel_Beam "Steel Beam")  
93  | [Packaged Heavy Oil Residue](/wiki/Packaged_Heavy_Oil_Residue "Packaged Heavy Oil Residue")  
111  | [Uranium Pellet](/wiki/Uranium_Pellet "Uranium Pellet")  
126  | [Black Powder](/wiki/Black_Powder "Black Powder")  
143  | [Rubber](/wiki/Rubber "Rubber")  
160  | [Plastic](/wiki/Plastic "Plastic")  
180  | [Reinforced Iron Plate](/wiki/Reinforced_Iron_Plate "Reinforced Iron Plate")  
195  | [Fabric](/wiki/Fabric "Fabric")  
200  | [Medicinal Inhaler](/wiki/Medicinal_Inhaler "Medicinal Inhaler")  
210  | [Rotor](/wiki/Rotor "Rotor")  
252  | [Aluminum Ingot](/wiki/Aluminum_Ingot "Aluminum Ingot")  
291  | [Stator](/wiki/Stator "Stator")  
340  | [Beacon](/wiki/Beacon "Beacon")  
840  | [AI Limiter](/wiki/AI_Limiter "AI Limiter")  
882  | [Modular Frame](/wiki/Modular_Frame "Modular Frame")  
1 044  | [Encased Industrial Beam](/wiki/Encased_Industrial_Beam "Encased Industrial Beam")  
1 170  | [Smart Plating](/wiki/Smart_Plating "Smart Plating")  
1 194  | [Parachute](/wiki/Parachute "Parachute")  
1 353  | [Automated Wiring](/wiki/Automated_Wiring "Automated Wiring")  
1 364  | [Encased Uranium Cell](/wiki/Encased_Uranium_Cell "Encased Uranium Cell")  
1 517  | [Alclad Aluminum Sheet](/wiki/Alclad_Aluminum_Sheet "Alclad Aluminum Sheet")  
1 968  | [Circuit Board](/wiki/Circuit_Board "Circuit Board")  
2 619  | [Versatile Framework](/wiki/Versatile_Framework "Versatile Framework")  
2 744  | [Filter](/wiki/Filter "Filter")  
3 006  | [Motor](/wiki/Motor "Motor")  
3 336  | [Cartridge](/wiki/Cartridge "Cartridge")  
3 830  | [Electromagnetic Control Rod](/wiki/Electromagnetic_Control_Rod "Electromagnetic Control Rod")  
5 848  | [Crystal Oscillator](/wiki/Crystal_Oscillator "Crystal Oscillator")  
10 880  | [High-Speed Connector](/wiki/High-Speed_Connector "High-Speed Connector")  
12 504  | [Iodine Infused Filter](/wiki/Iodine_Infused_Filter "Iodine Infused Filter")  
21 207  | [Heat Sink](/wiki/Heat_Sink "Heat Sink")  
23 080  | [Battery](/wiki/Battery "Battery")  
41 988  | [Modular Engine](/wiki/Modular_Engine "Modular Engine")  
51 175  | [Heavy Modular Frame](/wiki/Heavy_Modular_Frame "Heavy Modular Frame")  
113 680  | [Computer](/wiki/Computer "Computer")  
225 528  | [Uranium Fuel Rod](/wiki/Uranium_Fuel_Rod "Uranium Fuel Rod")  
924 213  | [Adaptive Control Unit](/wiki/Adaptive_Control_Unit "Adaptive Control Unit")  
1 033 220  | [Radio Control Unit](/wiki/Radio_Control_Unit "Radio Control Unit")  
1 330 800  | [Supercomputer](/wiki/Supercomputer "Supercomputer")  
10 833 620  | [Turbo Motor](/wiki/Turbo_Motor "Turbo Motor")  
  
## References

  1. ↑ [Twitch Clip of Dev Stream - Max Points Per Minute is Visual Only](https://clips.twitch.tv/RespectfulPolishedCormorantDerp-fr1PFfrwQl1yHtX7)
  2. ↑ [YouTube - June 8th, 2020 Livestream - Q&A: How about repeatable Space Elevator shipments to make more use of it?](https://youtu.be/fbCEIVUNDe0)



  * [v](/wiki/Template:BuildingNav "Template:BuildingNav")
  * [e](https://satisfactory.wiki.gg/wiki/Template:BuildingNav?action=edit)
  * [h](https://satisfactory.wiki.gg/wiki/Template:BuildingNav?action=history)

[Buildings](/wiki/Buildings "Buildings")  
---  
Special| [](/wiki/The_HUB "The HUB") [The HUB](/wiki/The_HUB "The HUB") • [](/wiki/MAM "MAM") [MAM](/wiki/MAM "MAM") • [](/wiki/Space_Elevator "Space Elevator") [Space Elevator](/wiki/Space_Elevator "Space Elevator") • [](/wiki/AWESOME_Sink "AWESOME Sink") AWESOME Sink • [](/wiki/AWESOME_Shop "AWESOME Shop") [AWESOME Shop](/wiki/AWESOME_Shop "AWESOME Shop") • [](/wiki/Blueprint_Designer "Blueprint Designer") [Blueprint Designer](/wiki/Blueprint_Designer "Blueprint Designer") • [](/wiki/Crafting_Bench "Crafting Bench") [Crafting Bench](/wiki/Crafting_Bench "Crafting Bench") • [](/wiki/Equipment_Workshop "Equipment Workshop") [Equipment Workshop](/wiki/Equipment_Workshop "Equipment Workshop")  
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
[Railway Transport](/wiki/Trains "Trains")| [](/wiki/Electric_Locomotive "Electric Locomotive") [Electric Locomotive](/wiki/Electric_Locomotive "Electric Locomotive") • [](/wiki/Freight_Car "Freight Car") [Freight Car](/wiki/Freight_Car "Freight Car") • [](/wiki/Train_Station "Train Station") [Train Station](/wiki/Train_Station "Train Station") • [](/wiki/Freight_Platform "Freight Platform") [Freight Platform](/wiki/Freight_Platform "Freight Platform") ([Fluid](/wiki/Freight_Platform#Fluid "Freight Platform")) • [](/wiki/Empty_Platform "Empty Platform") [Empty Platform](/wiki/Empty_Platform "Empty Platform") ([With Catwalk](/wiki/Empty_Platform_With_Catwalk "Empty Platform With Catwalk")) • [](/wiki/Railway "Railway") [Railway](/wiki/Railway "Railway") ([Railroad Switch Control](/wiki/Railroad_Switch_Control "Railroad Switch Control")) • [](/wiki/Buffer_Stop "Buffer Stop") [Buffer Stop](/wiki/Buffer_Stop "Buffer Stop") • [Train Signals](/wiki/Train_Signals "Train Signals") ([](/wiki/Train_Signals#Block "Train Signals") [Block](/wiki/Train_Signals#Block "Train Signals") • [](/wiki/Train_Signals#Path "Train Signals") [Path](/wiki/Train_Signals#Path "Train Signals"))  
Hypertubes| [](/wiki/Hypertube "Hypertube") [Hypertube](/wiki/Hypertube "Hypertube") • [](/wiki/Hypertube_Entrance "Hypertube Entrance") [Hypertube Entrance](/wiki/Hypertube_Entrance "Hypertube Entrance") • [](/wiki/Hypertube_Supports "Hypertube Supports") [Hypertube Supports](/wiki/Hypertube_Supports "Hypertube Supports") ([Stackable](/wiki/Hypertube_Supports#Stackable "Hypertube Supports"), [Wall Support](/wiki/Hypertube_Supports#Wall "Hypertube Supports"), [Wall Hole](/wiki/Hypertube_Supports#Hole "Hypertube Supports"), [Floor Hole](/wiki/Hypertube_Supports#Floor "Hypertube Supports")) • [](/wiki/Hypertube_Junction "Hypertube Junction") [Hypertube Junction](/wiki/Hypertube_Junction "Hypertube Junction") ([Branch](/wiki/Hypertube_Branch "Hypertube Branch"))  
Pioneer Transport| [](/wiki/Jump_Pad "Jump Pad") [Jump Pad](/wiki/Jump_Pad "Jump Pad") • [](/wiki/U-Jelly_Landing_Pad "U-Jelly Landing Pad") [U-Jelly Landing Pad](/wiki/U-Jelly_Landing_Pad "U-Jelly Landing Pad") • [](/wiki/Personnel_Elevator "Personnel Elevator") [Personnel Elevator](/wiki/Personnel_Elevator "Personnel Elevator") • [](/wiki/Portal "Portal") [Portal](/wiki/Portal "Portal") ([Main](/wiki/Main_Portal "Main Portal"), [Satellite](/wiki/Satellite_Portal "Satellite Portal"))  
  
Organization| [](/wiki/Lights "Lights") [Lights](/wiki/Lights "Lights") • [](/wiki/Signs "Signs") [Signs](/wiki/Signs "Signs") • [](/wiki/Crate "Crate") [Crate](/wiki/Crate "Crate") • [](/wiki/Personal_Storage_Box "Personal Storage Box") [Personal Storage Box](/wiki/Personal_Storage_Box "Personal Storage Box") ([Medical](/wiki/Personal_Storage_Box#Medical "Personal Storage Box"), [Hazard](/wiki/Personal_Storage_Box#Hazard "Personal Storage Box")) • [](/wiki/Basic_Shelf_Unit "Basic Shelf Unit") [Basic Shelf Unit](/wiki/Basic_Shelf_Unit "Basic Shelf Unit") • [](/wiki/Storage_Container "Storage Container") [Storage Container](/wiki/Storage_Container "Storage Container") ([Industrial](/wiki/Storage_Container#Industrial "Storage Container")) • [](/wiki/Dimensional_Depot_Uploader "Dimensional Depot Uploader") [Dimensional Depot Uploader](/wiki/Dimensional_Depot_Uploader "Dimensional Depot Uploader") • [](/wiki/Fluid_Buffer "Fluid Buffer") [Fluid Buffer](/wiki/Fluid_Buffer "Fluid Buffer") ([Industrial](/wiki/Fluid_Buffer#Industrial "Fluid Buffer")) • [](/wiki/Lookout_Tower "Lookout Tower") [Lookout Tower](/wiki/Lookout_Tower "Lookout Tower") • [](/wiki/Radar_Tower "Radar Tower") [Radar Tower](/wiki/Radar_Tower "Radar Tower")  
Foundations| [](/wiki/Foundations#Foundations "Foundations") [Foundations](/wiki/Foundations#Foundations "Foundations") • [](/wiki/Foundations#Ramps "Foundations") [Ramps](/wiki/Foundations#Ramps "Foundations") • [](/wiki/Foundations#Inverted_Ramps "Foundations") [Inverted Ramps](/wiki/Foundations#Inverted_Ramps "Foundations") • [](/wiki/Foundations#Quarter-Pipes "Foundations") [Quarter-Pipes](/wiki/Foundations#Quarter-Pipes "Foundations") • [](/wiki/Foundations#Half_Foundations "Foundations") [Half Foundations](/wiki/Foundations#Half_Foundations "Foundations")  
Walls| [](/wiki/Walls#Basic "Walls") [Basic Walls](/wiki/Walls#Basic "Walls") • [](/wiki/Walls#Ramp "Walls") [Ramp Walls](/wiki/Walls#Ramp "Walls") • [](/wiki/Walls#Inverted_Ramp "Walls") [Inverted Ramp Walls](/wiki/Walls#Inverted_Ramp "Walls") • [](/wiki/Walls#Tilted "Walls") [Tilted Walls](/wiki/Walls#Tilted "Walls") • [](/wiki/Walls#Windows "Walls") [Windows](/wiki/Walls#Windows "Walls") • [](/wiki/Walls#Doors "Walls") [Doors](/wiki/Walls#Doors "Walls") • [](/wiki/Walls#Conveyor "Walls") [Conveyor Walls](/wiki/Walls#Conveyor "Walls")  
Architecture| [](/wiki/Frame_Structures "Frame Structures") [Frames](/wiki/Frame_Structures "Frame Structures") • [](/wiki/Roofs "Roofs") [Roofs](/wiki/Roofs "Roofs") • [](/wiki/Beams "Beams") [Beams](/wiki/Beams "Beams") • [](/wiki/Pillars "Pillars") [Pillars](/wiki/Pillars "Pillars") • [](/wiki/Walkways "Walkways") [Walkways](/wiki/Walkways "Walkways") • [](/wiki/Walls "Walls") [Railings](/wiki/Walls "Walls") • [](/wiki/Foundations#Stairs "Foundations") [Stairs](/wiki/Foundations#Stairs "Foundations") • [](/wiki/Ladder "Ladder") [Ladder](/wiki/Ladder "Ladder") • [](/wiki/Large_Fan "Large Fan") [Large Fan](/wiki/Large_Fan "Large Fan") ([Vent](/wiki/Large_Vent "Large Vent"))
  *[v]: View this template
  *[e]: Edit this template
  *[h]: History of this template
