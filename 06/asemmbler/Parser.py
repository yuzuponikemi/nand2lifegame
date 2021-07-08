# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 13:15:33 2021

@author: IKM1YH


Routine Arguments Returns Function

"""

class Parser:
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
        f = open(self.filename, 'r')
        self.lines = [(x.rstrip('\n')).split('//')[0] for x in f.readlines()]
        self.cmds = [x.replace(' ', '') for x in self.lines if x != '']
        f.close()
        self.currentcmd = self.cmds[self.counter]
        
    def countagain(self):
        self.counter = 0


    
    def hasMoreCommands(self):
        '''Boolean Are there more commands in the input?'''
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
        '''A_COMMAND, C_COMMAND, L_COMMAND
        Returns the type of the current
        command:
            m A_COMMAND for @Xxx where
            Xxx is either a symbol or a
            decimal number
            m C_COMMAND for
            dest=comp;jump
            m L_COMMAND (actually, pseudocommand)
            for (Xxx) where Xxx
            is a symbol.
        '''
        if self.currentcmd[0] == '@':
            return 'A_COMMAND'
        elif self.currentcmd[0] == '(':
            return 'L_COMMAND'
        else:
            return 'C_COMMAND'
        

    
    def symbol(self, commandType):
        '''string Returns the symbol or decimal
        Xxx of the current command
        @Xxx or (Xxx). Should be called
        only when commandType() is
        A_COMMAND or L_COMMAND.'''
        if commandType == 'A_COMMAND':
            return self.currentcmd[1:]
        elif commandType == 'L_COMMAND':
            return self.currentcmd[1:-1]
        else:
            return None 
    
    def dest(self):
        '''string Returns the dest mnemonic in
        the current C-command (8 possibilities).
        Should be called only
        when commandType() is C_COMMAND.'''
        if '=' in self.currentcmd:
            return self.currentcmd.split('=')[0]
        else:
            return 'null'
    
    def comp(self):
        '''string Returns the comp mnemonic in
        the current C-command (28 possibilities).
        Should be called only
        when commandType() is C_COMMAND.'''
        if '=' in self.currentcmd:
            return self.currentcmd.split('=')[1].split(';')[0]
        else:
            return self.currentcmd.split(';')[0]      

    
    def jump(self):
        '''string Returns the jump mnemonic in
        the current C-command (8 possibilities).
        Should be called only
        when commandType() is C_COMMAND.'''
        if ';' in self.currentcmd:
            return self.currentcmd.split(';')[-1]
        else:
            return 'null'






