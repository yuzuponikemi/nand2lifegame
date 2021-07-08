 # -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 18:13:20 2021

VM
CodeWriter

CodeWriter: Translates VM commands into Hack assembly code.

@author: IKM1YH
"""
import os

class VMCodeWriter():
    '''
    Translates VM commands into Hack assembly code.
    '''
    
    
    def __init__(self, Outputfile):
        '''Opens the outputfile.asm and gets ready to write into it.'''
        self.filename=Outputfile
        self.ifunc = 0
        self.funcstate = ['base']
        self.eqgtltnum = {'eq':0,'gt':0,'lt':0}
        self.Arithdic = {'add':['//add','@SP','A=M-1','D=M','A=A-1','M=D+M','@SP','M=M-1'],\
                         'sub':['//sub','@SP','A=M-1','D=M','A=A-1','M=M-D','@SP','M=M-1'],\
                         'neg':['//neg','@SP','A=M-1','M=-M'],\
                         'eq':[],\
                         'gt':[], \
                         'lt':[], \
                         'and':['//and','@SP','A=M-1','D=M','A=A-1','M=D&M','@SP','M=M-1'], \
                         'or':['//or','@SP','A=M-1','D=M','A=A-1','M=D|M','@SP','M=M-1'], \
                         'not':['//not','@SP','A=M-1','M=!M']}
        self.f = open(self.filename, 'w')
        
    def setFileName(self,newvmfile):
        '''Informs the code writer that the translation of a new VM file is started.'''
        self.vmfile = os.path.basename(newvmfile)
        self.funcstate == []
        
        
        
    def writeArithmetic(self, command):
        '''Wites the assembly code that iis the translation of the given arithmetic command.
        add, sub, neg, eq, gt, lt, and, or, not '''
        self.currentcodels=self.Arithdic[command]
        if command in ['eq','gt','lt']: self.currentcodels = self.eqgtlt(command)
        
        for code in self.currentcodels:
            self.f.write(code +'\n')
        

    def eqgtlt(self,arith):
        self.eqgtltnum[arith] += 1
        cap = "".join([word.capitalize() for word in arith])
        ide = cap + str(self.eqgtltnum[arith])
        
        return ['//'+cap,'@SP','A=M-1','D=M','A=A-1','D=M-D',\
                '@'+self.funcstate[-1]+'$'+ide,'D;J'+cap,\
                '@SP','A=M-1','A=A-1','M=0',\
                '@'+self.funcstate[-1]+'$OUT'+ide,'0;JMP',\
                '('+self.funcstate[-1]+'$'+ide+')','@SP','A=M-1','A=A-1','M=-1',\
                '('+self.funcstate[-1]+'$OUT'+ide+')','@SP','M=M-1']
        
        
    def writePushPop(self, command, segment, index):
        '''Writes assembly code that is the translatiion of the given command, 
        where command is eithr C_PUSH or C_POP. push constant x'''
        sind = str(index)


        
        if segment == 'constant':
            self.currentcodels = ['//push','@'+sind,'D=A','@SP','M=M+1','A=M-1','M=D']
        else:
            self.segs = {'argument':['@ARG','D=M','@'+sind,'D=D+A','@13','M=D'],\
             'local':['@LCL','D=M','@'+sind,'D=D+A','@13','M=D'],\
             'static':['@'+self.vmfile+sind,'D=A','@13','M=D'],\
             #'constant':['@'+index,'D=A','@13','M=D'],\
             'this':['@THIS','D=M','@'+sind,'D=D+A','@13','M=D'],\
             'that':['@THAT','D=M','@'+sind,'D=D+A','@13','M=D'],\
             'pointer':['@'+str(3+index),'D=A','@13','M=D'],\
             'temp':['@'+str(5+index),'D=A','@13','M=D']\
             }
            self.pushpop = {'push':['//push']+self.segs[segment]+['@13','A=M','D=M', \
                            '@SP','M=M+1','A=M-1','M=D'], \
                            'pop':['//pop']+self.segs[segment]+['@SP','M=M-1','A=M','D=M',\
                            '@13','A=M','M=D']\
                            }
            self.currentcodels = self.pushpop[command]
            
        for code in self.currentcodels:
            self.f.write(code +'\n')
        
    def writeInit(self):
        '''Wites the assembly code that VM Initialization, also called bootstrap code.\
        This code must be placed at the beggining of the outputfile. 
        In order for any translated VM program to start running,\
        it must include a preamble startup
        code that forces the VM implementation to start executing it on the host platform.In addition, in order for
        any VM code to operate properly, the VM implementation must store the base addresses of the virtual
        segments in selected locations in the host RAM. The first three test programs in this project assume that
        the startup code was not yet implemented and include test scripts that effect the necessary initializations
        “manually.” The last two programs assume that the startup code is already part of the VM implementation.'''
        self.currentcodels = ['//Initializatiion','@256','D=A','@SP','M=D']
        for code in self.currentcodels:
            self.f.write(code +'\n')
        self.writeCall('Sys.init',0)
            
    def writeLabel(self,label):
        '''Wites the assembly code that label '''
        if self.funcstate == []:
            self.currentcodels = '('+str(label)+')'
        else:
            self.currentcodels = '('+self.funcstate[-1]+'$'+str(label)+')'
        self.f.write(self.currentcodels +'\n')
            
    def writeGoto(self,label):
        '''Wites the assembly code that goto '''
        if self.funcstate == []:
            self.currentcodels = ['//Goto','@'+str(label),'0;JMP']
        else:
            self.currentcodels = ['//Goto','@'+self.funcstate[-1]+'$'+str(label),'0;JMP']
        for code in self.currentcodels:
            self.f.write(code +'\n')
            
    def writeIf(self,label):
        '''Wites the assembly code that if-goto C_IF-GOTO'''
        if self.funcstate == []:
            self.currentcodels = ['//if-Goto','@SP','AM=M-1','D=M','@'+str(label),'D;JNE']
        else:
            self.currentcodels = ['//if-Goto','@SP','AM=M-1','D=M','@'+self.funcstate[-1]+'$'+str(label),'D;JNE']
        for code in self.currentcodels:
            self.f.write(code +'\n')
            
    def writeCall(self,functionName, numArgs):
        '''Wites the assembly code that call
        Before calling the function, the caller must push as many arguments as necessary onto the stack;
        ■ Next, the caller invokes the function using the call command;
        ■ After the called function returns, the arguments that the caller has pushed before the call have
        disappeared from the stack, and a return value (that always exists) appears at the top of the stack;
        ■ After the called function returns, the caller’s memory segments argument, local, static, this, that,
        and pointer are the same as before the call, and the temp segment is undefined.'''
        
        self.ifunc += 1
        self.f.write('//Call\n')
        
        self.writePushPop( 'push', 'constant', 'Return.'+functionName+str(self.ifunc))

        
#        self.writePushPop('push', 'local', 0)
#        self.writePushPop( 'push', 'argument', 0)
#        self.writePushPop( 'push', 'this', 0)
#        self.writePushPop( 'push', 'that', 0)
        self.currentcodels = ['@LCL','D=M','@SP','M=M+1','A=M-1','M=D',\
                              '@ARG','D=M','@SP','M=M+1','A=M-1','M=D',\
                              '@THIS','D=M','@SP','M=M+1','A=M-1','M=D',\
                              '@THAT','D=M','@SP','M=M+1','A=M-1','M=D',\
                              '@'+str(5+numArgs), 'D=A', '@SP', 'D=M-D','@ARG','M=D',\
                              '@SP','D=M','@LCL','M=D']
        for code in self.currentcodels:
            self.f.write(code +'\n')

#        self.writeGoto(functionName)
#        self.writeLabel('Return.'+functionName+str(self.ifunc))
        self.currentcodels = ['//Goto','@'+functionName,'0;JMP','('+'Return.'+functionName+str(self.ifunc)+')']
        for code in self.currentcodels:
            self.f.write(code +'\n')
            
    def writeReturn(self):
        '''Wites the assembly code that return '''
        self.f.write('//Return\n')
        self.currentcodels = ['@LCL','D=M','@R14','M=D',\
                              '@R14','D=M','@5','A=D-A','D=M','@R15','M=D']#returnAdd(@(endframe-5))->R15
        for code in self.currentcodels:
            self.f.write(code +'\n')
        
        self.writePushPop( 'pop','argument', 0)
                              
        self.currentcodels = ['@ARG','D=M','@SP','M=D+1',\
                              '@R14','D=M','@1','A=D-A','D=M','@THAT','M=D',\
                              '@R14','D=M','@2','A=D-A','D=M','@THIS','M=D',\
                              '@R14','D=M','@3','A=D-A','D=M','@ARG','M=D',\
                              '@R14','D=M','@4','A=D-A','D=M','@LCL','M=D',\
                              '//Goto','@R15','A=M','0;JMP']
        for code in self.currentcodels:
            self.f.write(code +'\n')

        
        
    def writeFunction(self,functionName, numLocals):
        '''Wites the assembly code that function When the called function starts executing,
        its argument segment has been initialized with actual argument values passed by the caller 
        and its local variables segment has been allocated and initialized to zeros. 
        The static segment that the called function sees has been set to the static segment
        of the VM file to which it belongs, and the working stack that it sees is empty. 
        The segments this, that, pointer, and temp are undefined upon entry.
        ■ Before returning, the called function must push a value onto the stack.'''
        self.f.write('//Function\n')
        self.funcstate.append(functionName)
         
        nset = ['('+functionName+')']
        setlocalvar = ['//push','@0','D=A','@SP','M=M+1','A=M-1','M=D']
        for n in range(numLocals): nset.extend(setlocalvar)
        
        self.currentcodels = nset
        for code in self.currentcodels:
            self.f.write(code +'\n')
        
        
    def close(self):
        '''Closes the output file.'''
        self.f.close()
