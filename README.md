# Introduction
A snake xenzia variant in which the player controls the main character whose score increases with every berry they eat which is generated randomly by the computer. Compete with your friends to show who can get the highest score in a set amount of time while showing off your DIY skills!

## Connections

### OLED (SSD1306 0.9 inch display)
GND -> Pin 28 -> GND
VDD -> Pin 36 -> 3V3(OUT)
SCK -> Pin 22 -> GP17
SDA -> Pin 21 -> GP16

### Analog Joystick (PS2 Joystick Module Breakout Sensor)
GND -> Pin 33 -> GND
+5V -> Pin 36 -> 3V3(OUT)
VRX -> Pin 32 -> GP27
VRY -> Pin 31 -> GP26
SW  -> Pin 29 -> GP22

## Firmware
> NOTE: This program is coded in micropython. 
- In order to make this work, 
    1. Hold the bootsel button on your pico while plugging it in.
    2. Download the latest micropython firmware for your pico / pico w.
    3. Copy it to the pico's working directory. 
    4. It will restart itself and boot up in micropython mode.
    5. Clone the repo
    6. Re-plug the pico back in the computer or provide direct power from your outlet using the micro usb cable.
    7. Enjoy!
