# Clock speed/zh

[](/wiki/File:Cleanup.svg) | **本文可能需要清理以符合质量标准。** 如果可以请帮助[改进](https://satisfactory.wiki.gg/wiki/Clock_speed/zh?action=edit)。[讨论页面](/wiki/Talk:Clock_speed/zh?action=edit&redlink=1 "Talk:Clock speed/zh \(page does not exist\)")可能包含建议。  
原因："_该页面非常详细，因此休闲玩家很难阅读，拆分为：[进阶时钟速度](/wiki/Tutorial:Advanced_clock_speed/zh?action=edit&redlink=1 "Tutorial:Advanced clock speed/zh \(page does not exist\)")_"   
---|---  
  
**This article may need cleanup to meet quality standards.**  
Please help [improve this](https://satisfactory.wiki.gg/wiki/Clock_speed/zh?action=edit) if you can. The [Discussion page](/wiki/Talk:Clock_speed/zh?action=edit&redlink=1 "Talk:Clock speed/zh \(page does not exist\)") may contain suggestions.  
Reason: "_该页面非常详细，因此休闲玩家很难阅读，拆分为：[进阶时钟速度](/wiki/Tutorial:Advanced_clock_speed/zh?action=edit&redlink=1 "Tutorial:Advanced clock speed/zh \(page does not exist\)")_"

## 时钟速度

## Info

### 解锁条件

[能量蛞蝓研究](/wiki/Power_Slugs_Research/zh?action=edit&redlink=1 "Power Slugs Research/zh \(page does not exist\)") \- 超频生产

生产和动力[建筑](/wiki/Buildings/zh "Buildings/zh")，例如[采矿器](/wiki/Miner/zh "Miner/zh")、[构筑站](/wiki/Constructor/zh "Constructor/zh")或[生物质燃烧器](/wiki/Biomass_Burner/zh "Biomass Burner/zh")，可以将其**时钟速度** 设置为 1% 到 250% 之间的任意百分比，精度可达小数点后 4 位。对于生产建筑，这允许它们以大幅减少或增加电力使用量为代价，降低或加快运行速度。对于发电建筑，最大功率输出和相应的燃料消耗可以同步增加，从而使单个建筑发挥更大的效用。超频和降频都可以优化工厂，帮助实现同步生产，提高能源效率，平滑电力消耗的峰值。 

## Contents

  * 1 术语解释
  * 2 解锁
  * 3 用法
    * 3.1 目的
    * 3.2 配置
    * 3.3 精确度
  * 4 生产建筑的时钟速度
    * 4.1 常见的时钟速度
    * 4.2 基本降频
    * 4.3 进阶降频
    * 4.4 索莫晶体降频 ("underslooping"“索降”)
    * 4.5 均衡时钟速度
  * 5 发电机的时钟速度
    * 5.1 燃料燃烧时间公式
    * 5.2 功率容量/燃料消耗速度计算公式
  * 6 采矿机和提取器的时钟速度
    * 6.1 资源井增压站的时钟速度
    * 6.2 Optimization
  * 7 也可以看看
  * 8 画廊
  * 9 历史
  * 10 引用



## 术语解释

**时钟速度** 是指建筑物的运行速度。250% 的时钟速度意味着建筑物的运行速度是原来的 2.5 倍。 

**超频** 是指将时钟速度设置为高于 100%，相反，**降频** 是指将时钟速度设置为低于 100%。降频不需要任何[](/wiki/Power_Shard/zh "Power Shard/zh") [能量碎片](/wiki/Power_Shard/zh "Power Shard/zh"). 

## 解锁

在[](/wiki/MAM/zh "MAM/zh") [MAM研究站](/wiki/MAM/zh "MAM/zh")中可以解锁改变时钟速度的科技。令人困惑的是，这项研究被命名为 “超频生产”，但同时也解锁了低频。 

**[](/wiki/Clock_speed/zh "Clock speed/zh")时钟速度** 是通过[](/wiki/MAM/zh "MAM/zh") [MAM研究站](/wiki/MAM/zh "MAM/zh")利用以下材料研究**[能量碎片研究链](/wiki/%E8%83%BD%E9%87%8F%E7%A2%8E%E7%89%87%E7%A0%94%E7%A9%B6?action=edit&redlink=1 "能量碎片研究 \(page does not exist\)")** 解锁的  
[](/wiki/Power_Shard "Power Shard")1| [](/wiki/Iron_Plate "Iron Plate")50| [](/wiki/Wire "Wire")50  
---|---|---  
  
将时钟速度提高到100%以上所需的[](/wiki/Power_Shard/zh "Power Shard/zh") [能量碎片](/wiki/Power_Shard/zh "Power Shard/zh")可以用[](/wiki/Power_Slug/zh "Power Slug/zh") [能量蛞蝓](/wiki/Power_Slug/zh "Power Slug/zh")制作，[](/wiki/Power_Slug/zh "Power Slug/zh") [能量蛞蝓](/wiki/Power_Slug/zh "Power Slug/zh")可以在[世界](/wiki/World/zh "World/zh")的固定地点找到。在[阶级9](/wiki/Tier_9/zh?action=edit&redlink=1 "Tier 9/zh \(page does not exist\)")后，可以通过人工合成的方式自动生产能量碎片。 

## 用法

### 目的

改变时钟速度有多种原因，其中最常见是为了使工厂生产线以最高效率运行而匹配机器的生产和消耗速度、通过超频节省空间或通过降频节省电力。 

为了匹配生产和消耗速度，超频和降频都是可行的。您可以自行决定是使用[](/wiki/Power_Shard/zh "Power Shard/zh") [能量碎片](/wiki/Power_Shard/zh "Power Shard/zh")进行超频，从而节省一点空间并使用额外的电能，还是反之，使用不需要[](/wiki/Power_Shard/zh "Power Shard/zh") [能量碎片](/wiki/Power_Shard/zh "Power Shard/zh")的降频。 

时钟速度对生产建筑/资源提取器和发电机的影响不同，请参见下文。 

### 配置

时钟速度只能在具有可配置配方、资源提取器和发电机的生产建筑中进行配置。其他耗电设备，如[](/wiki/Hypertube_Entrance/zh "Hypertube Entrance/zh") [超级管道入口](/wiki/Hypertube_Entrance/zh?action=edit&redlink=1 "Hypertube Entrance/zh \(page does not exist\)"), [](/wiki/Pipeline_Pump/zh "Pipeline Pump/zh") [管道泵](/wiki/Pipeline_Pump/zh?action=edit&redlink=1 "Pipeline Pump/zh \(page does not exist\)")或[](/wiki/Train_Station/zh "Train Station/zh") [火车站](/wiki/Train_Station/zh "Train Station/zh")，则无法超频。 

时钟速度可以通过每个建筑用户界面上的菜单进行设置，使用[`E`](/wiki/Controls/zh?action=edit&redlink=1 "Controls/zh \(page does not exist\)")与之交互即可进入。可以在菜单中插入 [](/wiki/Power_Shard/zh "Power Shard/zh") [能量碎片](/wiki/Power_Shard/zh "Power Shard/zh")，每个能量碎片将允许的最高时钟速度提高 50%，最多可提高 3 次。有多种方法可以在该菜单中设置时钟速度： 

  * 拖动滑块，以 1%的增量改变数值。
  * 直接输入百分比或目标生产率。
  * 输入一个公式，类似于使用快速搜索 [`N`](/wiki/Controls/zh?action=edit&redlink=1 "Controls/zh \(page does not exist\)") 访问[游戏内计算器](/wiki/Controls/zh?action=edit&redlink=1 "Controls/zh \(page does not exist\)")，该公式将从左到右进行计算。



此外，配方和时钟速度配置可以通过 [`Ctrl`](/wiki/Controls/zh?action=edit&redlink=1 "Controls/zh \(page does not exist\)")+[`C`](/wiki/Controls/zh?action=edit&redlink=1 "Controls/zh \(page does not exist\)") 进行复制，也可以通过 [`Ctrl`](/wiki/Controls/zh?action=edit&redlink=1 "Controls/zh \(page does not exist\)")+[`V`](/wiki/Controls/zh?action=edit&redlink=1 "Controls/zh \(page does not exist\)") 在同类型建筑之间进行粘贴。如果需要 [](/wiki/Power_Shard/zh "Power Shard/zh") [能量碎片](/wiki/Power_Shard/zh "Power Shard/zh")，且[库存](/wiki/Inventory/zh?action=edit&redlink=1 "Inventory/zh \(page does not exist\)")中有足够的[](/wiki/Power_Shard/zh "Power Shard/zh") [能量碎片](/wiki/Power_Shard/zh "Power Shard/zh")，则会自动将其插入建筑物中。 

如果降频建筑的工作耗电量低于 0.1 兆瓦的空闲耗电量，空闲时仍将使用 0.1 兆瓦的耗电量。[1]

### 精确度

结果配置始终以百分比形式存储，精度为小数点后四位。内部使用根据配置的时钟速度计算出的精确值。但是，用户界面通常会对数值进行四舍五入或截断，从而列出不准确的结果。 

例如，[](/wiki/Constructor/zh "Constructor/zh") [构筑站](/wiki/Constructor/zh "Constructor/zh")每分钟产生 15 个 [](/wiki/Concrete/zh "Concrete/zh") [混凝土](/wiki/Concrete/zh "Concrete/zh") 时，永远无法精确设置为每分钟产生 5 个。最接近 33.3333% 的时钟速度将产生 15 × 0.333333 = 4.999995/min 的速度，尽管用户界面将其四舍五入为精确的 5/min 。 

对于大多数玩家来说，这种程度的误差可以忽略不计；减少无限重复小数的方法之一是使用所谓的**45-81规则** 如果配方的生产率是 45/min 或 81/min 的倍数或分数，则其时钟速度可能不会出现重复小数。81 适用于大多数油类配方，45 适用于大多数其他配方。这并不适用于所有配方。 

例如，使用“稀释 + 再生循环”时，[](/wiki/Plastic/zh "Plastic/zh") [塑料](/wiki/Plastic/zh?action=edit&redlink=1 "Plastic/zh \(page does not exist\)")的生产速度不要设计为 100/分钟，而是 81 + 20.25 = 101.25/分钟。 

## 生产建筑的时钟速度

生产建筑的制作速度与其时钟速度成正比，但其耗电量却以 N=1.321928 的指数变化。随着物品生产速度的提高，原料消耗速度也随之提高。这意味着使用时钟速度较高的建筑生产相同数量的资源需要消耗更多的电力，但却节省了空间。 

下表显示了[](/wiki/Constructor/zh "Constructor/zh") [构筑站](/wiki/Constructor/zh "Constructor/zh")生产[](/wiki/Iron_Rod/zh "Iron Rod/zh") [铁棒](/wiki/Iron_Rod/zh?action=edit&redlink=1 "Iron Rod/zh \(page does not exist\)")时的五种不同时钟速度。 

[](/wiki/File:Clock_speed_power_consumption_graph.png)

[](/wiki/File:Clock_speed_power_consumption_graph.png "Enlarge")

基于时钟速度的每次制作的功耗比。该比率是与默认时钟速度下每次制作的耗电量进行比较。这仅适用于生产建筑。发电机超频是线性的

时钟速度 | 制作时间 | 消耗的电力 | 每根铁棒的能量   
---|---|---|---  
10% | 40s | 0.19 兆瓦 | 7.62 兆焦 | 47.6%   
50% | 8s | 1.6 兆瓦 | 12.8 兆焦 | 80%   
100% (默认) | 4s | 4 兆瓦 | 16 兆焦 | 100%   
150% | 2.67s | 6.8兆瓦 | 18.2 兆焦 | 113.9%   
200% | 2s | 10 兆瓦 | 20 兆焦 | 125%   
250% | 1.6s | 13.4 兆瓦 | 21.5 兆焦 | 134.3%   
  
[](/wiki/File:Overclocking_at_999.jpg)

[](/wiki/File:Overclocking_at_999.jpg "Enlarge")

超频值可任意设定，但游戏会自动将其限制在 1% 到 250% 之间。

电力消耗的公式是： 

power usage=initial power usage×(clock speed100)1.321928 其中power usage是实际功率、initial power usage是默认功率，clock speed是时钟速度   
---  
  
其中， _时钟速度_ 是一个在 1 到 250 之间最多有 4 位小数的数字，而 _实际功率_ 和 _默认功率_ 均以兆瓦为单位。 

指数 1.321928 是向下舍入的 log2(2.5)，这意味着你需要 2.5 倍的功率才能将生产速度提高一倍，这适用于任何时钟速度。 

对于每个生产项目的相对能源使用量，请将指数系数减去 1，即 

energy usage=initial energy usage×(clock speed100)0.321928 其中energy usage是实际能量消耗、initial energy usage是默认能量消耗，clock speed是时钟速度   
---  
  
请注意，实际功率的大小还会受到[生产增幅](/wiki/Production_amplification/zh?action=edit&redlink=1 "Production amplification/zh \(page does not exist\)")的进一步影响。 

  


### 常见的时钟速度

  * 在 59% 时钟速度 （59.1943）下，你的耗电量减少了一半，但你仍能生产 59% 的物品，因此，在相同耗电量的情况下，增加一个 59% 建筑，你将比单个 100% 建筑多生产 18% 的物品。
  * 在 169% 时钟速度（168.9353）下，你的耗电量等于 2 个 100% 建筑的耗电量，但你生产的物品数量会减少 169/200≈16%。
  * 在230%的时钟速度（229.5770）下，你的耗电量等于3个100%建筑的耗电量，但你将会生产230/300≈23%更少的物品。
  * 在最高时钟速度（250）下，你的耗电量等于 3.36 个 100% 建筑的耗电量，但你将会生产 250/336≈26% 更少的物品。



### 基本降频

电力是任何工厂的重要组成，一些基本的降频可以帮助您减少电力的使用。 

如果将一个时钟速度为 100% 的建筑换成两个时钟速度为 50% 的建筑，产率将保持不变，但耗电量将减少 20%。 

计算方法如下： 

每个 50%的建筑将使用100×(50100)1.321928≈40%，约为默认功率的 40%，2 座建筑为 80%，因此你将节省 20% 的电力消耗。 

将生产平均分配给更多的建筑，可以节省更多的电力，但随着建筑数量的增加，收益也会越来越少： 

建筑数量 | 时钟速度 | 功率消耗 | 备注   
---|---|---|---  
1 | 100 | 100% |   
2 | 50 | 80% | -20% 最大收益是增建一栋建筑   
3 | 33.3333 | 70.21% | -9.79% 再增建一栋建筑   
4 | 25 | 64% | -6.21%   
5 | 20 | 59.56% | -4.44%   
  
本例使用的基本时钟速度为 100%，但您也可以使用不同的时钟速度。 将产量平均分配给 2 座建筑，总能节省 20% 的电能，而且 n 座建筑也能节省相同的电能。 

降频还能节省[](/wiki/Power_Shard/zh "Power Shard/zh") [能量碎片](/wiki/Power_Shard/zh "Power Shard/zh")，而能量碎片最适合用于发电机、采矿机和提取机（见下文），因此当你的某些建筑的时钟速度高于100%时，超频的收益会更高。例如 

建筑数量 | 时钟速度 | 功率消耗 | 功率消耗比 | 备注   
---|---|---|---|---  
1 | 250 | 335.77% | 100% | 需要3个能量碎片   
2 | 125 | 268.62% | 80% | -20% 功率消耗，且少需要1个能量碎片   
3 | 83.3333 | 235.75% | 70.21% | 几乎 -30% 功率消耗且不需要能量碎片   
  
  
总之，这种方法可以在降低功耗的同时保持产量，但还有一种更先进的降频方法，可以在保持相同功耗的情况下提高产量。 

### 进阶降频

以下设置的耗电量相同： 

建筑数量 | 时钟速度% | 产率 | 备注   
---|---|---|---  
1 | 100.0000 | 100% |   
2 | 59.1943 | 118% | +18% 最大收益是增建一栋建筑   
3 | 43.5584 | 131% | +13% 再增建一栋建筑   
4 | 35.0396 | 140% | +9%   
5 | 29.5971 | 148% | +8%   
10 | 17.5198 | 175% | 10 可能不是很值得   
100 | 3.0694 | 307% | 祝你好运   
440 | 1.0007 | 440% | 你真闲   
441 | 0.9990 | - | 时钟速度不能设置小于 1%   
  
您必须在拥有多座建筑的后勤复杂性与生产收益之间取得平衡。 

为清楚起见，上表中的产量以四舍五入的方式表示，但精确值可使用以下公式计算： 

n 栋建筑的时钟速度： 

clock speed=base clock speed×exp⁡(−ln⁡(n)1.321928) 其中clock speed是时钟速度、base clock speed是基本时钟速度，exp是自然指数函数   
---  
  
n 栋建筑的产率： 

production=n×clock speed 其中production是产率，clock speed是时钟速度   
---  
  
在上表中， _基本时钟速度_ = 100，但您可以在公式中使用 1 到 250 之间的任何基本时钟速度，这样您就可以在保持相同功率使用的情况下对任何建筑进行降频，并获得无需额外能量的生产。 

与基本时钟速度相比，n建筑物的生产收益始终相同。例如，基础时钟速度为 250： 

建筑数量 | 时钟速度% | 产率 | 备注   
---|---|---|---  
1 | 250.0000 | 250% | 需要3个能量碎片   
2 | 147.9856 | 296% | 同样的生产增益 118%（减少一个能量碎片）   
3 | 108.8959 | 327% | 同样的生产增益 131%（与默认相比）   
4 | 87.5990 | 350% | 同样的生产增益 140% （而且不需要能量碎片）   
  
有关此技巧的其他说明： 

  * 新增的生产无需电力，但显然不是无需原料，您必须有足够的资源来支持它。
  * 如果当前生产线不需要额外增加产量，你可以使用[](/wiki/Smart_Splitter/zh "Smart Splitter/zh") [智能分流器](/wiki/Smart_Splitter/zh?action=edit&redlink=1 "Smart Splitter/zh \(page does not exist\)")将多余的产量传送到另一条生产线，或放入[](/wiki/AWESOME_Sink/zh "AWESOME Sink/zh") [AWESOME 回收器](/wiki/AWESOME_Sink/zh "AWESOME Sink/zh")，或放入一个绿色的[](/wiki/Storage_Container/zh "Storage Container/zh") [存储容器](/wiki/Storage_Container/zh?action=edit&redlink=1 "Storage Container/zh \(page does not exist\)")，并在上面贴上足够的 “环保”[](/wiki/Display_Sign/zh "Display Sign/zh") [标志](/wiki/Display_Sign/zh?action=edit&redlink=1 "Display Sign/zh \(page does not exist\)")。



  


### 索莫晶体降频 ("underslooping"“索降”)

[](/wiki/Somersloop "Somersloop") [索莫晶体](/wiki/Somersloop "Somersloop")可以用于[生产增幅](/wiki/Production_amplification/zh?action=edit&redlink=1 "Production amplification/zh \(page does not exist\)")，因此在降频的建筑中使用它们似乎有违直觉，但如果你需要生产一种资源不足的物品，这种技巧就非常有用了。 

当所有的索莫晶体插槽都被填满时，建筑物的耗电量会增加 4 倍，但同样的输入却能多生产出 2 倍的物品，因此如果将时钟速度设置为 50%，那么只需一半的资源和 60% 的耗电量就能以 100% 的速度生产出所需物品（关于耗电量计算公式，请参阅[生产增幅](/wiki/Production_amplification/zh?action=edit&redlink=1 "Production amplification/zh \(page does not exist\)")）。 

通过“索降”可以获得不同的结果，下表对此进行了总结： 

时钟速度% | 产率 | 功率消耗 | 备注   
---|---|---|---  
35.0396 | 70.0792 | 100 | 将耗电量保持在 100%，您可以用 35% 的资源生产 70% 的物品   
50 | 100 | 160 | 只需增加 60% 的能量，就能以 50% 的资源生产 100% 的物品   
59.1943 | 118.3885 | 200 | 功率提高 2 倍，就能以 59% 的资源生产 118% 的物品   
80.4429 | 160.8857 | 300 | 功率提高 3 倍，就能以 80% 的资源生产 160% 的物品   
100 | 200 | 400 | 基础数据：增加 4 倍能量，就能以 100% 的资源生产 2 倍的物品   
  
如果使用索莫晶体时耗电量过高，也可以使用基本降频中解释的技巧。例如，如果你将一个时钟速度为100%的装有索莫晶体的建筑替换为 2 个时钟速度为 50%的装有索莫晶体建筑，你的产量将保持不变，但你的耗电量将是 160+160=320% 而不是 400%，因此你将获得 320/400=20% 的电力。不过，这需要额外的索莫晶体，而且数量有限。 

### 均衡时钟速度

为了优化功耗，最好是均衡时钟速度，而不是在同一条生产线上使用不同的时钟速度。 

例如，如果你有两台[](/wiki/Blender/zh "Blender/zh") [混料站](/wiki/Blender/zh?action=edit&redlink=1 "Blender/zh \(page does not exist\)")，一台设置为100%，另一台设置为50%，那么它们需要75+30=105 MW，如果将它们都设置为(100+50)/2=75% ，那么它们只需要2×51.27≈102.5 MW。 

均衡可以节省[](/wiki/Power_Shard "Power Shard") [能量碎片](/wiki/Power_Shard "Power Shard")。(150%+50%->100%+100%，你将获得一个能量碎片），但如果产生的时钟速度高于100%（例如150%+100%->125%+125%），均衡也可能需要更多的能量碎片。在这种情况下，可以通过增加生产建筑来解决问题。 

## 发电机的时钟速度

发电装置的发电量和燃料消耗量都与其时钟速度成正比。其时钟速度每提高 1%，就会多产生 1%的功率，多消耗 1%的燃料。相同数量的燃料总是能产生相同数量的电能。因此，超频发电机只是节省了空间，但对于大型发电站来说，可能会耗费大量的[](/wiki/Power_Shard/zh "Power Shard/zh") [能量碎片](/wiki/Power_Shard/zh "Power Shard/zh")。 

下表详细列出了以[](/wiki/Coal/zh "Coal/zh") [煤炭](/wiki/Coal/zh "Coal/zh")为燃料的[](/wiki/Coal_Generator/zh "Coal Generator/zh") [煤炭发电机](/wiki/Coal_Generator/zh "Coal Generator/zh")的发电速率。同样的逻辑适用于所有其他发电机，但不包括[](/wiki/Geothermal_Generator/zh "Geothermal Generator/zh") [地热发电机](/wiki/Geothermal_Generator/zh?action=edit&redlink=1 "Geothermal Generator/zh \(page does not exist\)")，因为后者根本无法超频。 

时钟速度 | 煤炭燃烧时间 | 每分钟消耗煤炭 | 每块煤炭的能量 | 发电速度   
---|---|---|---|---  
10% | 40 秒 | 1.5 | 300 兆焦 | 7.5 兆瓦 | 10%   
100% (默认) | 4 秒 | 15 | 300 兆焦 | 75 兆瓦 | 100%   
250% | 1.6 秒 | 37.5 | 300 兆焦 | 187.5 兆瓦 | 250%   
  
### 燃料燃烧时间公式

fuel burn time=initial fuel burn time×100clock speed 其中fuel burn time是燃料燃烧时间，initial fuel burn time是默认燃料燃烧时间，clock speed时钟速度   
---  
  
  
_时钟速度_ 是一个在到1到250之间且有4位小数精度的数字， _燃料燃烧时间_ 和 _默认燃料燃烧时间_ 都以秒为单位。 

### 功率容量/燃料消耗速度计算公式

power capacity=initial power capacity×clock speed100 其中power capacity是功率容量，initial power capacity是默认功率容量，clock speed时钟速度   
---  
  
  
_时钟速度_ 是一个在到1到250之间且有4位小数精度的数字， _默认功率容量_ 和 _功率容量_ 都以兆瓦为单位。 把 _功率容量_ 和 _默认功率容量_ 替换为 _燃料燃烧速度_ 和 _默认燃料燃烧速度_ ，并以分/分钟或立方米/分钟为单位计算，可算出燃料消耗速度。 

## 采矿机和提取器的时钟速度

超频[](/wiki/Miner/zh "Miner/zh") [采矿机](/wiki/Miner/zh "Miner/zh")和[油井](/wiki/Oil_Extractor/zh "Oil Extractor/zh")是很有益的，因为它可以让你在每个资源点上榨取更多的矿石/石油。就每提取一个矿石/石油所需的能量而言，在纯度较高的资源点上使用超频的采矿机/提取器也比在纯度较低的资源点上使用未超频的采矿机/提取器效率更高。将能源效率定义为开采每块矿石或石油所需的能量： 

  * 以 250% 的纯度开采一个纯净资源点与以 78.74% 的纯度开采一个正常资源点或以 24.80% 的纯度开采一个不纯资源点具有相同的能源效率。
  * 以 250% 的纯度开采一个普通资源点的能源效率与以 78.74% 的纯度开采一个不纯资源点的能源效率相同。



一般地说，将资源点纯度提高一级，同时将时钟速度提高 25/3≈3.175，从而获得相同的能源效率（开采每块矿石或石油所需的能量）。 

由于在时钟速度相同的情况下，纯度较高的资源点提取每块矿石或油所需的能量要少得多，因此减少与提取相关的功耗的简单策略是： 

  1. 在从普通资源点提取任何东西之前，先完全超频纯净资源点
  2. 在从不纯资源点提取任何东西之前，先让正常资源点完全超频。



更优化的方法将在下文详述，但相对于这一简单策略而言，所节省的电力通常并不多。 

### 资源井增压站的时钟速度

_主要文章:_[资源井增压站](/wiki/Resource_Well_Pressurizer "Resource Well Pressurizer")

### Optimization

当你有足够多的资源点来满足你的开采要求时,_最_ 省电的开采矿石或石油的方法就是从纯净资源点开采大量矿石或石油，从正常资源点开采适量矿石或石油，从不纯净资源点开采少量矿石或石油，这样所有资源点开采每块矿石或石油的能效都是一样的。假设你开采： 

  * np 个纯净资源点
  * nn 个正常资源点
  * ni 个不纯净资源点



并且您将用提取器提取每个资源点，设其基本提取率为 _B_ ，可以用下表概括： 

提取器 | 基本提取速率, B  
---|---  
1级采矿机 | 60 矿石/分钟   
2级采矿机 | 120 矿石/分钟   
3级采矿机 | 240 矿石/分钟   
油井 | 120 原油/分钟   
  
如果您的目标提取率是每分钟 X矿石或石油，则最节能的时钟速度可按以下方式计算： 

  1. 计算上述简单方法（先超频高纯度，再使用低纯度）所需的功耗。这是对完全优化时钟速度所能节省的功耗的乐观上限--你觉得是不是很多？如果不是，那就不应该费心进行优化。 
  2. 设c 为:  c=XB(2⋅np+2−5/3⏟≈0.315⋅nn+2−13/3⏟≈0.0496⋅ni)  
---  
  3. 假设没有传送带或时钟限制，理想的时钟速度为 
     * 100%⋅c ，对于每个纯净资源点
     * 100%⋅c/25/3≈31.5%⋅c ，对于每个正常资源点
     * 100%⋅c/210/3≈9.92%⋅c ，对于每个不纯净资源点
遗憾的是，这个工作点并不总能实现，原因如下： 
     * 它要求纯净资源点提取器的运行时钟速度超过 250%
     * 要求纯净资源点提取器超过 600 流体/分钟的2级管道限制
在这种情况下，应将纯净资源点提取器设置为最高可用时钟速度（对于使用6级传送带的3级采矿机和使用 2级管道的油井，时钟速度应为 250%），然后重复该算法，以确定如何最好地使用正常资源点和不纯净资源点来采集剩余的矿石或石油。如果第二种解决方案要求将正常提取器的时钟频率设置为 250% 以上，那么就应该将正常提取器的时钟频率设置为 250%，而将不纯提取器的时钟速度设置为收集矿石或石油平衡所需的任何速度。如果这也需要超过 250% 的时钟频率，那么对于给定资源点来说，X 太高了。 




例如，如果您想从 2 个纯净资源点、3 个正常资源点和 5 个不纯净资源点的组合中提取 1800 石油，那么 

  * B=120 原油/分钟，使用1台油井
  * np=2, nn=3, 和ni=5
  * X=1800 原油/分钟
  * 要达到这一提取速度，简单的方法是对两个纯净资源点进行完全超频（1200 原油/分钟），然后只对两个普通资源点进行挖掘和完全超频（600 原油/分钟）。这将需要 4 个完全超频的油井，消耗 693.14 兆瓦。因此，这是最乐观的节电上限。虽然这只是 “乐观 ”估计，实际节省的功率可能会更低，但这似乎是值得的。
  * 计算得到 c=2.889, 于是 
    * 纯净资源点提取器的运行速度应为 288.9%。这超过了 250%，因此我们必须假定 2 台纯净资源点提取器的运行率为 250%，总产量为 1200 原油/分钟。
    * 第二步计算，我们重复 np=𝟎, nn=3, ni=5, X=𝟔𝟎𝟎 原油/分钟. 计算出 c=4.19, 于是 
      * 正常资源点应以 132.0% 的速度运行
      * 不纯资源点应以 41.58% 的速度运行



这将需要 582.83 兆瓦，节省 110.3 兆瓦。 

## 也可以看看

  * [生产增幅](/wiki/Production_amplifier/zh?action=edit&redlink=1 "Production amplifier/zh \(page does not exist\)")



## 画廊

  * [](/wiki/File:Underclocking_tutorial.png "一台降频的构筑站。可以输入百分比、每分钟项目或使用滑块调整数值。")

一台降频的[构筑站](/wiki/Constructor/zh "Constructor/zh")。可以输入百分比、每分钟项目或使用滑块调整数值。

  * [](/wiki/File:Overclocking_tutorial.png "一台超频的采矿机。需要能量碎片来超频到超过100%")

一台超频的[采矿机](/wiki/Miner/zh "Miner/zh")。需要[能量碎片](/wiki/Power_Shard/zh "Power Shard/zh")来超频到超过100%




## 历史

[](/wiki/File:Icon-boilerplate.png) | 本文的历史部分不完整。如果可以，请帮助[编辑扩展它](https://satisfactory.wiki.gg/wiki/Clock_speed/zh?action=edit)。信息可从[版本&补丁](/wiki/Category:Patch_notes "Category:Patch notes")中收集。   
---|---  
  
  * [Patch 0.8.2.0](/wiki/Patch_0.8.2.0 "Patch 0.8.2.0"): 修复了超频时手动输入文本后键盘输入丢失的问题
  * [Patch 0.7.0.0](/wiki/Patch_0.7.0.0 "Patch 0.7.0.0")
    * 将超频生产建筑（包括提取器）的能源成本降至较低指数 
      * 将生产建筑和提取器指数从 1.6 改为 1.321928
    * 使发电机的超频操作速率与时钟速度相匹配 
      * 超频的基本机制基本保持不变，但降低了功率成本的指数变化。这意味着超频的成本比以前低，而降频的成本则不那么低。
      * 发电机是唯一的例外： 它们的超频和降频完全是线性的。
  * [Patch 0.6.1.1](/wiki/Patch_0.6.1.1 "Patch 0.6.1.1")
    * 超频现在有了一个可见的文本框，可以手动输入百分比或数字
    * 在下一个制作周期应用新的超频之前，制造建筑现在应预览每个输入和输出的每分钟超频统计数据
  * [Patch 0.4.0.4](/wiki/Patch_0.4.0.4 "Patch 0.4.0.4"): 修复了在某些情况下粘贴设置时超频无法显示正确值的问题
  * [Patch 0.4.0.3](/wiki/Patch_0.4.0.3 "Patch 0.4.0.3"): 超频中的小数点精度由 1 改为 4
  * [Patch 0.4.0.0](/wiki/Patch_0.4.0.0 "Patch 0.4.0.0"): 现在可以将十进制百分比设置为时钟速度，游戏不再将其四舍五入为最接近的整数百分比



## 引用

  1. ↑ [Satisfactory Wiki - August 1st, 2021 - Underlocked-below-idle-power-while-active.webp](/wiki/File:Underlocked-below-idle-power-while-active.webp "File:Underlocked-below-idle-power-while-active.webp")



  * [v](/wiki/Template:PioneerNav "Template:PioneerNav")
  * [e](https://satisfactory.wiki.gg/wiki/Template:PioneerNav?action=edit)
  * [h](https://satisfactory.wiki.gg/wiki/Template:PioneerNav?action=history)

[幸福工厂](/wiki/Satisfactory/zh "Satisfactory/zh") 游戏机制  
---  
玩家能力| [百科](/wiki/Codex/zh?action=edit&redlink=1 "Codex/zh \(page does not exist\)") • [资源扫描器](/wiki/Resource_Scanner/zh?action=edit&redlink=1 "Resource Scanner/zh \(page does not exist\)") • [建造枪](/wiki/Build_Gun/zh "Build Gun/zh") • [库存](/wiki/Inventory/zh?action=edit&redlink=1 "Inventory/zh \(page does not exist\)") • [生命](/wiki/Health/zh?action=edit&redlink=1 "Health/zh \(page does not exist\)") • [战斗](/wiki/Combat/zh?action=edit&redlink=1 "Combat/zh \(page does not exist\)") • [移动](/wiki/Movement/zh?action=edit&redlink=1 "Movement/zh \(page does not exist\)") • [手电筒](/wiki/Flashlight/zh?action=edit&redlink=1 "Flashlight/zh \(page does not exist\)") • [HUD](/wiki/HUD/zh?action=edit&redlink=1 "HUD/zh \(page does not exist\)") • [箱子](/wiki/Crate/zh?action=edit&redlink=1 "Crate/zh \(page does not exist\)") • [待办事项列表](/wiki/To-Do_List/zh?action=edit&redlink=1 "To-Do List/zh \(page does not exist\)")  
可解锁的能力| [配方](/wiki/Recipes/zh?action=edit&redlink=1 "Recipes/zh \(page does not exist\)") • [电力](/wiki/Power/zh "Power/zh") • 超频、降频 • [生产增幅](/wiki/Production_amplifier/zh?action=edit&redlink=1 "Production amplifier/zh \(page does not exist\)") • [定制器](/wiki/Customizer/zh "Customizer/zh") • [地图](/wiki/Map/zh?action=edit&redlink=1 "Map/zh \(page does not exist\)") • [生产力显示](/wiki/Productivity_Display/zh?action=edit&redlink=1 "Productivity Display/zh \(page does not exist\)") • [扬程](/wiki/Head_lift/zh "Head lift/zh") • [蓝图](/wiki/Blueprints/zh?action=edit&redlink=1 "Blueprints/zh \(page does not exist\)") • [燃料](/wiki/Category:Fuels "Category:Fuels") • [高产包包乐豪华版](/wiki/FICSIT_Productive_Packer_Deluxe/zh?action=edit&redlink=1 "FICSIT Productive Packer Deluxe/zh \(page does not exist\)")  
流程| [剧情](/wiki/Codex/Story/zh?action=edit&redlink=1 "Codex/Story/zh \(page does not exist\)") • [降落仓](/wiki/Drop-pod/zh?action=edit&redlink=1 "Drop-pod/zh \(page does not exist\)") • [入职培训](/wiki/Onboarding/zh?action=edit&redlink=1 "Onboarding/zh \(page does not exist\)") • [里程碑](/wiki/Milestones/zh?action=edit&redlink=1 "Milestones/zh \(page does not exist\)") • [MAM研究站](/wiki/MAM/zh "MAM/zh") • [替代配方|](/wiki/Hard_Drive#Alternate_recipes/zh "Hard Drive") • [太空电梯](/wiki/Space_Elevator/zh "Space Elevator/zh") • [AWESOME 回收站](/wiki/AWESOME_Sink/zh "AWESOME Sink/zh") • [AWESOME 商店](/wiki/AWESOME_Shop/zh?action=edit&redlink=1 "AWESOME Shop/zh \(page does not exist\)") • [FICSMAS](/wiki/FICSMAS/zh?action=edit&redlink=1 "FICSMAS/zh \(page does not exist\)")  
环境| [世界](/wiki/World/zh "World/zh") • [资源节点](/wiki/Resource_node/zh?action=edit&redlink=1 "Resource node/zh \(page does not exist\)") • [资源井](/wiki/Resource_well/zh?action=edit&redlink=1 "Resource well/zh \(page does not exist\)") • [资源可再生性](/wiki/Resource_renewability/zh?action=edit&redlink=1 "Resource renewability/zh \(page does not exist\)") • [坠机点](/wiki/Crash_Site/zh?action=edit&redlink=1 "Crash Site/zh \(page does not exist\)") • [辐射](/wiki/Radiation/zh?action=edit&redlink=1 "Radiation/zh \(page does not exist\)") • [毒气](/wiki/Poison_Gas/zh?action=edit&redlink=1 "Poison Gas/zh \(page does not exist\)") • [破裂的巨石](/wiki/Cracked_boulder/zh?action=edit&redlink=1 "Cracked boulder/zh \(page does not exist\)") • [洞穴](/wiki/Cave/zh?action=edit&redlink=1 "Cave/zh \(page does not exist\)")  
游玩| [控制](/wiki/Controls/zh?action=edit&redlink=1 "Controls/zh \(page does not exist\)") • [设置](/wiki/Settings/zh?action=edit&redlink=1 "Settings/zh \(page does not exist\)") • [未来内容](/wiki/Future_content/zh?action=edit&redlink=1 "Future content/zh \(page does not exist\)") • [社区资源](/wiki/Community_resources/zh?action=edit&redlink=1 "Community resources/zh \(page does not exist\)") • [进阶游戏设置](/wiki/Advanced_Game_Settings/zh?action=edit&redlink=1 "Advanced Game Settings/zh \(page does not exist\)") • [缩写词](/wiki/Acronyms/zh?action=edit&redlink=1 "Acronyms/zh \(page does not exist\)") • [成就](/wiki/Achievements/zh?action=edit&redlink=1 "Achievements/zh \(page does not exist\)") • [复活节彩蛋](/wiki/Easter_eggs/zh?action=edit&redlink=1 "Easter eggs/zh \(page does not exist\)") • [游戏菜单](/wiki/Game_menus/zh?action=edit&redlink=1 "Game menus/zh \(page does not exist\)") • [指示灯](/wiki/Indicator_Light/zh?action=edit&redlink=1 "Indicator Light/zh \(page does not exist\)") • [多人游戏](/wiki/Multiplayer/zh?action=edit&redlink=1 "Multiplayer/zh \(page does not exist\)") • [音乐](/wiki/Music/zh?action=edit&redlink=1 "Music/zh \(page does not exist\)")  
技术| [控制台](/wiki/Console/zh?action=edit&redlink=1 "Console/zh \(page does not exist\)") • [启动参数](/wiki/Launch_arguments/zh?action=edit&redlink=1 "Launch arguments/zh \(page does not exist\)") • [保存文件](/wiki/Save_files/zh?action=edit&redlink=1 "Save files/zh \(page does not exist\)") • [系统需求](/wiki/System_requirements/zh "System requirements/zh") • [计量单位](/wiki/Units/zh?action=edit&redlink=1 "Units/zh \(page does not exist\)") • [虚幻引擎](/wiki/Unreal_Engine/zh?action=edit&redlink=1 "Unreal Engine/zh \(page does not exist\)")  
指引和教程| | 基本| [如何游玩](/wiki/Tutorial:How_to_play/zh?action=edit&redlink=1 "Tutorial:How to play/zh \(page does not exist\)") • [基本生产线](/wiki/Tutorial:Production_line/zh?action=edit&redlink=1 "Tutorial:Production line/zh \(page does not exist\)") • [进阶生产线](/wiki/Tutorial:Production_line_design_tips/zh?action=edit&redlink=1 "Tutorial:Production line design tips/zh \(page does not exist\)") • [选择替代配方](/wiki/Tutorial:Picking_an_alternate_recipe/zh?action=edit&redlink=1 "Tutorial:Picking an alternate recipe/zh \(page does not exist\)") • [分布式](/wiki/Tutorial:Decentralization/zh?action=edit&redlink=1 "Tutorial:Decentralization/zh \(page does not exist\)") • [铝锭生产](/wiki/Tutorial:Setting_up_Aluminum_Ingot_production/zh?action=edit&redlink=1 "Tutorial:Setting up Aluminum Ingot production/zh \(page does not exist\)")  
---|---  
物流| [歧管](/wiki/Manifold/zh?action=edit&redlink=1 "Manifold/zh \(page does not exist\)") • [平衡](/wiki/Balancer/zh?action=edit&redlink=1 "Balancer/zh \(page does not exist\)") • [管道歧管](/wiki/Pipeline_manifold/zh?action=edit&redlink=1 "Pipeline manifold/zh \(page does not exist\)") • [素数分离器阵列](/wiki/Tutorial:Prime_splitter_arrays/zh?action=edit&redlink=1 "Tutorial:Prime splitter arrays/zh \(page does not exist\)") • [火车](/wiki/Tutorial:Trains/zh?action=edit&redlink=1 "Tutorial:Trains/zh \(page does not exist\)") • [列车吞吐量](/wiki/Tutorial:Train_throughput/zh?action=edit&redlink=1 "Tutorial:Train throughput/zh \(page does not exist\)")  
专用服务器| [专用服务器](/wiki/Dedicated_servers/zh?action=edit&redlink=1 "Dedicated servers/zh \(page does not exist\)") • [如何运作服务器](/wiki/Dedicated_servers/Running_as_a_Service/zh?action=edit&redlink=1 "Dedicated servers/Running as a Service/zh \(page does not exist\)") • [配置文件](/wiki/Dedicated_servers/Configuration_files/zh?action=edit&redlink=1 "Dedicated servers/Configuration files/zh \(page does not exist\)") • [自动更新](/wiki/Dedicated_servers/Automatic_updates/zh?action=edit&redlink=1 "Dedicated servers/Automatic updates/zh \(page does not exist\)") • [HTTPS API](/wiki/Dedicated_servers/HTTPS_API/zh?action=edit&redlink=1 "Dedicated servers/HTTPS API/zh \(page does not exist\)") • [轻量级查询API](/wiki/Dedicated_servers/Lightweight_Query_API/zh?action=edit&redlink=1 "Dedicated servers/Lightweight Query API/zh \(page does not exist\)")  
其他| [超级大炮](/wiki/Tutorial:Hypertube_cannon/zh?action=edit&redlink=1 "Tutorial:Hypertube cannon/zh \(page does not exist\)") • [超级管道刹车](/wiki/Tutorial:Hypertube_brake/zh?action=edit&redlink=1 "Tutorial:Hypertube brake/zh \(page does not exist\)") • [Steam Deck 和控制器设置](/wiki/Tutorial:Controller_setup/zh?action=edit&redlink=1 "Tutorial:Controller setup/zh \(page does not exist\)") • [提取 UI 图标](/wiki/Tutorial:Extracting_UI_icons/zh?action=edit&redlink=1 "Tutorial:Extracting UI icons/zh \(page does not exist\)")
  *[v]: View this template
  *[e]: Edit this template
  *[h]: History of this template
