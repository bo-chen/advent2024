import math
import numpy as np
import os
import re
import sys
import copy
from functools import *
from pathlib import Path

source_path = Path(__file__).resolve()
source_dir = source_path.parent

def pm(m):
    for r in m:
        s = ""
        for c in r:
            print(c, end="")
        print("")

def cpm(m):
    return [r[:] for r in m]

def stoia(pstr, delim = ","):
    return list(map(lambda x: int(x), pstr.strip().split(delim)))

def iatos(p):
    return ",".join(map(lambda x: str(x), p))

ls = []
with open(f'{source_dir}/in.txt') as fp:
    for line in fp:
        lstripped = line.strip()

        if lstripped != "":
            ls.append(lstripped)


num2coord = {"7": (0,0), "8": (1,0), "9": (2,0), "4": (0,1), "5": (1,1), "6": (2,1), "1": (0,2), "2": (1,2), "3":(2,2), "0": (1,3), "A": (2,3)}
dir2coord = {"^": (1,0), "A": (2,0), "<": (0,1), "v": (1,1), ">": (2,1)}

ca = {}

def padcommands(targets, pads, missing = (0,0), c = None):
    ck = (str(targets), pads, c)
    if ck in ca.keys():
        return ca[ck]

    pad = {}
    if pads == "num":
        pad = num2coord
    else:
        pad = dir2coord

    if c is None:
        c = pad["A"]
    if len(targets) == 0:
        return [[]]
    t = targets[0]

    tc = pad[t]
    dx = tc[0] - c[0]
    dy = tc[1] - c[1]
    rest = padcommands(targets[1:], pads, missing, tc)
    perms = []
    if c[1] == missing[1] and tc[0] == missing[0]:
        r = []
        if dy > 0:
            r = r + list("v" * dy)
        elif dy < 0:
            r = r + list("^" * abs(dy))
        if dx > 0:
            r = r + list(">" * dx)
        elif dx < 0:
            r = r + list("<" * abs(dx))
        prefix = r + ["A"]
        for p in rest:
            perms.append(prefix + p)

    else:
        r = []
        if dx > 0:
            r = r + list(">" * dx)
        elif dx < 0:
            r = r + list("<" * abs(dx))
        if dy > 0:
            r = r + list("v" * dy)
        elif dy < 0:
            r = r + list("^" * abs(dy))
        prefix = r + ["A"]
        for p in rest:
            perms.append(prefix + p)

        rr = list(reversed(r))
        if rr != r or c[0] == missing[0] and tc[1] == missing[1]:
            prefix = list(reversed(r)) + ["A"]
            for p in rest:
                perms.append(prefix + p)

    ca[ck] = perms
    return perms

t = 0
for l in ls:
    l
    r0s = padcommands(l, "num", (0,3))
    r1s = []
    for r0 in r0s:
        r1s = r1s + padcommands(r0, "dir", (0,0))
    r2s = []
    for r1 in r1s:
        r2s = r2s + padcommands(r1, "dir", (0,0))

    minil = 99999
    for r2 in r2s:
        if len(r2) < minil:
            minil = len(r2)

    print(f"{minil} * {int(l[:3])}")
    t += minil * int(l[:3])


print(t)
