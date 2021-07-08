# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 19:23:21 2021

@author: IKM1YH
"""
class VMWriter():
    '''
    Writes VM codes
    '''


    def __init__(self, fileinstance,tbl):
        '''Creates a new vm file.'''
        self.f = fileinstance
        self.tbl = tbl #symboltable instance
        



        
    def writePush(self, segment, Index):
        ''''''
        
        self.f.write('push '+segment+' '+str(Index) +'\n')
        
        # for vmcmd in self.currentvmcmdls:
        #     self.f.write(vmcmd +'\n')
        
    def writePop(self, segment, Index):
        ''''''
        self.f.write('pop '+segment+' '+str(Index) +'\n')
        
    def writeArithmetic(self, command,Unaryop=False):#add, sub, neg, eq, gt, lt, and, or, not
        ''''''
        Aridic ={ '+':'add', '-':'sub', '*':'Math.multiply', '/':'Math.divide', '&':'and', \
                       '|':'or', '<':'lt', '>':'gt', '=':'eq','~':'not'}
        UnaryAridic ={'~':'not','-':'neg'}
        if command in ['*', '/']:
            self.writeCall(Aridic[command], 2)
        elif Unaryop:
            self.f.write(UnaryAridic[command]+'\n')
        else:
            self.f.write(Aridic[command]+'\n')
        
    
    def writeLabel(self,label):
        ''''''
        self.f.write('label '+label +'\n')
        
    def writeGoto(self,label):
        ''''''
        self.f.write('goto '+label +'\n')
        
    def writeIf(self,label):
        ''''''
        self.f.write('if-goto '+label +'\n')
        
    
    def writeCall(self, name, nArgs):
        ''''''
        self.f.write('call '+name+' '+str(nArgs) +'\n')
    
    def writeFunction(self,name, nLocals):
        ''''SquareGame.moveSquare': ['void', 'method', 1]
                            #name : [type, kind, index]   '''
        self.f.write('function '+name+' '+str(nLocals) +'\n')
        subtype = self.tbl.kindOf(name)
        if subtype == 'method':
            self.writePush('argument', 0)
            self.writePop('pointer', 0)
        elif subtype == 'constructor':
            #print('allocate memory, and set base of this to new base')
            self.writePush('constant',self.tbl.varCount('field'))
            self.writeCall('Memory.alloc', 1)
            self.writePop('pointer', 0)
        else:
            print(None)
        
    
    def Return(self,subroutine):
        ''''''
        if self.tbl.typeOf(subroutine) == 'void':self.writePush('constant',0)
        if self.tbl.kindOf(subroutine) == 'constructor':self.writePush('pointer',0)
        self.f.write('return'+'\n')
    
    def close(self):
        '''Closes the output file.'''
        self.f.close()