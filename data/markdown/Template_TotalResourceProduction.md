# Template:TotalResourceProduction

Template Documentation

[[view](/wiki/Template:TotalResourceProduction/doc "Template:TotalResourceProduction/doc")] [[edit](https://satisfactory.wiki.gg/wiki/Template:TotalResourceProduction/doc?action=edit)] [[history](https://satisfactory.wiki.gg/wiki/Template:TotalResourceProduction/doc?action=history)] [[purge](https://satisfactory.wiki.gg/wiki/Template:TotalResourceProduction?action=purge)]

## Contents

  * 1 Parameters
  * 2 Example
  * 3 TemplateData



Displays the maximum possible extraction for the given number of nodes. 

## Parameters

  * `title`: optional. Title of the table
  * `maxMk`: maximum Mk. (only for the column-header, does not change calculations). default: 3
  * `normalRate`: the rate for the maxMk on a single normal node. default is 240.



## Example
    
    
    {{TotalResourceProduction|title=[[Iron]] Nodes|impure=24|normal=35|pure=37}}
    

[Iron](/wiki/Iron "Iron") Nodes  
---  
Node  
purity | Number  
of nodes | Mk.3  
mining rate | Mk.3 mining rate  
at 250 %  
Impure | 24 | 2,880 | 7,200  
Normal | 35 | 8,400 | 21,000  
Pure | 37 | 17,760 | 44,400  
Total | 96 | 29,040 | 72,600  
      
    
    {{TotalResourceProduction|title=[[Crude Oil]] Nodes|impure=10|normal=12|pure=8|kind=Fluid}}
    

[Crude Oil](/wiki/Crude_Oil "Crude Oil") Nodes  
---  
Node  
purity | Number  
of nodes | Extraction rate | Extraction rate  
at 250 %  
Impure | 10 | 600 | 1,500  
Normal | 12 | 1,440 | 3,600  
Pure | 8 | 1,920 | 4,800  
Total | 30 | 3,960 | 9,900  
  
## TemplateData

Displays the maximum possible extraction for the given number of nodes.

Template parameters

Parameter| Description| Type| Status  
---|---|---|---  
Title| `title`| Title of the table

| Content| suggested  
Impure Nodes| `impure`| The amount of impure nodes

Default
    0
| Number| suggested  
Normal Nodes| `normal`| The number of normal nodes

Default
    0
| Number| suggested  
Pure Nodes| `pure`| The number of pure nodes

Default
    0
| Number| suggested  
Maximum Extractor Mk.| `maxMk`| Only for the column-header, does not change calculations

Default
    

  * “1” when kind is “Fluid”
  * “3” when kind is “Ore”


| Number| optional  
Normal Node Extraction Rate| `normalRate`| The rate for the maxMk on a single normal node

Default
    

  * “120” when kind is “Fluid”
  * “240” when kind is “Ore”


| Number| optional  
Omit Note?| `noNote`| Whether to omit the note after the table (when multiple tables are used consecutively)

Default
    0
Auto value
    `1`
| Boolean| optional  
Kind| `kind`| The kind of the item. 

Valid values
    

  * “Ore”
  * “Fluid”
  * “Oil” (alias for “Fluid”)



Default
    Ore
Auto value
    `Fluid`
| String| optional  
  
The above documentation is transcluded from [Template:TotalResourceProduction/doc](/wiki/Template:TotalResourceProduction/doc "Template:TotalResourceProduction/doc"). ([edit](https://satisfactory.wiki.gg/wiki/Template:TotalResourceProduction/doc?action=edit) | [history](https://satisfactory.wiki.gg/wiki/Template:TotalResourceProduction/doc?action=history))
  *[v]: View this template
  *[e]: Edit this template
  *[h]: History of this template
  *[his]: his trivia section
  *[N/A]: Not applicable
