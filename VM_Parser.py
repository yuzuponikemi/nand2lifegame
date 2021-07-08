# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 18:14:24 2021

VM

Parser

Parser: Handles the parsing of a single .vm file, and encapsulates access to the input code. 
It reads VM commands, parses them, and provides convenient access to their components. 
In addition, it removes all white space and comments.

@author: IKM1YH
"""

class VMParser:
    '''
    Parser: Encapsulates access to the input code. Reads an assembly language command,
    parses it, and provides convenient access to the command’s components
    (fields and symbols). In addition, removes all white space and comments.
    '''


    def __init__(self, filename):
        '''Opens the input file and gets ready to parse it.'''
        self.filename=filename
        self.counter = 0
        #print('Start to parse '+str(self.filename))
        
        #extract commands from strings
        f = open(self.filename, 'r') #ex SimpleAdd.vm
        self.lines = [(x.rstrip('\n')).split('//')[0] for x in f.readlines()]
        self.cmds = [x.split() for x in self.lines if x != '']
        f.close()
        self.currentcmd = self.cmds[self.counter]
        
#    def countagain(self):
#        self.counter = 0
    
    def hasMoreCommands(self):
        '''Are there more commands in the input?'''
        if (len(self.cmds)) >= (self.counter+1):
            return True
        else: 
            return False
        
    
    def advance(self):
        '''Reads the next command from
        the input and makes it the current
        command. Should be called only
        if hasMoreCommands() is true.
        Initially there is no current command.'''
        
        self.currentcmd = self.cmds[self.counter]
        self.counter += 1

    
    def commandType(self):
        '''
        Return the type of the current VM command. 
        C_ARITHMETIC is returned for all the arithmetic commands.
        '''
#        self.typedic = {C_ARITHMETIC, C_PUSH, C_POP, C_LABEL, C_GOTO,\
#                   C_IF-GOTO, C_FUNCTION, C_RETURN, C_CALL,}
        
        if self.currentcmd[0] in ['add', 'sub','neg', 'eq', 'gt', 'lt', 'and', 'or', 'not']:
            return 'C_ARITHMETIC'

        else:
            capitalizedcmd = "".join([word.capitalize() \
                                      for word in self.currentcmd[0]])
            return 'C_' + capitalizedcmd


    def argone(self):
        '''
        Return the first argument of the current command.
        In case of C_ARITHMETIC, the command itself is returned.
        Should not be called if the current command is C_RETURN.
        '''
        
        if self.commandType() == 'C_ARITHMETIC':
            return self.currentcmd[0]
        elif self.commandType() == 'C_RETURN':
            return None
        else:
            return self.currentcmd[1]
        
    def argtwo(self):
        '''
        Return the second argument of the current command.
        Should be called only if the current command is C_PUSH,C_POP,C_FUNCTION, or C_CALL.
        '''
        if self.commandType() in ['C_PUSH','C_POP',"C_FUNCTION","C_CALL"]:
            return int(self.currentcmd[2])
        else:
            return None

    


