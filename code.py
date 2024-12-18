import time
import board
import busio
import struct

import adafruit_gps

uart = busio.UART(board.GP16, board.GP17, baudrate=9600, timeout=10)
gps = adafruit_gps.GPS(uart, debug=False)  # Use UART/pyserial
gps.send_command(b"$PMTK314,0,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0*")
gps.send_command(b"PMTK220,1000")

last_print = time.monotonic()

filename = None

while True:
    gps.update()
    current = time.monotonic()
    if current - last_print >= 1.0:
        last_print = current
        if not gps.has_fix:
            continue
        ctime = gps.timestamp_utc

        xdate = int(str(ctime.tm_year) + "0"*(2-len(str(ctime.tm_mon))) + str(ctime.tm_mon) + "0"*(2-len(str(ctime.tm_mday))) + str(ctime.tm_mday))
        xtime = int("0"*(2-len(str(ctime.tm_hour))) + str(ctime.tm_hour) + "0"*(2-len(str(ctime.tm_min))) + str(ctime.tm_min) + "0"*(2-len(str(ctime.tm_sec))) + str(ctime.tm_sec))

        lat = gps.latitude
        long = gps.longitude
        alt = gps.altitude_m
        hdop = gps.hdop
        vdop = gps.vdop

        if not filename:
            filename = str(xdate)

        with open(filename + ".gpb", "ab") as f:
            f.write(struct.pack("iifffff", xdate, xtime, lat, long, alt, hdop, vdop))
