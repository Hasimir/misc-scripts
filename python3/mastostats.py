#!/usr/bin/env python3

from future import unicode_literals

import requests
import sys

if len(sys.argv) >= 2:
    urls = sys.argv[1:]
else:
    urls = input("Enter the URL(s) of the instances to check: ")

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
    lines = r.content.decode().splitlines()
    for line in lines:
        if line.startswith("<strong>") is True:
            newline = line.replace("<strong>", "").replace("</strong>", "")
            strings.append(newline)
            numline = newline.replace(",", "")
            integers.append(int(numline))
            floats.append(float(numline))
        else:
            pass

    result = """
  Current {0} stats are:

    Total users:  {1}
    Total toots:  {2}

  {3} is currently connected to {4} other servers.
""".format(host, strings[0], strings[1], r_url, strings[2])

    print(result)
