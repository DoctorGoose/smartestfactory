# Power/zh

大多数的[建筑](/wiki/Buildings/zh "Buildings/zh")需要电，或者说 **电力** 来工作。电力是由发电机（详见下文）产生的，被[蓄电池](/wiki/Power_Storage/zh?action=edit&redlink=1 "Power Storage/zh \(page does not exist\)")储存或释放，并由工作建筑所消耗。电力通过[电缆](/wiki/Power_Line/zh "Power Line/zh")、[电线杆](/wiki/Power_Poles/zh "Power Poles/zh")、[墙壁插座](/wiki/Wall_Outlets/zh?action=edit&redlink=1 "Wall Outlets/zh \(page does not exist\)")、[输电塔](/wiki/Power_Tower/zh?action=edit&redlink=1 "Power Tower/zh \(page does not exist\)")、[火车站](/wiki/Train_Station/zh "Train Station/zh")或[轨道](/wiki/Railway/zh "Railway/zh")进行传输。   
  
功率以兆瓦（MW）为单位。电站储存的能量以兆瓦时（MWh）为单位，而燃料的能量密度则以兆焦耳（MJ）为单位。(详见[计量单位](/wiki/Units/zh?action=edit&redlink=1 "Units/zh \(page does not exist\)"))。 

## Contents

  * 1 概述
  * 2 电网
  * 3 电闸
  * 4 电力曲线图
  * 5 耗电设施
  * 6 发电机
    * 6.1 发电机种类
  * 7 电力储存
  * 8 时钟速度
    * 8.1 耗电设施
    * 8.2 发电机
  * 9 生产增幅
  * 10 能量
  * 11 成就
  * 12 琐事
  * 13 也可以看看
  * 14 历史
  * 15 引用



## 概述

消耗（或供应）电力的建筑只有在连接到电网（见下节）时才能运行，在该电网中，要么所有发电机 的总供应量足以满足所有耗电设施的总需求，要么[蓄电池](/wiki/Power_Storage/zh?action=edit&redlink=1 "Power Storage/zh \(page does not exist\)")中仍有能源。如果电力需求超过电力供应，且所有蓄能器都空了，电闸就会跳闸，使该电网上的所有建筑停止运行，直到问题得到解决，然后再重置断路器。 

## 电网

电网是由发电建筑和用电建筑组成的网络，通过电力线、电线杆、电力塔、火车站和铁路相连。与电网中的任何电线杆、发电机、火车站或电源开关进行[`E`](/wiki/Controls/zh?action=edit&redlink=1 "Controls/zh \(page does not exist\)")交互，即可查看总电量、发电量和耗电量的图表。 

电网可以使用[电源开关](/wiki/Power_Switch/zh?action=edit&redlink=1 "Power Switch/zh \(page does not exist\)")进行分割。多余的能量可以储存在[蓄电池](/wiki/Power_Storage/zh?action=edit&redlink=1 "Power Storage/zh \(page does not exist\)")中，在电力的消耗超过生产时可以释放能量。 

## 电闸

如果电力消耗超过生产，而电力储存库中又没有能量可供使用，电网就会跳闸。电网中所有连接的发电机和用电设备都将停止工作。无论跳闸设备与[先驱者](/wiki/Pioneer/zh "Pioneer/zh")之间的距离有多远，在地图的任何地方都能听到跳闸的声音效果。 

  * 与其他游戏不同，当发电量不足时，建筑物的运行速度不会变慢。电网将直接跳闸，与电网相连的 _**所有**_ 建筑将停止运行。



先驱者可以通过在任何已连接的发电机或电线杆上交互 [`E`](/wiki/Controls/zh?action=edit&redlink=1 "Controls/zh \(page does not exist\)") 来重置断路器。在用户界面中，拉下控制杆（如下图）即可恢复供电。重置前，建议在电网上安装更多发电机，或暂时移除工厂部分区域的供电电缆。否则，一旦重新启动，电网就会再次过载。 

电源跳闸还可能允许[敌对生物重生](/wiki/Combat/zh?action=edit&redlink=1 "Combat/zh \(page does not exist\)")。 

  * [](/wiki/File:Power_graph.jpg "功率图，功率消耗低于功率容量。")

功率图，功率消耗低于功率容量。

  * [](/wiki/File:Power_trip.jpg "在断电期间，与电网中的任何电线杆或发电机互动E，拉下左侧的拉杆即可重置断路器。")

