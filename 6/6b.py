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

def stoia(pstr):
    return list(map(lambda x: int(x), pstr.split(",")))

def iatos(p):
    return ",".join(map(lambda x: str(x), p))

ls = []
with open(f'{source_dir}/in.txt') as fp:
    for line in fp:
        lstripped = line.strip()

        if lstripped != "":
            ls.append(lstripped)

spos = []
sdir = ""
dirs = {"^": np.array([0,-1]), ">": np.array([1,0]), "v": np.array([0,1]), "<" : np.array([-1,0])}
dirorder = {"^": ">", ">": "v", "v": "<", "<" :"^"}
for j, l in enumerate(ls):
    ls[j] = list(l)
    l = ls[j]
    for i, c in enumerate(l):
        if c in dirs:
            spos = np.array([i, j])
            sdir = c
            ls[j][i] = "P"

fm = [r[:] for r in ls]
def isloop(m, mark = False):
    pos = np.array([spos[0], spos[1]])
    d = sdir
    been = set()
    while True:
        been.add((pos[0], pos[1], d))
        npos = dirs[d] + pos
        if npos[0] < 0 or npos[0] >= len(m[0]) or npos[1] < 0 or npos[1] >= len(m):
            return False
        if (npos[0], npos[1], d) in been:
            return True
        if m[npos[1]][npos[0]] == "#":
            d = dirorder[d]
        else:
            if mark:
                m[npos[1]][npos[0]] = "X"
            pos = npos

t = 0
isloop(ls, True)
for j, l in enumerate(ls):
    print(j)
    for i, c in enumerate(l):
        if c == "X":
            fm[j][i] = "#"
            if isloop(fm):
                t += 1
            fm[j][i] = "X"

print(t)



