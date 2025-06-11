#include <Servo.h>

// --- Configuration ---
const int PAN_SERVO_PIN = 9;  // Connect Pan servo signal wire to Arduino pin 9

// Define servo movement limits (full range)
const int PAN_MIN_ANGLE = 0;
const int PAN_MAX_ANGLE = 180;
const int PAN_CENTER_ANGLE = 90;

// Define how much the servo moves per command step
const int ANGLE_STEP = 2; // Degrees to move per step

// Serial communication baud rate (must match Python script)
const long BAUD_RATE = 9600;

// --- Global Variables ---
Servo panServo;
int currentPanAngle = PAN_CENTER_ANGLE;

// --- Setup Function ---
void setup() {
  Serial.begin(BAUD_RATE);
  Serial.println("Arduino Face Tracker (0-180 Range) Ready.");
  
  panServo.attach(PAN_SERVO_PIN);
  panServo.write(currentPanAngle);
  delay(500); // Give servo time to reach initial position
}

// --- Loop Function ---
void loop() {
  if (Serial.available() > 0) {
    char command = Serial.read();
    
    switch (command) {
      case 'L': // Move Left (increase pan angle)
        currentPanAngle += ANGLE_STEP;
        break;
        
      case 'R': // Move Right (decrease pan angle)
        currentPanAngle -= ANGLE_STEP;
        break;
        
      case 'C': // Center (No Move)
        // Stay put - no movement
        break;
        
      case 'H': // Home position (center servo)
        currentPanAngle = PAN_CENTER_ANGLE;
        break;
        
      default:
        // Ignore unknown commands
        break;
    }
    
    // Constrain angle to full range limits (0-180)
    currentPanAngle = constrain(currentPanAngle, PAN_MIN_ANGLE, PAN_MAX_ANGLE);
    
    // Write new angle to servo
    panServo.write(currentPanAngle);
    
    
    delay(20); 
  }
}