# Customizer/zh

## Customizer/zh  
  
_此建造槍軟體升級為建造選單新增一個標籤：自定義工具。從這裡先驅者可以訪問顏色部分，以及在AWESOME商店購買的材料和圖案選項。_

### Unlocked by

[Tier 2](/wiki/Tier_2 "Tier 2") \- Resource Sink Bonus Program

**自定義工具** 是[建造槍](/wiki/Build_Gun "Build Gun")的擴展，新增了一個建造選單中的標籤。[1]

增加自定義工具的原因是為了擴展先驅者處理可建造物（如地基、牆壁、建築物、機器等）的自定義方式。[2]

## Contents

  * 1 解鎖
  * 2 訪問
  * 3 顏色
    * 3.1 默認
    * 3.2 自定義
    * 3.3 常規
    * 3.4 顏色管理器
    * 3.5 默認分配
    * 3.6 快捷鍵分配
  * 4 材料
    * 4.1 用法
    * 4.2 地基材料
    * 4.3 牆壁材料
    * 4.4 屋頂材料
    * 4.5 快捷欄分配
  * 5 圖案
    * 5.1 使用
      * 5.1.1 應用
      * 5.1.2 移除
    * 5.2 顏色
    * 5.3 反射率
    * 5.4 有效目標
    * 5.5 組
      * 5.5.1 箭頭
      * 5.5.2 圖標
      * 5.5.3 線
      * 5.5.4 數字
      * 5.5.5 路徑
      * 5.5.6 區域
  * 6 外觀
  * 7 當前問題
  * 8 趣聞
  * 9 圖庫
  * 10 歷史
  * 11 參考文獻



### 解鎖

你在第2層，第4里程碑解鎖自定義工具。[3]

最初你只能為可建造物上色，但後來可以在[AWESOME Shop](/wiki/AWESOME_Shop "AWESOME Shop")中購買材料和圖案來解鎖使用，這需要一些進度前提條件。 

### 訪問

通過默認鍵[`X`](/wiki/Controls "Controls")訪問自定義工具，用於自定義[建築](/wiki/Buildings "Buildings")和[車輛](/wiki/Vehicles "Vehicles")的顏色、材料（或紋理）和圖案。也可以通過點擊建造選單中的“自定義工具”標籤訪問自定義工具。 

## 顏色

顏色分為20個色板，由主要顏色和次要顏色組成[4]，這些顏色出現在3個不同的組別中（默認、自定義和常規）。 

默認和常規組中出現的19個色板是“實例化”的，自定義組中的1個色板是“持久化”的。[5]

要使用色板，只需點擊它。選擇色板後，玩家會被提示為目標物體上色。 

  * [](/wiki/File:Customizer_Default_Colors.png "自定義工具默認顏色")

自定義工具默認顏色




### 默認

此組中的顏色將影響**新的可建造物** 。除了地基、混凝土結構和管道有自己的默認色板外，FICSIT工廠色板用於建築、機器、支撐柱等。[6] 和車輛。[7]

當使用任何默認色板時，如果你稍後使用顏色管理器（見下文）更改這些色板中的任何一個，則使用該特定顏色的每個“實例”也會更改。 

名稱  | 圖標  | 主要顏色  | 次要顏色  | 默認活動色板   
---|---|---|---|---  
自定義HSV  
(通用HSV)  | RGB  | 十六進位碼  | 自定義HSV  
(通用HSV)  | RGB  | 十六進位碼   
FICSIT工廠色板  |  | 16, 0.93, 0.95  
(25, 70, 98)  | 250, 149, 73  | #FA9549  | 232, 0.57, 0.26  
(230, 32, 54)  | 95, 102, 140  | #5F668C  | 標準  
車輛   
FICSIT [地基](/wiki/Foundation "Foundation")色板  |  | 0, 0, 0.11  
(0, 0, 36)  | 93, 93, 93  | #5D5D5D  | 16, 0.93, 0.95  
(25, 70, 98)  | 250, 149, 73  | #FA9549  | Ficsit地基   
混凝土結構色板  |  | 0, 0, 1  
(0, 0, 100)  | 255, 255, 255  | #FFFFFF  | 16, 0.93, 0.95  
(25, 70, 98)  | 250, 149, 73  | #FA9549  | 混凝土地基  
塗層混凝土地基  
混凝土牆   
[管道](/wiki/Pipeline "Pipeline")色板  |  | 16, 0.93, 0,96  
(26, 71, 98)  | 250, 149, 73  | #FA9549  | 232, 0.57, 0.26  
(230, 32, 54)  | 95, 102, 140  | #5F668C  | 管道   
  
### 自定義

與其他顏色色板不同，自定義色板是“無後果的”。使用單一自定義色板時，如果稍後使用顏色管理器（見下文）更改色板，任何之前使用此色板上色的可建造物將 _持續_ （不更改）。[8]

名稱  | 圖標  | 主要顏色  | 次要顏色  | 默認活動色板   
---|---|---|---|---  
自定義HSV  
(通用HSV)  | RGB  | 十六進位碼  | 自定義HSV  
(通用HSV)  | RGB  | 十六進位碼   
自定義色板  |  | 16, 0.93, 0.95  
(25, 70, 98)  | 182, 102, 191  | #B666BF  | 232, 0.57, 0.26  
(230, 32, 54)  | 128, 195, 82  | #80C352  | 無   
  
