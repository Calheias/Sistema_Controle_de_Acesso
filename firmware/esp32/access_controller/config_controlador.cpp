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
    config.tempoAberturaMs = pref.getUShort("tempo", 2000);  // getUShort por conta do tipo uint16_t (2 bytes)
    pref.end();
}


void salvarConfiguracao()
{
    pref.begin("controller", false);
    pref.putInt("deviceId", config.deviceId);
    pref.putInt("doorId", config.doorId);
    pref.putString("nome", config.nomeDevice);
    pref.putUShort("tempo", config.tempoAberturaMs);
    pref.end();
}


void configurarPadrao()
{
    config.deviceId = 0;
    config.doorId = 0;
    config.nomeDevice = "NAO_CONFIGURADO";
    config.tempoAberturaMs = 2000;
}


void imprimirConfiguracao()
{
    Serial.println();
    Serial.println("================================");
    Serial.println("CONTROLADOR INICIADO");
    Serial.print("Nome: ");
    Serial.println(config.nomeDevice);
    Serial.print("device_ID: ");
    Serial.println(config.deviceId);
    Serial.print("door_ID: ");
    Serial.println(config.doorId);
    Serial.print("Tempo Porta: ");
    Serial.print(config.tempoAberturaMs);
    Serial.println(" ms");
    Serial.println("================================");
}
