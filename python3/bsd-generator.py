#!/usr/bin/env python3

##
# Copyright (C) Ben McGinnes, 2014
# ben@adversary.org
# OpenPGP/GPG key:  0x321E4E2373590E5D
#
# Version:  0.0.1
#
# License:  Modified BSD
#
# https://www.gnu.org/copyleft/gpl.html
#
# Requirements:
#
# * Python 3.2 or later (developed with Python 3.4.x)
# * Converted from scripts initially developed with Python 2.7.x.
#
# Options and notes:
#
# Usage:  
#
##

__author__ = "Ben McGinnes <ben@adversary.org>"
__copyright__ = "Copyright © Benjamin D. McGinnes, 2014"
__copyrighta__ = "Copyright (C) Benjamin D. McGinnes, 2014"
__copyrightu__ = "Copyright \u00a9 Benjamin D. McGinnes, 2014"
__license__ = "Modified BSD"
__version__ = "0.0.1"

from datetime import datetime
import sys
import textwrap

print("""
    If entering all three options (start year, name and institution) on
    the command line then the name and institution must be included in
    quotation marks (e.g. "Jane Doe") in order to be assigned correctly to
    the license output.

    Three text files containing the license are created, one in plain
    text and the others in Unicode.
""")

l = len(sys.argv)

if l == 1:
    year1 = input("Enter the year to begin copyright from: ")
    name = input("Enter your name as you want it to appear on the copyright: ")
    inst = input("Enter the company or institution name: ")
elif l == 2:
    year1 = sys.argv[1]
    name = input("Enter your name as you want it to appear on the copyright: ")
    inst = input("Enter the company or institution name: ")
elif l == 3:
    year1 = sys.argv[1]
    name = sys.argv[2]
    inst = input("Enter the company or institution name: ")
elif l >= 4:
    year1 = sys.argv[1]
    name = sys.argv[2]
    inst = sys.argv[3]

year2 = str(datetime.now().year)

if year1 == year2:
    year3 = year2
else:
    year3 = year1+"-"+year2

text = "Neither the name of %s nor the %s name may be used to endorse or promote products derived from this software without specific prior written permission." % (name, inst)
wtext = textwrap.fill(text, 66).replace("\n", "\n    ")

template_a = """Copyright (C) %s, %s
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are
met:
  * Redistributions of source code must retain the above copyright
    notice, this list of conditions and the following disclaimer.
  * Redistributions in binary form must reproduce the above copyright
    notice, this list of conditions and the following disclaimer in
    the documentation and/or other materials provided with the
    distribution.
  * %s

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
"AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
""" % (year3, name, wtext)

template = """Copyright © %s, %s
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are
met:
  * Redistributions of source code must retain the above copyright
    notice, this list of conditions and the following disclaimer.
  * Redistributions in binary form must reproduce the above copyright
    notice, this list of conditions and the following disclaimer in
    the documentation and/or other materials provided with the
    distribution.
  * %s

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
"AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
""" % (year3, name, wtext)

template_u = """Copyright \u00a9 %s, %s
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are
met:
  * Redistributions of source code must retain the above copyright
    notice, this list of conditions and the following disclaimer.
  * Redistributions in binary form must reproduce the above copyright
    notice, this list of conditions and the following disclaimer in
    the documentation and/or other materials provided with the
    distribution.
  * %s

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
"AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
""" % (year3, name, wtext)

afile = open("LICENSE_a.txt", "w")
afile.write(template_a)
afile.close()

bfile = open("LICENSE.txt", "w")
bfile.write(template)
bfile.close()

cfile = open("LICENSE_u.txt", "w")
cfile.write(template_u)
cfile.close()
