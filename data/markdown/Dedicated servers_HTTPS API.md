# Dedicated servers/HTTPS API

## Contents

  * 1 HTTPS API
    * 1.1 Certificate Validation and Encryption
    * 1.2 Schema
      * 1.2.1 Request Schema
      * 1.2.2 Response Schema
      * 1.2.3 File Responses
      * 1.2.4 Multipart Requests
  * 2 Authentication
  * 3 HealthCheck
    * 3.1 Summary
    * 3.2 Function Request Data
    * 3.3 Function Response Data
  * 4 VerifyAuthentication Token
    * 4.1 Summary
  * 5 PasswordlessLogin
    * 5.1 Summary
    * 5.2 Function Request Data
    * 5.3 Function Response Data
    * 5.4 Possible Errors
  * 6 PasswordLogin
    * 6.1 Summary
    * 6.2 Function Request Data
    * 6.3 Function Response Data
    * 6.4 Possible Errors
  * 7 QueryServerState
    * 7.1 Summary
    * 7.2 Function Response Data
    * 7.3 ServerGameState
    * 7.4 Community Notes
  * 8 GetServerOptions
    * 8.1 Summary
    * 8.2 Function Response Data
  * 9 GetAdvancedGameSettings
    * 9.1 Summary
    * 9.2 Function Response Data
  * 10 ApplyAdvancedGameSettings
    * 10.1 Summary
    * 10.2 Function Request Data
  * 11 ClaimServer
    * 11.1 Summary
    * 11.2 Function Request Data
    * 11.3 Function Response Data
    * 11.4 Possible Errors
  * 12 RenameServer
    * 12.1 Summary
    * 12.2 Function Request Data
    * 12.3 Possible Errors
  * 13 SetClientPassword
    * 13.1 Summary
    * 13.2 Function Request Data
    * 13.3 Possible Errors
  * 14 SetAdminPassword
    * 14.1 Summary
    * 14.2 Function Request Data
    * 14.3 Possible Errors
  * 15 SetAutoLoadSessionName
    * 15.1 Summary
    * 15.2 Function Request Data
  * 16 Run Command
    * 16.1 Summary
    * 16.2 Function Request Data
    * 16.3 Function Response Data
  * 17 Shutdown
    * 17.1 Summary
  * 18 ApplyServerOptions
    * 18.1 Summary
    * 18.2 Function Request Data
  * 19 CreateNewGame
    * 19.1 Summary
    * 19.2 Function Request Data
    * 19.3 ServerNewGameData
      * 19.3.1 Note
  * 20 SaveGame
    * 20.1 Summary
    * 20.2 Function Request Data
    * 20.3 Possible Errors
  * 21 DeleteSaveFile
    * 21.1 Summary
    * 21.2 Function Request Data
    * 21.3 Possible Errors
  * 22 DeleteSaveSession
    * 22.1 Summary
    * 22.2 Function Request Data
    * 22.3 Possible Errors
  * 23 EnumerateSessions
    * 23.1 Summary
    * 23.2 Function Response Data
    * 23.3 Possible Errors
    * 23.4 SessionSaveStruct
    * 23.5 SaveHeader
  * 24 LoadGame
    * 24.1 Summary
    * 24.2 Function Request Data
    * 24.3 Possible Errors
  * 25 UploadSaveGame
    * 25.1 Summary
    * 25.2 Multipart Field
    * 25.3 Function Request Data
    * 25.4 Possible Errors
  * 26 DownloadSaveGame
    * 26.1 Summary
    * 26.2 Function Request Data
    * 26.3 Possible Errors
  * 27 See also



This page is a copy of the HTTPS API section of the `DedicatedServerAPIDocs.md` document distributed to every player, with some community notes and edits. 

