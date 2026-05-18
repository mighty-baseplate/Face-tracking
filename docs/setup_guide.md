# Setup Guide

## What you need

**Hardware:**
- Arduino Uno or Nano
- 2x SG90 servo motors
- Pan-tilt camera bracket
- USB webcam (720p or better)
- Jumper wires

**Software:**
- Python 3.7+
- Arduino IDE

---

## Hardware setup

1. Assemble the pan-tilt bracket with both servos and mount the webcam on it.
2. Wire the servos to the Arduino — see [wiring_diagram.md](wiring_diagram.md).
3. Plug the Arduino into your computer via USB.

---

## Arduino setup

1. Open `arduino/face_tracker_arduino.ino` in the Arduino IDE.
2. Under **Tools**, select your board and port.
3. Click **Upload**.

---

## Python setup

```bash
pip install -r requirements.txt
```

---

## Running it

Find your port in the Arduino IDE under **Tools > Port**, then:

```bash
python python/face_tracker.py --port YOUR_PORT
```

Add `--visualize` if you want to see the camera feed.

---

## Troubleshooting

- **Servos not moving** — check wiring, make sure the Arduino is powered and the sketch uploaded correctly
- **Can't find webcam** — make sure it's plugged in; try a different `WEBCAM_ID` value in the script if you have multiple cameras
- **Serial connection error** — double-check the port name; on Linux you may need `sudo` or to add your user to the `dialout` group
