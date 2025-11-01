# Template:Current version

  


[](/wiki/File:Template-info.svg) Documentation

[[purge](https://satisfactory.wiki.gg/wiki/Template:Current_version?action=purge)]

This template contains the version number of the most recent major update, experimental patch, and early access patch. It can be optionally linked or provide the date instead. 

## Modifying

To update the current version, edit the source of this page and in the first few lines you'll see: 

| major = 1.1.1.0  
| experimental = 1.1.1.6  
| #default = 1.1.1.4 

Major means the last major update, experimental is the latest experimental branch update, and `#default` is the last update to the early access branch. Simply change the version number on the appropriate line here. 

Below that, you'll also see: 

| major = 2025-06-10  
| experimental = 2025-10-10  
| #default = 2025-09-08 

These work the same as the version number, but store the dates instead. These are in the form of yyyy-mm-dd and should use the UTC timezone. 

## Usage

`{{Current version}}` gives the latest early access update, which is: 1.1.1.4 

`{{Current version|experimental}}` gives the latest experimental update, which is: 1.1.1.6 

`{{Current version|major}}` gives the latest major update, which is: 1.1.1.0 

Dates

`{{Current version}}` gives the date of the latest early access update: 2025-09-08 

`{{Current version|experimental}}` gives the date of the latest experimental update, which is: 2025-10-10 

`{{Current version|major}}` gives the date of the latest major update, which is: 2025-06-10 

### Linking

If a second parameter is given any value that equates to true (anything other than 0 or nothing) a link will be provided to the corresponding patch notes page. For major updates, the display text will be Update X instead of a version number. If a third parameter is given, that will be used as display text instead. 

For example:  
`{{Current version|1}}` produces: [1.1.1.4](/wiki/Patch_1.1.1.4 "Patch 1.1.1.4")  
`{{Current version|experimental|1|latest experimental version}}` produces: [latest experimental version](/wiki/Patch_1.1.1.6 "Patch 1.1.1.6")  
`{{Current version|major|1}}` produces: [Update 1.1](/wiki/Patch_1.1.1.0 "Patch 1.1.1.0")

The above documentation is transcluded from [Template:Current version/doc](/wiki/Template:Current_version/doc "Template:Current version/doc"). ([edit](https://satisfactory.wiki.gg/wiki/Template:Current_version/doc?action=edit) | [history](https://satisfactory.wiki.gg/wiki/Template:Current_version/doc?action=history))
  *[v]: View this template
  *[e]: Edit this template
  *[h]: History of this template
  *[his]: his trivia section
  *[N/A]: Not applicable
