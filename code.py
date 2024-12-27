import time
import board
import busio
import struct
import digitalio

import adafruit_gps

uart = busio.UART(board.GP16, board.GP17, baudrate=9600, timeout=10)
gps = adafruit_gps.GPS(uart, debug=False)
gps.send_command(b"$PMTK314,0,1,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0")
gps.send_command(b"PMTK220,1000")

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

last_print = time.monotonic()

filename = None

while True:
    gps.update()
    current = time.monotonic()
    if current - last_print >= 1.0:
        last_print = current
        if not gps.has_fix:
            led.value = False
            time.sleep(0.25)
            led.value = True
            continue
        ctime = gps.timestamp_utc

        xdate = int(str(ctime.tm_year) + "0"*(2-len(str(ctime.tm_mon))) + str(ctime.tm_mon) + "0"*(2-len(str(ctime.tm_mday))) + str(ctime.tm_mday))
        xtime = int("0"*(2-len(str(ctime.tm_hour))) + str(ctime.tm_hour) + "0"*(2-len(str(ctime.tm_min))) + str(ctime.tm_min) + "0"*(2-len(str(ctime.tm_sec))) + str(ctime.tm_sec))

        try:
            lat = gps.latitude
            long = gps.longitude
            alt = gps.altitude_m
            hdop = gps.hdop
            vdop = gps.vdop

            if not hdop:
                hdop = 0
            if not vdop:
                vdop = 0

            if not filename:
                filename = str(xdate) + str(xtime)

            with open(filename + ".gpb", "ab") as f:
                f.write(struct.pack("iifffff", xdate, xtime, lat, long, alt, hdop, vdop))
                led.value = True
        except:
            while True:
                led.value = False
                time.sleep(0.5)
                led.value = True
