const int PinLED = 13;
const int PinAnalog = A1;
int ByteLido;
float Valor = 0;
int ValSensor = 0;

void setup() {
  // Inicializa a COM Serial
  Serial.begin(115200);
  // Define o LED como saida
  pinMode(PinLED, OUTPUT);
}

void loop() {
  // Olha se tem dado na porta serial
  if (Serial.available()>0){
    // Le o byte na porta Serial
    ByteLido = Serial.read();
    if (ByteLido == 'H'){
      digitalWrite(PinLED, HIGH);
      }
    if (ByteLido == 'L'){
      digitalWrite(PinLED, LOW);
      }
    if (ByteLido == 'S'){
      Valor = analogRead(PinAnalog);
      Serial.println(Valor);
      }
    
    }
}
