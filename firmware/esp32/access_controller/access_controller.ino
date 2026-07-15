#include <Arduino.h>

#include "conexao_wifi.h"
#include "comunicacao_api.h"


void setup()
{
    Serial.begin(115200);
    
    iniciarWifi();

    Serial.println();
    Serial.println("==============================");
    Serial.println("Controlador de acesso iniciado");
    Serial.println("==============================");

    autenticarAcesso(
        "ABC12345",
        1,
        1
    );
}

void loop()
{
    // Futuramente:
    // verificarConexao();
    // verificarRFID();
    // verificarTouch();
    // autenticarAcesso();
}