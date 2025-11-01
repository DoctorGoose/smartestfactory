# Template:Doc

[File:Icon-warning-red.svg](/wiki/Special:Upload?wpDestFile=Icon-warning-red.svg "File:Icon-warning-red.svg") | Deprecated  This template is deprecated in favour of `{{[Documentation](/wiki/Template:Documentation "Template:Documentation")}}`, which doesn't rely on unbalanced templates.   
---|---  
  
[](/wiki/File:Template-info.svg) Documentation

[[purge](https://satisfactory.wiki.gg/wiki/Template:Doc?action=purge)]

To use, create a sub-page from the template called **doc** , put `{{[doc/start](/wiki/Template:Doc/start "Template:Doc/start")}}` at the start of your documentation, and `{{[doc/end](/wiki/Template:Doc/end "Template:Doc/end")}}` at the end. 

Go back to your main template page and put <noinclude>`{{doc}}`</noinclude> on a newline after the end of the template. /doc pages will automatically be added to [Category:Template documentation](/wiki/Category:Template_documentation "Category:Template documentation"). 

## Contents

  * 1 Optional parameters
    * 1.1 clear
    * 1.2 nodoc=1
    * 1.3 baddoc=1



## Optional parameters

### clear

If your main template page has floating content and you would like to stop it going over the documentation, put `{{[doc/start](/wiki/Template:Doc/start "Template:Doc/start")|clear}}` instead of `{{[doc/start](/wiki/Template:Doc/start "Template:Doc/start")}}` on your documentation page.  
This is also useful for templates not using <includeonly>, as it will put some space between the template and the documentation box. 

### nodoc=1

If a template has no documentation and you don't know how to use it, put `{{[doc/start](/wiki/Template:Doc/start "Template:Doc/start")|nodoc=1}}` (or if the template needs clear as well, `{{[doc/start](/wiki/Template:Doc/start "Template:Doc/start")|clear|nodoc=1}}`) instead of `{{[doc/start](/wiki/Template:Doc/start "Template:Doc/start")}}` on your documentation page.  
The documentation's background will become red to make it more noticeable, and the page will be added to [Category:Templates with no documentation](/wiki/Category:Templates_with_no_documentation "Category:Templates with no documentation"). 

### baddoc=1

Similar to nodoc, this is used to mark templates that **do** have documentation, but it isn't very good. This can mean it doesn't have enough examples, doesn't explain all the functions properly, or doesn't explain the point of the template properly.  
The documentation's background will become yellow to make it more noticeable, and the page will be added to [Category:Templates with bad documentation](/wiki/Category:Templates_with_bad_documentation "Category:Templates with bad documentation"). 

If both nodoc and baddoc are specified, baddoc will be ignored. 
  *[v]: View this template
  *[e]: Edit this template
  *[h]: History of this template
  *[his]: his trivia section
  *[N/A]: Not applicable