在断电期间，与电网中的任何电线杆或发电机互动[`E`](/wiki/Controls/zh?action=edit&redlink=1 "Controls/zh \(page does not exist\)")，拉下左侧的拉杆即可重置断路器。




如果没有连接任何发电设备（例如使用开关一次性断开所有发电设备），建筑物将直接关闭，不会跳闸。在这种情况下，只要重新连接上足够的电源，建筑物就会恢复运行，而无需重新设置保险丝。 

## 电力曲线图

[](/wiki/File:Power_pole_-_graph.png)

[](/wiki/File:Power_pole_-_graph.png "Enlarge")

电线杆的电力曲线图，耗电量与发电量部分重叠

电力曲线图显示当前电网的电力生产和消耗信息，以及电网上所有 [蓄电池](/wiki/Power_Storage/zh?action=edit&redlink=1 "Power Storage/zh \(page does not exist\)") 储存的能量总和。蓄电池不会影响图表中的任何线条，相关信息会显示在图表右侧的菜单中。  
■ 容量： 电网中所有现有发电机同时运行时的最大功率输出总和。  
■ 发电量： 电网中所有发电机的当前输出功率。只有在电网上有[生物质燃烧器](/wiki/Biomass_Burners/zh?action=edit&redlink=1 "Biomass Burners/zh \(page does not exist\)")的情况下才与 “发电量 ”不同，因为只有生物质燃烧器才能根据需求进行调节。  
■ 耗电量： 电网中所有建筑物当前的电力需求。如果消耗量超过生产量，就会从蓄电池（如果有的话）提取能量，否则就会发生电力跳闸。  
■ 最大耗电量： 电网中所有建筑物同时运行时的最大电力需求总和。 

## 耗电设施

  * 大多数[建筑](/wiki/Building/zh?action=edit&redlink=1 "Building/zh \(page does not exist\)")都需要电力才能运转。它们被称为耗电设施。有关它们的电力需求（以兆瓦为单位），请参见各个建筑的页面。
  * 每个处于待机模式的建筑（无论是先驱者打开了待机开关，还是由于后勤问题导致建筑无法运行）都需要消耗 0.1 兆瓦。 
    * 将游戏初期的建筑超频至极低的时钟速度，可使它们在运行时比闲置时消耗更少的电力。
  * [指示灯](/wiki/Indicator_Light/zh?action=edit&redlink=1 "Indicator Light/zh \(page does not exist\)")会显示建筑是否在运行和消耗电力。



## 发电机

发电机将 [燃料](/wiki/Fuels/zh?action=edit&redlink=1 "Fuels/zh \(page does not exist\)") 转化为动力。每种发电机建筑都有自己的燃料种类和功率输出。 

除生物质燃烧器外，所有发电设备都会满负荷运转。生物质燃烧器会根据电力消耗量进行调整，在需求量较小的情况下燃烧速度会减慢。例如，如果电网容量为 105 兆瓦，由一台煤炭发电机提供 75 兆瓦，一台生物质燃烧器提供 30 兆瓦，而耗电量为 95 兆瓦，那么煤炭发电机的全部容量将首先使用，然后是生物质燃烧器容量的三分之二，这意味着燃料的燃烧速度将是最大需求时的三分之二。这也使得生物质燃烧机无法为蓄电池充电。 

### 发电机种类

发电机共有六种类型： 

  * [](/wiki/Biomass_Burner/zh "Biomass Burner/zh") [生物质燃烧炉](/wiki/Biomass_Burner/zh "Biomass Burner/zh")
  * [](/wiki/Coal-Powered_Generator/zh "Coal-Powered Generator/zh") [煤炭发电机](/wiki/Coal-Powered_Generator/zh "Coal-Powered Generator/zh")
  * [](/wiki/Fuel-Powered_Generator/zh "Fuel-Powered Generator/zh") [燃油发电机](/wiki/Fuel-Powered_Generator/zh?action=edit&redlink=1 "Fuel-Powered Generator/zh \(page does not exist\)")
  * [](/wiki/Geothermal_Generator/zh "Geothermal Generator/zh") [地热发电站](/wiki/Geothermal_Generator/zh?action=edit&redlink=1 "Geothermal Generator/zh \(page does not exist\)")
  * [](/wiki/Nuclear_Power_Plant/zh "Nuclear Power Plant/zh") [核电站](/wiki/Nuclear_Power_Plant/zh?action=edit&redlink=1 "Nuclear Power Plant/zh \(page does not exist\)")
  * [](/wiki/Alien_Power_Augmenter/zh "Alien Power Augmenter/zh") [外星能源强化装置](/wiki/Alien_Power_Augmenter/zh?action=edit&redlink=1 "Alien Power Augmenter/zh \(page does not exist\)")



