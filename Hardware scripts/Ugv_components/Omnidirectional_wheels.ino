// Include the necessary libraries
#include <AFMotor.h>

// Define motor pins
#define MOTOR1_IN1 2
#define MOTOR1_IN2 3
#define MOTOR2_IN3 4
#define MOTOR2_IN4 5
#define MOTOR3_IN1 6
#define MOTOR3_IN2 7
#define MOTOR4_IN3 8
#define MOTOR4_IN4 9

// Create motor objects
AF_DCMotor motor1(1);
AF_DCMotor motor2(2);
AF_DCMotor motor3(3);
AF_DCMotor motor4(4);

void setup() {
  // Set motor control pins as outputs
  pinMode(MOTOR1_IN1, OUTPUT);
  pinMode(MOTOR1_IN2, OUTPUT);
  pinMode(MOTOR2_IN3, OUTPUT);
  pinMode(MOTOR2_IN4, OUTPUT);
  pinMode(MOTOR3_IN1, OUTPUT);
  pinMode(MOTOR3_IN2, OUTPUT);
  pinMode(MOTOR4_IN3, OUTPUT);
  pinMode(MOTOR4_IN4, OUTPUT);
}

// Function to move the robot in different directions
void moveRobot(int speed1, int speed2, int speed3, int speed4) {
  // Set motor speeds
  motor1.setSpeed(speed1);
  motor2.setSpeed(speed2);
  motor3.setSpeed(speed3);
  motor4.setSpeed(speed4);

  // Move the robot
  motor1.run(FORWARD);
  motor2.run(BACKWARD);
  motor3.run(FORWARD);
  motor4.run(BACKWARD);
}

void loop() {
  // Move forward
  moveRobot(255, 255, 255, 255);
  delay(2000); // Adjust the delay according to your robot's speed and size

  // Move backward
  moveRobot(-255, -255, -255, -255);
  delay(2000);

  // Move left
  moveRobot(255, -255, 255, -255);
  delay(2000);

  // Move right
  moveRobot(-255, 255, -255, 255);
  delay(2000);

  // Stop
  moveRobot(0, 0, 0, 0);
  delay(2000);
}
