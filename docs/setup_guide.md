# Setup Guide 📋

## Prerequisites

### Software Requirements
- **Python 3.7+**
- **Arduino IDE**
- **Git** (optional)

### Hardware Requirements
- Arduino Uno/Nano/Pro Mini
- 2x SG90 Servo motors (or similar)
- Pan-tilt camera bracket
- USB Webcam (720p+ recommended)
- USB cable for Arduino
- Jumper wires

## Step 1: Hardware Setup

### 1.1 Assemble Pan-Tilt Bracket
- Assemble the pan-tilt bracket with the two servo motors.
- Mount the webcam on the bracket.

### 1.2 Connect Servos to Arduino
- Follow the [Wiring Diagram](wiring_diagram.md) to connect the servos to the Arduino.

### 1.3 Connect Arduino to Computer
- Use a USB cable to connect the Arduino to your computer.

## Step 2: Arduino Software Setup

### 2.1 Install Arduino IDE
- Download and install the Arduino IDE from the [official website](https://www.arduino.cc/en/software).

### 2.2 Configure Arduino IDE
- In the Arduino IDE, select your board and port from the **Tools** menu.

### 2.3 Upload Arduino Code
- Open the `arduino/face_tracker_arduino.ino` sketch.
- Click the **Upload** button.

## Step 3: Python Environment Setup

### 3.1 Install Python
- If you don't have Python, download and install it from the [official website](https://www.python.org/downloads/).

### 3.2 Install Dependencies
- Open a terminal or command prompt and run:
  ```bash
  pip install -r requirements.txt
  ```

## Step 4: Running the System

### 4.1 Find Your Arduino's Port
- You can find the port in the Arduino IDE under **Tools > Port**.

### 4.2 Run the Script
- Run the following command, replacing `YOUR_ARDUINO_PORT` with your Arduino's serial port:
  ```bash
  python python/face_tracker.py --port YOUR_ARDUINO_PORT
  ```
- To enable the video feed visualization, add the `--visualize` flag:
  ```bash
  python python/face_tracker.py --port YOUR_ARDUINO_PORT --visualize
  ```

## Step 5: Troubleshooting

- **Servo not moving:** Double-check your wiring and make sure the Arduino is powered.
- **Camera not found:** Make sure your webcam is connected and try running the script without the `--visualize` flag.
- **Errors on startup:** Ensure you have installed all the required Python packages.