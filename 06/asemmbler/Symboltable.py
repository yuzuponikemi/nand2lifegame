# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 20:56:16 2021

@author: IKM1YH

SymbolTable: Keeps a correspondence between symbolic labels and numeric
addresses.
Routine Arguments Returns Function
Constructor — — Creates a new empty symbol
table.
addEntry symbol (string),
address (int)
— Adds the pair (symbol,
address) to the table.
contains symbol (string) Boolean Does the symbol table contain
the given symbol?
GetAddress symbol (string) int Returns the address associated
with the symbol.


Predefined Symbols Any Hack assembly program is allowed to use the following
predefined symbols.
Label RAM address (hexa)
SP 0 0x0000
LCL 1 0x0001
ARG 2 0x0002
THIS 3 0x0003
THAT 4 0x0004
R0-R15 0-15 0x0000-f
SCREEN 16384 0x4000
KBD 24576 0x6000

"""

class SymbolTable():
    '''
    Keeps a correspondence between symbolic labels and numeric
    addresses.
    '''
    rs = {('R'+str(n)):n for n in range(0,16)}
    defa = {'SP':0,'LCL':1, 'ARG':2,'THIS':3,'THAT':4, 'SCREEN':16384,\
                       'KBD':24576}

    def __init__(self):
        '''Creates a new empty symbol
        table.'''
        
        self.sbltbl = dict(SymbolTable.rs,**SymbolTable.defa)
        
        
    def addEntry(self, symbol, address):
        '''Adds the pair (symbol,
        address) to the table.'''
        self.sbltbl[symbol] = address
        
    def contains(self, symbol):
        '''Does the symbol table contain
        the given symbol?'''
        return (symbol in self.sbltbl) #Boolean 
    
    def GetAddress(self,symbol):
        '''Returns the address associated with the symbol'''
        return self.sbltbl[symbol] #int