#include <SoftwareSerial.h>

SoftwareSerial GPS(9, 10); // RX, TX
double baseLat = 0;
double baseLong = 0;
bool baseSet = false;

void setup() {
  Serial.begin(9600);
  GPS.begin(9600);
  Serial.println("Waiting for GPS signal...");
}

void loop() {
  while (GPS.available() < 1);
  String sentence = GPS.readStringUntil('\r');
  sentence.trim();
  if (sentence.startsWith("$GPGGA")) {
    String tokens[15];
    int tokenIndex = 0;
    int startIndex = 0;
    int endIndex = sentence.indexOf(',');
    while (endIndex != -1) {
      tokens[tokenIndex] = sentence.substring(startIndex, endIndex);
      tokenIndex++;
      startIndex = endIndex + 1;
      endIndex = sentence.indexOf(',', startIndex);
    }
    tokens[tokenIndex] = sentence.substring(startIndex);

    String latitude = tokens[2];
    String longitude = tokens[4];

    float latDegrees = latitude.substring(0, 2).toFloat();
    float latMinutes = latitude.substring(2).toFloat();
    float latDecimal = latDegrees + (latMinutes / 60.0);
    float longDegrees = longitude.substring(0, 3).toFloat();
    float longMinutes = longitude.substring(3).toFloat();
    float longDecimal = longDegrees + (longMinutes / 60.0);

    if (!baseSet){
      baseLat = latDecimal;
      baseLong = longDecimal;
      baseSet = true;
      Serial.print("Base Latitude: ");
      Serial.println(baseLat, 6);
      Serial.print("Base Longitude: ");
      Serial.println(baseLong, 6);
    } else {
      Serial.println("Relative poisition");
      double currentLat = latDecimal;
      double currentLong = longDecimal;
      Serial.print("Current Latitude: ");
      Serial.println(latDecimal, 6);
      double deltaLat = currentLat - baseLat;
      double deltaLong = currentLong - baseLong;
      Serial.print("Base Latitude: ");
      Serial.println(deltaLat, 6);
      Serial.print("Base Longitude: ");
      Serial.println(deltaLong, 6);
    }
    
  }
}