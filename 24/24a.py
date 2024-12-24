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

vs = {}
gates = []

i = 0
for l in ls:
    if l == "":
        break

    vs[l[:3]] = l[5] == "1"
    i += 1

for l in ls[i+1:]:
    m = re.search("^(.+) (.+) (.+) -> (.+)$", l)
    gates.append([m[1],m[2],m[3],m[4]])

togo = gates
while len(togo) > 0:
    ntogo = []
    for g in togo:
        inp1,op,inp2,out = g
        if inp1 in vs and inp2 in vs:
            if op == "AND":
                vs[out] = vs[inp1] and vs[inp2]
            elif op == "OR":
                vs[out] = vs[inp1] or vs[inp2]
            elif op == "XOR":
                vs[out] = vs[inp1] ^ vs[inp2]
        else:
            ntogo.append(g)
    togo = ntogo

t = 0
for k, v in vs.items():
    if k[0] == "z" and v == True:
        t += 2 ** int(k[1:])

print(t)