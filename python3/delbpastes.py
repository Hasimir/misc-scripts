#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import unicode_literals
from __future__ import print_function

import datetime
import os.path
import requests

# Copyright © Benjamin D. McGinnes, 2018
# Copyright (c) Benjamin D. McGinnes, 2018
#
# Ben McGinnes <ben@adversary.org>, 0x321E4E2373590E5D
# OpenPGP: DB4724E6FA4286C92B4E55C4321E4E2373590E5D
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
Removes all pastes made with bpaste.py.

A 404 response means it was already deleted, a 200 response means it was
successfully deleted and anything else probably means the request never reached
bpaste.net.
"""

bpastehist = os.path.expanduser("~/bin/pasters/bpasted_history.txt")
bpastegone = os.path.expanduser("~/bin/pasters/bpasted_removed.txt")
bpastelog = os.path.realpath(bpastehist)
bpastedel = os.path.realpath(bpastegone)

with open(bpastelog, "r") as f:
    bpastes = f.readlines()

with open(bpastedel, "r") as f:
    deleted = f.readlines()

history = []
repeats = []

for paste in bpastes:
    line = paste.split()[-1].strip()
    history.append(line)

for void in deleted:
    if history.count(void) > 0:
        history.remove(void)
    else:
        repeats.append(void)

for url in history:
    utc = datetime.datetime.utcnow().isoformat()
    try:
        r = requests.get(url, verify=True)
        with open(bpastedel, "a") as f:
            f.write("{0}\n".format(url))
        print("{0}Z: {1} - {2}".format(utc, url, r.status_code))
    except Exception as e:
        print("{0}Z: Cannot remove {0} due to: {1}".format(utc, url, e))

if len(repeats) > 0:
    for url in repeats:
        utc = datetime.datetime.utcnow().isoformat()
        try:
            r = requests.get(url, verify=True)
            print("{0}Z: {1} - {2}".format(utc, url, r.status_code))
        except Exception as e:
            print("{0}Z: Cannot remove {0} due to: {1}".format(utc, url, e))
else:
    pass
