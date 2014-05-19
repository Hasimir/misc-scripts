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
__license__ = "GPLv3"
__version__ = "0.0.1"
__bitcoin__ = "19J2Dc5DTztWRWMPcLwshj96NAnXAxtCvk"

import re
import sys

l = len(sys.argv)

if l == 2:
    filename = sys.argv[1]
    pattern = input("Enter the pattern to match and remove: ")
    logrus = input("Enter the pattern to replace with: ")
elif l == 3:
    filename = sys.argv[1]
    pattern = sys.argv[2]
    logrus = input("Enter the pattern to replace with: ")
elif l >= 4:
    filename = sys.argv[1]
    pattern = sys.argv[2]
    logrus = sys.argv[3]
else:
    filename = input("Enter the name of the file: ")
    pattern = input("Enter the pattern to match and remove: ")
    logrus = input("Enter the pattern to replace with: ")

f = open(filename, "r")
lines = f.readlines()
f.close()

f = open(filename, "w")
for line in lines:
    if pattern in line:
        line = re.sub(pattern, logrus, line)
    f.write(line)
f.close()
