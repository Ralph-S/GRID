#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>

RF24 radio(7, 8); // CE, CSN
const byte address[6] = "00001";

void setup() {
  Serial.begin(9600);
  radio.begin();
  radio.openReadingPipe(0, address);
  radio.setPALevel(RF24_PA_LOW); // Match the power level to the sender
  radio.startListening();
}

void loop() {
  if (radio.available()) {
    char text[32] = ""; // Ensure this is large enough for the incoming message
    radio.read(&text, sizeof(text));
    Serial.println(text); // Print the received message to the serial monitor
  } else {
    Serial.println("No radio available.");
  }
  delay(1000);
}
