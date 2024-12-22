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

def nextnum(n):
    n = (n << 6 ^ n) % 16777216
    n = ((n >> 5) ^ n) % 16777216
    n = ((n << 11) ^ n) % 16777216
    return n

t = 0
totalbprices = {}
for l in ls:
    n = int(l)
    deltas = [0, 0, 0, 0]
    bprices = {}
    for i in range(3):
        lastp = n % 10
        n = nextnum(n)
        p = n % 10
        deltas[i % 4] = p - lastp

    for i in range(3, 2000):
        n = nextnum(n)
        lastp = p
        p = n % 10
        deltas[i % 4] = (p - lastp) 
        pk = tuple(deltas[(i%4)+1:] + deltas[:(i%4)+1])
        if pk not in bprices.keys():
            bprices[pk] = p

    for k, p in bprices.items():
        if k in totalbprices.keys():
            totalbprices[k].append(p)
        else:
            totalbprices[k] = [p]

maxt = 0
for ps in totalbprices.values():
    maxt = max(maxt, sum(ps))

print(maxt)