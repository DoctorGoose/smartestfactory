# AWESOME Sink/Theoretical maximum of points

Since Satisfactory map has finite amount of resource nodes, the amount of maximum resources generated per minute is finite, and the amount of sink points generated per minute is finite too.   
  
Determining the amount of these resources generated is a linear optimization problem. And since the addition of somersloops, that also becomes an integer optimization problem. 

There are tools to deal with these problems, one of these tools is a Google OrTools package with **CBC_MIXED_INTEGER_PROGRAMMING** backend. 

I think these results are final but there may be some mistakes. 

  


There are also some important preconditions that may affect end result. These are the main ones: 

  * What clock speed do we use for buildings? For miners, power generation, and buildings with somersloops inside the only correct answer is 250%. But for other buildings you can go as low as 1% to save some power (and use those resources to generate more sink points). Here I will do calculations for 3 different power amounts: 
    * 1% as an absolute theoretcial maximum, totally not feasible to build
    * 100% as the default and mid-point amount
    * 250% as the most realistically buildable amount
  * Do we research the power amplification technology in a MAM? The most optimal solution is to not use power amplifiers at all, so it is possible to save 1 somersloop by not researching power amplifiers. For the calculations below I assume that this 1 extra somersloop is available. If you are going to build some of these and you already spent this somersloop, remove it from one of the AI Expansion Server buildings.
  * Do we allow to store uranium/plutonium waste indefinitely? By doing that it is possible to generate more points. But for the calculations below the answer is **no**



There are 106 somersloops, 3 or 2 are used for research, 103 or 104 remaining to be used. 

Also interesting points: 

  * Fewer alternate recipes used than expected. Alternate recipes often use less amount of rarer resources. But since the map has abundance of basic resources, it is more efficient to use those.
  * Plutonium/ficsonium is not used for power. Ficsonium requires SAM and that is too precious of a resource to use on the power. So optimal bases only use uranium rods and sink plutonium fuel rods like in stone age.



### 1% clock speed buildings, 104 Somersloops

  * Sink points per minute: 511,613,703
  * Alien power amplifiers: 0
  * Extra power: 
    * 7100MW from geothermal generators
    * -30MW for a single sink

