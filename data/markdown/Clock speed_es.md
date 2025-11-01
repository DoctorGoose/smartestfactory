# Clock speed/es

  
  
  
## Velocidad de reloj

[ ](/wiki/File:Clock_speed.png "Clock speed.png")

### Desbloqueado en

[Investigación de Electrobabosas](/wiki/MAM/es#Electrobabosas "MAM/es") \- Hacer Overclock a la producción

Los [edificios](/wiki/Buildings/es?action=edit&redlink=1 "Buildings/es \(page does not exist\)") de producción y energía, como [Taladros](/wiki/Miner/es?action=edit&redlink=1 "Miner/es \(page does not exist\)"), [Constructores](/wiki/Constructor/es?action=edit&redlink=1 "Constructor/es \(page does not exist\)") o [Quemadores de biomasa](/wiki/Biomass_Burner/es?action=edit&redlink=1 "Biomass Burner/es \(page does not exist\)"), pueden tener su **velocidad de reloj** configurada en cualquier porcentaje entre 1.0000% y 250.0000% con cuatro decimales. Para los edificios de producción, esto les permite operar más lento o más rápido a costa de un uso de energía muy reducido o aumentado. Para los edificios de energía, la potencia máxima de salida y el consumo de combustible correspondiente se pueden aumentar en conjunto, otorgando más utilidad de un solo edificio. Hacer tanto overclock como underclock tienen utilidad para optimizar una fábrica, ayudando a sincronizar la producción, aumentar la eficiencia energética y suavizar los picos en el consumo de energía de la fábrica. 

## Contents

  * 1 Terminología
  * 2 Desbloqueo
  * 3 Uso
  * 4 Velocidad de reloj para taladros y extractores
    * 4.1 Optimización
  * 5 Velocidad de reloj para edificios de producción
  * 6 Velocidad de reloj para generadores de energía
  * 7 Historial
  * 8 Galería



## Terminología

**La velocidad de reloj** es la velocidad de operación de un edificio. Una velocidad de reloj del 200% significa que el edificio va a operar el doble de rápido, al 50% significa la mitad de velocidad de operación, sin embargo, este no es el cado para los generadores de energía, consulte a continuación. 

**Hacer Overclock** se refiere a configurar la velocidad de reloj sobre el 100%. 

**Hacer Underclock** se refiere a configurar la velocidad de reloj bajo el 100%. Hacer Underclock no requiere [Esquirlas de energía](/wiki/Power_Shard "Power Shard"). 

## Desbloqueo

**Velocidad de reloj** se desbloquea mediante la **[cadena de investigación de Electrobabosas](/wiki/MAM/es#Electrobabosas "MAM/es")** en el [](/wiki/MAM/es "MAM/es") [MAM](/wiki/MAM/es "MAM/es") usando:  
[](/wiki/Barra_de_hierro "Barra de hierro")50| [](/wiki/L%C3%A1mina_de_hierro "Lámina de hierro")50| [](/wiki/Alambre "Alambre")50  
---|---|---  
  
## Uso

Para cambiar la velocidad de reloj, presiona [`E`](/wiki/Controls "Controls") en un edificio y mira en la parte inferior de la interfaz de usuario. Se puede hacer Underclock libremente, sin embargo hacer Overclock requiere [Esquirlas de energía](/wiki/Power_Shard/es?action=edit&redlink=1 "Power Shard/es \(page does not exist\)"), que son elaboradas con [Electrobabosas](/wiki/Power_Slug/es?action=edit&redlink=1 "Power Slug/es \(page does not exist\)"). Se pueden colocar hasta tres fragmentos de energía en un edificio, cada uno de los cuales permite aumentar la velocidad máxima del reloj en un 50%. La velocidad del reloj se puede cambiar en incrementos del 1% usando el control deslizante o escribiendo directamente el valor deseado para _Velocidad del reloj_ o _Tasa de producción objetiva_. 

En cualquier caso a continuación, el porcentaje de overclock se redondeará a 4 decimales: 

  * Ingrese la producción deseada del artículo por minuto 
    * Una vez guardado el porcentaje de velocidad del reloj en la máquina, el artículo por minuto se volverá a evaluar con 2 decimales.
  * Ingrese el porcentaje de velocidad del reloj directamente
  * Escribir una ecuación simple en objeto por minuto o en velocidad del reloj 
    * Tenga en cuenta que, al igual que la calculadora disponible en la búsqueda rápida, evalúa de derecha a izquierda, por lo que es posible que las ecuaciones de varios pasos no den el resultado esperado.



La velocidad real del reloj guardada en esa máquina se puede verificar volviendo a abrir la interfaz de usuario. Escribir un valor arbitrariamente alto se redondeará hacia abajo al valor válido más cercano (como 250%), mientras que las entradas no numéricas se ignorarán. Configurar la velocidad del reloj por debajo del 1% dará como resultado un 1% de velocidad del reloj; esto es visible cuando se vuelve a abrir la interfaz de usuario de la máquina. 

Existe un problema en el que el redondeo hacia abajo se aplica a 5 y menos, y el redondeo hacia arriba solo se aplica a 6 y más. 

## Velocidad de reloj para taladros y extractores

Hacer Overclock a [Taladros](/wiki/Miner/es?action=edit&redlink=1 "Miner/es \(page does not exist\)") y [Extractores de petróleo](/wiki/Oil_Extractor/es "Oil Extractor/es") es altamente benéfico ya que permite extraer mas mineral/petróleo por nodo. En términos de energía por mineral/petróoleo extraído, un taladro/extractor overclockeado en un nodo de mayor pureza puede ser también mas eficiente que uno no overclockado en un nodo de menor pureza. Definiendo la eficiencia de energía como la energía requerida por mineral o petróleo extraído: 

  * extraer un nodo puro al 250% tiene la misma eficiencia energética que extraer un nodo normal al 78,74% o un nodo impuro al 24,80%
  * extraer un nodo normal al 250% tiene la misma eficiencia energética que extraer un nodo impuro al 78,74%



De manera más general, aumentar la pureza del nodo en un nivel y al mismo tiempo multiplicar la velocidad del reloj por 25/3≈3,175 resulta en la misma eficiencia energética (requerimiento de energía por mineral o aceite extraído). 

Dado que, para la misma frecuencia de reloj, los nodos de mayor pureza requieren significativamente menos energía por mineral o petróleo extraído, una estrategia simple para reducir el consumo de energía asociado con la extracción es: 

  1. hacer overclock completamente a los nodos puros (o, para Taladros Mk.3, hacer overclock a los nodos puros al 162.5%, debido al límite del cinta Mk.5) antes de extraer cualquier cosa de los nodos normales, luego
  2. hacer overclock completamente a los nodos normales antes de extraer nada de los nodos impuros.



A continuación se detalla un enfoque más óptimo, pero los ahorros de energía en relación con esta estrategia simple son generalmente modestos. 

### Optimización

Cuando tiene acceso a nodos más que suficientes para satisfacer sus requisitos de extracción, la forma _más_ energéticamente eficiente de extraer mineral o petróleo implica tomar una gran cantidad de los nodos puros, una cantidad moderada de los nodos normales y una pequeña cantidad de los nodos impuros, de modo que la eficiencia energética por mineral o petróleo extraído sea la misma en todos los nodos. Suponga que tiene acceso a 

  * np nodos puros
  * nn nodos normales
  * ni modos impuros



y que estará tocando a cada nodo con un extractor con una tasa de extracción base de B como se describe a continuación: 

Extractor | tasa de extracción base, B  
---|---  
Taladro Mk.1 | 60 mineral/min   
Taladro Mk.2 | 120 mineral/min   
Taladro Mk.3 | 240 mineral/min   
Extractor de petróleo | 120 petróleo/min   
  
Si su tasa de extracción objetivo es X mineral o petróleo por minuto, las tasas de reloj con mayor eficiencia energética se pueden determinar de la siguiente manera 

  1. Calcule el consumo de energía requerido para el enfoque simple descrito anteriormente (hacer overclock de alta pureza antes de aprovechar la menor pureza). Este es un límite superior optimista en la energía que podría ahorrar optimizando completamente las velocidades del reloj. ¿Le parece mucho? Si no es así, no debería molestarse con esta optimización. 
  2. Resolver c como: 

c=XB(2⋅np+2−5/3⏟≈0,315⋅nn+2−13/3⏟≈0,0496⋅ni)

  3. Suponiendo que no hay límites de cintas o reloj, las frecuencias de reloj ideales serían: 
     * 100%⋅c para cada nodo puro
     * 100%⋅c/25/3≈31,5%⋅c para cada nodo normal
     * 100%⋅c/210/3≈4,96%⋅c para cada nodo impuro
Desafortunadamente, este punto de funcionamiento no siempre será realizable, ya sea porque: 
     * Requiere que los extractores puros operen a una velocidad de reloj superior al 250%, o
     * Requiere que los extractores puros excedan el límite de la cinta Mk.5 de 780 objetos/min o el límite de tubería Mk.2 de 600 fluido/min
En estos casos, los extractores puros deben ajustarse a la frecuencia de reloj utilizable más alta (162.5% para mineros Mk.3 con cintas Mk.5, 250% para extractores de petróleo con tuberías Mk.2) y luego el algoritmo debe repetirse para determinar cuál es la mejor forma de utilizar los nodos normales e impuros para reunir el resto del mineral o petróleo. Si esta segunda solución requiere que los extractores normales se configuren a una frecuencia de reloj superior al 250%, entonces los extractores de normales deben configurarse al 250% y los extractores de impuros deben configurarse a la tasa que se requiera para recolectar el resto del mineral o petróleo. Si esto nuevamente requiere una frecuencia de reloj superior al 250%, entonces X es demasiado alto para los nodos dados. 



Por ejemplo, si desea extraer 1800 de petróleo de una combinación de 2 nodos puros, 3 nodos normales y 5 nodos impuros, entonces: 

  * B=120 petróleo/min de un extractor de petróleo
  * np=2, nn=3, y ni=5
  * X=1800 petróleo/min
  * La forma sencilla de lograr esta tasa de extracción es hacer overclock completamente a ambos nodos puros (1200 petróleo/min) y luego tocar y hacer overclock completamente solo a dos nodos normales (600 petróleo/min). Esto requeriría 4 extractores de petróleo totalmente overclockeados, que consumirían 693,14 MW. Por tanto, este es el límite superior optimista del ahorro de energía. Parece que vale la pena, aunque debemos recordar que se trata de una estimación "optimista" y que nuestros ahorros reales probablemente serán menores.
  * El cálculo da c=2,889, así que 
    * Los extractores puros deben funcionar al 288,9%. Esto excede el 250%, por lo que debemos asumir que los 2 extractores puros operan al 250%, produciendo colectivamente 1200 petróleo/min.
    * Como subcálculo, repetimos con np=𝟎, nn=3, ni=5, X=𝟔𝟎𝟎 petróleo/min. Esto da c=4,19, así que 
      * Los nodos normales deben operarse al 132,0%
      * Los nodos impuros deben operarse al 41,58%



Esto requeriría 582,83 MW, un ahorro de 110,3 MW. 

## Velocidad de reloj para edificios de producción

Para los edificios de producción, el tiempo de fabricación es directamente proporcional a la velocidad de reloj, pero la energía requerida cambia polinomialmente (N=1,6). A medida que la tasa de fabricación de objetos incrementa, la tasa de consumo de los ingredientes incrementa también. La tabla a continuación muestra cinco diferentes velocidades de reloj en un Constructor, por ejemplo, producir barras de hierro toma 4 segundos. 

[](/wiki/File:Clock_speed_power_consumption_graph.png)

[](/wiki/File:Clock_speed_power_consumption_graph.png "Enlarge")

La relación de consumo de energía por fabricación basada en la velocidad del reloj. La relación se compara con la cantidad de energía de cada fabricación a la velocidad de reloj predeterminada.

[](/wiki/File:Overclocking_graph.png)

[](/wiki/File:Overclocking_graph.png "Enlarge")

La relación entre el consumo o la producción de energía de los edificios en función de la velocidad del reloj.

Velocidad de reloj | Tiempo de fabricación | Energía requerida | Energía por barra de hierro   
---|---|---|---  
10% | 40s | 0,1 MW | 4 MJ  | 25%   
50% | 8s | 1,3 MW | 10,4 MJ  | 66%   
100% (por defecto) | 4s | 4 MW | 16 MJ  | 100%   
150% | 2,67s | 7,7MW | 20,4 MJ  | 128%   
200% | 2s | 12,1 MW | 24,2 MJ  | 151%   
250%  | 1,6s  | 17,3 MW  | 27,7 MJ  | 173%   
  
[](/wiki/File:Overclocking_at_999.jpg)

[](/wiki/File:Overclocking_at_999.jpg "Enlarge")

El overclock puede tener cualquier valor, pero el juego lo acortará automáticamente entre el 1% y el 250%.

La fórmula para el uso de energía es: 

uso de potencia=uso de potencial inicial×(velocidad de reloj100)1,6  
Dondevelocidad de reloj es un numero con hasta 4 decimales entre 1 y 250, y  
Ambos uso de energiayuso de potencia inicialson medidos en MW.  
Para el uso de energía relativo por objeto producido, restar el exponente por 1, esto es. 

uso de energi´a=uso de energi´a inicial×(velocidad de reloj100)0,6  
Hacer **Underclock** en [Constructores](/wiki/Constructor/es?action=edit&redlink=1 "Constructor/es \(page does not exist\)") y [Ensambladoras](/wiki/Assembler/es?action=edit&redlink=1 "Assembler/es \(page does not exist\)") en el juego temprano es altamente beneficioso. Puede producir un ahorro considerable de combustible ([Biomasa](/wiki/Biomass/es?action=edit&redlink=1 "Biomass/es \(page does not exist\)")). Con [Divisores](/wiki/Splitter/es?action=edit&redlink=1 "Splitter/es \(page does not exist\)") y [Uniones](/wiki/Merger/es?action=edit&redlink=1 "Merger/es \(page does not exist\)") de cinta disponibles, ahorrar combustible puede ser acompañado de una perdida cero en la tasa de producción. Un [Taladro Mk.1](/wiki/Miner/es?action=edit&redlink=1 "Miner/es \(page does not exist\)") con dos [Fundiciones](/wiki/Smelter/es?action=edit&redlink=1 "Smelter/es \(page does not exist\)") operando a velocidad de reloj completa produce mas de 570 lingotes de un nodo normal con la energía de una pila de [hojas](/wiki/Leaves/es?action=edit&redlink=1 "Leaves/es \(page does not exist\)").Un Taladro Mk.1 con nueve Fundiciones operando a una velocidad de reloj del 22% rinden más de 900 piezas con la misma cantidad de energía. La tasa de producción neta será prácticamente idéntica y la energía ahorrada se puede utilizar en otros lugares. 

Cabe señalar que los edificios de producción utilizan el valor calculado completo y, como tal, el valor redondeado que aparece en el juego no siempre es exacto. 

Los edificios de producción que están underlockeadas para tener un consumo de energía activo por debajo de la tasa de inactividad de 0.1MW seguirán usando 0.1MW mientras estén inactivos.[1]

## Velocidad de reloj para generadores de energía

**Hacer Overclock a todos los tipos de generadores de energía no otorga otro beneficio mas que ahorrar espacio de construcción.**  
Para edificios generadores de energía ambos tanto la capacidad de energía como la tasa de consumo de combustible aumentan al mismo ritmo. El efecto de esto es que la energía producida por tipo de combustible, o **valor de Combustible** , se mantiene igual. Por ejemplo, una pieza de [Carbón](/wiki/Coal/es?action=edit&redlink=1 "Coal/es \(page does not exist\)") siempre vale 300MJ de energía independientemente de la velocidad del reloj. La tabla a continuación muestra tres diferentes velocidades de reloj en un [Generador de carbón](/wiki/Coal_Generator/es "Coal Generator/es"). Notar que a un overclock de 250% no dará un 250% de energía como sugiere el valor de _MW objetivo_ en el juego. Los verdaderos valores de producción están listados con el combustible del generador. 

Velocidad de reloj | Tiempo de combustión del carbón | Carbón por minuto | Energía por carbón | Capacidad del generador   
---|---|---|---|---  
10% | 23,51s | 2,55 | 300 MJ | 12,76 MW | 17%   
100% (por defecto) | 4s | 15 | 300 MJ | 75 MW | 100%   
246,2288% | 2s | 30 | 300 MJ | 150 MW | 200%   
250% | 1,98s | 30,35 | 300 MJ | 151,76 MW | 202,35%   
  
El porcentaje para el 200% de la capacidad del generador también se puede memorizar como `100*2^1,13`, que se puede ingresar en el campo de velocidad del reloj. 

**La formula para el tiempo de combustión del combustible es:**

tiempo de combustion del combustible=tiempo de combustio´n del combustible inicial×100velocidad de reloj1,13

donde velocidad de reloj es un número con hasta 4 decimales entre 1 y 250, y   
tantotiempo de combustio´n del combustible y tiempo de combustio´n del combustible inicial se miden en segundos. 

**La fórmula para la capacidad de potencia o la tasa de consumo de combustible es:**

capacidad de potencia=capacidad de potencia inicial×velocidad de reloj1001,3  
donde velocidad de relojes un numero con hasta 4 decimales entre 1 y 250, y   
tanto capacidad de potencia y capacidad de potencia inicialson medidos en MW.  
remplaza capacidad de potencia ycapacidad de potencia inicial con tasa de consumo de combustibley tasa de consumo de combustible inicial medido en partes por minuto o m3/min para obtener la tasa de consumo de combustible. 

**La fórmula para encontrar la velocidad del reloj para configurar un generador de energía para una tasa de operación deseada es:**

velocidad de reloj=100×(tasa de operacion100)1,3  
donde velocidad de relojes un numero con hasta 4 decimales entre 1 y 250, y   
tasa de operaciones el porcentaje deseado de la tasa de funcionamiento normal.  
tasa de operacionpuede ser obtenida dividiendo la capacidad de potenciao tasa de consumo de combustiblepor la capacidad de potencia inicial y multiplicando por 100. 

  
ejemplos: 

  * Al 150% de la velocidad del reloj para un generador de combustible que quema combustible normal, el tiempo de combustión sería 5×1001501,3= ∼3,66029 segundos (redondeado a 4 dígitos)
  * Al 250% de la velocidad del reloj para un generador de combustible, el multiplicador de la capacidad de potencia y la tasa de consumo de combustible sería 2501001,3= ∼2,0235lo que significaría que la capacidad de potencia es 150×∼2,0235= ∼303,52814 MWy la tasa de consumo de combustible es 12×∼2,0235= ∼24,2823 m3/min (todo redondeado a 4 dígitos, multiplicador utilizado hasta 13 dígitos)
  * Para lograr una tasa de operación del 200% de un generador normal, la velocidad del reloj sería: 100×(200100)1.3= ∼246.2288%(redondeado a 4 dígitos, da 199,999948% de operación)
  * Para lograr una tasa de operación del 75% de un generador normal, la velocidad del reloj sería: velocidad de reloj=100×(75100)1,3= ∼68,7986% (redondeado a 4 dígitos)
  * Si quisieras quemar 4 combustibles por minuto para un generador de combustible que usa combustible normal, necesitaría una tasa de operación de412×100=25%
  * Si tuviera 246m3 / min de combustible para quemar, necesitaría24612=20,5 generadores lo que significa que necesitaría 20 generadores con una tasa de operación del 100% y 1 generador con una tasa de operación del 50%.



**Central nuclear**

La [Central nuclear](/wiki/Nuclear_Power_Plant/es?action=edit&redlink=1 "Nuclear Power Plant/es \(page does not exist\)") escala de manera diferente con el overclock. Usan 1,321928 en lugar de 1,3 como exponente y número raíz. Al 250% de la velocidad del reloj, uno opera 2,00000009951 veces más rápido en comparación con el 100% de la velocidad del reloj. 

## Historial

[](/wiki/File:Icon-boilerplate.png) | The history section is incomplete in this article. Please help [expanding it](https://satisfactory.wiki.gg/wiki/Clock_speed/es?action=edit) if you can. Information can be gathered from [patch notes](/wiki/Category:Patch_notes "Category:Patch notes").   
---|---  
  
  * [Parche 0.4.0.4](/wiki/Patch_0.4.0.4/es?action=edit&redlink=1 "Patch 0.4.0.4/es \(page does not exist\)"): Se corrigió que el overclock no mostrara el valor correcto al pegar configuraciones en algunas situaciones
  * [Parche 0.4.0.3](/wiki/Patch_0.4.0.3/es?action=edit&redlink=1 "Patch 0.4.0.3/es \(page does not exist\)"): Se cambió el número de decimales en overclock de 1 a 4
  * [Parche 0.4.0.0](/wiki/Patch_0.4.0.0/es?action=edit&redlink=1 "Patch 0.4.0.0/es \(page does not exist\)"): Ahora es posible establecer porcentajes decimales como velocidad del reloj, el juego ya no lo redondea al porcentaje entero más cercano.



## Galería

  * [](/wiki/File:Underclocking_tutorial.png "Un Constructor Underlockeado. Se puede ingresar un valor en porcentaje, objetos por minuto o ajustar usando el control deslizante.")

Un [Constructor](/wiki/Constructor/es?action=edit&redlink=1 "Constructor/es \(page does not exist\)") Underlockeado. Se puede ingresar un valor en porcentaje, objetos por minuto o ajustar usando el control deslizante.

  * [](/wiki/File:Overclocking_tutorial.png "Un Taladro Overlockeado. Esquirlas de energía son requeridas para hacer overlock mas allá del 100%.")

Un [Taladro](/wiki/Miner/es?action=edit&redlink=1 "Miner/es \(page does not exist\)") Overlockeado. [Esquirlas de energía](/wiki/Power_Shard/es?action=edit&redlink=1 "Power Shard/es \(page does not exist\)") son requeridas para hacer overlock mas allá del 100%.




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
  
  


  1. ↑ [Satisfactory Wiki - August 1st, 2021 - Underlocked-below-idle-power-while-active.webp](/wiki/File:Underlocked-below-idle-power-while-active.webp "File:Underlocked-below-idle-power-while-active.webp")


  *[v]: View this template
  *[e]: Edit this template
  *[h]: History of this template
