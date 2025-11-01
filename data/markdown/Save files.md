# Save files

**Save files** are files that contain data about a given game session. They use the `.sav` file extension. 

## Contents

  * 1 Save file location
    * 1.1 Automatic backup
    * 1.2 Save editing
    * 1.3 Cloud sync
  * 2 Save file format
    * 2.1 Basic data types
      * 2.1.1 Byte
      * 2.1.2 Int
      * 2.1.3 Uint32
      * 2.1.4 Long
      * 2.1.5 Uint64
      * 2.1.6 Float
      * 2.1.7 Double
      * 2.1.8 String
    * 2.2 Composite data types
      * 2.2.1 SaveFileHeader
      * 2.2.2 CompressedSaveFileBody
      * 2.2.3 SaveFileBody
      * 2.2.4 Level-Grouping Grid
      * 2.2.5 Level
      * 2.2.6 ObjectHeader
      * 2.2.7 ActorHeader
      * 2.2.8 ComponentHeader
      * 2.2.9 LevelObject
      * 2.2.10 ActorObject
      * 2.2.11 ComponentObject
      * 2.2.12 ObjectReference
      * 2.2.13 Properties
        * 2.2.13.1 PropertyList
        * 2.2.13.2 ArrayProperty
        * 2.2.13.3 BoolProperty
        * 2.2.13.4 ByteProperty
        * 2.2.13.5 EnumProperty
        * 2.2.13.6 FloatProperty
        * 2.2.13.7 DoubleProperty
        * 2.2.13.8 IntProperty
        * 2.2.13.9 Int8Property
        * 2.2.13.10 UInt32Property
        * 2.2.13.11 Int64Property
        * 2.2.13.12 MapProperty
        * 2.2.13.13 NameProperty
        * 2.2.13.14 ObjectProperty
        * 2.2.13.15 SoftObjectProperty
        * 2.2.13.16 SetProperty
        * 2.2.13.17 StrProperty
        * 2.2.13.18 StructProperty
        * 2.2.13.19 TextProperty
      * 2.2.14 TypedData
        * 2.2.14.1 Box
        * 2.2.14.2 FluidBox
        * 2.2.14.3 InventoryItem
        * 2.2.14.4 LinearColor
        * 2.2.14.5 Quat
        * 2.2.14.6 RailroadTrackPosition
        * 2.2.14.7 Vector
        * 2.2.14.8 DateTime
        * 2.2.14.9 ClientIdentityInfo
      * 2.2.15 Trailing Bytes
    * 2.3 Libraries and implementations
  * 3 Dedicated Server settings file
  * 4 History
  * 5 References



## Save file location

Both Steam and Epic Games use the same path: 

  * Windows 
    * `%LOCALAPPDATA%\FactoryGame\Saved\SaveGames\{YOUR ID}`
    * `C:\Users\<your Windows username>\AppData\Local\FactoryGame\Saved\SaveGames\{YOUR ID}`
      * If you cannot find your Steam save folder (such as due to purchasing the game on Steam after previously owning on Epic), first start a new game with Steam, then save the new game. You should now be able to see your Steam save folder besides Epic. The Steam ID is usually shorter than the Epic ID. The folder location is stated above.
  * Linux 
    * Using Steam Play (one of these locations): 
      * `~/.local/share/Steam/steamapps/compatdata/526870/pfx/drive_c/users/steamuser/Local Settings/Application Data/FactoryGame/Saved/SaveGames/{YOUR STEAM ID}`
      * `~/.steam/steam/steamapps/compatdata/526870/pfx/drive_c/users/steamuser/Local Settings/Application Data/FactoryGame/Saved/SaveGames/{YOUR STEAM ID}`
    * Steam: `~/.var/app/com.valvesoftware.Steam/.local/share/Steam/steamapps/compatdata/526870/pfx/drive_c/users/steamuser/AppData/Local/FactoryGame/Saved/SaveGames/{YOUR STEAM ID}`
    * Steam (installation on another drive than your home dir): `{YOUR DRIVE}/SteamLibrary/steamapps/compatdata/526870/pfx/drive_c/users/steamuser/AppData/Local/FactoryGame/Saved/SaveGames/{YOUR STEAM ID}`
    * Using Steam Deck: 
      * `/home/deck/.steam/root/steamapps/compatdata/526870/pfx/dosdevices/c:/users/steamuser/AppData/Local/FactoryGame/Saved/SaveGames/{YOUR STEAM ID}`
      * **⭑ NOTE:** Steam Deck saved games are within a _hidden_ folder, and you must first **show hidden files** before you can view the folder via the Steam Deck File Explorer.[1] Files are contained in a _compacted data folder_ with name of **526870**.
  * Unraid, docker 
    * ich777/steamcmd:satisfactory: `/mnt/user/appdata/satisfactory/.config/Epic/FactoryGame/Saved/SaveGames/{YOUR ID}`



### Automatic backup

When a save file is saved by overwriting another, the game creates a backup of the previous save file. This doesn't happen when an autosave occurs, unless you manually overwrite it. 

Both Steam and Epic Games use the same path: 

  * Windows 
    * `%LOCALAPPDATA%\FactoryGame\Saved\SaveGames\SaveGames_backup`
    * `C:\Users\<your Windows username>\AppData\Local\FactoryGame\Saved\SaveGames\SaveGames_backup`
      * If you cannot find your steam save folder (probably because you have owned the game in Epic and just bought the Steam copy recently), first start a new game with Steam, then save the new game. You should now be able to see your steam save folder beside epic. The steam ID is usually shorter than the Epic ID. The folder location is stated above.
  * Linux 
    * Using Steam Play: `~/.local/share/Steam/steamapps/compatdata/526870/pfx/drive_c/users/steamuser/Local Settings/Application Data/FactoryGame/Saved/SaveGames/SaveGames_backup`
    * Steam: `~/.var/app/com.valvesoftware.Steam/.local/share/Steam/steamapps/compatdata/526870/pfx/drive_c/users/steamuser/AppData/Local/FactoryGame/Saved/SaveGames/SaveGames_backup`
    * Steam (installation on another drive than your home dir): `{YOUR DRIVE}/SteamLibrary/steamapps/compatdata/526870/pfx/drive_c/users/steamuser/AppData/Local/FactoryGame/Saved/SaveGames/SaveGames_backup`
  * Unraid, Docker 
    * ich777/steamcmd:satisfactory: `/mnt/user/appdata/satisfactory/.config/Epic/FactoryGame/Saved/SaveGames_backup`



### Save editing

Save files can be edited using [online tools](/wiki/Online_tools "Online tools"). 

### Cloud sync

[](/wiki/File:Steam_Cloud_Conflict_Dialog.png)

[](/wiki/File:Steam_Cloud_Conflict_Dialog.png "Enlarge")

Example of a sync conflict dialog on Steam

If playing on Epic Games or Steam and Cloud Sync is enabled, a notification may sometimes appear when the player: 

  * Switches the game version between experimental and stable
  * Copies over the save game across different platforms
  * Continues a game at different machine



