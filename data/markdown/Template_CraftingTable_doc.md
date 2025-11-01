# Template:CraftingTable/doc

[](/wiki/File:Template-info.svg) Documentation

[[purge](https://satisfactory.wiki.gg/wiki/Template:CraftingTable/doc?action=purge)]

This template is used to add recipes to _crafting_recipes_ cargo table. It can also be used to display these recipes in a table, but consider using [Template:AutomatedCrafting](/wiki/Template:AutomatedCrafting "Template:AutomatedCrafting") for that instead. 

**Note: by default table will be invisible but the recipe will be added to cargo. If you need to display the table itself, use`| makeVisible = 1`**  
**To display information from all CraftingTables at once use`{{AutomatedCrafting}}` after that.**

## Parameters

This template is used to add recipes to crafting_recipes cargo table.

Template parameters

This template prefers block formatting of parameters.

Parameter| Description| Type| Status  
---|---|---|---  
Recipe Name| `recipeName`| Optional. The name of the recipe, if different from `product`.

Default
    {{{product}}}
| Line| optional  
Main Product Name| `product`| The name of the main crafted product.

| Page name| required  
Main Product Count| `productCount`| Count of created main product.

Default
    1
| Number| suggested  
Product 2 Name| `product2`| The name of the byproducts.

| Page name| optional  
Product 2 Count| `productCount2`| Count of created byproducts.

Default
    1
| Number| optional  
Product 3 Name| `product3`| no description

| Page name| optional  
Product 3 Count| `productCount3`| no description

Default
    1
| Number| optional  
Product 4 Name| `product4`| no description

| Page name| optional  
Product 4 Count| `productCount4`| no description

Default
    1
| Number| optional  
alternateRecipe| `alternateRecipe`| Set to `1` if the recipe is an alternate recipe. Defaults to 0.

Default
    0
Auto value
    `1`
| Boolean| optional  
mainRecipe| `mainRecipe`| Set to `1` if it's the first recipe you learn for this item or it's the primary mean of acquiring the item (e.g. crafting [[Empty Canister]] from plastic is a main recipe in contrast to all unpackage recipes, which also yield Empty Canisters). Used for ordering recipes. You can use numbers higher than 1 to give the recipe even more ordering priority if there're multiple 'main' recipes. 

Default
    0
Auto value
    `1`
| Number| optional  
Ingredient 1 Name| `ingredient1`| The name of ingredients used.

| Page name| optional  
Ingredient 1 Count| `quantity1`| The count of ingredients used.

Default
    1
| Number| optional  
Ingredient 2 Name| `ingredient2`| no description

| Page name| optional  
Ingredient 2 Count| `quantity2`| no description

Default
    1
| Number| optional  
Ingredient 3 Name| `ingredient3`| no description

| Page name| optional  
Ingredient 3 Count| `quantity3`| no description

Default
    1
| Number| optional  
Ingredient 4 Name| `ingredient4`| no description

| Page name| optional  
Ingredient 4 Count| `quantity4`| no description

Default
    1
| Number| optional  
Ingredient 5 Name| `ingredient5`| no description

| Page name| optional  
Ingredient 5 Count| `quantity5`| no description

Default
    1
| Number| optional  
Ingredient 6 Name| `ingredient6`| no description

| Page name| optional  
Ingredient 6 Count| `quantity6`| no description

Default
    1
| Number| optional  
Ingredient 7 Name| `ingredient7`| no description

| Page name| optional  
Ingredient 7 Count| `quantity7`| no description

Default
    1
| Number| optional  
Ingredient 8 Name| `ingredient8`| no description

| Page name| optional  
Ingredient 8 Count| `quantity8`| no description

Default
    1
| Number| optional  
Ingredient 9 Name| `ingredient9`| no description

| Page name| optional  
Ingredient 9 Count| `quantity9`| no description

Default
    1
| Number| optional  
Ingredient 10 Name| `ingredient10`| no description

| Page name| optional  
Ingredient 10 Count| `quantity10`| no description

Default
    1
| Number| optional  
Building| `craftedIn`| Name of the building where this recipe is used.

| Page name| optional  
Average Power| `avgPower`| The average power consumption for the selected recipe, if power consumption depends on this recipe. Currently only used for [[Particle Accelerator]] recipes.

| Number| optional  
inCraftBench| `inCraftBench`| Set to `1` if the recipe can be crafted by hand in the [[Craft Bench]].

Default
    0
Auto value
    `1`
| Boolean| optional  
inWorkshop| `inWorkshop` `inWorkShop`| Set to `1` if the recipe can be crafted by hand in the [[Equipment Workshop]].

Default
    0
Auto value
    `1`
| Boolean| optional  
Automatic Crafting Time| `craftingTime`| Duration of crafting in buildings without overclocking.

| Number| optional  
Manual Crafting Time| `craftingClicks`| The amount of clicks/cycles needed for manual crafting in Craft Bench or Equipment Workshop.

| Number| optional  
Research Tier| `researchTier`| The milestone tier or the M.A.M. research category in which this item is unlocked.

| Content| suggested  
Make Visible?| `makeVisible`| Set to `1` to display the table, otherwise it will be invisible and will only add the recipe to cargo.

Default
    0
Auto value
    `1`
| Boolean| optional  
Table End?| `tableEnd`| Set to `1` for the last row to end the table. '''Do not forget this parameter or page layout may start acting weird!'''

Default
    0
Auto value
    `1`
| Boolean| optional  
Store in Cargo?| `storeInCargo`| Set to `0` to skip storing data in cargo. Normally it will store in cargo automatically if page name matches the main product of the recipe.

Default
    1
Auto value
    `0`
| Boolean| optional  
Experimental?| `experimental`| Set to `1` if this recipe is only available in Experimental version of the game.

Default
    0
Auto value
    `1`
| Boolean| optional  
Unreleased?| `unreleased`| Set to `1` if this recipe is not available in the game but was datamined or removed at some point.

Default
    0
Auto value
    `1`
| Boolean| optional  
Season| `season`| The name of the season. 

Valid values
    FICSMAS

Example
    FICSMAS
| String| optional  
  
## Example usage
    
    
    {{CraftingTable
    | recipeName = Reinforced Iron Plate
    | craftingTime = 10
    | craftingClicks = 5
    | craftedIn = Assembler
    | inCraftBench = 1
    | product = Reinforced Iron Plate
    | productCount = 1
    | ingredient1 = Iron Plate
    | quantity1 = 3
    | ingredient2 = Screw
    | quantity2 = 30
    | makeVisible = 1
    }}
    {{CraftingTable
    | recipeName = Stitched Iron Plate
    | alternateRecipe = 1
    | craftingTime = 24
    | craftedIn = Assembler
    | product = Reinforced Iron Plate
    | productCount = 3
    | ingredient1 = Iron Plate
    | quantity1 = 6
    | ingredient2 = Wire
    | quantity2 = 30
    | makeVisible = 1
    }}
    {{CraftingTable
    | recipeName = FICSMAS Ornament Bundle
    | researchTier = [[FICSMAS#MAM Research|FICSMAS Research]] - FICSMAS Lights
    | craftingTime = 12
    | craftedIn = Assembler
    | product = FICSMAS Ornament Bundle
    | productCount = 1
    | ingredient1 = Copper FICSMAS Ornament
    | quantity1 = 1
    | ingredient2 = Iron FICSMAS Ornament
    | quantity2 = 1
    | season = FICSMAS
    | makeVisible = 1
    }}
    {{CraftingTable
    | recipeName = Foundation 8m x 1m
    | researchTier = [[Tier 1]] - Base Building
    | craftedIn = Build Gun
    | product = Foundation 8m x 1m
    | productCount = 1
    | ingredient1 = Concrete
    | quantity1 = 5
    | ingredient2 = Iron Plate
    | quantity2 = 2
    | experimental = 1
    | makeVisible = 1
    }}
    {{CraftingTable
    | recipeName = SAM Ingot
    | inCraftBench = 1
    | craftingClicks = 6
    | craftingTime = 2
    | craftedIn = Smelter
    | product = SAM Ingot
    | productCount = 1
    | ingredient1 = SAM Ore
    | quantity1 = 6
    | unreleased = 1
    | makeVisible = 1
    | tableEnd = 1
    }}
    

Recipe| Ingredients| Time (s)| Product  
---|---|---|---  
Reinforced Iron Plate |  3 × [](/wiki/Iron_Plate "Iron Plate") [Iron Plate](/wiki/Iron_Plate "Iron Plate") | 10 | 1 × [](/wiki/Reinforced_Iron_Plate "Reinforced Iron Plate") [Reinforced Iron Plate](/wiki/Reinforced_Iron_Plate "Reinforced Iron Plate") (6 / min)  
30 × [](/wiki/Screw "Screw") [Screw](/wiki/Screw "Screw")  
[Alt](/wiki/Hard_Drive "Hard Drive") Stitched Iron Plate |  6 × [](/wiki/Iron_Plate "Iron Plate") [Iron Plate](/wiki/Iron_Plate "Iron Plate") | 24 | 3 × [](/wiki/Reinforced_Iron_Plate "Reinforced Iron Plate") [Reinforced Iron Plate](/wiki/Reinforced_Iron_Plate "Reinforced Iron Plate") (7.5 / min)  
30 × [](/wiki/Wire "Wire") [Wire](/wiki/Wire "Wire")  
FICSMAS Ornament Bundle[FICS⁕MAS](/wiki/FICSMAS "FICSMAS") |  1 × [](/wiki/Copper_FICSMAS_Ornament "Copper FICSMAS Ornament") [Copper FICSMAS Ornament](/wiki/Copper_FICSMAS_Ornament "Copper FICSMAS Ornament") | 12 | 1 × [](/wiki/FICSMAS_Ornament_Bundle "FICSMAS Ornament Bundle") [FICSMAS Ornament Bundle](/wiki/FICSMAS_Ornament_Bundle "FICSMAS Ornament Bundle") (5 / min)  
1 × [](/wiki/Iron_FICSMAS_Ornament "Iron FICSMAS Ornament") [Iron FICSMAS Ornament](/wiki/Iron_FICSMAS_Ornament "Iron FICSMAS Ornament")  
Foundation 8m x 1mExp |  5 × [](/wiki/Concrete "Concrete") [Concrete](/wiki/Concrete "Concrete") | 0 | 1 × [](/wiki/Foundation_8m_x_1m "Foundation 8m x 1m") [Foundation 8m x 1m](/wiki/Foundation_8m_x_1m "Foundation 8m x 1m")  
2 × [](/wiki/Iron_Plate "Iron Plate") [Iron Plate](/wiki/Iron_Plate "Iron Plate")  
SAM IngotUnreleased |  6 × [](/wiki/SAM_Ore "SAM Ore") [SAM Ore](/wiki/SAM_Ore "SAM Ore") | 2 | 1 × [](/wiki/SAM_Ingot "SAM Ingot") [SAM Ingot](/wiki/SAM_Ingot?action=edit&redlink=1 "SAM Ingot \(page does not exist\)") (30 / min)  
  
This is the documentation page, it should be transcluded into the main template page. See [Template:Doc](/wiki/Template:Doc "Template:Doc") for more information.
  *[v]: View this template
  *[e]: Edit this template
  *[h]: History of this template
  *[his]: his trivia section
  *[N/A]: Not applicable
