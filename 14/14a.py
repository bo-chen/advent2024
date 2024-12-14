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

aw = 101
ah = 103


robots = []
for l in ls:
    m = re.search("^p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)$", l)
    r = [np.array([int(m[1]), (int(m[2]))]),np.array([int(m[3]), int(m[4])])]
    robots.append(r)

qt = [0, 0, 0, 0]

for r in robots:
    newp = r[0] + 100 * r[1]
    newp[0] = newp[0] % aw
    newp[1] = newp[1] % ah
    q = 0 

    if newp[0] == 50:
        continue

    if newp[0] > 50:
        q += 1
    
    if newp[1] == 51:
        continue

    if newp[1] > 51:
        q += 2

    qt[q] += 1


print(qt[0] * qt[1] * qt[2] * qt[3])
