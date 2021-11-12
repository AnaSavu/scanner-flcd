import string

from ProgramInternalForm import PIF
from SymbolTable import ST
from scanner import *
from FiniteAutomata import FA
from S import *

if __name__ == "__main__":
    st = ST()
    pif = PIF()
    faInt = FA('faIntegerConstant.in')
    faIdn = FA('faIdentifier.in')

    # Q = ['q1', 'q2']

    # E1 = list(string.ascii_lowercase)
    # E2 = list(string.ascii_uppercase)
    # E = []
    # E.append('0')
    # E.append('1')
    # E.append('2')
    # E.append('3')
    # E.append('4')
    # E.append('5')
    # E.append('6')
    # E.append('7')
    # E.append('8')
    # E.append('9')
    #
    # E += E1 + E2
    #
    # S = S('SFile.in', Q, E)
    # S.writeData()

    scanner = Scanner(st, pif, "token.in", "p1.txt", faInt, faIdn)
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
