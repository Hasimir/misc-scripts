#!/usr/bin/env python3

##
# Copyright (C) Ben McGinnes, 2014
# ben@adversary.org
# OpenPGP/GPG key:  0x321E4E2373590E5D
#
# Version:  0.0.1
#
# BTC:  19J2Dc5DTztWRWMPcLwshj96NAnXAxtCvk
# Licenses:  To Be Advised
#
# Requirements:
#
# * Python 3.2 or later (developed with Python 3.4.x)
# * python-requests 2.3.0 or later
#
# Options:
#
##

__author__ = 'Ben McGinnes <ben@adversary.org>'
__copyright__ = 'Copyright (C) Benjamin D. McGinnes, 2014'
__copyrightu__ = u'Copyright \xa9 Benjamin D. McGinnes, 2014'.encode('UTF-8')
__copyrightl__ = u'Copyright \xa9 Benjamin D. McGinnes, 2014'.encode('iso-8859-1')
__license__ = ''
__version__ = '0.0.1'
__bitcoin__ = '19J2Dc5DTztWRWMPcLwshj96NAnXAxtCvk'


url = input("Enter the LocalBitcoins URL (including https:): ")

lbtcid = "2wff"
jsonid = { "ch": "2wff" }

newurl = url+"?ch="+lbtcid

print("""
{0}
""".format(newurl))
