#ifndef CONFIG_CONTROLADOR_H
#define CONFIG_CONTROLADOR_H

#include <Arduino.h>

struct ConfigControlador
{
    int deviceId;
    int doorId;
    String nomeDevice;
};

extern ConfigControlador config;

void carregarConfiguracao();
void salvarConfiguracao();

#endif