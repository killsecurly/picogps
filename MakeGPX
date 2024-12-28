import struct
import gpxpy
import gpxpy.gpx
import datetime

gpx = gpxpy.gpx.GPX()
gpx.name = 'Raspberry Pi GPS'
gpx.description = 'GPS track'
gpx_track = gpxpy.gpx.GPXTrack()
gpx.tracks.append(gpx_track)
gpx_segment = gpxpy.gpx.GPXTrackSegment()
gpx_track.segments.append(gpx_segment)


# Time Lat Long Alt HDOP VDOP
# (8, 18, 36.0) to 081836.000
# 081836.000 to 08:18:36Z 

filename = input("Filename [No ext]: ")
datafile = input("Datafile [No ext]: ")

with open(datafile + ".gpb", "rb") as file:
    read = file.read()
    unpacked = struct.iter_unpack("iifffff", read)
    
    for i in unpacked:
        date, time, lat, long, alt, hdop, vdop = i[0], i[1], i[2], i[3], i[4], i[5], i[6]

        # Handle 24:XX:XX as 00:XX:XX
        if str(time)[:2] == '24':  # Check for '24' at the beginning
            time_str = "00" + str(time)[2:]  # Replace '24' with '0'
        else:
            time_str = str(time)

        combined_str = str(date) + time_str 
        time_obj = datetime.datetime.strptime(combined_str, '%Y%m%d%H%M%S') 
        gpx_segment.points.append(gpxpy.gpx.GPXWaypoint(lat, long, elevation=alt, time=time_obj, horizontal_dilution=hdop, vertical_dilution=vdop))

with open(filename + ".gpx", "w") as file:
    file.write(gpx.to_xml())
