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

t = 0
doit = True
for l in ls:
    ms = re.findall("(don't\(\))|(do\(\))|mul\((\d+),(\d+)\)",l)
    for m in ms:
        if len(m[0]) > 0:
            doit = False
        elif len(m[1]) > 0:
            doit = True
        elif doit:
            t += int(m[2]) * int(m[3]) 

print(t)