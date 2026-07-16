#include <Arduino.h>

#include "leitor_rfid.h"

void iniciarRFID()
{
  Serial.println("[RFID] Leitor iniciando.......");
}

bool cartaoDisponivel()
{
  // Simulando -> sempre existe um cartão disponível
  return true;
  // futuramente return mfrc522.PICC_IsNewCardPresent();
}

String lerRFID()
{
  // Simulando a leitura do módulo rfid
  return "ABC12345";
}
