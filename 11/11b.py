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

starts = stoia(ls[0], " ")

def blink(ss):
    nss = []
    for s in ss:
        if s == 0:
            nss.append(1)
            continue
        sstr = str(s)
        if len(sstr) % 2 == 0:
            w = int(len(sstr) / 2)
            nss.append(int(sstr[:w]))
            nss.append(int(sstr[w:]))
        else:
            nss.append(s * 2024)

    return nss

# cached counts single digit -> num_blinks -> {'cached': [(digit, blinks)], 'rest': [stones], 'total': n}
cached = {}
for i in range(10):
    cached[i] = {0: {'cache': [], 'rest': [i], 'total': 1}}

cached["s"] = {0: {'cache': [], 'rest': starts, 'total': len(starts)}}

def advanceCache(cdict):
    sc = cdict['cache']
    sr = cdict['rest']

    restblink = blink(sr)

    newcache = []
    newrest = []
    for s in restblink:
        if s < 10:
            newcache.append([s, 0])
        else:
            newrest.append(s)

    total = len(restblink)
    for s, n in sc:
        total += cached[s][n+1]['total']
        newcache.append([s, n+1])
    
    return {'cache': newcache, 'rest': newrest, 'total': total}

for i in range(1, 76):
    for j in range(10):
        cached[j][i] = advanceCache(cached[j][i - 1])
    cached['s'][i] = advanceCache(cached['s'][i - 1])
    test = 1 + 1

print(cached['s'][75]['total'])

