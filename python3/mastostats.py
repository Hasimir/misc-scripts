#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import sys

if len(sys.argv) >= 2:
    urls = sys.argv[1:]
else:
    urls = input("Enter the URL(s) of the instances to check: ")

pleromas = []

for i in range(len(urls)):
    strings = []
    integers = []
    floats = []
    
    if urls[i].startswith("https://") is True:
        url = urls[i]
    elif urls[i].startswith("http://") is True:
        url = urls[i].replace("http://", "https://")
    else:
        url = "https://{0}".format(urls[i])
    
    weakurl = url.replace("https://", "http://")
    path = "about/more"
    host = url.replace("https://", "")

    try:
        uri = "{0}/{1}".format(url, path)
        r = requests.get(uri, verify=True)
        r_url = url
    except:
        uri = "{0}/{1}".format(weakurl, path)
        r = requests.get(uri)
        r_url = weakurl

    if r.content.decode().lower().find("pleroma") >= 1:
        pleromas.append(host)
    else:
        pass

    if len(pleromas) >= 1:
        for n in range(len(pleromas)):
            if r.url.count(pleromas[n]) == 1:
                strings.append("unknown")
                strings.append("unknown")
                strings.append("an unknown number of")
            else:
                lines = r.content.decode().splitlines()
                for line in lines:
                    if line.startswith("<strong>") is True:
                        newline = line.replace("<strong>", "").replace("</strong>", "")
                        strings.append(newline)
                        numline = newline.replace(",", "")
                        integers.append(int(numline))
                        floats.append(float(numline))
    else:
        lines = r.content.decode().splitlines()
        for line in lines:
            if line.startswith("<strong>") is True:
                newline = line.replace("<strong>", "").replace("</strong>", "")
                strings.append(newline)
                numline = newline.replace(",", "")
                integers.append(int(numline))
                floats.append(float(numline))

    result = """
  Current {0} stats are:

    Total users:  {1}
    Total toots:  {2}

  {3} is currently connected to {4} other servers.
""".format(host, strings[0], strings[1], r_url, strings[2])

    print(result)

if len(pleromas) >= 1:
    print("")
    for n in range(len(pleromas)):
        print("{0} is a Pleroma instance.".format(pleromas[n]))
    print("")
else:
    pass
