#!/usr/local/bin/python3

# Copyright ©  Benjamin D. McGinnes, 2018
# Ben McGinnes <ben@adversary.org>
# OpenPGP key: DB4724E6FA4286C92B4E55C4321E4E2373590E5D
# Licensed under the Apache 2.0 License

import sys
from geopy.geocoders import ArcGIS

if len(sys.argv) > 1:
    meatspace = " ".join(sys.argv[1:])
else:
    meatspace = input("Enter the address: ")

gloc = ArcGIS()
target = gloc.geocode(meatspace)
is_positive_lat = target.latitude >= 0
is_positive_lon = target.longitude >= 0
abs_lat = abs(target.latitude)
abs_lon = abs(target.longitude)

def dd2dms(dd):
    minutes, seconds = divmod(dd * 3600, 60)
    degrees, minutes = divmod(minutes, 60)
    return degrees, minutes, seconds

if is_positive_lat is True:
    dd = abs_lat
    lat_deg, lat_min, lat_sec = dd2dms(dd)
    dms_lat = """{0}° {1}' {2}" N""".format(lat_deg, lat_min, lat_sec)
else:
    dd = abs_lat
    lat_deg, lat_min, lat_sec = dd2dms(dd)
    dms_lat = """{0}° {1}' {2}" S""".format(lat_deg, lat_min, lat_sec)

if is_positive_lon is True:
    dd = abs_lon
    lon_deg, lon_min, lon_sec = dd2dms(dd)
    dms_lon = """{0}° {1}' {2}" E""".format(lon_deg, lon_min, lon_sec)
else:
    dd = abs_lon
    lon_deg, lon_min, lon_sec = dd2dms(dd)
    dms_lon = """{0}° {1}' {2}" W""".format(lon_deg, lon_min, lon_sec)

result = """
Full address:  {0}
GPS Coordinates:  {1}
Old Coordinates:  {2},
                  {3}
""".format(target.address, (target.latitude, target.longitude), dms_lat,
           dms_lon)

print(result)
