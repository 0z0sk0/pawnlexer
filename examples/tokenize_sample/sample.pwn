// Modules
#include <src/systems/features/auth/auth_connect.pwn>
#include <src/systems/features/auth/auth_utils.pwn>
#include "src/systems/features/auth/auth_utils.pwn"


// Callbacks
/*
Multiline
Comments
There
*/
forward auth_OnPlayerConnect(playerid);
public auth_OnPlayerConnect(playerid)
{
    authconnect(playerid);
    new sampleVar = 0.01;
}

native PC_EmulateCommand(playerid, const cmdtext[]);