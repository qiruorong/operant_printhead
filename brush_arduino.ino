
// define enA = 9
// define in1 = 6
// define in2 = 7

void setup() {
  pinMode(enA, OUTPUT);
  pinMode(in1, OUTPUT);
  pinMode(in2, OUTPUT);
  pinMode(button, INPUT);

  Serial.begin(9600);
}

void loop() {
  int potValue = analogRead(A0); // potentiometer
  int motorSpeed = map(potValue, 0, 1023, 0 , 255); 
  analogWrite(enA, motorSpeed); // Send to L298N
  int randomValue = random(2);

    if (randomValue = 0) {
        digitalWrite(in1, HIGH);
        digitalWrite(in2, LOW);
        wheelDirection = 1;

    else {
        digitalWrite(in1, LOW);
        digitalWrite(in2, HIGH);
        
    delay(200);
        }
    }
}








#include <AFMotor.h>

AF_DCMotor motor(1); // channel 1

void setup() {
  motor.setSpeed(100); // 0-255
  randomSeed(analogRead(0)); 
}

void loop() {
  int randomNumber = random(2); 
  if (randomNumber == 0) {
    motor.run(FORWARD);
  } else {
    motor.run(BACKWARD);
  }
  delay(2000);
}
