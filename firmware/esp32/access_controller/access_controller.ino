#include <Arduino.h>

#include "conexao_wifi.h"
#include "comunicacao_api.h"
#include "atuador_porta.h"
#include "leitor_credencial.h"


void setup()
{
    Serial.begin(115200);
    
    iniciarWifi();
    iniciarPorta();
    iniciarLeitor();

    // uid = RFID.readUID();
    

    Serial.println();
    Serial.println("==============================");
    Serial.println("Controlador de acesso iniciado");
    Serial.println("==============================");
}

void loop()
{
    Serial.println();
    Serial.println("=================================");
    Serial.println("Nova tentativa de acesso iniciado");
    Serial.println("=================================");

    String uid = lerCredencial(); 
    
    bool autorizado = autenticarAcesso(
        uid,
        1,
        1
    );

    if (autorizado)
    {
        abrirPorta();
        delay(2000);
        fecharPorta();
    }else{
        Serial.println("Acesso Negado.");
    }

    delay(5000);

    // Futuramente:
    // verificarConexao();
    // verificarRFID();
    // verificarTouch();
    // autenticarAcesso();
}