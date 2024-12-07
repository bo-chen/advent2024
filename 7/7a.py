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

def check(r, vs):
    if len(vs) == 1:
        return vs[0] == r
    
    return check(r, [int(vs[0]) * int(vs[1])] + vs[2:]) or check(r, [int(vs[0]) + int(vs[1])] + vs[2:])

t = 0
for l in ls:
    r, vstr = l.split(":")
    r = int(r)
    vs = list(vstr.split(" "))
    vs.remove("")
    if check(r, vs):
        t += r

print(t)
