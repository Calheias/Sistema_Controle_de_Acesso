#ifndef AUTENTICACAO_H
#define AUTENTICACAO_H

#include <Arduino.h>


struct Autenticacao
{
    bool autorizado;
    String motivo;
    int credentialId;
    int userId;
    int deviceId;
    int doorId;
    String uid;
};

#endif