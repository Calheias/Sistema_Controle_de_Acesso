// Define o pino digital conectado ao módulo relé
const int pinoRele = 7;

void setup() {
  // Configura o pino do relé como saída
  pinMode(pinoRele, OUTPUT);
}

void loop() {
  // Liga o relé (o LED acende)
  digitalWrite(pinoRele, HIGH);
  delay(3000); // Aguarda 2 segundos
  
  // Desliga o relé (o LED apaga)
  digitalWrite(pinoRele, LOW);
  delay(3000); // Aguarda 2 segundos
}
