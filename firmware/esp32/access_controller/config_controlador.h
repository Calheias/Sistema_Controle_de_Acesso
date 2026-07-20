#ifndef CONFIG_CONTROLADOR_H
#define CONFIG_CONTROLADOR_H

#include <Arduino.h>

struct ConfigControlador
{
    int deviceId;
    int doorId;
    String nomeDevice;
    uint16_t tempoAberturaMs;  // tipo inteiro para 2 bytes (vai até 65 segundos)
};

extern ConfigControlador config;

void carregarConfiguracao();
void salvarConfiguracao();
void configurarPadrao();
void imprimirConfiguracao();

#endif