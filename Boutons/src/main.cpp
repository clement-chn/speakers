#include <Arduino.h>

#define BTN1 2
#define BTN2 3
#define BTN3 4
#define LED 6

bool ledOn = false;

void setup() {
  Serial.begin(9600);
  pinMode(BTN1, INPUT_PULLUP);
  pinMode(BTN2, INPUT_PULLUP);
  pinMode(BTN3, INPUT_PULLUP);
  pinMode(LED, OUTPUT);
}

void loop() {
  if (digitalRead(BTN1) == LOW) {
    digitalWrite(LED, HIGH);
    Serial.println("LED_ON");
    delay(15000);
    digitalWrite(LED, LOW);
    Serial.println("LED_OFF");
    delay(200);
  }
  if (digitalRead(BTN2) == LOW) {
    digitalWrite(LED, HIGH);
    Serial.println("LED_ON");
    delay(30000);
    digitalWrite(LED, LOW);
    Serial.println("LED_OFF");
    delay(200);
  }
  if (digitalRead(BTN3) == LOW) {
    ledOn = !ledOn;
    digitalWrite(LED, ledOn ? HIGH : LOW);
    Serial.println(ledOn ? "LED_ON" : "LED_OFF");
    delay(200);
  } 
}