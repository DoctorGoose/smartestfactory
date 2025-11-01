# Template:FP link/doc

[](/wiki/File:Template-info.svg) Documentation

[[purge](https://satisfactory.wiki.gg/wiki/Template:FP_link/doc?action=purge)]

This template is for creating the styled links used within boxes on the front page: [Satisfactory Wiki](/ "Satisfactory Wiki"). It relies heavily on CSS in [MediaWiki:Hydra.css](/wiki/MediaWiki:Hydra.css?action=edit&redlink=1 "MediaWiki:Hydra.css \(page does not exist\)") / [MediaWiki:Hydradark.css](/wiki/MediaWiki:Hydradark.css?action=edit&redlink=1 "MediaWiki:Hydradark.css \(page does not exist\)") and [MediaWiki:Mobile.css](/wiki/MediaWiki:Mobile.css "MediaWiki:Mobile.css"). 

## Contents

  * 1 Usage
    * 1.1 Internal (wiki) links
    * 1.2 External links
  * 2 Parameters
    * 2.1 Internal (wiki) links
    * 2.2 External links
    * 2.3 Style parameters
  * 3 Examples
    * 3.1 Links only
    * 3.2 With images



## Usage

Any group of `{{[FP link](/wiki/Template:FP_link "Template:FP link")}}` templates must be enclosed by an element with the class `fplinks`. 

### Internal (wiki) links
    
    
    {{FP link | destination | display text /optional
    | image = file link /optional
    | width = <normal/wide/full> /optional
    | imageonly = <true/false> /optional
    | plain = <true/false> /optional
    }}
    

### External links
    
    
    {{FP link | url = destination | display text /optional
    | image = file link /optional
    | width = <normal/wide/full> /optional
    | imageonly = <true/false> /optional
    | plain = <true/false> /optional
    }}
    

## Parameters

### Internal (wiki) links

`_destination_`
    Destination wiki page. **Required**.
`_display text_`
    Optional text to display instead of the name of the destination page.

### External links

`|url=`
    The destination URL. **Required** for external links.
`_display text_`
    Optional text to display instead of the URL. If omitted, the full URL will be displayed.

### Style parameters

`|image=`
    Optional image, to be displayed above the link.
`|width=`
    Determines the size of the link box. `normal` links take up to 25% of the width of the containing element. `wide` links take up to 33% of the containing element. `full` links take the entire width of the containing element. If omitted, defaults to `normal`.
`|imageonly=`
    When an image is specified, this determines whether to show only the image or both the image and the link. `true` will show only the image, `false` will show the link as well. If omitted, defaults to `false`.
`|plain=`
    This provides an option to remove backgrounds and borders for certain links. `true` will remove visible styles, `false` will use the default styles. If omitted, defaults to `false`.

## Examples

### Links only
    
    
    <div class="fplinks">
    {{FP link | Main Page | Normal}}
    {{FP link | Main Page | Wide | width = wide}}
    {{FP link | Main Page | Plain | plain = true}}
    
    {{FP link | Main Page | Full width | width = full}}
    </div>
    

[ Normal](/wiki/Main_Page "Main Page")

[ Wide ](/wiki/Main_Page "Main Page")

[ Plain ](/wiki/Main_Page "Main Page")

[ Full width ](/wiki/Main_Page "Main Page")

### With images
    
    
    <div class="fplinks">
    {{FP link | Main Page | With image | image = Wiki.png}}
    {{FP link | Main Page | Hidden text | image = Wiki.png | imageonly = true}}
    {{FP link | Main Page | Plain | image = Wiki.png | plain = true}}
    {{FP link | Main Page | Plain | image = Wiki.png | plain = true | imageonly = true}}
    
    {{FP link | Main Page | Wide with image | image = Wiki.png | width = wide}}
    {{FP link | Main Page | Wide hidden text | image = Wiki.png | width = wide | imageonly = true}}
    </div>
    

[](/wiki/Main_Page "Main Page")

[ With image ](/wiki/Main_Page "Main Page")

[](/wiki/Main_Page "Main Page")

[](/wiki/Main_Page "Main Page")

[ Plain ](/wiki/Main_Page "Main Page")

[](/wiki/Main_Page "Main Page")

[](/wiki/Main_Page "Main Page")

[ Wide with image ](/wiki/Main_Page "Main Page")

[](/wiki/Main_Page "Main Page")

This is the documentation page, it should be transcluded into the main template page. See [Template:Doc](/wiki/Template:Doc "Template:Doc") for more information.
  *[v]: View this template
  *[e]: Edit this template
  *[h]: History of this template
  *[his]: his trivia section
  *[N/A]: Not applicable
