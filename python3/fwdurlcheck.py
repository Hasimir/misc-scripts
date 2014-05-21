#!/usr/bin/env python3

##
# Copyright (C) Ben McGinnes, 2013-2014
# ben@adversary.org
# OpenPGP/GPG key:  0x321E4E2373590E5D
#
# Version:  0.0.1
#
# BTC:  19J2Dc5DTztWRWMPcLwshj96NAnXAxtCvk
# License:  GPLv3
#
# https://www.gnu.org/copyleft/gpl.html
#
# Requirements:
#
# * Python 3.2 or later (developed with Python 3.4.x)
#
# Options and notes:
#
# Usage:  
#
##

__author__ = "Ben McGinnes <ben@adversary.org>"
__copyright__ = "Copyright \u00a9 Benjamin D. McGinnes, 2013-2014"
__copyrighta__ = "Copyright (C) Benjamin D. McGinnes, 2013-2014"
__license__ = "GPLv3 or WTFNMFPL"
__version__ = "0.0.1"
__bitcoin__ = "19J2Dc5DTztWRWMPcLwshj96NAnXAxtCvk"
    
import requests
import sys

h = "http://"
hs = "https://"

if len(sys.argv) >= 2:
    fwdurl = sys.argv[1]
else:
    fwdurl = raw_input("Enter the shortened URL in its entirety: ")

if fwdurl[0:4] == "t.co":
    url = hs+fwdurl
else:
    url = fwdurl

r = requests.get(url, verify=False)
    
print("""
The shortened URL forwards to:

    %s
""" % r.url)
