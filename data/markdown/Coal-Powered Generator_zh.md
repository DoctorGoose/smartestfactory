# Coal-Powered Generator/zh

## Coal-Powered Generator  
  
[ ](/wiki/File:Coal-Powered_Generator.png "Coal-Powered Generator.png")

_Burns Coal to boil Water. The steam produced rotates turbines that generate electricity for the power grid.  
Has Conveyor Belt and Pipeline input ports that allow the Coal and Water supply to be automated.  
Caution: Always generates power at the set clock speed. Shuts down if fuel requirements are not met._

### Unlocked by

[Tier 3](/wiki/Tier_3 "Tier 3") \- Coal Power

### Class name

Desc_GeneratorCoal_C

## Building

### [Power  
generated](/wiki/Power "Power")

75 MW

### [Overclock­able](/wiki/Clock_speed "Clock speed")

Yes

### Conveyor  
inputs

1

### Pipeline  
inputs

1

## Dimensions

### Width

10 m

### Length

26 m

### Height

36 m

### Area

260 m2

## Fuel

### Supplement  
input rate

45 / min

  * **[](/wiki/Petroleum_Coke "Petroleum Coke")[Petroleum Coke](/wiki/Petroleum_Coke "Petroleum Coke")** \+ [](/wiki/Water "Water") [Water](/wiki/Water "Water")
  * **[](/wiki/Coal "Coal")[Coal](/wiki/Coal "Coal")** \+ [](/wiki/Water "Water") [Water](/wiki/Water "Water")
  * **[](/wiki/Compacted_Coal "Compacted Coal")[Compacted Coal](/wiki/Compacted_Coal "Compacted Coal")** \+ [](/wiki/Water "Water") [Water](/wiki/Water "Water")



## Ingre­dients

**20 ×[](/wiki/Reinforced_Iron_Plate "Reinforced Iron Plate") [Reinforced Iron Plate](/wiki/Reinforced_Iron_Plate "Reinforced Iron Plate")**

**10 ×[](/wiki/Rotor "Rotor") [Rotor](/wiki/Rotor "Rotor")**

**30 ×[](/wiki/Cable "Cable") [Cable](/wiki/Cable "Cable")**

**燃煤發電機** 是一種[發電機](/wiki/Power_generator "Power generator") [建築](/wiki/Building "Building")，通過燃燒[](/wiki/Coal "Coal") [煤炭](/wiki/Coal "Coal")、[](/wiki/Compacted_Coal "Compacted Coal") [壓縮煤炭](/wiki/Compacted_Coal "Compacted Coal")或[](/wiki/Petroleum_Coke "Petroleum Coke") [石油焦](/wiki/Petroleum_Coke "Petroleum Coke")和[](/wiki/Water "Water") [水](/wiki/Water "Water")來產生[電力](/wiki/%E9%9B%BB%E5%8A%9B?action=edit&redlink=1 "電力 \(page does not exist\)")。它是先鋒可以使用的第一個完全自動化的電源，也是第一個使用開採資源的電源。 

一台燃煤發電機在100% [時鐘速度](/wiki/Clock_Speed "Clock Speed") 下可產生75兆瓦的電力。 

## Contents

  * 1 燃料消耗
  * 2 每個煤礦點的發電機數量
  * 3 使用壓縮煤炭的發電機
  * 4 使用石油焦的發電機
  * 5 超頻
  * 6 燃煤發電設置教程
    * 6.1 緊湊佈局
  * 7 外部鏈接
  * 8 另見
  * 9 圖庫
  * 10 歷史



## 燃料消耗

在100%時鐘速度下，一台燃煤發電機消耗45立方米的[水](/wiki/Water "Water")/分鐘，無論使用何種燃料。 

這意味著3個[抽水器](/wiki/Water_Extractor "Water Extractor")將生產足夠的水供8台燃煤發電機使用，前提是Mk.1管道的300立方米每分鐘吞吐量限制未被超過（請參見下文以了解可能的設置）。 

