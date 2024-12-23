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
cliqs = set()

def addconn(c1, c2):
    if c1 not in condict.keys():
        condict[c1] = set([c2])
    else:
        condict[c1].add(c2)
    if c2 not in condict.keys():
        condict[c2] = set([c1])
    else:
        condict[c2].add(c1)

def encliqs(connected, notchecked, badchecked):
    if len(notchecked) == 0 and len(badchecked) == 0:
        cliqs.add(tuple(sorted(connected)))
        return
    
    nnc = notchecked.copy()
    nbc = badchecked.copy()
    for c in notchecked:
        ccs = condict[c]
        encliqs(connected.union(set([c])), nnc.intersection(ccs), nbc.intersection(ccs))
        nnc.remove(c)
        nbc.add(c)

t = 0
for l in ls:
    c1 = l[:2]
    c2 = l[3:]
    addconn(c1, c2)
    
encliqs(set(), set(condict.keys()), set())
maxc = set()
for cliq in cliqs:
    if len(cliq) > len(maxc):
        maxc = cliq

print(iatos(maxc))