#!/usr/bin/env python3

##
# Copyright (C) Ben McGinnes, 2014
# ben@adversary.org
# OpenPGP/GPG key:  0x321E4E2373590E5D
#
# Version:  0.0.1
#
# License:  BSD
#
##

__author__ = "Ben McGinnes <ben@adversary.org>"
__copyright__ = "Copyright © Benjamin D. McGinnes, 2014"
__copyrighta__ = "Copyright (C) Benjamin D. McGinnes, 2014"
__copyrightu__ = "Copyright \u00a9 Benjamin D. McGinnes, 2014"
__license__ = "Modified BSD"
__version__ = "0.0.1"

import requests
import sys
import time

l = len(sys.argv)

if l == 1:
    btc = input("Enter the Bitcoin address to check: ")
else:
    btc = sys.argv[1]

url = "http://blockchain.info/q/addressbalance/%s/100000000" % btc

r = requests.get(url, verify=False)
i = float(r.text) / 100000000.0

print("""%s has %s BTC on it
as of %s UTC.""" % (btc, str(i), time.asctime(time.gmtime())))
