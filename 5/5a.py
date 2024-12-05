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

        ls.append(lstripped)

i = 0
rules = []
for l in ls:
    i += 1
    if l == "":
        break
    rules.append([int(l[:2]), int(l[3:])])

t = 0
for j in range(i, len(ls)):
    ns = stoia(ls[j])
    good = True
    for r in rules:
        if r[0] not in ns or r[1] not in ns:
            continue
        if ns.index(r[0]) > ns.index(r[1]):
            good = False
            break
    if good:
        t += ns[math.floor(len(ns) / 2)]
    
print(t)



