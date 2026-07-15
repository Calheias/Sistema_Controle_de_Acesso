// Definindo os pinos do Trigger e Echo
const int pinoTrig = 9;
const int pinoEcho = 11;

void setup() {
  Serial.begin(9600); // Inicializa a comunicação serial
  pinMode(pinoTrig, OUTPUT); // Define o Trig como saída
  pinMode(pinoEcho, INPUT); // Define o Echo como entrada
}

void loop() {
  // Limpa o pino Trig
  digitalWrite(pinoTrig, LOW);
  delayMicroseconds(2);

  // Envia um pulso ultrassônico de 10 microssegundos
  digitalWrite(pinoTrig, HIGH);
  delayMicroseconds(10);
  digitalWrite(pinoTrig, LOW);

  // Lê o tempo de duração do pulso no pino Echo
  long duracao = pulseIn(pinoEcho, HIGH);

  // Calcula a distância: velocidade do som é 340 m/s ou 29 ms por cm
  // Como o som vai e volta, dividimos a distância total por 2
  float distanciaCm = duracao * 0.034 / 2;

  // Imprime a distância no Monitor Serial
  Serial.print("Distancia: ");
  Serial.print(distanciaCm);
  Serial.println(" cm");

  delay(500); // Aguarda meio segundo para a próxima leitura
}