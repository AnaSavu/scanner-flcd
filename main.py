from ProgramInternalForm import PIF
from SymbolTable import ST
from scanner import *

if __name__ == "__main__":
    st = ST()
    pif = PIF()

    fileName = input("Name of the file: ")
    file = open(fileName, "r")

    for line in file:
        tokens = getTokens(line)


    print('Program Internal Form: ', pif)
    print('Symbol Table: ', st)
