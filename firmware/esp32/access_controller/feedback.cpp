#include <Arduino.h>
#include "feedback.h"

void resultadoAutenticacao(
    const Autenticacao& resultado
)

{    
    Serial.println();
    Serial.println("================================");
    Serial.println("[API] Resultado da Autenticação");
    Serial.println("================================");
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
    Serial.println("================================");
}