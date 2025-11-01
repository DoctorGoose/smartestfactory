# Electric Locomotive/zh

## Electric Locomotive  
  
[ ](/wiki/File:Electric_Locomotive.png "Electric Locomotive.png")

_Moves Freight Cars from station to station.  
Requires between 25-110 MW of power to move.   
Must be built on a Railway.  
Nicknamed 'Leif' by FICSIT pioneers because of its reliability._

### Unlocked by

[Tier 6](/wiki/Tier_6 "Tier 6") \- Monorail Train Technology

### Class name

Desc_Locomotive_C

## Vehicle

### Max speed

120 km/h

## Dimensions

### Width

6 m

### Length

16 m

### Height

6 m

### Area

96 m2

## Ingre­dients

**5 ×[](/wiki/Modular_Frame "Modular Frame") [Modular Frame](/wiki/Modular_Frame "Modular Frame")**

**10 ×[](/wiki/Motor "Motor") [Motor](/wiki/Motor "Motor")**

**20 ×[](/wiki/Steel_Pipe "Steel Pipe") [Steel Pipe](/wiki/Steel_Pipe "Steel Pipe")**

**20 ×[](/wiki/Rubber "Rubber") [Rubber](/wiki/Rubber "Rubber")**

**50 ×[](/wiki/Wire "Wire") [Wire](/wiki/Wire "Wire")**

