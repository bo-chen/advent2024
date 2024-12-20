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

m = []
s = []
e = []
for y, l in enumerate(ls):
    for x, c in enumerate(l):
        if c == "S":
            s = (x, y)
        if c == "E":
            e = (x, y)
    m.append(list(l))

# returns {coord: distfromstart}
def builddist(start, end):
    q = [(start, 0)]
    
    seen = {start: 0}
    while len(q) > 0:
        c, d = q.pop(0)
        if c == end:
            return seen
        
        for dir in [(1,0), (-1,0), (0, -1), (0, 1)]:
            nc = (c[0] + dir[0], c[1] + dir[1])
            if nc in seen.keys():
                continue
            if m[nc[1]][nc[0]] == "#":
                continue
            q.append((nc, d+1))
            seen[nc] = d+1

distfroms = builddist(s, e)
distfrome = builddist(e, s)

baseline = distfroms[e]

t = 0
for n1, n1dfroms in distfroms.items():
    for n2, n2dfrome in distfrome.items():
        delta = abs(n1[0]-n2[0]) + abs(n1[1] - n2[1])
        if delta <= 20 and baseline - (n1dfroms + n2dfrome + delta) >= 100:
            t += 1

print(t)