Sinking  Sink object  | Amount per minute  | Sink points per minute   
---|---|---  
Sink Uranium  | 284.7850324  | 9967.476135   
Sink Assembly Director System  | 186.2936079  | 93179591.64   
Sink Ballistic Warp Drive  | 120.0546188  | 347598219.8   
Sink AI Expansion Server  | 116.7622496  | 69783192.02   
Sink Plutonium Fuel Rod  | 6.807056128  | 1042732.086   
Recipes and mining  Recipe name  | Building count  | Cycles per minute  | Power used (MW)  | Clock speed  | Somersloops   
---|---|---|---|---|---  
Ballistic Warp Drive  | 24  | 60  | 17728.92  | 2.5  | 4 (96)   
AI Expansion Server  | 2  | 20  | 26862  | 2.5  | 4 (8)   
Alternate: Iron Wire  | 501695.7498  | 12542.39374  | 4556.636799  | 0.01  | 0   
Alternate: Pure Iron Ingot  | 255522.9266  | 12776.14633  | 17405.84564  | 0.01  | 0   
Alternate: Pure Copper Ingot  | 231534.9019  | 5788.372548  | 15771.81671  | 0.01  | 0   
Cable  | 124195.7386  | 37258.72159  | 1128.00412  | 0.01  | 0   
Alternate: Steamed Copper Sheet  | 112774.1529  | 8458.061471  | 7682.009298  | 0.01  | 0   
Alternate: Iron Pipe  | 96681.45673  | 4834.072836  | 878.1064693  | 0.01  | 0   
Automated Wiring  | 74517.44317  | 1862.936079  | 2538.009271  | 0.01  | 0   
Modular Frame  | 69138.87138  | 691.3887138  | 2354.819074  | 0.01  | 0   
Alternate: Pure Aluminum Ingot  | 66879.15073  | 20063.74522  | 607.4279072  | 0.01  | 0   
Stator  | 61469.71759  | 3073.485879  | 2093.61334  | 0.01  | 0   
Alternate: Silicon Circuit Board  | 59662.05412  | 1491.551353  | 2032.045653  | 0.01  | 0   
Alternate: Compacted Steel Ingot  | 53339.51347  | 1333.487837  | 1937.81821  | 0.01  | 0   
Alternate: Fused Quickwire  | 47458.26261  | 3559.369696  | 1616.393496  | 0.01  | 0   
Time Crystal  | 43929.85302  | 2635.791181  | 24936.97437  | 0.01  | 0   
Alternate: Stitched Iron Plate  | 42212.25308  | 791.4797452  | 1437.718272  | 0.01  | 0   
Alternate: Heavy Oil Residue  | 41125.78895  | 4112.578895  | 2801.428207  | 0.01  | 0   
Alternate: Insulated Crystal Oscillator  | 39757.87449  | 745.4601467  | 4965.121128  | 0.01  | 0   
Alternate: Encased Industrial Pipe  | 39432.01924  | 1577.280769  | 1343.025554  | 0.01  | 0   
Adaptive Control Unit  | 37258.72159  | 372.5872159  | 4653.016996  | 0.01  | 0   
Alternate: Recycled Rubber  | 35745.07353  | 1787.253676  | 2434.901793  | 0.01  | 0   
Screw  | 32232.50707  | 3223.250707  | 292.7507915  | 0.01  | 0   
Alternate: Caterium Computer  | 30998.08519  | 1162.428195  | 3871.16388  | 0.01  | 0   
Alternate: Recycled Plastic  | 29539.89097  | 1476.994549  | 2012.213891  | 0.01  | 0   
AI Limiter  | 26438.44163  | 1321.922081  | 900.4738636  | 0.01  | 0   
Alternate: Wet Concrete  | 25433.09635  | 5086.61927  | 1732.465086  | 0.01  | 0   
Assembly Director System  | 24839.14772  | 186.2936079  | 846.0030902  | 0.01  | 0   
Alternate: Steel Rod  | 23999.82348  | 2879.978818  | 217.9776865  | 0.01  | 0   
Alclad Aluminum Sheet  | 23017.73631  | 2301.773631  | 783.967158  | 0.01  | 0   
Alternate: Diluted Fuel  | 21751.2661  | 2175.12661  | 3704.160574  | 0.01  | 0   
Residual Rubber  | 20562.89447  | 2056.289447  | 1400.714103  | 0.01  | 0   
Alternate: Fused Wire  | 19579.39287  | 587.3817861  | 666.859711  | 0.01  | 0   
Alternate: Crystal Computer  | 18902.15815  | 315.0359692  | 643.793595  | 0.01  | 0   
Alternate: Coated Iron Plate  | 17857.27166  | 1339.295374  | 608.2055299  | 0.01  | 0   
Packaged Turbofuel  | 17397.099  | 1739.7099  | 395.0215918  | 0.01  | 0   
Alternate: Heavy Encased Frame  | 16824.32821  | 157.7280769  | 2101.088866  | 0.01  | 0   
Modular Engine  | 15013.65471  | 150.1365471  | 1874.964775  | 0.01  | 0   
Smart Plating  | 15013.65471  | 300.2730942  | 511.3540295  | 0.01  | 0   
Alternate: Pure Caterium Ingot  | 14722.14183  | 1766.65702  | 1002.850631  | 0.01  | 0   
Electromagnetic Control Rod  | 14411.54837  | 288.2309674  | 490.8467307  | 0.01  | 0   
Alternate: Electrode Aluminum Scrap  | 13375.83015  | 2006.374522  | 911.1418607  | 0.01  | 0   
Copper Powder  | 12010.92377  | 1201.092377  | 109.0888596  | 0.01  | 0   
Alternate: Super-State Computer  | 11793.99407  | 283.0558576  | 1472.880778  | 0.01  | 0   
Alternate: Sloppy Alumina  | 10031.87261  | 2006.374522  | 683.3563956  | 0.01  | 0   
Alternate: Quartz Purification  | 9939.468623  | 496.9734312  | 677.061972  | 0.01  | 0   
Magnetic Field Generator  | 9676.224963  | 48.38112481  | 329.5651007  | 0.01  | 0   
Alternate: Classic Battery  | 9435.195252  | 707.6396439  | 1178.304622  | 0.01  | 0   
Coal (Limestone)  | 9353.987353  | 935.3987353  | 5309.832081  | 0.01  | 0   
Alternate: Turbo Diamonds  | 8698.549498  | 1739.7099  | 9875.539796  | 0.01  | 0   
Reanimated SAM  | 8500  | 2550  | 77.20099843  | 0.01  | 0   
Petroleum Coke  | 8137.673323  | 813.7673323  | 554.3263283  | 0.01  | 0   
Radio Control Unit  | 7926.325142  | 99.07906427  | 989.8709357  | 0.01  | 0   
Alternate: Turbo Blend Fuel  | 7732.043998  | 579.9032999  | 1316.738639  | 0.01  | 0   
Nitric Acid  | 7357.154499  | 735.7154499  | 1252.896337  | 0.01  | 0   
Alternate: Dark Matter Trap  | 7173.266443  | 2151.979933  | 16287.74504  | 0.01  | 0   
Alternate: Cheap Silica  | 6989.500676  | 524.2125507  | 238.0572488  | 0.01  | 0   
Alternate: Rigor Motor  | 6979.632114  | 87.24540143  | 871.644154  | 0.01  | 0   
Sulfuric Acid  | 6961.9288  | 696.19288  | 474.2363421  | 0.01  | 0   
Alternate: Copper Rotor  | 6611.796322  | 247.9423621  | 225.1929165  | 0.01  | 0   
Alternate: Leached Caterium Ingot  | 6611.373506  | 396.6824104  | 450.3570315  | 0.01  | 0   
Nuclear Pasta  | 6005.461884  | 30.02730942  | 13636.10745  | 0.01  | 0   
Thermal Propulsion Rocket  | 6005.461884  | 30.02730942  | 749.98591  | 0.01  | 0   
Alternate: Coated Iron Canister  | 5799.032999  | 869.8549498  | 197.5107959  | 0.01  | 0   
Alternate: Compacted Coal  | 5333.951347  | 266.6975674  | 181.6704572  | 0.01  | 0   
Bauxite (Caterium)  | 5264.362844  | 526.4362844  | 2988.338733  | 0.01  | 0   
Excited Photonic Matter  | 5129.949832  | 1025.989966  | 2912.038595  | 0.01  | 0   
Alternate: Distilled Silica  | 4969.734312  | 496.9734312  | 846.327465  | 0.01  | 0   
Ficsite Trigon  | 4838.112481  | 483.8112481  | 43.94201342  | 0.01  | 0   
Alternate: Uranium Fuel Unit  | 4538.037419  | 9.076074838  | 566.72812  | 0.01  | 0   
Superposition Oscillator  | 4337.429746  | 216.8714873  | 9848.644324  | 0.01  | 0   
Alternate: Heat Exchanger  | 4283.982743  | 428.3982743  | 145.9092993  | 0.01  | 0   
Encased Plutonium Cell  | 4084.233677  | 204.2116839  | 139.1059931  | 0.01  | 0   
Pressure Conversion Cube  | 4054.239612  | 40.54239612  | 138.0844173  | 0.01  | 0   
Alternate: Alclad Casing  | 3960.644337  | 297.0483253  | 134.8966311  | 0.01  | 0   
Encased Uranium Cell  | 3630.429935  | 181.5214968  | 618.2488582  | 0.01  | 0   
Alternate: Cooling Device  | 3603.27713  | 90.08192825  | 613.6248354  | 0.01  | 0   
Alternate: Heat-Fused Frame  | 3353.233832  | 100.597015  | 571.0433819  | 0.01  | 0   
Alternate: Flexible Framework  | 3225.408321  | 120.952812  | 402.8017897  | 0.01  | 0   
Neural-Quantum Processor  | 3225.408321  | 96.76224963  | 7323.668904  | 0.01  | 0   
Singularity Cell  | 3002.730942  | 30.02730942  | 374.992955  | 0.01  | 0   
Plutonium Fuel Rod  | 2722.822451  | 6.807056128  | 340.036872  | 0.01  | 0   
Non-Fissile Uranium  | 2722.822451  | 68.07056128  | 463.6866437  | 0.01  | 0   
AI Expansion Server  | 1919.056241  | 76.76224963  | 4357.442877  | 0.01  | 0   
Alternate: Molded Beam  | 1884.986406  | 94.24932028  | 68.48133296  | 0.01  | 0   
Ficsite Ingot (Aluminum)  | 1612.70416  | 483.8112481  | 915.458613  | 0.01  | 0   
Alternate: Turbo Electric Motor  | 1387.535838  | 13.00814848  | 173.2809812  | 0.01  | 0   
Plutonium Pellet  | 1361.411226  | 13.61411226  | 1545.622146  | 0.01  | 0   
Bauxite (Copper)  | 1205.424839  | 120.5424839  | 684.2647141  | 0.01  | 0   
Alternate: Turbo Pressure Motor  | 560.804624  | 10.5150867  | 70.03550675  | 0.01  | 0   
Packaged Nitrogen Gas  | 420.603468  | 252.3620808  | 9.550296375  | 0.01  | 0   
Empty Fluid Tank  | 420.603468  | 252.3620808  | 3.82011855  | 0.01  | 0   
Alternate: Molded Steel Pipe  | 383.9776847  | 38.39776847  | 13.94986383  | 0.01  | 0   
Alternate: Oil-Based Diamonds  | 131.131658  | 26.22633159  | 148.8749253  | 0.01  | 0   
Burn Uranium Fuel Rod in Nuclear Power Plant  | 54.45644903  | 27.22822451  | -340352.8064  | 2.5  | 0   
Ballistic Warp Drive  | 5.461883606  | 0.05461883606  | 0.6821016977  | 0.01  | 0   
Mining Iron Ore using Miner Mk.3 on a Impure node  | 39  | 11700  | 5892.85125  | 2.5  | 0   
Mining Iron Ore using Miner Mk.3 on a Normal node  | 42  | 25200  | 6346.1475  | 2.5  | 0   
Mining Iron Ore using Miner Mk.3 on a Pure node  | 46  | 55200  | 6950.5425  | 2.5  | 0   
Mining Copper Ore using Miner Mk.3 on a Impure node  | 13  | 3900  | 1964.28375  | 2.5  | 0   
Mining Copper Ore using Miner Mk.3 on a Normal node  | 29  | 17400  | 4381.86375  | 2.5  | 0   
Mining Copper Ore using Miner Mk.3 on a Pure node  | 13  | 15600  | 1964.28375  | 2.5  | 0   
Mining Limestone using Miner Mk.3 on a Impure node  | 15  | 4500  | 2266.48125  | 2.5  | 0   
Mining Limestone using Miner Mk.3 on a Normal node  | 50  | 30000  | 7554.9375  | 2.5  | 0   
Mining Limestone using Miner Mk.3 on a Pure node  | 29  | 34800  | 4381.86375  | 2.5  | 0   
Mining Coal using Miner Mk.3 on a Impure node  | 15  | 4500  | 2266.48125  | 2.5  | 0   
Mining Coal using Miner Mk.3 on a Normal node  | 31  | 18600  | 4684.06125  | 2.5  | 0   
Mining Coal using Miner Mk.3 on a Pure node  | 16  | 19200  | 2417.58  | 2.5  | 0   
Mining Caterium Ore using Miner Mk.3 on a Normal node  | 9  | 5400  | 1359.88875  | 2.5  | 0   
Mining Caterium Ore using Miner Mk.3 on a Pure node  | 8  | 9600  | 1208.79  | 2.5  | 0   
Mining Raw Quartz using Miner Mk.3 on a Impure node  | 3  | 900  | 453.29625  | 2.5  | 0   
Mining Raw Quartz using Miner Mk.3 on a Normal node  | 7  | 4200  | 1057.69125  | 2.5  | 0   
Mining Raw Quartz using Miner Mk.3 on a Pure node  | 7  | 8400  | 1057.69125  | 2.5  | 0   
Mining Sulfur using Miner Mk.3 on a Impure node  | 6  | 1800  | 906.5925  | 2.5  | 0   
Mining Sulfur using Miner Mk.3 on a Normal node  | 5  | 3000  | 755.49375  | 2.5  | 0   
Mining Sulfur using Miner Mk.3 on a Pure node  | 5  | 6000  | 755.49375  | 2.5  | 0   
Mining Uranium using Miner Mk.3 on a Impure node  | 3  | 900  | 453.29625  | 2.5  | 0   
Mining Uranium using Miner Mk.3 on a Normal node  | 2  | 1200  | 302.1975  | 2.5  | 0   
Mining Bauxite using Miner Mk.3 on a Impure node  | 5  | 1500  | 755.49375  | 2.5  | 0   
Mining Bauxite using Miner Mk.3 on a Normal node  | 6  | 3600  | 906.5925  | 2.5  | 0   
Mining Bauxite using Miner Mk.3 on a Pure node  | 6  | 7200  | 906.5925  | 2.5  | 0   
Mining SAM using Miner Mk.3 on a Impure node  | 10  | 3000  | 1510.9875  | 2.5  | 0   
Mining SAM using Miner Mk.3 on a Normal node  | 6  | 3600  | 906.5925  | 2.5  | 0   
Mining SAM using Miner Mk.3 on a Pure node  | 3  | 3600  | 453.29625  | 2.5  | 0   
Mining Crude Oil using Oil Extractor on a Impure node  | 10  | 1500  | 1343.1  | 2.5  | 0   
Mining Crude Oil using Oil Extractor on a Normal node  | 12  | 3600  | 1611.72  | 2.5  | 0   
Mining Crude Oil using Oil Extractor on a Pure node  | 8  | 4800  | 1074.48  | 2.5  | 0   
Mining Crude Oil using Resource Well Extractor on a Impure node  | 8  | 600  | 0  | 2.5  | 0   
Mining Crude Oil using Resource Well Extractor on a Normal node  | 6  | 900  | 0  | 2.5  | 0   
Mining Crude Oil using Resource Well Extractor on a Pure node  | 4  | 1200  | 0  | 2.5  | 0   
Mining Crude Oil using Resource Well Pressurizer  | 3  |  | 1510.9875  | 2.5  | 0   
Mining Nitrogen Gas using Resource Well Extractor on a Impure node  | 2  | 150  | 0  | 2.5  | 0   
Mining Nitrogen Gas using Resource Well Extractor on a Normal node  | 7  | 1050  | 0  | 2.5  | 0   
Mining Nitrogen Gas using Resource Well Extractor on a Pure node  | 36  | 10800  | 0  | 2.5  | 0   
Mining Nitrogen Gas using Resource Well Pressurizer  | 6  |  | 3021.975  | 2.5  | 0   
Mining Water using Water Extractor on a Normal node  | 169618.1012  | 203541.7214  | 7702.75692  | 0.01  | 0   
  