### 常規

使用任何常規顏色色板時，如果稍後使用顏色管理器（見下文）更改這些色板中的任何一個，則使用該特定顏色的每個 _實例_ 也會更改。 

名稱  | 圖標  | 主要顏色  | 次要顏色  | 默認活動色板   
---|---|---|---|---  
自定義HSV  
(通用HSV)  | RGB  | 十六進位碼  | 自定義HSV  
(通用HSV)  | RGB  | 十六進位碼   
色板 1  |  | 211, 0.77, 0.65  
(205, 0.49, 0.83)  | 108, 168, 212  | #6CA8D4  | 36, 0.64, 0.34  
(39, 0.37, 0.61)  | 157, 137, 98  | #9D8962  | 無   
色板 2  |  | 11, 0.91, 0.8  
(18, 0.66, 0.90)  | 232, 125, 77  | #E87D4D  | 234, 0.20, 0.38  
(232, 0.09, 0.65)  | 150, 152, 166  | #9698A6   
色板 3  |  | 236, 0.32, 0.18  
(234, 0.16, 0.46)  | 99, 101, 119  | #636577  | 147, 0.34, 0.36  
(150, 0.17, 0.63)  | 134, 162, 148  | #86A294   
色板 4  |  | 221, 0.08, 0.81  
(220, 0.03, 0.91)  | 224, 227, 233  | #E0E3E9  | 232, 0.57, 0.26  
(230, 0.32, 0.54)  | 95, 102, 140  | #5F668C   
色板 5  |  | 91, 0.61, 0.73  
(87, 0.34, 0.87)  | 187, 222, 146  | #BBDE92  | 232, 0.57, 0.26  
(230, 0.32, 0.54)  | 95, 102, 140  | #5F668C   
色板 6  |  | 319, 0.65, 1.00  
(315, 0.37, 1.00)  | 255, 160, 231  | #FFA0E7  | 232, 0.57, 0.26  
(230, 0.32, 0.54)  | 95, 102, 140  | #5F668C   
色板 7  |  | 176, 0.48, 0.87  
(176, 0.25, 0.94)  | 179, 214, 237  | #B3F1ED  | 232, 0.58, 0.26  
(229, 0.33, 0.54)  | 93, 101, 139  | #5D658B   
色板 8  |  | 35, 0.79, 0.49  
(40, 0.51, 0.72)  | 186, 155, 90  | #BA9B5A  | 180, 0.06, 0.35  
(180, 0.02, 0.62)  | 155, 159, 159  | #9B9F9F   
色板 9  |  | 35, 0.29, 0.96  
(36, 0.13, 0.98)  | 251, 237, 216  | #FBEDD8  | 232, 0.58, 0.26  
(229, 0.33, 0.54)  | 93, 101, 139  | #5D658B   
色板 10  |  | 263, 0.66, 0.98  
(268, 0.38, 0.99)  | 201, 155, 253  | #C99BFD  | 232, 0.58, 0.26  
(229, 0.33, 0.54)  | 93, 101, 139  | #5D658B   
色板 11  |  | 159, 0.69, 0.64  
(162, 0.40, 0.82)  | 124, 210, 185  | #7CD2B9  | 232, 0.58, 0.26  
(229, 0.33, 0.54)  | 93, 101, 139  | #5D658B   
色板 12  |  | 52, 0.65, 0.93  
(53, 0.37, 0.96)  | 247, 237, 154  | #F7ED9A  | 232, 0.58, 0.26  
(229, 0.33, 0.54)  | 93, 101, 139  | #5D658B   
色板 13  |  | 65, 0.14, 0.31  
(65, 0.06, 0.59)  | 150, 151, 141  | #96978D  | 232, 0.58, 0.26  
(229, 0.33, 0.54)  | 93, 101, 139  | #5D658B   
色板 14  |  | 309, 0.79, 0.47  
(306, 0.51, 0.71)  | 183, 88, 173  | #B758AD  | 232, 0.58, 0.26  
(229, 0.33, 0.54)  | 93, 101, 139  | #5D658B   
色板 15  |  | 0, 0, 0.22  
(0, 0, 0.50)  | 130, 130, 130  | #828282  | 235, 0.10, 0.87  
(230, 0.04, 0.94)  | 229, 231, 241  | #E5E7F1   
  
### 顏色管理器

可以通過突出顯示顏色色板並點擊底部的“編輯”來編輯個別色板，這會彈出顏色管理器界面。[9]

可以通過點擊右下角的“保存”圖標並輸入自定義預設名稱來保存顏色預設，以便稍後使用。[10] 要恢復特定顏色色板，請點擊底部中間的“加載預設”。 

顏色可以通過調整各個滑塊來設置，或通過在左下角手動輸入所需的十六進位碼，或通過在右側編輯HSV[note 1]個別值來製作自定義HSV顏色空間，這與常見的HSV顏色空間不同。 

  * **色相** 可以是0°到359°之間的任何度數值。[note 2]
  * **飽和度** 可以是0%（純灰色）到100%（由色相定義的純色）之間的任何百分比值。[note 3]
  * **亮度** 可以是0%（黑色）到100%（全亮度）之間的任何百分比值。[note 3]



