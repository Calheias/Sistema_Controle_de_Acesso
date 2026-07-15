// Módulo de comunicação com o FastAPI

#include <Arduino.h>
#include <WiFi.h>
#include <HTTPClient.h>
#include <ArduinoJson.h>

#include "comunicacao_api.h"
#include "credenciais.h"


bool autenticarAcesso(
    const String &uid,
    int deviceId,
    int doorId
)
{
    Serial.println();
    Serial.println("==============");
    Serial.println("Autenticando...");
    Serial.println("==============");

    HTTPClient http;
    http.begin(API_URL);
    http.addHeader(
    "Content-Type",
    "application/json"
    );

    String json = 
    "{"
    "\"uid\":\"" + uid + "\","
    "\"tipo_credencial\":\"RFID\","
    "\"device_id\":" + String(deviceId) + "," 
    "\"door_id\":" + String(doorId) + 
    "}";

    int httpCode = http.POST(json);
    Serial.print("HTTP: ");
    Serial.println(httpCode);

    if (httpCode != 200)
    {
      Serial.println("Erro na comunicação com a API.");
      http.end();
      return false;
    }

    String resposta = http.getString();
    JsonDocument doc;
    deserializeJson(doc, resposta);
    bool autorizado = doc["autorizado"];
    String motivo = doc["motivo"];
    Serial.println("==============");
    Serial.println(resposta);
    Serial.println("Resultado: ");
    Serial.println(motivo);
    http.end();

    return autorizado;
}