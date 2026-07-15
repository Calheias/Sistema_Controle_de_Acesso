#include <SPI.h>
#include <MFRC522.h>

// ==============================
// Configuração dos pinos
// ==============================

constexpr byte SS_PIN  = 10;
constexpr byte RST_PIN = 9;

// ==============================
// Objeto do leitor RFID
// ==============================

MFRC522 rfid(SS_PIN, RST_PIN);

// ==============================
// Protótipos das funções
// ==============================

void iniciarSerial();
void iniciarRFID();
void imprimirMensagemInicial();
void verificarCartao();
void imprimirUID();

// ==============================

void setup()
{
    iniciarSerial();
    iniciarRFID();
    imprimirMensagemInicial();
}

void loop()
{
    verificarCartao();
}

// ==============================

void iniciarSerial()
{
    Serial.begin(9600);

    while (!Serial);

    Serial.println();
    Serial.println("==============================");
    Serial.println("Sistema RFID iniciado");
    Serial.println("==============================");
}

// void iniciarRFID()
// {
//     SPI.begin();
//     rfid.PCD_Init();
// }

void iniciarRFID()
{
    Serial.println("Iniciando SPI...");

    SPI.begin();

    Serial.println("Inicializando RC522...");

    rfid.PCD_Init();

    Serial.println("RC522 inicializado.");
}

void imprimirMensagemInicial()
{
    Serial.println("Aproxime um cartao...");
    Serial.println();
}

void verificarCartao()
{
    
    if (!rfid.PICC_IsNewCardPresent())
        return;

    if (!rfid.PICC_ReadCardSerial())
        return;

    imprimirUID();

    rfid.PICC_HaltA();
    delay(1000);
}

void imprimirUID()
{
    Serial.print("UID: ");

    for (byte i = 0; i < rfid.uid.size; i++)
    {
        if (rfid.uid.uidByte[i] < 0x10)
            Serial.print("0");

        Serial.print(rfid.uid.uidByte[i], HEX);
    }

    Serial.println();
}