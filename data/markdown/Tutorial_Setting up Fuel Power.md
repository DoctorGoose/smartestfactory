# Tutorial:Setting up Fuel Power

_Main article:_[Fuel Generator](/wiki/Fuel_Generator "Fuel Generator")

This page serves to go more in depth on the creation and use of [Fuel](/wiki/Fuel "Fuel") as a power source. 

## Contents

  * 1 Overview
    * 1.1 Stage 1 - Fuel
    * 1.2 Stage 2 - Turbofuel
    * 1.3 Diluted Packaged Fuel vs Diluted Fuel
    * 1.4 Stage 3 - Diluted Fuel
    * 1.5 Stage 4 - Turbo Heavy Fuel
    * 1.6 Stage 5 - Turbo Heavy Fuel & Diluted Fuel
    * 1.7 Stage 6 - Turbo Blend Fuel
    * 1.8 Stage 7 - Rocket Fuel



## Overview

Fuel Power is unlocked at [Tier 6](/wiki/Milestones "Milestones") \- Logistics Mk.4 

  * Once unlocked, you can begin to follow the following stages.



The first stage uses the base Fuel recipe, with no alternates 

  * The following stages use [Turbofuel](/wiki/Turbofuel "Turbofuel"), which can only be acquired through researching [Hard Drives](/wiki/Hard_Drive "Hard Drive"), and unlocking the Turbofuel and [Compacted Coal](/wiki/Compacted_Coal "Compacted Coal") Recipes to start. 
    * Later, more complicated alternate recipes will also need to be unlocked.



### Stage 1 - Fuel

