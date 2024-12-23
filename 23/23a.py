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

condict = {}
trips = set()

def addconn(c1, c2):
    if c1 not in condict.keys():
        condict[c1] = set([c2])
    else:
        condict[c1].add(c2)
    if c2 not in condict.keys():
        condict[c2] = set([c1])
    else:
        condict[c2].add(c1)

    ct = 0
    inter = condict[c1].intersection(condict[c2])
    for c3 in inter:
        tk = tuple(sorted([c1, c2, c3]))
        if tk not in trips:
            trips.add(tk)
            if c1[0] == "t" or c2[0] == "t" or c3[0] == "t":
                ct += 1
    
    return ct


t = 0
for l in ls:
    c1 = l[:2]
    c2 = l[3:]
    t += addconn(c1, c2)
    

print(t)