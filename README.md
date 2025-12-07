# Face Tracking Pan-Tilt Camera 🎯

**A real-time, pan-tilt face tracking system that uses computer vision to control two servo motors, making a camera follow a face smoothly.**

*Perfect for robotics, automated video calls, security systems, and interactive art projects.*

---

## 🌟 Key Features

- **Pan & Tilt Control:** Full 2-axis tracking (left/right and up/down).
- **Dual Detection Engine:** Uses MediaPipe for high-performance face detection with a Haar Cascade fallback for robustness.
- **Real-Time Performance:** Low-latency tracking with an FPS counter for performance monitoring.
- **Command-Line Control:** Easy to run and configure, with options to specify the serial port and enable a visualizer.
- **Comprehensive Documentation:** Includes a detailed setup guide and wiring diagrams.

---


## 📂 Project Structure

```
Face-tracking/
├── arduino/                # Arduino source code (.ino)
├── docs/                   # Documentation files (setup guide, wiring diagram)
├── python/                 # Main Python script (face_tracker.py)
├── .gitignore              # Git ignore file
├── LICENSE                 # Project license
├── README.md               # This file
└── requirements.txt        # Python dependencies
```

---

## 🛠️ Hardware & Software

*(See the [Setup Guide](docs/setup_guide.md) for a detailed list of requirements.)*

---

## ⚡ Quick Start

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/mighty-baseplate/Face-tracking.git
    cd Face-tracking
    ```

2.  **Install Python dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Set up the hardware:**
    *   Connect the servos to the Arduino as shown in the [Wiring Diagram](docs/wiring_diagram.md).
    *   Upload the `arduino/face_tracker_arduino.ino` sketch to your Arduino.

4.  **Run the tracker:**
    *   Find your Arduino's serial port (e.g., `COM3` on Windows, `/dev/ttyACM0` on Linux).
    *   Run the script from the command line:
        ```bash
        python python/face_tracker.py --port YOUR_ARDUINO_PORT
        ```
    *   To see the video feed with tracking overlays, use the `--visualize` flag:
        ```bash
        python python/face_tracker.py --port YOUR_ARDUINO_PORT --visualize
        ```

5.  **Press `q` to quit.**

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a pull request.

---

## 📝 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
