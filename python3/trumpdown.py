#! /usr/bin/env python3

import datetime
import time

# All times have been converted to UTC or seconds since the epoch.

epoch = datetime.datetime(1970, 1, 1)
dtd0 = datetime.date(2017, 1, 21)
dtd1 = datetime.date(2021, 1, 21)
dtd2 = datetime.date(2025, 1, 21)
dtt0 = datetime.datetime(2017, 1, 20, 17, 0, 0)
dtt1 = datetime.datetime(2021, 1, 20, 17, 0, 0)
dtt2 = datetime.datetime(2025, 1, 20, 17, 0, 0)
today = datetime.date.today()
now0 = datetime.datetime.utcnow()
now1 = time.time()
now2 = time.ctime(now1)
now3 = time.asctime(time.gmtime(now1))

r0 = (dtd1 - today).days
r1 = (dtd2 - today).days
r2 = (today - dtd0).days

d0 = (dtt1 - now0)
d0ts = d0.total_seconds()
d0str = str(datetime.timedelta(seconds=abs(d0ts)))

d1 = (dtt2 - now0)
d1ts = d1.total_seconds()
d1str = str(datetime.timedelta(seconds=abs(d1ts)))

d2 = (now0 - dtt0)
d2ts = d2.total_seconds()
d2str = str(datetime.timedelta(seconds=abs(d2ts)))

print("""
Time until Trump's first term is over:

    {0} days
    {1}

Time until Trump's second term is over:

    {2} days
    {3}

Time Trump has currently spent in office:

    {4} days
    {5}

""".format(r0, d0str, r1, d1str, r2, d2str))


