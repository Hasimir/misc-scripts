#!/usr/bin/env python3

import requests

doc_id = input("Enter the document ID (e.g. 12345-foo-bar): ")
dl_dir = input("Enter directory to download to (e.g. /tmp) or a full stop (period) for the current directory: ")
api_url = "https://www.documentcloud.org/api/documents/"+doc_id+".json"

r1 = requests.get(api_url, verify=True)
url = r1.json()["document"]["resources"]["pdf"]

r2 = requests.get(url, verify=True)

newfile = "{0}/{1}.pdf".format(dl_dir, doc_id)
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
