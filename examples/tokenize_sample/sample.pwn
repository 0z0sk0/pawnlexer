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

    new x = 3;
    x = x >> 1;
    x = x << 2;
    x <<= 2;
    x >>= 3;
    x = ~x;
    x = x | 7;
    x |= 7;
    x = x & 12;
    x &= 12;
    x = x ^ 6;
    x ^= 6;
}

native PC_EmulateCommand(playerid, const cmdtext[]);