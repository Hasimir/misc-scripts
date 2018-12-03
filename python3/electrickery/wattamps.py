#!/usr/bin/env python3

from __future__ import division, print_function, unicode_literals

"""Conversion script to calculate watts to voltage to amps."""

watts = input("Enter watts value (if known): ")
volts = input("Enter volts value (if known): ")
amps = input("Enter amps value (if known): ")
nfi = None

if len(watts) == 0:
    w = None
else:
    try:
        w = float(watts)
    except Exception as e:
        raise e

if len(volts) == 0:
    v = None
else:
    try:
        v = float(volts)
    except Exception as e:
        raise e

if len(amps) == 0:
    a = None
else:
    try:
        a = float(amps)
    except Exception as e:
        raise e

if w:
    if v:
        if a:
            a == w / v
        else:
            a = w / v
    elif a:
        if v:
            v == w / a
        else:
            v = w / a
    else:
        nfi = "Must have two data points to calculate the third."
else:
    if v:
        if a:
            w = v * a
        else:
            nfi = "Must have two data points to calculate the third."
    else:
        nfi = "Must have two data points to calculate the third."

if nfi is not None:
    print("""
{0}
""".format(nfi))
else:
    print("""
Watts:  {0}
Volts:  {1}
Amps:   {2}
""".format(str(w), str(v), str(a)))
    
