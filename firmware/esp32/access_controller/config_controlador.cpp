#include "config_controlador.h"
#include <Preferences.h>


ConfigControlador config;
Preferences pref;


void carregarConfiguracao()
{
    pref.begin("controller", true);
    config.deviceId = pref.getInt("deviceId", 1);
    config.doorId = pref.getInt("doorId", 1);
    config.nomeDevice = pref.getString("nome", "ESP 32");
    pref.end();
}


void salvarConfiguracao()
{
    pref.begin("controller", false);
    config.deviceId = pref.getInt("deviceId", config.deviceId);
    config.doorId = pref.getInt("doorId", config.doorId);
    config.nomeDevice = pref.getString("nome", config.nomeDevice);
    pref.end();
}
