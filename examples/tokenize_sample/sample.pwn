// Modules
#include <src/systems/features/auth/auth_connect.pwn>
#include <src/systems/features/auth/auth_utils.pwn>
#include "src/systems/features/auth/auth_utils.pwn"


// Callbacks
public auth_OnPlayerConnect(playerid)
{
    authconnect(playerid);
}