# Power/pt

A maioria das [buildings](/wiki/Buildings "Buildings") requerem electricidade, ou **energia** , para funcionar. A energia é produzida nos power generators (see below) e consumida por construções. A energia é transferida via [Power Lines](/wiki/Power_Line "Power Line"), [Power Poles](/wiki/Power_Poles "Power Poles") ou [Train Stations](/wiki/Train_Station "Train Station") e [Railways](/wiki/Railway "Railway"). A energia é medida em megawatts (MW).   
  
## Contents

  * 1 Princípio
  * 2 Rede energética
  * 3 Falha de energia
  * 4 Gráfico de energia
  * 5 Consumidores de energia
  * 6 Power generators
    * 6.1 Type of generators
  * 7 Resource consumption
  * 8 Clock speed
    * 8.1 Power consumer
    * 8.2 Power generator
  * 9 Energy
  * 10 Trivia
  * 11 References
  * 12 See also



## Princípio

No jogo, a palavra _energia_ funciona de forma semelhante à corrente eléctrica: Um gerador de energia produz alguma corrente e cada consumidor de energia, como por exemplo os Construtores, vai consumir alguma corrente. Quando a procura de corrente está dentro da capacidade de produção de energia, está tudo bem. Quando a procura é maior que a produção, a rede em questão vai abaixo. 

Não existem os conceitos de voltagem e resistência no jogo. 

## Rede energética

Uma rede energética é uma rede, consistindo em construções que produzem e consomem energia, conectadas através de Cabos de Energia, Postes de Energia, Estações Ferroviárias e Carris. Um gráfico com a capacidade total de produção, a produção energética e o consumo de energia pode ser mostrado interagindo [`E`](/wiki/Controls "Controls") com qualquer Poste de Energia, gerador ou Estação Ferroviária nessa rede. 

Redes Energéticas podem ser separadas usando um [Power Switch](/wiki/Power_Switch "Power Switch"). Energia em excesso pode ser armazenada em [Power Storages](/wiki/Power_Storage "Power Storage"), para ser usada em casos em que o consumo exceda a produção. 

## Falha de energia

Se o consumo energético exceder a produção e não houver energia disponível nos [Power Storages](/wiki/Power_Storage "Power Storage"), haverá uma falha de energia. Todos os geradores e consumidores de energia nessa rede vão parar de funcionar. O engenheiro irá ouvir um aviso sonoro da falha, independentemente do ponto do mapa onde esteja e da distância entre os dispositivos afectados e o engenheiro. 

  * Ao contrário de outros jogos, as construções não vão continuar mais devagar quando a geração de energia não for suficiente. A rede eléctrica falha simplesmente e faz com que as construções deixem de funcionar.



O engenheiro pode reiniciar o disjuntor interagindo [`E`](/wiki/Controls "Controls") com qualquer poste ou gerador de energia conectado à rede que falhou. Na Interface do Utilizador (IU), puxa a alavanca para baixo (ver imagem abaixo) para re-estabelecer a energia. Antes de reiniciar, é aconselhável adicionar mais geradores de energia à rede ou remover temporariamente cabos de energia para algumas áreas da fábrica, senão a rede energética vai simplesmente sobrecarregar novamente assim que for re-activada. Desconectar consumidores de energia suficientes vai reiniciar automaticamente o disjuntor. [_[citation needed](/wiki/Category:Citation_needed "Category:Citation needed")_]

