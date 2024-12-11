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

stones = stoia(ls[0], " ")

def blink(ss):
    nss = []
    for s in ss:
        if s == 0:
            nss.append(1)
            continue
        sstr = str(s)
        if len(sstr) % 2 == 0:
            w = int(len(sstr) / 2)
            nss.append(int(sstr[:w]))
            nss.append(int(sstr[w:]))
        else:
            nss.append(s * 2024)

    return nss


for i in range(25):
    stones = blink(stones)

print(len(stones))

