
// CNC Shield Stepper  Control Demo
// Superb Tech
// www.youtube.com/superbtech

const int StepX = 2;
const int DirX = 5;
const int StepY = 3;
const int DirY = 6;
const int StepZ = 4;
const int DirZ = 7;


void setup() {
  pinMode(StepX,OUTPUT);
  pinMode(DirX,OUTPUT);
  pinMode(StepY,OUTPUT);
  pinMode(DirY,OUTPUT);
  pinMode(StepZ,OUTPUT);
  pinMode( DirZ,OUTPUT);

}

void loop() {
 digitalWrite(DirX, HIGH); // set direction, HIGH for clockwise, LOW for anticlockwise
 digitalWrite(DirY, HIGH);
 
 for(int x = 0; x<1000; x++) { // loop for 200 steps
  digitalWrite(StepX,HIGH);
  delayMicroseconds(500);
  digitalWrite(StepX,LOW); 
  delayMicroseconds(500);
 }
delay(500); // delay for 1 second

for(int x = 0; x<1000; x++) { // loop for 200 steps
  digitalWrite(StepY,HIGH);
  delayMicroseconds(500);
  digitalWrite(StepY,LOW); 
  delayMicroseconds(500);
 }
delay(500); // delay for 1 second

//Reverse directions

digitalWrite(DirX, LOW);
digitalWrite(DirY, LOW);

 for(int x = 0; x<1000; x++) { // loop for 200 steps
  digitalWrite(StepX,HIGH);
  delayMicroseconds(500);
  digitalWrite(StepX,LOW); 
  delayMicroseconds(500);
 }
delay(500); // delay for 1 second

for(int x = 0; x<1000; x++) { // loop for 200 steps
  digitalWrite(StepY,HIGH);
  delayMicroseconds(500);
  digitalWrite(StepY,LOW); 
  delayMicroseconds(500);
 }
delay(500); // delay for 1 second

}
