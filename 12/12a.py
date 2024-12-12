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

w = len(ls[0])
h = len(ls)

def measure(i, j, l = None, seen = set()):
    first = False
    if l is None:
        l = ls[j][i]
        if l == '0':
            return (0, 0)
        first = True

    seen.add((i, j))
    a = 1
    p = 0
    for dir in (0,1), (1,0), (-1,0), (0,-1):
        ni = i + dir[0]
        nj = j + dir[1]
        if ni < 0 or ni >= w or nj < 0 or nj >= h or ls[nj][ni] != l:
            p += 1
            continue
        else:
            if (ni, nj) in seen:
                continue
            na, np = measure(ni, nj, l, seen)
            a += na
            p += np
    
    if first:
        for i,j in seen:
            ls[j][i] = '0'

    return (a, p)

nls = []
for l in ls:
    nls.append(list(l))

ls = nls

t = 0
for j, l in enumerate(ls):
    for i, c in enumerate(l):
        a, p = measure(i, j)
        t += a * p

print(t)


