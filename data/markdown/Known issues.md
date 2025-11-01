# Known issues

# [Update 5](/wiki/Patch_0.5.1.0 "Patch 0.5.1.0")

  * Packet routing is incompatible with multihome, so we're automatically disabling the former when the latter is enabled


  * A reminder for people who have been having issues with unexpected crashes on startup or weird behavior with the game, in that case please try to verify your game files. You can do this on Steam by Right Clicking the game in your **Library > Properties > Local Files > Verify integrity of game files**... And on Epic by clicking on the **three dots** (“...”) next to the title or at the right side, depending on your selected library view > **Verify**. This may or may not redownload a large amount of files which might take a while depending on your internet connection or hard drive speeds so be wary of that.


  * If you are using mods, they might need to be updated or uninstalled after updating so please keep this in mind too.


  * If you are experiencing issues launching the game or loading a save and you have already verified your files, you might have some incompatibility with DX12 as the default renderer, you can try the following launch options to try to force DX11, DX12 or Vulkan to run respectively. 
    * `-d3d11`
    * `-DX11`
    * `-d3d12`
    * `-DX12`
    * `-vulkan`


  * Dedicated Server Crash reports, Currently Crashes that happen on a Dedicated Server are automatically sent to us, this is enabled by default, we plan on including a toggle for this in GUI but for the moment, if you want to disable automatically sending crash logs you can do this: 
    * Go to the Server Install folder
    * Open “Engine.ini”
    * Add the following:


    
    
       [CrashReportClient]
       bImplicitSend=False
    

  *     * Save changes and restart the Server


  * To Disable Seasonal Events on Dedic`ated Server, you need to enter this command from the server console and then reload the game or restart the server: (Save and Load from the Save Manager also works)


    
    
       FG.DisableSeasonalEvents 1
    

  *     * Using the following launch option should also work:


    
    
       -DisableSeasonalEvents
    

  * Packet routing is incompatible with multihome, so we're automatically disabling the former when the latter is enabled


  *[v]: View this template
  *[e]: Edit this template
  *[h]: History of this template
  *[his]: his trivia section