**電動火車頭** 是一種用於沿著[鐵路](/wiki/Railway "Railway")運輸貨物和[先鋒](/wiki/Pioneer "Pioneer")的[載具](/wiki/Vehicle "Vehicle")。連接的[貨車廂](/wiki/Freight_Car "Freight Car")可以通過[貨運月台](/wiki/Freight_Platform "Freight Platform")進行裝載或卸載。電動火車頭可以通過設定停靠的[火車站](/wiki/Train_Station "Train Station")清單進行[自動化](/wiki/Vehicle#Automation "Vehicle")運行。 

多個貨車廂和火車頭可以連接在一起形成一列火車。目前，火車是遊戲中最快的地面載具，可以實現高效的長距離資源運輸。在[第7層](/wiki/Tier_7 "Tier 7")解鎖的空中[無人機](/wiki/Drone "Drone")速度是其兩倍，但它們有自己的一套優缺點。 

## Contents

  * 1 功率消耗
  * 2 建造
  * 3 用法
    * 3.1 火車頭UI
    * 3.2 時間表
    * 3.3 停靠設定
    * 3.4 駕駛
      * 3.4.1 剎車
      * 3.4.2 速度
    * 3.5 自動化
      * 3.5.1 路徑規劃
    * 3.6 碰撞
      * 3.6.1 修理脫軌的火車
  * 4 火車長度
  * 5 重量和力
  * 6 火車吞吐量
  * 7 當前問題
  * 8 趣聞
  * 9 另見
  * 10 圖庫
  * 11 歷史
  * 12 References



## 功率消耗

電動火車頭在任何時候運作都需要至少25 MW的電力，即使它沒有移動。加速時可能會消耗高達110 MW，具體取決於所承受的“負荷”有多大。例如，在爬坡時會消耗更多電力，而在平坦的軌道上則會自動降低功耗，下坡時會降至最低25 MW。火車頭在沒有電力的情況下無法加速，但始終可以使用其剎車。 

注意，HUD中顯示的功率消耗是該列火車上所有火車頭的總消耗量。一列有四個火車頭的火車可能顯示為100-440 MW。 

通過按住與當前行駛方向相反的鍵（[`S`](/wiki/Controls "Controls")或[`W`](/wiki/Controls "Controls")），火車頭將使用再生制動。根據火車頭的當前速度，再生制動最多可產生33 MW的電力。減去基礎需求的25 MW，這將導致最多8 MW的淨功率增益。 

## 建造

火車頭只能在鐵路上建造。 _帶有擋風玻璃和駕駛室的一面是前面_ ，帶有六個馬達的一側是後面。手動駕駛火車時，火車頭在火車中的位置不會影響行駛方向，也不會影響最大速度。 

然而，自動駕駛只能在至少有一個火車頭在火車前端且前端面向行駛方向的情況下行駛。只有前端火車頭面向前方的火車只能向前自動駕駛，並需要在終點線處進行迴圈才能轉身；中間的火車頭不能在自動駕駛中運行；至少有一個火車頭在兩端，前端彼此相對的火車可以在兩個方向上自動駕駛，不再需要轉身。 

每個火車頭在火車中始終提供全部動力，使其可以添加更多火車頭，以便重型火車能夠爬上陡坡。 

當沒有駕駛員時，火車頭會自動啟動剎車。因此，它們可以自由地建造在斜坡上，並且即使在自動駕駛中也會嘗試停止。 

要向火車添加更多火車頭或貨車廂，只需瞄準火車前方或後方的鐵路，藍圖通常會自動對齊。有時藍圖看起來不會對齊，但如果建造火車頭或車廂，它們仍會連接到火車的其餘部分，只要距離足夠近。無法編輯火車的中間部分；編輯火車中間部分的唯一方法是拆除整個火車並按新的佈局重新建造。即使在多人遊戲中，主持人也可以在火車移動時添加火車頭或車廂。 

在移動或自動排程時無法拆除火車頭，只有在完全靜止且自動駕駛禁用時才能拆除。然而，可以拆除其下方的鐵路，火車將突然停止並停留在空中。 

## 用法

### 火車頭UI

使用[`E`](/wiki/Controls "Controls")鍵與任何禁用自動駕駛的火車頭互動，然後使用[`Q`](/wiki/Controls "Controls")鍵將提供對UI的存取。 

你可以任意命名火車頭（火車）、編輯時間表，甚至開始自動化（自動駕駛）。 

### 時間表

存取火車頭UI將提供對 _該火車頭_ 時間表UI的存取。 

時間表包括一個地圖，可以使用“拖放”方式設定時間表，將可用的火車站拖動到右側，或懸停在任何可用火車站上的“+”號並使用[](/wiki/File:Keyboard_White_Mouse_Left.png "Left")點擊。 [1]

當前的時間表提供了一種調整火車在[火車站](/wiki/Train_Station "Train Station")停靠時設定的方法。 

重要：時間表必須**儲存** 才能使更改生效。 

  * [](/wiki/File:Train_Station_UI_0.png "顯示時間表UI存取的火車頭UI範例")

顯示時間表UI存取的火車頭UI範例

  * [](/wiki/File:Train_Station_UI_1.png "顯示將火車站拖動到時間表中的火車站時間表UI範例")

顯示將火車站拖動到時間表中的火車站時間表UI範例

  * [](/wiki/File:Train_Station_UI_2.png "顯示“停靠設定”選項的火車站時間表UI範例")

顯示“停靠設定”選項的火車站時間表UI範例




### 停靠設定

在時間表UI中，在**當前時間表** 列中，對於所需的火車站，點擊齒輪圖標⚙️（在右側），這會打開一個新UI以允許調整特定火車站的停靠設定。 [2]

根據個別[貨運月台](/wiki/Freight_Platform "Freight Platform")的設定，可以選擇裝載/卸載所有物品或僅裝載/卸載特定物品，或完全不操作。 

此外，可以設定火車在繼續行駛前等待的時間（以秒為單位）。 

停靠設定是**每列火車/每站** 不同的， _不同火車_ 可以有不同的停靠設定。 

重要：停靠設定和時間表必須**儲存** 才能使更改生效。 

  * [](/wiki/File:Train_Station_UI_3.png "顯示預設設定的火車站停靠設定UI範例")

顯示預設設定的火車站停靠設定UI範例

  * [](/wiki/File:Train_Station_UI_4.png "顯示僅裝載範例的火車站停靠設定UI範例")

顯示僅裝載範例的火車站停靠設定UI範例

  * [](/wiki/File:Train_Station_UI_5.png "顯示火車應停留，直到AI限制器和鋁錠完全裝載並等待15秒的火車站停靠設定UI範例")

顯示火車應停留，直到AI限制器和鋁錠完全裝載並等待15秒的火車站停靠設定UI範例




### 駕駛

使用[`E`](/wiki/Controls "Controls")鍵與任何禁用自動駕駛的火車頭互動，將允許你手動駕駛 _該火車頭_ 。 

手動駕駛火車頭時，按[`Q`](/wiki/Controls "Controls")鍵將打開時間表UI（見上文）。 

按住[`W`](/wiki/Controls "Controls")（前進）或[`S`](/wiki/Controls "Controls")（後退）方向鍵將開始“加速”火車頭，逐漸增加功率消耗，直到馬達產生足夠的扭矩來克服其重量，火車開始加速。 

剎車可以在火車頭達到足夠的功率以啟動前釋放，這意味著如果火車在坡道上，它將開始向後滾動，直到火車頭增加功率以拉動火車上坡。 

#### 剎車

  * 火車有兩種不同的剎車系統： 
    * 按下與行駛方向相反的方向鍵（[`S`](/wiki/Controls "Controls")或[`W`](/wiki/Controls "Controls")）將啟動再生電制動。它們安靜且沒有明顯的外部視覺標誌，除了閃爍的UI元素顯示“BRAKE”和在高速行駛時部分伸出的空氣剎車襟翼（位於火車頭頂部的面板）。這些剎車在高速時效果較差，在低於80公里/小時時達到最大剎車力。
    * 按下手剎鍵（[`Space`](/wiki/Controls "Controls")）將啟動空氣剎車。它們聲音大且啟動火車上的多個活動部件，包括完全伸出的空氣剎車襟翼、位於火車頭兩組車輪之間的大剎車片直接壓在鐵軌上，以及按在整列火車上的每個車輪上的剎車片，包括貨車廂，這會產生高音的尖叫聲，在足夠高的速度下使貨車廂車輪發紅，並在完全停止時釋放出一股空氣壓力。這些剎車的剎車力在任何速度下都相同。
  * 這兩種剎車系統可以單獨啟動，也可以一起啟動以達到最大剎車力。手動駕駛時，釋放剎車會使火車開始滾動。離開火車會自動啟動剎車，它會嘗試停止滾動。它會一直剎車，直到再次收到玩家輸入或自動駕駛啟動並運行。



[](/wiki/File:Train_speed_test.png)

[](/wiki/File:Train_speed_test.png "Enlarge")

使用約2400公尺高的[4公尺雙坡道](/wiki/Double_Ramp_8m_x_4m "Double Ramp 8m x 4m")塔，火車可以達到極高的速度。

#### 速度

在其自身動力下，火車頭的最高速度在平坦鐵路上約為120公里/小時。 

在爬陡坡時最高速度較慢，但只要火車不太重，應始終能夠至少達到54公里/小時。 

下坡時，它可以快速加速，超過其最高速度，長坡道下速度接近500公里/小時（見圖）。 

### 自動化

使用[`E`](/wiki/Controls "Controls")鍵與任何禁用自動駕駛的火車頭互動，將允許你切換該火車頭的自動駕駛開/關。 

火車站只接受來自一個方向的火車，但火車可以向任一方向出發。 

如果設定路線後火車沒有開始移動，請檢查鐵路是否正確連接，所有火車站是否面向正確方向，並且線路是否有電力。 

自動火車加速和剎車較慢，在急轉彎時剎車，並嘗試在其時間表上靠近車站時減速。然而，如果火車無法在預定停靠點前停下來（例如在陡坡底部的車站），它將會像到達鐵路盡頭一樣突然停止。 

所有連接的火車頭被視為單一列火車，共享相同的火車時間表。 

只有一個站的火車時間表不會循環——一旦火車在車站停下，它將不會移動，並抱怨“路徑無效”。至少需要兩個車站才能使火車循環。 

#### 路徑規劃

_路徑規劃由火車頭完成，而非號誌。_ 單個[火車號誌](/wiki/Train_Signals "Train Signals")無法改變火車選擇的路徑，它們只能告訴火車是否可以在其路徑上繼續前進。 

火車總是試圖找到最短路徑。不過有一個例外：如果路徑經過一個[火車站](/wiki/Train_Station "Train Station")，每經過一個火車站，該路徑將增加額外的**100公尺的成本** 。這樣火車應該會選擇避開車站而選擇側線。[3]

### 碰撞

如果不使用[火車號誌](/wiki/Train_Signals "Train Signals")或火車碰撞框相互重疊，火車將碰撞並被摧毀。 [4]

目前，火車只能與其他火車和有輪[載具](/wiki/Vehicles "Vehicles")碰撞。碰撞的火車將會脫軌。發生碰撞時，先鋒會在HUD中聽到聲音通知，並在指南針上顯示火車脫軌的位置標記。 

火車會自由穿過其他所有物體，包括自然地形、玩家建築的結構，甚至玩家本身，不會造成任何[損害](/wiki/Damage "Damage")，也不會失去動量。火車的側面有碰撞框，但僅用於防止先鋒穿過側面。火車只能與 _其他_ 火車碰撞，無法與自身碰撞：這意味著大型火車仍然可以使用使前部與後部相交的迴圈而不會出現問題。 

#### 修理脫軌的火車

先鋒可以修理脫軌的火車[5][6]，走到火車的任何脫軌部分並按[`E`](/wiki/Controls "Controls")鍵將火車重新上軌，火車將返回到脫軌前的位置。如果火車無法接近，會有一個**黃色全像投影** ，你可以使用[`E`](/wiki/Controls "Controls")鍵方法與之互動。[7]

  * [](/wiki/File:Derailed_Train_Repair.png "更新5 - 修理脫軌火車的範例")

更新5 - 修理脫軌火車的範例

  * [](/wiki/File:Train_Rerail_Holograms.png "更新5 - 碰撞現場顯示的黃色火車全像投影範例")

更新5 - 碰撞現場顯示的黃色火車全像投影範例




## 火車長度

單個火車頭可以在平坦鐵路上牽引大約100節空貨車廂。（ _見下面的重量和力部分_ ） 

然而，即使是輕微的坡度也會使貨車的重量迅速超過火車頭的能力，它將開始向後滾動。使用自然坡道或建造混合的2公尺和4公尺坡道，可以實現最陡的坡度（見[](/wiki/Railway "Railway") [Railway](/wiki/Railway "Railway")了解更多詳細信息），但一系列2公尺坡道或[雙坡道](/wiki/Double_Ramp_8m_x_2m "Double Ramp 8m x 2m")是能夠支撐鐵路的最陡坡度，可以快速輕鬆地建造。  
由於貨車廂的重量隨著裝滿程度而變化，所需的火車頭數量也會有所不同。軌道的坡度也會影響這一點。 

有關火車頭與貨車廂比例，請參見[貨車廂 - 重量](/wiki/Freight_Car#Weight "Freight Car")中的表格。 

## 重量和力

火車頭重 _300 噸_ 。在最大負荷下，它們消耗110 MW，施加的力為**2000 kN** 。火車的總重量會影響加速。一列擁有一個火車頭和總重量2000噸（包括17節滿載貨車廂）的火車將以大約2000 kN2000 t=1 m/s2的速度加速。這意味著它將在10秒或50米後達到36公里/小時。超過60公里/小時後，火車將逐漸減少施加的力，因此達到最高速度的總時間比預期的要長。施加的總力是火車頭力和負坡力減去所有阻力的總和。 

空氣剎車施加 _900 kN_ 的力（在貨車廂上為 _200 kN_ ），而再生剎車在超過80公里/小時時施加 _600 kN_ 的力，在低於80公里/小時時施加 _2000 kN_ 的力。一列火車的剎車力是所有剎車力的總和。 

阻力影響火車的速度和大小。火車中的每一節貨車廂和火車頭都受到這些力的單獨影響。這些力包括： 

  * **阻力** : 也稱為空氣阻力，這種力隨著火車速度的增加而增加。它以速度的平方增長。前方的火車頭在120公里/小時時大約經受 _15 kN_ ，每節貨車廂大約增加 _5.4 kN_ 。
  * **滾動阻力** : 這是車輪的摩擦力。對於火車頭，它是靜態的4.4 kN。對於貨車廂，它範圍從0.4到1.5 kN，隨著車廂總重量的增加而增加。
  * **坡度力** : 這是在坡道上經歷的力。它向後拉動火車，等於total weight×slope.。如果火車在下坡移動，這個力是負的，並添加到火車頭的力中。（見[貨車廂 - 重量](/wiki/Freight_Car#Weight "Freight Car")了解更多詳細信息。）
  * **曲線阻力** : 當火車轉彎時，它們會經歷額外的滾動阻力。這取決於曲線半徑和火車速度。它可以近似為：0.4×重量×速度半徑。注意對於貨車廂，僅考慮其有效載荷。曲線半徑從軌道中間測量。3x3地基上的四分之一圓曲線半徑為22米，6x6曲線半徑為46米。較大的曲線具有較小的曲線阻力。



一節空貨車廂重30噸，而滿載時重100噸（載重量為70噸，包含14噸的集裝箱和每個滿載堆疊的1.75噸）。 

## 火車吞吐量

_Main article:_[Tutorial:Train throughput](/wiki/Tutorial:Train_throughput "Tutorial:Train throughput")

## 當前問題

  * 當在多人遊戲伺服器中作為客戶端玩遊戲時，火車目前有多個問題： 
    * 移動中的火車會出現延遲。
    * 客戶端無法手動駕駛火車或編輯自動化時間表。
    * 火車總是顯示沒有電力。
    * 客戶端無法在移動中的火車上添加額外的火車頭或車廂。
    * 站在火車上嘗試“乘坐”火車會使遊戲崩潰，並可能在嘗試重新加入伺服器時殺死客戶端角色。
  * 有時候離開火車後，[建造槍](/wiki/Build_Gun "Build Gun")選單會被鎖定。可以通過按兩次P鍵、儲存和載入遊戲或進入和退出超疾管來解決這個問題。 
    * 如果火車經過水體，這可能會引起問題
  * 如果建造兩個火車站而沒有間隙分隔兩個站結構（例如火車站、貨運月台、火車站、貨運月台設定），並且兩列火車分別在每個站停靠，兩列火車將會卡在對接狀態，直到遊戲重新載入。
  * 改變遊戲選項中的網路質量為超高（Ultra）可能解決其中一些問題，然而在連接不良的情況下，這可能會使問題變得更糟。建議進行測試。



## 趣聞

  * 在遊戲的早期版本中，使用喇叭（按下左鍵）時，有非常小的機會聽到蒸汽火車頭的喇叭聲[8]而不是正常的聲音。這在[Patch 0.5.0.0](/wiki/Patch_0.5.0.0 "Patch 0.5.0.0")中被移除。
  * 與有輪載具不同，自動火車在水下運行時仍然正常工作。然而，手動駕駛的火車進入水中時，會使先鋒下車。
  * 先鋒在火車內免受[毒氣](/wiki/Poison_Gas "Poison Gas")和[輻射](/wiki/Radiation "Radiation")傷害。
  * 火車在轉彎時會略微傾斜。
  * 火車頭的設計類似於[EMD F40PH 柴油火車頭](https://en.wikipedia.org/wiki/EMD_F40PH "wikipedia:EMD F40PH")。



## 另見

  * [](/wiki/Freight_Car "Freight Car") [貨車廂](/wiki/Freight_Car "Freight Car")
  * [](/wiki/Railway "Railway") [鐵路](/wiki/Railway "Railway")
  * [](/wiki/Train_Station "Train Station") [火車站](/wiki/Train_Station "Train Station")
  * [](/wiki/Freight_Platform "Freight Platform") [貨運月台](/wiki/Freight_Platform "Freight Platform")
  * [](/wiki/Empty_Platform "Empty Platform") [空月台](/wiki/Empty_Platform "Empty Platform")



## 圖庫

  * [](/wiki/File:Electric_Locomotive_%26_Freight_Car,_Parked.png "遊戲中出現的單個裝滿貨車廂的電動火車頭。")

遊戲中出現的單個裝滿貨車廂的電動火車頭。

  * [](/wiki/File:Electric_Train_Overpass.png "在高架鐵路上的雙向火車，有三節貨車廂。注意兩個火車頭面向相反方向。")

在高架[鐵路](/wiki/Railway "Railway")上的雙向火車，有三節[貨車廂](/wiki/Freight_Car "Freight Car")。注意兩個火車頭面向相反方向。

  * [](/wiki/File:Train_on_elevated_Railway.png "在高架鐵路上的較長的單向火車。注意兩個火車頭面向相同方向。")

在高架鐵路上的較長的單向火車。注意兩個火車頭面向相同方向。

  * [](/wiki/File:Train_timing_tutorial.png "展示多列火車在同一時間表上計時的示意圖。")

展示多列火車在同一時間表上計時的示意圖。

  * [](/wiki/File:Bi-Directional_Rail_System_Design_1.webp "使用雙向鐵路的鐵路系統示意圖，顯示火車號誌設定。")

使用雙向鐵路的鐵路系統示意圖，顯示火車號誌設定。

  * [](/wiki/File:Freight_Platform_E3.png "E3預告片中看到的帶有吊車平台的停靠火車（舊版視覺）。")

E3預告片中看到的帶有吊車平台的停靠火車（舊版視覺）。

  * [](/wiki/File:Train_screenshot_old.jpg "火車和核更新前的火車頭和車廂的早期設計。")

火車和核更新前的火車頭和車廂的早期設計。

  * [](/wiki/File:Train_on_railway_dev_blog.png "在開發博客中揭示的火車。")

在開發博客中揭示的火車。




## 歷史

  * [Patch 0.8.3.1](/wiki/Patch_0.8.3.1 "Patch 0.8.3.1"): [反轉視角](/wiki/Settings#Controls "Settings")選項現在也適用於[載具](/wiki/Vehicles "Vehicles")和火車
  * [Patch 0.8.2.9](/wiki/Patch_0.8.2.9 "Patch 0.8.2.9"): 現在在火車頭和[貨運車](/wiki/Freight_Car "Freight Car")停靠在[火車站](/wiki/Train_Station "Train Station")時，可以更容易地與之互動
  * [Patch 0.8.2.0](/wiki/Patch_0.8.2.0 "Patch 0.8.2.0"): 禁用自動駕駛後火車頭應該開始剎車
  * [Patch 0.8.1.0](/wiki/Patch_0.8.1.0 "Patch 0.8.1.0"): 修復了一個與路徑查找結果中的重複項相關的[火車](/wiki/Train "Train")路徑問題。這將使火車有時在火車站外的第一個轉向處選擇錯誤的方向。
  * [Patch 0.8.0.5](/wiki/Patch_0.8.0.5 "Patch 0.8.0.5"): 修復了在打開火車選單UI時無法退出火車頭的問題
  * [Patch 0.8.0.1](/wiki/Patch_0.8.0.1 "Patch 0.8.0.1"): 火車調度已恢復到穩定版本，一些正在進行的工作意外進入了更新8，這導致了一些路徑號誌設定問題。例如允許火車進入未清除出口的路徑區塊。
  * [Patch 0.8.0.0](/wiki/Patch_0.8.0.0 "Patch 0.8.0.0"): 修復了火車在載入儲存時不必等待2秒進行路徑查找（冷卻時間）。這修復了火車在載入時靠近轉向處時可能走錯路的情況。
  * [Patch 0.7.0.3](/wiki/Patch_0.7.0.3 "Patch 0.7.0.3")
    * 當火車失去電力時，火車燈現在應該會正確更新
    * 火車燈現在應該會在脫軌後正確恢復到正確位置
  * [Patch 0.6.0.10](/wiki/Patch_0.6.0.10 "Patch 0.6.0.10"): 為電動火車頭添加了燈光。燈光現在實際發光，類似於汽車
  * [Patch 0.6.0.0](/wiki/Patch_0.6.0.0 "Patch 0.6.0.0"): 移除了信標成本
  * [Patch 0.5.1.11](/wiki/Patch_0.5.1.11 "Patch 0.5.1.11")
    * 修復了自動火車可能完全卡住（“死鎖”）的一些問題
    * 修復了火車的重新上軌全像投影有時消失的問題
    * 修復了火車和[火車站](/wiki/Train_Station "Train Station")在[地圖](/wiki/Map "Map")和[指南針](/wiki/HUD#Compass "HUD")上顯示位置不正確的問題
  * [Patch 0.5.1.7](/wiki/Patch_0.5.1.7 "Patch 0.5.1.7")
    * 現在預設使用[`Q`](/wiki/Controls "Controls")鍵打開火車UI
    * 修復了貨車廂無法正確裝載/卸載的問題，導致它們在停靠時被卡住直到強制取消
    * 修復了[多人遊戲](/wiki/Multiplayer "Multiplayer")和[專用伺服器](/wiki/Dedicated_servers "Dedicated servers")客戶端無法取消停靠過程的問題
  * [Patch 0.5.1.4](/wiki/Patch_0.5.1.4 "Patch 0.5.1.4")
    * 修復了一個火車在[火車站](/wiki/Train_Station "Train Station")停靠時可能會在儲存和載入時保留[路徑號誌](/wiki/Train_Signals "Train Signals")的錯誤
    * 修復了一種情況，火車在火車站停靠後的路徑號誌處會不斷保留相同的路徑號誌
  * [Patch 0.5.1.1](/wiki/Patch_0.5.1.1 "Patch 0.5.1.1"): 修復了一個火車在低速碰撞時可能會生成粒子效果並導致性能下降並在某些情況下導致遊戲崩潰的錯誤
  * [Patch 0.5.0.14](/wiki/Patch_0.5.0.14 "Patch 0.5.0.14"): 增加了一些防止火車脫軌時掉出世界的措施
  * [Patch 0.5.0.12](/wiki/Patch_0.5.0.12 "Patch 0.5.0.12"): 在[鐵路](/wiki/Railway "Railway")上顯示全像投影，以便在發生脫軌時更容易讓火車重新上軌，並且所有火車/貨車至少距離軌道50米
  * [Patch 0.5.0.8](/wiki/Patch_0.5.0.8 "Patch 0.5.0.8")
    * 修復了當[多人遊戲](/wiki/Multiplayer "Multiplayer") / [專用伺服器](/wiki/Dedicated_Servers "Dedicated Servers")客戶端乘坐火車時，自動駕駛火車速度緩慢的問題
    * 修復了火車喇叭無法重新綁定，並且將左鍵設定為前進會使火車始終鳴喇叭的問題
  * [Patch 0.5.0.6](/wiki/Patch_0.5.0.6 "Patch 0.5.0.6"): 修復了火車在號誌處等待時，有時可能與平行軌道上的火車相撞的某些情況
  * [Patch 0.5.0.5](/wiki/Patch_0.5.0.5 "Patch 0.5.0.5"): 修復了一個導致火車永遠卡在停靠狀態的錯誤，導致受影響的儲存文件性能下降
  * [Patch 0.5.0.4](/wiki/Patch_0.5.0.4 "Patch 0.5.0.4")
    * 修復了火車載荷在載入時被重置並保持這樣直到下次載入的問題
    * 臨時修復了火車卡在停靠狀態的問題，停靠動畫在應用適當修復前可能無法正常工作
  * [Patch 0.5.0.2](/wiki/Patch_0.5.0.2 "Patch 0.5.0.2") _（在[Patch 0.5.0.3](/wiki/Patch_0.5.0.3 "Patch 0.5.0.3")中重新發布）_
    * 修復了退出電動火車頭時“按 _ 停靠”信息卡住的問題
    * 修復了無法用[`V`](/wiki/Controls "Controls")鍵關閉火車頭選單的問題
    * 修復了裝有流體的貨車無法上坡的問題
  * [Patch 0.5.0.0](/wiki/Patch_0.5.0.0 "Patch 0.5.0.0")
    * 現在可以相互碰撞而不是穿過 
      * 火車不能與汽車、建築物或地形碰撞，只能與其他火車碰撞
      * 脫軌的火車可以通過接近並按[`E`](/wiki/Controls "Controls")鍵重新上軌
    * 現在遵循火車號誌
    * 駕駛時現在顯示按鍵綁定列表
    * 現在可以在駕駛時遠程切換交叉口
    * 時間表UI已重新設計，增加了停靠設定
    * 現在可以從定制器中塗裝
    * **未記錄的更改** \- 移除了蒸汽汽笛彩蛋。
  * [Patch 0.3.6.8](/wiki/Patch_0.3.6.8 "Patch 0.3.6.8"): 修復了電動火車頭的計時類型
  * [Patch 0.3.4.13](/wiki/Patch_0.3.4.13 "Patch 0.3.4.13"): 火車手剎動畫不再陷入循環
  * [Patch 0.3.4.9](/wiki/Patch_0.3.4.9 "Patch 0.3.4.9"): 當主持人不在附近時，客戶端玩家現在可以與火車互動
  * [Patch 0.2.1.20](/wiki/Patch_0.2.1.20 "Patch 0.2.1.20"): 修復了火車在載入遊戲時無法獲得電力的問題
  * [Patch 0.2.1.17](/wiki/Patch_0.2.1.17 "Patch 0.2.1.17"): 火車現在會在跳入並加油門（W或S鍵）時自動鬆開剎車。
  * [Patch 0.2.1.16](/wiki/Patch_0.2.1.16 "Patch 0.2.1.16"): 
    * 錯誤修正：火車不再因多個連接站而卡在停靠中。
    * 錯誤修正：更新玩家駕駛火車在載入時的主火車頭。
    * 錯誤修正：進入火車不再自動鬆開剎車，需要手動用空格鍵鬆開。
  * [Patch 0.2.1.15](/wiki/Patch_0.2.1.15 "Patch 0.2.1.15"): 
    * 雙向火車“倒車”時現在會正確剎車。
    * 附加AI控制的火車不會使AI失去對火車的控制。
    * 無人駕駛的火車（無論是玩家還是AI駕駛）現在會自動剎車。
  * [Patch 0.2.1.14](/wiki/Patch_0.2.1.14 "Patch 0.2.1.14"): 
    * 手動停靠有時會崩潰，避免了崩潰但在此情況下可能不會停靠。
    * 修復了客戶端或退出遊戲時火車有時會崩潰的問題。
    * 雙向火車的倒車更新不正確導致其中一個方向無法駕駛。這影響了玩家和AI。
  * [Patch 0.2.1.13](/wiki/Patch_0.2.1.13 "Patch 0.2.1.13"): 
    * 你可以在火車內啟用AI。
    * 自動駕駛計算改進以更好地預測剎車；這縮短了剎車距離，並修復了一些上坡或下坡時的問題。
    * 當火車不在玩家附近時，聲音不再播放。
    * 每列火車只有一個AI；修復了2個AI試圖駕駛同一列火車的邊緣情況。
    * 火車有時運行過快而錯過車站。這使它們不可靠；現在AI剎車更好，車站捕捉火車。
    * 如果火車在交叉口處分成兩半，火車將重新定位在一起。
    * 修復了玩家駕駛火車靠近水體時角色可能被摧毀的情況。
    * 無法在水體附近使用建造槍。
    * 火車現在會儲存其速度，因此在載入時保持運行。
  * [Patch 0.2.1.11](/wiki/Patch_0.2.1.11 "Patch 0.2.1.11"): 
    * 火車名字現在應該正確儲存（包括客戶端）
    * 火車現在應該正確顯示在指南針上
  * [Patch 0.2.1.3](/wiki/Patch_0.2.1.3 "Patch 0.2.1.3"): 長時間積累並導致性能下降的火車粒子效果現在會被正確移除。
  * [Patch 0.2.1.1](/wiki/Patch_0.2.1.1 "Patch 0.2.1.1"): 添加了火車停止時的蒸汽聲
  * [Patch 0.1.20](/wiki/Patch_0.1.20 "Patch 0.1.20"): 
    * 電力消耗增加。從15增加到25，最大從80增加到110
    * 修復了導致火車提前中止停靠過程的錯誤
    * 修復了兩人同時嘗試停靠同一列火車的問題
    * 多個火車頭的火車現在應該正確停靠
    * 火車現在在轉彎時會傾斜
  * [Patch 0.1.19](/wiki/Patch_0.1.19 "Patch 0.1.19"): 
    * 火車的電力警告
    * 客戶端現在可以部分駕駛火車頭
  * [Patch 0.1.17 build 101353](/wiki/Patch_0.1.17_build_101353 "Patch 0.1.17 build 101353"): 
    * 在駕駛火車時添加了停靠通知
    * 火車AI在前方鐵路被移除時不再卡住
    * 火車現在可以倒車停靠
    * 自動駕駛AI的總體改進
    * 更新了一些火車UI
  * [Patch 0.1.17](/wiki/Patch_0.1.17 "Patch 0.1.17"): 如果火車沒有任何有效的貨運月台，現在應該不會再卡住
  * [Patch 0.1.16](/wiki/Patch_0.1.16 "Patch 0.1.16"): 引入



## References

  1. ↑ [YouTube - Update 5 Trains Collisions, Signals, New "Stop Settings" & more - Train Timetable UI Changes](https://www.youtube.com/watch?v=CskxkIepX6Y&t=889s)
  2. ↑ [YouTube - Update 5 Trains Collisions, Signals, New "Stop Settings" & more - New "Stop Settings" Feature](https://youtu.be/CskxkIepX6Y?t=911s)
  3. ↑ [Satisfactory Q&A Post - How are train paths calculated?](https://questions.satisfactorygame.com/post/6250bd4aca608e080350be1b)
  4. ↑ [YouTube - Update 5 Trains Collisions, Signals, New "Stop Settings" & more - Train Collisions](https://youtu.be/CskxkIepX6Y?t=163s)
  5. ↑ [YouTube - Update 5 Trains Collisions, Signals, New "Stop Settings" & more - Repairing de-railed trains (General)](https://youtu.be/CskxkIepX6Y?t=202s)
  6. ↑ [YouTube - Update 5 Trains Collisions, Signals, New "Stop Settings" & more - Repairing derailed trains (Steps)](https://youtu.be/CskxkIepX6Y?t=240s)
  7. ↑ [YouTube - Update 5 Trains Collisions, Signals, New "Stop Settings" & more - Repairing de-railed trains (Inaccessible)](https://youtu.be/CskxkIepX6Y?t=285s)
  8. ↑ [YouTube - Satisfactory train steam whistle sound](https://www.youtube.com/watch?v=yMwMj7e6DEc)



  * [v](/wiki/Template:VehicleNav "Template:VehicleNav")
  * [e](https://satisfactory.wiki.gg/wiki/Template:VehicleNav?action=edit)
  * [h](https://satisfactory.wiki.gg/wiki/Template:VehicleNav?action=history)

[Transportation](/wiki/Vehicles "Vehicles")  
---  
Motor vehicles| [](/wiki/Tractor "Tractor") [Tractor](/wiki/Tractor "Tractor") • [](/wiki/Truck "Truck") [Truck](/wiki/Truck "Truck") • [](/wiki/Explorer "Explorer") [Explorer](/wiki/Explorer "Explorer") • [](/wiki/Factory_Cart "Factory Cart") [Factory Cart](/wiki/Factory_Cart "Factory Cart") • [](/wiki/Golden_Factory_Cart "Golden Factory Cart") [Golden Factory Cart](/wiki/Golden_Factory_Cart "Golden Factory Cart") • [](/wiki/Cyber_Wagon "Cyber Wagon") [Cyber Wagon](/wiki/Cyber_Wagon "Cyber Wagon") • [](/wiki/Truck_Station "Truck Station") [Truck Station](/wiki/Truck_Station "Truck Station") • [](/wiki/Drone_Port "Drone Port") [Drone Port](/wiki/Drone_Port "Drone Port") • [](/wiki/Drone "Drone") [Drone](/wiki/Drone "Drone")  
Rail vehicles| [](/wiki/Electric_Locomotive "Electric Locomotive") [Electric Locomotive](/wiki/Electric_Locomotive "Electric Locomotive") • [](/wiki/Freight_Car "Freight Car") [Freight Car](/wiki/Freight_Car "Freight Car") • [](/wiki/Train_Station "Train Station") [Train Station](/wiki/Train_Station "Train Station") • [](/wiki/Freight_Platform "Freight Platform") [Freight Platform](/wiki/Freight_Platform "Freight Platform") • [](/wiki/Fluid_Freight_Platform "Fluid Freight Platform") [Fluid Freight Platform](/wiki/Fluid_Freight_Platform "Fluid Freight Platform") • [](/wiki/Empty_Platform "Empty Platform") [Empty Platform](/wiki/Empty_Platform "Empty Platform") • [](/wiki/Empty_Platform_With_Catwalk "Empty Platform With Catwalk") [Empty Platform With Catwalk](/wiki/Empty_Platform_With_Catwalk "Empty Platform With Catwalk") • [](/wiki/Railway "Railway") [Railway](/wiki/Railway "Railway") • [](/wiki/Railroad_Switch_Control "Railroad Switch Control") [Railroad Switch Control](/wiki/Railroad_Switch_Control "Railroad Switch Control") • [](/wiki/Buffer_Stop "Buffer Stop") [Buffer Stop](/wiki/Buffer_Stop "Buffer Stop") • [](/wiki/Block_Signal "Block Signal") [Block Signal](/wiki/Block_Signal "Block Signal") • [](/wiki/Path_Signal "Path Signal") [Path Signal](/wiki/Path_Signal "Path Signal")  
Hypertubes| [](/wiki/Hypertube "Hypertube") [Hypertube](/wiki/Hypertube "Hypertube") • [](/wiki/Hypertube_Entrance "Hypertube Entrance") [Hypertube Entrance](/wiki/Hypertube_Entrance "Hypertube Entrance") • [](/wiki/Hypertube_Support "Hypertube Support") [Hypertube Support](/wiki/Hypertube_Support "Hypertube Support") • [](/wiki/Stackable_Hypertube_Support "Stackable Hypertube Support") [Stackable Hypertube Support](/wiki/Stackable_Hypertube_Support "Stackable Hypertube Support") • [](/wiki/Hypertube_Wall_Hole "Hypertube Wall Hole") [Hypertube Wall Hole](/wiki/Hypertube_Wall_Hole "Hypertube Wall Hole") • [](/wiki/Hypertube_Wall_Support "Hypertube Wall Support") [Hypertube Wall Support](/wiki/Hypertube_Wall_Support "Hypertube Wall Support") • [](/wiki/Hypertube_Floor_Hole "Hypertube Floor Hole") [Hypertube Floor Hole](/wiki/Hypertube_Floor_Hole "Hypertube Floor Hole") • [](/wiki/Hypertube_Junction "Hypertube Junction") [Hypertube Junction](/wiki/Hypertube_Junction "Hypertube Junction") • [](/wiki/Hypertube_Branch "Hypertube Branch") [Hypertube Branch](/wiki/Hypertube_Branch "Hypertube Branch")  
Pioneer transport| [](/wiki/Jump_Pad "Jump Pad") [Jump Pad](/wiki/Jump_Pad "Jump Pad") • [](/wiki/U-Jelly_Landing_Pad "U-Jelly Landing Pad") [U-Jelly Landing Pad](/wiki/U-Jelly_Landing_Pad "U-Jelly Landing Pad") • [](/wiki/Personnel_Elevator "Personnel Elevator") [Personnel Elevator](/wiki/Personnel_Elevator "Personnel Elevator") • [](/wiki/Main_Portal "Main Portal") [Main Portal](/wiki/Main_Portal "Main Portal") • [](/wiki/Satellite_Portal "Satellite Portal") [Satellite Portal](/wiki/Satellite_Portal "Satellite Portal")
  *[v]: View this template
  *[e]: Edit this template
  *[h]: History of this template
  *[his]: his trivia section
