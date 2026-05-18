# Face Tracking Pan-Tilt Camera

A pan-tilt camera mount that follows your face in real time. The Python script uses MediaPipe to detect faces via webcam, then sends serial commands to an Arduino which moves two servo motors to keep you centered in frame.

I built this because I kept getting cut off during video calls when I moved around. Figured it was a good excuse to learn some computer vision.

---

## Hardware you'll need

- Arduino Uno (or Nano)
- 2x SG90 servo motors
- Pan-tilt bracket (cheap ones off Amazon work fine)
- USB webcam (720p or better)
- Jumper wires

See [docs/wiring_diagram.md](docs/wiring_diagram.md) for how to connect everything.

---

## Setup

**1. Upload the Arduino sketch**

Open `arduino/face_tracker_arduino.ino` in the Arduino IDE, select your board and port, and upload it.

**2. Install Python dependencies**

```bash
pip install -r requirements.txt
```

**3. Find your Arduino's serial port**

On Windows it'll be something like `COM3`. On Linux/Mac, something like `/dev/ttyACM0`. You can check in the Arduino IDE under Tools > Port.

**4. Run it**

```bash
python python/face_tracker.py --port YOUR_PORT
```

Add `--visualize` to see the video feed with the detection overlay:

```bash
python python/face_tracker.py --port YOUR_PORT --visualize
```

Press `q` to quit.

---

## How it works

- MediaPipe handles face detection (fast, works well in decent lighting)
- Falls back to OpenCV's Haar Cascade if MediaPipe doesn't find anything
- Tracks the largest detected face if multiple are in frame
- Sends single-character commands over serial (`L`, `R`, `U`, `D`, `C`, `S`) to the Arduino
- Arduino moves the servos by a fixed step per command — simple but responsive enough

---

## Known issues / TODO

- Tracking gets shaky under poor lighting — tweaking `min_detection_confidence` in the script helps
- The step-based servo control can jitter a bit; a PID loop would smooth it out
- Default port is `COM7` in the script — change it or always pass `--port`
- Only tracks one face at a time (picks the largest one)
