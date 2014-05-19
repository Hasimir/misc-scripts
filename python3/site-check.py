#!/usr/bin/env python3

##
# Copyright (C) Ben McGinnes, 2014
# ben@adversary.org
# OpenPGP/GPG key:  0x321E4E2373590E5D
#
# Version:  0.0.1
#
# BTC:  19J2Dc5DTztWRWMPcLwshj96NAnXAxtCvk
# Licenses:  BSD, GPLv3 and WTFNMFPL.
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

__author__ = "Ben McGinnes <ben@adversary.org>"
__copyright__ = "Copyright © Benjamin D. McGinnes, 2014"
__copyrighta__ = "Copyright (C) Benjamin D. McGinnes, 2014"
__copyrightu__ = "Copyright \u00a9 Benjamin D. McGinnes, 2014"
__license__ = "BSD, GPLv3 and WTFNMFPL"
__version__ = "0.0.1"
__bitcoin__ = "19J2Dc5DTztWRWMPcLwshj96NAnXAxtCvk"

import requests
import sys

l = len(sys.argv)
h1 = "http://"
h2 = "https://"

headers = { "User-Agent": "Requests Over Tor" }
proxies = { "http": "http://127.0.0.1:8118",
            "https": "https://127.0.0.1:8118", }

if l == 1:
    domain = input("Enter the domain name (without the www.): ")
elif l >= 2:
    domain = sys.argv[1]

url1 = h1 + domain
url2 = h1 + "www." + domain
url3 = h2 + domain
url4 = h2 + "www." + domain

r1 = requests.get(url1)
r2 = requests.get(url2)
r3 = requests.get(url3, verify=False)
r4 = requests.get(url4, verify=False)
r5 = requests.get(url1, headers=headers, proxies=proxies, verify=False)
r6 = requests.get(url2, headers=headers, proxies=proxies, verify=False)
r7 = requests.get(url3, headers=headers, proxies=proxies, verify=False)
r8 = requests.get(url4, headers=headers, proxies=proxies, verify=False)

if r1.status_code == requests.codes.ok:
    print("%s is up." % url1)
else:
    print("%s is not responding." % url1)

if r2.status_code == requests.codes.ok:
    print("%s is up." % url2)
else:
    print("%s is not responding." % url2)

if r3.status_code == requests.codes.ok:
    print("%s is up." % url3)
else:
    print("%s is not responding." % url3)

if r4.status_code == requests.codes.ok:
    print("%s is up." % url4)
else:
    print("%s is not responding." % url4)

if r5.status_code == requests.codes.ok:
    print("%s is up through Tor." % url5)
else:
    print("%s is not responding through Tor." % url5)

if r6.status_code == requests.codes.ok:
    print("%s is up through Tor." % url6)
else:
    print("%s is not responding through Tor." % url6)

if r7.status_code == requests.codes.ok:
    print("%s is up through Tor." % url7)
else:
    print("%s is not responding through Tor." % url7)

if r8.status_code == requests.codes.ok:
    print("%s is up through Tor." % url8)
else:
    print("%s is not responding through Tor." % url8)
