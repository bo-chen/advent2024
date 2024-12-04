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

# down
dirs = [[[-1,-1],[1,-1],[-1,1],[1,1]], 
        #r
        [[-1,-1],[-1,1],[1,-1],[1,1]], 
        #l
        [[1,-1],[1,1],[-1,-1],[-1,1]],
        #u 
        [[-1,1],[1,1],[-1,-1],[1,-1]]
        ]

letters = "MMSS"
def isxmas(x, y):
    if ls[y][x] != "A":
        return False

    for inds in dirs:
        allt = True
        for i in range(4):
            ind = inds[i]
            ny = y + ind[1]
            nx = x + ind[0]
            if nx < 0 or nx >= len(ls[0]):
                allt = False
                break
            if ny < 0 or ny >= len(ls):
                allt = False
                break
            if ls[ny][nx] != letters[i]:
                allt = False
                break
        if allt:
            return True
    
    return False

t = 0
for y in range(len(ls)):
    for x in range(len(ls[0])):
        if isxmas(x, y):
            t += 1

print(t)

