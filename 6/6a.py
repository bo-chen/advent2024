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

pos = []
d = ""
spos = []
sdir = ""
dirs = {"^": [0,-1], ">": [1,0], "v": [0,1], "<" :[-1,0]}
dirorder = {"^": ">", ">": "v", "v": "<", "<" :"^"}
for j, l in enumerate(ls):
    ls[j] = list(l)
    l = ls[j]
    for i, c in enumerate(l):
        if c in dirs:
            pos = [i, j]
            d = c
            spos = [i, j]
            sdir = c
            ls[j][i] = "X"

while True:
    npos = [dirs[d][0] + pos[0], dirs[d][1] + pos[1]]
    if npos[0] < 0 or npos[0] >= len(ls[0]) or npos[1] < 0 or npos[1] >= len(ls):
        break
    if npos[0] == spos[0] and npos[1] == spos[1] and d == sdir:
        break
    if ls[npos[1]][npos[0]] == "#":
        d = dirorder[d]
    else:
        ls[npos[1]][npos[0]] = "X"
        pos = npos

t = 0
for l in ls:
    for c in l:
        if c == "X":
            t += 1

print(t)



