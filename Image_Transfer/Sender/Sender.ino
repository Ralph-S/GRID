#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>

RF24 radio(7, 8); // CE, CSN pins
const byte address[6] = "00001";

void setup() {
  Serial.begin(115200);
  while (!Serial); // Wait for Serial connection to become ready
  radio.begin();
  radio.openWritingPipe(address);
  radio.setPALevel(RF24_PA_LOW);
  radio.stopListening();
  Serial.println("Sender ready");
}

void loop() {
  if (Serial.available() > 0) {
    byte data[32];
    int index = 0;
    while (index < 32 && Serial.available()) {
      data[index] = Serial.read();
      index++;
    }
    Serial.print("Received data: ");
    Serial.write(data, index); // Display received data
    Serial.println();
    
    // Send the chunk
    bool report = radio.write(&data, index);
    Serial.print("Sending packet... ");
    if (report) {
      Serial.println("Success");
    } else {
      Serial.println("Failed");
    }
  }
}

