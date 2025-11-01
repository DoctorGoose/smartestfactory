# Template:IsFluid/doc

[](/wiki/File:Template-info.svg) Documentation

[[purge](https://satisfactory.wiki.gg/wiki/Template:IsFluid/doc?action=purge)]

This template can be used to check if provided page belongs to Category:Fluids 

Returns **1** if True or empty string if False 

#### Usage

{{IsFluid|Water}} → 1 

{{IsFluid|Packaged Water}} → 

{{#vardefine: ingredient | Fuel}} {{#if: {{IsFluid|{{#var: ingredient}} }} | fluid | solid}} → fluid 

This is the documentation page, it should be transcluded into the main template page. See [Template:Doc](/wiki/Template:Doc "Template:Doc") for more information.
  *[v]: View this template
  *[e]: Edit this template
  *[h]: History of this template
  *[his]: his trivia section
  *[N/A]: Not applicable
