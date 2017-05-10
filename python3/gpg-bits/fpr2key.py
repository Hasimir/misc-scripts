#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import sys

if len(sys.argv) < 2:
    fpr = input("Enter the fingerprint: ")
else:
    fpr = sys.argv[1:]

fkid = "".join(fpr)
lkid = fkid[-16:]
skid = fkid[-8:]

info = """
The key full key ID (fingerprint) is:

    {0}

 The long key ID is:  0x{1}
The short key ID is:  0x{2}
""".format(fkid, lkid, skid)

print(info)
