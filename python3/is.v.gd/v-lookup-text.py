#!/usr/bin/env python3

# Copyright (C) Ben McGinnes, 2013
# ben@adversary.org
#

import requests
import sys

l = len(sys.argv)

if l == 1:
    target = input("Enter the URL of the v.gd link to check: ")
elif l >= 2:
    target = sys.argv[1]
else:
    target = input("Enter the URL of the v.gd link to check: ")

url = "http://v.gd/forward.php"
payload = {"format": "simple", "shorturl": target}

r = requests.get(url, params=payload)

print("""
The URL of the API Access:

    %s

The shortened link is:

    %s

The URL the short linkened forwards to is:

    %s
""" % (r.url, target, r.content))
