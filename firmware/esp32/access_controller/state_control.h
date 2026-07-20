// módulo usado para transformar o loop em uma máquina de estados

#ifndef STATE_CONTROL_H
#define STATE_CONTROL_H

enum StateControl
{
    INICIALIZANDO,
    AGUARDANDO_PROVISIONAMENTO,
    CONECTANDO_WIFI,
    AGUARDANDO_CREDENCIAL,
    AUTENTICANDO,
    ACESSO_AUTORIZADO,
    PORTA_ABERTA,
    ACESSO_NEGADO,
    ERRO_DE_COMUNICACAO
};

