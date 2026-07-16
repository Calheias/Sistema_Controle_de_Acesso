#ifndef LEITOR_RFID_H
#define LEITOR_RFID_H

#include <Arduino.h>

void iniciarRFID();
bool cartaoDisponivel();
String lerRFID();

#endif