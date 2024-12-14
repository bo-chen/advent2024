import math
import numpy as np
import os
import re
import sys
import copy
import time
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


for i in range(10404):
        
    m = []
    for j in range(103):
        m.append( ["."] * 101)

    tx = 0
    xs = []
    for ri, r in enumerate(robots):
        newp = r[0] + i * r[1]
        newp[0] = newp[0] % aw
        newp[1] = newp[1] % ah
        tx += newp[0]
        xs.append(newp[0])

        m[newp[1]][newp[0]] = "X"

    qt = [0, 0]
    for x in xs:
        if x < tx / 2:
            qt[0] += 1 #tx - x 
        elif x > tx / 2:
            qt[1] += 1 #x - tx

    # 83, 184
    if (i - 83) % 101 == 0  or qt[0] == qt[1]:
        pm(m)
        print("")
        print(i)
        print("")
        print("")
        
        time.sleep(0.2)
