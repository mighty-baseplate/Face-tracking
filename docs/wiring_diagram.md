# Wiring Diagram

## Components Needed

- Arduino Uno or Nano  
- 2x SG90 Servo Motors (or similar)  
- Jumper wires (x6)  
- Breadboard (optional)  
- USB Cable for Arduino

---

## Pin Connections

### Pan Servo to Arduino

| Servo Wire | Color         | Arduino Pin | Description             |
|------------|---------------|-------------|-------------------------|
| Signal     | Orange/Yellow | Pin 9       | PWM control signal      |
| Power      | Red           | 5V          | Positive power supply   |
| Ground     | Brown/Black   | GND         | Ground connection       |

### Tilt Servo to Arduino

| Servo Wire | Color         | Arduino Pin | Description             |
|------------|---------------|-------------|-------------------------|
| Signal     | Orange/Yellow | Pin 10      | PWM control signal      |
| Power      | Red           | 5V          | Positive power supply   |
| Ground     | Brown/Black   | GND         | Ground connection       |

---

## Power Considerations

### SG90 Servos (Small):
- Can be powered directly from Arduino 5V pin (for one or two small servos)
- Current draw: ~100–200 mA per servo

### Larger Servos or Multiple Servos:
- Use an external 5V power supply
- Connect Arduino GND to external power GND
- Only signal wire connects to Arduino (e.g., Pin 9 and Pin 10)

---

## Safety Notes

- Double-check wire connections before powering on  
- Ensure correct polarity (Red = +, Brown/Black = –)  
- Do not reverse power connections (can damage servo)  
- Use external power for servos drawing more than 500mA (e.g., for multiple servos or larger ones)

---

## Testing Connection

1. Upload Arduino code
2. Open Serial Monitor (9600 baud)
3. Output should be: `Arduino Pan-Tilt Face Tracker Ready.`
4. Servos should move to center position (90°)

---

## Troubleshooting

| Issue             | Check / Fix                                    |
|------------------|------------------------------------------------|
| Servo not moving | Check wiring, power, try a different servo     |
| Servo jittering  | Improve power supply, ensure solid GND, add capacitor |
| Arduino unresponsive | Check USB cable, correct COM port, replace cable |

---

## Alternative Pin Configurations

If Pin 9 or Pin 10 are used by another device, you may use other PWM pins:

**Available PWM Pins on Arduino Uno:**  
`3, 5, 6, 11`

Update the pin definitions in your Arduino code:
```cpp
#define PAN_SERVO_PIN 3  // Replace with desired PWM pin
#define TILT_SERVO_PIN 5 // Replace with desired PWM pin
```