from ProgramInternalForm import PIF
from SymbolTable import ST
from scanner import *

if __name__ == "__main__":
    st = ST()
    pif = PIF()

    scanner = Scanner(st, pif, "token.in", "p3.txt")
    scanner.scan()

    # print()
    # print('Program Internal Form: ')
    # for line in scanner.getPIF():
    #     print(line)
    #
    # print()
    # print('Symbol Table: ')
    # for line in scanner.getST():
    #     print(line)
