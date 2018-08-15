#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import unicode_literals
from __future__ import print_function

import datetime
import os.path
import requests
import sys

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
Pastes the contents of a file to bpaste.net.

Upon success it prints the URL of the paste and a URL to remove the paste to
STDOUT.  Upon failure it prints a message to try again or manually.

Requires a relative subdirectory called "pasters/" for persistent storage of
some metadata (lexers and paste records for manual deletion).

Usage: bpaste.py <path/to/filename> <lexer> <expiration>
"""

bpastehist = os.path.expanduser("~/bin/pasters/bpasted_history.txt")
lexicon = os.path.expanduser("~/bin/pasters/bpaste_lexers.txt")
lexers = []
bpastelog = os.path.realpath(bpastehist)
lexfile = os.path.realpath(lexicon)
with open(lexfile, "r") as f:
    lexed = f.readlines()

for lexx in lexed:
    lexers.append(lexx.strip())

if len(sys.argv) >= 4:
    filename = sys.argv[1]
    lexer = sys.argv[2]
    expire = sys.argv[3]
elif len(sys.argv) == 3:
    filename = sys.argv[1]
    lexer = sys.argv[2]
    expire = input("Expiration (default is 1 week): ")
elif len(sys.argv) == 2:
    filename = sys.argv[1]
    lexer = input("File format (optional): ")
    expire = input("Expiration (default is 1 week): ")
else:
    filename = input("Enter the path and filename to paste: ")
    lexer = input("File format (optional): ")
    expire = input("Expiration (default is 1 week): ")

if len(lexer) == 0:
    lexer = None
    lex = None
    lxr = None
else:
    lex = lexer.lower()
    lxr = None

if expire.lower().startswith("d") is True:
    die = "1day"
elif expire.lower().startswith("m") is True:
    die = "1month"
elif expire.lower().startswith("n") is True:
    die = "never"
elif expire.lower().startswith("w") is True:
    die = "1week"
elif expire.lower().startswith("1d") is True:
    die = "1day"
elif expire.lower().startswith("1m") is True:
    die = "1month"
elif expire.lower().startswith("0") is True:
    die = "never"
elif expire.lower().startswith("1w") is True:
    die = "1week"
else:
    die = "1week"

if lexer is not None and lexers.count(lex) > 0:
    lxi = lexers.index(lex)
    lxr = lexers[lxi]
elif lexer is not None and lexers.count(lex) == 0:
    # add logic to determine file type based on extension
    # or maybe using python-magic/libmagic
    # or use input that does not match list to match own list
    if lex == "py3":
        lxr = "python3"
    elif lex == "py2":
        lxr = "python"
    elif lex == "python2":
        lxr = "python"
    elif lex == "org":
        lxr = "text"
    elif lex == "orgmode":
        lxr = "text"
    elif lex == "org-mode":
        lxr = "text"
    elif lex == "txt":
        lxr = "text"
    elif lex == "markdown":
        lxr = "md"
    elif lex == "htm":
        lxr = "html"
    elif lex == "xhtml":
        lxr = "html"
    elif lex == "sgml":
        lxr = "xml"
    elif lex == "dita":
        lxr = "xml"
    elif lex == "ditamap":
        lxr = "xml"
    else:
        pass
else:
    # final check for associating filetype with lexer to be added.
    pass

if lxr is None:
    lxr = "text"

with open(filename, "r") as f:
    code = f.read()

url = "https://bpaste.net"
payload = {"code": code, "lexer": lxr, "expiry": die}
if die != "never":
    exp = "expires in one {0}".format(die[1:])
else:
    exp = "never expires"

response = requests.post(url, verify=True, data=payload)
runtime = datetime.datetime.utcnow().isoformat()[:19]

if response.ok is True:
    removals = response.text.splitlines()[-9]
    removal = removals.strip().replace('"', ' ').split()[2]
    remover = url + removal
    servtime = response.headers["Date"]
    logtext = "{0}Z: {1} - {2} - {3} - {4} - {5}\n".format(
        runtime, servtime, filename, exp, response.url, remover)
    with open(bpastelog, "a") as f:
        f.write(logtext)
    print(response.url)
    print(remover)
else:
    with open(bpastelog, "a") as f:
        f.write("{0}Z: paste of {1} failed.\n")
    print("HTTP Post failed; try again or manually at: {0}".format(url))
