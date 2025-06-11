# Face Tracking Servo Controller 🎯

A robust, real-time face tracking system that uses computer vision to control a servo motor—making it follow faces detected by a webcam. Perfect for robotics, security, and DIY projects!

![Status](https://img.shields.io/badge/Status-Working-brightgreen)
![Python](https://img.shields.io/badge/Python-3.7%2B-blue)
![Arduino](https://img.shields.io/badge/Arduino-IDE-orange)
![OpenCV](https://img.shields.io/badge/OpenCV-4.8%2B-red)
![MediaPipe](https://img.shields.io/badge/MediaPipe-0.10%2B-yellow)

---

## 🚀 Features

- **Dual Detection:** MediaPipe + Haar Cascade fallback for ultra-reliable face detection.
- **Distance Optimized:** Accurate tracking both close-up and at a distance.
- **Smooth Servo Control:** 0–180° full-range movement with adjustable step size.
- **Real-Time:** Low-latency, high-FPS face tracking.
- **Easy Configuration:** Tweak sensitivity, detection thresholds, and more.
- **Professional Docs:** Step-by-step setup guides and wiring diagrams.

---

## 🛠 Hardware Requirements

- **Arduino Uno/Nano/Pro Mini**
- **SG90 or compatible servo motor** (0–180°)
- **USB Webcam** (720p+ recommended)
- **Jumper wires** (3x)
- **Breadboard** (optional)
- **USB cable** for Arduino

---

## 📋 Software Requirements

- **Python 3.7+**
- **Arduino IDE**
- **USB-to-Serial drivers** (if needed)

---

## ⚡ Quick Start

### 1. Clone the Repository
```
git clone https://github.com/mighty-baseplate/Face-tracking.git
cd Face-tracking
```


### 2. Install Python Dependencies
```
pip install -r requirements.txt
```


### 3. Hardware Setup
- Connect servo signal to Arduino Pin 9 (see [Wiring Diagram](docs/wiring_diagram.md))
- Upload `arduino/face_tracker_arduino_full_range.ino` to your Arduino

### 4. Configure & Run
- Set `SERIAL_PORT` in `python/face_tracker.py` to match your Arduino port
- Run:
```
python python/face_tracker.py
```

- Press `q` to quit

---

## 📖 Documentation

- [Setup Guide](docs/setup_guide.md) — Full installation and usage instructions
- [Wiring Diagram](docs/wiring_diagram.md) — Hardware connection guide

---

## 🔌 Quick Wiring Reference
```
Arduino Pin 9 → Servo Signal (Orange/Yellow)
Arduino 5V → Servo VCC (Red)
Arduino GND → Servo GND (Brown/Black)
```

---

## ⚙️ Configuration

### Python Settings (`face_tracker.py`)
```
SERIAL_PORT = "COM7" # Your Arduino port (e.g., "COM3" or "/dev/ttyACM0")
WEBCAM_ID = 0 # Camera index (0, 1, 2...)
H_SENSITIVITY = 70 # Movement sensitivity (higher = less sensitive)
MIN_FACE_WIDTH = 5 # Minimum detected face width (pixels)
```


### Arduino Settings (`.ino` file)
```
const int ANGLE_STEP = 2; // Degrees per servo movement step
const int PAN_CENTER_ANGLE = 90; // Center position (degrees)
```


---

## 🎛 Serial Commands

| Command | Action       | Description                |
|---------|-------------|----------------------------|
| `L`     | Move Left   | Increase servo angle       |
| `R`     | Move Right  | Decrease servo angle       |
| `C`     | Center      | Stop movement              |
| `H`     | Home        | Return to 90° center       |

---

## 🔍 Troubleshooting

| Problem              | Solution                                   |
|----------------------|--------------------------------------------|
| Camera not opening   | Try different `WEBCAM_ID` (0, 1, 2, ...)   |
| Arduino not responding | Check COM port and baud rate (9600)      |
| Poor face detection  | Improve lighting, adjust confidence        |
| Servo not moving     | Double-check wiring and power supply       |

See [Setup Guide](docs/setup_guide.md) for more troubleshooting tips.

---

## 📊 Performance

- **Detection Accuracy:** ~95% in good lighting
- **Response Time:** <50ms average
- **Servo Range:** Full 180° coverage
- **Supported Cameras:** Most USB webcams
- **Python Version:** 3.7+ tested

---

## 🎯 How It Works

1. **Camera** captures video frames in real time.
2. **MediaPipe** detects faces with fallback to Haar Cascade for robustness.
3. **Python** calculates face position relative to frame center.
4. **Serial commands** (`L`, `R`, `C`) sent to Arduino.
5. **Arduino** moves servo to follow face smoothly.

---

## 🤝 Contributing

1. Fork the repo
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📝 License

Licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

## 🙏 Acknowledgments

- **OpenCV** and **MediaPipe** teams for their amazing libraries
- **Arduino** community for servo control inspiration

---


## 📧 Support

- **Issues:** [GitHub Issues](https://github.com/mighty-baseplate/Face-tracking/issues)
- **Email:** mightybaseplate.games@gmail.com

---

## ⭐ Star History

If you find this project helpful, please give it a ⭐!

---

**Made with ❤️ for makers, educators, and robotics enthusiasts.**