### 100% clock speed buildings, 104 Somersloops

  * Sink points per minute: 480,345,879
  * Alien power amplifiers: 0
  * Extra power: 
    * 7100MW from geothermal generators
    * -30MW for a single sink

Sinking  Sink object  | Amount per minute  | Sink points per minute   
---|---|---  
Sink Assembly Director System  | 122.4561239  | 61249614.24   
Sink Ballistic Warp Drive  | 120  | 347440080   
Sink AI Expansion Server  | 116.6666667  | 69726066.67   
Sink Plutonium Fuel Rod  | 12.6  | 1930118.4   
Recipes and mining  Recipe name  | Building count  | Cycles per minute  | Power used (MW)  | Clock speed  | Somersloops   
---|---|---|---|---|---  
Ballistic Warp Drive  | 24  | 60  | 17728.92  | 2.5  | 4 (96)   
AI Expansion Server  | 4  | 40  | 30219.75  | 2.5  | 2 (8)   
Alternate: Iron Wire  | 4173.697971  | 10434.24493  | 16694.79188  | 1  | 0   
Alternate: Pure Iron Ingot  | 2537.40234  | 12687.0117  | 76122.07019  | 1  | 0   
Alternate: Pure Copper Ingot  | 2251.774651  | 5629.436626  | 67553.23952  | 1  | 0   
Alternate: Steamed Copper Sheet  | 1046.565346  | 7849.240095  | 31396.96038  | 1  | 0   
Alternate: Iron Pipe  | 962.2729093  | 4811.364546  | 3849.091637  | 1  | 0   
Cable  | 816.3741594  | 24491.22478  | 3265.496638  | 1  | 0   
Burn Rocket Fuel in Fuel-Powered Generator  | 719.7510515  | 7497.406786  | -449844.4072  | 2.5  | 0   
Alternate: Pure Aluminum Ingot  | 667.8443872  | 20035.33162  | 2671.377549  | 1  | 0   
Stator  | 578.4895082  | 2892.447541  | 8677.342624  | 1  | 0   
Alternate: Fused Quickwire  | 528.9101565  | 3966.826174  | 7933.652347  | 1  | 0   
Automated Wiring  | 489.8244957  | 1224.561239  | 7347.367435  | 1  | 0   
Alternate: Silicon Circuit Board  | 471.5771513  | 1178.942878  | 7073.65727  | 1  | 0   
Time Crystal  | 438.8888889  | 2633.333333  | 109722.2222  | 1  | 0   
Iron Plate  | 436.242998  | 4362.42998  | 1744.971992  | 1  | 0   
Alternate: Heavy Oil Residue  | 420  | 4200  | 12600  | 1  | 0   
Alternate: Compacted Steel Ingot  | 358.958453  | 897.3961326  | 5743.335249  | 1  | 0   
Alternate: Steeled Frame  | 342.9466794  | 342.9466794  | 5144.20019  | 1  | 0   
Alternate: Pure Caterium Ingot  | 330.5688478  | 3966.826174  | 9917.065434  | 1  | 0   
Alternate: Cheap Silica  | 295.0166031  | 2212.624523  | 4425.249046  | 1  | 0   
Alternate: Insulated Crystal Oscillator  | 284.6511705  | 533.7209446  | 15655.81438  | 1  | 0   
Alternate: Encased Industrial Pipe  | 283.7520952  | 1135.008381  | 4256.281428  | 1  | 0   
Alternate: Caterium Computer  | 279.7765813  | 1049.16218  | 15387.71197  | 1  | 0   
Alternate: Cast Screw  | 275.6277253  | 689.0693133  | 1102.510901  | 1  | 0   
Alclad Aluminum Sheet  | 273.8216278  | 2738.216278  | 4107.324418  | 1  | 0   
AI Limiter  | 266.1364356  | 1330.682178  | 3992.046535  | 1  | 0   
Adaptive Control Unit  | 244.9122478  | 244.9122478  | 13470.17363  | 1  | 0   
Alternate: Recycled Rubber  | 228.2721688  | 1141.360844  | 6848.165065  | 1  | 0   
Alternate: Wet Concrete  | 225.9639587  | 4519.279174  | 6778.918761  | 1  | 0   
Residual Rubber  | 210  | 2100  | 6300  | 1  | 0   
Electromagnetic Control Rod  | 199.2403084  | 398.4806168  | 2988.604626  | 1  | 0   
Alternate: Recycled Plastic  | 187.1770146  | 935.8850731  | 5615.310438  | 1  | 0   
Packaged Turbofuel  | 175.5555556  | 1755.555556  | 1755.555556  | 1  | 0   
Alternate: Stitched Iron Plate  | 175.2699304  | 328.6311196  | 2629.048957  | 1  | 0   
Alternate: Diluted Fuel  | 171.2281807  | 1712.281807  | 12842.11356  | 1  | 0   
Assembly Director System  | 163.2748319  | 122.4561239  | 2449.122478  | 1  | 0   
Smart Plating  | 150  | 300  | 2250  | 1  | 0   
Modular Engine  | 150  | 150  | 8250  | 1  | 0   
Alternate: Turbo Blend Fuel  | 148.4590244  | 1113.442683  | 11134.42683  | 1  | 0   
Alternate: Electrode Aluminum Scrap  | 133.5688774  | 2003.533162  | 4007.066323  | 1  | 0   
Alternate: Heavy Encased Frame  | 121.0675606  | 113.5008381  | 6658.715835  | 1  | 0   
Copper Powder  | 120  | 1200  | 480  | 1  | 0   
Alternate: Steel Rotor  | 105.3932858  | 526.9664288  | 1580.899286  | 1  | 0   
Alternate: Pure Quartz Crystal  | 101.6611323  | 762.4584923  | 3049.833969  | 1  | 0   
Burn Uranium Fuel Rod in Nuclear Power Plant  | 100.8  | 50.4  | -630000  | 2.5  | 0   
Alternate: Sloppy Alumina  | 100.1766581  | 2003.533162  | 3005.299742  | 1  | 0   
Magnetic Field Generator  | 96.66666667  | 48.33333333  | 1450  | 1  | 0   
Alternate: Crystal Computer  | 94.7008865  | 157.8348108  | 1420.513298  | 1  | 0   
Petroleum Coke  | 94.62050579  | 946.2050579  | 2838.615174  | 1  | 0   
Alternate: Super-State Computer  | 91.30116274  | 219.1227906  | 5021.563951  | 1  | 0   
Alternate: Turbo Diamonds  | 87.77777778  | 1755.555556  | 43888.88889  | 1  | 0   
Radio Control Unit  | 87.05557369  | 108.8194671  | 4788.056553  | 1  | 0   
Coal (Limestone)  | 86.44778428  | 864.4778428  | 21611.94607  | 1  | 0   
Reanimated SAM  | 85  | 2550  | 340  | 1  | 0   
Alternate: Infused Uranium Cell  | 84  | 420  | 4620  | 1  | 0   
Alternate: Uranium Fuel Unit  | 84  | 16.8  | 4620  | 1  | 0   
Encased Plutonium Cell  | 75.6  | 378  | 1134  | 1  | 0   
Alternate: Classic Battery  | 73.04093019  | 547.8069765  | 4017.251161  | 1  | 0   
Alternate: Dark Matter Trap  | 71.66666667  | 2150  | 71666.66667  | 1  | 0   
Alternate: Copper Rotor  | 70.67377572  | 265.026659  | 1060.106636  | 1  | 0   
Nitric Acid  | 68.29932097  | 682.9932097  | 5122.449073  | 1  | 0   
Heat Sink  | 64.8  | 486  | 972  | 1  | 0   
Nuclear Pasta  | 60  | 30  | 60000  | 1  | 0   
Thermal Propulsion Rocket  | 60  | 30  | 3300  | 1  | 0   
Alternate: Coated Iron Canister  | 58.51851852  | 877.7777778  | 877.7777778  | 1  | 0   
Rocket Fuel  | 52.82574977  | 528.2574977  | 3961.931233  | 1  | 0   
Excited Photonic Matter  | 51.25  | 1025  | 12812.5  | 1  | 0   
Plutonium Fuel Rod  | 50.4  | 12.6  | 2772  | 1  | 0   
Non-Fissile Uranium  | 50.4  | 126  | 3780  | 1  | 0   
Versatile Framework  | 48.33333333  | 120.8333333  | 725  | 1  | 0   
Ficsite Trigon  | 48.33333333  | 483.3333333  | 193.3333333  | 1  | 0   
Bauxite (Caterium)  | 47.10898435  | 471.0898435  | 11777.24609  | 1  | 0   
Superposition Oscillator  | 43.33333333  | 216.6666667  | 43333.33333  | 1  | 0   
Motor  | 42.77223201  | 213.8611601  | 641.5834802  | 1  | 0   
Alternate: Electric Motor  | 41.65493275  | 156.2059978  | 624.8239913  | 1  | 0   
Alternate: Cooling Device  | 36  | 90  | 2700  | 1  | 0   
Pressure Conversion Cube  | 35.59026644  | 35.59026644  | 533.8539966  | 1  | 0   
Neural-Quantum Processor  | 32.22222222  | 96.66666667  | 32222.22222  | 1  | 0   
Alternate: Heat-Fused Frame  | 31.86342215  | 95.59026644  | 2389.756661  | 1  | 0   
Alternate: Alclad Casing  | 30.95309287  | 232.1481965  | 464.296393  | 1  | 0   
Singularity Cell  | 30  | 30  | 1650  | 1  | 0   
Alternate: Molded Beam  | 29.91320442  | 149.5660221  | 478.6112707  | 1  | 0   
Plutonium Pellet  | 25.2  | 25.2  | 12600  | 1  | 0   
Alternate: Turbo Electric Motor  | 17.35803275  | 16.27315571  | 954.6918014  | 1  | 0   
Bauxite (Copper)  | 17.35211245  | 173.5211245  | 4338.028113  | 1  | 0   
Ficsite Ingot (Aluminum)  | 16.11111111  | 483.3333333  | 4027.777778  | 1  | 0   
Sulfuric Acid  | 15.12  | 151.2  | 453.6  | 1  | 0   
Alternate: Nitro Rocket Fuel  | 14.76554598  | 369.1386349  | 1107.415949  | 1  | 0   
Alternate: Aluminum Beam  | 14.69803561  | 110.235267  | 58.79214242  | 1  | 0   
AI Expansion Server  | 14.16666667  | 56.66666667  | 14166.66667  | 1  | 0   
Coal (Iron)  | 6.093415191  | 60.93415191  | 1523.353798  | 1  | 0   
Alternate: Turbo Pressure Motor  | 2.981475436  | 5.590266442  | 163.981149  | 1  | 0   
Empty Fluid Tank  | 2.236106577  | 134.1663946  | 8.944426307  | 1  | 0   
Packaged Nitrogen Gas  | 2.236106577  | 134.1663946  | 22.36106577  | 1  | 0   
Sulfur (Iron)  | 1.331037058  | 13.31037058  | 332.7592644  | 1  | 0   
Mining Iron Ore using Miner Mk.3 on a Impure node  | 39  | 11700  | 5892.85125  | 2.5  | 0   
Mining Iron Ore using Miner Mk.3 on a Normal node  | 42  | 25200  | 6346.1475  | 2.5  | 0   
Mining Iron Ore using Miner Mk.3 on a Pure node  | 46  | 55200  | 6950.5425  | 2.5  | 0   
Mining Copper Ore using Miner Mk.3 on a Impure node  | 13  | 3900  | 1964.28375  | 2.5  | 0   
Mining Copper Ore using Miner Mk.3 on a Normal node  | 29  | 17400  | 4381.86375  | 2.5  | 0   
Mining Copper Ore using Miner Mk.3 on a Pure node  | 13  | 15600  | 1964.28375  | 2.5  | 0   
Mining Limestone using Miner Mk.3 on a Impure node  | 15  | 4500  | 2266.48125  | 2.5  | 0   
Mining Limestone using Miner Mk.3 on a Normal node  | 50  | 30000  | 7554.9375  | 2.5  | 0   
Mining Limestone using Miner Mk.3 on a Pure node  | 29  | 34800  | 4381.86375  | 2.5  | 0   
Mining Coal using Miner Mk.3 on a Impure node  | 15  | 4500  | 2266.48125  | 2.5  | 0   
Mining Coal using Miner Mk.3 on a Normal node  | 31  | 18600  | 4684.06125  | 2.5  | 0   
Mining Coal using Miner Mk.3 on a Pure node  | 16  | 19200  | 2417.58  | 2.5  | 0   
Mining Caterium Ore using Miner Mk.3 on a Normal node  | 9  | 5400  | 1359.88875  | 2.5  | 0   
Mining Caterium Ore using Miner Mk.3 on a Pure node  | 8  | 9600  | 1208.79  | 2.5  | 0   
Mining Raw Quartz using Miner Mk.3 on a Impure node  | 3  | 900  | 453.29625  | 2.5  | 0   
Mining Raw Quartz using Miner Mk.3 on a Normal node  | 7  | 4200  | 1057.69125  | 2.5  | 0   
Mining Raw Quartz using Miner Mk.3 on a Pure node  | 7  | 8400  | 1057.69125  | 2.5  | 0   
Mining Sulfur using Miner Mk.3 on a Impure node  | 6  | 1800  | 906.5925  | 2.5  | 0   
Mining Sulfur using Miner Mk.3 on a Normal node  | 5  | 3000  | 755.49375  | 2.5  | 0   
Mining Sulfur using Miner Mk.3 on a Pure node  | 5  | 6000  | 755.49375  | 2.5  | 0   
Mining Uranium using Miner Mk.3 on a Impure node  | 3  | 900  | 453.29625  | 2.5  | 0   
Mining Uranium using Miner Mk.3 on a Normal node  | 2  | 1200  | 302.1975  | 2.5  | 0   
Mining Bauxite using Miner Mk.3 on a Impure node  | 5  | 1500  | 755.49375  | 2.5  | 0   
Mining Bauxite using Miner Mk.3 on a Normal node  | 6  | 3600  | 906.5925  | 2.5  | 0   
Mining Bauxite using Miner Mk.3 on a Pure node  | 6  | 7200  | 906.5925  | 2.5  | 0   
Mining SAM using Miner Mk.3 on a Impure node  | 10  | 3000  | 1510.9875  | 2.5  | 0   
Mining SAM using Miner Mk.3 on a Normal node  | 6  | 3600  | 906.5925  | 2.5  | 0   
Mining SAM using Miner Mk.3 on a Pure node  | 3  | 3600  | 453.29625  | 2.5  | 0   
Mining Crude Oil using Oil Extractor on a Impure node  | 10  | 1500  | 1343.1  | 2.5  | 0   
Mining Crude Oil using Oil Extractor on a Normal node  | 12  | 3600  | 1611.72  | 2.5  | 0   
Mining Crude Oil using Oil Extractor on a Pure node  | 8  | 4800  | 1074.48  | 2.5  | 0   
Mining Crude Oil using Resource Well Extractor on a Impure node  | 8  | 600  | 0  | 2.5  | 0   
Mining Crude Oil using Resource Well Extractor on a Normal node  | 6  | 900  | 0  | 2.5  | 0   
Mining Crude Oil using Resource Well Extractor on a Pure node  | 4  | 1200  | 0  | 2.5  | 0   
Mining Crude Oil using Resource Well Pressurizer  | 3  |  | 1510.9875  | 2.5  | 0   
Mining Nitrogen Gas using Resource Well Extractor on a Impure node  | 2  | 150  | 0  | 2.5  | 0   
Mining Nitrogen Gas using Resource Well Extractor on a Normal node  | 7  | 1050  | 0  | 2.5  | 0   
Mining Nitrogen Gas using Resource Well Extractor on a Pure node  | 36  | 10800  | 0  | 2.5  | 0   
Mining Nitrogen Gas using Resource Well Pressurizer  | 6  |  | 3021.975  | 2.5  | 0   
Mining Water using Water Extractor on a Normal node  | 1876.818762  | 225218.2514  | 37536.37524  | 1  | 0   
  
