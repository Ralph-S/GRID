#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>

RF24 radio(7, 8); // CE, CSN pins
const byte address[6] = "00001";

bool handshakeReceived = false;

void setup() {
  Serial.begin(115200);
  radio.begin();
  radio.openReadingPipe(0, address);
  radio.setPALevel(RF24_PA_LOW);
  radio.startListening();
  Serial.println("Receiver ready, waiting for handshake...");
}

void loop() {
  if (Serial.available() > 0) {
    char incomingByte = Serial.read();
    if (incomingByte == '1') {
      handshakeReceived = true;
      Serial.println("Handshake received, starting data transmission...");
    }
  }

  if (handshakeReceived) {
    if (radio.available()) {
      byte data[32];
      while (radio.available()) {
        radio.read(&data, sizeof(data));
        Serial.write(data, sizeof(data)); // Send received data over serial to the PC
      }
    }
  }
}
