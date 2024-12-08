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

w = len(ls[0])
h = len(ls)

antd = {}
nodes = set()

for j, l in enumerate(ls):
    for i, c in enumerate(l):
        if c != ".":
            if c in antd:
                antd[c].append((i,j))
            else:
                antd[c] = [(i,j)]

def addnode(a1, a2):
    ni = 2 * a1[0] - a2[0]
    nj = 2 * a1[1] - a2[1]
    if ni >= 0 and ni < w and nj >= 0 and nj < h:
        nodes.add((ni, nj))

for ps in antd.values():
    for x in ps:
        for y in ps:
            if x == y:
                continue
            addnode(x, y)
            addnode(y, x)

print(len(nodes))