註釋： 

  1. ↑ 縮寫[HSV](https://en.wikipedia.org/wiki/HSL_and_HSV)代表色相、飽和度和亮度，也經常稱為HSB（B代表亮度）。
  2. ↑ 色相度數值顯示為0到359的整數。
  3. ↑ 3.0 3.1 飽和度和亮度百分比值顯示為0到1的小數（例如5%顯示為0.05，75%顯示為0.75，100%顯示為1）。



  * [](/wiki/File:Customizer_Color_Manager_1.png "自定義工具顏色管理器 - 顏色編輯")

自定義工具顏色管理器 - 顏色編輯

  * [](/wiki/File:Customizer_Color_Manager_2.png "自定義工具顏色管理器 - 保存預設")

自定義工具顏色管理器 - 保存預設




### 默認分配

可以通過右鍵點擊顏色色板並為各種可建造物分配該顏色色板作為默認顏色來覆蓋默認活動色板。[11][12]另請參見下面的當前問題。 

這不會追溯地將所選色板應用於所選類型的對象，但會將其設置為**新建對象的默認顏色** 。 

例如，如果右鍵點擊色板1並勾選“Ficsit Foundation”，從那時起建造的任何地基都會應用色板1。 

  * [](/wiki/File:Customizer_Color_Assignment.png "自定義工具顏色默認分配")

自定義工具顏色默認分配




### 快捷鍵分配

可以通過突出顯示顏色色板並按數字（0 - 9）將顏色色板綁定到快捷鍵位置來為快捷鍵分配顏色色板。 

## 材料

某些建築可以通過更改其材料來重新設置紋理。嘗試應用已經在使用的材料，或應用於不兼容的建築時，將顯示“無效的自定義目標”錯誤。 

材料有多種類型，出現在3個不同的組別中（地基、牆壁和屋頂）。 

  * [](/wiki/File:Customizer_Materials.png "自定義工具材料")

自定義工具材料




### 用法

可以通過選擇適當的篩選器將建築選單篩選到特定材料。[13] 可以在放置地基、牆壁或屋頂之前，通過按住 [`E`](/wiki/Controls "Controls") 鍵調出快速切換徑向選單，然後使用滑鼠右鍵 [](/wiki/File:Keyboard_White_Mouse_Right.png "Right") 選擇要使用的材料類型來更改材料。[14]

當你的[庫存](/wiki/Inventory "Inventory")**已滿** 時應用材料將導致出現持有未使用材料的[庫存溢出箱](/wiki/Crate "Crate")。[15] 例如，將使用 5x [](/wiki/Concrete "Concrete") [Concrete](/wiki/Concrete "Concrete") 和 2x [](/wiki/Iron_Plate "Iron Plate") [Iron Plate](/wiki/Iron_Plate "Iron Plate") 的[FICSIT 地基](/wiki/Foundations#FICSIT-0 "Foundations")更改為使用 5x [](/wiki/Concrete "Concrete") [Concrete](/wiki/Concrete "Concrete") 和 2x [](/wiki/Plastic "Plastic") [Plastic](/wiki/Plastic "Plastic") 的[塗層混凝土地基材料](/wiki/Foundations#Coated_Concrete-0 "Foundations")，會導致出現包含未使用 2x [](/wiki/Iron_Plate "Iron Plate") [Iron Plate](/wiki/Iron_Plate "Iron Plate") 的一個或多個庫存溢出箱。 

  * [](/wiki/File:Customizer_Materials_Filter.png "使用自定義工具材料建築選單篩選的示例")

使用自定義工具材料建築選單篩選的示例

  * [](/wiki/File:Customizer_Materials_Quick_Switch.png "使用自定義工具材料快速切換的示例")

使用自定義工具材料快速切換的示例

  * [](/wiki/File:Customizer_Material_Change_Crates.png "當更改材料時，由於玩家庫存已滿而產生的庫存溢出箱示例")

當更改材料時，由於玩家庫存已滿而產生的庫存溢出箱示例




### 地基材料

名稱 | 解鎖於 | 先決條件   
---|---|---  
FICSIT 地基 | 始終可用 | [Tier 1, 里程碑 1](/wiki/Milestones#Tier_1 "Milestones") \- 基礎建設   
混凝土地基 | [AWESOME Shop](/wiki/AWESOME_Shop "AWESOME Shop") \- 混凝土地基材料 | [Tier 1, 里程碑 1](/wiki/Milestones#Tier_1 "Milestones") \- 基礎建設   
瀝青地基 | [AWESOME Shop](/wiki/AWESOME_Shop "AWESOME Shop") \- 瀝青地基材料 | [Tier 1, 里程碑 1](/wiki/Milestones#Tier_1 "Milestones") \- 基礎建設  
[Tier 3, 里程碑 2](/wiki/Milestones#Tier_3 "Milestones") \- 車輛運輸   
抓地金屬地基 | [AWESOME Shop](/wiki/AWESOME_Shop "AWESOME Shop") \- 抓地金屬地基材料 | [Tier 1, 里程碑 1](/wiki/Milestones#Tier_1 "Milestones") \- 基礎建設  
[Tier 3, 里程碑 3](/wiki/Milestones#Tier_3 "Milestones") \- 基礎鋼鐵生產   
塗層混凝土地基 | [AWESOME Shop](/wiki/AWESOME_Shop "AWESOME Shop") \- 塗層混凝土地基材料 | [Tier 1, 里程碑 1](/wiki/Milestones#Tier_1 "Milestones") \- 基礎建設  
[Tier 5, 里程碑 1](/wiki/Milestones#Tier_5 "Milestones") \- 石油加工   
  
### 牆壁材料

名稱 | 解鎖於 | 先決條件   
---|---|---  
FICSIT 牆壁 | 始終可用 | [Tier 1, Milestone 1](/wiki/Milestones#Tier_1 "Milestones") \- 基礎建築   
混凝土牆壁 | [AWESOME Shop](/wiki/AWESOME_Shop "AWESOME Shop") \- 混凝土牆壁材料 | [Tier 1, Milestone 1](/wiki/Milestones#Tier_1 "Milestones") \- 基礎建築   
鋼牆壁 | [AWESOME Shop](/wiki/AWESOME_Shop "AWESOME Shop") \- 鋼牆壁材料 | [Tier 1, Milestone 1](/wiki/Milestones#Tier_1 "Milestones") \- 基礎建築  
[Tier 3, Milestone 3](/wiki/Milestones#Tier_3 "Milestones") \- 基本鋼材生產   
  
### 屋頂材料

名稱 | 解鎖於 | 先決條件   
---|---|---  
FICSIT 屋頂 | 始終可用 | [AWESOME Shop](/wiki/AWESOME_Shop "AWESOME Shop") \- FICSIT 屋頂   
焦油屋頂 | [AWESOME Shop](/wiki/AWESOME_Shop "AWESOME Shop") \- 焦油屋頂材料 | [AWESOME Shop](/wiki/AWESOME_Shop "AWESOME Shop") \- FICSIT 屋頂   
玻璃屋頂 | [AWESOME Shop](/wiki/AWESOME_Shop "AWESOME Shop") \- 玻璃屋頂材料 | [AWESOME Shop](/wiki/AWESOME_Shop "AWESOME Shop") \- FICSIT 屋頂  
[石英研究, 節點 3](/wiki/MAM#Quartz "MAM") \- 矽石   
金屬屋頂 | [AWESOME Shop](/wiki/AWESOME_Shop "AWESOME Shop") \- 鋼屋頂材料 | [AWESOME Shop](/wiki/AWESOME_Shop "AWESOME Shop") \- FICSIT 屋頂  
[Tier 3, Milestone 3](/wiki/Milestones#Tier_3 "Milestones") \- 基本鋼材生產   
  
### 快捷欄分配

材料可以綁定到快捷欄，方法是選中使用所需材料的可建築物，然後按數字 (0 - 9) 對應的快捷欄位置來放置材料。[16]

您還可以通過右鍵單擊自定義工具中的材料並選擇**將材料應用於快捷欄建築** 來分配材料類型到快捷欄。[17]

在查看快捷欄時，按住左[`Alt`](/wiki/Controls "Controls")鍵和數字 (0 - 9)，對應當前使用所需材料類型的快捷欄位置。這將把快捷欄上所有適用的其他可建築物切換為相同的材料類型。[18]

  * [](/wiki/File:Customizer_Materials_Hotbar_1.png "自定義工具材料快捷欄分配的示例（主要）")

自定義工具材料快捷欄分配的示例（主要）

  * [](/wiki/File:Customizer_Materials_Hotbar_2.png "自定義工具材料快捷欄分配的示例（替代）。按下了數字8，將快捷欄中1到7的可建築物改變。")

自定義工具材料快捷欄分配的示例（替代）。 _按下了數字8，將快捷欄中1到7的可建築物改變。_




## 圖案

圖案可以應用於[基礎](/wiki/Foundations "Foundations")和[屋頂](/wiki/Roofs "Roofs")，每放置一個圖案需要使用一個[顏料盒](/wiki/Color_Cartridge "Color Cartridge")。 

### 使用

#### 應用

每個基礎只能在其中心應用一個圖案。應用前可以使用滑鼠中鍵[](/wiki/File:Keyboard_White_Mouse_Middle.png "Middle")旋轉圖案。 

應用不同的圖案將替換現有圖案，包括具有不同旋轉角度的相同圖案。應用相同的圖案和相同的旋轉角度將顯示“自定義已應用”的錯誤，因為沒有發生變化。 

  * [](/wiki/File:Customizer_Pattern_Use_Example.png "自定義工具圖案的示例使用")

自定義工具圖案的示例使用




#### 移除

要移除圖案，選擇“圖案移除”。當圖案被移除時，拓荒者不會獲得任何顏料盒。 

  * [](/wiki/File:Pattern_Removal.png "圖案移除（所有圖案組通用）")

圖案移除 _（所有圖案組通用）_




### 顏色

應用圖案的顏色遵循基礎顏色板塊中的**次要顏色** ，該顏色在基礎初始構建或最近更新時使用。 

### 反射率

如同油漆一樣，應用在基礎上的圖案是光亮的，會反射周圍的物品、建築/機械、牆壁、景觀等。[19][20]

使用黑色次要基礎顏色板塊是查看任何反射的最佳選擇，使用其他顏色仍會有反射，但顏色越淺越難看到反射。白色可以被認為是所有圖案顏色中“最不反光”的。 

### 有效目標

所有基礎、倒置基礎、斜坡、雙斜坡、轉角斜坡、倒置轉角斜坡、四分之一管和倒置四分之一管以及屋頂都可以應用圖案，其他無法應用圖案。然而，在有效目標中，應用於玻璃和框架基礎、屋頂、四分之一管和倒置四分之一管的圖案將不可見。 

將新材料應用於有圖案的基礎時，也會通過旋轉材料來旋轉圖案。 

### 組

自定義工具圖案顯示在6個不同的組中。 

#### 箭頭

類型 | 圖標 | 名稱 | 解鎖於 | 先決條件   
---|---|---|---|---  
所有  | [](/wiki/File:Arrow_Straight.png) | 直箭頭  | [AWESOME Shop](/wiki/AWESOME_Shop "AWESOME Shop") \- 自定義工具 - 箭頭圖案  | [第2級, 第4里程碑](/wiki/Milestones#Tier_2 "Milestones") \- 資源回收獎勵計劃   
[](/wiki/File:Arrow_Left.png) | 左箭頭   
[](/wiki/File:Arrow_Right.png) | 右箭頭   
[](/wiki/File:Arrow_U-Turn.png) | U形箭頭   
[](/wiki/File:Arrow_Straight_No.png) | 禁止直行箭頭   
[](/wiki/File:Arrow_Left_No.png) | 禁止左轉箭頭   
[](/wiki/File:Arrow_Right_No.png) | 禁止右轉箭頭   
  
#### 圖標

類型 | 圖標 | 名稱 | 解鎖於 | 先決條件   
---|---|---|---|---  
工廠  | [](/wiki/File:Icon_Factory.png) | 工廠圖標  | [AWESOME Shop](/wiki/AWESOME_Shop "AWESOME Shop") \- 自定義工具 - 工廠圖標圖案  | [第2級, 第4里程碑](/wiki/Milestones#Tier_2 "Milestones") \- 資源回收獎勵計劃   
[](/wiki/File:Icon_Power.png) | 電力圖標   
[](/wiki/File:Icon_Storage.png) | 儲存圖標   
[](/wiki/File:Icon_Nuclear_Warning.png) | 核警告圖標   
[](/wiki/File:Icon_Liquid.png) | 液體圖標   
[](/wiki/File:Icon_Cross.png) | 十字圖標   
[](/wiki/File:Icon_Pioneer.png) | 拓荒者圖標   
[](/wiki/File:Icon_Pioneer_No.png) | 禁止拓荒者圖標   
運輸  | [](/wiki/File:Icon_Tractor.png) | 拖拉機圖標  | [AWESOME Shop](/wiki/AWESOME_Shop "AWESOME Shop") \- 自定義工具 - 運輸圖標圖案  | [第2級, 第4里程碑](/wiki/Milestones#Tier_2 "Milestones") \- 資源回收獎勵計劃   
[](/wiki/File:Icon_Truck.png) | 卡車圖標   
[](/wiki/File:Icon_Explorer.png) | 探險車圖標   
[](/wiki/File:Icon_Factory_Cart.png) | 工廠手推車圖標   
[](/wiki/File:Icon_Factory_Cart_No.png) | 禁止工廠手推車圖標   
[](/wiki/File:Icon_Parking.png) | 停車圖標   
[](/wiki/File:Icon_Parking_No.png) | 禁止停車圖標   
  
#### 線

類型 | 圖標 | 名稱 | 解鎖於 | 先決條件   
---|---|---|---|---  
實線  | [](/wiki/File:Line_Center.png) | 中心線  | [AWESOME Shop](/wiki/AWESOME_Shop "AWESOME Shop") \- 自定義工具 - 實線圖案  | [第2級, 第4里程碑](/wiki/Milestones#Tier_2 "Milestones") \- 資源回收獎勵計劃   
[](/wiki/File:Line_Center_Corner.png) | 中心轉角線   
[](/wiki/File:Line_Split.png) | 分割線   
[](/wiki/File:Line_Cross.png) | 交叉線   
[](/wiki/File:Line_Side.png) | 側邊線   
[](/wiki/File:Line_Side_Corner.png) | 側邊轉角線   
[](/wiki/File:Line_Double.png) | 雙線   
虛線  | [](/wiki/File:Line_Center_Dotted.png) | 中心虛線  | [AWESOME Shop](/wiki/AWESOME_Shop "AWESOME Shop") \- 自定義工具 - 虛線圖案  | [第2級, 第4里程碑](/wiki/Milestones#Tier_2 "Milestones") \- 資源回收獎勵計劃   
[](/wiki/File:Line_Center_Corner_Dotted.png) | 中心轉角虛線   
[](/wiki/File:Line_Split_Dotted.png) | 分割虛線   
[](/wiki/File:Line_Cross_Dotted.png) | 交叉虛線   
[](/wiki/File:Line_Side_Dotted.png) | 側邊虛線   
[](/wiki/File:Line_Side_Corner_Dotted.png) | 側邊轉角虛線   
[](/wiki/File:Line_Double_Dotted.png) | 雙虛線   
  
#### 數字

類型 | 圖標 | 名稱 | 解鎖於 | 先決條件   
---|---|---|---|---  
所有  | [](/wiki/File:Number_0.png) | 數字 0  | [AWESOME Shop](/wiki/AWESOME_Shop "AWESOME Shop") \- 自定義工具 - 數字圖案  | [第2級, 第4里程碑](/wiki/Milestones#Tier_2 "Milestones") \- 資源回收獎勵計劃   
[](/wiki/File:Number_1.png) | 數字 1   
[](/wiki/File:Number_2.png) | 數字 2   
[](/wiki/File:Number_3.png) | 數字 3   
[](/wiki/File:Number_4.png) | 數字 4   
[](/wiki/File:Number_5.png) | 數字 5   
[](/wiki/File:Number_6.png) | 數字 6   
[](/wiki/File:Number_7.png) | 數字 7   
[](/wiki/File:Number_8.png) | 數字 8   
[](/wiki/File:Number_9.png) | 數字 9   
  
#### 路徑

類型 | 圖標 | 名稱 | 解鎖於 | 先決條件   
---|---|---|---|---  
工廠  | [](/wiki/File:Path_Straight.png) | 直線路徑  | [AWESOME Shop](/wiki/AWESOME_Shop "AWESOME Shop") \- 自定義工具 - 路徑圖案  | [第2級, 第4里程碑](/wiki/Milestones#Tier_2 "Milestones") \- 資源回收獎勵計劃   
[](/wiki/File:Path_Corner.png) | 轉角路徑   
[](/wiki/File:Path_Split.png) | 分叉路徑   
[](/wiki/File:Path_Cross.png) | 交叉路徑   
[](/wiki/File:Path_Pioneer.png) | 拓荒者路徑   
[](/wiki/File:Path_Cart.png) | 手推車路徑   
[](/wiki/File:Path_Small_Crosswalk.png) | 小型斑馬線   
運輸  | [](/wiki/File:Path_Large_Crosswalk.png) | 大型斑馬線  | [AWESOME Shop](/wiki/AWESOME_Shop "AWESOME Shop") \- 自定義工具 - 運輸圖案  | [第2級, 第4里程碑](/wiki/Milestones#Tier_2 "Milestones") \- 資源回收獎勵計劃   
  
#### 區域

類型 | 圖標 | 名稱 | 解鎖於 | 先決條件   
---|---|---|---|---  
所有  | [](/wiki/File:Zone_Full_Factory.png) | 全廠區  | [AWESOME Shop](/wiki/AWESOME_Shop "AWESOME Shop") \- 自定義工具 - 廠區圖案  | [第2級, 第4里程碑](/wiki/Milestones#Tier_2 "Milestones") \- 資源回收獎勵計劃   
[](/wiki/File:Zone_Half_Factory.png) | 半廠區   
[](/wiki/File:Zone_Quarter_Factory.png) | 四分之一廠區   
[](/wiki/File:Zone_Factory_Line.png) | 廠區線   
  
## 外觀

目前，自定義工具只有在[FICSMAS季節性活動](/wiki/FICSMAS "FICSMAS")中解鎖的基本和高級皮膚。解鎖後，自定義工具UI中將添加一個額外的**外觀** 標籤。 

另見: [FICSMAS 自定義工具皮膚](/wiki/FICSMAS#Customizer_skins "FICSMAS")

  * [](/wiki/File:Customizer_-_Basic_FICSMAS_Skin.png "自定義工具 FICSMAS 基本皮膚。於2021年FICSMAS第5天引入。")

自定義工具 FICSMAS 基本皮膚。於2021年FICSMAS第5天引入。

  * [](/wiki/File:Customizer_-_Premium_FICSMAS_Skin.png "自定義工具 FICSMAS 高級皮膚。於2021年FICSMAS第11天引入。")

自定義工具 FICSMAS 高級皮膚。於2021年FICSMAS第11天引入。




## 當前問題

由於當前問題，自定義顏色樣板不應設為任何建造物的默認顏色。參見 [自定義工具將永遠把所有東西變成黑色](https://questions.satisfactorygame.com/post/61cccf45831c852052367613)。 

## 趣聞

  * 在更新5中引入自定義工具的同時，也引入了由Coffee Stain Studios社區經理扮演的角色Snutty Mays ([Snutt Treptow](/wiki/Coffee_Stain_Studios#Snutt "Coffee Stain Studios"))和Juice Velvet ([Jace Varlet](/wiki/Coffee_Stain_Studios#Jace "Coffee Stain Studios"))，這些角色在本Wiki的其他地方也有提及。[21]
  * [Snutt](/wiki/Snutt "Snutt") 為自定義工具創作了一首主題曲。[22]
  * 用戶u/Vencam 為自定義工具列出了一個遊戲中顏色的巨大清單。[在r/SatisfactoryGame上查找它](https://www.reddit.com/r/SatisfactoryGame/comments/ukl1t6/psa_list_of_colours_ive_accrued_so_far_as_close/)



## 圖庫

  * [](/wiki/File:Customizer_Introduction.png "自定義工具介紹，顯示Snutty Mays和Juice Velvet（見趣聞）")

自定義工具介紹，顯示Snutty Mays和Juice Velvet（見趣聞）

  * [](/wiki/File:Customizer_Advertisement.jpg "自定義工具假廣告，如在現已停用網站所見")

自定義工具假廣告，如在[現已停用網站](https://www.customizer-4-lyfe.com)所見

  * [](/wiki/File:Customizer_Ad.png "自定義工具圖案的假廣告")

自定義工具圖案的假廣告




## 歷史

  * [Patch 0.8.2.0](/wiki/Patch_0.8.2.0 "Patch 0.8.2.0"): 修復了在快速切換菜單中更改材料（自定義工具）後首次使用後停止工作的問題
  * [Patch 0.8.0.4](/wiki/Patch_0.8.0.4 "Patch 0.8.0.4")
    * 修復了在啟用無建造成本時自定義工具仍從庫存中消耗資源的問題
    * 修復了在啟用無建造成本時，自定義工具材料和圖案的退款問題（所以你的庫存不會充滿你不想要的東西）
    * 修復了使用自定義篩選器時與自定義工具相關的崩潰
  * [Patch 0.7.0.8](/wiki/Patch_0.7.0.8 "Patch 0.7.0.8"): 添加了在嘗試保存具有相同名稱的顏色選取器預設時的反饋
  * [Patch 0.7.0.6](/wiki/Patch_0.7.0.6 "Patch 0.7.0.6")
    * 修復了必須點擊兩次基礎、牆壁和屋頂材料篩選器，以便顯示“將材料應用於快捷鍵建築”按鈕的問題
    * 添加了在嘗試保存具有相同名稱的顏色選取器預設時的反饋
  * [Patch 0.7.0.5](/wiki/Patch_0.7.0.5 "Patch 0.7.0.5"): 修復了顏色預設名稱無字符限制的問題
  * [Patch 0.6.0.12](/wiki/Patch_0.6.0.12 "Patch 0.6.0.12"): 修復了玩家可以在未解鎖之前打開自定義工具菜單的問題
  * [Patch 0.6.0.10](/wiki/Patch_0.6.0.10 "Patch 0.6.0.10")
    * 無法上色的建築現在應該可以上色
    * 修復了某些情況下自定義工具UI顯示N/A的問題
  * [Patch 0.6.0.4](/wiki/Patch_0.6.0.4 "Patch 0.6.0.4"): 修復了如果在顏色選取器打開時關閉[建造菜單](/wiki/Build_Gun "Build Gun")/ 自定義工具，所有玩家輸入都會停止工作的問題
  * [Patch 0.6.0.0](/wiki/Patch_0.6.0.0 "Patch 0.6.0.0"): 設備現在將被著色為自定義工具中選擇的默認工廠顏色
  * [Patch 0.5.0.13](/wiki/Patch_0.5.0.13 "Patch 0.5.0.13"): 修復了[電力線](/wiki/Power_Line "Power Line")能夠被選為自定義工具目標的問題，這會導致應用顏色樣板後顯示異常
  * [Patch 0.5.0.12](/wiki/Patch_0.5.0.12 "Patch 0.5.0.12")
    * 引入了現在可以在[AWESOME Shop](/wiki/AWESOME_Shop "AWESOME Shop")購買的瀝青基礎材料
    * 修復了與顏色樣板相關的崩潰問題，受影響的玩家可能仍需應用正確的默認值來恢復一切正常。
    * 添加了一些後備數據，使受空顏色樣板組影響的保存可以恢復其顏色樣板
    * 修復了[Pipeline](/wiki/Pipeline "Pipeline")建築上的顏色樣板問題
  * [Patch 0.5.0.11](/wiki/Patch_0.5.0.11 "Patch 0.5.0.11"): 修復了上次更新後，一些自定義工具FICSIT工廠顏色樣板錯誤應用於某些[Foundation](/wiki/Foundation "Foundation")類型的問題
  * [Patch 0.5.0.10](/wiki/Patch_0.5.0.10 "Patch 0.5.0.10"): 修復了自定義工具中的搜索功能無法正常工作
  * [Patch 0.5.0.9](/wiki/Patch_0.5.0.9 "Patch 0.5.0.9"): 修復了自定義工具圖案不再根據基礎旋轉（加倍）的問題
  * [Patch 0.5.0.6](/wiki/Patch_0.5.0.6 "Patch 0.5.0.6"): 修復了自定義工具快捷方式在離線保存中被擦除的問題
  * [Patch 0.5.0.2](/wiki/Patch_0.5.0.2 "Patch 0.5.0.2") _(再次發布於[Patch 0.5.0.3](/wiki/Patch_0.5.0.3 "Patch 0.5.0.3"))_: 修復了[Multiplayer](/wiki/Multiplayer "Multiplayer") / [Dedicated Servers](/wiki/Dedicated_Servers "Dedicated Servers")客戶端無法在自定義工具中保存或刪除顏色預設的問題
  * [Patch 0.5.0.0](/wiki/Patch_0.5.0.0 "Patch 0.5.0.0"): 引入，替代了顏色槍（包括顏色樣板、圖案和材料）



## 參考文獻

  1. ↑ [YouTube - The CUSTOMIZER and Update 5 RELEASE DATE - Customizer General Information 1](https://youtu.be/8Tok_vdqZH8?t=55)
  2. ↑ [YouTube - The CUSTOMIZER and Update 5 RELEASE DATE - Customizer General Information 2](https://youtu.be/8Tok_vdqZH8?t=75)
  3. ↑ [YouTube - The CUSTOMIZER and Update 5 RELEASE DATE - Customizer Unlocking](https://youtu.be/8Tok_vdqZH8?t=133)
  4. ↑ [YouTube - The CUSTOMIZER and Update 5 RELEASE DATE - Customizer Colors - General](https://youtu.be/8Tok_vdqZH8?t=399)
  5. ↑ [YouTube - The CUSTOMIZER and Update 5 RELEASE DATE - Customizer Colors - Description](https://youtu.be/8Tok_vdqZH8?t=472)
  6. ↑ [YouTube - The CUSTOMIZER and Update 5 RELEASE DATE - Customizer Default Color - General](https://youtu.be/8Tok_vdqZH8?t=597)
  7. ↑ [YouTube - The CUSTOMIZER and Update 5 RELEASE DATE - Customizer Default Color - Vehicles](https://youtu.be/8Tok_vdqZH8?t=625)
  8. ↑ [YouTube - The CUSTOMIZER and Update 5 RELEASE DATE - Customizer Custom Color](https://youtu.be/8Tok_vdqZH8?t=519)
  9. ↑ [YouTube - The CUSTOMIZER and Update 5 RELEASE DATE - Customizer Color Manager - General](https://youtu.be/8Tok_vdqZH8?t=417)
  10. ↑ [YouTube - The CUSTOMIZER and Update 5 RELEASE DATE - Customizer Color Manager - Saving Color Presets](https://youtu.be/8Tok_vdqZH8?t=440)
  11. ↑ [YouTube - The CUSTOMIZER Guide - Everything You Need To Know Satisfactory Update 6 - Default Assignment](https://www.youtube.com/watch?v=Mxh4Qx2xY_Y&t=163s)
  12. ↑ [Reddit - TIL: Right click a color swatch and change the default color for newly constructed buildings](https://www.reddit.com/r/SatisfactoryGame/comments/rwvm85/til_right_click_a_color_swatch_and_change_the/)
  13. ↑ [YouTube - The CUSTOMIZER and Update 5 RELEASE DATE - Customizer Materials - Build Menu Filter](https://youtu.be/8Tok_vdqZH8?t=225)
  14. ↑ [YouTube - The CUSTOMIZER and Update 5 RELEASE DATE - Customizer Materials - Quick Switch](https://youtu.be/8Tok_vdqZH8?t=726)
  15. ↑ [Reddit - Coated Concrete creating crates?](https://www.reddit.com/r/SatisfactoryGame/comments/1dr4qyw/coated_concrete_creating_crates/)
  16. ↑ [YouTube - The CUSTOMIZER and Update 5 RELEASE DATE - Customizer Materials - Hotbar Assignment](https://youtu.be/8Tok_vdqZH8?t=248)
  17. ↑ [YouTube - The CUSTOMIZER and Update 5 RELEASE DATE - Customizer Materials - Hotbar Assignment - Tip 1](https://youtu.be/8Tok_vdqZH8?t=767)
  18. ↑ [YouTube - The CUSTOMIZER and Update 5 RELEASE DATE - Customizer Materials - Hotbar Assignment - Tip 2](https://youtu.be/8Tok_vdqZH8?t=805)
  19. ↑ [YouTube - The CUSTOMIZER and Update 5 RELEASE DATE - Using Patterns](https://www.youtube.com/watch?v=8Tok_vdqZH8&t=295s)
  20. ↑ [Reddit - How did Snutt get a reflective pattern on the floor?](https://www.reddit.com/r/SatisfactoryGame/comments/18e0b3y/how_did_snutt_get_a_reflective_pattern_on_the/)
  21. ↑ [YouTube - Satisfactory Update 5 OUT NOW on Experimental - Patch Notes Video - Snutty Mays & Juice Velvet Talk: Introducing The Customizer™](https://youtu.be/QfaReoks6OM?t=273s)
  22. ↑ [YouTube - The CUSTOMIZER and Update 5 RELEASE DATE - Theme song for the Customizer](https://www.youtube.com/clip/UgkxRTK8kKuLF_XwhQLqEYE7gwhyYN6mejyy)



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
Other| [Hypertube cannon](/wiki/Tutorial:Hypertube_cannon "Tutorial:Hypertube cannon") • [Hypertube brake](/wiki/Tutorial:Hypertube_brake "Tutorial:Hypertube brake") • [Steam Deck & Controller setup](/wiki/Tutorial:Controller_setup "Tutorial:Controller setup") • [Extracting UI icons](/wiki/Tutorial:Extracting_UI_icons "Tutorial:Extracting UI icons")
  *[v]: View this template
  *[e]: Edit this template
  *[h]: History of this template
  *[his]: his trivia section
