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

blocks = set()
i = 0
while i < 1024:
    m = re.search("^(\d+),(\d+)$", ls[i])
    blocks.add((int(m[1]),int(m[2])))
    i += 1

end = (70,70)

def pathd(bs):
    seen = set((0,0))
    q = [((0,0),0)]

    while len(q) > 0:
        cp, d = q.pop(0)
        if cp == end:
            return d

        for dx, dy in [(0,1),(1,0),(0,-1), (-1, 0)]:
            nx = cp[0] + dx
            ny = cp[1] + dy
            if nx >= 0 and nx <= 70 and ny >= 0 and ny <= 70 and (nx, ny) not in seen and (nx, ny) not in blocks:
                seen.add((nx, ny))
                q.append(((nx, ny), d+1))
    
    return -1

while i < len(ls):
    m = re.search("^(\d+),(\d+)$", ls[i])
    blocks.add((int(m[1]),int(m[2])))
    d = pathd(blocks)
    if d == -1:
        print(f"{m[1]},{m[2]}")
        exit(0)
    
    i += 1

print("Bad")
        




