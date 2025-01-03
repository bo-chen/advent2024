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
with open(f'{source_dir}/s.txt') as fp:
    for line in fp:
        lstripped = line.strip()

        if lstripped != "":
            ls.append(lstripped)

xs = []
ys = []

for l in ls:
    x = l[:5]
    y = l[8:]
    xs.append(x)
    ys.append(y)

xs.sort()
ys.sort()

t = 0
for x in xs:
    c = 0
    for y in ys:
        if y == x:
            c += 1

    t += c * int(x)

print(t)
