#include <Arduino.h>
#include <WiFi.h>

#include "conexao_wifi.h"
#include "comunicacao_api.h"
#include "atuador_porta.h"
#include "leitor_rfid.h"
#include "state_control.h"
#include "autenticacao.h"
#include "feedback.h"
#include "config_controlador.h"


StateControl estado = INICIALIZANDO;

void setup()
{
    Serial.begin(115200);
    iniciarPorta();
    iniciarRFID();

    Serial.println();
    Serial.println("================================");
    Serial.println("CONTROLADOR INICIADO");
    Serial.print("Nome: ");
    Serial.println(NOME_CONTROLADOR);
    Serial.print("Device ID: ");
    Serial.println(DEVICE_ID);
    Serial.print("Door ID: ");
    Serial.println(DOOR_ID);
    Serial.println("================================");
        
    estado = CONECTANDO_WIFI;
}

void loop()
{
    if (WiFi.status() != WL_CONNECTED && estado != CONECTANDO_WIFI)
    {
        Serial.println();
        Serial.println("================================");
        Serial.println("Wi-Fi desconectado!");
        Serial.println("================================");    

        estado = CONECTANDO_WIFI;
    } 
    switch (estado)
    {
        case CONECTANDO_WIFI:
        {
            Serial.println("[WIFI] Tentando conexão....");
            iniciarWifi();
            if (WiFi.status() == WL_CONNECTED)
            {
                Serial.println("[WIFI] Conectado!");
                estado = AGUARDANDO_CREDENCIAL;
            }
            delay(1000);
            break;
        }
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
            Serial.println("================================");
            Serial.println("Nova tentativa de acesso.");
            Serial.println("================================");

            Serial.println("Cartão detectado!");
            String uid = lerRFID();

            Autenticacao resultado = autenticarAcesso(
                uid,
                DEVICE_ID,
                DOOR_ID
            );

            resultadoAutenticacao(resultado);

            if (resultado.motivo == "ERRO_API")
            {
                estado = ERRO_DE_COMUNICACAO;
            }
            else if (resultado.autorizado)
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
            Serial.println("================================");
            Serial.println("ACESSO AUTORIZADO");
            Serial.println("================================");
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

        case ERRO_DE_COMUNICACAO:
        {
            Serial.println();
            Serial.println("[API] Erro de Comunicação!");
            Serial.println("  Sem acesso ao Servidor");
            delay(2000);
            estado = CONECTANDO_WIFI;
            break;            
        }

        default:
            break;
    }
}