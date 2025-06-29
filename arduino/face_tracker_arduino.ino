#include <Servo.h>

// --- Configuration ---
const int PAN_SERVO_PIN = 9;
const int TILT_SERVO_PIN = 10;

const int PAN_MIN_ANGLE = 0;
const int PAN_MAX_ANGLE = 180;
const int PAN_CENTER_ANGLE = 90;

const int TILT_MIN_ANGLE = 45;
const int TILT_MAX_ANGLE = 135;
const int TILT_CENTER_ANGLE = 90;

const int ANGLE_STEP = 2;
const long BAUD_RATE = 9600;

// --- Global Variables ---
Servo panServo;
Servo tiltServo;
int currentPanAngle = PAN_CENTER_ANGLE;
int currentTiltAngle = TILT_CENTER_ANGLE;

// --- Setup Function ---
void setup() {
  Serial.begin(BAUD_RATE);
  Serial.println("Arduino Pan-Tilt Face Tracker Ready.");
  
  panServo.attach(PAN_SERVO_PIN);
  tiltServo.attach(TILT_SERVO_PIN);
  
  panServo.write(currentPanAngle);
  tiltServo.write(currentTiltAngle);
  delay(500);
}

// --- Loop Function ---
void loop() {
  if (Serial.available() > 0) {
    char command = Serial.read();
    
    switch (command) {
      case 'L': currentPanAngle += ANGLE_STEP; break;
      case 'R': currentPanAngle -= ANGLE_STEP; break;
      case 'U': currentTiltAngle += ANGLE_STEP; break;
      case 'D': currentTiltAngle -= ANGLE_STEP; break;
      case 'C': break; // Center - No horizontal movement
      case 'S': break; // Still - No vertical movement
      case 'H': 
        currentPanAngle = PAN_CENTER_ANGLE;
        currentTiltAngle = TILT_CENTER_ANGLE;
        break;
    }
    
    currentPanAngle = constrain(currentPanAngle, PAN_MIN_ANGLE, PAN_MAX_ANGLE);
    currentTiltAngle = constrain(currentTiltAngle, TILT_MIN_ANGLE, TILT_MAX_ANGLE);
    
    panServo.write(currentPanAngle);
    tiltServo.write(currentTiltAngle);
    
    delay(20);
  }
}
