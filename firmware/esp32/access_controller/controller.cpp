#include <Arduino.h>
#include <WiFi.h>

#include "controller.h"
#include "conexao_wifi.h"
#include "comunicacao_api.h"
#include "atuador_porta.h"
#include "leitor_rfid.h"
#include "state_control.h"
#include "autenticacao.h"
#include "feedback.h"
#include "config_controlador.h"


StateControl estado = INICIALIZANDO;
unsigned long tempoAbertura = 0;

void iniciarControlador()
{ 
    delay(2000);
    carregarConfiguracao();

    if (config.deviceId == 0 && config.nomeDevice.isEmpty())
    {
        configurarPadrao();
        salvarConfiguracao();
    }
    
    iniciarPorta();
    iniciarRFID();

    imprimirConfiguracao();

    if (config.deviceId == 0)
    {    
        estado = AGUARDANDO_PROVISIONAMENTO;
    }else{
        estado = CONECTANDO_WIFI;
    }
}

void executarControlador()
{
    if (WiFi.status() != WL_CONNECTED && estado != CONECTANDO_WIFI &&
    estado != AGUARDANDO_PROVISIONAMENTO)
    {
        Serial.println();
        Serial.println("================================");
        Serial.println("Wi-Fi desconectado!");
        Serial.println("================================");    

        estado = CONECTANDO_WIFI;
    } 
    switch (estado)
    {
        case AGUARDANDO_PROVISIONAMENTO:
        {
            Serial.println();
            Serial.println("================================");
            Serial.println("CONTROLADOR NAO CONFIGURADO");
            Serial.println("Aguardando provisionamento...");
            Serial.println("================================");

            delay(5000);
            break;
        }
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
                config.deviceId,
                config.doorId
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
            abrirPorta();
            tempoAbertura = millis();
            estado = PORTA_ABERTA;
            Serial.println("[STATE] PORTA_ABERTA");
            break;
        }

        case PORTA_ABERTA:
        {
            if (millis() - tempoAbertura >= config.tempoAberturaMs)
            {
                fecharPorta();
                estado = AGUARDANDO_CREDENCIAL;
            }
            break;
        }

        case ACESSO_NEGADO:
        {
            Serial.println("ACESSO NEGADO");
            estado = AGUARDANDO_CREDENCIAL;
            Serial.println("[STATE] AGUARDANDO_CREDENCIAL");
            delay(2000);
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