# Template:Navbox/doc

[](/wiki/File:Template-info.svg) Documentation

[[purge](https://satisfactory.wiki.gg/wiki/Template:Navbox/doc?action=purge)]

[](/wiki/File:Lua.svg) | This template uses [Lua](https://en.wikipedia.org/wiki/Lua_\(programming_language\) "wikipedia:Lua \(programming language\)"): 

  * [Module:Navbox](/wiki/Module:Navbox "Module:Navbox")

  
---|---  
  
This template allows a navigational template to be set up relatively quickly by supplying it with one or more lists of links. Using this template is highly recommended for standardization of navigational templates, and for ease of use. 

## Contents

  * 1 Usage
  * 2 Parameter list
  * 3 Parameter descriptions
    * 3.1 Setup parameters
    * 3.2 Cells
  * 4 Layout of table
    * 4.1 Without image, above and below
    * 4.2 With image, above and below
    * 4.3 With image and without groups
  * 5 TemplateData



## Usage

Please remove the parameters that are left blank. 
    
    
    {{Navbox
    | name       = {{subst:PAGENAME}}
    | title      =
    | listclass  = hlist
    | state      = {{{state|}}}
    
    | above      =
    | image      =
    
    | group1     =
    | list1      =
    
    | group2     =
    | list2      =
    
    | group3     =
    | list3      =
    
    <!-- ... -->
    
    | below      =
    }}
    

## Parameter list

  * v
  * [e](https://satisfactory.wiki.gg/wiki/Template:Navbox/doc?action=edit)
  * [h](https://satisfactory.wiki.gg/wiki/Template:Navbox/doc?action=history)

{{{title}}}  
---  
{{{above}}}  
{{{group1}}}| {{{list1}}}| {{{image}}}  
{{{group2}}}| {{{list2}}}  
{{{list3}}} _without {{{group3}}}_  
{{{group4}}}| {{{list4}}}  
{{{below}}}  
  
The navbox uses lowercase parameter names, as shown in the box (_above_). The required _name_ and _title_ will create a one-line box if other parameters are omitted. 

Notice "group1" (etc.) is optional, as are sections named "above/below". 

The basic and most common parameters are as follows (see below for the full list): 

    `name` – the name of the template.
    `title` – text in the title bar, such as: [[Widget stuff]].
    `class` \- an optional CSS class for the entire navbox, to enable custom styling.
    `listclass` – a CSS class for the list cells, usually `hlist` for horizontal lists.
    `state` – controls when a navbox is expanded or collapsed.
    `above` – text to appear above the group/list section (could be a list of overall wikilinks).
    `image` – an optional right-side image, coded as the whole image. Typically it is purely decorative, so it should be coded as `[[File:XX.jpg|80px|link=|alt=]]`.
    `imageleft` – an optional left-side image (code the same as the "image" parameter).
    `groupn` – the left-side text before list-n (if group-n omitted, list-n starts at left of box).
    `listn` – text listing wikilinks using a [wikilist](https://en.wikipedia.org/wiki/Help:Lists "wikipedia:Help:Lists") format.
    `below` – optional text to appear below the group/list section.
    `groupnstyle` – CSS style to apply to a given group.
    `groupstyle` – CSS style to apply to all groups.

## Parameter descriptions

The following is a complete list of parameters for using `{{[Navbox](/wiki/Template:Navbox "Template:Navbox")}}`. In most cases, the only required parameters are `name`, `title`, and `list1`. 

### Setup parameters

    

_name_
    The name of the template, which is needed for the "V • T • E" ("View • Talk • Edit") links to work properly on all pages where the template is used. You can enter `{{subst:PAGENAME}}` for this value as a shortcut. The name parameter is only mandatory if a `title` is specified, and the `border` parameter is not set, and the `navbar` parameter is not used to disable the navbar.
_state_ [`autocollapse, collapsed, expanded, plain, off`]

  * Defaults to `autocollapse`. A navbox with `autocollapse` will start out collapsed if there are two or more tables on the same page that use other collapsible tables. Otherwise, the navbox will be expanded.
  * If set to `collapsed`, the navbox will always start out in a collapsed state.
  * If set to `expanded`, the navbox will always start out in an expanded state.
  * If set to `plain`, the navbox will always be expanded with no [hide] link on the right, and the title will remain centered (by using padding to offset the V • T • E links).
  * If set to `off`, the navbox will always be expanded with no [hide] link on the right, but no padding will be used to keep the title centered. This is for advanced use only; the "plain" option should suffice for most applications where the [show]/[hide] button needs to be hidden.


    To show the box when standalone (non-included) but then auto-hide contents when in an article, put "expanded" inside `<noinclude|>`...`</noinclude|>` tags. This setting will force the box visible when standalone (even when followed by other boxes), displaying "[hide]", but then it will auto-collapse the box when stacked inside an article: 

    `| state = ``<noinclude|>`expanded`</noinclude|>`
    Often times, editors will want a default initial state for a navbox, which may be overridden in an article. Here is the trick to do this: 

  * In your intermediate template, create a parameter also named "state" as a pass-through like this:



    `| state = {{{state<includeonly>|your_desired_initial_state</includeonly>}}}`

  * The `<includeonly>``|` will make the template expanded when viewing the template page by itself.



_navbar_
    If set to `plain`, the V • T • E links on the left side of the titlebar will not be displayed, and padding will be automatically used to keep the title centered. Use `off` to remove the V • T • E links, but not apply padding (this is for advanced use only; the "plain" option should suffice for most applications where a navbar is not desired). It is highly recommended that one not hide the navbar, in order to make it easier for users to edit the template, and to keep a standard style across pages.

    _See later section onusing navboxes within one another for examples and a more complete description._ If set to `child` or `subgroup`, then the navbox can be used as a borderless child that fits snugly in another navbox. The border is hidden and there is no padding on the sides of the table, so it fits into the _list_ area of its parent navbox. If set to `none`, then the border is hidden and padding is removed, and the navbox may be used as a child of another container (do not use the `none` option inside of another navbox; similarly, only use the `child`/`subgroup` option inside of another navbox). If set to anything else (default), then a regular navbox is displayed with a 1px border. An alternate way to specify the border to be a subgroup style is like this (i.e. use the first unnamed parameter instead of the named _border_ parameter):
    
    
    
    {{Navbox|child|...}}

### Cells

_title_ *
    Text that appears centered in the top row of the table. It is usually the template's topic, i.e. a succinct description of the body contents. This should be a single line, but if a second line is needed, use `{{-}}` to ensure proper centering. This parameter is technically not mandatory, but using `{{[Navbox](/wiki/Template:Navbox "Template:Navbox")}}` is rather pointless without a title.
_above_ *
    A full-width cell displayed between the titlebar and first group/list, i.e. _above_ the template's body (groups, lists and image). In a template without an image, _above_ behaves in the same way as the _list1_ parameter without the _group1_ parameter.
_group n_*
    (i.e. _group1_ , _group2_ , etc.) If specified, text appears in a header cell displayed to the left of _list n_. If omitted, _list n_ uses the full width of the table.
_list n_*
    (i.e. _list1_ , _list2_ , etc.) The body of the template, usually a list of links. Format is inline, although the text can be entered on separate lines if the entire list is enclosed within `<div> </div>`. At least one _list_ parameter is required; each additional _list_ is displayed in a separate row of the table. Each _list n_ may be preceded by a corresponding _group n_ parameter, if provided (see below).
    Entries should be separated using a newline and an asterisk (*). If instead two asterisks are used, it provides [nesting](https://en.wikipedia.org/wiki/Nesting_\(computing\) "wikipedia:Nesting \(computing\)") within the previous entry by enclosing the entry with brackets. Increasing the number of asterisks used increases the number of brackets around entries.
_imageleft_ *
    An image to be displayed in a cell below the title and to the left of the body (lists). For the image to display properly, the _list1_ parameter must be specified and no groups can be specified. It accepts the same sort of parameter that _image_ accepts.
_below_ *
    A full-width cell displayed _below_ the template's body (groups, lists and image).

## Layout of table

### Without image, above and below

Table generated by `{{[Navbox](/wiki/Template:Navbox "Template:Navbox")}}` **without** _image_ , _above_ and _below_ parameters: 

  * v
  * [e](https://satisfactory.wiki.gg/wiki/Template:Navbox/doc?action=edit)
  * [h](https://satisfactory.wiki.gg/wiki/Template:Navbox/doc?action=history)

{{{title}}}  
---  
{{{group1}}}| {{{list1}}}  
{{{group2}}}| {{{list2}}}  
{{{list3}}} _without {{{group3}}}_  
{{{group4}}}| {{{list4}}}  
  
### With image, above and below

Table generated by `{{[Navbox](/wiki/Template:Navbox "Template:Navbox")}}` **with** _image_ , _above_ and _below_ parameters: 

  * v
  * [e](https://satisfactory.wiki.gg/wiki/Template:Navbox/doc?action=edit)
  * [h](https://satisfactory.wiki.gg/wiki/Template:Navbox/doc?action=history)

{{{title}}}  
---  
{{{above}}}  
{{{group1}}}| {{{list1}}}| {{{image}}}  
{{{group2}}}| {{{list2}}}  
{{{list3}}} _without {{{group3}}}_  
{{{group4}}}| {{{list4}}}  
{{{below}}}  
  
### With image and without groups

Table generated by `{{[Navbox](/wiki/Template:Navbox "Template:Navbox")}}` **with** _image_ , _imageleft_ , _lists_ , and **without** _groups_ , _above_ , _below_ : 

  * v
  * [e](https://satisfactory.wiki.gg/wiki/Template:Navbox/doc?action=edit)
  * [h](https://satisfactory.wiki.gg/wiki/Template:Navbox/doc?action=history)

{{{title}}}  
---  
{{{imageleft}}}| {{{list1}}}| {{{image}}}  
{{{list2}}}  
{{{list3}}}  
{{{list4}}}  
  
## TemplateData

Creates a navigational box for links to other pages.

Template parameters

Parameter| Description| Type| Status  
---|---|---|---  
Name| `name`| The name of the template. Needed for "View • Talk • Edit" links to work properly.

Default
    {{subst:PAGENAME}}
| String| suggested  
Title| `title`| Text in the title bar; centered in the top row of the table. Usually the template's topic.

Example
    [[Template:Navbox]]
| Unknown| suggested  
Navbox class| `class`| CSS class for the navbox.

Example
    navbox-items
| String| optional  
Group 1| `group1`| If specified, text appears in a header cell displayed to the left of list 1. If omitted, list 1 uses the full width of the table.

| Unknown| suggested  
List 1| `list1`| Body of the template; usually a list of links. Format is inline. At least one list parameter is required; each additional list is displayed in a separate row of the table. Each listn may be preceded by a corresponding groupn parameter. Entries should be separated using a newline and an asterisk. If two asterisks are used, it provides nesting within the previous entry with brackets.

| Unknown| required  
List class| `listclass`| CSS class for the list cells, usually hlist for horizontal lists.

Example
    hlist
| String| optional  
State| `state`| Controls when a navbox is expanded or collapsed

Suggested values
    `autocollapse` `collapsed` `expanded` `plain` `off`
Default
    autocollapse
Example
    autocollapse
| Unknown| suggested  
Above| `above`| Full-width cell displayed between the titlebar and first group/list, i.e. above the template's body (groups, lists and image)

| String| suggested  
Below| `below`| Full-width cell displayed below the template's body.

| Unknown| suggested  
Image| `image`| Image to be displayed in a cell below the title and to the right of the body

Example
    [[File:XX.jpg | 80px | link= | alt= ]]
| File| suggested  
group2| `group2`| no description

| Unknown| suggested  
list2| `list2`| no description

| Unknown| suggested  
group3| `group3`| no description

| Unknown| suggested  
list3| `list3`| no description

| Unknown| suggested  
group4| `group4`| no description

| Unknown| optional  
list4| `list4`| no description

| Unknown| optional  
Image left| `imageleft`| Image to be displayed in a cell below the title and to the left of the body. For the image to display properly, list1 parameter must be specified and no groups can be specified.

Example
    [[File:XX.jpg | 80px | link= | alt= ]]
| File| optional  
Navbar status| `navbar`| no description

Example
    plain, off
| String| optional  
Border status| `border`| no description

Example
    child, subgroup, none
| String| optional  
evenodd| `evenodd`| no description

Suggested values
    `swap` `even` `odd` `off`
| Unknown| optional  
  
This is the documentation page, it should be transcluded into the main template page. See [Template:Doc](/wiki/Template:Doc "Template:Doc") for more information.
  *[v]: View this template
  *[e]: Edit this template
  *[h]: History of this template
  *[his]: his trivia section
  *[N/A]: Not applicable
