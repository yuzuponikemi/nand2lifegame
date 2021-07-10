# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 18:43:06 2021

@author: IKM1YH

JackCompiler.py
The analyzer program operates on a given source, where source is either a file name of the form Xxx.jack
or a directory name containing one or more such files. For each source Xxx.jack file, the analyzer goes
through the following logic:
1. Create a JackTokenizer from the Xxx.jack input file.
2. Create an output file called Xxx.vm and pretne it for writing.
3. Use the CompilationEngine to compile the input JackTokenizer into the output file.

(CompilationEngine uses VMWriter.py and SymbolTable))
"""

import JackTokenizer
import CompilationEngine
import os
import sys

args = sys.argv

class JackCompiler:
    def __init__(self,tgtname):
        self.vmtgtname = tgtname
        if '.jack' in tgtname:
            self.vmfile = tgtname[:-4]+'vm'
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
                self.vmfile = tgtname+'/'+'/'+filename[:-4]+'vm'
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


                
        
if __name__ == "__main__":
    # execute only if run as a script
    #tgt = 'C:/Users/ikm1yh/Desktop/nand2tetris/projects/09/Lifegame/LifeGame.jack'
    tgt = 'C:/Users/ikm1yh/Desktop/nand2tetris/projects/11/ConvertToBin'
    tgt = 'C:/Users/ikm1yh/Desktop/nand2tetris/projects/11/Pong'
    tgt = 'C:/Users/ikm1yh/Desktop/nand2tetris/projects/11/Square'
    if len(args) != 1 : tgt = args[1]
    print('tranlating...'+tgt)
#    asm = Assembler(sys.argv)
#    print(asm)
    ja = JackCompiler(tgt)
#    path_w = r'C:\\Users\\ikm1yh\\Desktop\\nand2tetris\\projects\\07\\'+vm.asmfile
    ja.compile(tgt)


    print('Translation finished')