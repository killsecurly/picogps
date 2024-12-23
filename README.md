# PicoGPS
## A Pi Pico based CircuitPython GPS tracker.

## Required Materials
1. Adafruit Ultimate GPS Breakout v3 (https://www.adafruit.com/product/746)
  - Possible to subtitute with a Ublox NEO-6M, though not recommended because of the quality
2. Raspberry Pi Pico 2 - RP2350 (https://www.adafruit.com/product/6006)
  - You can use any CircuitPython board but it will require changing of the pins inside the code
3. 3-pin 2-position Slide Switch (https://www.adafruit.com/product/805)
  - Any generic slide switch will work if its pins are breadboard friendly
4. Prototyping PCBs/Perfboards (https://www.adafruit.com/product/2670)
  - Any generic one will work if its holes are breadboard sized
5. 30 AWG Prototyping Wire (https://www.adafruit.com/product/1446)
  - Any decent generic 24AWG-30AWG will work, but smaller is better for overall finish

## .GPB Specifications
Struct binary file (iifffff)

Int  | Int  | Float | Float | Float    | Float | Float
Date | Time | Lat   | Long  | Altitude | HDOP  | VDOP
