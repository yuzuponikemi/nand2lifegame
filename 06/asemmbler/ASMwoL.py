# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 21:26:17 2021

@author: IKM1YH

Hack assembler

The Hack assembler reads as input a text file named Prog.asm, containing a Hack
assembly program, and produces as output a text file named Prog.hack, containing
the translated Hack machine code. The name of the input file is supplied to the
assembler as a command line argument:
    
prompt> Assembler Prog.asm

Initialization 
Initialize the symbol table with all the predefined symbols and their
pre-allocated RAM addresses, according to section 6.2.3.

First Pass 
Go through the entire assembly program, line by line, and build the
symbol table without generating any code. As you march through the program lines,
keep a running number recording the ROM address into which the current command
will be eventually loaded. This number starts at 0 and is incremented by 1 whenever
a C-instruction or an A-instruction is encountered, but does not change when a label
pseudocommand or a comment is encountered. Each time a pseudocommand (Xxx)
is encountered, add a new entry to the symbol table, associating Xxx with the ROM
address that will eventually store the next command in the program. This pass results
in entering all the program’s labels along with their ROM addresses into the symbol
table. The program’s variables are handled in the second pass.

Second Pass 
Now go again through the entire program, and parse each line. Each
time a symbolic A-instruction is encountered, namely, @Xxx where Xxx is a symbol
and not a number, look up Xxx in the symbol table. If the symbol is found in the
table, replace it with its numeric meaning and complete the command’s translation.
If the symbol is not found in the table, then it must represent a new variable. To
handle it, add the pair (Xxx, n) to the symbol table, where n is the next available
RAM address, and complete the command’s translation. The allocated RAM
addresses are consecutive numbers, starting at address 16 ( just after the addresses
allocated to the predefined symbols).
"""
import Coder
import Parser
import Symboltable
import sys



class Assembler:
    def __init__(self,filename):
        self.asmfilename = filename
        self.hackfile = self.asmfilename[:-3]+'hack'
        self.code = Coder.Code()
        self.Par = Parser.Parser(filename)
        self.sbl = Symboltable.SymbolTable()


    def getbin(self):
        self.binline = '111' + \
        self.code.comp(self.Par.comp()) + \
        self.code.dest(self.Par.dest()) + \
        self.code.jump(self.Par.jump())
    
    def firstpass(self):
        self.romn = 0
        while asm.Par.hasMoreCommands():
            asm.Par.advance()
            if self.Par.commandType() != 'L_COMMAND' : 
                self.romn += 1
                continue
            self.csbl = self.Par.symbol(self.Par.commandType())
            if self.sbl.contains(self.csbl):
                continue
            else:
                self.sbl.addEntry(self.csbl,self.romn)
                
        self.Par.countagain()

    def secondpass(self,path_w):
        #s = '// This file is assembled from ' + self.asmfilename+'\n'
        with open(path_w, mode='w') as self.f:
            #f.write(s)
            self.ramn = 16
            while self.Par.hasMoreCommands():
                self.Par.advance()
                if self.Par.commandType() == 'C_COMMAND':
                    self.getbin()
                    self.f.write(self.binline+'\n')
                elif self.Par.commandType() == 'A_COMMAND':
                    self.csbl=self.Par.symbol('A_COMMAND')
                    if self.csbl.isdigit():
                        self.binline='0' + str(format(int(self.csbl), '015b'))
                    else:
                        if self.sbl.contains(self.csbl):  
                            self.binline='0' + str(format(self.sbl.sbltbl[self.csbl], '015b'))
                        else:
                            self.sbl.addEntry(self.csbl,self.ramn)
                            self.ramn += 1
                            self.binline='0' + str(format(self.sbl.sbltbl[self.csbl], '015b'))

                    self.f.write(self.binline+'\n')
                else:
                    continue
                        
        
        
if __name__ == "__main__":
    # execute only if run as a script
    print('tranlating...')
#    asm = Assembler(sys.argv)
#    print(asm)
    asm = Assembler('Pong.asm')
    asm.firstpass()

    path_w = r'C:\\Users\\ikm1yh\\Desktop\\nand2tetris\\projects\\06\\'+asm.hackfile
    asm.secondpass(path_w)
    

    print('Translation finished')

        
        
    
