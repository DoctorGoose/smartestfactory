# Template:Fullurl/doc

[](/wiki/File:Template-info.svg) Documentation

[[purge](https://satisfactory.wiki.gg/wiki/Template:Fullurl/doc?action=purge)]

This template can be used to output the full wiki URL e.g. (`https://help.gamepedia.com/index.php?title=`) in plaintext or within a plainlink span using the fullurl magic word. 

This template is useful for actions, for example action=edit to link to the edit box. 

## Usage

To use this template you put the name of the page you want and any actions you want to perform (anything that is after an &). 

### Examples
    
    
    {{fullurl|Blocks|action=edit}}

Will output: `//help.gamepedia.com/index.php?title=Blocks&action=edit`
    
    
    {{fullurl|Blocks|action=edit|nolink=1}}

Will output: `https://help.gamepedia.com/index.php?title=Blocks&action=edit`
    
    
    {{fullurl|Blocks|action=edit|text=Edit page}}

Will output: [Edit page](https://help.gamepedia.com/index.php?title=Blocks&action=edit)

### Notes

  * All url parameters are kept within the same parameter. (`{{fullurl|MediaWiki:Common.css|action=raw&ctype=text/css}}` instead of `{{fullurl|MediaWiki:Common.css|action=raw|ctype=text/css}}`)



This is the documentation page, it should be transcluded into the main template page. See [Template:Doc](/wiki/Template:Doc "Template:Doc") for more information.
  *[v]: View this template
  *[e]: Edit this template
  *[h]: History of this template
  *[his]: his trivia section
  *[N/A]: Not applicable
