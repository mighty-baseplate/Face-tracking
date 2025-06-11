# Wiring Diagram

## Components Needed

- Arduino Uno or Nano  
- SG90 Servo Motor (or similar)  
- Jumper wires (x3)  
- Breadboard (optional)  
- USB Cable for Arduino

---

## Pin Connections

### Servo to Arduino

| Servo Wire | Color         | Arduino Pin | Description             |
|------------|---------------|-------------|-------------------------|
| Signal     | Orange/Yellow | Pin 9       | PWM control signal      |
| Power      | Red           | 5V          | Positive power supply   |
| Ground     | Brown/Black   | GND         | Ground connection       |

---

## Visual Wiring Diagram


Arduino Uno                    SG90 Servo Motor
┌─────────────┐               ┌──────────────┐
│             │               │              │
│         Pin9├───────────────┤Signal(Orange)│
│             │               │              │
│          5V ├───────────────┤Power  (Red)  │
│             │               │              │
│         GND ├───────────────┤Ground (Brown)│
│             │               │              │
│        USB  │               └──────────────┘
└─────────────┘
     │
     │ USB Cable
     │
┌────▼────┐
│Computer │
└─────────┘

---

## Breadboard Connection (Optional)

| Arduino Pin | Breadboard Rail | Servo Wire       |
|-------------|------------------|------------------|
| Pin 9       | Red Rail         | Signal (Orange)  |
| 5V          | Red Rail         | Power (Red)      |
| GND         | Blue Rail        | Ground (Brown)   |

---

## Power Considerations

### SG90 Servo (Small):
- Can be powered directly from Arduino 5V pin
- Current draw: ~100–200 mA

### Larger Servos:
- Use an external 5V power supply
- Connect Arduino GND to external power GND
- Only signal wire connects to Arduino Pin 9


---

## Safety Notes

- Double-check wire connections before powering on  
- Ensure correct polarity (Red = +, Brown/Black = –)  
- Do not reverse power connections (can damage servo)  
- Use external power for servos drawing more than 500mA

---

## Testing Connection

1. Upload Arduino code
2. Open Serial Monitor (9600 baud)
3. Output should be:

4. Servo should move to center position (90°)

---

## Troubleshooting

| Issue             | Check / Fix                                    |
|------------------|------------------------------------------------|
| Servo not moving | Check wiring, power, try a different servo     |
| Servo jittering  | Improve power supply, ensure solid GND, add capacitor |
| Arduino unresponsive | Check USB cable, correct COM port, replace cable |

---

## Alternative Pin Configurations

If Pin 9 is used by another device, you may use other PWM pins:

**Available PWM Pins on Arduino Uno:**  
`3, 5, 6, 10, 11`

Update the pin definition in your Arduino code:
```cpp
#define PAN_SERVO_PIN 3  // Replace with desired PWM pin
