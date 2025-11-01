# Template:Key/doc

[](/wiki/File:Template-info.svg) Documentation

[[purge](https://satisfactory.wiki.gg/wiki/Template:Key/doc?action=purge)]

When used, this template displays game controls, supporting both keyboard keys and controller buttons. 

  * Images used by this template are hosted at <https://commons.wiki.gg/>.
  * This template's display is styled using the `.keysDark` and `.keysLight` classes located in [MediaWiki:Common.css](/wiki/MediaWiki:Common.css "MediaWiki:Common.css").



## Contents

  * 1 Usage
    * 1.1 Keyboard
      * 1.1.1 Example
    * 1.2 Consoles and controllers
      * 1.2.1 Example
        * 1.2.1.1 Without Size
        * 1.2.1.2 With Size
  * 2 Changing the default color



## Usage

  * **Note:** For a summary of possible console, key, and button values, see [Template:Key/library](/wiki/Template:Key/library "Template:Key/library").



### Keyboard

If using the template for keyboard keys, there is only one required input. For mouse usage, see the #Consoles and controllers, using "mouse" as the console. 

**`{{key |_button_ }}`**

  * `button` is the keyboard key to be pressed. Some key inputs, such as Shift or Tab will automatically add symbols or other formatting. Any other inputs will be output as they are with the first letter capitalized.
  * _Optional_ : there is an additional parameter, `keyboardvariant` which determines whether the key is dark text on a light key (default) or the inverse. This will likely never be used, and if a wiki would prefer light on dark, it should be changed as the default.



#### Example
    
    
    Press {{Key|Shift}} and {{Key|F}} at the same time.

produces:  
Press [`⇧ Shift`](/wiki/Controls "Controls") and [`F`](/wiki/Controls "Controls") at the same time. 

### Consoles and controllers

**`{{key |_console_ | _button_ | size = _optional size_ }}`**

  * `console` is the console the key belongs to. The parameter is **not** case-sensitive and supports many possible consoles. See [Template:Key/library](/wiki/Template:Key/library "Template:Key/library") for possible values.
  * `button` is the button to be pressed, such as "A" or "Right Trigger". While the template tries to be intuitive such that the correct input for a button is whatever you think it is, if your attempt at a button isn't working, see [Template:Key/library](/wiki/Template:Key/library "Template:Key/library") for possible values.
  * The `size` parameter is optional, and sizes the button image. If this parameter is not entered, the default image size is 20px.



#### Example

##### Without Size
    
    
    Press {{Key|Xbox|RT}} to open your inventory wheel and select the item with {{Key|Xbox|A}}

produces:  
Press [](/wiki/File:XboxOne_RT.png "RT") to open your inventory wheel and select the item with [](/wiki/File:XboxOne_A.png "A")

##### With Size
    
    
    Press {{Key|Xbox|RT|size=48px}} to open your inventory wheel and select the item with {{Key|Xbox|A|size=48px}}

produces:  
Press [](/wiki/File:XboxOne_RT.png "RT") to open your inventory wheel and select the item with [](/wiki/File:XboxOne_A.png "A")

## Changing the default color

The default color for the keyboard and mouse is suitable for dark-skinned wikis. To change the default settings so it fits for a light-skinned wiki, without having to use `keyboardvariant = light` each time, you can search for and change these sections in the template: 

  
Search for: `|#default = _White_Mouse_`  
...and change it to: `|#default = _Black_Mouse_`

  


Search for: `<kbd class="{{#switch: {{lc:{{{keyboardvariant}}}}} |dark=keysDark|light=keysLight|

keysDark

}}">`  


...and change _keysDark_ at the end of the line to `_keysLight_`. 

This is the documentation page, it should be transcluded into the main template page. See [Template:Doc](/wiki/Template:Doc "Template:Doc") for more information.
  *[v]: View this template
  *[e]: Edit this template
  *[h]: History of this template
  *[his]: his trivia section
  *[N/A]: Not applicable
