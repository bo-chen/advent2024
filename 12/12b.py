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
            ls.append(list(lstripped))

w = len(ls[0])
h = len(ls)

def expand_measure(i, j, l, seen, sides):
    seen.add((i, j))
    for dir in (0,1), (1,0), (-1,0), (0,-1):
        ni = i + dir[0]
        nj = j + dir[1]
        if ni < 0 or ni >= w or nj < 0 or nj >= h or ls[nj][ni] != l:
            sides.add(((i, j), (ni, nj)))
            continue
        else:
            if (ni, nj) in seen:
                continue
            expand_measure(ni, nj, l, seen, sides)

def measure(i, j):
    l = ls[j][i]
    if l == '0':
        return (0, 0)

    seen = set()
    sides = set()

    expand_measure(i, j, l, seen, sides)

    for i,j in seen:
        ls[j][i] = '0'

    p = 0
    while len(sides) > 0:
        p += 1
        p0, p1 = sides.pop()
        if p0[0] == p1[0]:
            ci = p0[0]
            lj = p0[1]
            rj = p1[1]
            for dir in (-1, 1):
                nci = ci
                while True:
                    nci += dir
                    if ((nci, lj), (nci, rj)) in sides:
                        sides.remove(((nci, lj), (nci, rj)))
                    else:
                        break

        if p0[1] == p1[1]:
            ui = p0[0]
            di = p1[0]
            cj = p0[1]
            for dir in (-1, 1):
                ncj = cj
                while True:
                    ncj += dir
                    if ((ui, ncj), (di, ncj)) in sides:
                        sides.remove(((ui, ncj), (di, ncj)))
                    else:
                        break

    return (len(seen), p)


t = 0
for j, l in enumerate(ls):
    for i, c in enumerate(l):
        a, p = measure(i, j)
        t += a * p

print(t)


