#include <Arduino.h>

#include "conexao_wifi.h"
#include "comunicacao_api.h"
#include "atuador_porta.h"
#include "leitor_rfid.h"
#include "state_control.h"
#include "autenticacao.h"

StateControl estado = INICIALIZANDO;

void setup()
{
    Serial.begin(115200);

    iniciarWifi();
    iniciarPorta();
    iniciarRFID();
    ;

    Serial.println();
    Serial.println("===============================");
    Serial.println("Controlador de acesso iniciado");
    Serial.println("===============================");

    estado = AGUARDANDO_CREDENCIAL;
}

void loop()
{
    switch (estado)
    {
    case AGUARDANDO_CREDENCIAL:
    {
        if (!cartaoDisponivel())
        {
            Serial.println("Nenhum cartão disponível");
            delay(100);
            return;
        }
        estado = AUTENTICANDO;
        break;
    }

    case AUTENTICANDO:
    {
        Serial.println();
        Serial.println("===============================");
        Serial.println("Nova tentativa de acesso.");
        Serial.println("===============================");

        Serial.println("Cartão detectado!");
        String uid = lerRFID();

        Autenticacao resultado = autenticarAcesso(
            uid,
            1,
            1);
        Serial.println();
        Serial.println("===============================");
        Serial.println("[API] Resultado da Autenticação");
        Serial.println("===============================");
        Serial.println();

        Serial.print("Autorizado: ");
        Serial.println(resultado.autorizado);
        Serial.print("Motivo: ");
        Serial.println(resultado.motivo);
        Serial.print("UID: ");
        Serial.println(resultado.uid);
        Serial.print("Usuário: ");
        Serial.println(resultado.userId);
        Serial.print("Credencial: ");
        Serial.println(resultado.credentialId);
        Serial.println("=====================================");

        if (resultado.autorizado)
        {
            estado = ACESSO_AUTORIZADO;
        }
        else
        {
            estado = ACESSO_NEGADO;
        }
        break;
    }

    case ACESSO_AUTORIZADO:
    {
        Serial.println("ACESSO AUTORIZADO");
        abrirPorta();
        delay(2000);
        fecharPorta();
        estado = AGUARDANDO_CREDENCIAL;
        break;
    }

    case ACESSO_NEGADO:
    {
        Serial.println("ACESSO NEGADO");
        estado = AGUARDANDO_CREDENCIAL;
        break;
    }

    default:
        break;
    }
}