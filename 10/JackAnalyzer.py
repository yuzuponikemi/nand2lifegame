# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 18:43:06 2021

@author: IKM1YH

JackAnalyzer.py
The analyzer program operates on a given source, where source is either a file name of the form Xxx.jack
or a directory name containing one or more such files. For each source Xxx.jack file, the analyzer goes
through the following logic:
1. Create a JackTokenizer from the Xxx.jack input file.
2. Create an output file called Xxx.xml and pretne it for writing.
3. Use the CompilationEngine to compile the input JackTokenizer into the output file.

"""

import JackTokenizer
import CompilationEngine
import os
import sys

args = sys.argv

class JackAnalyzer:
    def __init__(self,tgtname):
        self.vmtgtname = tgtname
        if '.jack' in tgtname:
            self.vmfile = tgtname[:-4]+'xml'
        #else:
            #self.tgtfolder = tgtname.split('/')[-1]
            #self.vmfile = tgtname+'/'+self.tgtfolder+'.vm'
        
        
        

    def compile(self,tgtname):
        
        if '.jack' in tgtname:
            filename = tgtname
            ja.firstpass(filename,self.vmfile)
        else:
            self.jackfilels = [x for x in os.listdir(path=tgtname) if '.jack' in x]
            for self.num, filename in enumerate(self.jackfilels):
                self.vmfile = tgtname+'/'+'/'+filename[:-4]+'xml'
                print('Translating_'+filename)
                self.firstpass(tgtname+'/'+filename,self.vmfile)
        self.ce.close()
       

    
    def firstpass(self,filename,output):
        self.tn = JackTokenizer.JackTokenizer(filename)
        self.ce = CompilationEngine.CompilationEngine(self.tn,output)
        #self.ce.setFileName(vmname)
        #if self.num==0:self.ce.writeInit()
        #self.ce.f.write('//////'+filename +'\n')
        while self.tn.hasMoreTokens():
            #self.ce.f.write('outnow\n')
            self.tn.advance()
            self.ce.writetkn(True)
        #     #print(self.tn.tokenType())
        #     #self.typedic = {KEYWORD, SYMBOL, IDENTIFIER, INT_CONST, STRING_CONST}
        #     if self.tn.tokenType() == 'KEYWORD':
        #         #self.ce.compilekeyword()
        #         print(self.tn.keyWord())

        #     elif self.tn.tokenType() == 'SYMBOL':
        #         #self.ce.compilesymbol()
        #         print(self.tn.symbol())
        #     elif self.tn.tokenType() == 'IDENTIFIER':
        #         #self.ce.compileidentifier()
        #         print(self.tn.identifier())
        #     elif self.tn.tokenType() == 'INT_CONST':
        #         #self.ce.compileintVal()
        #         print(self.tn.intVal())
        #     elif self.tn.tokenType() == 'STRING_CONST':
        #         #self.ce.compilestringVal()
        #         print(self.tn.stringVal())
        #     else:
        #         continue
            

        
        

                
        
if __name__ == "__main__":
    # execute only if run as a script
    #tgt = 'C:/Users/ikm1yh/Desktop/nand2tetris/projects/09/Lifegame/LifeGame.jack'
    tgt = 'C:/Users/ikm1yh/Desktop/nand2tetris/projects/10/Square/SquareGame.jack'
    tgt = "C:/Users/ikm1yh/Desktop/nand2tetris/projects/10/ArrayTest/Main.jack"
    tgt = 'C:/Users/ikm1yh/Desktop/nand2tetris/projects/10/Square'
    if len(args) != 1 : tgt = args[1]
    print('tranlating...'+tgt)
#    asm = Assembler(sys.argv)
#    print(asm)
    ja = JackAnalyzer(tgt)
#    path_w = r'C:\\Users\\ikm1yh\\Desktop\\nand2tetris\\projects\\07\\'+vm.asmfile
    ja.compile(tgt)


    print('Translation finished')