#include <Arduino.h>

#include "controller.h"


void setup()
{
    Serial.begin(115200);
    
    iniciarControlador();
}

void loop()
{
    executarControlador();
}