#include <OneWire.h>
#include <DallasTemperature.h>
#define ONE_WIRE_BUS A1
#define trigPin 9 // Pin connected to the sensor's TRIG pin
#define echoPin 10 // Pin connected to the sensor's ECHO pin
const int pirPin = 8; // Replace with the pin connected to the PIR sensor output
const int ledPin = 13; // Replace with the pin connected to the LED 
int pirState = LOW; // Initial state of the PIR sensor
int motionDetected = 0; // Flag to indicate motion detection

int pin7 = 7;//Mq5 digital pin
int sensor = A0;//MQ5 analog pin

int sensorValue =0;
OneWire oneWire(ONE_WIRE_BUS);
DallasTemperature sensors(&oneWire);


long duration; // Variable to store the pulse duration

void setup() {
  // Set trigger pin as output
  pinMode(trigPin, OUTPUT);
  // Set echo pin as input
  pinMode(echoPin, INPUT);
  pinMode(pin7, OUTPUT);//MQ5 gas sensor
  // Open serial communication at 9600 baud rate
  sensors.begin();
  pinMode(pirPin, INPUT); // Set the PIR sensor pin as input
  pinMode(ledPin, OUTPUT); // Set the LED pin as output
  Serial.begin(9600);
  motionDetected = 0; // Initialize motion detection flag
}

void loop() {
  // Trigger the sensor by sending a HIGH pulse for 10 microseconds
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  

  // Measure the pulse duration (time taken for the sound wave to travel)
  duration = pulseIn(echoPin, HIGH);

  // Calculate the distance in centimeters (speed of sound * travel time / 2)
  float distance = duration * 0.034 / 2;

  // Print the distance to the serial monitor
  Serial.print("Distance: ");
  Serial.print(distance);
  Serial.println(" cm");

  // Check if distance is less than 10 cm
  if (distance < 10) {
    Serial.println(" Too close");
  }

  // Wait for 1 second before taking another measurement
  delay(1000);
  sensorValue = analogRead(sensor);
  
  Serial.print(sensorValue, DEC);
  
  if (sensorValue > 500) {
    
    digitalWrite(pin7, HIGH);
    Serial.println(" :Gas detection High ");
  }
  else {
    
    digitalWrite(pin7, LOW);
    Serial.println(" :Gas detection Low ");
  }
   // Call sensors.requestTemperatures() to issue a global temperature request
  sensors.requestTemperatures();

  // Get the temperature in Celsius
  float temperatureC = sensors.getTempCByIndex(0);

  // Print temperature to serial monitor
  Serial.print("Temperature in degrees: ");
  Serial.println(String(temperatureC));
  Serial.println();

  //delay(500); // Adjust delay time as needed
  pirState = digitalRead(pirPin); // Read the PIR sensor state

  if (pirState == HIGH) {
    if (!motionDetected) { // Only print and light the LED once per detection
      Serial.println("Motion detected!"); // Print to serial monitor (optional)
      digitalWrite(ledPin, HIGH); // Turn on the LED (optional)
      motionDetected = 1;
    }
  } else {
    if (motionDetected) { // Only print and turn off the LED once after motion stops
      Serial.println("Motion stopped!"); // Print to serial monitor (optional)
      digitalWrite(ledPin, LOW); // Turn off the LED (optional)
      motionDetected = 0;
    }
  }
  delay(500); // Add a delay to avoid rapid blinking of the LED

}
