#!/usr/bin/env python3

from __future__ import unicode_literals

##
# Copyright (C) Ben McGinnes, 2013-2015
# Copyright © Ben McGinnes, 2013-2015
# ben@adversary.org
# OpenPGP/GPG key:  0x321E4E2373590E5D
#
# Version:  0.0.3
#
# BTC:  19J2Dc5DTztWRWMPcLwshj96NAnXAxtCvk
# License:  GPLv3
#
# https://www.gnu.org/copyleft/gpl.html
#
# Requirements:
#
# * Python 3.2 or later (developed with Python 3.4.x)
# * Might work with more recent versions of 2.7.x.
#
# Options and notes:
#
# Usage:  
#
##

__author__ = "Ben McGinnes <ben@adversary.org>"
__copyright__ = "Copyright © Benjamin D. McGinnes, 2013-2015"
__license__ = "GPLv3"
__version__ = "0.0.3"
__bitcoin__ = "19J2Dc5DTztWRWMPcLwshj96NAnXAxtCvk"

import os
import os.path
import re
import sys

ls = os.listdir
op = os.path
sa = sys.argv
l = len(sa)
modded = []

if l == 2:
    folder = sa[1]
    pattern = input("Enter the pattern to match and remove: ")
    logrus = input("Enter the pattern to replace with: ")
elif l == 3:
    folder = sa[1]
    pattern = sa[2]
    logrus = input("Enter the pattern to replace with: ")
elif l >= 4:
    folder = sa[1]
    pattern = sa[2]
    logrus = sa[3]
else:
    folder = input("Enter the path to the file(s): ")
    pattern = input("Enter the pattern to match and remove: ")
    logrus = input("Enter the pattern to replace with: ")

if op.isdir(folder) is False:
    if op.isfile(folder) is True:
        files = []
        files.append(folder)
    elif op.isfile is False and len(folder) == 0:
        files = ls(op.curdir)
    else:
        files = folder
elif op.isdir(folder) is True:
    files = ls(folder)
else:
    files = None
    print("You must enter a valid directory or a filename.")
    pass

if files is not None:
    for filename in files:
        if op.isfile(filename) is True and op.islink(filename) is False:
            modded.append(filename)
            try:
                f = open(filename, "r")
                lines = f.readlines()
                f.close()
                fisbyte = False
            except:
                f = open(filename, "rb")
                lines = f.readlines()
                f.close()
                fisbyte = True

            if fisbyte is True:
                wbit = "wb"
                pbit = pattern.encode("utf-8")
                lbit = logrus.encode("utf-8")
            elif fisbyte is False:
                wbit = "w"
                pbit = pattern
                lbit = logrus
                
            f = open(filename, wbit)
            for line in lines:
                if pattern in line:
                    line = re.sub(pbit, lbit, line)
                f.write(line)
            f.close()
else:
    print("There are no files to process.")
    pass

if len(modded) > 0:
    print("{0} files were able to be modified.".format(len(modded)))
else:
    print("No files were able to be modified.")
    pass
