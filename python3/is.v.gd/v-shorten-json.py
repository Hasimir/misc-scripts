#!/usr/bin/env python3

# Copyright (C) Ben McGinnes, 2013
# ben@adversary.org
#

import requests
import sys

l = len(sys.argv)

if l == 1:
    target = input("Enter the URL to shorten via v.gd: ")
elif l >= 2:
    target = sys.argv[1]
else:
    target = input("Enter the URL to shorten via v.gd: ")

url = "http://v.gd/create.php"
payload = {"format": "json", "url": target, "logstats": "1"}

r = requests.get(url, params=payload)

print("""
The URL of the API Access:

    %s

The URL to be shortened:

    %s

The URL of the shortened link:

    %s
""" % (r.url, target, r.json()["shorturl"]))