### 250% clock speed buildings, 104 Somersloops

  * Sink points per minute: 463,281,456
  * Alien power amplifiers: 0
  * Extra power: 
    * 7100MW from geothermal generators
    * -30MW for a single sink

Sinking  Sink object  | Amount per minute  | Sink points per minute   
---|---|---  
Sink Assembly Director System  | 140.8644009  | 70456992.56   
Sink AI Expansion Server  | 120  | 71718240   
Sink Ballistic Warp Drive  | 110.2380952  | 319176105.2   
Sink Plutonium Fuel Rod  | 12.6  | 1930118.4   
Recipes and mining  Recipe name  | Building count  | Cycles per minute  | Power used (MW)  | Clock speed  | Somersloops   
---|---|---|---|---|---  
Ballistic Warp Drive  | 22  | 55  | 16251.51  | 2.5  | 4 (88)   
AI Expansion Server  | 8  | 80  | 60439.5  | 2.5  | 2 (16)   
Alternate: Iron Wire  | 1723.291397  | 10770.57123  | 23145.50981  | 2.5  | 0   
Burn Rocket Fuel in Fuel-Powered Generator  | 1187.383727  | 12368.58049  | -742114.8294  | 2.5  | 0   
Alternate: Pure Iron Ingot  | 963.4433341  | 12043.04168  | 97049.98459  | 2.5  | 0   
Alternate: Pure Copper Ingot  | 900.7245939  | 5629.528712  | 90732.17372  | 2.5  | 0   
Alternate: Steamed Copper Sheet  | 452.3935483  | 8482.379031  | 45570.69974  | 2.5  | 0   
Cable  | 375.6384023  | 28172.88017  | 5045.195687  | 2.5  | 0   
Alternate: Iron Pipe  | 374.8641952  | 4685.80244  | 5034.797319  | 2.5  | 0   
Alternate: Pure Aluminum Ingot  | 245.5250863  | 18414.38147  | 3297.64502  | 2.5  | 0   
Automated Wiring  | 225.3830414  | 1408.644009  | 11351.6903  | 2.5  | 0   
Alternate: Fused Quickwire  | 222.655209  | 4174.78517  | 11214.29971  | 2.5  | 0   
Stator  | 218.3510583  | 2729.388229  | 10997.51594  | 2.5  | 0   
Alternate: Silicon Circuit Board  | 208.3411534  | 1302.132209  | 10493.35493  | 2.5  | 0   
Alternate: Heavy Oil Residue  | 168  | 4200  | 16923.04761  | 2.5  | 0   
Time Crystal  | 156.8253968  | 2352.380952  | 131645.0227  | 2.5  | 0   
Alternate: Steeled Frame  | 142.9638914  | 357.4097285  | 7200.549823  | 2.5  | 0   
Alternate: Pure Caterium Ingot  | 139.1595057  | 4174.78517  | 14017.87464  | 2.5  | 0   
Alternate: Cheap Silica  | 128.3310804  | 2406.207757  | 6463.550543  | 2.5  | 0   
Alternate: Caterium Computer  | 125.0778562  | 1172.604902  | 23098.89253  | 2.5  | 0   
Alternate: Encased Industrial Pipe  | 121.5286482  | 1215.286482  | 6120.937795  | 2.5  | 0   
Adaptive Control Unit  | 112.6915207  | 281.7288017  | 20811.43221  | 2.5  | 0   
AI Limiter  | 109.5238136  | 1369.04767  | 5516.299739  | 2.5  | 0   
Alclad Aluminum Sheet  | 104.8874078  | 2622.185195  | 5282.781536  | 2.5  | 0   
Alternate: Insulated Crystal Oscillator  | 104.224325  | 488.5515234  | 19247.74341  | 2.5  | 0   
Alternate: Recycled Rubber  | 102.1834279  | 1277.292849  | 10293.18462  | 2.5  | 0   
Burn Uranium Fuel Rod in Nuclear Power Plant  | 100.8  | 50.4  | -630000  | 2.5  | 0   
Alternate: Diluted Fuel  | 100.1623905  | 2504.059761  | 25224.00152  | 2.5  | 0   
Alternate: Wet Concrete  | 89.33327779  | 4466.66389  | 8998.757816  | 2.5  | 0   
Electromagnetic Control Rod  | 88.04961469  | 440.2480734  | 4434.725659  | 2.5  | 0   
Alternate: Recycled Plastic  | 84.11970299  | 1051.496287  | 8473.581777  | 2.5  | 0   
Residual Rubber  | 84  | 2100  | 8461.523804  | 2.5  | 0   
Assembly Director System  | 75.12768046  | 140.8644009  | 3783.896765  | 2.5  | 0   
Alternate: Stitched Iron Plate  | 70.47181747  | 330.3366444  | 3549.398578  | 2.5  | 0   
Packaged Turbofuel  | 62.73015873  | 1568.253968  | 2106.320363  | 2.5  | 0   
Iron Plate  | 56.33735711  | 1408.433928  | 756.6664893  | 2.5  | 0   
Smart Plating  | 55.23809524  | 276.1904762  | 2782.133677  | 2.5  | 0   
Modular Engine  | 55.23809524  | 138.0952381  | 10201.15682  | 2.5  | 0   
Alternate: Heavy Encased Frame  | 51.85222323  | 121.5286482  | 9575.867128  | 2.5  | 0   
Turbofuel  | 50.73180689  | 475.6106896  | 5110.337996  | 2.5  | 0   
Alternate: Electrode Aluminum Scrap  | 49.10501726  | 1841.438147  | 4946.46753  | 2.5  | 0   
Copper Powder  | 44.19047619  | 1104.761905  | 593.5218511  | 2.5  | 0   
Alternate: Copper Rotor  | 37.72500882  | 353.6719577  | 1900.065834  | 2.5  | 0   
Alternate: Pure Quartz Crystal  | 37.22297321  | 697.9307478  | 3749.560404  | 2.5  | 0   
Alternate: Sloppy Alumina  | 36.82876295  | 1841.438147  | 3709.850647  | 2.5  | 0   
Alternate: Super-State Computer  | 36.81073348  | 220.8644009  | 6798.063241  | 2.5  | 0   
Radio Control Unit  | 35.35238095  | 110.4761905  | 6528.740362  | 2.5  | 0   
Reanimated SAM  | 34  | 2550  | 456.6536656  | 2.5  | 0   
Coal (Limestone)  | 33.85441987  | 846.3604967  | 28418.64877  | 2.5  | 0   
Alternate: Infused Uranium Cell  | 33.6  | 420  | 6205.117457  | 2.5  | 0   
Alternate: Uranium Fuel Unit  | 33.6  | 16.8  | 6205.117457  | 2.5  | 0   
Alternate: Crystal Computer  | 32.9277942  | 137.1991425  | 1658.4483  | 2.5  | 0   
Magnetic Field Generator  | 32  | 40  | 1611.71882  | 2.5  | 0   
Alternate: Turbo Diamonds  | 31.36507937  | 1568.253968  | 52658.00906  | 2.5  | 0   
Encased Plutonium Cell  | 30.24  | 378  | 1523.074285  | 2.5  | 0   
Alternate: Classic Battery  | 29.44858678  | 552.1610021  | 5438.450592  | 2.5  | 0   
Alternate: Coated Iron Plate  | 28.63521793  | 536.9103361  | 1442.247489  | 2.5  | 0   
Alternate: Steel Screw  | 28.29375661  | 353.6719577  | 380.0131668  | 2.5  | 0   
Petroleum Coke  | 28.20140929  | 705.0352323  | 2840.796382  | 2.5  | 0   
Alternate: Nitro Rocket Fuel  | 26.62338944  | 1663.961774  | 6704.596532  | 2.5  | 0   
Alternate: Dark Matter Trap  | 26.03174603  | 1952.380952  | 87408.03124  | 2.5  | 0   
Alternate: Electric Motor  | 26.02328042  | 243.968254  | 1310.694088  | 2.5  | 0   
Heat Sink  | 24.39619048  | 457.4285714  | 1228.743729  | 2.5  | 0   
Nitric Acid  | 22.0978417  | 552.4460425  | 5564.923023  | 2.5  | 0   
Thermal Propulsion Rocket  | 22.0952381  | 27.61904762  | 4080.462727  | 2.5  | 0   
Nuclear Pasta  | 22.0952381  | 27.61904762  | 74190.23139  | 2.5  | 0   
Alternate: Coated Iron Canister  | 20.91005291  | 784.1269841  | 1053.160181  | 2.5  | 0   
Alternate: Solid Steel Ingot  | 20.80783365  | 1040.391682  | 1117.879236  | 2.5  | 0   
Plutonium Fuel Rod  | 20.16  | 12.6  | 3723.070474  | 2.5  | 0   
Non-Fissile Uranium  | 20.16  | 126  | 5076.914283  | 2.5  | 0   
Alternate: Turbo Blend Fuel  | 19.46080352  | 364.8900661  | 4900.834889  | 2.5  | 0   
Excited Photonic Matter  | 17.52380952  | 876.1904762  | 14710.13209  | 2.5  | 0   
Ficsite Trigon  | 16  | 400  | 214.8958427  | 2.5  | 0   
Superposition Oscillator  | 15.23809524  | 190.4761905  | 51165.67682  | 2.5  | 0   
Bauxite (Caterium)  | 13.4416544  | 336.0413601  | 11283.42051  | 2.5  | 0   
Alternate: Cooling Device  | 13.25714286  | 82.85714286  | 3338.560413  | 2.5  | 0   
Alternate: Alclad Casing  | 12.56973545  | 235.6825397  | 633.0899745  | 2.5  | 0   
Alternate: Heat-Fused Frame  | 11.04761905  | 82.85714286  | 2782.133677  | 2.5  | 0   
Singularity Cell  | 11.04761905  | 27.61904762  | 2040.231363  | 2.5  | 0   
Pressure Conversion Cube  | 11.04761905  | 27.61904762  | 556.4267354  | 2.5  | 0   
Neural-Quantum Processor  | 10.66666667  | 80  | 35815.97378  | 2.5  | 0   
Alternate: Molded Beam  | 10.40391682  | 130.0489603  | 558.9396182  | 2.5  | 0   
Sulfur (Iron)  | 10.39827769  | 259.9569422  | 8728.697835  | 2.5  | 0   
Plutonium Pellet  | 10.08  | 25.2  | 16923.04761  | 2.5  | 0   
Rocket Fuel  | 9.539239387  | 238.4809847  | 2402.27682  | 2.5  | 0   
Alternate: Flexible Framework  | 9.221570916  | 86.45222734  | 1703.003889  | 2.5  | 0   
Alternate: Turbo Electric Motor  | 7.856084656  | 18.41269841  | 1450.831192  | 2.5  | 0   
Bauxite (Copper)  | 6.939617177  | 173.4904294  | 5825.370629  | 2.5  | 0   
Sulfuric Acid  | 6.048  | 151.2  | 609.2297139  | 2.5  | 0   
Nitrogen Gas (Caterium)  | 5.366030867  | 134.1507717  | 4504.444238  | 2.5  | 0   
Ficsite Ingot (Aluminum)  | 5.333333333  | 400  | 4476.996722  | 2.5  | 0   
Versatile Framework  | 2.167643626  | 13.54777266  | 109.1760008  | 2.5  | 0   
Alternate: Aluminum Beam  | 1.623430241  | 30.43931701  | 21.8042756  | 2.5  | 0   
Ballistic Warp Drive  | 0.09523809524  | 0.2380952381  | 17.58820141  | 2.5  | 0   
Mining Iron Ore using Miner Mk.3 on a Impure node  | 39  | 11700  | 5892.85125  | 2.5  | 0   
Mining Iron Ore using Miner Mk.3 on a Normal node  | 42  | 25200  | 6346.1475  | 2.5  | 0   
Mining Iron Ore using Miner Mk.3 on a Pure node  | 46  | 55200  | 6950.5425  | 2.5  | 0   
Mining Copper Ore using Miner Mk.3 on a Impure node  | 13  | 3900  | 1964.28375  | 2.5  | 0   
Mining Copper Ore using Miner Mk.3 on a Normal node  | 29  | 17400  | 4381.86375  | 2.5  | 0   
Mining Copper Ore using Miner Mk.3 on a Pure node  | 13  | 15600  | 1964.28375  | 2.5  | 0   
Mining Limestone using Miner Mk.3 on a Impure node  | 15  | 4500  | 2266.48125  | 2.5  | 0   
Mining Limestone using Miner Mk.3 on a Normal node  | 50  | 30000  | 7554.9375  | 2.5  | 0   
Mining Limestone using Miner Mk.3 on a Pure node  | 29  | 34800  | 4381.86375  | 2.5  | 0   
Mining Coal using Miner Mk.3 on a Impure node  | 15  | 4500  | 2266.48125  | 2.5  | 0   
Mining Coal using Miner Mk.3 on a Normal node  | 31  | 18600  | 4684.06125  | 2.5  | 0   
Mining Coal using Miner Mk.3 on a Pure node  | 16  | 19200  | 2417.58  | 2.5  | 0   
Mining Caterium Ore using Miner Mk.3 on a Normal node  | 9  | 5400  | 1359.88875  | 2.5  | 0   
Mining Caterium Ore using Miner Mk.3 on a Pure node  | 8  | 9600  | 1208.79  | 2.5  | 0   
Mining Raw Quartz using Miner Mk.3 on a Impure node  | 3  | 900  | 453.29625  | 2.5  | 0   
Mining Raw Quartz using Miner Mk.3 on a Normal node  | 7  | 4200  | 1057.69125  | 2.5  | 0   
Mining Raw Quartz using Miner Mk.3 on a Pure node  | 7  | 8400  | 1057.69125  | 2.5  | 0   
Mining Sulfur using Miner Mk.3 on a Impure node  | 6  | 1800  | 906.5925  | 2.5  | 0   
Mining Sulfur using Miner Mk.3 on a Normal node  | 5  | 3000  | 755.49375  | 2.5  | 0   
Mining Sulfur using Miner Mk.3 on a Pure node  | 5  | 6000  | 755.49375  | 2.5  | 0   
Mining Uranium using Miner Mk.3 on a Impure node  | 3  | 900  | 453.29625  | 2.5  | 0   
Mining Uranium using Miner Mk.3 on a Normal node  | 2  | 1200  | 302.1975  | 2.5  | 0   
Mining Bauxite using Miner Mk.3 on a Impure node  | 5  | 1500  | 755.49375  | 2.5  | 0   
Mining Bauxite using Miner Mk.3 on a Normal node  | 6  | 3600  | 906.5925  | 2.5  | 0   
Mining Bauxite using Miner Mk.3 on a Pure node  | 6  | 7200  | 906.5925  | 2.5  | 0   
Mining SAM using Miner Mk.3 on a Impure node  | 10  | 3000  | 1510.9875  | 2.5  | 0   
Mining SAM using Miner Mk.3 on a Normal node  | 6  | 3600  | 906.5925  | 2.5  | 0   
Mining SAM using Miner Mk.3 on a Pure node  | 3  | 3600  | 453.29625  | 2.5  | 0   
Mining Crude Oil using Oil Extractor on a Impure node  | 10  | 1500  | 1343.1  | 2.5  | 0   
Mining Crude Oil using Oil Extractor on a Normal node  | 12  | 3600  | 1611.72  | 2.5  | 0   
Mining Crude Oil using Oil Extractor on a Pure node  | 8  | 4800  | 1074.48  | 2.5  | 0   
Mining Crude Oil using Resource Well Extractor on a Impure node  | 8  | 600  | 0  | 2.5  | 0   
Mining Crude Oil using Resource Well Extractor on a Normal node  | 6  | 900  | 0  | 2.5  | 0   
Mining Crude Oil using Resource Well Extractor on a Pure node  | 4  | 1200  | 0  | 2.5  | 0   
Mining Crude Oil using Resource Well Pressurizer  | 3  |  | 1510.9875  | 2.5  | 0   
Mining Nitrogen Gas using Resource Well Extractor on a Impure node  | 2  | 150  | 0  | 2.5  | 0   
Mining Nitrogen Gas using Resource Well Extractor on a Normal node  | 7  | 1050  | 0  | 2.5  | 0   
Mining Nitrogen Gas using Resource Well Extractor on a Pure node  | 36  | 10800  | 0  | 2.5  | 0   
Mining Nitrogen Gas using Resource Well Pressurizer  | 6  |  | 3021.975  | 2.5  | 0   
Mining Water using Water Extractor on a Normal node  | 771.3740412  | 231412.2124  | 51801.58581  | 2.5  | 0   
  
  * 

  *[v]: View this template
  *[e]: Edit this template
  *[h]: History of this template
