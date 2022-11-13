#!/usr/bin/python3

from Modules import intro
from Modules import response
import sys



f = open(sys.argv[1])
lines = f.readlines()

def main():
    intro.introMsg()
    response.responseCheck(lines)
    response.resultMsg()

main()
f.close()