And you will be prompted to either upload your save file to the cloud or download the save file from the cloud to your PC. 

Unless you are playing across multiple PC, always choose **upload your save file to the cloud** to avoid losing your progress. And always back up your saves! 

## Save file format

A save file has a header and a body. The body of the file is compressed in chunks. 

As of [Patch 1.0.0.3](/wiki/Patch_1.0.0.3 "Patch 1.0.0.3") (Build 368883, released on September 25, 2024), the produced save file header has version 13, the save version is 46 and the editor object version is 40. For these versions, this format description should be correct, but may not be complete: It is possible that not all potential structures were present in the analyzed save files. 

As of [Patch 1.1.1.1](/wiki/Patch_1.1.1.1 "Patch 1.1.1.1") (Build 418783, released on June 18, 2025), the produced save file header has version 14, which inserted a new string into the structure for the save name. The SaveFileHeader description below should be correct for this version, but the SaveFileBody has not been analyzed beyond [Patch 1.0.0.3](/wiki/Patch_1.0.0.3 "Patch 1.0.0.3") as described above. 

### Basic data types

There are nine basic types that are used to compose more elaborated structures in the save files: 

#### Byte

A single 8-bit byte that represents a signed integer between -128 and 127. 

#### Int

Four consecutive bytes in [little-endian order](https://en.wikipedia.org/wiki/Endianness "wikipedia:Endianness") that represent a signed integer between -2,147,483,648 and 2,147,483,647. 

#### Uint32

Four consecutive bytes in [little-endian order](https://en.wikipedia.org/wiki/Endianness "wikipedia:Endianness") that represent an unsigned integer between 0 and 4,294,967,295. 

#### Long

Eight consecutive bytes in little-endian order that represent a signed integer between -9,223,372,036,854,775,808 and 9,223,372,036,854,775,807. 

#### Uint64

Eight consecutive bytes in little-endian order that represent an unsigned integer between 0 and 18,446,744,073,709,551,615. 

#### Float

Four consecutive bytes in little-endian order that represent a signed floating-point number with single precision, according to the [binary32 format of IEEE 754](https://en.wikipedia.org/wiki/Single-precision_floating-point_format#IEEE_754_standard:_binary32 "wikipedia:Single-precision floating-point format"). 

#### Double

Eight consecutive bytes in little-endian order that represent a signed floating-point number with double precision, according to the [binary64 format of IEEE 754](https://en.wikipedia.org/wiki/Double-precision_floating-point_format "wikipedia:Double-precision floating-point format"). 

#### String

A variable-length byte sequence of UTF-encoded characters, null-terminated: 

number of bytes  | description  | example  | notes   
---|---|---|---  
4  | string length in characters, including null-termination bytes  | 22  | as an Int, see above   
variable  | the encoded characters  | "Hello [Massage-2(A-B)b](/wiki/World "World")"  | without the quotation marks   
1 or 2  | null-termination  | N/A  | one byte if UTF-8, two bytes if UTF-16   
  
A length of zero represents the empty string and occupies just these four bytes. A positive length means that the characters are encoded in UTF-8. A negative length means that the characters are encoded in UTF-16 little-endian, without a byte-order mark. In this case, the given negative length has to be multiplied by minus two to get the number of bytes the rest of the string occupies (including the two bytes for null-termination). 

### Composite data types

Using the basic data types defined above, a save file has two top-level structures: a SaveFileHeader and a SaveFileBody. These are composed of different intermediate data types themselves. 

These composite data types are documented below. A data type is a list of ordered fields, each field is a row in the table of the data type. So, for example: The SaveFileHeader begins with an Int (four bytes) that represents the save header version. This is followed by another Int (the next four bytes) that represents the save version and so on. 

#### SaveFileHeader

basic data type  | description  | example  | notes   
---|---|---|---  
Uint32  | save header version  | 14  | for a version list see the header FGSaveManagerInterface.h in the [Community resources](/wiki/Community_resources "Community resources")  
Uint32  | save version  | 52  | for a version list see the header SaveCustomVersion.h in the [Community resources](/wiki/Community_resources "Community resources")  
Uint32  | build version  | 418,783  | this is [Patch 1.1.1.1](/wiki/Patch_1.1.1.1 "Patch 1.1.1.1")  
String  | save name  | "only one way to find out_autosave_0"  | the original name of the save file without the extension (only used by consoles)   
String  | map name  | "Persistent_Level"  |   
String  | map options  | "?startloc=Rocky Desert?sessionName=only one way to find out?Visibility=SV_Private"  |   
String  | session name  | "[only one way to find out](https://www.youtube.com/playlist?list=PLrBjj4brdIRwRkGTLKqH5hlS_mlMYn_J0)"  |   
Uint32  | played seconds  | 941,514  |   
Uint64  | save timestamp as [Ticks](https://docs.microsoft.com/en-us/dotnet/api/system.datetime.ticks) | 637,894,867,432,920,000  | this is 2022-05-30 05:52:23 UTC   
Byte  | flags  | 0  | 

  * bit 0 - visibility (this is "private" visibility, 1 would be "friends only")
  * bit 1 - always 0


  * bit 2 - always 0


  * bit 3 - unknown
  * bit 4 - unknown
  * bit 5 - unknown
  * bit 6 - unknown
  * bit 7 - unknown

  
Uint32  | editor object version  | 40  | depends on the [unreal engine](https://docs.unrealengine.com/4.26/en-US/ProgrammingAndScripting/ProgrammingWithCPP/UnrealArchitecture/VersioningAssetsAndPackages/) version used   
String  | mod metadata  | ""  | empty if no mods where used   
Uint32  | mod flags  | 0  | zero if no mods where used   
String  | save identifier  | _tYytyulUk6z2Ah42xvScg  | a unique identifier ([GUID](https://en.wikipedia.org/wiki/Universally_unique_identifier "wikipedia:Universally unique identifier")) for this save, for analytics purposes   
Uint32  | is partitioned world  | 1  | always 1   
Uint32  | creative mode enabled  | 1  | always 1 (unrelated to [Advanced Game Settings](/wiki/Advanced_Game_Settings "Advanced Game Settings"))   
N/A  | 16-byte checksum  |  | an MD5 hash of all data after the header (save game editors should leave this property unmodified)   
Uint32  | cheat flag  | 0  | 0 or 1   
  
#### CompressedSaveFileBody

Directly after the save file header, the save file body begins with a list of [zlib-compressed](https://en.wikipedia.org/wiki/Zlib "wikipedia:Zlib") chunks. Each compressed chunk has this format: 

basic data type  | description  | example  | notes   
---|---|---|---  
Uint32  | unreal engine package signature  | 2,653,586,369  | always the [magic number](https://en.wikipedia.org/wiki/List_of_file_signatures "wikipedia:List of file signatures") "9E2A83C1" in hex (not really an Int as defined above, more like a four byte unsigned integer)   
Uint32  |  | 0x22222222  | always 0x22222222   
Uint32  | maximum chunk size  | 131,072  | in number of bytes, always 128 * 1,024   
Byte  |  | 0  | always 0   
Uint32  |  | 0x03000000  | always 0x03000000   
Uint64  | compressed size  | 3,814  | in number of bytes   
Uint64  | uncompressed size  | 131,072  | in number of bytes   
Uint64  | compressed size  | 3,814  | this is a repeat of the above data   
Uint64  | uncompressed size  | 131,072  | this is a repeat of the above data   
N/A  | compressed bytes of the chunk  | N/A  | number of bytes: see "compressed size" above   
  
#### SaveFileBody

The save file body is the concatenation of the uncompressed chunks. The body mainly consists of a list of [sublevels and the persistent level](https://docs.unrealengine.com/4.26/en-US/Basics/Levels/LevelsWindow/). 

data type  | description  | example  | notes   
---|---|---|---  
Uint64  | uncompressed size  | 90,103,391  | in number of bytes, for the whole body except this size field itself   
Uint32  |  | 6  | always 6   
String  |  | "None"  | always "None"   
Uint32  |  | 0  | always 0   
Uint32  |  |  |   
Uint32  |  | 1  | always 1   
String  |  | "None"  | always "None"   
Uint32  |  |  |   
N/A  | 5 level-grouping grids  | N/A  |   
Uint32  | sublevel count  | 107  | the number of sublevels that follow - does not include the persistent level   
N/A  | levels  | N/A  | sublevels and the persistent level. There is one more level than the sublevel count above, the last entry being the persistent level. For the format of one Level, see below   
Uint32  | reference list count  | 6  | the number of object references to follow   
N/A  | reference list  |  | a list of object references of type ObjectReference. Seems to always be references to Mercer Sphere instances.   
  
#### Level-Grouping Grid

Five groups of level lists. 

basic data type  | description  | example  | notes   
---|---|---|---  
String  | grid name  | "MainGrid"  | "MainGrid", "LandscapeGrid", "ExplorationGrid", "FoliageGrid", "HLOD0_256m_1023m"   
Uint32  |  |  |   
Uint32  |  |  |   
Uint32  | level count  |  | the number of string/integer pairs   
N/A  | level info  | N/A  | a String and a Uint32 per level   
  
#### Level

Each level has a list of game objects (actors and components), preceded by a list of headers for these objects. 

basic data type  | description  | example  | notes   
---|---|---|---  
String  | sublevel name  | "Level /Game/FactoryGame/Map/GameLevel01/Cave_X3_Y4_DesertCanyon_1_01.Cave_X3_Y4_DesertCanyon_1_01:PersistentLevel"  | the name of the sublevel; if this is the persistent level, the field is absent   
Uint64  | object header and collectables size  | 21,499,825  | in number of bytes, including the count Uint32s   
Uint32  | object header count  | 86,644  | the number of headers that follow   
N/A  | object headers  | N/A  | for the format of one ObjectHeader, see below   
Uint32  | extra level names count  | 1  | the number of strings that follow; present only if this is the persistent level   
String  | extra level names  | "Persistent_Level"  | present only if this is the persistent level   
Uint32  | collectables count  | 223  | the number of collectable objects that follow (e.g. [Power Slugs](/wiki/Power_Slug "Power Slug"))   
N/A  | collectables  | N/A  | a list of object references, for the format of one such ObjectReference, see below   
Uint64  | objects size  | 92,259  | in number of bytes, for all game objects in that level (actors and components), including the count Uint32   
Uint32  | object count  | 504  | should be the same as the number of object headers above   
N/A  | objects  | N/A  | the additional data for each of the object headers above. for the format of each entry, see LevelObject below   
Uint32  | save version  | 52  | similar to the save version in SaveFileHeader; if this is the persistent level, the field is absent   
Uint32  | second extra level names count  | 1  | the number of strings that follow; present only if this is the persistent level   
String  | second extra level names  | "Persistent_Level"  | present only if this is the persistent level   
Uint32  | second collectables count  | 223  | the number of collectables in the second list that follows. can be igonred, since the collectables should be exactly the same as above   
N/A  | second collectables  | N/A  | a list of object references, for the format of one such ObjectReference, see below. can also be ignored   
  
#### ObjectHeader

basic data type  | description  | example  | notes   
---|---|---|---  
Uint32  | header type  | 1  | this is a header for an actor object, 0 would be a component header   
N/A  | the bytes of the header  | N/A  | either an ActorHeader or a ComponentHeader, see below   
  
#### ActorHeader

basic data type  | description  | example  | notes   
---|---|---|---  
String  | type path  | "/Game/FactoryGame/Buildable/Factory/ConstructorMk1/Build_ConstructorMk1.Build_ConstructorMk1_C"  | the type of actor, described in a hierarchical path   
String  | root object  | "Persistent_Level"  |   
String  | instance name  | "Persistent_Level:PersistentLevel.Build_ConstructorMk1_C_2147169479"  | the name of this single actor object   
Uint32  | unknown  | 2621448  |   
Float  | rotation x  | -0.0  |   
Float  | rotation y  | 0.0  |   
Float  | rotation z  | -0.99999994  |   
Float  | rotation w  | 3.5762787E-7  |   
Float  | position x  | -165,200.0  |   
Float  | position y  | -33,599.996  |   
Float  | position z  | -450.0  |   
Float  | scale x  | 1.0  |   
Float  | scale y  | 1.0  |   
Float  | scale z  | 1.0  |   
Uint32  | need transform?  | 1  | seems to be more like a boolean flag, semantics unclear   
Uint32  | was placed in level?  | 0  | seems to be more like a boolean flag, semantics unclear   
  
#### ComponentHeader

basic data type  | description  | example  | notes   
---|---|---|---  
String  | type path  | "/Script/FactoryGame.FGPowerCircuit"  | the type of component, described in a hierarchical path   
String  | root object  | "Persistent_Level"  |   
String  | instance name  | "Persistent_Level:PersistentLevel.CircuitSubsystem.FGPowerCircuit_2147177256"  | the name of this single component object   
Uint32  | unknown  | 0x002C0008  |   
String  | parent actor name  | "Persistent_Level:PersistentLevel.CircuitSubsystem"  | a reference to the instance name of an actor   
  
#### LevelObject

basic data type  | description  | example  | notes   
---|---|---|---  
Uint32  | save version  | 46  | similar to the save version in SaveFileHeader, but can contain older values for saves played during older game releases   
Uint32  | flag  | 0  | 0 or 1   
N/A  | the bytes of the object  | N/A  | either an ActorObject or ComponentObject, depending on the corresponding header type the object belongs to   
  
#### ActorObject

basic data type  | description  | example  | notes   
---|---|---|---  
Uint32  | size  | 2,333  | the number of bytes this ActorObject has, including trailing bytes   
N/A  | parent object reference  | N/A  | ObjectReference   
Uint32  | component count  | 8  | the number of components this actor has (e.g. a Constructor has an input inventory)   
N/A  | components  | N/A  | a list of object references, for the format of one such ObjectReference, see below   
N/A  | properties  | N/A  | a list of properties, see PropertyList below   
Uint32  |  | 0  | always 0   
N/A  | trailing bytes  | N/A  | some actors have trailing bytes that contain additional information. for interpreting this data, see TrailingBytes   
  
#### ComponentObject

basic data type  | description  | example  | notes   
---|---|---|---  
Uint32  | size  | 194,584  | the number of bytes this ComponentObject has, including trailing bytes. Some components only have their header information, so this size could be zero   
N/A  | properties  | N/A  | a list of properties, see PropertyList below   
Uint32  |  | 0  | always 0   
N/A  | trailing bytes  | N/A  | some components have trailing bytes that contain additional information or are just padding zeros. for interpreting this data, see TrailingBytes or [existing save file parsers like SCIM](https://github.com/AnthorNet/SC-InteractiveMap/blob/ea5217e58ccd92de31e350d86816e7f093178804/src/SaveParser/Read.js#L469)  
  
#### ObjectReference

basic data type  | description  | example  | notes   
---|---|---|---  
String  | level name  | "Persistent_Level"  |   
String  | path name  | "Persistent_Level:PersistentLevel.Build_WorkBench_C_2146781450.FGFactoryLegs"  |   
  
#### Properties

Properties contain very different types of information. Every property has a name, which has the basic data type String. 

##### PropertyList

Zero, one or multiple concatenated properties form a PropertyList. A "name" field with the string value "None" indicates the immediate end of property list (with no other property fields following). 

The overall structure of one item in a PropertyList is as follows: 

basic data type  | description  | example  | notes   
---|---|---|---  
String  | name  | "mBerryIndex"  | If "None", then indicates the end of the property list   
String  | type name  | "IntProperty"  | Only present if name was not "None".   
Uint32  | payload size  | 0  | Only present if name was not "None". Indicates the size of the type-specific "payload", which starts after the pad byte; however, more type-specific headers may precede the pad byte first.   
N/A  | additional headers  | N/A  | Only present if name was not "None". Type-specific headers. Size and layout depends on the type name.   
Uint8  | pad byte  | 0  | Only present if name was not "None". Always zero.   
N/A  | payload  | N/A  | Only present if name was not "None". Size is indicated in "payload size". Layout depends on the type name.   
  
The sections below describe the type-specific parts of a property. 

##### ArrayProperty

basic data type  | description  | example  | notes   
---|---|---|---  
String  | name  | "mSpawnData"  |   
String  | type name  | "ArrayProperty"  |   
Uint32  | payload size  | 112  | the number of bytes this property has, starting after the first padding   
Uint32  | index  | 0  |   
String  | type  | "ObjectProperty"  | the type of the elements in this array   
Byte  | [padding](https://en.wikipedia.org/wiki/Data_structure_alignment "wikipedia:Data structure alignment") | 0  | always zero, as all padding should be   
Uint32  | length  | 1  | the number of elements in this array   
N/A  | array elements  | N/A  | a list of values, according to the stated element type and number of elements. although the types are named like the other "...Property" structures here, most are actually simpler: 

  * "ByteProperty": a single Byte per element
  * "EnumProperty" or "StrProperty": a single String per element
  * "InterfaceProperty" or "ObjectProperty": two Strings per element, "level name" and "path name"
  * "IntProperty": a single Int per element
  * "Int64Property": a single Long per element
  * "FloatProperty": a single Float per element
  * "SoftObjectProperty": an ObjectReference and a Uint32 per element


  * "StructProperty": same layout as a "Property", except the payload repeats for "length" times. The property header has the same name and type as the ArrayProperty name and type ("StructProperty"). For example:

| basic data type  | description  | example  | notes   
---|---|---|---  
String  | name  | "mStops"  | always matches the ArrayProperty name   
String  | type name  | "StructProperty"  | seems to always be "StructProperty"   
Uint32  | payload size  | 1234  | the combined size of all values in the array, starting after the "UUID" and the one byte padding below   
Uint32  | padding  | 0  |   
String  | element type  | "TimeTableStop"  | the type of elements in the payload of these StructProperty array elements "LinearColor", "Vector", "SpawnData", "BlueprintCategoryRecord", "BlueprintSubCategoryRecord", "DroneTripInformation", "FactoryCustomizationColorSlot", "FeetOffset", "FGCachedConnectedWire", "FGDroneFuelRuntimeData", "GCheckmarkUnlockData", "GlobalColorPreset", "HardDriveData", "HighlightedMarkerPair", "Hotbar", "InventoryStack", "ItemAmount", "MapMarker", "MessageData", "MiniGameResult", "PhaseCost", "PrefabIconElementSaveData", "PrefabTextElementSaveData", "ProjectAssemblyLaunchSequenceValue", "ResearchData", "ResearchTime", "ResourceSinkHistory", "ScannableObjectData", "ScannableResourcePair", "SchematicCost", "ShoppingListBlueprintEntry", "ShoppingListClassEntry", "ShoppingListRecipeEntry", "SplinePointData", "SplitterSortRule", "SubCategoryMaterialDefault", "TimeTableStop", "WireInstance"   
Uint32  | UUID  | 0  | In v0.8 and later, these four Uint32s are always zeros like in a padding   
Uint32  | UUID  | 0   
Uint32  | UUID  | 0   
Uint32  | UUID  | 0   
Byte  | padding  | 0  |   
N/A  | typed data  | N/A  | the list of elements with the actual payload of the property, see "TypedData" below for one such element   
  
##### BoolProperty

basic data type  | description  | example  | notes   
---|---|---|---  
String  | name  | "mSpawnedDebris"  |   
String  | type name  | "BoolProperty"  |   
Uint32  | payload size  | 0  | always 0 for BoolProperty   
Uint32  | index  | 0  | seems to always be zero   
Byte  | the boolean value  | 1  | 0 or 1. zero is considered "false", everything else is "true"   
Byte  | padding  | 0  | always 0   
  
##### ByteProperty

basic data type  | description  | example  | notes   
---|---|---|---  
String  | name  | "mLastAutoSaveId"  |   
String  | type name  | "ByteProperty"  |   
Uint32  | payload size  | 17  | the number of bytes this property has, starting after the padding   
Uint32  | index  | 0  | seems to always be zero   
String  | type  | "EGamePhase"  | semantics unclear, why is it not just a byte?   
Byte  | padding  | 0  | always 0   
Byte or String  | the byte value  | "EGP_LateGame"  | the actual value of this property. if type is "None", then its just a Byte, otherwise a String   
  
##### EnumProperty

basic data type  | description  | example  | notes   
---|---|---|---  
String  | name  | "mDestructibleActorState"  |   
String  | type name  | "EnumProperty"  |   
Uint32  | payload size  | 34  | the number of bytes this property has, starting after the padding   
Uint32  | index  | 0  | seems to always be zero   
String  | type  | "EIntroTutorialSteps"  | semantics unclear   
Byte  | padding  | 0  | always 0   
String  | the enum value  | "EIntroTutorialSteps::ITS_DONE"  | the actual value of this property   
  
##### FloatProperty

basic data type  | description  | example  | notes   
---|---|---|---  
String  | name  | "mCurrentHealth"  |   
String  | type name  | "FloatProperty"  |   
Uint32  | payload size  | 4  | the number of bytes this property has, starting after the padding   
Uint32  | index  | 0  | seems to always be zero   
Byte  | padding  | 0  | always 0   
Float  | the float value  | 0.37677494  | the actual value of this property   
  
##### DoubleProperty

basic data type  | description  | example  | notes   
---|---|---|---  
String  | name  |  |   
String  | type name  | "DoubleProperty"  |   
Uint32  | payload size  | 8  | the number of bytes this property has, starting after the padding   
Uint32  | index  | 0  | seems to always be zero   
Byte  | padding  | 0  | always 0   
Double  | the double value  | 0.37677494  | the actual value of this property   
  
##### IntProperty

basic data type  | description  | example  | notes   
---|---|---|---  
String  | name  | "mResourcesLeft"  |   
String  | type name  | "IntProperty"  |   
Uint32  | payload size  | 4  | the number of bytes this property has, starting after the padding   
Uint32  | index  | 0  | seems to always be zero   
Byte  | padding  | 0  | always 0   
Int  | the int value  | 10  | the actual value of this property   
  
##### Int8Property

basic data type  | description  | example  | notes   
---|---|---|---  
String  | name  | "mSelectedPoleVersion"  |   
String  | type name  | "Int8Property'  |   
Uint32 | payload size | 1 | the number of bytes this property has, starting after the padding   
Uint32 | index | 0 | seems to always be zero   
Byte | padding | 0 | always 0   
Byte | the int8 value | 4 | the actual value of this property   
  
##### UInt32Property

basic data type  | description  | example  | notes   
---|---|---|---  
String  | name  | "mSavedFoliageGridSize"  |   
String  | type name  | "UInt32Property"  |   
Uint32  | payload size  | 4  | the number of bytes this property has, starting after the padding   
Uint32  | index  | 0  | seems to always be zero   
Byte  | padding  | 0  | always 0   
Uint32  | the uint32 value  | 2,830,424,080  | the actual value of this property   
  
##### Int64Property

basic data type  | description  | example  | notes   
---|---|---|---  
String  | name  | "TotalDismantled"  |   
String  | type name  | "Int64Property"  |   
Uint32  | payload size  | 8  | the number of bytes this property has, starting after the padding   
Uint32  | index  | 0  | seems to always be zero   
Byte  | padding  | 0  | always 0   
Long  | the long value  | 2,830,424,080  | the actual value of this property   
  
##### MapProperty

basic data type  | description  | example  | notes   
---|---|---|---  
String  | name  | "mSaveData"  |   
String  | type name  | "MapProperty"  |   
Uint32  | payload size  | 370  | the number of bytes this property has, starting after the padding   
Uint32  | index  | 0  | seems to always be zero   
String  | key type  | "ObjectProperty"  | the type the keys of this map have   
String  | value type  | "IntProperty"  | the type the values of this map have   
Byte  | padding  | 0  | always 0   
Uint32  | mode type  | 0  | semantics unclear, seems to be always 0, but does not seem to be a simple padding   
Uint32  | number of elements  | 4  | the number of key-value pairs in this map   
N/A  | map elements  | N/A  | a list of key-value pairs, according to the stated types and number of pairs. although the types are named like the other "...Property" structures here, they are actually simpler: 

  * the key types seem to always be one of these: 
    * "ObjectProperty": a single ObjectReference per key-value pair
    * "IntProperty": a single Int per key-value pair
    * "StructProperty": 3 Int's per key-value pair
  * the value types seem to always be one of these: 
    * "ByteProperty": a single Byte per key-value pair
    * "IntProperty": a single Int per key-value pair
    * "Int64Property": a single Int64 per key-value pair
    * "StructProperty": a list of properties per key-value pair, see "PropertyList" above for one of this list

  
  
##### NameProperty

basic data type  | description  | example  | notes   
---|---|---|---  
String  | name  | "mStartingPointTagName"  |   
String  | type name  | "NameProperty"  |   
Uint32  | payload size  | 17  | the number of bytes this property has, starting after the padding   
Uint32  | index  | 0  | seems to always be zero   
Byte  | padding  | 0  | always 0   
String  | the string value  | "Rocky Desert"  | the actual value of this property   
  
##### ObjectProperty

data type  | description  | example  | notes   
---|---|---|---  
String  | name  | "mBuildableSubsystem"  |   
String  | type name  | "ObjectProperty"  |   
Uint32  | payload size  | 104  | the number of bytes this property has, starting after the padding   
Uint32  | index  | 0  | seems to always be zero   
Byte  | padding  | 0  | always 0   
ObjectReference  | level/path  |  | the actual value of this property   
  
##### SoftObjectProperty

data type  | description  | example  | notes   
---|---|---|---  
String  | name  |  |   
String  | type name  | "SoftObjectProperty"  |   
Uint32  | payload size  | 104  | the number of bytes this property has, starting after the padding   
Uint32  | index  | 0  | seems to always be zero   
Byte  | padding  | 0  | always 0   
ObjectReference  | level/path  |  | the actual value of this property   
Uint32  |  |  | the actual value of this property   
  
##### SetProperty

basic data type  | description  | example  | notes   
---|---|---|---  
String  | name  | "mLootedDropPods"  |   
String  | type name  | "SetProperty"  |   
Uint32  | payload size  | 5,240  | the number of bytes this property has, starting after the first padding   
Uint32  | index  | 0  | seems to always be zero   
String  | type  | "StructProperty"  | the type of the elements in this set, either "UInt32Property" or "StructProperty"   
Byte  | padding  | 0  | always 0   
Uint32  | padding  | 0  | always 0   
Uint32  | length  | 436  | the number of elements in this set   
N/A  | set elements  | N/A  | a list of values, according to the stated element type and number of elements. e.g. for the "mRemovalLocations" property of "/Script/FactoryGame.FGFoliageRemoval", each removal location element is of type "StructProperty". The actual location element is simpler than the StructProperty described below, since a location is just x/y/z, each of basic data type Float. 

  * "UInt32Property": a single Uint32 per element
  * "StructProperty": 2 Uint64s per element
  * "ObjectProperty": a single ObjectReference

  
  
##### StrProperty

basic data type  | description  | example  | notes   
---|---|---|---  
String  | name  | "mSaveSessionName"  |   
String  | type name  | "StrProperty"  |   
Uint32  | payload size  | 9  | the number of bytes this property has, starting after the padding   
Uint32  | index  | 0  | seems to always be zero   
Byte  | padding  | 0  | always 0   
String  | the string value  | "Name"  | the actual value of this property   
  
##### StructProperty

basic data type  | description  | example  | notes   
---|---|---|---  
String  | name  | "mFluidBox"  |   
String  | type name  | "StructProperty"  |   
Uint32  | payload size  | 387  | the number of bytes this property has, starting after the padding   
Uint32  | index  | 1  |   
String  | type  | "TrainDockingRuleSet"  | the type of structure this property's payload represents: , "BlueprintRecord", "BoomBoxPlayerState", "DroneDockingStateInfo", "DroneTripInformation", "FGPlayerPortalData", "FGPortalCachedFactoryTickData", "FactoryCustomizationColorSlot", "FactoryCustomizationData", "InventoryStack", "LightSourceControlData", "MapMarker", "PersistentGlobalIconId", "PlayerCustomizationData", "PlayerRules", "ResearchData", "ShoppingListSettings", "TimerHandle", "TopLevelAssetPath", "TrainDockingRuleSet", "TrainSimulationData", "Transform", "Vector_NetQuantize"   
Long  | padding  | 0  |   
Long  | padding  | 0  |   
Byte  | padding  | 0  |   
N/A  | typed data  | N/A  | the actual payload of the property, see "TypedData" below for "InventoryItem", "LinearColor", "Vector", "Quat", "Box", "FluidBox", "RailroadTrackPosition", "DateTime", "ClientIdentityInfo"; all other types represent a PropertyList   
  
##### TextProperty

basic data type  | description  | example  | notes   
---|---|---|---  
String  | name  | "mBlueprintName"  |   
String  | type name  | "NameProperty"  |   
Uint32  | payload size  | 34  | the number of bytes this property has, starting after the padding   
Uint32  | index  | 0  | seems to always be zero   
Byte  | padding  | 0  |   
Uint32  | flags  | 18  | semantics unclear   
Byte  | history type  | -1  | semantics unclear, seems to be always -1   
Uint32  | is text culture invariant?  | 1  | semantics unclear, seems to be always 1 (as a boolean, this would be "true", sincei it is not zero)   
String  | the text value  | "my fancy train station"  | the actual value of this property   
  
#### TypedData

As the payload of a ArrayProperty's StructProperty, several custom types can occur. Note that the actual type is stated beforehand as a String, with a gap of 17 bytes to this structure. 

##### Box

basic data type  | description  | example  | notes   
---|---|---|---  
Double  | min x  | -269,069.38  |   
Double  | min y  | -309,234.5  |   
Double  | min z  | -27,460.76  |   
Double  | max x  | 318,316.0  |   
Double  | max y  | 303,073.75  |   
Double  | max z  | 29,100.76  |   
Byte  | is valid?  | 1  | 0 or 1. semantics unclear   
  
##### FluidBox

basic data type  | description  | example  | notes   
---|---|---|---  
Float  | the float value of this FluidBox  | 6.3548093  |   
  
##### InventoryItem

data type  | description  | example  | notes   
---|---|---|---  
Uint32  | padding  | 0  | always 0   
String  | item name  |  |   
Uint32  | item has properties flag  | 0  | 0 or 1   
Uint32  | padding  | 0  | present only when "item has properties flag" is non-zero; always 0   
String  | item type  | "/Game/FactoryGame/Resource/Equipment/NailGun/Desc_RebarGunProjectile.Desc_RebarGunProjectile_C"  | present only when "item has properties flag" is non-zero   
Uint32  | property size  | the number of bytes of the following properties  | present only when "item has properties flag" is non-zero   
PropertyList  | properties  |  | present only when "item has properties flag" is non-zero   
  
##### LinearColor

basic data type  | description  | example  | notes   
---|---|---|---  
Float  | r  | 0.783538  |   
Float  | g  | 0.291771  |   
Float  | b  | 0.057805  |   
Float  | a  | 1.0  |   
  
##### Quat

basic data type  | description  | example  | notes   
---|---|---|---  
Double  | x  | 0.42907318  |   
Double  | y  | -0.13565472  |   
Double  | z  | -0.23136456  |   
Double  | w  | 0.8625337  |   
  
##### RailroadTrackPosition

data type  | description  | example  | notes   
---|---|---|---  
ObjectReference  | object reference  |  |   
Float  | offset  | 93.29132  |   
Float  | forward  | 1.0  |   
  
##### Vector

basic data type  | description  | example  | notes   
---|---|---|---  
Double  | x  | 2.1905906  |   
Double  | y  | 2.1905906  |   
Double  | z  | 2.1905909  |   
  
Note: Unlike "Vector", "Vector_NetQuantize" is serialized as a regular property list. 

##### DateTime

basic data type  | description  | example  | notes   
---|---|---|---  
Int64  | date time  |  |   
  
##### ClientIdentityInfo

basic data type  | description  | example  | notes   
---|---|---|---  
String  |  |  | UUID   
Uint32  | identity count  | 1  | the number of identities to follow   
N/A  | identity  |  |  | basic data type  | description  | example  | notes   
---|---|---|---  
Byte  |  | 6  | 1=Epic. 6=Steam.   
Uint32  | identity data size  | 8  | the number of bytes of the following data   
N/A  | identity data  |  |   
  
#### Trailing Bytes

Trailing bytes can be present after an ActorObject or ComponentObject. The format of the trailing bytes is specific to the game object. 

Note: Saves created by Satisfactory Calculator's Interactive Map have trailing bytes for additional objects not shown in this table. This table includes only those objects given trailing bytes by Satifactory game itself. The additional SCIM bytes are always a single zero Uint32. 

object type  | object name  | trailing bytes format   
---|---|---  
ActorObject  | "/Game/FactoryGame/Buildable/Factory/ConveyorBeltMk1/Build_ConveyorBeltMk1.Build_ConveyorBeltMk1_C" "/Game/FactoryGame/Buildable/Factory/ConveyorBeltMk2/Build_ConveyorBeltMk2.Build_ConveyorBeltMk2_C" "/Game/FactoryGame/Buildable/Factory/ConveyorBeltMk3/Build_ConveyorBeltMk3.Build_ConveyorBeltMk3_C" "/Game/FactoryGame/Buildable/Factory/ConveyorBeltMk4/Build_ConveyorBeltMk4.Build_ConveyorBeltMk4_C" "/Game/FactoryGame/Buildable/Factory/ConveyorBeltMk5/Build_ConveyorBeltMk5.Build_ConveyorBeltMk5_C" "/Game/FactoryGame/Buildable/Factory/ConveyorBeltMk6/Build_ConveyorBeltMk6.Build_ConveyorBeltMk6_C" "/Game/FactoryGame/Buildable/Factory/ConveyorLiftMk1/Build_ConveyorLiftMk1.Build_ConveyorLiftMk1_C" "/Game/FactoryGame/Buildable/Factory/ConveyorLiftMk2/Build_ConveyorLiftMk2.Build_ConveyorLiftMk2_C" "/Game/FactoryGame/Buildable/Factory/ConveyorLiftMk3/Build_ConveyorLiftMk3.Build_ConveyorLiftMk3_C" "/Game/FactoryGame/Buildable/Factory/ConveyorLiftMk4/Build_ConveyorLiftMk4.Build_ConveyorLiftMk4_C" "/Game/FactoryGame/Buildable/Factory/ConveyorLiftMk5/Build_ConveyorLiftMk5.Build_ConveyorLiftMk5_C" "/Game/FactoryGame/Buildable/Factory/ConveyorLiftMk6/Build_ConveyorLiftMk6.Build_ConveyorLiftMk6_C"  | Uint32 count For each element: 

  * Uint32 length
  * String name
  * String always empty
  * String always empty
  * Float position

  
ActorObject  | "/Game/FactoryGame/-Shared/Blueprint/BP_GameMode.BP_GameMode_C" "/Game/FactoryGame/-Shared/Blueprint/BP_GameState.BP_GameState_C"  | Uint32 count For each element: ObjectReference   
ActorObject  | "/Game/FactoryGame/Character/Player/BP_PlayerState.BP_PlayerState_C"  | Byte: Formatting, either 3 or 241 If the initial byte is 3, no more trailing data If the initial byte is 241: 

  * Byte: 1=Epic, 6=Steam
  * Uint32: number of bytes remaining
  * Bytes of length specified

  
ActorObject  | "/Game/FactoryGame/Buildable/Factory/DroneStation/BP_DroneTransport.BP_DroneTransport_C"  |   
ActorObject  | "/Game/FactoryGame/-Shared/Blueprint/BP_CircuitSubsystem.BP_CircuitSubsystem_C"  | Uint32 count For each element: 

  * Uint32
  * ObjectReference

  
ActorObject  | "/Game/FactoryGame/Buildable/Factory/PowerLine/Build_PowerLine.Build_PowerLine_C" "/Game/FactoryGame/Events/Christmas/Buildings/PowerLineLights/Build_XmassLightsLine.Build_XmassLightsLine_C"  | 2 ObjectReferences   
ActorObject  | "/Game/FactoryGame/Buildable/Vehicle/Train/Locomotive/BP_Locomotive.BP_Locomotive_C" "/Game/FactoryGame/Buildable/Vehicle/Train/Wagon/BP_FreightWagon.BP_FreightWagon_C"  |   
ActorObject  | "/Game/FactoryGame/Buildable/Vehicle/Cyberwagon/Testa_BP_WB.Testa_BP_WB_C" "/Game/FactoryGame/Buildable/Vehicle/Explorer/BP_Explorer.BP_Explorer_C" "/Game/FactoryGame/Buildable/Vehicle/Golfcart/BP_Golfcart.BP_Golfcart_C" "/Game/FactoryGame/Buildable/Vehicle/Tractor/BP_Tractor.BP_Tractor_C" "/Game/FactoryGame/Buildable/Vehicle/Truck/BP_Truck.BP_Truck_C"  | Uint32 count For each element: 

  * Uint32
  * 105 Bytes

  
ActorObject  | "/Script/FactoryGame.FGItemPickup_Spawnable"  |   
ActorObject  | "/Script/FactoryGame.FGLightweightBuildableSubsystem"  | 

  * Uint32
  * Uint32 count


  * For each element: 
    * Uint32 always 0
    * String
    * Uint32 count
    * For each element: 
      * 4 Doubles rotation quaternion
      * 3 Doubles position
      * 3 Doubles scale (always 1.0)
      * Uint32 always 0
      * String: swatch
      * 3 Uint32 always 0
      * String: pattern description number
      * 2 Uint32 always 0
      * 4 Floats primary color
      * 4 Floats secondary color
      * Uint32 always 0
      * Uint32 data size of unknown data
      * N/A Unknown data of specified size
      * Uint32: Seen values 0 thru 4
      * Byte always 0
      * String recipe
      * ObjectReference blueprint proxy
      * Uint32 always 0

  
ActorObject  | "/Script/FactoryGame.FGConveyorChainActor" "/Script/FactoryGame.FGConveyorChainActor_RepSizeNoCull" "/Script/FactoryGame.FGConveyorChainActor_RepSizeMedium" "/Script/FactoryGame.FGConveyorChainActor_RepSizeLarge" "/Script/FactoryGame.FGConveyorChainActor_RepSizeHuge"  | ObjectReference starting belt (the same reference as the first belt in the list below) ObjectReference ending belt (the same reference as the last belt in the list below) Uint32 number of belts in chain For each belt: 

  * ObjectReference conveyor chain actor (the same reference for each belt)
  * ObjectReference belt
  * Uint32 number of elements
  * For each element: 
    * 9 Uint64s in 3 groups of 3
  * 3 Uint32s
  * 2 Ints
  * Uint32 belt index

Uint32 3 Ints Uint32 number of items For each item: 

  * Uint32 always 0
  * String item
  * Uint32 always 0
  * Uint32

  
ComponentObject  | "/Script/FactoryGame.FGDroneMovementComponent" "/Script/FactoryGame.FGFactoryConnectionComponent" "/Script/FactoryGame.FGFactoryLegsComponent" "/Script/FactoryGame.FGHealthComponent" "/Script/FactoryGame.FGInventoryComponent" "/Script/FactoryGame.FGInventoryComponentEquipment" "/Script/FactoryGame.FGInventoryComponentTrash" "/Script/FactoryGame.FGPipeConnectionComponent" "/Script/FactoryGame.FGPipeConnectionComponentHyper" "/Script/FactoryGame.FGPipeConnectionFactory" "/Script/FactoryGame.FGPowerConnectionComponent" "/Script/FactoryGame.FGPowerInfoComponent" "/Script/FactoryGame.FGRailroadTrackConnectionComponent" "/Script/FactoryGame.FGShoppingListComponent" "/Script/FactoryGame.FGTrainPlatformConnection"  | Uint32 always 0   
  
### Libraries and implementations

For manipulating save and blueprint files, instead of writing a parser/writer from scratch, you can use the following community implementations: 

Save file format community implementations  Name  | Language  | URL   
---|---|---  
Satisfactory Interactive Map  | JavaScript  | <https://github.com/AnthorNet/SC-InteractiveMap/blob/dev/src/SaveParser/Read.js>  
SatisfactorySaveNet  | C#  | <https://github.com/R3dByt3/SatisfactorySaveNet/>  
satisfactory-3d-map  | C++ / Python  | <https://github.com/moritz-h/satisfactory-3d-map>  
satisfactory.save  | D  | <https://gitlab.com/cybershadow/satisfactory-save-files/>  
  
## Dedicated Server settings file

_See:_[Dedicated_servers#Server_File_Locations](/wiki/Dedicated_servers#Server_File_Locations "Dedicated servers")

  
This file is also an Unreal Engine save file. 

Using the in-game Server Manager UI is currently the only supported method for modifying this file. Settings may also be changed through the [HTTPS API](/wiki/Dedicated_servers/HTTPS_API "Dedicated servers/HTTPS API"). 

`ServerSettings.PORT.sav` Property | Description   
---|---  
ServerName | Just a friendly name for this server. Can be used in UI dialogs to identify the server   
AutoLoadSessionName | If set, the most recent save from this session will be automatically loaded on server startup   
AdminPassword | Admin password set on the server. Used to access administration based functions of the Server API   
ClientPassword | Client password set on the server. Required to join the game in the first place.   
ServerSecret | Server secret encoded as hex nibble string. Used to hash the data used for the tokens and generate the fingerprint   
CertificateData | Generated certificate data that should be re-used across server restarts   
  
## History

  * [Patch 1.1.1.2](/wiki/Patch_1.1.1.2 "Patch 1.1.1.2"): Fix for a Crash on specific saves that had faulty [Blueprints](/wiki/Blueprint "Blueprint") using auto connected [Conveyor Belts](/wiki/Conveyor_Belts "Conveyor Belts") during a previous update during experimental
  * [Patch 1.1.0.2](/wiki/Patch_1.1.0.2 "Patch 1.1.0.2"): Fixed crash when loading a save caused by [Railway Switches](/wiki/Railroad_Switch_Control "Railroad Switch Control")
  * [Patch 1.0.1.0](/wiki/Patch_1.0.1.0 "Patch 1.0.1.0"): Fixed a Crash when there is a Failure to open Save game and [blueprint](/wiki/Blueprint "Blueprint") files for reading
  * [Patch 1.0.0.6](/wiki/Patch_1.0.0.6 "Patch 1.0.0.6"): Fixed so that items don’t respawn when loading save files created in [1.0.0.4](/wiki/Patch_1.0.0.4 "Patch 1.0.0.4")
  * [Patch 1.0.0.4](/wiki/Patch_1.0.0.4 "Patch 1.0.0.4")
    * Fix for some buildable's disappearing in very old saves (Around [Update 2](/wiki/Update_2 "Update 2")) 
      * This fix is not retroactive, this means if you have overwritten a save with missing buildings after playing the 1.0 version, those buildings will remain missing.  
This only prevents buildables disappearing on old saves that are loaded/re-saved from this patch onwards. We’re sorry for the inconvenience, this was a very complicated issue.
  * [Patch 1.0](/wiki/Patch_1.0 "Patch 1.0"): Saving and Autosaving should now take considerably less time than ever before. This should make it so the autosaving happening is a lot less disruptive and will be especially noticeable in big factories!
  * [Patch 0.8.1.1](/wiki/Patch_0.8.1.1 "Patch 0.8.1.1"): Potential fix for a Crash related to save session
  * [Patch 0.8.0.0](/wiki/Patch_0.8.0.0 "Patch 0.8.0.0"): Optimized the [save](/wiki/Save_file "Save file") system to decrease saving time on larger saves by roughly 80-90%
  * [Patch 0.6.0.11](/wiki/Patch_0.6.0.11 "Patch 0.6.0.11"): Potentially fixed crash when saving/autosaving introduced in [CL 198647](/wiki/Patch_0.6.0.10 "Patch 0.6.0.10")
  * [Patch 0.6.0.5](/wiki/Patch_0.6.0.5 "Patch 0.6.0.5")
    * Fixed not being able to save without typing a name for the session first (Name will be auto set to “SessionName_Timestamp” if the name field is blank)
    * Fixed Delete Save button not working properly
  * [Patch 0.6.0.4](/wiki/Patch_0.6.0.4 "Patch 0.6.0.4"): Fixed a bug where “Invalid Session ID” could be displayed in the name of saves when trying to save a new session without typing a new save name
  * [Patch 0.6.0.0](/wiki/Patch_0.6.0.0 "Patch 0.6.0.0"): Implemented Sublevel Saving



## References

  1. ↑ [YouTube - How to find save game files on Steam Deck (2025)](https://www.youtube.com/watch?v=zqYgPf4u2yc)



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
Technical| [Console release](/wiki/Console_release "Console release") • [Debug console](/wiki/Debug_console "Debug console") • [Launch arguments](/wiki/Launch_arguments "Launch arguments") • Save files • [System requirements](/wiki/System_requirements "System requirements") • [Units](/wiki/Units "Units") • [Unreal Engine](/wiki/Unreal_Engine "Unreal Engine")  
Guides and tutorials| | Basics| [Walkthrough/How to play](/wiki/Tutorial:How_to_play "Tutorial:How to play") • [New Pioneer Guide](/wiki/Tutorial:New_Pioneer_Guide "Tutorial:New Pioneer Guide") • [Production line basics](/wiki/Tutorial:Production_line "Tutorial:Production line") • [Advanced production line tips](/wiki/Tutorial:Production_line_design_tips "Tutorial:Production line design tips") • [Picking an alternate recipe](/wiki/Tutorial:Picking_an_alternate_recipe "Tutorial:Picking an alternate recipe") • [Independency](/wiki/Tutorial:Independency "Tutorial:Independency") • [Aluminum Ingot production](/wiki/Tutorial:Setting_up_Aluminum_Ingot_production "Tutorial:Setting up Aluminum Ingot production")  
---|---  
Logistics| [Manifold](/wiki/Manifold "Manifold") • [Balancer](/wiki/Balancer "Balancer") • [Pipeline manifold](/wiki/Pipeline_manifold "Pipeline manifold") • [Prime Splitter Arrays](/wiki/Tutorial:Prime_splitter_arrays "Tutorial:Prime splitter arrays") • [Trains](/wiki/Tutorial:Trains "Tutorial:Trains") • [Train throughput](/wiki/Tutorial:Train_throughput "Tutorial:Train throughput")  
Dedicated servers| [Dedicated servers](/wiki/Dedicated_servers "Dedicated servers") • [Running as a Service](/wiki/Dedicated_servers/Running_as_a_Service "Dedicated servers/Running as a Service") • [Configuration files](/wiki/Dedicated_servers/Configuration_files "Dedicated servers/Configuration files") • [Automatic updates](/wiki/Dedicated_servers/Automatic_updates "Dedicated servers/Automatic updates") • [HTTPS API](/wiki/Dedicated_servers/HTTPS_API "Dedicated servers/HTTPS API") • [Lightweight Query API](/wiki/Dedicated_servers/Lightweight_Query_API "Dedicated servers/Lightweight Query API")  
Other| [Hypertube cannon](/wiki/Tutorial:Hypertube_cannon "Tutorial:Hypertube cannon") • [Hypertube brake](/wiki/Tutorial:Hypertube_brake "Tutorial:Hypertube brake") • [Steam Deck & Controller setup](/wiki/Tutorial:Controller_setup "Tutorial:Controller setup") • [Extracting UI icons](/wiki/Tutorial:Extracting_UI_icons "Tutorial:Extracting UI icons")
  *[v]: View this template
  *[e]: Edit this template
  *[h]: History of this template
  *[his]: his trivia section
