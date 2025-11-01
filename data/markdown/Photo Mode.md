# Photo Mode

**Photo Mode** allows taking screenshots within the game, while allowing to hide the user interface, detach the camera from the [pioneer](/wiki/Pioneer "Pioneer") or apply effects. 

It can be accessed using [`P`](/wiki/Controls "Controls") which will display the photo mode overlay along with the photo mode hotbar on the bottom.[1]

NOTE: The game does not pause while using Photo Mode.[2]

## Contents

  * 1 Overlay
    * 1.1 Gauges
    * 1.2 Hotbar
  * 2 Decoupled camera
  * 3 Settings
    * 3.1 General
    * 3.2 Camera
      * 3.2.1 Camera settings
      * 3.2.2 Other
    * 3.3 Image
      * 3.3.1 Color correction
      * 3.3.2 Effect settings
    * 3.4 Pioneer
      * 3.4.1 Pose
      * 3.4.2 Positioning
  * 4 Color filters
  * 5 Effect filters
  * 6 Pioneer poses
    * 6.1 Default
    * 6.2 Emotes
    * 6.3 Action
      * 6.3.1 Standing
      * 6.3.2 Seated
      * 6.3.3 Sleep, kneel, pray
      * 6.3.4 Dance
  * 7 Dolly
    * 7.1 Settings
    * 7.2 Usage
      * 7.2.1 Setting start point and end point
      * 7.2.2 Tracking point
      * 7.2.3 Blend camera settings
      * 7.2.4 Interpolation
    * 7.3 Recording
  * 8 Vehicles
  * 9 History
  * 10 References



## Overlay

