# Template:Temporal Illusion/Sandbox/MainSub/doc

[](/wiki/File:Template-info.svg) Documentation

[[purge](https://satisfactory.wiki.gg/wiki/Template:Temporal_Illusion/Sandbox/MainSub/doc?action=purge)]

This template is primarily used to show a formatted link to a specific article subsection. It is similar to `{{[Main](/wiki/Template:Main "Template:Main")}}` and uses `{{[hatnote](/wiki/Template:Hatnote "Template:Hatnote")}}`. 

## Contents

  * 1 Usage
  * 2 Parameters
  * 3 Truncation
  * 4 Output
  * 5 Examples



## Usage

_Main article:_[ Satisfactory > Official description > On storefronts](/wiki/Satisfactory#On_storefronts "Satisfactory") _(See also:**Early game development**)_

`{{[Temporal_Illusion/Sandbox/MainSub](/wiki/Template:Temporal_Illusion/Sandbox/MainSub "Template:Temporal Illusion/Sandbox/MainSub")|Main|Format Type|Before Text|Note}}`

## Parameters

  * **Main:** This will be the direct link to an article subsection as seen in the url following _<https://satisfactory.wiki.gg/wiki/>_ , for example like `Satisfactory#On_storefronts`. 
    * 🚩 If this is blank the template returns an null / empty string.
  * **Format Type:** This will determine how the resulting link will be shown. _For Format Types 4 thru 7 see**Truncation** below._
    * _No format type or a format type other than 0 thru 7 was entered_ = Main Only.
    * 0 = Main (Part 1) + Main (Part 2)
    * 1 = Main (Part 1) + Before Text + Main (Part 2)
    * 2 = Main (Part 1) + Main (Part 2) + Note
    * 3 = Main (Part 1) + Before Text + Main (Part 2) + Note
    * 4 = Main (Part 1) + Main (Part 2 - _Truncated_)
    * 5 = Main (Part 1) + Before Text + Main (Part 2 - _Truncated_)
    * 6 = Main (Part 1) + Main (Part 2 - _Truncated_) + Note
    * 7 = Main (Part 1) + Before Text + Main (Part 2 - _Truncated_) + Note
  * **Before Text:** This is required for all Format Types with the exception of 0, 2 and 6. 
    * The direct link might lead to a sub-subsection and to provide clarity the Before Text can be used to show the parent subsection to where the direct link results in.
    * The Before Text can be _anything_ but is automatically formatted to show first character in upper case and rest in lower case.
    * The Before Text will appear after Part 1 and before Part 2 _(see**Output** below)_.
  * **Note:** This is optional. 
    * If used the entered text will be show in _italics_ and prefaced with "See also:".
    * The Note can be _anything_ , and may include wiki text formatting like '''bold text''' which appears as **bold text** , or <u>underlined text</u> which appears as _underlined text_ , or even include wiki links like [[Settings]] which appears as [Settings](/wiki/Settings "Settings").



## Truncation

Often the direct link will end with a **suffix** consisting of a single underscore and number like for example `Settings#Controller_2` which the user might not want to appear. In this case, the use of Format Types 4 thru 7 will truncate (remove) the suffix. 

## Output

If Format Types 0 thru 7 are used, the direct link will be split into two parts as determined by the position of the pound sign "#", and will be displayed as `Part 1 (Main Article) > Before Text (if used) > Part 2 (Subsection) > Note (if used)`. 

In Part 1 and Part 2 all underscores "_" are automatically changed to a single space " ". 

## Examples

The follow shows various examples for illustrative purposes: 

  
0\. `{{[Temporal_Illusion/Sandbox/MainSub](/wiki/Template:Temporal_Illusion/Sandbox/MainSub "Template:Temporal Illusion/Sandbox/MainSub")|Settings#Controller_2|0}}` results in: 

_Main article:_[ Settings > Controller 2](/wiki/Settings#Controller_2 "Settings")

    

    **Notes:** Only Main Link (split).

1\. `{{[Temporal Illusion/Sandbox/MainSub](/wiki/Template:Temporal_Illusion/Sandbox/MainSub "Template:Temporal Illusion/Sandbox/MainSub")|Settings#Controller_2|1|CONTROLS}}` results in: 

_Main article:_[ Settings > Controls > Controller 2](/wiki/Settings#Controller_2 "Settings")

    

    **Notes:** Before Text corrected, and Part 2 suffix not removed.

2\. `{{[Temporal_Illusion/Sandbox/MainSub](/wiki/Template:Temporal_Illusion/Sandbox/MainSub "Template:Temporal Illusion/Sandbox/MainSub")|Settings#Controller_2|2| |'''General > Select Controls''' settings}}` results in: 

_Main article:_[ Settings > Controller 2](/wiki/Settings#Controller_2 "Settings") _(See also:**General > Select Controls** settings)_

    

    **Notes:** No Before Text due to use of blank Before Text parameter, and Part 2 suffix not removed.

3\. `{{[Temporal Illusion/Sandbox/MainSub](/wiki/Template:Temporal_Illusion/Sandbox/MainSub "Template:Temporal Illusion/Sandbox/MainSub")|Settings#Controller_2|3|CONTROLS|<u>General > Select Controls</u>}}` results in: 

_Main article:_[ Settings > Controls > Controller 2](/wiki/Settings#Controller_2 "Settings") _(See also:_General > Select Controls_)_

    

    **Notes:** Before Text corrected, and Part 2 suffix not removed.

4\. `{{[Temporal Illusion/Sandbox/MainSub](/wiki/Template:Temporal_Illusion/Sandbox/MainSub "Template:Temporal Illusion/Sandbox/MainSub")|Settings#Controller_2|4}}` results in: 

_Main article:_[ Settings > Controller](/wiki/Settings#Controller_2 "Settings")

    

    **Notes:** Part 2 truncated.

5\. `{{[Temporal Illusion/Sandbox/MainSub](/wiki/Template:Temporal_Illusion/Sandbox/MainSub "Template:Temporal Illusion/Sandbox/MainSub")|Settings#Controller_2|5|Controls}}` results in: 

_Main article:_[ Settings > Controls > Controller](/wiki/Settings#Controller_2 "Settings")

    

    **Notes:** Before Text corrected _(but appears unchanged)_ , and Part 2 truncated.

6\. `{{[Temporal Illusion/Sandbox/MainSub](/wiki/Template:Temporal_Illusion/Sandbox/MainSub "Template:Temporal Illusion/Sandbox/MainSub")|Settings#Controller_2|6| |General > Select Controls}}` results in: 

_Main article:_[ Settings > Controller](/wiki/Settings#Controller_2 "Settings") _(See also: General > Select Controls)_

    

    **Notes:** No Before Text due to use of blank Before Text parameter, and Part 2 truncated.

7\. `{{[Temporal Illusion/Sandbox/MainSub](/wiki/Template:Temporal_Illusion/Sandbox/MainSub "Template:Temporal Illusion/Sandbox/MainSub")|Settings#Controller_2|7|controls|[[Settings#General_3|Settings > Controls > General]] and view '''Select Controls''' settings}}` results in: 

_Main article:_[ Settings > Controls > Controller](/wiki/Settings#Controller_2 "Settings") _(See also:[Settings > Controls > General](/wiki/Settings#General_3 "Settings") and view **Select Controls** settings)_

    

    **Notes:** Before Text corrected, and Part 2 truncated, plus example use in Note of wiki link and wiki text formatting.

8\. `{{[Temporal_Illusion/Sandbox/MainSub](/wiki/Template:Temporal_Illusion/Sandbox/MainSub "Template:Temporal Illusion/Sandbox/MainSub")|Settings#Controller_2}}` results in: 

_Main article:_[ Settings#Controller_2](/wiki/Settings#Controller_2 "Settings")

    

    **Notes:** No changes made to direct link due to no Format Type used.

This is the documentation page, it should be transcluded into the main template page. See [Template:Doc](/wiki/Template:Doc "Template:Doc") for more information.
  *[v]: View this template
  *[e]: Edit this template
  *[h]: History of this template
  *[his]: his trivia section
  *[N/A]: Not applicable