## 电力储存

阅读主要文章 [电力储存](/wiki/Power_Storage/zh?action=edit&redlink=1 "Power Storage/zh \(page does not exist\)")

[](/wiki/File:Power_Storage.png)

[](/wiki/File:Power_Storage.png "Enlarge")

蓄电池

**[蓄电池](/wiki/Power_Storage/zh?action=edit&redlink=1 "Power Storage/zh \(page does not exist\)")** 是[阶级4](/wiki/%E9%87%8C%E7%A8%8B%E7%A2%91/zh?action=edit&redlink=1 "里程碑/zh \(page does not exist\)")解锁的一个游戏中期[建筑](/wiki/%E5%BB%BA%E7%AD%91/zh?action=edit&redlink=1 "建筑/zh \(page does not exist\)")，用于缓冲**电力** 能量。每个可储存 100 兆瓦时（即100 兆瓦 使用1 小时）。由于它允许 2 个电线连接，因此可以通过菊花链式连接多个 “蓄电池 ”来储存大量能源。 

当连接到由[生物质燃烧器](/wiki/Biomass_Burner/zh "Biomass Burner/zh")以外的发电机供电的电网时，它将使用多余的发电功率充电，每个功率最高为 100 兆瓦。因此，为一个空的蓄电池充满电至少需要一个小时的现实时间，如果剩余电量不足以满足电网中所有蓄电池的需要，则需要更长的时间（未充满电的蓄电池将分摊剩余电量，将其充电率降低到可用剩余电量除以部分充电的蓄电池数量）。为蓄电池充电不会增加电网耗电量或最大耗电量，也不会降低容量，因为如果对可用电量有其他需求，蓄电池会减慢或停止充电。 

只要蓄电池中储存有电量，并且出现电力短缺（消耗大于生产），所有蓄电池都会放电以补足差额，并立即启动。放电速度没有限制，将与电力不足完全匹配。这样，先驱者就可以迅速做出反应，恢复电力状况，无论是增加电力生产还是安装[电力开关](/wiki/Power_Switch/zh?action=edit&redlink=1 "Power Switch/zh \(page does not exist\)")。一旦储存的能量全部放完，但电力仍然不足，电网就会跳闸。 

## 时钟速度

_主要文章:_[时钟速度](/wiki/Clock_speed/zh "Clock speed/zh")

超频在[MAM研究站](/wiki/MAM/zh "MAM/zh")处解锁。通过[`E`](/wiki/Controls/zh?action=edit&redlink=1 "Controls/zh \(page does not exist\)")与建筑物互动并调节滑块，可以调整建筑物的时钟速度。 只有装有[](/wiki/Power_Shard/zh "Power Shard/zh") [能量碎片](/wiki/Power_Shard/zh "Power Shard/zh") 才可以将时钟速度提高100%以上，最高可达250%。 

一旦研究出超频，就可以自由地进行降频，而且不需要任何能量碎片。 

### 耗电设施

  * 耗电设施以用户设置的时钟速度工作。例如，当[构筑站](/wiki/Constructor/zh "Constructor/zh")的时钟速度设置为 200% 时，它的工作速度是原来的两倍。
  * 激活的超频建筑拥有更低的能源效率（同等电量完成的工作更少）。不过，闲置的超频建筑仍然只消耗标准的 0.1MW 闲置电力。 
    * 在上述示例中，其耗电量将超过标准耗电量的 2 倍。这也意味着，一栋超频 200% 的建筑比两栋超频 100% 的建筑消耗更多的电能。
  * 另一方面，低频运行建筑可以节省电能。 
    * 两个以 50% 速度工作的建筑消耗的电量要比一个以 100% 速度工作的建筑消耗的电量少。
    * 不过，工厂的占地面积会更大。
    * 低频后的用电设备的有效耗电量低于 0.1MW 的建筑在空闲时仍会使用 0.1MW的闲置电力。[1]



### 发电机

  * 发电机的超频方式与耗电设施不同。然而，它们的燃料消耗率总是与建筑物的发电量成正比。因此，发电机超频并不会提高燃料效率。 
    * 这意味着发电机会更快或更慢地燃烧燃料，但不会从相同数量的燃料中产生更多能量。
    * 生产率和消耗率直接随时钟速度变化，这与电力消耗者不同。详见[时钟速度](/wiki/Clock_speed/zh "Clock speed/zh")文章。



