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

fileidlocsize =[]
spacelocsize = []
fileid = 0
loc = 0

l = list(map(lambda x: int(x), ls[0]))
i = 0
while i < len(l):
    fileidlocsize.append([fileid, loc, l[i]])
    fileid += 1
    loc += l[i]
    i += 1
    if i < len(l):
        spacelocsize.append([loc, l[i]])
        loc += l[i]
        i += 1

filei = 0
spacei = 0
checksum = 0

for i in range(len(fileidlocsize) - 1, -1, -1):
    fid, fl, fs = fileidlocsize[i]
    while fs > 0:
        sl, ss = spacelocsize[0]
        if sl >= fl:
            lsubt = (fl + fl + fs - 1) * fs / 2
            checksum += fid * lsubt
            break
        if ss > fs:
            lsubt = (sl + sl + fs - 1) * fs / 2
            checksum += fid * lsubt
            spacelocsize[0] = [sl + fs, ss - fs]
        else:
            lsubt = (sl + sl + ss - 1) * ss / 2
            checksum += fid * lsubt
            spacelocsize.pop(0)
        fs = fs - ss

print(checksum)



    






