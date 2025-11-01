# Template:Infobox simple/ko/doc

[](/wiki/File:Template-info.svg) Documentation

[[purge](https://satisfactory.wiki.gg/wiki/Template:Infobox_simple/ko/doc?action=purge)]

Infobox simple은 건물, 항목, 유체 및 차량 정보를 표시하기 위한 다목적 템플릿입니다. 

## Contents

  * 1 매개 변수
    * 1.1 기본
    * 1.2 숨기기
    * 1.3 건물
    * 1.4 차량
    * 1.5 치수
    * 1.6 아이템
    * 1.7 장비
    * 1.8 연료
    * 1.9 재료
  * 2 예시



## 매개 변수

### 기본

매개 변수 | 유형 | 설명   
---|---|---  
name | Page | 템플릿의 “name”을 정합니다. 기본값은 문서 이름입니다.   
displayName | Strings | 문서 이름과 다를 경우 사용합니다.   
image | Page | 기본값은 "name".png입니다.   
description | String | 템플릿의 내용을 추가하기 위해 사용됩니다.   
researchTier | Wikitext | Tier와 해제 조건을 표시하기 위해 사용됩니다.   
category | String | 건물 분류를 표시하기 위해 사용됩니다. (wiki 분류는 “noCategories”으로 비활성화할 수 있습니다.)   
subCategory | String | 건물 하위 분류를 표시하기 위해 사용됩니다.   
blueprintPath | String | 청사진 경로를 표시하기 위해 사용됩니다.   
  
### 숨기기

매개 변수 | 유형 | 설명   
---|---|---  
noCategories | Boolean | true인 경우 모든 분류를 비활성화합니다.   
noCargo | Boolean | true인 경우 모든 cargo storing을 비활성화합니다.   
recipeName | String | recipe name (eponymous for buildings) 기본값은 문서 이름입니다.   
experimental | Boolean | 실험 버전에서만 사용할 수 있는지 여부를 결정합니다.   
unreleased | Boolean | 제작법이 공개되지 않았거나 다른 방법으로 얻을 수 없는지를 나타냅니다.   
alternateRecipe | Boolean | 제작법이 대체 제작법인지 아닌지를 결정합니다. (거의 사용하지 않습니다.)   
mainRecipe | Boolean | 제작법이 기본 제작법인지 아닌지를 결정합니다. (거의 사용하지 않습니다.)   
product | Page | the actual product 기본값은 문서 이름입니다. (거의 사용하지 않습니다.)   
productCount | Integer | the actual product count 기본값은 1입니다. (거의 사용하지 않습니다.)   
bioFuel | Boolean | Whether the fuel is a valid fuel for the Biomass Burner   
  
### 건물

매개 변수 | 유형 | 설명   
---|---|---  
inventorySize | String | 건물 인벤토리 크기를 표시하기 위해 사용됩니다. 또한 차량 부분에서도 사용됩니다.   
powerUsage | String | 전기사용량(MW)을 추가하기 위해 사용됩니다.   
powerGenerated | String | 전기생산량(MW)을 추가하기 위해 사용됩니다.   
fuel | Wikitext | 사용할 수 있는 연료를 표시하기 위해 사용됩니다. 또한 차량 부분에서도 사용됩니다.   
overclockable | Boolean | 건물의 오버클럭 가능한지 여부를 결정합니다.   
inputs | Wikitext | 총입력을 추가하기 위해 사용됩니다.   
outputs | Wikitext | 총출력을 추가하기 위해 사용됩니다.   
  
### 차량

매개 변수 | 유형 | 설명   
---|---|---  
maxSpeed | Float | 중요한 매개 변수, determines whether the Vehicle or Building group is used for colliding parameters  
평평한 직선 경로에서 차량의 최대 속도를 표시합니다.   
inventorySize | String | 차량의 인벤토리 크기를 표시하기 위해 사용됩니다. 또한 건물 부분에서도 사용됩니다.   
time0_50 | Float | 50km/h까지 걸리는 시간(s)을 표시하기 위해 사용됩니다.   
power | Float | 연료 연소율을 표시하기 위해 사용됩니다.   
fuel | Wikitext | 사용할 수 있는 연료를 표시하기 위해 사용됩니다. 또한 건물 부분에서도 사용됩니다.   
  
### 치수

매개 변수 | 유형 | 설명   
---|---|---  
size_width | String | 너비(m)를 표시하기 위해 사용됩니다.   
size_length | String | 길이(m)를 표시하기 위해 사용됩니다.   
size_height | String | 높이(m)를 표시하기 위해 사용됩니다.   
size_note | String | 적층 가능 여부와 추가 크기 정보를 표시하기 위해 사용됩니다.   
  
### 아이템

매개 변수 | 유형 | 설명   
---|---|---  
stackSize | Integer | 한 세트의 양을 표시하기 위해 사용됩니다.   
isRadioactive | Integer | Radioactive decay value (acquired from Docs.json)   
  
### 장비

매개 변수 | 유형 | 설명   
---|---|---  
ammo | Page | 사용할 수 있는 탄약을 표시하기 위해 사용됩니다. (또는 가스 필터와 같은 소모품)   
magSize | String | 재장전 탄창 크기를 표시하기 위해 사용됩니다.   
damage | String | 타격당 대미지를 표시하기 위해 사용됩니다.   
rateOfFire | String | 발사 속도를 표시하기 위해 사용됩니다.   
reloadTime | String | 재장전 시간(s)을 표시하기 위해 사용됩니다.   
damagePerSecond | String | 초당 피해량을 표시하기 위해 사용됩니다.   
range | String | 유효 사거리를 표시하기 위해 사용됩니다.   
  
### 연료

매개 변수 | 유형 | 설명   
---|---|---  
energy | Integer OR "N/A" | Energy per item or m3 in MJ   
  
### 재료

매개 변수 | 유형 | 설명   
---|---|---  
craftedIn | Page | 제품을 제작하는 데 사용되는 건물 또는 도구를 표시합니다.   
ingredientX | Page | X 번째의 재료 이름, 인게임과 같은 재료로 표시해야 합니다. (X의 범위는 1–10)   
quantityX | Float | X 번째의 재료 총개수   
  
## 예시
    
    
    {{Infobox simple/ko
     | description = 부품 두 개를 결합하여 다른 부품을 만듭니다.<br/>입력부에 컨베이어 벨트로 부품을 공급함으로써 자동화가 가능합니다. 제조된 부품은 출력부에 연결된 컨베이어 벨트를 통해 자동으로 배출됩니다.
     | category = Production
     | subCategory = Manufacturers
     | researchTier = [[Tier 2]] - Part Assembly
     | powerUsage = 15
     | overclockable = 가능
     | craftedIn = Build Gun
     | inputs = 2
     | outputs = 1
     | quantity1 = 8
     | ingredient1 = 보강된 철판
     | quantity2 = 4
     | ingredient2 = 회전자
     | quantity3 = 10
     | ingredient3 = 케이블
     | size_width = 10
     | size_length = 15
     | size_height = 10
     }}
    

## 조립기

[ ](/wiki/File:%EC%A1%B0%EB%A6%BD%EA%B8%B0.png "조립기.png")

_부품 두 개를 결합하여 다른 부품을 만듭니다.  
입력부에 컨베이어 벨트로 부품을 공급함으로써 자동화가 가능합니다. 제조된 부품은 출력부에 연결된 컨베이어 벨트를 통해 자동으로 배출됩니다._

### 해금 조건

[Tier 2](/wiki/Tier_2 "Tier 2") \- 부품 조립

### 분류

[Production](/wiki/Category:Production_buildings?action=edit&redlink=1 "Category:Production buildings \(page does not exist\)")

### 하위­ 분류

[Manufacturers](/wiki/Category:Manufacturers?action=edit&redlink=1 "Category:Manufacturers \(page does not exist\)")

## 건물

### [전기 소모량](/wiki/Power "Power")

15 MW

### [오버클럭­](/wiki/Overclock "Overclock")

가능

### 입력부

2

### 출력부

1

## 치수

### 너비

10 m

### 길이

15 m

### 높이

10 m

### 면적

150 m2

## 재료

### 도구

Build Gun

**8×** [](/wiki/%EB%B3%B4%EA%B0%95%EB%90%9C_%EC%B2%A0%ED%8C%90 "보강된 철판") [보강된 철판](/wiki/%EB%B3%B4%EA%B0%95%EB%90%9C_%EC%B2%A0%ED%8C%90?action=edit&redlink=1 "보강된 철판 \(page does not exist\)")

**4×** [](/wiki/%ED%9A%8C%EC%A0%84%EC%9E%90 "회전자") [회전자](/wiki/%ED%9A%8C%EC%A0%84%EC%9E%90?action=edit&redlink=1 "회전자 \(page does not exist\)")

**10×** [](/wiki/%EC%BC%80%EC%9D%B4%EB%B8%94 "케이블") [케이블](/wiki/%EC%BC%80%EC%9D%B4%EB%B8%94?action=edit&redlink=1 "케이블 \(page does not exist\)")

This is the documentation page, it should be transcluded into the main template page. See [Template:Doc](/wiki/Template:Doc "Template:Doc") for more information.
  *[v]: View this template
  *[e]: Edit this template
  *[h]: History of this template
  *[his]: his trivia section
  *[N/A]: Not applicable