燃料類型 | 能量 (MJ) | 堆疊大小 | **堆疊能量 (MJ)** | 燃燒時間 (秒) | **每分鐘物品數量**  
---|---|---|---|---|---  
[](/wiki/Coal "Coal") [煤炭](/wiki/Coal "Coal") | 300 | 100 | 30,000 | 4 | 15   
[](/wiki/Compacted_Coal "Compacted Coal") [壓縮煤炭](/wiki/Compacted_Coal "Compacted Coal") | 630 | 100 | 63,000 | 8.4 | 7.142857   
[](/wiki/Petroleum_Coke "Petroleum Coke") [石油焦](/wiki/Petroleum_Coke "Petroleum Coke") | 180 | 200 | 36,000 | 2.4 | 25   
  
## 每個煤礦點的發電機數量

使用以下公式： 燃煤發電機數量： `燃煤發電機 = 煤炭開採率 / 15` 抽水器數量： `抽水器 = 燃煤發電機 / 2.6666` 將水供應分散到多條管道上： `管道數量 = 燃煤發電機 / 6.6666`

  * 煤炭燃燒時間為4秒，這意味著一台燃煤發電機消耗15煤炭/分鐘。
  * [Mk.1管道](/wiki/Pipeline#Mk.1 "Pipeline")的容量僅為300立方米每分鐘。因此，當將抽水器連接到供應七台或更多燃煤發電機的管道時，需將水輸入分散或分開。 
    * 或者，將抽水器下調至75%，並將每個抽水器精確連接到兩台燃煤發電機。這樣，抽水器的數量是燃煤發電機數量的一半。
    * 使用下調至75%的抽水器需要為每八台燃煤發電機增加一個額外的抽水器，以空間換取比例的簡單性。對於八台燃煤發電機，需要三個100%工作的抽水器（3 * 20 = 60兆瓦）或四個75%工作的抽水器（4 * 12.6 = 50.4兆瓦）。這在早期節省抽水器的能耗特別有用。
    * 一個抽水器的寬度大約是兩個燃煤發電機的寬度，所以更容易排列佈局。
  * [Mk.2管道](/wiki/Pipeline#Mk.2 "Pipeline")的容量為600立方米每分鐘。因此，一條Mk.2管道最多可連接13台燃煤發電機和5個抽水器。
  * 在純煤炭點上的Mk.3採礦機應僅超頻到163%，以適應Mk.5輸送帶的吞吐量限制。
  * 由於採礦機和抽水器消耗電力，因此淨功率容量較低。 
    * 抽水器使用大約10%的毛功率。從毛功率中減去10%後，再減去[採礦機](/wiki/Miner "Miner")、[管道泵](/wiki/Pipeline_Pump "Pipeline Pump")、[車輛](/wiki/Vehicle "Vehicle")等的功耗，以計算出淨功率產量。



100% 採礦機250% 採礦機

100% [採礦機](/wiki/Miner "Miner") 在 [煤礦](/wiki/Coal "Coal") 點上可支持以下數量的100%功率使用的燃煤發電機（十進制數量的機器意味著最後一台機器需要[降低時鐘速度](/wiki/Underclock "Underclock")以實現最大效率）： 

採礦機 | 礦點  
純度 | 煤炭/分鐘 | [抽水器  
(@ 100%)](/wiki/Water_Extractor "Water Extractor") | [抽水器  
(@ 75%)](/wiki/Water_Extractor "Water Extractor") | 水 m3/min | 燃煤發電機數量 | 毛功率   
---|---|---|---|---|---|---|---  
**Mk.1** | 低純度 | 30 | 0.75 | 1 | 90 | 2 | 150 MW   
中純度 | 60 | 1.5 | 2 | 180 | 4 | 300 MW   
高純度 | 120 | 3 | 4 | 360 | 8 | 600 MW   
**Mk.2** | 低純度 | 60 | 1.5 | 2 | 180 | 4 | 300 MW   
中純度 | 120 | 3 | 4 | 360 | 8 | 600 MW   
高純度 | 240 | 6 | 8 | 720 | 16 | 1200 MW   
**Mk.3** | 低純度 | 120 | 3 | 4 | 360 | 8 | 600 MW   
中純度 | 240 | 6 | 8 | 720 | 16 | 1200 MW   
高純度 | 480 | 12 | 16 | 1440 | 32 | 2400 MW   
  
250% [採礦機](/wiki/Miner "Miner") 在 [煤礦](/wiki/Coal "Coal") 點上可支持以下數量的100%功率使用的燃煤發電機（十進制數量的機器意味著最後一台機器需要[降低時鐘速度](/wiki/Underclock "Underclock")以實現最大效率）： 

採礦機 | 礦點  
純度 | 煤炭/分鐘 | [抽水器  
(@ 100%)](/wiki/Water_Extractor "Water Extractor") | [抽水器  
(@ 75%)](/wiki/Water_Extractor "Water Extractor") | 水 m3/min | 燃煤發電機數量 | 毛功率   
---|---|---|---|---|---|---|---  
**Mk.1** | 低純度 | 75 | 1.875 | 2.5 | 225 | 5 | 375 MW   
中純度 | 150 | 3.75 | 5 | 450 | 10 | 750 MW   
高純度 | 300 | 7.5 | 10 | 900 | 20 | 1500 MW   
**Mk.2** | 低純度 | 150 | 3.75 | 5 | 450 | 10 | 750 MW   
中純度 | 300 | 7.5 | 10 | 900 | 20 | 1500 MW   
高純度 | 600 | 15 | 20 | 1800 | 40 | 3000 MW   
**Mk.3** | 低純度 | 300 | 7.5 | 10 | 900 | 20 | 1500 MW   
中純度 | 600 | 15 | 20 | 1800 | 40 | 3000 MW   
高純度 | 780 ~~1200~~ | 19.5 | 26 | 2340 | 52 | 3900 MW   
  
## 使用壓縮煤炭的發電機

這是上表的簡化版本，對[](/wiki/Compacted_Coal "Compacted Coal") [壓縮煤炭](/wiki/Compacted_Coal "Compacted Coal")作為輸入進行相同計算，因此每分鐘只需要7.143物品而不是15。 

每個製造機以每分鐘25個零件運行。 

煤炭和硫磺/分鐘  | 製造機數量 (@100%)  | 壓縮煤炭/分鐘  | 抽水器 (@100%)  | 燃煤發電機數量  | 毛功率   
---|---|---|---|---|---  
60  | 2.4  | 60  | 3.15  | 8.4  | 630 MW   
120  | 4.8  | 120  | 6.3  | 16.8  | 1260 MW   
240  | 9.6  | 240  | 12.6  | 33.6  | 2520 MW   
480  | 19.2  | 480  | 25.2  | 67.2  | 5040 MW   
780  | 31.2  | 780  | 40.95  | 109.2  | 8190 MW   
  
## 使用石油焦的發電機

燃燒[](/wiki/Petroleum_Coke "Petroleum Coke") [石油焦](/wiki/Petroleum_Coke "Petroleum Coke")來發電是處理[重油殘渣](/wiki/Heavy_Oil_Residue "Heavy Oil Residue")的好方法，只要處理好溢出問題（以防止焦炭堆積，導致重油殘渣堆積，進而導致塑料或橡膠生產停止）。一台燃煤發電機每分鐘消耗25個石油焦。 

由於重油殘渣的量可能因使用的配方而顯著不同，下表僅根據重油殘渣進行計算，而不包括[原油](/wiki/Crude_Oil "Crude Oil")。 

重油殘渣/分鐘 | 焦炭精煉廠數量 | 石油焦/分鐘 | 抽水器(@100%) | 燃煤發電機數量 | 毛功率   
---|---|---|---|---|---  
40 | 1 | 120 | 1.8 | 4.8 | 360 MW   
100 | 2.5 | 300 | 4.5 | 12 | 900 MW   
120 | 3 | 360 | 5.4 | 14.4 | 1080 MW   
200 | 5 | 600 | 9 | 24 | 1800 MW   
260 | 6.5 | 780 | 11.7 | 31.2 | 2340 MW   
300 | 7.5 | 900 | 13.5 | 36 | 2700 MW   
400 | 10 | 1200 | 18 | 48 | 3600 MW   
  
## 超頻

_Main article:_[Clock speed](/wiki/Clock_speed "Clock speed")

The Coal-Powered Generator/zh can be overclocked using [Power Shards](/wiki/Power_Shard "Power Shard"). Overclocking increases the fuel and Water consumption rate and produced power linearly. The same amount of power is always produced from the same input resources. 

## 燃煤發電設置教程

請參閱以下頁面以獲取指南。指南基於[岩石沙漠](/wiki/Rocky_Desert "Rocky Desert")起始區域編寫，但也適用於其他具有四個[煤炭](/wiki/Coal "Coal")節點和[水](/wiki/Water "Water")的區域。 

  * [第一部分](/wiki/Tutorial:How_to_play#Coal_Power "Tutorial:How to play")
  * [第二部分](/wiki/Tutorial:How_to_play#Coal_Power_2 "Tutorial:How to play")
  * [第三部分](/wiki/Tutorial:How_to_play#Coal_Power_3 "Tutorial:How to play")



### 緊湊佈局

由於燃煤發電機體積較大，當在兩排對立的行中建立並由中央[輸送帶](/wiki/Conveyor_Belt "Conveyor Belt")和[管道](/wiki/Pipe "Pipe")供電時，可能很難對齊。然而，當從右到左建造時，它們可以被壓縮到8米（基礎寬度）中心到中心。請確保不使用'吸附'模式，僅使用手動對齊。 

[File:Coal Generator squeezed.png](/wiki/Special:Upload?wpDestFile=Coal_Generator_squeezed.png "File:Coal Generator squeezed.png")

## 外部鏈接

  * [煤炭和燃料發電的深入指南](https://steamcommunity.com/sharedfiles/filedetails/?id=2124946046)



## 另見

  * [](/wiki/Coal "Coal") [煤炭](/wiki/Coal "Coal")
  * [](/wiki/Compacted_Coal "Compacted Coal") [壓縮煤炭](/wiki/Compacted_Coal "Compacted Coal")
  * [](/wiki/Petroleum_Coke "Petroleum Coke") [石油焦](/wiki/Petroleum_Coke "Petroleum Coke")
  * [](/wiki/Water_Extractor "Water Extractor") [抽水器](/wiki/Water_Extractor "Water Extractor")
  * [](/wiki/Biomass_Burner "Biomass Burner") [生質發電機](/wiki/Biomass_Burner "Biomass Burner")
  * [](/wiki/Fuel_Generator "Fuel Generator") [燃料發電機](/wiki/Fuel_Generator "Fuel Generator")
  * [](/wiki/Geothermal_Generator "Geothermal Generator") [地熱發電機](/wiki/Geothermal_Generator "Geothermal Generator")
  * [](/wiki/Nuclear_Power_Plant "Nuclear Power Plant") [核電站](/wiki/Nuclear_Power_Plant "Nuclear Power Plant")



## 圖庫

  * [](/wiki/File:Coal_Generator_Schematic.png "符合8:3比例的常見燃煤發電機設置，沒有吞吐量限制。")

符合8:3比例的常見燃煤發電機設置，沒有吞吐量限制。

  * [](/wiki/File:Coal_generator_pipe_analysis.png "可能的管道設置的流量分析。")

可能的管道設置的流量分析。

  * [](/wiki/File:Coal_power_Water_Extractor.png "三個抽水器供應八台發電機的頂視圖，使用公共管道和兩條Mk.1輸送帶，每條供應四台發電機。這兩條Mk.1輸送帶可以合併成一條Mk.2輸送帶。")

三個抽水器供應八台發電機的頂視圖，使用公共管道和兩條Mk.1輸送帶，每條供應四台發電機。這兩條Mk.1輸送帶可以合併成一條Mk.2輸送帶。

  * [](/wiki/File:Coal_power_ladder.png "從正面看到的幾台燃煤發電機。")

從正面看到的幾台燃煤發電機。

  * [](/wiki/File:Coal_Generator_Manifold_2.png "以雙重歧管方式建造的幾台燃煤發電機。")

以雙重[歧管](/wiki/Manifold "Manifold")方式建造的幾台燃煤發電機。

  * [](/wiki/File:Coal_Power_elevated.png "建在抽水器之上的燃煤發電機。每排有九台發電機，由兩條垂直管道分組供應。底部的兩條垂直管道由三個抽水器供應。第九台發電機有自己的獨立管道和抽水器。")

建在[抽水器](/wiki/Water_Extractor "Water Extractor")之上的燃煤發電機。每排有九台發電機，由兩條垂直管道分組供應。底部的兩條垂直管道由三個抽水器供應。第九台發電機有自己的獨立管道和抽水器。

  * [](/wiki/File:Coal_Generator_old.png "在遊戲的預發布版本中，煤炭運行到燃煤發電機。")

在遊戲的預發布版本中，[煤炭](/wiki/Coal "Coal")運行到燃煤發電機。

  * [](/wiki/File:Coal_Generator_x_16_%2B_Water_Extractor_x_6.png "使用六個抽水器、Mk.2管道和每行一個管道泵設置的16台燃煤發電機，沒有重複線路，也沒有冗餘。")

使用六個抽水器、Mk.2管道和每行一個管道泵設置的16台燃煤發電機，沒有重複線路，也沒有冗餘。




## 歷史

  * [Patch 0.7.1.1](/wiki/Patch_0.7.1.1 "Patch 0.7.1.1"): 修正了將[燃煤發電機](/wiki/Coal_Generator "Coal Generator")放置在藍圖邊緣並仍能連接電源的問題
  * [Patch 0.3.8.2](/wiki/Patch_0.3.8.2 "Patch 0.3.8.2"): 修正了燃煤發電機中的流體指示UI顯示不正確的問題
  * [Patch 0.3](/wiki/Patch_0.3 "Patch 0.3"): 現在需要水來操作，外觀相應更改以包括管道輸入。煙囪現在完全在碰撞箱內。



  * [v](/wiki/Template:BuildingNav "Template:BuildingNav")
  * [e](https://satisfactory.wiki.gg/wiki/Template:BuildingNav?action=edit)
  * [h](https://satisfactory.wiki.gg/wiki/Template:BuildingNav?action=history)

[Buildings](/wiki/Buildings "Buildings")  
---  
Special| [](/wiki/The_HUB "The HUB") [The HUB](/wiki/The_HUB "The HUB") • [](/wiki/MAM "MAM") [MAM](/wiki/MAM "MAM") • [](/wiki/Space_Elevator "Space Elevator") [Space Elevator](/wiki/Space_Elevator "Space Elevator") • [](/wiki/AWESOME_Sink "AWESOME Sink") [AWESOME Sink](/wiki/AWESOME_Sink "AWESOME Sink") • [](/wiki/AWESOME_Shop "AWESOME Shop") [AWESOME Shop](/wiki/AWESOME_Shop "AWESOME Shop") • [](/wiki/Blueprint_Designer "Blueprint Designer") [Blueprint Designer](/wiki/Blueprint_Designer "Blueprint Designer") • [](/wiki/Crafting_Bench "Crafting Bench") [Crafting Bench](/wiki/Crafting_Bench "Crafting Bench") • [](/wiki/Equipment_Workshop "Equipment Workshop") [Equipment Workshop](/wiki/Equipment_Workshop "Equipment Workshop")  
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
