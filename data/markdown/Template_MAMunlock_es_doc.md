# Template:MAMunlock/es/doc

[](/wiki/File:Template-info.svg) Documentation

[[purge](https://satisfactory.wiki.gg/wiki/Template:MAMunlock/es/doc?action=purge)]

La plantilla MAMunlock/es se utiliza en la sección de Obtención de piezas y edificios en Desbloqueo. Muestra que la pieza/edificio se desbloquea en el M.A.M. utilizando qué partes en qué cadena de investigación. 

## Uso

### Parametros

Parametro | Tipo de Data | Descripción   
---|---|---  
nombre | String | Nombre del objeto o edificio que se usará   
plural | Any | Si cualquier valor no en blando se ingresa, cambiara "desbloquea" o "añade" a plural   
Escáner de recursos | Any | Si cualquier valor no en blando se ingresa, cambia "desbloquea" por "añade al escáner de recursos"   
cadena | Required | Nombre de la cadena de investigación, sin "investigación" o "cadena de investigación" **(requerido)**  
ingredienteN | String | (N = 1-5) Nombre del objeto usado en la investigación **(requerido)**  
cantidadN | Integer | (N = 1-5) Cantidad del objeto usado en la investigación **(requerido)**  
  
## ejemplo
    
    
    {{MAMunlock/es
    |nombre= Lingote de caterio
    |cadena = Caterio
    |ingrediente1 = Mineral de Caterio
    |cantidad1 = 50
    }}

**Caterio** se desbloquea mediante la **[cadena de investigación de Caterio](/wiki/MAM/es#Caterio "MAM/es")** en el [](/wiki/MAM/es "MAM/es") [MAM](/wiki/MAM/es "MAM/es") usando:  
[File:Mineral de Caterio.png](/wiki/Special:Upload?wpDestFile=Mineral_de_Caterio.png "File:Mineral de Caterio.png")10  
---  
      
    
    {{MAMunlock/es
    |nombre= Turbopatines
    |plural = 1
    |cadena = Caterio
    |ingrediente1 = Turboalambre
    |cantidad1 = 100
    |ingrediente2 = Estructura modular
    |cantidad2 = 10
    }}

**Turbopatines** se desbloquean mediante la **[cadena de investigación de Caterio](/wiki/MAM/es#Caterio "MAM/es")** en el [](/wiki/MAM/es "MAM/es") [MAM](/wiki/MAM/es "MAM/es") usando:  
[](/wiki/Turboalambre "Turboalambre")100| [](/wiki/Estructura_modular "Estructura modular")10  
---|---  
      
    
    {{MAMunlock/es
    |nombre= {{ItemLink/es|Mineral de caterio|Caterium Ore}}
    |Escáner de recursos=1
    |cadena=Caterio
    |ingrediente1=Mineral de caterio
    |cantidad1=10}}
    }}

**[File:Mineral de caterio.png](/wiki/Special:Upload?wpDestFile=Mineral_de_caterio.png "File:Mineral de caterio.png") [Mineral de caterio](/wiki/Caterium_Ore "Caterium Ore")** se añade al escáner de recursos de la **[cadena de investigación de Caterio](/wiki/MAM/es#Caterio "MAM/es")** en el [](/wiki/MAM/es "MAM/es") [MAM](/wiki/MAM/es "MAM/es") usando:  
[File:Mineral de caterio.png](/wiki/Special:Upload?wpDestFile=Mineral_de_caterio.png "File:Mineral de caterio.png")10  
---  
  
}} 

This is the documentation page, it should be transcluded into the main template page. See [Template:Doc](/wiki/Template:Doc "Template:Doc") for more information.
  *[v]: View this template
  *[e]: Edit this template
  *[h]: History of this template
  *[his]: his trivia section
  *[N/A]: Not applicable