The overlay does not appear in any screenshots and when using the Dolly function. However, equipped [equipment](/wiki/Inventory#Equipment_slots "Inventory") will appear and can be unequipped or holstered [`H`](/wiki/Controls "Controls") if desired. Hiding [Hoverpack](/wiki/Hoverpack "Hoverpack") controls is not possible while airborne. 

### Gauges

In addition to corner lines showing the area which will be captured, there is also a left and right gauge. 

  * **Left gauge:** Displays an arrow ◀ showing the camera altitude in relation to the pioneer (player). When the arrow is on the bottom, the camera is level with the pioneer, otherwise it's higher than the pioneer.
  * **Right gauge:** Displays an arrow ▶ showing the camera zoom. When the arrow is on the bottom, the camera is fully zoomed out, when it's at the top, it's fully zoomed in.



### Hotbar

The Photo Mode hotbar is displayed on the bottom and has the following functions: 

Keyboard/mouse  | Function  | Notes   
---|---|---  
[`Tab ↹`](/wiki/Controls "Controls") | Show / Hide settings  | Displays or removes the main Photo Mode UI.   
[](/wiki/File:Keyboard_White_Mouse_Left.png "Left") | Take Photo  | See Settings > General below.   
[`R`](/wiki/Controls "Controls") | Enable Decoupled Camera  | Allows third person view mode and enables free movement of camera.   
[`F`](/wiki/Controls "Controls") | Focus  | Sets the focus distance to what is shown in the center of the camera.   
[`T`](/wiki/Controls "Controls") | Hide UI  | Removes the Photo Mode overlay and hotbars to allow screen recording.   
  
  * [](/wiki/File:Photo_Mode_0.png "Photo Mode overlay")

Photo Mode overlay




## Decoupled camera

Pressing [`R`](/wiki/Controls "Controls") will decouple from or restore the camera's normal first-person view. When decoupled, the camera will be in third-person view[3] and can be controlled as follows: 

Keyboard/mouse  | Action  | Notes   
---|---|---  
[`W`](/wiki/Controls "Controls") | Move forward  |   
[`A`](/wiki/Controls "Controls") | Move left  |   
[`S`](/wiki/Controls "Controls") | Move backwards  |   
[`D`](/wiki/Controls "Controls") | Move right  |   
[`Space`](/wiki/Controls "Controls") | Move up  |   
[`C`](/wiki/Controls "Controls") | Move down  |   
[](/wiki/File:Keyboard_White_Mouse_None.png "None") | Move around  | Not re-bindable.   
[`⇧ Left Shift`](/wiki/Controls "Controls") | Sprint  | Used to fly faster.   
  
The decoupled camera has a maximum distance of 150m (soft limit) to 160m (hard limit), which is 18 to 20 Foundations, that it can move from the pioneer.[4] In between 150m and 160m rubber-banding will occur to bring you back to 150m.[5]

## Settings

Pressing [`T`](/wiki/Controls "Controls") will display the settings UI with tabs for **Camera** , **Image** , and **Pioneer** , along with **Show Dolly Settings**.[6][7]

### General

At bottom of Photo Mode Settings UI you have the following buttons: 

  * **Take photo** : Takes a photo, just like pressing [](/wiki/File:Keyboard_White_Mouse_Left.png "Left").
  * **Open Screenshot Folder** : Opens the following directory: 
    * Windows (both Steam and Epic use the same directory) 
      * `%LOCALAPPDATA%\FactoryGame\Saved\Screenshots\Windows`
      * `C:\Users\<your Windows username>\AppData\Local\FactoryGame\Saved\Screenshots\Windows`
    * Linux 
      * Using Steam Play (one of these locations): 
        * `~/.local/share/Steam/steamapps/compatdata/526870/pfx/drive_c/users/steamuser/Local Settings/Application Data/FactoryGame/Saved/Screenshots/Windows`
        * `~/.steam/steam/steamapps/compatdata/526870/pfx/drive_c/users/steamuser/Local Settings/Application Data/FactoryGame/Saved/Screenshots/Windows`
      * Steam: `~/.var/app/com.valvesoftware.Steam/.local/share/Steam/steamapps/compatdata/526870/pfx/drive_c/users/steamuser/AppData/Local/FactoryGame/Saved/Screenshots/Windows`
      * Steam (installation on another drive than your home dir): `{YOUR DRIVE}/SteamLibrary/steamapps/compatdata/526870/pfx/drive_c/users/steamuser/AppData/Local/FactoryGame/Saved/Screenshots/Windows`
    * Steam Deck 
      * `/home/deck/.steam/root/steamapps/compatdata/526870/pfx/dosdevices/c:/users/steamuser/AppData/Local/FactoryGame/Saved/Screenshots/`
      * **⭑ NOTE:** Steam Deck screenshots are within a hidden folder, and you must first show hidden files before you can view the folder via the Steam Deck File Explorer.[8] Files are contained in a compacted data folder named 526870.
    * Unraid, Docker 
      * ich777/steamcmd:satisfactory: `/mnt/user/appdata/satisfactory/.config/Epic/FactoryGame/Saved/Screenshots/Windows`
  * Reset will restore Photo Mode settings to their defaults.



### Camera

#### Camera settings

The following camera settings are available: 

Setting  | Options  | Default  | Effects   
---|---|---|---  
Camera Mode  | First Person, Decoupled  | First Person  |   
Zoom  | 1 to 100  | 50  | Range is 1 (zoomed in) to 100 (zoomed out).  
Zoom can be optionally used as binoculars by zooming in which can help during exploration and aids in determining what distant objects are.   
Roll  | -45 to +45  | 0  | Rolls camera counterclockwise (negative) or clockwise (positive).   
Aperture[9] | 0.001 to 24.000  | 24.000  | Controls image depth of field where smaller numbers open the aperture making the image more blurry, while larger numbers close the aperture making image more focused.   
Focus Mode[note 1][10] | Manual Focus, Auto Focus, Tracking  | Auto Focus  | **Manual Focus** allows player manually choose level and what to focus on.  
**Auto Focus** will automatically focus on what is in center of camera.  
**Tracking** sets focal point that remains in focus regardless of where the camera is moved.   
Focus Distance[note 2] | 0.000 to 10.000  | 0.500  | Controls how far away the focal point is from the camera in meters where smaller number is more blurry and larger number is more focused.   
Focus[note 2] | Set (Button)  | N/A  | Sets focus distance to what is shown in center of camera.   
Set Tracking Point[note 3] | Set (Button)  | N/A  | Sets a focal point.   
  
Notes: 

  1. ↑ Greyed out until you change Aperture value below 24.000.
  2. ↑ 2.0 2.1 Additional setting when using Manual Focus.
  3. ↑ Additional setting when using Tracking.



  * [](/wiki/File:Photo_Mode_1.png "Photo Mode settings UI with the camera tab selected")

Photo Mode settings UI with the camera tab selected

  * [](/wiki/File:Photo_Mode_2a.png "Photo Mode camera aperture setting where the aperture is fully closed and the image is more focused")

Photo Mode camera aperture setting where the aperture is fully closed and the image is more focused

  * [](/wiki/File:Photo_Mode_2b.png "Photo Mode camera aperture setting where the aperture is fully open and the image is more blurry")

Photo Mode camera aperture setting where the aperture is fully open and the image is more blurry




#### Other

The following additional camera settings are available: 

Setting  | Options  | Default  | Effects   
---|---|---|---  
Grid  | None, Grid 1, Grid 2  | None  | **Grid 1** is the 3 by 3 square grid.  
**Grid 2** is simplified with marks around the edges along with crosses "+" in center of screen.   
Crop[11] | None, Square, Portrait, Anamorphic, Cinerama, 4:3, Super Ultra Wide  | None  | Used to improve composition, focus the viewer's attention on the main subject, and adapt the image to different formats or aspect ratios.   
  
  * [](/wiki/File:Photo_Mode_3a.png "Grid 1")

Grid 1

  * [](/wiki/File:Photo_Mode_3b.png "Grid 2")

Grid 2

  * [](/wiki/File:Photo_Mode_3c.png "Square crop")

Square crop

  * [](/wiki/File:Photo_Mode_3d.png "Portrait crop")

Portrait crop

  * [](/wiki/File:Photo_Mode_3e.png "Anamorphic crop")

Anamorphic crop

  * [](/wiki/File:Photo_Mode_3f.png "Cinerama crop")

Cinerama crop

  * [](/wiki/File:Photo_Mode_3g.png "4:3 crop")

4:3 crop

  * [](/wiki/File:Photo_Mode_3h.png "Super Ultra Wide crop")

Super Ultra Wide crop




### Image

These settings are similar to what you find in most photo editing software. 

#### Color correction

The following image color correction settings are available:[12][13]

Setting  | Options  | Default  | Effects   
---|---|---|---  
Exposure  | -5.0 to 5.0  | 1.0  | Adjusts the overall brightness or darkness of an image.   
Saturation  | 0.0 to 2.0  | 1.0  | Adjusts the intensity or purity of colors in an image   
Contrast  | 0.0 to 2.0  | 1.0  | Adjusts the light and dark areas in an image.   
Tint  | -1.0 to 1.0  | 0.0  | Adds a subtle or strong color overlay to an image, affecting the overall color balance and mood.   
Tint Intensity[note 1] | 0.0 to 1.0  | 0.5  | Adjusts the intensity of the tint color to make it stronger or weaker.   
Color Filter  | None, Sepia, Vibrant, Sunset, Lonely, Negative, Good Ol' Days, 2007, Somebody's Sky, Cheese Times, Metro, The Ring, End of Times, LCD, Vice, Orange and Purple  | None  | Used to enhance certain colors, create specific moods, or correct color inaccuracies.  
See also color filters below.   
Color Filter Strength[note 2] | 0.0 to 1.0  | 1.0  | Sets the intensity of the color filter used.   
  
Notes: 

  1. ↑ Additional setting when Tint is not 0.0.
  2. ↑ Additional setting when using Color Filter other than None.



  * [](/wiki/File:Photo_Mode_4a.png "Color correction UI")

Color correction UI




#### Effect settings

The following image effect settings are available:[14]

Setting  | Options  | Default  | Effects   
---|---|---|---  
Effect Filter  | None, Posterized, Noire, Pixel Posterized, Pixel, Kuwahara, Poster, Comic, Fresnel, VHS  | None  | Modifies the appearance of an image by altering various aspects like color, brightness, contrast, and texture.  
See also effect filters below.   
Effects Filter Intensity[note 1] | -1.0 to 1.0  | 0.0  | Adjusts the amount (more or less) of the effect selected.   
Bloom  | 1.0 to 100.0  | 1.0  | Simulates the optical phenomenon where light from a bright source seems to "leak" or "bloom" into surrounding areas, creating a soft, hazy glow.   
Aberration  | 0.0 to 20.0  | 0.0  | Simulate the optical imperfections, specifically [chromatic aberration](https://en.wikipedia.org/wiki/Chromatic_aberration), which causes color fringing around edges in an image resulting from the separation of the red, blue, and green image layers.   
Vignette  | 0.0 to 5.0  | 0.0  | Darkens or lightens the edges of an image, while leaving the center relatively untouched.   
Grain  | 0.0 to 1.0  | 0.0  | Adds a subtle, random texture to the image, making it appear less sharp and more like a physical print.   
  
Notes: 

  1. ↑ Additional setting using Effect Filter other than None.



  * [](/wiki/File:Photo_Mode_4b.png "Effect settings UI")

Effect settings UI




### Pioneer

If you decouple the camera you will see a setting tab for Pioneer on the right.[15]

#### Pose

The following pioneer settings are available: 

Setting  | Options  | Default  | Effects   
---|---|---|---  
Pose  | 0 to 30  | 0  | Changes the pose of the Pioneer to one of 30 static _(non-animated)_ poses.  
See also pioneer poses below.   
Hide Pioneer  | Off, On  | Off  | Removes the pioneer from the screenshot.   
Look Into Camera  | Off, On  | Off  | Moves the pioneer helmet so pioneer is looking at camera. As long as this setting is ON, the pioneers head will continue to look at the camera in a limited horizontal and vertical arc, but won't turn 180° _(there is a limit)._  
  
#### Positioning

The following additional pioneer settings are available: 

Setting  | Options  | Default  | Effects   
---|---|---|---  
Rotation  | -180 to 180  | 0  | Rotates pioneer along Z-axes (center) in degrees.   
Nudge X  | -30 to 30  | 0  | Moves pioneer along X-axes (left / right) in centimeters.  
_100 = 1 Meter._  
Nudge Y  | -30 to 30  | 0  | Moves pioneer along Y-axes (forward / back) in centimeters.  
_100 = 1 Meter._  
  
## Color filters

There are 15 color filters available: 

  * **2007** boosts saturation and contrast, making colors and shadows appear more pronounced.
  * **Cheese Times** creates a soft-glow, cinematic effect by reducing contrast between highlights and shadows.
  * **End of Times** creates a stylized, slightly eerie, and desaturated effect.
  * **Good Ol' Days** aims to evoke a sense of nostalgia and creates a warm, soft look by adding a subtle pinkish tone to photos.
  * **LCD** allows only specific colors to be used, while blocking others.
  * **Lonely** creates a melancholic or nostalgic aesthetic, by reducing the intensity of colors, making the photo appear softer and less vibrant.
  * **Metro** used to increase saturation and contrast.
  * **Negative** reverses both the colors and the brightness of an image, effectively creating a "negative" version of the original.
  * **Orange and Purple** adds a specific tint to the highlights or shadows of your photo, creating a distinct visual effect.
  * **Sepia** adds a warm, brownish tone to your photos, giving them a vintage or nostalgic feel.
  * **Somebody's Sky** alters the color palette of a photo, making it appear dreamlike or romantic.
  * **Sunset** replicate the warm, vibrant tones associated with sunsets, potentially by enhancing colors, particularly oranges, reds, and yellows, while also subtly adjusting shadows and highlights.
  * **The Ring** sets focus to center of photo with outer ring being more blurry.
  * **Vibrant** enhances colors by increasing saturation, particularly in muted areas, while protecting highlights and shadows.
  * **Vice** creates a muted, desaturated effect, often with a slightly cool or dark undertone.


  * [](/wiki/File:Photo_Filter_2007.png "2007 color filter")

2007 color filter

  * [](/wiki/File:Photo_Filter_Cheese_Times.png "Cheese Times color filter")

Cheese Times color filter

  * [](/wiki/File:Photo_Filter_End_of_Times.png "End of Times color filter")

End of Times color filter

  * [](/wiki/File:Photo_Filter_Good_Ol%27_Days.png "Good Ol' Days color filter")

Good Ol' Days color filter

  * [](/wiki/File:Photo_Filter_Lonely.png "Lonely color filter")

Lonely color filter

  * [](/wiki/File:Photo_Filter_Metro.png "Metro color filter")

Metro color filter

  * [](/wiki/File:Photo_Filter_Negative.png "Negative color filter")

Negative color filter

  * [](/wiki/File:Photo_Filter_Sepia.png "Sepia color filter")

Sepia color filter

  * [](/wiki/File:Photo_Filter_Somebody%27s_Sky.png "Somebody's Sky color filter")

Somebody's Sky color filter

  * [](/wiki/File:Photo_Filter_Sunset.png "Sunset color filter")

Sunset color filter

  * [](/wiki/File:Photo_Filter_The_Ring.png "The Ring color filter")

The Ring color filter

  * [](/wiki/File:Photo_Filter_Vibrant.png "Vibrant color filter")

Vibrant color filter

  * [](/wiki/File:Photo_Filter_Combo_1.png "End of Times combined with Pixel Posterized color filter")

End of Times combined with Pixel Posterized color filter

  * [](/wiki/File:Photo_Filter_Combo_2.png "Vice combined with Poster color filter")

Vice combined with Poster color filter

  * [](/wiki/File:Photo_Filter_Combo_3.png "Orange and Purple combined with Poster color filter")

Orange and Purple combined with Poster color filter




## Effect filters

There are 9 photo effects available: 

  * **Comic** modifies an image to look like a hand-drawn comic book panel.
  * **Crosshatch** simulates a pencil sketch or drawing by creating an effect of dense, intersecting lines, mimicking the appearance of hand-drawn cross-hatching.
  * **Fresnel** two tone effect based on the angle between camera and surface direction. Surfaces that are perpendicular to the camera are black, parallel surfaces are white.
  * **Kuwahara** creates a painterly or stylized effect by smoothing the image while preserving edges.
  * **Noire** creates a high-contrast, black and white look, reminiscent of old Hollywood film noir.
  * **Pixel** create the appearance of an image being composed of large, noticeable blocks of color instead of smooth gradients.
  * **Pixel Posterized** combines both Pixel and Posterized effects.
  * **Poster** and **Posterized** both reduces the number of colors in an image, and applies a dark to light orange gradient to the image based on the distance from the camera to replicate the Satisfactory promotional material.
  * **VHS** mimics the visual characteristics of old VHS tapes, including a grainy texture, slight distortion, and color shifts, creating a retro aesthetic.


  * [](/wiki/File:Photo_Effect_Comic.png "Comic photo effect")

Comic photo effect

  * [](/wiki/File:Photo_Effect_Fresnel.png "Fresnel photo effect")

Fresnel photo effect

  * [](/wiki/File:Photo_Effect_Kuwahara.png "Kuwahara photo effect")

Kuwahara photo effect

  * [](/wiki/File:Photo_Effect_Noire.png "Noire photo effect")

Noire photo effect

  * [](/wiki/File:Photo_Effect_Pixel.png "Pixel photo effect")

Pixel photo effect

  * [](/wiki/File:Photo_Effect_Pixel_Posterized.png "Pixel Posterized photo effect that combines both Pixel and Posterized photo effects")

Pixel Posterized photo effect that combines both Pixel and Posterized photo effects

  * [](/wiki/File:Photo_Effect_Poster.png "Poster photo effect")

Poster photo effect

  * [](/wiki/File:Photo_Effect_Posterized.png "Posterized photo effect")

Posterized photo effect

  * [](/wiki/File:Photo_Effect_VHS.png "VHS photo effect")

VHS photo effect




## Pioneer poses

The pioneer can be both positioned and placed in one of the following 30 static _(non-animated)_ poses as desired. 

NOTE: The individual pioneer poses are not named, they are sorted here by appearance. 

### Default

There is only one pose in this group, that being Pose 0, which is the pioneer's default pose. 

Pose  | Example  | Description   
---|---|---  
0  | 

  * [](/wiki/File:Pioneer_Pose_0.png)

| Default   
  
### Emotes

The following pioneer poses duplicate some of the [Emotes](/wiki/Pioneer#Emote "Pioneer") in the game: 

Pose  | Example  | Description   
---|---|---  
1  | 

  * [](/wiki/File:Pioneer_Pose_1.png)

| Wave   
2  | 

  * [](/wiki/File:Pioneer_Pose_2.png)

| Point   
3  | 

  * [](/wiki/File:Pioneer_Pose_3.png)

| Finger Guns   
30  | 

  * [](/wiki/File:Pioneer_Pose_30.png)

| Heart   
  
### Action

The following pioneer poses show a specific action: 

#### Standing

Pose  | Example  | Description   
---|---|---  
4  | 

  * [](/wiki/File:Pioneer_Pose_4.png)

| Look   
6  | 

  * [](/wiki/File:Pioneer_Pose_6.png)

| Finger Snaps   
7  | 

  * [](/wiki/File:Pioneer_Pose_7.png)

| Pride   
9  | 

  * [](/wiki/File:Pioneer_Pose_9.png)

| Strength   
11  | 

  * [](/wiki/File:Pioneer_Pose_11.png)

| Question   
12  | 

  * [](/wiki/File:Pioneer_Pose_12.png)

| Slap   
13  | 

  * [](/wiki/File:Pioneer_Pose_13.png)

| Yes! or Success!   
17  | 

  * [](/wiki/File:Pioneer_Pose_17.png)

| Relaxed   
19  | 

  * [](/wiki/File:Pioneer_Pose_19.png)

| Thumbs Up   
20  | 

  * [](/wiki/File:Pioneer_Pose_20.png)

| Thumbs Down   
21  | 

  * [](/wiki/File:Pioneer_Pose_21.png)

| Point or Hey You!   
22  | 

  * [](/wiki/File:Pioneer_Pose_22.png)

| Stop or Fight   
24  | 

  * [](/wiki/File:Pioneer_Pose_24.png)

| Time   
26  | 

  * [](/wiki/File:Pioneer_Pose_26.png)

| No! or OMG!   
28  | 

  * [](/wiki/File:Pioneer_Pose_28.png)

| Balance or Sneak   
  
#### Seated

Pose  | Example  | Description   
---|---|---  
8  | 

  * [](/wiki/File:Pioneer_Pose_8.png)

| Seated 1   
23  | 

  * [](/wiki/File:Pioneer_Pose_23.png)

| Seated 2   
27  | 

  * [](/wiki/File:Pioneer_Pose_27.png)

| Seated 3   
  
#### Sleep, kneel, pray

Pose  | Example  | Description   
---|---|---  
15  | 

  * [](/wiki/File:Pioneer_Pose_15.png)

| Sleeping   
18  | 

  * [](/wiki/File:Pioneer_Pose_18.png)

| Kneel   
25  | 

  * [](/wiki/File:Pioneer_Pose_25.png)

| Pray   
  
#### Dance

The following pioneer poses show an action similar to a dance move: 

Pose  | Example  | Description   
---|---|---  
5  | 

  * [](/wiki/File:Pioneer_Pose_5.png)

| Dance 1   
10  | 

  * [](/wiki/File:Pioneer_Pose_10.png)

| Dance 2   
14  | 

  * [](/wiki/File:Pioneer_Pose_14.png)

| Dance 3   
16  | 

  * [](/wiki/File:Pioneer_Pose_16.png)

| Dance 4   
29  | 

  * [](/wiki/File:Pioneer_Pose_29.png)

| Dance 5   
  
## Dolly

Dolly refers to a method that allows for smooth and controlled camera movements during filming, creating a "dolly shot". 

### Settings

A button to open dolly settings displays upon decoupling the camera.[16]

The following dolly settings are available: 

Setting  | Options  | Default  | Effects   
---|---|---|---  
Dolly Settings UI  | Show Dolly Settings, Hide Dolly Settings (Button)  | Show Dolly Settings  | Opens or closes the Dolly Settings UI that appears above the lower Photo Mode UI.   
Start Point  | Set Start Point (Button)  | Set Start Point  | Sets the starting camera position.   
End Point  | Set End Point (Button)  | Set End Point  | Sets the ending camera position.[note 1]  
Shot Start‡ | |◀ (Button)  | |◀ | Moves dolly shot to start point.   
Shot Play, Shot Stop‡ | ▶, ■ (Buttons)  | ▶  | Starts and stops play of the dolly shot.   
Shot End‡ | ▶| (Button)  | ▶| | Moves dolly shot to end point.   
Duration‡ | 2.0 to 40.0  | 5.0  | Amount of time in seconds for camera to move between start point and end point. The longer the time the _slower_ the motion.   
Lock on to Tracking Point‡ | Off, On  | Off  | Enables camera to point to a single point during a dolly shot.   
Set Tracking Point‡ | Set (Button)  | Set  | Sets where camera should point to based on what camera is looking at when set.   
Blend Camera Settings‡ | Off, On  | Off  | Allows you to animate focal distance, zoom, roll and aperture.   
Interpolation‡ | Linear, Ease In, Ease Out, Ease In / Ease Out, Expo In Out  | Linear  | Sets the type of interpolation to use during the dolly shot.   
  
Notes: 

  1. ↑ Additional dolly setting marked with ‡ appear **after** setting an end point.



  * [](/wiki/File:Photo_Dolly_0.png "Dolly settings UI")

Dolly settings UI

  * [](/wiki/File:Photo_Dolly_1.png "Dolly settings UI after setting an end point")

Dolly settings UI after setting an end point

  * [](/wiki/File:Photo_Dolly_2.png "Dolly shot using the End of Times color correction and Comic Effect filter")

Dolly shot using the End of Times color correction and Comic Effect filter

  * [](/wiki/File:Photo_Dolly_3.png "Dolly shot using the End of Times color correction and Fresnel Effect filter")

Dolly shot using the End of Times color correction and Fresnel Effect filter

  * [](/wiki/File:Photo_Dolly_4.png "Dolly shot using the End of Times color correction and Crosshatch Effect filter")

Dolly shot using the End of Times color correction and Crosshatch Effect filter




### Usage

To access dolly settings, the camera must first be decoupled in the **Camera** tab, followed by clicking the **Show Dolly Settings** button.[16]

#### Setting start point and end point

Dolly settings allows players to create a camera movement between a start point and end point.[17]

Once you have initially set the camera, you can **set start point** of the dolly shot, then move the camera however you wish to final location, and then **set end point**. 

You are able to independently adjust the start point and end point by stopping the dolly shot, moving to either the start point or end point, adjusting camera as desired, and then setting the start point or end point again. 

NOTE: The final dolly shot won't play all your camera movements made between setting start point and end point, but will show any horizontal, vertical, and rotational camera movements as determined by the location and direction of camera at start point as compared with camera at end point. 

#### Tracking point

If **Lock on Tracking Point** is turned on, and a tracking point set, during the dolly shot the camera will always point to the tracking point as it moves from the starting point to the ending point in the dolly shot. 

#### Blend camera settings

Using blend camera settings when making a dolly shot allows you to interpolate between different lens settings IF they are different between start and end point, creating various visual effects and transitions. Using blend camera setting function will also lock the sliders when the dolly plays. 

#### Interpolation

The dolly shot will make use of temporal Interpolation, also known as keyframe interpolation, which is the process of automatically filling in the values between keyframes in animation software, creating smooth transitions between the specified points.[18]

Dolly shot interpolations animations uses types of interpolation in animation with its own characteristic speed profile. Exponential easing functions, often referred to as "Expo" in animation contexts, are a type of easing function that utilizes exponential growth or decay to create specific animation effects. 

The types and description of the various interpolation dolly settings available are the following: 

  * **Linear** results in a constant motion from starting point to ending point with no change in speed.
  * **Ease In** results in a slow start with motion increasing in speed over time.
  * **Ease Out** results in a fast start with motion decreasing in speed over time.
  * **Ease In** / **Ease out** results in a fast start with motion decreasing in speed after reaching mid way point.
  * **Expo In** results in a slow start with motion very quickly increasing in speed over time.
  * **Expo Out** results in a fast start with motion very quickly decreasing in speed over time.
  * **Expo In Out** results in a slow start with motion very quickly increasing in speed and then very quickly decreasing in speed after reaching mid way point.



The speed of each type of interpolation can be adjusted by changing the **Duration** setting. 

### Recording

Before recording a dolly shot, the Photo Mode UI should be hidden by pressing [`T`](/wiki/Controls "Controls"). 

The use of an external video capture software like OBS, AMD Radeon ReLive, Nvidia ShadowPlay etc. is required if you wish to record any played dolly shot. 

## Vehicles

Photo Mode does not currently support vehicles. Pressing [`T`](/wiki/Controls "Controls") while riding a vehicle hides the UI, which can be used to take screenshots. 

## History

  * [Patch 1.1.0.4](/wiki/Patch_1.1.0.4 "Patch 1.1.0.4"): Fixed a bug where [Compass Icons](/wiki/HUD#Compass "HUD") would turn grey after using Decoupled Camera
  * [Patch 1.1.0.3](/wiki/Patch_1.1.0.3 "Patch 1.1.0.3")
    * Fixed Photo Mode Poses and Pioneer Positioning Nudge affecting [Vehicles](/wiki/Vehicles "Vehicles") and [Hypertubes](/wiki/Hypertube "Hypertube")
    * Fixed Photo mode reset button not properly resetting Nudge and Rotation in some scenarios
    * Improved UX by greying out options based on context
    * Moved Saturation, Contrast and Tint to affect the final image instead of being in the middle of the colour correction stack to provide a more intuitive and predictable experience
    * Reworked Tinting function to allow it to go through the whole colour spectrum
    * Added Tint Intensity Slider
    * Increased Decouple Max Range
    * Increased minimum possible value for Dolly Duration to prevent the camera from moving too fast
    * Increased maximum Dolly duration to 40 seconds (Previously 20 seconds)
  * [Patch 1.1.0.2](/wiki/Patch_1.1.0.2 "Patch 1.1.0.2")
    * Added a new option to Hide HUD while inside of all Vehicles by pressing [`T`](/wiki/Controls "Controls") on keyboard _(useful when taking screenshots)'_
    * Fixed issues where mouse clicks in Photo Mode would trigger equipment in hand
    * Potential fix for issues with the vertical movement for the Decoupled Camera in Photo Mode
    * Fixed Photo mode reset button not properly resetting Nudge and Rotation in some scenarios
    * Fixed issue where while in Dolly Mode and having Blend Camera ON the Zoom would move in steps instead of smoothly
    * Fixed Photo Mode Poses and Pioneer Positioning Nudge affecting [Vehicles](/wiki/Vehicles "Vehicles") and [Hypertubes](/wiki/Hypertube "Hypertube")
    * Fixed incorrect player name tag in [Multiplayer](/wiki/Multiplayer "Multiplayer") when entering Decoupled Camera
    * Fixed bug where hostile [Creatures](/wiki/Creatures "Creatures") would lose hostility when using Photo Mode and entering the Decoupled Camera
    * Improved UX by greying out options based on context
    * Moved Saturation, Contrast and Tint to affect the final image instead of being in the middle of the colour correction stack to provide a more intuitive and predictable experience
    * Reworked Tinting function to allow it to go through the whole colour spectrum
    * Added Tint Intensity Slider
    * Increased Decouple Max Range
    * Increased minimum possible value for Dolly Duration to prevent the camera from moving too fast
    * Increased maximum Dolly duration to 40 seconds (Previously 20 seconds)
  * [Patch 1.1.0.0](/wiki/Patch_1.1.0.0 "Patch 1.1.0.0")
    * Photo Mode got a major overhaul with brand new UI and Settings 
      * Added a new grid type and several crop settings for various aspect ratios
      * Added a multitude of new filters, effects, pioneer poses, frames, colour adjustments, camera lens controls
      * Added ability to decouple the camera to move it around within a range of the pioneer
      * Added toggle visibility options for the Pioneer
      * Added option to have the Pioneer’s helmet follow the camera around within a 180 degree arc
      * Added a dolly mode so you can create small transitions and videos or anything your creativity allows
  * [Patch 1.0.0.1](/wiki/Patch_1.0.0.1 "Patch 1.0.0.1"): Removed the remaining functionality to take high-res screenshots while using Photo Mode since it was previously broken and causing crashes
  * [Patch Closed Alpha 4](/wiki/Patch_Closed_Alpha_4 "Patch Closed Alpha 4"): Introduced



## References

  1. ↑ [YouTube - Satisfactory's NEW Photo Mode Guide - Basics](https://www.youtube.com/watch?v=NSSIKurDcWw&t=44s)
  2. ↑ [YouTube - March 18th, 2025 Livestream - Q&A: Can we pause the game in Photo Mode?](https://www.youtube.com/watch?v=Hl90Nq3gQsQ&t=1400s)
  3. ↑ [YouTube - Satisfactory's NEW Photo Mode Guide - Enable Decoupled Camera](https://www.youtube.com/watch?v=NSSIKurDcWw&t=57s)
  4. ↑ [YouTube - Satisfactory's NEW Photo Mode Guide - Enable Decoupled Camera - Distance](https://www.youtube.com/watch?v=NSSIKurDcWw&t=83s)
  5. ↑ [Discord - Decoupled Camera Maximum Distance Possible](https://discord.com/channels/370472939054956546/464495516433121281/1412030831463239773)
  6. ↑ [YouTube - Satisfactory's NEW Photo Mode Guide - Settings](https://www.youtube.com/watch?v=NSSIKurDcWw&t=107s)
  7. ↑ [Discord - Photo Mode Wiki Page Developer Recommended Changes](https://discord.com/channels/370472939054956546/464495516433121281/1412444505914736641)
  8. ↑ [YouTube - How to find save game files on Steam Deck (2025)](https://www.youtube.com/watch?v=zqYgPf4u2yc)
  9. ↑ [YouTube - Satisfactory's NEW Photo Mode Guide - Settings - Aperture](https://www.youtube.com/watch?v=NSSIKurDcWw&t=137s)
  10. ↑ [YouTube - Satisfactory's NEW Photo Mode Guide - Settings - Focus Mode](https://www.youtube.com/watch?v=NSSIKurDcWw&t=268s)
  11. ↑ [YouTube - Satisfactory's NEW Photo Mode Guide - Settings - Crop](https://www.youtube.com/watch?v=NSSIKurDcWw&t=361s)
  12. ↑ [YouTube - What's in 1.1? - Photo Mode - Color Filters](https://www.youtube.com/watch?v=Ty7GdZvCETo&t=222s)
  13. ↑ [YouTube - Satisfactory's NEW Photo Mode Guide - Settings - Image - Color Correction](https://www.youtube.com/watch?v=NSSIKurDcWw&t=380s)
  14. ↑ [YouTube - Satisfactory's NEW Photo Mode Guide - Settings - Image - Effect Settings](https://www.youtube.com/watch?v=NSSIKurDcWw&t=564s)
  15. ↑ [YouTube - Satisfactory's NEW Photo Mode Guide - Settings - Pioneer](https://www.youtube.com/watch?v=NSSIKurDcWw&t=754s)
  16. ↑ 16.0 16.1 [YouTube - Satisfactory's NEW Photo Mode Guide - Dolly Settings - General](https://www.youtube.com/watch?v=NSSIKurDcWw&t=820s)
  17. ↑ [YouTube - Satisfactory's NEW Photo Mode Guide - Dolly Settings - Setting Start and End Points](https://www.youtube.com/watch?v=NSSIKurDcWw&t=862s)
  18. ↑ [YouTube - Satisfactory's NEW Photo Mode Guide - Dolly Settings - Interpolation](https://www.youtube.com/watch?v=NSSIKurDcWw&t=1082s)



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
