// Código Servo Motor SG90 (Tranca do Controle de Acesso)

#include <Arduino.h>
#include <ESP32Servo.h>

#include "atuador_porta.h"


Servo servoPorta;

// uint8_t -> tipo inteiro de 8 bits (0 a 255)
constexpr uint8_t PINO_SERVO = 18;
constexpr uint8_t POSICAO_FECHADA = 0;
constexpr uint8_t POSICAO_ABERTA = 90;

void iniciarPorta()
{
    servoPorta.attach(PINO_SERVO);

    fecharPorta();

    Serial.println("[PORTA] Servo inicializado.");
}

void abrirPorta()
{
    
    Serial.println("Abrindo porta...");
    servoPorta.write(POSICAO_ABERTA);
    /*
    servoPorta.write(POSICAO_ABERTA);

    Serial.println("Porta aberta.");
    */
}

void fecharPorta()
{
    
    Serial.println("Fechando porta...");
    servoPorta.write(POSICAO_FECHADA);
    /*
    servoPorta.write(POSICAO_FECHADA);

    Serial.println("Porta fechada.");
    */
}