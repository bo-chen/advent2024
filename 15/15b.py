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
    nl = []
    for x, c in enumerate(l):
        if c == "@":
            rp = np.array([2*x, y])
            nl = nl + ["@", "."]
        if c == ".":
            nl = nl + list("..")
        if c == "#":
            nl = nl + list("##")
        if c == "O":
            nl = nl + list("[]")

    m.append(list(nl))
    i += 1

def move(p, dir, depth):
    newp = p + dir
    c = m[newp[1]][newp[0]]
    myupdate = [[depth, [newp[0],newp[1]], m[p[1]][p[0]]], [depth, [p[0],p[1]], "."] ]
    if c == ".":
        return True, myupdate
    elif c == "#":
        return False, []
    elif c in set(["[","]"]):
        r, updates = move(newp, dir, depth + 1)
        if r:
            if dir[0] == 0:
                otherside = []
                if c == "[":
                    otherside = newp + np.array([1,0])
                elif c == "]": 
                    otherside = newp + np.array([-1,0])
                else:
                    print("bad3")
                    exit(1)
                r, u2 = move(otherside, dir, depth + 1)
                return r,  updates + u2 + myupdate
            else:
                return True, updates + myupdate
        else:
            return False, []
    else:
        print("Bad")
        exit(1)

def robotmove(p, dir):
    r, us = move(p, dir, 0)
    if r:
        us.sort(reverse= True)
        for d, pos, c in us:
            m[pos[1]][pos[0]] = c
        return True

        
dirs = {"^": np.array([0,-1]), ">": np.array([1,0]), "v": np.array([0,1]), "<": np.array([-1,0])}
step = 0

for j in range(i+1, len(ls)):
    for c in list(ls[j]):
        #print(step)
        #print(c)
        step += 1
        if c in dirs:
            d = dirs[c]
            r = robotmove(rp, d)
            #pm(m)
            if r:
                rp = rp + d
        else:
            print("bad2")
            exit(1)

t = 0
for y, l in enumerate(m):
    for x, c in enumerate(l):
        if c == "[":
            t += x + 100 * y

pm(m)
print(t)






