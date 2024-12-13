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

t = 0
i = 0
while i < len(ls): 
    m = re.search("^Button A: X\+(\d+), Y\+(\d+)$", ls[i])
    a = (int(m[1]), int(m[2]))
    m = re.search("^Button B: X\+(\d+), Y\+(\d+)$", ls[i+1])
    b = (int(m[1]), int(m[2]))
    m = re.search("^Prize: X=(\d+), Y=(\d+)$", ls[i+2])
    p = (int(m[1]), int(m[2]))
    i += 3

    det = a[0] * b[1] - a[1] * b[0]
    adet = a[0] * p[1] - a[1] * p[0]
    bdet = p[0] * b[1] - p[1] * b[0]

    if bdet % det != 0 or adet % det != 0:
        continue
    buta = bdet // det
    butb = adet // det

    t += buta * 3 + butb

print(t)
