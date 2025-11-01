# Patch 0.4.0.9

Patch Notes: Early Access (EXPERIMENTAL) – **v0.4.0.9** – Build 149356. This patch was released on 6 April 2021.   
  
The original post can be viewed on Satisfactory's [Discord](https://discord.com/channels/370472939054956546/557603412565426196/829062124088590426), [Reddit](https://www.reddit.com/r/SatisfactoryGame/comments/mliidm), and [Steam](https://store.steampowered.com/news/app/526870/view/3015697429672926857). 

## Contents

  * 1 Intro
  * 2 Bug fixes
  * 3 UI
  * 4 Optimisation
  * 5 Localisation
  * 6 Known issues



## Intro

Hi Pioneers! 

We have another round of fixes and improvements coming right up after our Easter break :) 

As always if we somehow made things worse please let us know at our QA site <https://questions.satisfactorygame.com/> we read your posts every day. 

There’s more on the way since we’re trying to wrap up remaining issues before we move to our EA release, so please stay tuned, see you all again soon <3 

## Bug fixes

  * Fixed multiple instances of building SFX playing at the same time when near each other.
  * Attempt #5 to fix the crash in AFGReplicationDetailActor_BuildableFactory. This time it’s different, no, really, it is.
  * Made the hologram material slightly more bearable with reduced contrast, should help with being able to see text inside some holograms. Still subject to change.
  * Hopefully fixed Giant items being left behind in the world when unequipping stuff.
  * Additional check to see if the game is running or not, should reduce crashes in FGBackgroundthread.
  * Balanced sounds in equipment that changed during the engine upgrade.



## UI

  * [Inventory](/wiki/Inventory "Inventory") tooltips now display a maximum of 3 recipes, with a hint to the [codex](/wiki/Codex "Codex") if there are more alternate recipes.
  * Made Tooltips a bit more compact.



## Optimisation

  * Added distance cull to skeletal meshes.
  * Enabled only ticking when rendered for several skeletal meshes.
  * Texture2D Array sampling stability / performance test for factory material, should reduce GPU cost for factory buildings in general, mainly noticeable on lower spec machines.
  * Improved [light](/wiki/Lights "Lights") falloff settings, light should have a smooth transition when possible.
  * Upped lighting scalability. Lights should render much longer on higher settings. (Be sure to reset the Light Quality option in the video settings for it to work properly)



## Localisation

  * Fixed a bunch of mistakes and typos.
  * Updated scripts for test languages and completion rates
  * Updated all languages with the latest translations.
  * Updated completion rates.