For a list of community tools, see [Dedicated_servers#Community_Tools](/wiki/Dedicated_servers#Community_tools "Dedicated servers"). 

## HTTPS API

The Dedicated Server HTTPS API is designed for reliably retrieving data from the running dedicated server instance and performing server management. It is available when the server has started up and is not actively loading a save game or performing a map change. To check for HTTPS API availability, the Lightweight Query API can be used. 

The HTTPS API endpoint is available at `/api/v1` (e.g. `<https://127.0.0.1:7777/api/v1>`). 

### Certificate Validation and Encryption

The HTTPS API is always wrapped in a TLS tunnel, even if the user did not provide a certificate for the Dedicated Server. 

User certificates will be looked up at the following path (where $InstallRoot$ is the path where the Dedicated Server is installed): 

File Path  | File Type  | Description   
---|---|---  
$InstallRoot$/FactoryGame/Certificates/cert_chain.pem  | Certificate Chain (PEM)  | Certificate chain in PEM format   
$InstallRoot$/FactoryGame/Certificates/private_key.pem  | Private Key (PEM)  | Certificate's private key in PEM format   
  
If no certificate is provided by the user, the Dedicated Server will generate its own self-signed certificate and use it to encrypt all traffic flowing through the HTTPS API. Clients should be able to handle the HTTPS certificate being self-signed, recognize that case, and handle it appropriately. 

**Community Note** : The generated TLS cert is saved into the ServerSettings.PORT.sav. See [Dedicated_servers/Configuration_files#Server_Settings_File](/wiki/Dedicated_servers/Configuration_files#Server_Settings_File "Dedicated servers/Configuration files")

When presented with a self-signed certificate from the Dedicated Server, the game client will prompt the user to manually confirm that the certificate is from a trusted authority. Once confirmed, the certificate is cached locally and is trusted for that specific server until the user revokes it or the server changes the certificate. 

**Community Note: Many implementations of cURL will fail when validating a self-signed certificate as used in many servers and adding`--insecure` or the equivalent may be required to establish a connection to the server**

### Schema

The HTTPS API is based on a simple JSON schema used to pass data to the functions executing on the server and pass responses back to the caller. All server API functions are executed as POST requests, although certain query requests can be executed via GET requests if they do not require any data to be provided. 

#### Request Schema

Content Type for requests should be set to `application/json`. Encoding should preferably be set to `utf-8`, but Dedicated Servers support all encodings supported by the ICU localization library. 

Request Object has the following properties: 

Property Name  | Property Type  | Description   
---|---|---  
function  | string  | Name of the API function to execute. Names of the API functions and their behavior are described below   
data  | object  | Data to pass to the function to execute. Format of the object depends on the function being executed   
  
An example JSON would look like this: 
    
    
    {
        "function": "SetAutoLoadSession",
        "data": {
            "SessionName": "What a game"
        }
    }
    

Dedicated Server HTTPS API supports the following standard headers: 

Header Name  | Notes   
---|---  
Content-Encoding  | Optional. Only gzip and deflate are supported   
Authorization  | Required for most non-Authorization API functions. Only Bearer tokens are supported. See Authorization for more info   
  
The following Satisfactory-specific headers can also be used in the request: 

Header Name  | Data Type  | Description   
---|---|---  
X-FactoryGame-PlayerId  | Hex String  | Hex-encoded byte array encoding the ID of the player on behalf of which the request is made   
  
The `X-FactoryGame-PlayerId` header is only needed to obtain the server join/encryption tickets used for joining the server, and its format is highly specific to the Satisfactory version running, Unreal Engine version, and the Online Backend used by the player. 

Generally, the first byte of the ID indicates the type of Online Backend used (1 for Epic Games Store, 6 for Steam, see values in UE's EOnlineServices type), and the following bytes are specific to the Online Backend, but generally represent the player account ID. For Steam, it would be a big-endian uint64 representing the player's SteamID64, and for Epic, it would be a HEX-encoded EOS ProductUserId string. 

#### Response Schema

The Dedicated Server can return a variety of different HTTP status codes, most prominent ones are described here: 

Status Code  | Status Code Name  | Description   
---|---|---  
200  | Ok  | The function has been executed successfully. The response body will either be an Error Response or a Success Response   
201  | Created  | The function has been executed and returned no error. Returned by some functions to indicate that a new file has been created, such as UploadSaveGame   
202  | Accepted  | The function has been executed, but is still being processed. This is returned by some functions with side effects, such as LoadGame   
204  | No Content  | The function has been executed successfully, but returned no data (and no error)   
400  | Bad Request  | Only returned when the request body failed to be parsed as valid JSON or multipart request. In other cases, error response `bad_request` is used   
401  | Denied  | Authentication token is missing, cannot be parsed, or has expired   
403  | Forbidden  | Provided authentication does not allow executing the provided function, or when a function requiring authentication is called without one   
404  | Not Found  | The specified function cannot be found, or when the function cannot find the specified resource in some cases (for example, for DownloadSaveGame)   
415  | Unsupported Media  | Specified charset or content encoding is not supported, or multipart data is malformed   
500  | Server Error  | An internal server error has occurred when executing the function   
  
The Content Type of the server response will be set to `application/json` and `utf-8` encoding. Depending on the outcome of the operation, it might return either an error response or a data response. 

Error Response has the following structure: 

Property Name  | Property Type  | Description   
---|---|---  
errorCode  | string  | Machine-friendly code indicating the type of the error that the executed function returned   
errorMessage  | string?  | Optional. Human-friendly error message explaining the error   
errorData  | object?  | Optional. Additional information about the error, for example, list of parameters that are missing   
  
An example JSON would look like this:
    
    
    {
        "errorCode": "insufficient_scope",
        "errorMessage": "The client is missing required privileges to access the given function"
    }
    

Success Response has the following structure: 

Property Name  | Property Type  | Description   
---|---|---  
data  | object?  | Data returned by the function executed. Type depends on the function the request performed   
  
#### File Responses

Certain Dedicated Server API functions can respond with a file attachment instead of using the standard Server Response JSON schema. Such responses can be distinguished by the presence of the `Content-Disposition` header, indicating that the `Content-Type` and body represent a file attachment and not a standard Server API response body. 

Such functions can still return a normal server response in case of an Error Response. Currently, the only function that utilizes the File Response functionality is `DownloadSaveGame`, which returns the save game file as a response without any additional Server API metadata attachments. 

#### Multipart Requests

Certain Server API functions can take both Server API request payload and a file attachment. Such functions should use `multipart/form-data` Content-Type and encode both the payload and the Server API request body as separate multipart parts. 

Multipart Part named `data` should be present in all multipart requests and encode the request object JSON with the same schema and restrictions as the normal non-multipart requests. The charset should be provided as a separate multipart part with a special name `_charset_`, and contain the name of the charset used for encoding the Server API request as plain text. 

Names of other multipart attachments are specific to the functions using multipart requests. Currently, multipart requests are only used by the `UploadSaveGame` function for uploading save game files. 

## Authentication

The Dedicated Server API requires authentication for most of its functions. Authentication format used is Bearer tokens, which are issued by the Dedicated Server when using certain API functions that require no Authentication (such as `PasswordlessLogin`), or functions that require additional security verification (such as `PasswordLogin`). Tokens generated by these functions are short-lived and are bound to the specific player account. 

Authentication Tokens internally consist of two parts separated by the dot character ('.'): 

  * Base64-encoded JSON token payload
  * HEX-encoded Fingerprint



JSON token payload can be retrieved to determine the privilege level granted by the token, while the fingerprint part is used by the server to check the validity of the token and whenever it can be used currently. 

Internal Authentication Token Payload: 

Property Name  | Property Type  | Description   
---|---|---  
pl  | string  | Privilege Level granted by this token. See possible values below   
  
Possible Privilege Level values: 

Privilege Level  | Description   
---|---  
NotAuthenticated  | The client is not Authenticated   
Client  | Client is Authenticated with Client privileges   
Administrator  | Client is Authenticated with Admin privileges   
InitialAdmin  | Client is Authenticated as Initial Admin with privileges to Claim the server   
APIToken  | Client is Authenticated as Third Party Application   
  
The following functions are used by the game client to perform player authentication: 

Function Name  | Description   
---|---  
PasswordlessLogin  | Attempts logging in as a player without a password.   
PasswordLogin  | Attempts logging in as a player with a password.   
VerifyAuthenticationToken  | Checks if the provided Authentication token is valid. Returns Ok if valid   
  
Third Party Applications should NOT use `PasswordLogin` or `PasswordlessLogin`, and should instead rely on the Application Tokens. 

Application tokens do not expire and are granted by issuing the command `server.GenerateAPIToken` in the Dedicated Server console. The generated token can then be passed to the `Authorization` header with Bearer type to perform any Server API requests on behalf of the server. 

Application tokens generated previously can still be pruned using the `server.InvalidateAPITokens` console command. 

Authentication requirement can be lifted for locally running Dedicated Server instances serving on the loopback network adapter. To allow unrestricted Dedicated Server API access on the localhost, set `FG.DedicatedServer.AllowInsecureLocalAccess` console variable to `1`. It can be performed automatically using the following command line argument: `-ini:Engine:[SystemSettings]:FG.DedicatedServer.AllowInsecureLocalAccess=1`

## HealthCheck

### Summary

Performs a health check on the Dedicated Server API. Allows passing additional data between Modded Dedicated Server and Modded Game Client. This function requires no Authentication. 

### Function Request Data

Function Request Data  Property Name | Property Type | Description   
---|---|---  
ClientCustomData | string | Custom Data passed from the Game Client or Third Party service. Not used by vanilla Dedicated Servers   
  
### Function Response Data

Function Response Data  Property Name | Property Type | Description   
---|---|---  
Health | string | "healthy" if tick rate is above ten ticks per second, "slow" otherwise   
ServerCustomData | string | Custom Data passed from the Dedicated Server to the Game Client or Third Party service. Vanilla Dedicated Server returns empty string   
  
## VerifyAuthentication Token

### Summary

Verifies the Authentication token provided to the Dedicated Server API. Returns No Content if the provided token is valid. This function does not require input parameters and does not return any data. 

  


## PasswordlessLogin

### Summary

Attempts to perform a passwordless login to the Dedicated Server as a player. Passwordless login is possible if the Dedicated Server is not claimed, or if Client Protection Password is not set for the Dedicated Server. This function requires no Authentication. 

### Function Request Data

Function Request Data  Property Name | Property Type | Description   
---|---|---  
MinimumPrivilegeLevel | string | Minimum privilege level to attempt to acquire by logging in. See Privilege Level enum for possible values   
  
### Function Response Data

Function Response Data  Property Name | Property Type | Description   
---|---|---  
authenticationToken | string | Authentication Token in case login is successful   
  
**Community Note** : In the official documentation, the property name is `AuthenticationToken` with an uppercase A, but this is incorrect. The server responds with the property name with a lowercase A. 

### Possible Errors

Possible Errors  Error Code | Description   
---|---  
passwordless_login_not_possible | Passwordless login is not currently possible for this Dedicated Server   
  
## PasswordLogin

### Summary

Attempts to log in to the Dedicated Server as a player using either Admin Password or Client Protection Password. This function requires no Authentication. 

### Function Request Data

Function Request Data  Property Name | Property Type | Description   
---|---|---  
MinimumPrivilegeLevel | string | Minimum privilege level to attempt to acquire by logging in. See Privilege Level enum for possible values   
Password | string | Password to attempt to log in with, in plaintext   
  
### Function Response Data

Function Response Data  Property Name | Property Type | Description   
---|---|---  
AuthenticationToken | string | Authentication Token in case login is successful   
  
### Possible Errors

Possible Errors  Error Code | Description   
---|---  
wrong_password | Provided Password did not match any of the passwords set for this Dedicated Server   
  
  


## QueryServerState

### Summary

Retrieves the current state of the Dedicated Server. Does not require any input parameters. 

### Function Response Data

Function Response Data  Property Name | Property Type | Description   
---|---|---  
ServerGameState | string | Current game state of the server   
  
**Community Note** : It's obviously not a string. Ignore that. Also it's `serverGameState`, with a lowercase 's' 

### ServerGameState

ServerGameState  Property Name | Property Type | Description   
---|---|---  
ActiveSessionName | string | Name of the currently loaded game session   
NumConnectedPlayers | integer | Number of the players currently connected to the Dedicated Server   
PlayerLimit | integer | Maximum number of players that can be connected to the Dedicated Server   
TechTier | integer | Maximum Tech Tier of all Schematics currently unlocked   
ActiveSchematic | string | Schematic currently set as Active Milestone   
GamePhase | string | Current game phase. None if no game is running   
IsGameRunning | boolean | True if the save is currently loaded, false if the server is waiting for the session to be created   
TotalGameDuration | integer | Total time the current save has been loaded, in seconds   
IsGamePaused | boolean | True if the game is paused. If the game is paused, total game duration does not increase   
AverageTickRate | float | Average tick rate of the server, in ticks per second   
AutoLoadSessionName | string | Name of the session that will be loaded when the server starts automatically   
  
### Community Notes

The first letter of all of the keys above for ServerGameState should be lowercase. 

GamePhase  Property Value | Phase Number | Description   
---|---|---  
/Script/FactoryGame.FGGamePhase'/Game/FactoryGame/GamePhases/GP_Project_Assembly_Phase_1.GP_Project_Assembly_Phase_1'  | Phase 1  | Distribution Platform   
/Script/FactoryGame.FGGamePhase'/Game/FactoryGame/GamePhases/GP_Project_Assembly_Phase_2.GP_Project_Assembly_Phase_2' | Phase 2 | Construction Dock   
  
Other phase names probably follow the same format. See [Space_Elevator#Project_Assembly_phases](/wiki/Space_Elevator#Project_Assembly_phases "Space Elevator")

ActiveSchematic  Property Value | Description | Tier   
---|---|---  
/Script/Engine.BlueprintGeneratedClass'/Game/FactoryGame/Schematics/Progression/Schematic_6-7.Schematic_6-7_C' | Railway Signalling | 6   
/Script/Engine.BlueprintGeneratedClass'/Game/FactoryGame/Schematics/Progression/Schematic_7-2.Schematic_7-2_C' | Logistics Mk.5 | 7   
  
## GetServerOptions

### Summary

Retrieves currently applied server options and server options that are still pending application (because of needing session or server restart) Does not require input parameters. 

### Function Response Data

Function Response Data  Property Name | Property Type | Description   
---|---|---  
ServerOptions | map<string, string> | All current server option values. Key is the name of the option, and value is its stringified value   
PendingServerOptions | map<string, string> | Server option values that will be applied when the session or server restarts   
  
## GetAdvancedGameSettings

### Summary

Retrieves currently applied advanced game settings. Does not require input parameters. 

### Function Response Data

Function Response Data  Property Name | Property Type | Description   
---|---|---  
CreativeModeEnabled | boolean | True if Advanced Game Settings are enabled for the currently loaded session   
AdvancedGameSettings | map<string, string> | Values of Advanced Game Settings. Key is the name of the setting, and value is its stringified value   
  
## ApplyAdvancedGameSettings

### Summary

Applies new values to the provided Advanced Game Settings properties. Will automatically enable Advanced Game Settings for the currently loaded save if they are not enabled already. 

### Function Request Data

Function Request Data  Property Name | Property Type | Description   
---|---|---  
AppliedAdvancedGameSettings | map<string, string> | Key is the name of the Advanced Game Setting, and the Value is the new setting value as string   
  
  


## ClaimServer

### Summary

Claims this Dedicated Server if it is not claimed. Requires InitialAdmin privilege level, which can only be acquired by attempting passwordless login while the server does not have an Admin Password set, e.g. it is not claimed yet. Function does not return any data in case of success, and the server is claimed. The client should drop InitialAdmin privileges after that and use returned AuthenticationToken instead, and update it's cached server game state by calling QueryServerState. 

### Function Request Data

Function Request Data  Property Name | Property Type | Description   
---|---|---  
ServerName | string | New name of the Dedicated Server   
AdminPassword | string | Admin Password to set on the Dedicated Server, in plaintext   
  
### Function Response Data

Function Response Data  Property Name | Property Type | Description   
---|---|---  
authenticationToken | string | New Authentication Token that the Caller should use to drop Initial Admin privileges   
  
**Community Note** : In the official documentation, the property name is `AuthenticationToken` with an uppercase A, but this is incorrect. The server responds with the property name with a lowercase A. 

### Possible Errors

Possible Errors  Error Code | Description   
---|---  
server_claimed | Server has already been claimed   
  
## RenameServer

### Summary

Renames the Dedicated Server once it has been claimed. Requires Admin privileges. Function does not return any data on success. 

### Function Request Data

Function Request Data  Property Name | Property Type | Description   
---|---|---  
ServerName | string | New name of the Dedicated Server   
  
### Possible Errors

Possible Errors  Error Code | Description   
---|---  
server_not_claimed | Server has not been claimed yet. Use ClaimServer function instead   
  
## SetClientPassword

### Summary

Updates the currently set Client Protection Password. This will invalidate all previously issued Client authentication tokens. Pass empty string to remove the password, and let anyone join the server as Client. Requres Admin privileges. Function does not return any data on success. 

### Function Request Data

Function Request Data  Property Name | Property Type | Description   
---|---|---  
Password | string | Client Password to set on the Dedicated Server, in plaintext   
  
### Possible Errors

Possible Errors  Error Code | Description   
---|---  
server_not_claimed | Server has not been claimed yet. Use ClaimServer function instead before calling SetClientPassword   
password_in_use | Same password is already used as Admin Password   
  
## SetAdminPassword

### Summary

Updates the currently set Admin Password. This will invalidate all previously issued Client and Admin authentication tokens. Requires Admin privileges. Function does not return any data on success. 

### Function Request Data

Function Request Data  Property Name | Property Type | Description   
---|---|---  
Password | string | Admin Password to set on the Dedicated Server, in plaintext   
AuthenticationToken | string | New Admin authentication token to use, since the token used for this request will become invalidated   
  
### Possible Errors

Possible Errors  Error Code | Description   
---|---  
server_not_claimed | Server has not been claimed yet. Use ClaimServer function instead   
cannot_reset_admin_password | Attempt to set Password to empty string. Admin Password cannot be reset   
password_in_use | Same password is already used as Client Protection Password   
  
## SetAutoLoadSessionName

### Summary

Updates the name of the session that the Dedicated Server will automatically load on startup. Does not change currently loaded session. Requires Admin privileges. Function does not return any data on success. 

### Function Request Data

Function Request Data  Property Name | Property Type | Description   
---|---|---  
SessionName | string | Name of the session to automatically load on Dedicated Server startup   
  
## Run Command

### Summary

Runs the given Console Command on the Dedicated Server, and returns it's output to the Console. Requires Admin privileges. 

### Function Request Data

Function Request Data  Property Name | Property Type | Description   
---|---|---  
Command | string | Command Line to run on the Dedicated Server   
  
### Function Response Data

Function Response Data  Property Name | Property Type | Description   
---|---|---  
CommandResult | string | Output of the command executed, with \n used as line separator   
ReturnValue | boolean | Whether the command executed successfully   
  
## Shutdown

### Summary

Shuts down the Dedicated Server. If automatic restart script is setup, this allows restarting the server to apply new settings or update. Requires Admin privileges. Shutdowns initiated by remote hosts are logged with their IP and their token. Function does not return any data on success, and does not take any parameters. 

## ApplyServerOptions

### Summary

Applies new Server Options to the Dedicated Server. Requires Admin privileges. 

### Function Request Data

Function Request Data  Property Name | Property Type | Description   
---|---|---  
UpdatedServerOptions | map<string, string> | Key is the name of the Server Option, and the Value is the new value as string   
  
## CreateNewGame

### Summary

Creates a new session on the Dedicated Server, and immediately loads it. HTTPS API becomes temporarily unavailable when map loading is in progress | Function does not return any data on success. 

### Function Request Data

Function Request Data  Property Name | Property Type | Description   
---|---|---  
NewGameData | ServerNewGameData | Parameters needed to create new game session   
  
### ServerNewGameData

ServerNewGameData  Property Name | Property Type | Description   
---|---|---  
SessionName | string | Name of the session to create   
MapName | string | Path Name to the Map Package to use as a map. If not specified, default level   
StartingLocation | string | Name of the starting location to use. Leaving it empty will use random starting location   
SkipOnboarding | boolean | Whether the Onboarding should be skipped. Currently, Onboarding is always skipped on the Dedicated Servers   
AdvancedGameSettings | map<string, string> | Advanced Game Settings to apply to the newly created session   
CustomOptionsOnlyForModding | map<string, string> | Custom Options to pass to the newly created session URL. Not used by vanilla Dedicated Servers   
  
##### Note

Currently SkipOnboarding must be set to bSkipOnboarding, due to an issue with the property names. 

## SaveGame

### Summary

Saves the currently loaded session into the new save game file named as the argument. Requires Admin privileges. SaveName might be changed to satisfy file system restrictions on file names. Function does not return any data on success. 

### Function Request Data

Function Request Data  Property Name | Property Type | Description   
---|---|---  
SaveName | string | Name of the save game file to create. Passed name might be sanitized   
  
### Possible Errors

Possible Errors  Error Code | Description   
---|---  
save_game_failed | Failed to save the game. Additional information might be available in errorMessage property   
  
## DeleteSaveFile

### Summary

Deletes the existing save game file from the server. Requires Admin privileges. SaveName might be changed to satisfy file system restrictions on file names. Function does not return any data on success. 

### Function Request Data

Function Request Data  Property Name | Property Type | Description   
---|---|---  
SaveName | string | Name of the save game file to delete. Passed name might be sanitized   
  
### Possible Errors

Possible Errors  Error Code | Description   
---|---  
delete_save_file_failed | Failed to delete the save game file. Additional information might be available in errorMessage property   
  
## DeleteSaveSession

### Summary

Deletes all save files belonging to the specific session name. Requires Admin privileges. SessionName must be a valid session name with at least one saved save game file belonging to it. Function does not return any data on success. 

### Function Request Data

Function Request Data  Property Name | Property Type | Description   
---|---|---  
SessionName | string | Name of the save session to delete   
  
### Possible Errors

Possible Errors  Error Code | Description   
---|---  
session_not_found | Failed to find any save game files belonging to the given session   
delete_save_session_failed | Failed to delete save session files. Additional information might be available in errorMessage property   
  
## EnumerateSessions

### Summary

Enumerates all save game files available on the Dedicated Server. Requires Admin privileges. Function does not require any additional parameters. 

### Function Response Data

Function Response Data  Property Name | Property Type | Description   
---|---|---  
Sessions | array<SessionSaveStruct> | List of sessions available on the Dedicated Server   
CurrentSessionIndex | integer | Index of the currently selected session in the list   
  
### Possible Errors

Possible Errors  Error Code | Description   
---|---  
enumerate_sessions_failed | Failed to enumerate save sessions. Additional information might be available in errorMessage property   
  
### SessionSaveStruct

SessionSaveStruct  Property Name | Property Type | Description   
---|---|---  
SessionName | string | Name of the save session   
SaveHeaders | array<SaveHeader> | All save game files belonging to this session   
  
### SaveHeader

SaveHeader  Property Name | Property Type | Description   
---|---|---  
SaveVersion | integer | Version of the Save Game format this file was saved with   
BuildVersion | integer | Changelist of the game or dedicated server this file was saved by   
SaveName | string | Name of the save game file in the filesystem   
MapName | string | Path to the map package this save game file is based on   
MapOptions | string | Additional Map URL options this save game was saved with   
SessionName | string | Name of the session this save game file belongs to   
PlayDurationSeconds | integer | Amount of seconds the game has been running for in total since the session was created   
SaveDateTime | string | Date and time on which the save game file was saved   
IsModdedSave | boolean | True if this save game file was saved with mods   
IsEditedSave | boolean | True if this save game file has been edited by third party tools   
IsCreativeModeEnabled | boolean | True if Advanced Game Settings are enabled for this save game   
  
## LoadGame

### Summary

Loads the save game file by name, optionally with Advanced Game Settings enabled. Requires Admin privileges. Dedicated Server HTTPS API will become temporarily unavailable when save game is being loaded. Function does not return any data on succcess. 

### Function Request Data

Function Request Data  Property Name | Property Type | Description   
---|---|---  
SaveName | string | Name of the save game file to load   
EnableAdvancedGameSettings | boolean | True if save game file should be loaded with Advanced Game Settings enabled   
  
### Possible Errors

Possible Errors  Error Code | Description   
---|---  
save_game_load_failed | Failed to find the save game file with the given name on the Dedicated Server   
  
## UploadSaveGame

### Summary

Uploads save game file to the Dedicated Server with the given name, and optionally immediately loads it. Requires Admin privileges. If save file is immediately loaded, Dedicated Server HTTPS API will become temporarily unavailable until save game is loaded. This function does not return any data on success. 

This function requires multipart-encoded form data as it's body. The following multipart part names are allowed: 

### Multipart Field

Multipart Field  Multipart Field | Description   
---|---  
data | Standard Request Data body for this request, encoded as utf-8 JSON. Note that this includes the envelope   
saveGameFile | File attachment containing the save game file. Contents of the file will be validated on the server   
  
### Function Request Data

Function Request Data  Property Name | Property Type | Description   
---|---|---  
SaveName | string | Name of the save game file to create on the Dedicated Server   
LoadSaveGame | boolean | True if save game file should be immediately loaded by the Dedicated Server   
EnableAdvancedGameSettings | boolean | True if save game file should be loaded with Advanced Game Settings enabled   
  
### Possible Errors

Possible Errors  Error Code | Description   
---|---  
invalid_save_game | Invalid save game file encoding, malformed header or corrupted contents   
unsupported_save_game | Save game file is too old to be loaded by the Dedicated Server, or is too new   
file_save_failed | Failed to save the save game file to the underlying file system   
save_game_load_failed | Failed to find the created save game file   
  
## DownloadSaveGame

### Summary

Downloads save game with the given name from the Dedicated Server. Requires Admin privileges. This function responds with the file attachment containing the save game file on success, and with normal error response in case of error. 

### Function Request Data

Function Request Data  Property Name | Property Type | Description   
---|---|---  
SaveName | string | Name of the save game file to download from the Dedicated Server   
  
### Possible Errors

Possible Errors  Error Code | Description   
---|---  
file_not_found | Save game file with the provided name is not found on the Dedicated Server   
  
## See also

  * [Dedicated Servers - Main Page](/wiki/Dedicated_servers "Dedicated servers")
  * [Dedicated Servers - Configuration Files](/wiki/Dedicated_servers/Configuration_files "Dedicated servers/Configuration files")
  * [Dedicated Servers - Running as a Service](/wiki/Dedicated_servers/Running_as_a_Service "Dedicated servers/Running as a Service")
  * [Dedicated Servers - Automatic Updates](/wiki/Dedicated_servers/Automatic_updates "Dedicated servers/Automatic updates")


  *[v]: View this template
  *[e]: Edit this template
  *[h]: History of this template
  *[his]: his trivia section
