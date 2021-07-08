# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 13:15:35 2021

@author: IKM1YH



A-instruction: @value 
// Where value is either a non-negative decimal number
// or a symbol referring to such number.
value (v ¼ 0 or 1)
Binary: 0 v v v v v v v v v v v v v v v

C-instruction: dest=comp;jump // Either the dest or jump fields may be empty.
// If dest is empty, the ‘‘=’’ is omitted;
// If jump is empty, the ‘‘;’’ is omitted.
comp dest jump
Binary: 1 1 1 a c1 c2 c3 c4 c5 c6 d1 d2 d3 j1 j2 j3


dest d1 d2 d3 jump j1 j2 j3
null 0 0 0 null 0 0 0
M 0 0 1 JGT 0 0 1
D 0 1 0 JEQ 0 1 0
MD 0 1 1 JGE 0 1 1
A 1 0 0 JLT 1 0 0
AM 1 0 1 JNE 1 0 1
AD 1 1 0 JLE 1 1 0
AMD 1 1 1 JMP 1 1 1



comp
(when a¼0) c1 c2 c3 c4 c5 c6 (when a¼1)
0 1 0 1 0 1 0
1 1 1 1 1 1 1
-1 1 1 1 0 1 0
D 0 0 1 1 0 0
A 1 1 0 0 0 0 M
!D 0 0 1 1 0 1
!A 1 1 0 0 0 1 !M
-D 0 0 1 1 1 1
-A 1 1 0 0 1 1 -M
D+1 0 1 1 1 1 1
A+1 1 1 0 1 1 1 M+1
D-1 0 0 1 1 1 0
A-1 1 1 0 0 1 0 M-1
D+A 0 0 0 0 1 0 D+M
D-A 0 1 0 0 1 1 D-M
A-D 0 0 0 1 1 1 M-D
D&A 0 0 0 0 0 0 D&M
D|A 0 1 0 1 0 1 D|M
"""

class Code():
    '''
    Translates Hack assembly language mnemonics into binary codes.
    '''
    
    destdic = {'null':'000', 'M':'001', 'D':'010', 'MD':'011', 'A':'100', 'AM':'101', 'AD':'110', 'AMD':'111'}

    jumpdic = {'null':'000', 'JGT':'001', 'JEQ':'010', 'JGE':'011', 'JLT':'100', 'JNE':'101', 'JLE':'110', 'JMP':'111'}

    compdic = {'0':'0101010', '1':'0111111', '-1':'0111010', 'D':'0001100', 'A':'0110000', '!D':'0001101',\
               '!A':'0110001', '-D':'0001111', '-A':'0110011', 'D+1':'0011111', 'A+1':'0110111', 'D-1':'0001110',\
               'A-1':'0110010','D+A':'0000010', 'D-A':'0010011', 'A-D':'0000111', 'D&A':'0000000', 'D|A':'0010101',\
               'M':'1110000','!M':'1110001','-M':'1110011',  'M+1':'1110111', 'M-1':'1110010',\
               'D+M':'1000010', 'D-M':'1010011', 'M-D':'1000111', 'D&M':'1000000', 'D|M':'1010101' }
    def __init__(self):
        '''No'''


    def dest(self,mnemonic):
        '''Returns the binary code of the
        dest mnemonic.'''

        return Code.destdic[mnemonic]
    
    def comp(self,mnemonic):
        '''Returns the binary code of the
        comp mnemonic.'''
        return Code.compdic[mnemonic]  
    def jump(self,mnemonic):
        '''Returns the binary code of the
        jump mnemonic.'''
        return Code.jumpdic[mnemonic]