## Known issues

  * [Battery](/wiki/Power_Storage "Power Storage") [_sic_] LODS will look a bit off this patch, VFX and Animated part will cull too early. Proper fix soon™
  * Texture tiling on some factory buildings will look off caused by the texture2D array test.



  * [v](/wiki/Template:PatchesNav "Template:PatchesNav")
  * [e](https://satisfactory.wiki.gg/wiki/Template:PatchesNav?action=edit)
  * [h](https://satisfactory.wiki.gg/wiki/Template:PatchesNav?action=history)

[Patches](/wiki/Category:Patch_notes "Category:Patch notes")  
---  
1.1| [1.1.1.0](/wiki/Patch_1.1.1.0 "Patch 1.1.1.0") • [1.1.1.1](/wiki/Patch_1.1.1.1 "Patch 1.1.1.1") • [1.1.1.2](/wiki/Patch_1.1.1.2 "Patch 1.1.1.2") • [1.1.1.3](/wiki/Patch_1.1.1.3 "Patch 1.1.1.3") • [1.1.1.4](/wiki/Patch_1.1.1.4 "Patch 1.1.1.4")  
Experimental 1.1| [1.1.0.0](/wiki/Patch_1.1.0.0 "Patch 1.1.0.0") • [1.1.0.1](/wiki/Patch_1.1.0.1 "Patch 1.1.0.1") • [1.1.0.2](/wiki/Patch_1.1.0.2 "Patch 1.1.0.2") • [1.1.0.3](/wiki/Patch_1.1.0.3 "Patch 1.1.0.3") • [1.1.0.4](/wiki/Patch_1.1.0.4 "Patch 1.1.0.4") • [1.1.0.5](/wiki/Patch_1.1.0.5 "Patch 1.1.0.5") • [1.1.0.6](/wiki/Patch_1.1.0.6 "Patch 1.1.0.6") • [1.1.1.5](/wiki/Patch_1.1.1.5 "Patch 1.1.1.5") • [1.1.1.6](/wiki/Patch_1.1.1.6 "Patch 1.1.1.6")  
1.0| [1.0](/wiki/Patch_1.0 "Patch 1.0") • [1.0.0.1](/wiki/Patch_1.0.0.1 "Patch 1.0.0.1") • [1.0.0.2](/wiki/Patch_1.0.0.2 "Patch 1.0.0.2") • [1.0.0.3](/wiki/Patch_1.0.0.3 "Patch 1.0.0.3") • [1.0.0.4](/wiki/Patch_1.0.0.4 "Patch 1.0.0.4") • [1.0.0.5](/wiki/Patch_1.0.0.5 "Patch 1.0.0.5") • [1.0.0.6](/wiki/Patch_1.0.0.6 "Patch 1.0.0.6") • [1.0.0.7](/wiki/Patch_1.0.0.7 "Patch 1.0.0.7") • [1.0.1.0](/wiki/Patch_1.0.1.0 "Patch 1.0.1.0") • [1.0.1.1](/wiki/Patch_1.0.1.1 "Patch 1.0.1.1") • [1.0.1.2](/wiki/Patch_1.0.1.2 "Patch 1.0.1.2") • [1.0.1.3](/wiki/Patch_1.0.1.3 "Patch 1.0.1.3") • [1.0.1.4](/wiki/Patch_1.0.1.4 "Patch 1.0.1.4")  
Experimental 1.0| [1.0.1.5](/wiki/Patch_1.0.1.5 "Patch 1.0.1.5") • [1.0.1.6](/wiki/Patch_1.0.1.6 "Patch 1.0.1.6")  
Update 8| [0.8.3.0](/wiki/Patch_0.8.3.0 "Patch 0.8.3.0") • [0.8.3.2](/wiki/Patch_0.8.3.2 "Patch 0.8.3.2") • [0.8.3.3](/wiki/Patch_0.8.3.3 "Patch 0.8.3.3")  
Experimental Update 8| [0.8.0.0](/wiki/Patch_0.8.0.0 "Patch 0.8.0.0") • [0.8.0.1](/wiki/Patch_0.8.0.1 "Patch 0.8.0.1") • [0.8.0.2](/wiki/Patch_0.8.0.2 "Patch 0.8.0.2") • [0.8.0.3](/wiki/Patch_0.8.0.3 "Patch 0.8.0.3") • [0.8.0.4](/wiki/Patch_0.8.0.4 "Patch 0.8.0.4") • [0.8.0.5](/wiki/Patch_0.8.0.5 "Patch 0.8.0.5") • [0.8.1.0](/wiki/Patch_0.8.1.0 "Patch 0.8.1.0") • [0.8.1.1](/wiki/Patch_0.8.1.1 "Patch 0.8.1.1") • [0.8.1.2](/wiki/Patch_0.8.1.2 "Patch 0.8.1.2") • [0.8.1.3](/wiki/Patch_0.8.1.3 "Patch 0.8.1.3") • [0.8.2.0](/wiki/Patch_0.8.2.0 "Patch 0.8.2.0") • [0.8.2.1](/wiki/Patch_0.8.2.1 "Patch 0.8.2.1") • [0.8.2.2](/wiki/Patch_0.8.2.2 "Patch 0.8.2.2") • [0.8.2.3](/wiki/Patch_0.8.2.3 "Patch 0.8.2.3") • [0.8.2.4](/wiki/Patch_0.8.2.4 "Patch 0.8.2.4") • [0.8.2.5](/wiki/Patch_0.8.2.5 "Patch 0.8.2.5") • [0.8.2.6](/wiki/Patch_0.8.2.6 "Patch 0.8.2.6") • [0.8.2.7](/wiki/Patch_0.8.2.7 "Patch 0.8.2.7") • [0.8.2.8](/wiki/Patch_0.8.2.8 "Patch 0.8.2.8") • [0.8.2.9](/wiki/Patch_0.8.2.9 "Patch 0.8.2.9") • [0.8.3.1](/wiki/Patch_0.8.3.1 "Patch 0.8.3.1")  
Update 7| [0.7.0.8](/wiki/Patch_0.7.0.8 "Patch 0.7.0.8") • [0.7.1.1](/wiki/Patch_0.7.1.1 "Patch 0.7.1.1")  
Experimental Update 7| [0.7.0.0](/wiki/Patch_0.7.0.0 "Patch 0.7.0.0") • [0.7.0.1](/wiki/Patch_0.7.0.1 "Patch 0.7.0.1") • [0.7.0.2](/wiki/Patch_0.7.0.2 "Patch 0.7.0.2") • [0.7.0.3](/wiki/Patch_0.7.0.3 "Patch 0.7.0.3") • [0.7.0.4](/wiki/Patch_0.7.0.4 "Patch 0.7.0.4") • [0.7.0.5](/wiki/Patch_0.7.0.5 "Patch 0.7.0.5") • [0.7.0.6](/wiki/Patch_0.7.0.6 "Patch 0.7.0.6") • [0.7.0.7](/wiki/Patch_0.7.0.7 "Patch 0.7.0.7") • [0.7.0.8 (Experimental)](/wiki/Patch_0.7.0.8_\(Experimental\) "Patch 0.7.0.8 \(Experimental\)")  
Update 6| [0.6.1.0](/wiki/Patch_0.6.1.0 "Patch 0.6.1.0") • [0.6.1.1](/wiki/Patch_0.6.1.1 "Patch 0.6.1.1") • [0.6.1.2](/wiki/Patch_0.6.1.2 "Patch 0.6.1.2") • [0.6.1.3](/wiki/Patch_0.6.1.3 "Patch 0.6.1.3") • [0.6.1.4](/wiki/Patch_0.6.1.4 "Patch 0.6.1.4") • [0.6.1.5](/wiki/Patch_0.6.1.5 "Patch 0.6.1.5")  
Experimental Update 6| [0.6.0.0](/wiki/Patch_0.6.0.0 "Patch 0.6.0.0") • [0.6.0.1](/wiki/Patch_0.6.0.1 "Patch 0.6.0.1") • [0.6.0.2](/wiki/Patch_0.6.0.2 "Patch 0.6.0.2") • [0.6.0.3](/wiki/Patch_0.6.0.3 "Patch 0.6.0.3") • [0.6.0.4](/wiki/Patch_0.6.0.4 "Patch 0.6.0.4") • [0.6.0.5](/wiki/Patch_0.6.0.5 "Patch 0.6.0.5") • [0.6.0.6](/wiki/Patch_0.6.0.6 "Patch 0.6.0.6") • [0.6.0.7](/wiki/Patch_0.6.0.7 "Patch 0.6.0.7") • [0.6.0.8](/wiki/Patch_0.6.0.8 "Patch 0.6.0.8") • [0.6.0.9](/wiki/Patch_0.6.0.9 "Patch 0.6.0.9") • [0.6.0.10](/wiki/Patch_0.6.0.10 "Patch 0.6.0.10") • [0.6.0.11](/wiki/Patch_0.6.0.11 "Patch 0.6.0.11") • [0.6.0.12](/wiki/Patch_0.6.0.12 "Patch 0.6.0.12") • [0.6.0.13](/wiki/Patch_0.6.0.13 "Patch 0.6.0.13") • [0.6.0.14](/wiki/Patch_0.6.0.14 "Patch 0.6.0.14") • [0.6.0.15](/wiki/Patch_0.6.0.15 "Patch 0.6.0.15")  
Update 5| [0.5.1.0](/wiki/Patch_0.5.1.0 "Patch 0.5.1.0") • [0.5.1.1](/wiki/Patch_0.5.1.1 "Patch 0.5.1.1") • [0.5.1.3](/wiki/Patch_0.5.1.3 "Patch 0.5.1.3") • [0.5.1.4](/wiki/Patch_0.5.1.4 "Patch 0.5.1.4") • [0.5.1.5](/wiki/Patch_0.5.1.5 "Patch 0.5.1.5") • [0.5.1.7](/wiki/Patch_0.5.1.7 "Patch 0.5.1.7") • [0.5.1.8](/wiki/Patch_0.5.1.8 "Patch 0.5.1.8") • [0.5.1.10](/wiki/Patch_0.5.1.10 "Patch 0.5.1.10") • [0.5.2.0](/wiki/Patch_0.5.2.0 "Patch 0.5.2.0") • [0.5.2.1](/wiki/Patch_0.5.2.1 "Patch 0.5.2.1")  
Experimental Update 5| [0.5.0.0](/wiki/Patch_0.5.0.0 "Patch 0.5.0.0") • [0.5.0.1](/wiki/Patch_0.5.0.1 "Patch 0.5.0.1") • [0.5.0.2](/wiki/Patch_0.5.0.2 "Patch 0.5.0.2") • [0.5.0.3](/wiki/Patch_0.5.0.3 "Patch 0.5.0.3") • [0.5.0.4](/wiki/Patch_0.5.0.4 "Patch 0.5.0.4") • [0.5.0.5](/wiki/Patch_0.5.0.5 "Patch 0.5.0.5") • [0.5.0.6](/wiki/Patch_0.5.0.6 "Patch 0.5.0.6") • [0.5.0.7](/wiki/Patch_0.5.0.7 "Patch 0.5.0.7") • [0.5.0.8](/wiki/Patch_0.5.0.8 "Patch 0.5.0.8") • [0.5.0.9](/wiki/Patch_0.5.0.9 "Patch 0.5.0.9") • [0.5.0.10](/wiki/Patch_0.5.0.10 "Patch 0.5.0.10") • [0.5.0.11](/wiki/Patch_0.5.0.11 "Patch 0.5.0.11") • [0.5.0.12](/wiki/Patch_0.5.0.12 "Patch 0.5.0.12") • [0.5.0.13](/wiki/Patch_0.5.0.13 "Patch 0.5.0.13") • [0.5.0.14](/wiki/Patch_0.5.0.14 "Patch 0.5.0.14") • [0.5.1.2](/wiki/Patch_0.5.1.2 "Patch 0.5.1.2") • [0.5.1.6](/wiki/Patch_0.5.1.6 "Patch 0.5.1.6") • [0.5.1.9](/wiki/Patch_0.5.1.9 "Patch 0.5.1.9") • [0.5.1.11](/wiki/Patch_0.5.1.11 "Patch 0.5.1.11") • [0.5.1.12](/wiki/Patch_0.5.1.12 "Patch 0.5.1.12") • [0.5.1.13](/wiki/Patch_0.5.1.13 "Patch 0.5.1.13")  
Update 4| [0.4.1.0](/wiki/Patch_0.4.1.0 "Patch 0.4.1.0") • [0.4.1.1](/wiki/Patch_0.4.1.1 "Patch 0.4.1.1") • [0.4.2.0](/wiki/Patch_0.4.2.0 "Patch 0.4.2.0") • [0.4.2.2](/wiki/Patch_0.4.2.2 "Patch 0.4.2.2") • [0.4.2.5](/wiki/Patch_0.4.2.5 "Patch 0.4.2.5") • [0.4.2.7](/wiki/Patch_0.4.2.7 "Patch 0.4.2.7") • [0.4.2.9](/wiki/Patch_0.4.2.9 "Patch 0.4.2.9") • [0.4.2.11](/wiki/Patch_0.4.2.11 "Patch 0.4.2.11")  
Experimental Update 4| [0.4.0.0](/wiki/Patch_0.4.0.0 "Patch 0.4.0.0") • [0.4.0.1](/wiki/Patch_0.4.0.1 "Patch 0.4.0.1") • [0.4.0.2](/wiki/Patch_0.4.0.2 "Patch 0.4.0.2") • [0.4.0.3](/wiki/Patch_0.4.0.3 "Patch 0.4.0.3") • [0.4.0.4](/wiki/Patch_0.4.0.4 "Patch 0.4.0.4") • [0.4.0.5](/wiki/Patch_0.4.0.5 "Patch 0.4.0.5") • [0.4.0.6](/wiki/Patch_0.4.0.6 "Patch 0.4.0.6") • [0.4.0.7](/wiki/Patch_0.4.0.7 "Patch 0.4.0.7") • [0.4.0.8](/wiki/Patch_0.4.0.8 "Patch 0.4.0.8") • 0.4.0.9 • [0.4.0.10](/wiki/Patch_0.4.0.10 "Patch 0.4.0.10") • [0.4.0.11](/wiki/Patch_0.4.0.11 "Patch 0.4.0.11") • [0.4.0.12](/wiki/Patch_0.4.0.12 "Patch 0.4.0.12") • [0.4.2.1](/wiki/Patch_0.4.2.1 "Patch 0.4.2.1") • [0.4.2.2 (Experimental)](/wiki/Patch_0.4.2.2_\(Experimental\) "Patch 0.4.2.2 \(Experimental\)") • [0.4.2.3](/wiki/Patch_0.4.2.3 "Patch 0.4.2.3") • [0.4.2.4](/wiki/Patch_0.4.2.4 "Patch 0.4.2.4") • [0.4.2.6](/wiki/Patch_0.4.2.6 "Patch 0.4.2.6") • [0.4.2.8](/wiki/Patch_0.4.2.8 "Patch 0.4.2.8") • [0.4.2.10](/wiki/Patch_0.4.2.10 "Patch 0.4.2.10") • [0.4.3.0](/wiki/Patch_0.4.3.0 "Patch 0.4.3.0") • [0.4.3.1](/wiki/Patch_0.4.3.1 "Patch 0.4.3.1")  
Update 3  
& Steam Release| [0.3.3.3](/wiki/Patch_0.3.3.3 "Patch 0.3.3.3") • [0.3.3.4](/wiki/Patch_0.3.3.4 "Patch 0.3.3.4") • [0.3.3.5](/wiki/Patch_0.3.3.5 "Patch 0.3.3.5") • [0.3.3.6](/wiki/Patch_0.3.3.6 "Patch 0.3.3.6") • [0.3.4.14](/wiki/Patch_0.3.4.14 "Patch 0.3.4.14") • [0.3.4.15](/wiki/Patch_0.3.4.15 "Patch 0.3.4.15") • [0.3.4.16](/wiki/Patch_0.3.4.16 "Patch 0.3.4.16") • [0.3.5](/wiki/Patch_0.3.5 "Patch 0.3.5") • [0.3.5.1](/wiki/Patch_0.3.5.1 "Patch 0.3.5.1") • [0.3.5.2](/wiki/Patch_0.3.5.2 "Patch 0.3.5.2") • [0.3.5.3](/wiki/Patch_0.3.5.3 "Patch 0.3.5.3") • [0.3.5.4](/wiki/Patch_0.3.5.4 "Patch 0.3.5.4") • [0.3.5.6](/wiki/Patch_0.3.5.6 "Patch 0.3.5.6") • [0.3.6.5](/wiki/Patch_0.3.6.5 "Patch 0.3.6.5") • [0.3.7](/wiki/Patch_0.3.7 "Patch 0.3.7") • [0.3.7.1](/wiki/Patch_0.3.7.1 "Patch 0.3.7.1") • [0.3.7.2](/wiki/Patch_0.3.7.2 "Patch 0.3.7.2") • [0.3.7.3](/wiki/Patch_0.3.7.3 "Patch 0.3.7.3") • [0.3.7.4](/wiki/Patch_0.3.7.4 "Patch 0.3.7.4") • [0.3.7.5](/wiki/Patch_0.3.7.5 "Patch 0.3.7.5") • [0.3.7.6](/wiki/Patch_0.3.7.6 "Patch 0.3.7.6") • [0.3.7.7](/wiki/Patch_0.3.7.7 "Patch 0.3.7.7")  
Experimental Update 3  
& Steam Release| [0.3](/wiki/Patch_0.3 "Patch 0.3") • [0.3.0.1](/wiki/Patch_0.3.0.1 "Patch 0.3.0.1") • [0.3.0.2](/wiki/Patch_0.3.0.2 "Patch 0.3.0.2") • [0.3.1.0](/wiki/Patch_0.3.1.0 "Patch 0.3.1.0") • [0.3.1.1](/wiki/Patch_0.3.1.1 "Patch 0.3.1.1") • [0.3.1.2](/wiki/Patch_0.3.1.2 "Patch 0.3.1.2") • [0.3.2.0](/wiki/Patch_0.3.2.0 "Patch 0.3.2.0") • [0.3.2.1](/wiki/Patch_0.3.2.1 "Patch 0.3.2.1") • [0.3.2.2](/wiki/Patch_0.3.2.2 "Patch 0.3.2.2") • [0.3.3.0](/wiki/Patch_0.3.3.0 "Patch 0.3.3.0") • [0.3.3.1](/wiki/Patch_0.3.3.1 "Patch 0.3.3.1") • [0.3.3.2](/wiki/Patch_0.3.3.2 "Patch 0.3.3.2") • [0.3.3.4](/wiki/Patch_0.3.3.4 "Patch 0.3.3.4") • [0.3.3.5](/wiki/Patch_0.3.3.5 "Patch 0.3.3.5") • [0.3.4.0](/wiki/Patch_0.3.4.0 "Patch 0.3.4.0") • [0.3.4.1](/wiki/Patch_0.3.4.1 "Patch 0.3.4.1") • [0.3.4.2](/wiki/Patch_0.3.4.2 "Patch 0.3.4.2") • [0.3.4.3](/wiki/Patch_0.3.4.3 "Patch 0.3.4.3") • [0.3.4.4](/wiki/Patch_0.3.4.4 "Patch 0.3.4.4") • [0.3.4.5](/wiki/Patch_0.3.4.5 "Patch 0.3.4.5") • [0.3.4.6](/wiki/Patch_0.3.4.6 "Patch 0.3.4.6") • [0.3.4.7](/wiki/Patch_0.3.4.7 "Patch 0.3.4.7") • [0.3.4.8](/wiki/Patch_0.3.4.8 "Patch 0.3.4.8") • [0.3.4.9](/wiki/Patch_0.3.4.9 "Patch 0.3.4.9") • [0.3.4.10](/wiki/Patch_0.3.4.10 "Patch 0.3.4.10") • [0.3.4.11](/wiki/Patch_0.3.4.11 "Patch 0.3.4.11") • [0.3.4.12](/wiki/Patch_0.3.4.12 "Patch 0.3.4.12") • [0.3.4.13](/wiki/Patch_0.3.4.13 "Patch 0.3.4.13") • [0.3.5.5](/wiki/Patch_0.3.5.5 "Patch 0.3.5.5") • [0.3.6](/wiki/Patch_0.3.6 "Patch 0.3.6") • [0.3.6.1](/wiki/Patch_0.3.6.1 "Patch 0.3.6.1") • [0.3.6.2](/wiki/Patch_0.3.6.2 "Patch 0.3.6.2") • [0.3.6.3](/wiki/Patch_0.3.6.3 "Patch 0.3.6.3") • [0.3.6.4](/wiki/Patch_0.3.6.4 "Patch 0.3.6.4") • [0.3.6.6](/wiki/Patch_0.3.6.6 "Patch 0.3.6.6") • [0.3.6.7](/wiki/Patch_0.3.6.7 "Patch 0.3.6.7") • [0.3.6.8](/wiki/Patch_0.3.6.8 "Patch 0.3.6.8") • [0.3.6.9](/wiki/Patch_0.3.6.9 "Patch 0.3.6.9") • [0.3.6.10](/wiki/Patch_0.3.6.10 "Patch 0.3.6.10") • [0.3.6.11](/wiki/Patch_0.3.6.11 "Patch 0.3.6.11") • [0.3.6.12](/wiki/Patch_0.3.6.12 "Patch 0.3.6.12") • [0.3.6.13](/wiki/Patch_0.3.6.13 "Patch 0.3.6.13") • [0.3.8.0](/wiki/Patch_0.3.8.0 "Patch 0.3.8.0") • [0.3.8.1](/wiki/Patch_0.3.8.1 "Patch 0.3.8.1") • [0.3.8.2](/wiki/Patch_0.3.8.2 "Patch 0.3.8.2") • [0.3.8.3](/wiki/Patch_0.3.8.3 "Patch 0.3.8.3") • [0.3.8.4](/wiki/Patch_0.3.8.4 "Patch 0.3.8.4") • [0.3.8.5](/wiki/Patch_0.3.8.5 "Patch 0.3.8.5") • [0.3.8.6](/wiki/Patch_0.3.8.6 "Patch 0.3.8.6") • [0.3.8.7](/wiki/Patch_0.3.8.7 "Patch 0.3.8.7") • [0.3.8.8](/wiki/Patch_0.3.8.8 "Patch 0.3.8.8") • [0.3.8.9](/wiki/Patch_0.3.8.9 "Patch 0.3.8.9") • [0.3.8.10](/wiki/Patch_0.3.8.10 "Patch 0.3.8.10") • [0.3.8.11](/wiki/Patch_0.3.8.11 "Patch 0.3.8.11")  
Update 2| [0.2.1](/wiki/Patch_0.2.1 "Patch 0.2.1") • [0.2.1.1](/wiki/Patch_0.2.1.1 "Patch 0.2.1.1") • [0.2.1.2](/wiki/Patch_0.2.1.2 "Patch 0.2.1.2") • [0.2.1.3](/wiki/Patch_0.2.1.3 "Patch 0.2.1.3") • [ 0.2.1.4](/wiki/Patch_0.2.1.4 "Patch 0.2.1.4") • [ 0.2.1.5](/wiki/Patch_0.2.1.5 "Patch 0.2.1.5") • [0.2.1.7](/wiki/Patch_0.2.1.7 "Patch 0.2.1.7") • [0.2.1.10](/wiki/Patch_0.2.1.10 "Patch 0.2.1.10") • [0.2.1.12](/wiki/Patch_0.2.1.12 "Patch 0.2.1.12") • [0.2.1.17](/wiki/Patch_0.2.1.17 "Patch 0.2.1.17") • [0.2.1.18](/wiki/Patch_0.2.1.18 "Patch 0.2.1.18")  
Experimental Update 2| [0.1.14](/wiki/Patch_0.1.14 "Patch 0.1.14") • [0.1.15](/wiki/Patch_0.1.15 "Patch 0.1.15") • [0.1.16](/wiki/Patch_0.1.16 "Patch 0.1.16") • [0.1.17 (101256)](/wiki/Patch_0.1.17 "Patch 0.1.17") • [0.1.17 (101353)](/wiki/Patch_0.1.17_build_101353 "Patch 0.1.17 build 101353") • [0.1.19](/wiki/Patch_0.1.19 "Patch 0.1.19") • [0.1.20](/wiki/Patch_0.1.20 "Patch 0.1.20") • [0.2.1.6](/wiki/Patch_0.2.1.6 "Patch 0.2.1.6") • [0.2.1.7 (Experimental)](/wiki/Patch_0.2.1.7_\(Experimental\) "Patch 0.2.1.7 \(Experimental\)") • [0.2.1.8](/wiki/Patch_0.2.1.8 "Patch 0.2.1.8") • [0.2.1.9](/wiki/Patch_0.2.1.9 "Patch 0.2.1.9") • [0.2.1.11](/wiki/Patch_0.2.1.11 "Patch 0.2.1.11") • [0.2.1.12 (Experimental)](/wiki/Patch_0.2.1.12_\(Experimental\) "Patch 0.2.1.12 \(Experimental\)") • [0.2.1.13](/wiki/Patch_0.2.1.13 "Patch 0.2.1.13") • [0.2.1.14](/wiki/Patch_0.2.1.14 "Patch 0.2.1.14") • [0.2.1.15](/wiki/Patch_0.2.1.15 "Patch 0.2.1.15") • [0.2.1.16](/wiki/Patch_0.2.1.16 "Patch 0.2.1.16") • [0.2.1.17 (Experimental)](/wiki/Patch_0.2.1.17_\(Experimental\) "Patch 0.2.1.17 \(Experimental\)") • [0.2.1.19](/wiki/Patch_0.2.1.19 "Patch 0.2.1.19") • [0.2.1.20](/wiki/Patch_0.2.1.20 "Patch 0.2.1.20")  
Update 1| [0.1.11](/wiki/Patch_0.1.11 "Patch 0.1.11") • [0.1.12](/wiki/Patch_0.1.12 "Patch 0.1.12") • [0.1.13](/wiki/Patch_0.1.13 "Patch 0.1.13")  
Experimental Update 1| [0.1.5](/wiki/Patch_0.1.5 "Patch 0.1.5") • [0.1.6 (98394)](/wiki/Patch_0.1.6_build_98394 "Patch 0.1.6 build 98394") • [0.1.6 (98445)](/wiki/Patch_0.1.6_build_98445 "Patch 0.1.6 build 98445") • [0.1.7](/wiki/Patch_0.1.7 "Patch 0.1.7") • [0.1.8](/wiki/Patch_0.1.8 "Patch 0.1.8") • [0.1.9](/wiki/Patch_0.1.9 "Patch 0.1.9") • [0.1.10](/wiki/Patch_0.1.10 "Patch 0.1.10")  
Early Access Release| [0.1](/wiki/Patch_0.1 "Patch 0.1") • [0.101](/wiki/Patch_0.101 "Patch 0.101") • [0.102](/wiki/Patch_0.102 "Patch 0.102") • [0.103](/wiki/Patch_0.103 "Patch 0.103") • [0.104](/wiki/Patch_0.104 "Patch 0.104")  
Closed Alpha| [Early game development](/wiki/Early_game_development "Early game development") • [2018-10-11](/wiki/Patch_2018-10-11 "Patch 2018-10-11") • [2018-10-17](/wiki/Patch_2018-10-17 "Patch 2018-10-17") • [2018-10-19](/wiki/Patch_2018-10-19 "Patch 2018-10-19") • [2018-10-27](/wiki/Patch_2018-10-27 "Patch 2018-10-27") • [2](/wiki/Patch_Closed_Alpha_2 "Patch Closed Alpha 2") • [2.1](/wiki/Patch_Closed_Alpha_2.1 "Patch Closed Alpha 2.1") • [3](/wiki/Patch_Closed_Alpha_3 "Patch Closed Alpha 3") • [3.1](/wiki/Patch_Closed_Alpha_3.1 "Patch Closed Alpha 3.1") • [3.2](/wiki/Patch_Closed_Alpha_3.2 "Patch Closed Alpha 3.2") • [4](/wiki/Patch_Closed_Alpha_4 "Patch Closed Alpha 4") • [4.1](/wiki/Patch_Closed_Alpha_4.1 "Patch Closed Alpha 4.1") • [Alpha Test Weekend](/wiki/Alpha_Test_Weekend "Alpha Test Weekend") • [5](/wiki/Patch_Closed_Alpha_5 "Patch Closed Alpha 5") • [5.1](/wiki/Patch_Closed_Alpha_5.1 "Patch Closed Alpha 5.1") • [5.3](/wiki/Patch_Closed_Alpha_5.3 "Patch Closed Alpha 5.3")
  *[v]: View this template
  *[e]: Edit this template
  *[h]: History of this template
  *[his]: his trivia section
