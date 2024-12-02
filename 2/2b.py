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

        if lstripped != "":
            ls.append(lstripped)

def safeseq(xs):
    lx = int(xs[0])
    unsafe = False
    if lx == int(xs[1]):
        return False
    inc = lx < int(xs[1])
    for i in range(1, len(xs)):
        c = int(xs[i])
        if inc:
            if (c - lx) < 1 or (c - lx) > 3:
                unsafe = True
                break
        else:
            if (lx - c) < 1 or (lx - c) > 3:
                unsafe = True
                break
        lx = c
    if not unsafe:
        return True
    else:
        return False

safes = 0
for l in ls:
    xs = re.split("\s+", l)
    for i in range(len(xs)):
        txs = xs[:i] + xs[i+1:]
        if safeseq(txs):
            safes += 1
            break

print(safes)