Uma falha de energia também permitirá [hostile creatures to respawn](/wiki/Combat#Creature_respawn_mechanism "Combat"). 

  * [](/wiki/File:Power_graph.jpg "Um gráfico de energia, com consumo de energia abaixo da capacidade de produção.")

Um gráfico de energia, com consumo de energia abaixo da capacidade de produção.

  * [](/wiki/File:Power_trip.jpg "Durante uma falha energética, interage E com qualquer poste ou gerador de energia no circuito e puxa a alavanca para baixo para reiniciar o disjuntor.")

Durante uma falha energética, interage [`E`](/wiki/Controls "Controls") com qualquer poste ou gerador de energia no circuito e puxa a alavanca para baixo para reiniciar o disjuntor.




Se não houver nenhum gerador conectado (como se desconectares a ligação entre os consumidores e os geradores de energia), as construções vão simplesmente desligar-se e não haverá uma falha de energia. Neste caso, as construções irão reiniciar funções assim que uma fonte de energia adequada for conectada ao circuito, sem necessidade de reiniciar o disjuntor. 

## Gráfico de energia

[](/wiki/File:Power_pole_-_graph.png)

[](/wiki/File:Power_pole_-_graph.png "Enlarge")

Gráfico de um poste de energia, com o consumo de energia e a capacidade de produção.

O Gráfico de Energia mostra informação sobre a produção e consumo de energia na rede de energia actual, bem como o somatório da energia armazenada em todos os Armazéns de Energia na rede. Armazéns de Energia não afectam nenhuma das linhas do gráfico - a informação de armazenamento é mostrada à direita do gráfico.  
■ Capacidade: A soma da **produção máxima** de todos os geradores de energia na rede.  
■ Produção: A **produção actual** de energia de todos os geradores de energia da rede. Só serádiferente da "capacidade" se existirem incineradoras de biomassa na rede, dado que são o único gerador que se adapta à procura de energia.  
■ Consumo: O **consumo actual** de energia de todos os consumidores da rede. Se o consumo exceder a produçao, a energia será retirada aos Armazéns de Energia, caso esta esteja disponível. Se não estiver, haverá uma falha de energia.  
■ Consumo máximo: A soma do **consumo máximo** de todos os consumidores de energia na rede. 

## Consumidores de energia

  * A maioria das [buildings](/wiki/Building "Building") necessita de energia para funcionar. Estas são chamadas consumidoras de energia. Vê a página de cada construção para ver o seu consumo de energia em MW.
  * Cada construção consome 0.1 MW quando está em espera (quer o engenheiro tenha desligado o seu interruptor ou a construção não esteja a funcionar por problemas logísticos). 
    * Subcarregar as construções do início do jogo para velocidades de produção muito baixas permite que elas consumam menos energia a produzir do que quando estão em espera.
  * [Indicator Lights](/wiki/Indicator_Light "Indicator Light") mostram se uma construção está a operar e a consumir energia ou não.



  


**Fim de tradução. O texto abaixo ainda não foi traduzido...**

  


## Power generators

Power generators convert [fuels](/wiki/Fuels "Fuels") into power. Each type of generator building has its own set of fuel item types and power output. 

All power generators with the exception of the Biomass Burner always operate at full capacity. Biomass Burners instead scale to power consumption and burn slower at lesser demand. For example, if grid capacity is 105 MW, provided by one Coal Generator producing 75 MW and one Biomass Burner producing 30 MW, and power consumption is 95 MW, the entire capacity of the Coal Generator will be used first followed by two thirds of the Biomass Burner's capacity, meaning fuel will be burned at two thirds of the rate it would at maximum demand. This also renders Biomass Burners unable to charge Power Storages. 

### Type of generators

There are five total types of power generators: 

  * [](/wiki/Biomass_Burner "Biomass Burner") [Biomass Burner](/wiki/Biomass_Burner "Biomass Burner")
  * [](/wiki/Coal_Generator "Coal Generator") [Coal Generator](/wiki/Coal_Generator "Coal Generator")
  * [](/wiki/Fuel_Generator "Fuel Generator") [Fuel Generator](/wiki/Fuel_Generator "Fuel Generator")
  * [](/wiki/Geothermal_Generator "Geothermal Generator") [Geothermal Generator](/wiki/Geothermal_Generator "Geothermal Generator")
  * [](/wiki/Nuclear_Power_Plant "Nuclear Power Plant") [Nuclear Power Plant](/wiki/Nuclear_Power_Plant "Nuclear Power Plant")



## Resource consumption

The table below shows the raw resource consumption rate (per min) for every 1 GW of net power generated, among different generation methods: 

Type | [](/wiki/Iron_Ore "Iron Ore") [Iron Ore](/wiki/Iron_Ore "Iron Ore") | [](/wiki/Copper_Ore "Copper Ore") [Copper Ore](/wiki/Copper_Ore "Copper Ore") | [](/wiki/Limestone "Limestone") [Limestone](/wiki/Limestone "Limestone") | [](/wiki/Water "Water") [Water](/wiki/Water "Water") | [](/wiki/Coal "Coal") [Coal](/wiki/Coal "Coal") | [](/wiki/Caterium_Ore "Caterium Ore") [Caterium Ore](/wiki/Caterium_Ore "Caterium Ore") | [](/wiki/Raw_Quartz "Raw Quartz") [Raw Quartz](/wiki/Raw_Quartz "Raw Quartz") | [](/wiki/Sulfur "Sulfur") [Sulfur](/wiki/Sulfur "Sulfur") | [](/wiki/Crude_Oil "Crude Oil") [Crude Oil](/wiki/Crude_Oil "Crude Oil") | [](/wiki/Bauxite "Bauxite") [Bauxite](/wiki/Bauxite "Bauxite") | [](/wiki/Nitrogen_Gas "Nitrogen Gas") [Nitrogen Gas](/wiki/Nitrogen_Gas "Nitrogen Gas") | [](/wiki/Uranium "Uranium") [Uranium](/wiki/Uranium "Uranium")  
---|---|---|---|---|---|---|---|---|---|---|---|---  
[](/wiki/Coal "Coal") [Coal](/wiki/Coal "Coal") | - | - | - | 700.44 | 233.48 | - | - | - | - | - | - | \-   
[](/wiki/Compacted_Coal "Compacted Coal") [Compacted Coal](/wiki/Compacted_Coal "Compacted Coal") | - | - | - | 747.74 | 118.81 | - | - | 118.81 | - | - | - | \-   
[](/wiki/Fuel "Fuel") [Fuel](/wiki/Fuel "Fuel") | - | - | - | 90.98 | - | - | - | - | 34.12 | - | - | \-   
[](/wiki/Turbofuel "Turbofuel") [Turbofuel](/wiki/Turbofuel "Turbofuel") | - | - | - | 40.88 | 27.25 | - | - | 27.25 | 15.29 | - | - | \-   
[](/wiki/Turbofuel "Turbofuel") [Turbo Blend Fuel](/wiki/Turbofuel "Turbofuel") | - | - | - | 11.13 | - | - | - | 16.70 | 25.00 | - | - | \-   
[](/wiki/Uranium_Fuel_Rod "Uranium Fuel Rod") [Uranium Fuel Rod](/wiki/Uranium_Fuel_Rod "Uranium Fuel Rod") | 1.95 | 4.31 | 1.54 | 130.72 | 0.87 | 3.57 | 2.03 | 3.58 | 0.20 | - | - | 3.58   
[](/wiki/Plutonium_Fuel_Rod "Plutonium Fuel Rod") [Uranium & Plutonium Rods](/wiki/Plutonium_Fuel_Rod "Plutonium Fuel Rod") | 2.38 | 2.62 | 4.70 | 132.45 | 2.98 | 2.06 | 3.23 | 2.81 | 0.23 | 3.11 | 4.16 | 1.90   
  
  * Note: Actual consumption of raw ores may differ according to the choice of [Alternate recipes](/wiki/Alternate_recipes "Alternate recipes").



## Clock speed

Overclocking is unlocked at the [MAM](/wiki/MAM "MAM"). The clock speed of buildings can be adjusted by interacting [`E`](/wiki/Controls "Controls") with it and adjusting the slider. [](/wiki/Power_Shard "Power Shard") [Power Shards](/wiki/Power_Shard "Power Shard") are required to increase the clock speed beyond 100%, up to 250% maximum. 

Underclocking can be done freely once overclocking has been researched and costs no Power Shards. **See main article:** [Clock Speed](/wiki/Clock_Speed "Clock Speed") __

### Power consumer

  * Power consumers work at the rate of user-defined clock speed. For example, a [Constructor](/wiki/Constructor "Constructor") works twice as fast when its clock speed is set to 200%.
  * It is always less power efficient when a building is overclocked. 
    * In the above example, its power consumption will be greater than 2x the usual power consumption. This also means a building at 200% consumes more power than 2 equal buildings each operating at 100%.
  * On the other hand, underclock a building saves power. 
    * Two constructors each working at 50% use less power compared to 1 Constructor working at 100%.
    * However, the footprint of the factory will be larger.



### Power generator

  * Power generators overclock differently from power consumers. However, their fuel consumption rate is always proportional to the power production of the building. Hence, overclocking a power generator will not increase fuel efficiency. 
    * This means the generator will burn the fuel faster or slower, but not produce more energy from the same amount of fuel.



## Energy

Energy is a derived unit of Power. When Power is being consumed (or produced) over some time, the product of Power and Time is called Energy. Where power fluctuates over time, the average power can be used instead. 

The unit of energy depends on the unit of Power and time measured. For example, 

  * `4 MW * 4 seconds = 16 MJ` the energy consumption of producing an [Iron Rod](/wiki/Iron_Rod "Iron Rod") in a [Constructor](/wiki/Constructor "Constructor"), with normal [Clock speed](/wiki/Clock_speed "Clock speed") and default recipe
  * `30 MW * 0.5 seconds = 15 MJ` the energy produced by [Leaves](/wiki/Leaves "Leaves") in a [Biomass Burner](/wiki/Biomass_Burner "Biomass Burner")
  * `2.5GW * 10 minutes = 2.5 GW * 600 seconds = 1500 GJ = 1.5 TJ` the energy produced by [Plutonium Fuel Rod](/wiki/Plutonium_Fuel_Rod "Plutonium Fuel Rod") in a [Nuclear Power Plant](/wiki/Nuclear_Power_Plant "Nuclear Power Plant")
  * `100 MW * 1 hour = 100 MWh = 360 GJ` the energy storage capacity of a [Power Storage](/wiki/Power_Storage "Power Storage")



Notes: 

  * `1 hour = 60 minutes = 3600 seconds`
  * `1 TW = 1000 GW = 1,000,000 MW` Similarly, `1 TJ = 1000 GJ = 1,000,000 MJ`



Energy can be used to compare the burning time of [Fuels](/wiki/Fuels "Fuels") in [vehicles](/wiki/Vehicle "Vehicle") or in generators, or comparing the energy efficiency between different [Alternate recipes](/wiki/Alternate_recipes "Alternate recipes") of an item. 

  * Stack energy is simply a product of energy and the number of items in its full [stack](/wiki/Stack "Stack").



Power Storages use MWh instead of MJ. 1 MWh equals 3 600 MJ. 

## Trivia

  * When interacting with any power building with a Power graph displayed, and if clicking on the graph for 6 times, the Power graph will first become glitched followed by a warning indicating that you are abusing the FICSIT property. The warning will go away if you close and re-open the Power graph.
  * A prototype of Satisfactory feature Wind Power, but it was removed.[1]


  * [](/wiki/File:Power_graph_glitched.png "This image will be displayed when the Power graph is clicked 6 times.")

This image will be displayed when the Power graph is clicked 6 times.

  * [](/wiki/File:Power_graph_warning.png "Shortly after that, this warning message will appear until you re-open the Power graph.")

Shortly after that, this warning message will appear until you re-open the Power graph.




## References

  1. ↑ [Instagram - February 26th, 2021 AMA - Can you bring wind turbines to Satisfactory?](/wiki/File:February_26th,_2021_Instagram_AMA_-_Can_you_bring_solar_power_and_wind_turbines_and_water_power_to_Satisfactory%3F.mp4 "File:February 26th, 2021 Instagram AMA - Can you bring solar power and wind turbines and water power to Satisfactory?.mp4")



## See also

  * [Clock Speed](/wiki/Clock_Speed "Clock Speed")
  * [Fuels](/wiki/Fuels "Fuels")
  * [](/wiki/Power_Line "Power Line") [Power Line](/wiki/Power_Line "Power Line")
  * [](/wiki/Power_Pole "Power Pole") [Power Pole](/wiki/Power_Pole "Power Pole")



  


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
