#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>

RF24 radio(7, 8); // CE, CSN
const byte address[6] = "00001";

void setup() {
  Serial.begin(9600);
  radio.begin();
  radio.openWritingPipe(address);
  radio.setPALevel(RF24_PA_LOW); // Set the power amplifier level to low to prevent issues at close range
  radio.stopListening();
}

void loop() {
  const char text[] = "HOW YOU DOIN"; // Message must be less than 32 characters
  Serial.println("Sending message...");
  bool success = radio.write(&text, sizeof(text)); // Send the message

  if (success) {
    Serial.println("Message sent successfully");
  } else {
    Serial.println("Message failed to send");
  }
  delay(1000);
}
