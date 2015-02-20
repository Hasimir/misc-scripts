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
# The document IDs can usually be found in the HTML source to a web
# page, usually encased in some javascript to make those annoying
# viewers which "prevent" downloading the file.
#
# Include each document ID on a separate line of the input (text)
# file.
#
##

import requests

filename = input("File name of document list (text file): ")
dl_dir = input("Enter directory to download to (e.g. /tmp) or a full stop (period) for the current directory: ")
logfile = input("Enter file to write log to (include full path and extension): ")

afile = open(filename, "r")
adata = afile.readlines()
afile.close()
for string in adata:
    doc_id = string.strip()
    api_url = "https://www.documentcloud.org/api/documents/"+doc_id+".json"
    r1 = requests.get(api_url, verify=True)
    url = r1.json()["document"]["resources"]["pdf"]
    r2 = requests.get(url, verify=True)
    newfile = "{0}/{1}.pdf".format(dl_dir, doc_id)
    pdfile = open(newfile, "wb")
    pdfile.write(r2.content)
    pdfile.close()
    bfile = open(logfile, "a")
    bfile.write("""
File saved as:  %s
Document Cloud file available at:  %s
Document last modified on:  %s
File size:  %s bytes

""" % (newfile, r1.json()["document"]["canonical_url"], r2.headers["last-modified"], r2.headers["content-length"]))
    bfile.close()
