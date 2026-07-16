#ifndef COMUNICACAO_API_H
#define COMUNICACAO_API_H

#include <Arduino.h>
#include "autenticacao.h"


Autenticacao autenticarAcesso(
    const String& uid,
    int deviceId,
    int doorId
);

#endif