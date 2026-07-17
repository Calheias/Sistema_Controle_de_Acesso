// módulo usado para transformar o loop em uma máquina de estados

#ifndef ESTADO_CONTROLADOR_H
#define ESTADO_CONTROLADOR_H

enum StateControl
{
    INICIALIZANDO,
    AGUARDANDO_CREDENCIAL,
    AUTENTICANDO,
    ACESSO_AUTORIZADO,
    ACESSO_NEGADO
};

#endif