# Template:Infobox simple/sandbox/doc

[](/wiki/File:Template-info.svg) Documentation

[[purge](https://satisfactory.wiki.gg/wiki/Template:Infobox_simple/sandbox/doc?action=purge)]

Infobox simple is an all-purpose infobox for building, item, fluid and vehicle pages. 

## Contents

  * 1 Parameters
    * 1.1 Common
    * 1.2 Unseen
    * 1.3 Building
    * 1.4 Vehicle
    * 1.5 Dimensions
    * 1.6 Item
    * 1.7 Equipment
    * 1.8 Fuel
    * 1.9 Ingredients
  * 2 Example



## Parameters

### Common

Parameter | Type | Description   
---|---|---  
name | Page | Infobox title, used for cargo; defaults to PAGENAME   
displayName | Strings | Overrides "name", but only for the infobox title (visually)   
image | Page | Defaults to "name".png   
description | String | Infobox description   
researchTier | Wikitext | Tier and milestone, MAM research or other source which unlocks the building   
category | String | Build menu tab (wiki categorization can be disabled with "noCategories")   
subCategory | String | Build menu category   
blueprintPath | String | Blueprint path   
  
### Unseen

Parameter | Type | Description   
---|---|---  
noCategories | Boolean | Disables all categorization if true   
noCargo | Boolean | Disables all cargo storing if true   
recipeName | String | Defaults to PAGENAME, recipe name (eponymous for buildings)   
experimental | Boolean | Whether the recipe is available only in the Experimental branch   
unreleased | Boolean | Whether the recipe is unreleased or otherwise unavailable   
alternateRecipe | Boolean | Whether the recipe is an alternate recipe (rarely used)   
mainRecipe | Boolean | Whether the recipe is the primary recipe (rarely used)   
product | Page | Defaults to PAGENAME, the actual product (rarely used)   
productCount | Integer | Defaults to 1, the actual product count (rarely used)   
bioFuel | Boolean | Whether the fuel is a valid fuel for the Biomass Burner   
  
### Building

Parameter | Type | Description   
---|---|---  
inventorySize | String | Building inventory size, in stacks or m3; also appears in the Vehicle section   
powerUsage | String | Power usage in MW   
powerGenerated | Float | Power generated in MW   
fuel | Wikitext | Accepted fuel; also appears in the Vehicle section   
overclockable | Boolean | Whether the building is overclockable   
inputs | Wikitext | Amount of inputs   
outputs | Wikitext | Amount of outputs   
  
### Vehicle

Parameter | Type | Description   
---|---|---  
maxSpeed | Float | Important parameter, determines whether the Vehicle or Building group is used for colliding parameters   
inventorySize | String | Vehicle inventory size, in stacks; also appears in the Building section   
time0_50 | Float | Time to reach 50 km/h in seconds   
power | Float | Fuel burn rate   
fuel | Wikitext | Accepted fuel; also appears in the Building section   
  
### Dimensions

Parameter | Type | Description   
---|---|---  
size_width | String | Width in meters   
size_length | String | Length in meters   
size_height | String | Height in meters   
size_note | String | Additional size information, such as whether the building is stackable   
  
### Item

Parameter | Type | Description   
---|---|---  
stackSize | Integer | Stack size   
isRadioactive | Integer | Radioactive decay value (acquired from Docs.json)   
  
### Equipment

Parameter | Type | Description   
---|---|---  
ammo | Page | Item used as ammo (or as a consumable, such as Gas Filters for the Gas Mask)   
magSize | String | Magazine size per reload   
damage | String | Damage per hit   
rateOfFire | String | Rate of fire   
reloadTime | String | Reload time in seconds   
range | String | Effective range in meters   
  
### Fuel

Parameter | Type | Description   
---|---|---  
energy | Integer OR "N/A" | Energy per item or M3 in MJ   
  
### Ingredients

Parameter | Type | Description   
---|---|---  
craftedIn | Page | Building or tool used to craft the product   
ingredientX | Page | Count of the Xth ingredient (X ranges 1–10)   
quantityX | Float | Xth ingredient, ordered the same way as in-game   
  
## Example
    
    
    {{Infobox simple/sandbox
     | description = Crafts two parts into another part.<br/>Can be automated by feeding parts into it with a conveyor belt connected to the input. The produced parts can be automatically extracted by connecting a conveyor belt to the output.
     | category = Production
     | subCategory = Manufacturers
     | researchTier = [[Tier 2]] - Part Assembly
     | powerUsage = 15
     | overclockable = Yes
     | craftedIn = Build Gun
     | inputs = 2
     | outputs = 1
     | quantity1 = 8
     | ingredient1 = Reinforced Iron Plate
     | quantity2 = 4
     | ingredient2 = Rotor
     | quantity3 = 10
     | ingredient3 = Cable
     | size_width = 10
     | size_length = 15
     | size_height = 10
     }}
    

## Infobox simple/sandbox/doc

_Crafts two parts into another part.  
Can be automated by feeding parts into it with a conveyor belt connected to the input. The produced parts can be automatically extracted by connecting a conveyor belt to the output._

### Unlocked at

[Tier 2](/wiki/Tier_2 "Tier 2") \- Part Assembly

### Category

[Production](/wiki/Category:Production_buildings?action=edit&redlink=1 "Category:Production buildings \(page does not exist\)")

### Sub-category

[Manufacturers](/wiki/Category:Manufacturers?action=edit&redlink=1 "Category:Manufacturers \(page does not exist\)")

## Building

### [Power usage](/wiki/Power "Power")

15 MW

### [Overclock-able](/wiki/Overclock "Overclock")

Yes

### Inputs

2

### Outputs

1

## Dimensions

### Width

10 m

### Length

15 m

### Height

10 m

### Area

150 m2

## Ingredients

### Made in

Build Gun

**8×** [](/wiki/Reinforced_Iron_Plate "Reinforced Iron Plate") [Reinforced Iron Plate](/wiki/Reinforced_Iron_Plate "Reinforced Iron Plate")

**4×** [](/wiki/Rotor "Rotor") [Rotor](/wiki/Rotor "Rotor")

**10×** [](/wiki/Cable "Cable") [Cable](/wiki/Cable "Cable")

This is the documentation page, it should be transcluded into the main template page. See [Template:Doc](/wiki/Template:Doc "Template:Doc") for more information.
  *[v]: View this template
  *[e]: Edit this template
  *[h]: History of this template
  *[his]: his trivia section
  *[N/A]: Not applicable
