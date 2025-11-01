# Dedicated servers/Lightweight Query API

This page is a copy of the Lightweight Query API section of the `DedicatedServerAPIDocs.md` document distributed to every player, with some community notes and edits. 

For a list of community tools, see [Dedicated_servers#Community_Tools](/wiki/Dedicated_servers#Community_Tools "Dedicated servers"). 

* * *

Lightweight Query API is a lightweight API designed to allow continuously pulling data from the server and track server state changes. 

## Contents

  * 1 Introduction and Flow
  * 2 Protocol
    * 2.1 Poll Server State
    * 2.2 Server State
    * 2.3 Server State Enum
    * 2.4 Server Flags Bits
    * 2.5 Server Sub States
  * 3 Flow
  * 4 API Availability



# Introduction and Flow

The Lightweight query API as the name implies is a low CPU usage request to the server to obtain basic information about the state of the server. This response can be used to determine if a call to the TCP API is necessary. The client will send a message of type _PollServerState_ to the Lightweight API with a unique identifier (cookie). When the server receives the message, it will send the _ServerStateResponce_ message to the relevant client with the previously provided unique identifier and basic status information in the response. The response form the server contains **SubStates** that can be used to determine if any changes to the the State of the game (tier progress, active players, Game Phase, etc), if game options have changed, or if a new save has been made. Checking with the Lightweight API prior to a call to the much more CPU demanding TCP API is highly recommended. 

# Protocol

Lightweight Query is a simple request-response UDP protocol with a message-based approach. 

Note that all data used in the Lightweight Query API is always _Little Endian_ , and not of network byte order. 

Since the protocol is UDP, it is unreliable, which means some of the requests might be dropped or not receive responses, so instead 

of waiting for the responses you should attempt to ping the server with a specific time interval. 

Be wary of not trying to ping a dead Lightweight Query API for too long though, since you might end up triggering anti-DDoS measures on the host network. 

The protocol consists of a simple message envelope format used for all messages: 

Offset (bytes)  | Data Type  | Name  | Description   
---|---|---|---  
0  | uint16 (LE)  | ProtocolMagic  | Always set to 0xF6D5   
2  | uint8  | MessageType  | Type ID of the payload in this envelope. See table down for details   
3  | uint8  | ProtocolVersion  | Version of the protocol desired by the client. Current protocol version is _1_  
…  | Variant  | Payload  | Payload of the message. Specific to the message type.   
3+sizeof(Payload)  | uint8  | Terminator Byte  | Always 0x1. Messages not ending with the terminator byte will be discarded.   
  
The following message types are currently supported. 

Message Type  | Name  | Description   
---|---|---  
0  | Poll Server State  | A request sent to the API to retrieve the information about the current server state   
1  | Server State Response  | A response sent by the server API back to the client containing the current state of the server   
  
## Poll Server State

Offset (bytes)  | Data Type  | Name  | Description   
---|---|---|---  
0 | uint64 (LE) | Cookie | An unique identifier for this request to mark the response. Game Client uses current time in UE ticks   
  
## Server State

Offset (bytes)  | Data Type  | Name  | Description   
---|---|---|---  
0  | uint64 (LE)  | Cookie  | An unique identifier for the request that triggered this response.   
8  | uint8  | ServerState  | Current state that the server is in. See Server States table for details.   
9  | uint32 (LE)  | ServerNetCL  | Game Changelist that the server is running. Changelist of the server must match the game client changelist for the client to be able to connect   
13  | uint64 (LE)  | ServerFlags  | Flags describing this server. Most values are reserved or available for modded servers to use. See Server Flags for more information   
21  | uint8  | NumSubStates  | Number of Sub State entries in this response. Sub state entries can be used to detect changes in server state   
22  | ServerSubState[]  | SubStates  | Sub state at index i. Number of sub states matches the value of NumSubStates   
22+sizeof(SubStates)  | uint16 (LE)  | ServerNameLength  | Length of the ServerName field in bytes   
22+sizeof(SubStates)+1  | uint8[]  | ServerName  | UTF-8 encoded Server Name, as set by the player   
  
Server Sub State is a sequential counter that is incremented by the server each time a state of the relevant system changes. 

This allows determining a set of data that the API client needs to refresh when the server changes it, without having to continuously poll the HTTPS API. 

ServerSubState structure is defined as following: 

Offset (bytes)  | Data Type  | Name  | Description   
---|---|---|---  
0 | uint8 | SubStateId | ID of the sub state being changed. See Server Sub States for list of values   
8 | uint16 (LE) | SubStateVersion | Current changelist of the sub state   
  
## Server State Enum

Enum Value  | Enum Name  | Description   
---|---|---  
0 | Offline | The server is offline. Servers will never send this as a response   
1 | Idle | The server is running, but no save is currently loaded   
2 | Loading | The server is currently loading a map. In this state, HTTPS API is unavailable   
3 | Playing | The server is running, and a save is loaded. Server is joinable by players   
  
## Server Flags Bits

Bit Index (LE)  | Flag Name  | Description   
---|---|---  
0  | Modded  | The server is considered Modded. Vanilla clients will not try to connect to Modded servers   
1 | Custom1 | A flag with server-specific or context-specific meaning   
2 | Custom2 | A flag with server-specific or context-specific meaning   
3 | Custom3 | A flag with server-specific or context-specific meaning   
4 | Custom4 | A flag with server-specific or context-specific meaning   
  
## Server Sub States

The following sub states are currently defined by the vanilla dedicated server. 

Sub states that are not known are not invalid, and should instead be silently discarded. 

Sub State ID  | Sub State Name  | Description   
---|---|---  
0 | ServerGameState | Game state of the server. Maps to QueryServerState HTTPS API function   
1 | ServerOptions | Global options set on the server. Maps to GetServerOptions HTTPS API function   
2 | AdvancedGameSettings | Advanced Game Settings in the currently loaded session. Maps to GetAdvancedGameSettings HTTPS API function   
3 | SaveCollection | List of saves available on the server for loading/downloading has changed. Maps to EnumerateSessions HTTPS API function   
4 | Custom1 | A value that can be used by the mods or custom servers. Not used by the vanilla clients or servers   
5 | Custom2 | A value that can be used by the mods or custom servers. Not used by the vanilla clients or servers   
6 | Custom3 | A value that can be used by the mods or custom servers. Not used by the vanilla clients or servers   
7 | Custom4 | A value that can be used by the mods or custom servers. Not used by the vanilla clients or servers   
  
# Flow

A client sends a message of type Poll Server State to the Server API with it’s Cookie. When the server receives the message, it will send the 

Server State Response message to the relevant client, with the Cookie value on the response copied from the received request. 

A client can continuously poll the server for the updates using that API without using much of server CPU, and investigate the changes 

in the Server Sub States changelists to determine which subset of information it has cached locally from the HTTPS API could need to be re-fetched from the server. 

# API Availability

Lightweight Server Query API is available at all times when the server is running, except for when it is starting up. When the server is performing 

a save game load or a map change, the lightweight query API will retain it’s availability, but will report Loading as the server status. 

In that state, HTTPS API becomes temporarily unavailable until the blocking work on the server is finished. 
  *[v]: View this template
  *[e]: Edit this template
  *[h]: History of this template
  *[his]: his trivia section
