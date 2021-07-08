# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 19:22:56 2021

@author: IKM1YH
"""


class SymbolTable():
    '''
    Keeps a correspondence between 
    symbolic labels and scope, type, attributes, index.
    -------name----classormethod-type - kind------ #
    '''


    def __init__(self):
        '''Creates class/method new empty symbol table.
        format --- name : [type, kind, #]
        '''
        
        self.ctbl = {'this': ['ObjectInstance', 'pointer', 0]} #class table
        self.mtbl = {} #method table
        self.staticn = 0
        self.fieldn = 0
        self.argn = 0
        self.varn = 0
        self.subroutinen =0
        self.classn = 0

    def startSubroutine(self):
        ''''''
        print(self.mtbl)
        self.mtbl = {} #method table
        self.argn = 0
        self.varn = 0
        
        
    def define(self, name, types, kind, k=0):
        ''''''
        if kind == 'static':
            self.ctbl[name] = [types, kind, self.staticn]
            self.staticn += 1
        elif kind == 'field':
            self.ctbl[name] = [types, 'this', self.fieldn]
            self.fieldn += 1
        elif kind == 'arg':
            self.mtbl[name] = [types, 'argument', self.argn]
            self.argn += 1
        elif kind == 'var':
            self.mtbl[name] = [types, 'local', self.varn]
            self.varn += 1
        elif kind in ['method', 'constructor', 'function']:
            self.ctbl[name] = [types, kind, k]
            self.subroutinen += 1
        elif kind == 'class':
            self.ctbl[name] = [types, kind, self.classn]
            self.classn += 1
        else:
            print('error')


        
    def varCount(self, kind):#static, field, arg, var
        ''''''
        if kind == 'static':
            return  self.staticn
        elif kind == 'field':
            return  self.fieldn
        elif kind == 'arg':
            return  self.argn
        else:
            return  self.varn
        
#name : [type, kind, index]
    def kindOf(self,name):
        ''''''
        if (name in list(self.mtbl.keys())):
            return self.mtbl[name][1]
        elif (name in list(self.ctbl.keys())):
            return self.ctbl[name][1]
        else:
            return None #(static, field, arg, var, none)
    
    def typeOf(self,name):
        ''''''
        if (name in list(self.mtbl.keys())):
            return self.mtbl[name][0]
        elif (name in list(self.ctbl.keys())):
            return self.ctbl[name][0]
        else:
            return None #str

    
    def indexOf(self,name):
        ''''''
        if (name in list(self.mtbl.keys())):
            return self.mtbl[name][2]
        elif (name in list(self.ctbl.keys())):
            return self.ctbl[name][2]
        else:
            return None #int