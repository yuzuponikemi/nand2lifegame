# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 18:12:43 2021

VM Main

Main Program The main program should construct a Parser to parse the VM input file and a CodeWriter
to generate code into the corresponding output file. It should then march through the VM commands in the
input file and generate assembly code for each one of them.
If the program’s argument is a directory name rather than a file name, the main program should process
all the .vm files in this directory. In doing so, it should use a separate Parser for handling each input file
and a single CodeWriter for handling the output.

@author: IKM1YH
"""
import VM_CodeWriter
import VM_Parser
import os
import sys

args = sys.argv

class VM:
    def __init__(self,tgtname):
        self.vmtgtname = tgtname #targetname can be a folder or vmfile
        if '.vm' in tgtname:
            #self.asmfile = tgtname[:-2]+'asm' #asm path
            self.asmfile = os.path.splitext(tgtname)[0] +'.asm'
        else:
            #self.tgtfolder = tgtname.split('/')[-1] #Only folder name
            self.tgtfolder = os.path.basename(tgtname) #Only folder name
            self.asmfile = os.path.join(tgtname,self.tgtfolder+'.asm') #asm path
        print('Output_to_'+self.asmfile)
        self.code = VM_CodeWriter.VMCodeWriter(self.asmfile)

        

    def vmtrans(self,tgtname):
        
        if '.vm' in tgtname:
            filename = tgtname
            self.num = 1
            self.firstpass(filename, filename)
        else:
            self.vmfilels = [x for x in os.listdir(path=tgtname) if '.vm' in x]
            for num, filename in enumerate(self.vmfilels):
                print('Translating_'+filename)
                self.num = num
                self.firstpass(tgtname+'/'+filename,filename)
        self.code.close()
       

    
    def firstpass(self,filename,vmname):
        self.Par = VM_Parser.VMParser(filename)
        self.code.setFileName(vmname)
        if self.num==0:self.code.writeInit()
        self.code.f.write('//////'+filename +'\n')
        while self.Par.hasMoreCommands():
            self.Par.advance()
            print(self.Par.commandType())
            if self.Par.commandType() == 'C_ARITHMETIC':
                self.code.writeArithmetic(self.Par.currentcmd[0])

            elif self.Par.commandType() in ['C_PUSH','C_POP']:
                self.code.writePushPop(self.Par.currentcmd[0],self.Par.argone(),self.Par.argtwo())
            elif self.Par.commandType() == 'C_LABEL':
                self.code.writeLabel(self.Par.argone())
            elif self.Par.commandType() == 'C_GOTO':
                self.code.writeGoto(self.Par.argone())
            elif self.Par.commandType() == 'C_IF-GOTO':
                self.code.writeIf(self.Par.argone())
            elif self.Par.commandType() == 'C_CALL':
                self.code.writeCall(self.Par.argone(),self.Par.argtwo())
            elif self.Par.commandType() == 'C_RETURN':
                self.code.writeReturn()
            elif self.Par.commandType() == 'C_FUNCTION':
                self.code.writeFunction(self.Par.argone(),self.Par.argtwo())
            else:
                continue
        

                
        
if __name__ == "__main__":
    # execute only if run as a script
    #tgt = 'C:/Users/ikm1yh/Desktop/nand2tetris/projects/08/FunctionCalls/SimpleFunction/SimpleFunction.vm'
    #tgt = 'C:/Users/ikm1yh/Desktop/nand2tetris/projects/07/StaticTest.vm'
    #tgt = 'C:/Users/ikm1yh/Desktop/nand2tetris/projects/07/StackArithmetic/StackTest/StackTest.vm'
    #tgt = 'C:/Users/ikm1yh/Desktop/nand2tetris/projects/07/StackArithmetic/SimpleAdd/SimpleAdd.vm'
    if len(args) != 1 : tgt = args[1]
    print('tranlating...'+tgt)
#    asm = Assembler(sys.argv)
#    print(asm)
    vm = VM(tgt)
#    path_w = r'C:\\Users\\ikm1yh\\Desktop\\nand2tetris\\projects\\07\\'+vm.asmfile
    vm.vmtrans(tgt)


    print('Translation finished')