// Módulo de comunicação com o FastAPI

#include <Arduino.h>
#include <WiFi.h>
#include <HTTPClient.h>
#include <ArduinoJson.h>

#include "comunicacao_api.h"
#include "credenciais.h"
#include "autenticacao.h"


Autenticacao autenticarAcesso(
    const String &uid,
    int deviceId,
    int doorId
)
{
    Serial.println();
    Serial.println("=====================");
    Serial.println("[API] Autenticando...");
    Serial.println("=====================");

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
      Serial.println("[API] Erro na comunicação com a API.");
      http.end();

      Autenticacao resultado;
      resultado.autorizado = false;
      resultado.motivo = "ERRO_API";
      resultado.uid = uid;
      resultado.deviceId = deviceId;
      resultado.doorId = doorId;
      resultado.userId = -1;
      resultado.credentialId = -1;      

      return resultado;
    }

    String resposta = http.getString();
    JsonDocument doc;
    deserializeJson(doc, resposta);

    Autenticacao resultado;
    resultado.autorizado = doc["autorizado"].as<bool>();
    resultado.motivo = doc["motivo"].as<String>();      // ????? tipo MemberProxy -> Versão do ArduinoJson
    resultado.credentialId = doc["credential_id"] | -1;
    resultado.userId = doc["user_id"] | -1;
    resultado.deviceId = doc["device_id"] | deviceId;
    resultado.doorId = doc["door_id"] | doorId;
    resultado.uid = doc["uid"].as<String>();

    Serial.println("==============");
    Serial.println(resposta);
    Serial.println("[API] Resultado: ");
    Serial.println(resultado.motivo);
    http.end();

    return resultado;
}