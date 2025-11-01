# Template:MAMunlock/doc

[](/wiki/File:Template-info.svg) Documentation

[[purge](https://satisfactory.wiki.gg/wiki/Template:MAMunlock/doc?action=purge)]

The MAMunlock template is used in the Obtaining section of parts and buildings under Unlocking. It displays that the part/building is unlocked in the M.A.M. using which parts in which research chain. 

## Usage

### Parameters

Parameter | Data Type | Description   
---|---|---  
name | String | Name of the part or building to be used, if left blank pagename is used   
plural | Any | If any non-blank value is entered, changes "is unlocked" to "are unlocked"   
resourcescanner | Any | If any non-blank value is entered, changes "unlocked" to "added to the Resource Scanner"   
chain | Required | Name of the research chain, without "research" or "research chain" **(required)**  
ingredient1 | String | First part used for the research **(required)**  
quantity1 | Integer | Amount of the first part **(required)**  
ingredient2 | String | Second part used for the research   
quantity2 | Integer | Amount of the second part   
ingredient3 | String | Third part used for the research   
quantity3 | Integer | Amount of the third part   
ingredient4 | String | Fourth part used for the research   
quantity4 | Integer | Amount of the fourth part   
ingredient5 | String | Fifth part used for the research   
quantity5 | Integer | Amount of the fifth part   
  
## Example
    
    
    {{MAMunlock
    |name = Nobelisk
    |chain = Sulfur
    |ingredient1 = Black Powder
    |quantity1 = 100
    |ingredient2 = Steel Beam
    |quantity2 = 100
    }}

**Nobelisk** is unlocked via the **[Sulfur Research chain](/wiki/Sulfur_Research "Sulfur Research")** in the [](/wiki/MAM "MAM") [MAM](/wiki/MAM "MAM") using:  
[](/wiki/Black_Powder "Black Powder")100| [](/wiki/Steel_Beam "Steel Beam")100  
---|---  
      
    
    {{MAMunlock
    |name = Blade Runners
    |plural = 1
    |chain = Caterium
    |ingredient1 = Quickwire
    |quantity1 = 100
    |ingredient2 = Modular Frame
    |quantity2 = 10
    }}

**Blade Runners** are unlocked via the **[Caterium Research chain](/wiki/Caterium_Research "Caterium Research")** in the [](/wiki/MAM "MAM") [MAM](/wiki/MAM "MAM") using:  
[](/wiki/Quickwire "Quickwire")100| [](/wiki/Modular_Frame "Modular Frame")10  
---|---  
      
    
    {{MAMunlock
    |name = {{ItemLink|Caterium Ore}}
    |resourcescanner=1
    |chain=Caterium
    |ingredient1=Caterium Ore
    |quantity1=10}}

**[](/wiki/Caterium_Ore "Caterium Ore")[Caterium Ore](/wiki/Caterium_Ore "Caterium Ore")** is added to the Resource Scanner via the **[Caterium Research chain](/wiki/Caterium_Research "Caterium Research")** in the [](/wiki/MAM "MAM") [MAM](/wiki/MAM "MAM") using:  
[](/wiki/Caterium_Ore "Caterium Ore")10  
---  
  
This is the documentation page, it should be transcluded into the main template page. See [Template:Doc](/wiki/Template:Doc "Template:Doc") for more information.
  *[v]: View this template
  *[e]: Edit this template
  *[h]: History of this template
  *[his]: his trivia section
  *[N/A]: Not applicable
