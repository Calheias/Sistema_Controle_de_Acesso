// Código de conexão com o módulo wifi da ESP 

#include <Arduino.h>
#include <WiFi.h>

#include "conexao_wifi.h"
#include "credenciais.h"


void iniciarWifi()
{
    Serial.println();
    Serial.println("=============================");
    Serial.println("[WIFI] Conectando ao Wi-Fi...");
    Serial.println("=============================");

    WiFi.mode(WIFI_STA);
    WiFi.begin(WIFI_SSID, WIFI_PASSWORD);

    while (WiFi.status() != WL_CONNECTED)
    {
        delay(500);
        Serial.print(".");
    }

    Serial.println(WiFi.localIP());

    IPAddress pc(192,168,1,33);

    Serial.print("Ping PC: ");
    Serial.println(WiFi.hostByName("192.168.1.33", pc));

    Serial.println();
    Serial.print("IP: ");
    Serial.println(WiFi.localIP());
    Serial.print("Gateway: ");
    Serial.println(WiFi.gatewayIP());

    Serial.print("Subnet: ");
    Serial.println(WiFi.subnetMask());

    Serial.print("DNS: ");
    Serial.println(WiFi.dnsIP());
}

bool wifiConectado()
{
    return WiFi.status() == WL_CONNECTED;
}