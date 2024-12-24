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

vals = {}
gates = []

i = 0
for l in ls:
    if l == "":
        break

    vals[l[:3]] = l[5] == "1"
    i += 1

outswaps = {}
outswaps["kcd"] = "z27"
outswaps["pfn"] = "z23"
outswaps["shj"] = "z07"
outswaps["tpk"] = "wkb"
outswaps["wkb"] = "tpk"
outswaps["z07"] = "shj"
outswaps["z23"] = "pfn"
outswaps["z27"] = "kcd"

for l in ls[i+1:]:
    m = re.search("^(.+) (.+) (.+) -> (.+)$", l)
    out = m[4]
    if out in outswaps:
        out = outswaps[out]
    gates.append([m[1],m[2],m[3],out])

def run(vs):
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

def istovs(x, y):
    vs = {}
    for i in range(45):
        vs["x" + str(i).zfill(2)] = (x % 2) == 1
        x = x // 2 
        vs["y" + str(i).zfill(2)] = (y % 2) == 1
        y = y // 2 
    return vs

def vstoi(vs):
    t = 0
    for k, v in vs.items():
        if k[0] == "z" and v == True:
            t += 2 ** int(k[1:])
    
    return t

    
def test(prefix, x, y, r, p):
    vs = istovs(x,y)
    run(vs)
    out = vstoi(vs)
    if out != r:
        print(f"{prefix}: {x} + {y} , expected {r} got {out} : expected {r>>p} got {out >> p}")

        return False

    return True

for p in range(45):

    test(f"{p}: 1+0", 1<<p, 0, 1<<p, p)
    test(f"{p}: 0+1", 0, 1<<p, 1<<p, p)
    test(f"{p}: 1+1", 1<<p, 1<<p, 1<<(p + 1), p)

    if p < 44:
        test(f"{p}: 1+11", 1<<p, (1<<(p+1)) + (1<<p), 1<<(p+2), p)
        test(f"{p}: 11+1", (1<<(p+1)) + (1<<p), 1<<p, 1<<(p+2), p)
        test(f"{p}: 11+11", (1<<(p+1)) + (1<<p), (1<<(p+1)) + (1<<p), (1<<(p+2)) + (1<<(p+1)), p)





