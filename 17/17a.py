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

        ls.append(lstripped)


rega = int(ls[0][12:])
regb = int(ls[1][12:])
regc = int(ls[2][12:])

prog = stoia(ls[4][9:])

def comboop(v, rega, regb, regc):
    if v < 4:
        return v
    if v == 4:
        return rega
    if v == 5:
        return regb
    if v == 6:
        return regc
    exit(1)

def runp(ra, rb, rc):
    r = []
    pc = 0
    while True:
        if pc >= len(prog):
            break

        ins = prog[pc]
        operand = prog[pc+1]

        if ins == 0:
            ra = ra // (2 ** comboop(operand, ra, rb, rc))
        if ins == 1:
            rb = rb ^ operand
        if ins == 2:
            rb = comboop(operand, ra, rb, rc) % 8
        if ins == 3:
            if ra != 0:
                pc = operand
                continue
        if ins == 4:
            rb = rb ^ rc
        if ins == 5:
            r.append(comboop(operand, ra, rb, rc) % 8)
        if ins == 6:
            rb = ra // (2 ** comboop(operand, ra, rb, rc))
        if ins == 7:
            rc = ra // (2 ** comboop(operand, ra, rb, rc))

        pc += 2

    return r

print(iatos(runp(rega, regb, regc)))




    