## 生产增幅

_主要文章:_[生产增幅](/wiki/Production_amplifier/zh?action=edit&redlink=1 "Production amplifier/zh \(page does not exist\)")

部分工厂建筑可以使用 [](/wiki/Somersloop/zh "Somersloop/zh") [索莫晶体](/wiki/Somersloop/zh "Somersloop/zh") 来进行生产增幅。这将使它们的耗电量最多增加 4 倍，与受时钟速度影响的耗电量相乘。 

## 能量

能量是 “功率 ”的衍生单位。当功率在一段时间内消耗（或产生）时，功率与时间的乘积称为能量。当功率随时间波动时，可以用平均功率来代替。 

能量的基本单位是焦耳（J）。确切的单位取决于所测量的功率和时间单位。例如 

  * `4 兆瓦 * 4 秒 = 16 兆焦` 在[构筑站](/wiki/Constructor/zh "Constructor/zh")中使用正常[时钟速度](/wiki/Clock_speed/zh "Clock speed/zh")和默认配方生产1份[铁棒](/wiki/Iron_Rod/zh?action=edit&redlink=1 "Iron Rod/zh \(page does not exist\)")所消耗的能量
  * `30 兆瓦 * 0.5 秒 = 15 兆焦` 1份[树叶](/wiki/Leaves/zh?action=edit&redlink=1 "Leaves/zh \(page does not exist\)") 在[生物质燃烧炉](/wiki/Biomass_Burner/zh "Biomass Burner/zh")里燃烧产生的能量
  * `2.5 吉瓦 * 10 分钟 = 2.5 吉瓦 * 600 秒 = 1,500 吉焦 = 1.5 太焦` 1份[钚燃料棒](/wiki/Plutonium_Fuel_Rod/zh?action=edit&redlink=1 "Plutonium Fuel Rod/zh \(page does not exist\)") 在 [核电站](/wiki/Nuclear_Power_Plant/zh?action=edit&redlink=1 "Nuclear Power Plant/zh \(page does not exist\)")里燃烧产生的能量
  * `100 兆瓦 * 1 小时 = 100 兆瓦时 = 360 吉焦` 1个 [蓄电池](/wiki/Power_Storage/zh?action=edit&redlink=1 "Power Storage/zh \(page does not exist\)")所能储存的能量



笔记: 

  * `1 小时 = 60 分钟 = 3600 秒`
  * `1 太瓦 = 1000 吉瓦 = 1,000,000 兆瓦`类似的, `1 太焦 = 1000 吉焦 = 1,000,000 兆焦`



蓄电池使用兆瓦时而不是兆焦。1 兆瓦时等于 3 600 兆焦。 

能量可用于比较[车辆](/wiki/Vehicle/zh?action=edit&redlink=1 "Vehicle/zh \(page does not exist\)")或发电机中[燃料](/wiki/Fuels/zh?action=edit&redlink=1 "Fuels/zh \(page does not exist\)")的燃烧时间，或比较物品的不同[替代配方](/wiki/Alternate_recipes/zh?action=edit&redlink=1 "Alternate recipes/zh \(page does not exist\)")之间的能量效率。 

  * 堆叠能量是物品能量与[堆叠](/wiki/Stack/zh?action=edit&redlink=1 "Stack/zh \(page does not exist\)")物品数量的乘积。



## 成就

