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
with open(f'{source_dir}/s.txt') as fp:
    for line in fp:
        lstripped = line.strip()

        if lstripped != "":
            ls.append(lstripped)
mh = len(ls)
mw = len(ls[0])

def followtrail(p, h):
    if p[0] < 0 or p[0] >= mw or p[1] < 0 or p[1] >= mh:
        return 0
    if h != int(ls[p[1]][p[0]]):
        return 0
    if h == 9:
        return 1
    else:
        return followtrail([p[0]-1, p[1]], h+1) + followtrail([p[0]+1, p[1]], h+1) + followtrail([p[0], p[1]-1], h+1) +followtrail([p[0], p[1]+1], h+1)

t = 0
for y, l in enumerate(ls):
    for x, c in enumerate(l):
        if c == '0':
            t += followtrail([x,y], 0)

print(t)
        

