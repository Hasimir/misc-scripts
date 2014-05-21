#!/usr/bin/env python3

##
# Copyright (C) Ben McGinnes, 2014
# ben@adversary.org
# OpenPGP/GPG key:  0x321E4E2373590E5D
#
# Version:  0.0.2
#
# BTC:  19J2Dc5DTztWRWMPcLwshj96NAnXAxtCvk
# License:  GPLv3
#
# https://www.gnu.org/copyleft/gpl.html
#
# Requirements:
#
# * Python 3.2 or later (developed with Python 3.4.x)
# * python-requests 2.1.0 or later
#
# Options:
#
##

__author__ = 'Ben McGinnes <ben@adversary.org>'
__copyright__ = 'Copyright (C) Benjamin D. McGinnes, 2014'
__copyrightu__ = u'Copyright \xa9 Benjamin D. McGinnes, 2014'.encode('UTF-8')
__copyrightl__ = u'Copyright \xa9 Benjamin D. McGinnes, 2014'.encode('iso-8859-1')
__license__ = 'GPLv3'
__version__ = '0.0.2'
__bitcoin__ = '19J2Dc5DTztWRWMPcLwshj96NAnXAxtCvk'

import requests
import sys

l = len(sys.argv)
url = "http://www.pirateparty.org.au/"
headers = { "User-Agent": "Requests Over Tor" }
proxies = { "http": "http://127.0.0.1:8118",
            "https": "https://127.0.0.1:8118", }

if l < 2:
    r = requests.get(url, verify=False)
elif l >= 3:
    r = requests.get(url, headers=headers, proxies=proxies, verify=False)
elif sys.argv[1].lower() == "tor":
    r = requests.get(url, headers=headers, proxies=proxies, verify=False)
elif sys.argv[1].lower() == "direct":
    r = requests.get(url, verify=False)
else:
    r = requests.get(url, verify=False)

print(r.status_code)

if r.status_code == requests.codes.ok:
    print(True)
else:
    print(False)
