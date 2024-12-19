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

ts = ls[0].split(", ")
ps = []

for i in range(2, len(ls)):
    ps.append(ls[i])


store = {}

def checkPat(pat):
    if len(pat) == 0:
        return 1
    if pat in store.keys():
        return store[pat]

    tr = 0
    for tow in ts:
        if pat.startswith(tow):
            r = checkPat(pat[len(tow):])
            tr += r
    
    store[pat] = tr
    return tr

num = 0
for pat in ps:
    num += checkPat(pat)

print(num)


    