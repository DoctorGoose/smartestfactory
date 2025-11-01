# Template:Infobox simple/es/doc

[](/wiki/File:Template-info.svg) Documentation

[[purge](https://satisfactory.wiki.gg/wiki/Template:Infobox_simple/es/doc?action=purge)]

Infobox Simple es una infobox de todo uso para las páginas de edificio, objeto, fluido y vehículo. 

## Contents

  * 1 Parametros
    * 1.1 Común
    * 1.2 Invisible
    * 1.3 Edificio
    * 1.4 Vehículo
    * 1.5 Dimensiones
    * 1.6 Objeto
    * 1.7 Equipamiento
    * 1.8 Combustible
    * 1.9 Componentes
  * 2 Ejemplo



## Parametros

### Común

Parametro | Tipo | Descripción   
---|---|---  
name | Nombre | Page | Titulo de la infobox, usada para cargo; PAGENAME por defecto   
displayName | Nombre para mostrar | Strings | Anula el "nombre", pero solo para el título de la infobox (visualmente)   
image | Imagen | Page | "nombre" .PNG por defecto   
description | Descripción | String | Descripción de la infobox   
researchTier | Nivel de Investigación | Wikitext | El nivel y el hito, la investigación MAM u otra fuente que desbloquea el edificio.   
category | Categoría | String | Pestaña menú de construcción (la categorización Wiki se puede deshabilitar con "Sin Categorías")   
subCategory | Sub categoría | String | Categoría menú de contrucción   
blueprintPath | Ruta del blueprint | String | Ruta del blueprint   
  
### Invisible

parametro | Tipo | Descripción   
---|---|---  
noCategories | sin Categorías | Boolean | Desactiva toda la categorización si es verdad   
noCargo | sin Cargo | Boolean | Desactiva todo el almacenamiento de cargo si es verdad   
recipeName | Nombre de la receta | String | PAGENAME por defecto, nombre de la receta (epónimo para edificios)   
experimental | Experimental | Boolean | Si la receta está disponible solo en la rama Experimental   
unreleased | Inedito | Boolean | Si la receta no se ha publicado o no está disponible.   
alternateRecipe | Receta alternativa | Boolean | Si la receta es una receta alternativa (rara vez se usa)   
mainRecipe | Receta principal | Boolean | Si la receta es la receta principal (rara vez se usa)   
product | Producto | Page | PAGENAME por defecto, el producto real (rara vez se usa)   
productCount | Recuento de producto | Intger | 1 por defecto, el recuento real de productos (rara vez se usa)   
bioFuel | biocombustible | Booleano | Si el combustible es un combustible válido para el Quemador de biomasa   
  
### Edificio

parametro | Tipo | Descripción   
---|---|---  
inventorySize | Tamaño del inventario | String | Tamaño del inventario del edificio, en pilas o m3; también aparece en la sección vehículo.   
powerUsage | Consumo de Electricidad | String | Consumo de electricidad en MW   
powerGenerated | Electricidad generada | Float | Electricidad generada en MW   
fuel | combustible | Wikitext | Combustible aceptado; también aparece en la sección Vehículo   
overclockable | overclockable | Boolean | Sí el edificio es overclockeable   
inputs | entradas | Wikitext | Cantidad de entradas   
outputs | salidas | Wikitext | Cantidad de salidas   
  
### Vehículo

parametro | Tipo | Descripción   
---|---|---  
maxSpeed | Velocidad maxima | Float | Parámetro importante, determina si el vehículo o el grupo de edificios se utiliza para parametros de colisión   
Velocidad máxima del vehículo en una trayectoria recta y plana   
inventorySize | Tamaño del inventario | String | Tamaño del inventario de vehículos, en pilas; también aparece en la sección Edificio   
time0_50 | Tiempo0_50 | Float | Tiempo en alcanzar 50 km/h en segundos   
power | Energía | Float | Tasa de quema de combustible   
fuel | Combustible | Wikitext | Combustible aceptado; también aparece en la sección Edificio   
  
  


### Dimensiones

parametro | Tipo | Descripción   
---|---|---  
size_width | Tamaño del ancho | String | Ancho en metros   
size_length | Tamaño del largo | String | Largo en metros   
size_height | Tamaño de la altura | String | Alto en metros   
size_note | Notas del tamaño | String | Información adicional del tamaño, por ejemplo si el edificio es apilable   
  
  


### Objeto

parametro | Tipo | Descripción   
---|---|---  
stackSize | Tamaño de apilado | Integer | Tamaño de apilado   
isRadioactive | Radioactividad | Integer | Valor de desintegración radiactiva (adquirido de Docs.json)   
  
### Equipamiento

parametro | Tipo | Descripción   
---|---|---  
ammo | Munición | Page | Objeto usado como munición (o como consumible, como los Filtros de gas para las Máscaras antigás   
magSize | Tamaño del cargador | String | Tamaño del cargador por recarga   
damage | Daño | String | Daño por golpe   
rateOfFire | Cadencia de fuego | String | Cadencia de fueg   
reloadTime | Tiempo de recarga | String | Tiempo de recarga en segundos   
damagePerSecond | Daño por segundo | String | Damage per second   
range | Rango | String | Rango efectivo en metros   
  
### Combustible

parametro | Tipo | Descripción   
---|---|---  
energy | Energía | Integer OR "N/A" | Energía por objeto o m3 en MJ   
  
### Componentes

parametro | Tipo | Descripción   
---|---|---  
craftedIn | Fabricado en | Page | Edificio o herramienta usada para fabricar el producto   
ingredientX | Componente x | Page | Recuento de ingrediente X (X rangos del 1 al 10)   
quantityX | Cantidad x | Float | X ingrediente, ordenado de la misma forma que en el juego   
  
## Ejemplo
    
    
    {{Infobox simple/es
    | description = Fabrica una pieza a partir de dos piezas. <br/> Se puede automatizar al surtirlo de piezas con una cinta transportadora conectada a la entrada. Las piezas producidas se pueden extraer automáticamente al conectar una cinta transportadora a la salida.
     | category = Producción
     | subCategory = Productores
     | researchTier = [[Nivel 2]] - Montaje de piezas
     | powerUsage = 15
     | overclockable = Si
     | craftedIn = Build Gun
     | inputs = 2
     | outputs = 1
     | quantity1 = 8
     | ingredient1 = Lámina de hierro reforzada
     | quantity2 = 4
     | ingredient2 = Rotor
     | quantity3 = 10
     | ingredient3 = Cable
     | size_width = 10
     | size_length = 15
     | size_height = 10
     |image=File:Generador de carbón.png
     }}
    

## Infobox simple/es/doc

[ ](/wiki/File:Generador_de_carb%C3%B3n.png "Generador de carbón.png")

_Fabrica una pieza a partir de dos piezas.  
Se puede automatizar al surtirlo de piezas con una cinta transportadora conectada a la entrada. Las piezas producidas se pueden extraer automáticamente al conectar una cinta transportadora a la salida._

### Desbloqueado en

[Nivel 2](/wiki/Nivel_2?action=edit&redlink=1 "Nivel 2 \(page does not exist\)") \- Montaje de piezas

### Categoría

[Producción](/wiki/Category:Producci%C3%B3n_buildings?action=edit&redlink=1 "Category:Producción buildings \(page does not exist\)")

### Subcategoría

[Productores](/wiki/Category:Productores?action=edit&redlink=1 "Category:Productores \(page does not exist\)")

## Edificio

### [Energía usada](/wiki/Energ%C3%ADa?action=edit&redlink=1 "Energía \(page does not exist\)")

15 MW

### [Overclockeable](/wiki/Overclock "Overclock")

Si

### Entradas

2

### Salidas

1

## Dimensiones

### Ancho

10 m

### Largo

15 m

### Alto

10 m

### Área

150 m2

## Componentes

### Hecho con

Build Gun

**8×** [](/wiki/File:Reinforced_Iron_Plate.png) Lámina de hierro reforzada

**4×** [](/wiki/File:Rotor.png) Rotor

**10×** [](/wiki/File:Cable.png) Cable

This is the documentation page, it should be transcluded into the main template page. See [Template:Doc](/wiki/Template:Doc "Template:Doc") for more information.
  *[v]: View this template
  *[e]: Edit this template
  *[h]: History of this template
  *[his]: his trivia section
  *[N/A]: Not applicable
