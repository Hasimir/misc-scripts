#!/usr/bin/env python3

import requests
import time

etype = input("Enter the type of check (e.g. nick, host, etc.): ")
target = input("Enter the subject of search (e.g. handle, hostname, etc.): ")

dom = "http://www.oedb.info"

url = "{0}/{1}/{2}".format(dom, etype, target)

payload = { "format": "json" }

r = requests.get(url, params=payload)

eventsnum = len(r.json()["events"])

if eventsnum == 0:
    print("There have been no events for the {0} {1}.".format(etype, target))
else:
    print("There have been {0} events for the {1} {2}.".format(
        eventsnum, etype, target))

for i in range(eventsnum):
    nick = r.json()["events"][i]["nick"]
    ipaddr = r.json()["events"][i]["ip"]
    event = r.json()["events"][i]["event"]["type"]
    channel = r.json()["events"][i]["channel"]
    ts = r.json()["events"][i]["ts"]
    tstampu = time.asctime(time.gmtime(ts))
    tstampl = time.ctime(ts)
    print("""
    Handle:      {0}
    IP address:  {1}
    Event type:  {2} {3}
    Timestamp:   {4} UTC
                 {5} local time
    """.format(nick, ipaddr, event, channel, tstampu, tstampl))
