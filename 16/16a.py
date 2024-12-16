import math
import numpy as np
import os
import re
import sys
import copy
from functools import *
from pathlib import Path
import heapq as hq


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

m = []
s = []
e = []
dir = (1,0)
for y, l in enumerate(ls):
    if len(l) == 0:
        break
    m.append(list(l))
    for x, c in enumerate(l):
        if c == "S":
            s = (x, y)
        elif c == "E":
            e = (x, y)


rotates = {(0,-1): [(-1,0), (1,0)], \
           (0,1): [(1,0), (-1,0)], \
           (1,0): [(0,-1), (0,1)], \
           (-1,0): [(0,1), (0,-1)]}

def search():
    nq = []
    done = set((s, dir))
    hq.heappush(nq, (0, (s, dir)))
    while len(nq) > 0:
        c, (p, d) = hq.heappop(nq)
        if (p, d) in done:
            continue

        done.add((p, d))

        if p == e:
            return c
        newp = tuple(np.array(p)+ np.array(d))
        if m[newp[1]][newp[0]] != "#":
            nel = (newp, d)
            if nel not in done:
                hq.heappush(nq, (c+1, nel))
        for nd in rotates[d]:
            nel = (p, nd)
            if nel not in done:
                hq.heappush(nq, (c+1000, nel))

print(search())
        


        

