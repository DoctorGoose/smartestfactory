# Template:Infobox simple/doc

[](/wiki/File:Template-info.svg) Documentation

[[purge](https://satisfactory.wiki.gg/wiki/Template:Infobox_simple/doc?action=purge)]

Infobox simple is an all-purpose infobox for building, item, fluid and vehicle pages. 

## Contents

  * 1 Parameters
    * 1.1 Common
    * 1.2 Building
    * 1.3 Vehicle
    * 1.4 Dimensions
    * 1.5 Item
    * 1.6 Equipment
    * 1.7 Fuel
    * 1.8 Ingredients
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
className | String | Class name   
  
### Building

Parameter | Type | Description   
---|---|---  
inventorySize | String | Building inventory size, in stacks or m3; also appears in the Vehicle section   
powerUsage | String | Power usage in MW   
powerGenerated | String | Power generated in MW   
fuel | Wikitext | Accepted fuel; also appears in the Vehicle section   
overclockable | Boolean | Whether the building is overclockable   
beltIinputs | Wikitext | Amount of conveyor inputs   
beltOutputs | Wikitext | Amount of conveyor outputs   
pipeIinputs | Wikitext | Amount of pipe inputs   
pipeOutputs | Wikitext | Amount of pipe outputs   
  
### Vehicle

Parameter | Type | Description   
---|---|---  
maxSpeed | Float | Important parameter, determines whether the Vehicle or Building group is used for colliding parameters  
Max speed of the vehicle on a flat straight path   
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
ammo | Wikitext | Item used as ammo (or as a consumable, such as Gas Filters for the Gas Mask)   
magSize | String | Magazine size per reload   
damage | String | Damage per hit   
rateOfFire | String | Rate of fire   
reloadTime | String | Reload time in seconds   
damagePerSecond | String | Damage per second   
range | String | Effective range in meters   
  
### Fuel

Parameter | Type | Description   
---|---|---  
energy | Integer OR "N/A" | Energy per item or m3 in MJ   
fuelConsumers | Wikitext | Bulleted list of fuel consumers, with burn cycle duration and per minute values   
  
### Ingredients

Parameter | Type | Description   
---|---|---  
ingredientX | Page | Xth ingredient, ordered the same way as in-game (X ranges 1–10)   
quantityX | Float | Amount of the Xth ingredient   
  
## Example
    
    
    {{Infobox simple
     | description = Crafts two parts into another part.<br/>Can be automated by feeding parts into it with a conveyor belt connected to the input. The produced parts can be automatically extracted by connecting a conveyor belt to the output.
     | researchTier = [[Tier 2]] - Part Assembly
     | powerUsage = 15
     | overclockable = Yes
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
    

## Assembler

[ ](/wiki/File:Assembler.png "Assembler.png")

_Crafts two parts into another part.  
Can be automated by feeding parts into it with a conveyor belt connected to the input. The produced parts can be automatically extracted by connecting a conveyor belt to the output._

### Unlocked by

[Tier 2](/wiki/Tier_2 "Tier 2") \- Part Assembly

## Building

### [Power usage](/wiki/Power "Power")

15 MW

### [Overclock­able](/wiki/Overclock "Overclock")

Yes

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

**8×** [](/wiki/Reinforced_Iron_Plate "Reinforced Iron Plate") [Reinforced Iron Plate](/wiki/Reinforced_Iron_Plate "Reinforced Iron Plate")

**4×** [](/wiki/Rotor "Rotor") [Rotor](/wiki/Rotor "Rotor")

**10×** [](/wiki/Cable "Cable") [Cable](/wiki/Cable "Cable")

This is the documentation page, it should be transcluded into the main template page. See [Template:Doc](/wiki/Template:Doc "Template:Doc") for more information.
  *[v]: View this template
  *[e]: Edit this template
  *[h]: History of this template
  *[his]: his trivia section
  *[N/A]: Not applicable
