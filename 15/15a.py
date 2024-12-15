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

        ls.append(lstripped)

m = []
i = 0
rp = 0
for y, l in enumerate(ls):
    if len(l) == 0:
        break
    m.append(list(l))
    for x, c in enumerate(l):
        if c == "@":
            rp = np.array([x, y])

    i += 1

def move(p, dir):
    np = p + dir
    if m[np[1]][np[0]] == ".":
        m[np[1]][np[0]] = m[p[1]][p[0]]
        m[p[1]][p[0]] = "."
        return True
    elif m[np[1]][np[0]] == "#":
        return False
    elif m[np[1]][np[0]] == "O":
        r = move(np, dir)
        if r:
            m[np[1]][np[0]] = m[p[1]][p[0]]
            m[p[1]][p[0]] = "."
            return True
        else:
            return False
    else:
        print("Bad")
        exit(1)
        
dirs = {"^": np.array([0,-1]), ">": np.array([1,0]), "v": np.array([0,1]), "<": np.array([-1,0])}
for j in range(i+1, len(ls)):
    for c in list(ls[j]):
        if c in dirs:
            d = dirs[c]
            r = move(rp, d)
            if r:
                rp = rp + d
        else:
            print("bad2")
            exit(1)

t = 0
for y, l in enumerate(m):
    for x, c in enumerate(l):
        if c == "O":
            t += x + 100 * y

print(t)






