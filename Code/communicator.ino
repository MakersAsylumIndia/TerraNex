const int moisturePin = A0;  

void setup() {
  Serial.begin(9600);
}

void loop() {
  int moistureValue = analogRead(moisturePin);
  Serial.println(moistureValue);
  delay(1000); 
}
