# Setup Guide 📋

## Prerequisites

### Software Requirements
- **Python 3.7+** - [Download Python](https://python.org/downloads/)
- **Arduino IDE** - [Download Arduino IDE](https://arduino.cc/downloads/)
- **Git** (optional) - [Download Git](https://git-scm.com/)

### Hardware Requirements
- Arduino Uno/Nano/Pro Mini
- SG90 Servo motor or similar
- USB Webcam (720p+ recommended)
- USB cable for Arduino
- 3x Jumper wires

## Step 1: Hardware Setup

### 1.1 Connect Servo to Arduino
Follow the [Wiring Diagram](wiring_diagram.md) to connect:
- Servo Signal (Orange) → Arduino Pin 9  
- Servo Power (Red) → Arduino 5V
- Servo Ground (Brown) → Arduino GND

### 1.2 Connect Arduino to Computer
- Use USB cable to connect Arduino to computer
- Note the COM port (Windows) or device path (Mac/Linux)

## Step 2: Arduino Software Setup

### 2.1 Install Arduino IDE
1. Download from [arduino.cc](https://arduino.cc/downloads/)
2. Install following the wizard
3. Launch Arduino IDE

### 2.2 Configure Arduino IDE
1. Go to **Tools → Board** → Select your Arduino model
2. Go to **Tools → Port** → Select the correct COM port
3. Test connection: **Tools → Get Board Info**

### 2.3 Upload Arduino Code
1. Open `arduino/face_tracker_arduino_full_range.ino`
2. Click **Upload** button (→) or Ctrl+U
3. Wait for "Done uploading" message
4. Open **Serial Monitor** (Ctrl+Shift+M)
5. Set baud rate to **9600**
6. You should see: "Arduino Face Tracker (0-180 Range) Ready."

## Step 3: Python Environment Setup

### 3.1 Check Python Installation
```bash
python --version
# Should show Python 3.7 or higher
```

### 3.2 Create Virtual Environment (Recommended)
```bash
# Navigate to project folder
cd face-tracking-servo

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate
```

### 3.3 Install Python Dependencies
```bash
pip install -r requirements.txt
```

Or install manually:
```bash
pip install opencv-python==4.8.1.78
pip install mediapipe==0.10.7
pip install pyserial==3.5
pip install numpy==1.24.3
```

## Step 4: Configure Python Script

### 4.1 Find Arduino COM Port

**Windows:**
- Device Manager → Ports → Note COM port (e.g., COM3, COM7)

**Mac:**
```bash
ls /dev/cu.*
# Look for something like /dev/cu.usbmodem14101
```

**Linux:**
```bash
ls /dev/ttyUSB* /dev/ttyACM*
# Usually /dev/ttyUSB0 or /dev/ttyACM0
```

### 4.2 Update Python Configuration
Edit `python/face_tracker.py`:
```python
SERIAL_PORT = "COM7"    # Change to your port
WEBCAM_ID = 0           # Try 0, 1, 2 if camera not found
```

### 4.3 Test Camera
```python
import cv2
cap = cv2.VideoCapture(0)  # Try 0, 1, 2...
ret, frame = cap.read()
if ret:
    print("Camera working!")
    cv2.imshow("Test", frame)
    cv2.waitKey(0)
cap.release()
cv2.destroyAllWindows()
```

## Step 5: Running the System

### 5.1 Start Arduino
- Arduino should be connected and running
- Serial Monitor should show "Ready" message

### 5.2 Run Python Script
```bash
python python/face_tracker.py
```

### 5.3 Expected Behavior
1. Camera window opens
2. Arduino connects successfully
3. Your face is detected (green rectangle)
4. Servo follows your face movement
5. Press 'q' to quit

## Step 6: Troubleshooting

### Camera Issues
```python
# Try different camera indices
WEBCAM_ID = 0  # Default
WEBCAM_ID = 1  # External USB camera
WEBCAM_ID = 2  # Second external camera
```

### Arduino Connection Issues
```bash
# Check if port is correct
python -c "import serial; print(serial.tools.list_ports.comports())"
```

### Face Detection Issues
- **Poor lighting:** Add more light or adjust camera angle
- **Too far:** Move closer to camera initially
- **Detection sensitivity:** Lower `min_detection_confidence` to 0.3

```python
face_detection = mp_face_detection.FaceDetection(
    model_selection=1,
    min_detection_confidence=0.3  # Lower = more sensitive
)
```

### Servo Movement Issues
- **Not moving:** Check wiring and power
- **Jittery:** Add delays or smooth movement code
- **Wrong direction:** Swap L/R commands in Arduino code

## Step 7: Optimization

### 7.1 Performance Tuning
```python
# Reduce resolution for better performance
FRAME_WIDTH = 640
FRAME_HEIGHT = 480

# Increase sensitivity for faster response
H_SENSITIVITY = 50  # Lower = more sensitive
```

### 7.2 Detection Tuning
```python
# For close-up use
MIN_FACE_WIDTH = 30
MIN_FACE_HEIGHT = 30

# For distant use  
MIN_FACE_WIDTH = 5
MIN_FACE_HEIGHT = 5
```

## Step 8: Advanced Configuration

### 8.1 Multiple Servo Control
Modify Arduino code to control X and Y servos:
```cpp
const int PAN_SERVO_PIN = 9;   // X-axis (left/right)
const int TILT_SERVO_PIN = 10; // Y-axis (up/down)
```

### 8.2 Add Face Recognition
```python
# Add face recognition with face_recognition library
pip install face_recognition
```

### 8.3 Web Interface
```python
# Add Flask web interface for remote control
pip install flask
```

## Common Error Solutions

### "Serial port not found"
- Check COM port in Device Manager
- Close Arduino IDE Serial Monitor
- Try different USB cable

### "Camera not detected"
- Close other camera applications
- Try different WEBCAM_ID values
- Check camera permissions

### "ModuleNotFoundError"
- Activate virtual environment
- Reinstall requirements: `pip install -r requirements.txt`

### "Servo not responding"
- Check wiring connections
- Verify Arduino code uploaded successfully
- Test with Arduino Serial Monitor