**Note: Always keep in mind the Pipeline throughput limit, 300 m 3/min for Mk.1 and 600 m3/min for Mk.2**

  1. Acquire 300 m3/min of [Crude Oil](/wiki/Crude_Oil "Crude Oil") (which is two impure Oil Extractors at 250%, one normal at 250% or one pure at 125%).
  2. Split the output of the Extractor and feed it to 5 Refineries, creating 200 fuel.
  3. Merge the fluid output of all the Refineries into a single Pipe, then split it to feed 10 Fuel Generators; which can be done with ten at 100% clock speed. See [ Clock Speed For Power Generators](/wiki/Tutorial:Advanced_clock_speed#Clock_speed_for_power_generators "Tutorial:Advanced clock speed") for more details.
  4. A manifold arrangement (aka. in-line splitting and merging) is advised for the above setup.
  5. To deal with the [Polymer Resin](/wiki/Polymer_Resin "Polymer Resin") (this setup will produce 150/min), either sink it or refine it into Residual Rubber/Plastic. Ensure these byproducts never back up, or Fuel production will stop, which will eventually result in the generators running out of it and stopping.



This setup provides **2 500 MW** of sustained power while using **150 MW.**

### Stage 2 - Turbofuel

  1. Unlock the "Compacted Coal" and "Turbofuel" recipes in the [MAM Sulfur Research chain](/wiki/Sulfur_Research "Sulfur Research"). Each unlock requires a single [Hard Drive](/wiki/Hard_Drive "Hard Drive").
  2. Mine 133.33 [Coal](/wiki/Coal "Coal") and [Sulfur](/wiki/Sulfur "Sulfur")/min and process it into Compacted Coal using 5.33 Assemblers.
  3. From the output of 5 Refineries creating Fuel at maximum production, combine it with the Compacted Coal to make 166.67 m3 Turbofuel/min by using 8.89 Refineries.
  4. Split the Turbofuel into 22.22 Fuel Generators (7.5m3/min).



This setup provides **5 555 MW** of sustained power. The total power consumption of all necessary buildings for the Turbofuel production is about **494.2 MW.**

### Diluted Packaged Fuel vs Diluted Fuel

If at any of the following stages you unlock [Blenders](/wiki/Blender "Blender") and the alternate "Diluted Fuel", use that recipe instead of "Diluted Packaged Fuel". It requires and gives the same amount of resources but skips the complicated packaging and unpackaging steps. It also takes less space and power. 

### Stage 3 - Diluted Fuel

    1\. Unlock the "Heavy Oil Residue" and either "Diluted Packaged Fuel" or "Diluted Fuel" alternate recipes.
    2\. Acquire 300 m3/min of Crude Oil
    3\. Use **10 Refineries** to process Crude Oil into [Heavy Oil Residue](/wiki/Heavy_Oil_Residue "Heavy Oil Residue") (400 m3/min) and sink or process the Polymer Resin byproduct (200/min)
    4\. Use **6.67[Water Extractors](/wiki/Water_Extractor "Water Extractor")** to get **800 m 3/min of Water**.
    5\. If using **"Diluted Fuel"** : 

    a. Use **8[Blenders](/wiki/Blender "Blender")** to process the Water and Heavy Oil Residue into **800 m 3/min of Fuel**.
    b. Skip step 6 if using this method.
    6\. If using **"Diluted Packaged Fuel"** : 

    a. Package the Water (using [Empty Canisters](/wiki/Empty_Canister "Empty Canister"), which are recycled in step 6d ) in **13.33 Packagers** to make [Packaged Water](/wiki/Packaged_Water "Packaged Water") (800/min).
    b. Process the Packaged Water and Heavy Oil Residue in **13.33 Refineries** to make [Packaged Fuel](/wiki/Packaged_Fuel "Packaged Fuel") using the Diluted Packaged Fuel alternate recipe (800/min).
    c. Unpackage the Packaged Fuel in **13.33 Packagers** (800 m3/min).
    d. Recycle the Empty Canisters to package the Water (in step 6a).
    7\. Distribute the Fuel to **40 Fuel Generators** (1 Fuel Generator consumes 20 m3/min of Fuel).

This setup provides **10 000 MW** of sustained power. The total power consumption of all necessary building for the Fuel production is **900 MW.**

### Stage 4 - Turbo Heavy Fuel

    1\. Unlock the "Compacted Coal", "Turbo Heavy Fuel", and "Heavy Oil Residue" alternate recipes.
    2\. Acquire 300 m3/min of Crude Oil.
    3\. Use **10 Refineries** to process Crude Oil into [Heavy Oil Residue](/wiki/Heavy_Oil_Residue "Heavy Oil Residue") (400 m3/min) and sink or process the Polymer Resin byproduct (200/min).
    4\. Mine **320[Coal](/wiki/Coal "Coal")/min** and **320[Sulfur](/wiki/Sulfur "Sulfur")/min**.
    5\. Use **12.8[Assemblers](/wiki/Assembler "Assembler")** to process Coal and Sulfur into **320[Compacted Coal](/wiki/Compacted_Coal "Compacted Coal")/min**.
    6\. Use **10.67 Refineries** to process Heavy Oil Residue and Compacted Coal into **[Turbofuel](/wiki/Turbofuel "Turbofuel") (320 m3/min)**.
    7\. Distribute the Turbofuel to **42.67 Fuel Generators** (1 Fuel Generator consumes 7.5 m3 of Turbofuel per minute).

This setup provides **10,666.67 MW** of sustained power. The total power consumption of all necessary buildings for Turbofuel production is **808.7 MW**. 

### Stage 5 - Turbo Heavy Fuel & Diluted Fuel

    1\. Unlock the "Heavy Oil Residue", "Diluted Packaged Fuel" or "Diluted Fuel", "Compacted Coal", and "Turbofuel" alternate recipes.
    2\. Acquire 300 m3/min of Crude Oil.
    3\. Use **10 Refineries** to process Crude Oil into [Heavy Oil Residue](/wiki/Heavy_Oil_Residue "Heavy Oil Residue") (400 m3/min) and sink or process the Polymer Resin byproduct (200/min).
    4\. Use **6.67[Water Extractors](/wiki/Water_Extractor "Water Extractor")** to get **800 m 3/min of Water**.
    5\. If using **"Diluted Fuel"** : 

    a. Use **8[Blenders](/wiki/Blender "Blender")** to process the Water and Heavy Oil Residue into **800 m 3/min of Fuel**.
    b. Skip step 6 if using this method.
    6\. If using **"Diluted Packaged Fuel"** : 

    a. Package the Water (using [Empty Canisters](/wiki/Empty_Canister "Empty Canister"), which are recycled in step 6d) in **13.33 Packagers** to make [Packaged Water](/wiki/Packaged_Water "Packaged Water") (800/min).
    b. Process the Packaged Water and Heavy Oil Residue in **13.33 Refineries** to make [Packaged Fuel](/wiki/Packaged_Fuel "Packaged Fuel") using the Diluted Packaged Fuel alternate recipe (800/min).
    c. Unpackage the Packaged Fuel in **13.33 Packagers** (800 m3/min).
    d. Recycle the Empty Canisters to package the Water (in step 6a).
    7\. Acquire **533.33[Compacted Coal](/wiki/Compacted_Coal "Compacted Coal")/min**. See substeps for acquisition 

    a. Mine **533.33[Coal](/wiki/Coal "Coal")/min** and **533.33[Sulfur](/wiki/Sulfur "Sulfur")/min**.
    b. Use **21.33[Assemblers](/wiki/Assembler "Assembler")** to process Coal and Sulfur into **533.33[Compacted Coal](/wiki/Compacted_Coal "Compacted Coal")/min**
    8\. Use **35.56 Refineries** to process Compacted Coal and Fuel into **[Turbofuel](/wiki/Turbofuel "Turbofuel") (666.67 m3/min)**.
    9\. Distribute the Turbofuel to **88.89 Fuel Generators** (1 Fuel Generator consumes 7.5 m3/min of Turbofuel).

This setup provides **22 222 MW** of sustained power. The total power consumption of all necessary buildings for Turbofuel production is **2 282.3 MW**. 

### Stage 6 - Turbo Blend Fuel

Optional late-game alternate to stage 5. Uses more oil in exchange for less sulfur usage and eliminates the need for coal. Which one is better will depend on your needs. 

    1\. Unlock the "Heavy Oil Residue", "Diluted Fuel", and "Turbo Blend Fuel" alternate recipes.
    2\. Acquire 500 m3/min of Crude Oil.
    3\. Use **16.67 Refineries** to process Crude Oil into [Heavy Oil Residue](/wiki/Heavy_Oil_Residue "Heavy Oil Residue") (666.8 m3/min) and process the [Polymer Resin](/wiki/Polymer_Resin "Polymer Resin") byproduct (333.33/min).
    4\. Use **1.86[Water Extractors](/wiki/Water_Extractor "Water Extractor")** to get **222.2 m 3/min of Water**.
    5\. Use **2.22[Blenders](/wiki/Blender "Blender")** to process the Water and 111.11 m3/min of Heavy Oil Residue into **222.2 m 3/min of Fuel**.
    6\. Use **2.78 Refineries** to process 111.11 m3/min of Heavy Oil Residue into **333.33/min Petroleum Coke**.
    7\. Mine **333.33[Sulfur](/wiki/Sulfur "Sulfur")/min**.
    8\. Use **14.81[Blenders](/wiki/Blender "Blender")** to process the remaining 444.4 m3/min of Heavy Oil Residue, the Fuel, Petroleum Coke, and Sulfur into **666.67 m 3/min of [Turbofuel](/wiki/Turbofuel "Turbofuel")** using the Turbo Blend Fuel alternate recipe.
    9\. Distribute the Turbofuel to **88.89 Fuel Generators** (1 Fuel Generator consumes 7.5 m3/min of Turbofuel).

This setup provides **22 222 MW** of sustained power. The total power consumption of all necessary buildings for Turbofuel production is **1 846.6 MW** , using 200 less sulfur and no coal, but 200 more oil compared to stage 5. 

### Stage 7 - Rocket Fuel

Optional late-game alternate to nuclear power, available earlier and provides enough power for most late game. Recommended to split production into 4 lines, 5 refineries into 4 blenders into 4 blenders. 

    1\. Unlock the "Heavy Oil Residue", "Diluted Fuel", and "Nitro Rocket Fuel" alternate recipes.
    2\. Acquire 600 m3/min of Crude Oil.
    3\. Use **20 Refineries** to process Crude Oil into [Heavy Oil Residue](/wiki/Heavy_Oil_Residue "Heavy Oil Residue") (800 m3/min) and process the [Polymer Resin](/wiki/Polymer_Resin "Polymer Resin") byproduct (400/min).
    4\. Use **13.333[Water Extractors](/wiki/Water_Extractor "Water Extractor")** to get **1600 m 3/min of Water**.
    5\. Use **16[Blenders](/wiki/Blender "Blender")** to process the Water and of Heavy Oil Residue into **1600 m 3/min of Fuel**.
    6\. Mine **1600[Sulfur](/wiki/Sulfur "Sulfur")/min**
    7\. Acquire **1200[Nitrogen Gas](/wiki/Nitrogen_Gas "Nitrogen Gas")/min**
    8\. Mine **800[Coal](/wiki/Coal "Coal")/min**
    9\. Use **16[Blenders](/wiki/Blender "Blender")** to process the Fuel, Sulfur, Nitrogen Gas and Coal into **2400 m 3/min of [Rocket Fuel](/wiki/Rocket_Fuel "Rocket Fuel")**. You will get 400 [Compacted Coal](/wiki/Compacted_Coal "Compacted Coal")/min, either sink it or use it in 56 [Coal-Powered Generators](/wiki/Coal-Powered_Generator "Coal-Powered Generator") with 2520 m3/min of Water to create **4 200 MW** of additional power.
    10\. Distribute the Rocket Fuel to **576 Fuel Generators** (1 Fuel Generator consumes 4.1667 m3/min of Rocket Fuel). Highly recommended to use Power Shards to reduce construction of Fuel Generators.

This setup provides **144 000 MW** of sustained power. The total power consumption of all necessary buildings for Rocket Fuel production is **3 000 MW** , This is easier to set up then nuclear power but tedious when it comes to power plant construction. 
  *[v]: View this template
  *[e]: Edit this template
  *[h]: History of this template
  *[his]: his trivia section
