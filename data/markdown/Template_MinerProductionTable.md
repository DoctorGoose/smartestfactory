# Template:MinerProductionTable

Displays the amount that can be mined using different source-purities and miner-generations. 

## Usage

### Parameter

  * `1`: Amount of resources that can be gathered from a normal purity with a [Miner Mk.1](/wiki/Miner_Mk.1 "Miner Mk.1") or [Oil Extractor](/wiki/Oil_Extractor "Oil Extractor") per minute.
  * `miner`: The name of the miner, default is `Miner`. MK1-3 will be appended
  * `maxMK`: maximum of displayed columns for MK, possible values are 1 to 3, default is 3.
  * `maxRate`: maximum belt or pipe speed, default is 1200.



For example, `{{MinerProductionTable|maxRate = 780}}`

Items produced per minute

100% Clock Speed250% Clock Speed

| [Miner Mk.1](/wiki/Miner_Mk.1 "Miner Mk.1")| [Miner Mk.2](/wiki/Miner_Mk.2 "Miner Mk.2")| [Miner Mk.3](/wiki/Miner_Mk.3 "Miner Mk.3")  
---|---|---|---  
Impure| 30| 60| 120  
Normal| 60| 120| 240  
Pure| 120| 240| 480  
  
| [Miner Mk.1](/wiki/Miner_Mk.1 "Miner Mk.1")| [Miner Mk.2](/wiki/Miner_Mk.2 "Miner Mk.2")| [Miner Mk.3](/wiki/Miner_Mk.3 "Miner Mk.3")  
---|---|---|---  
Impure| 75| 150| 300  
Normal| 150| 300| 600  
Pure| 300| 600| 1200  
  
  


`{{MinerProductionTable|120|miner = [[Oil Extractor]]| maxMK = 1|maxRate = 300}}`

Items produced per minute

100% Clock Speed250% Clock Speed

| [Oil Extractor](/wiki/Oil_Extractor "Oil Extractor")  
---|---  
Impure| 60  
Normal| 120  
Pure| 240  
  
| [Oil Extractor](/wiki/Oil_Extractor "Oil Extractor")  
---|---  
Impure| 150  
Normal| 300  
Pure| 300
  *[v]: View this template
  *[e]: Edit this template
  *[h]: History of this template
  *[his]: his trivia section
  *[N/A]: Not applicable
