# Template:Duration/doc

[](/wiki/File:Template-info.svg) Documentation

[[purge](https://satisfactory.wiki.gg/wiki/Template:Duration/doc?action=purge)]

Formats a duration given in seconds. 

### Usage
    
    
    {{duration|s|format}}
    

If the second parameter is given (any non-whitespace character will do), the format will be like dd:hh:mm:ss. If the second parameter is empty, the format will be like 1d 4h 23m 2s. Seconds will be rounded to 3 digits. 

### Examples

  * `{{duration|20}}` creates 20s
  * `{{duration|140}}` creates 2m 20s
  * `{{duration|86406}}` creates 1d 6s
  * `{{duration|20|f}}` creates 20
  * `{{duration|140|f}}` creates 2:20
  * `{{duration|86406|f}}` creates 1:00:00:06
  * `{{duration|118518.515625}}` creates 1d 8h 55m 18.516s
  * `{{duration|118518.515625|f}}` creates 1:08:55:18.516
  * `{{duration|}}` _(duration is not specified)_ creates ?



This is the documentation page, it should be transcluded into the main template page. See [Template:Doc](/wiki/Template:Doc "Template:Doc") for more information.
  *[v]: View this template
  *[e]: Edit this template
  *[h]: History of this template
  *[his]: his trivia section
  *[N/A]: Not applicable
