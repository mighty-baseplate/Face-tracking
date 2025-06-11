# Setup Guide 📋

---

## Prerequisites

### Software Requirements

- **Python 3.7+** – [Download Python](https://www.python.org/downloads/)  
- **Arduino IDE** – [Download Arduino IDE](https://www.arduino.cc/en/software)  
- **Git** (optional) – [Download Git](https://git-scm.com/)

### Hardware Requirements

- Arduino Uno / Nano / Pro Mini  
- SG90 Servo Motor (or similar)  
- USB Webcam (720p+ recommended)  
- USB cable for Arduino  
- 3x Jumper wires  

---

## Step 1: Hardware Setup

### 1.1 Connect Servo to Arduino

Refer to the wiring diagram.

- **Servo Signal (Orange)** → **Arduino Pin 9**  
- **Servo Power (Red)** → **Arduino 5V**  
- **Servo Ground (Brown)** → **Arduino GND**  

### 1.2 Connect Arduino to Computer

- Use a USB cable to connect Arduino to your computer  
- Note the **COM port** (Windows) or **device path** (Mac/Linux)  

---

## Step 2: Arduino Software Setup

### 2.1 Install Arduino IDE

- Download from [arduino.cc](https://www.arduino.cc/en/software)  
- Install using the setup wizard  
- Launch the IDE  

### 2.2 Configure Arduino IDE

- **Tools → Board** → Select your Arduino model  
- **Tools → Port** → Select the correct COM port  
- Test connection: **Tools → Get Board Info**

### 2.3 Upload Arduino Code

- Open: `arduino/face_tracker_arduino_full_range.ino`  
- Click **Upload** (→) or press `Ctrl+U`  
- Wait for `Done uploading` message  
- Open **Serial Monitor** (`Ctrl+Shift+M`)  
- Set **baud rate to 9600**  
- You should see:  


---