[](/wiki/Achievements "Achievements")**[New fear unlocked](/wiki/Achievements#New_fear_unlocked "Achievements")** •  _"Fix blown fuse."_

## 琐事

  * 当任何用户界面中的功率图被点击 6 次时，都会出现[复活节彩蛋](/wiki/Easter_egg/zh?action=edit&redlink=1 "Easter egg/zh \(page does not exist\)")，出现故障并显示关于滥用 FICSIT 属性的警告。
  * 幸福工厂的原型具有风力发电功能，但已被移除。[2]


  * [](/wiki/File:Power_graph_glitched.png "点击电力图表 6 次后，将显示该图像。")

点击电力图表 6 次后，将显示该图像。

  * [](/wiki/File:Power_graph_warning.png "之后不久，此警告信息就会出现，直到您重新打开电力图表。")

之后不久，此警告信息就会出现，直到您重新打开电力图表。




## 也可以看看

  * [燃油](/wiki/Fuels/zh?action=edit&redlink=1 "Fuels/zh \(page does not exist\)")
  * [时钟速度](/wiki/Clock_speed/zh "Clock speed/zh")
  * [生产增幅](/wiki/Production_amplifier/zh?action=edit&redlink=1 "Production amplifier/zh \(page does not exist\)")
  * [](/wiki/Power_Line/zh "Power Line/zh") [电缆](/wiki/Power_Line/zh "Power Line/zh")
  * [](/wiki/Power_Pole/zh "Power Pole/zh") [电线杆](/wiki/Power_Pole/zh?action=edit&redlink=1 "Power Pole/zh \(page does not exist\)")



## 历史

  * [Patch 0.8.3.3](/wiki/Patch_0.8.3.3 "Patch 0.8.3.3"): 修复了重置保险丝控制杆阴影偏移的问题
  * [Patch 2018-10-11](/wiki/Patch_2018-10-11 "Patch 2018-10-11"): 推出



## 引用

  1. ↑ [Satisfactory Wiki - August 1st, 2021 - Underlocked-below-idle-power-while-active.webp](/wiki/File:Underlocked-below-idle-power-while-active.webp "File:Underlocked-below-idle-power-while-active.webp")
  2. ↑ [Instagram - February 26th, 2021 AMA - Can you bring wind turbines to Satisfactory?](/wiki/File:February_26th,_2021_Instagram_AMA_-_Can_you_bring_solar_power_and_wind_turbines_and_water_power_to_Satisfactory%3F.mp4 "File:February 26th, 2021 Instagram AMA - Can you bring solar power and wind turbines and water power to Satisfactory?.mp4")



  * [v](/wiki/Template:PioneerNav "Template:PioneerNav")
  * [e](https://satisfactory.wiki.gg/wiki/Template:PioneerNav?action=edit)
  * [h](https://satisfactory.wiki.gg/wiki/Template:PioneerNav?action=history)

[幸福工厂](/wiki/Satisfactory/zh "Satisfactory/zh") 游戏机制  
---  
玩家能力| [百科](/wiki/Codex/zh?action=edit&redlink=1 "Codex/zh \(page does not exist\)") • [资源扫描器](/wiki/Resource_Scanner/zh?action=edit&redlink=1 "Resource Scanner/zh \(page does not exist\)") • [建造枪](/wiki/Build_Gun/zh "Build Gun/zh") • [库存](/wiki/Inventory/zh?action=edit&redlink=1 "Inventory/zh \(page does not exist\)") • [生命](/wiki/Health/zh?action=edit&redlink=1 "Health/zh \(page does not exist\)") • [战斗](/wiki/Combat/zh?action=edit&redlink=1 "Combat/zh \(page does not exist\)") • [移动](/wiki/Movement/zh?action=edit&redlink=1 "Movement/zh \(page does not exist\)") • [手电筒](/wiki/Flashlight/zh?action=edit&redlink=1 "Flashlight/zh \(page does not exist\)") • [HUD](/wiki/HUD/zh?action=edit&redlink=1 "HUD/zh \(page does not exist\)") • [箱子](/wiki/Crate/zh?action=edit&redlink=1 "Crate/zh \(page does not exist\)") • [待办事项列表](/wiki/To-Do_List/zh?action=edit&redlink=1 "To-Do List/zh \(page does not exist\)")  
可解锁的能力| [配方](/wiki/Recipes/zh?action=edit&redlink=1 "Recipes/zh \(page does not exist\)") • 电力 • [超频、降频](/wiki/Clock_speed/zh "Clock speed/zh") • [生产增幅](/wiki/Production_amplifier/zh?action=edit&redlink=1 "Production amplifier/zh \(page does not exist\)") • [定制器](/wiki/Customizer/zh "Customizer/zh") • [地图](/wiki/Map/zh?action=edit&redlink=1 "Map/zh \(page does not exist\)") • [生产力显示](/wiki/Productivity_Display/zh?action=edit&redlink=1 "Productivity Display/zh \(page does not exist\)") • [扬程](/wiki/Head_lift/zh "Head lift/zh") • [蓝图](/wiki/Blueprints/zh?action=edit&redlink=1 "Blueprints/zh \(page does not exist\)") • [燃料](/wiki/Category:Fuels "Category:Fuels") • [高产包包乐豪华版](/wiki/FICSIT_Productive_Packer_Deluxe/zh?action=edit&redlink=1 "FICSIT Productive Packer Deluxe/zh \(page does not exist\)")  
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
  *[his]: his trivia section
