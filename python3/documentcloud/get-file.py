#!/usr/bin/env python3

##
# Copyright (C) Ben McGinnes, 2013-2015
# ben@adversary.org
# OpenPGP/GPG key:  0x321E4E2373590E5D
#
# Version:  0.0.2
#
# BTC:  19J2Dc5DTztWRWMPcLwshj96NAnXAxtCvk
# License:  3-clause BSD
#
# Requirements:
#
# * Python 3.2 or later (developed with Python 3.4.x)
# * Python Requests 2.3.0 or later
#
# Options and notes:
#
# Usage:  Just run it and respond to the prompts.
#
# The document ID can usually be found in the HTML source to a web
# page, usually encased in some javascript to make those annoying
# viewers which "prevent" downloading the file.
#
##

import requests

doc_id = input("Enter the Document Cloud document ID (e.g. 12345-foo-bar): ")
dl_dir = input("Enter directory to download to (e.g. /tmp/) or blank for current directory: ")
f_type = input("Enter file type (e.g. pdf, odt, ods, xls, doc, docx, etc.): ")
ftype = f_type.lower()
api_url = "https://www.documentcloud.org/api/documents/"+doc_id+".json"

r1 = requests.get(api_url, verify=True)
url = r1.json()["document"]["resources"][ftype]

r2 = requests.get(url, verify=True)

newfile = "{0}/{1}.{2}".format(dl_dir, doc_id, ftype)
pdfile = open(newfile, "wb")
pdfile.write(r2.content)
pdfile.close()

print("""
File saved as:

    %s

Document Cloud file available at:

    %s

Document last modified on:

    %s

""" % (newfile, r1.json()["document"]["canonical_url"], r2.headers["last-modified"]))
