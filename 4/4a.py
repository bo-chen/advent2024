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

word = "XMAS"
def isxmas(x, y, dirx, diry):
    for i in range(0, 4):
        ny = y+i*diry
        nx = x+i*dirx
        if nx < 0 or nx >= len(ls[0]):
            return False
        if ny < 0 or ny >= len(ls):
            return False
        if ls[y+i*diry][x+i*dirx] != word[i]:
            return False
    
    return True

t = 0
for y in range(len(ls)):
    for x in range(len(ls[0])):
        for dirx in [-1, 0, 1]:
            for diry in [-1, 0, 1]:
                if dirx == 0 and diry == 0:
                    continue
                if isxmas(x, y, dirx, diry):
                    t += 1

print(t)

