# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 18:59:53 2021

JackTokenizer.py

@author: IKM1YH
"""
import re
import sys

args = sys.argv

class JackTokenizer:
    '''
    Parser: Encapsulates access to the input code. Reads an assembly language command,
    parses it, and provides convenient access to the command’s components
    (fields and symbols). In addition, removes all white space and comments.
    '''


    def __init__(self, filename):
        '''Opens the input file and gets ready to parse it.'''
        self.filename=filename
        self.counter = 0
         
        self.unitedtkns =[]
        self.tkns = []
        
        f = open(self.filename, 'r') #ex SimpleAdd.jack
        #taking comment out from strings
        self.lines = [(x.rstrip('\n')).split('//')[0] for x in f.readlines()]
        self.deComments()
        
        #remember string val
        self.fulltext = ''
        for line in self.lines: self.fulltext +=line
        self.mojinow = 1
        self.stringls = ['']
        for moji in self.fulltext:
            if moji == '"':
                self.mojinow += 1
                if (self.mojinow)%2==0:self.stringls.append('')
                continue
            if (self.mojinow)%2==0:
                self.stringls[int(self.mojinow/2)-1]+=moji
        self.numstr = -1
                
        
        #making single plane list
        self.splines = [x.split() for x in self.lines if x != '']
        for spline in self.splines:self.unitedtkns.extend(spline)
        
        #taking care of symbols
        for unitedtkn in self.unitedtkns:

            self.tkns.extend(re.split('(\W)',unitedtkn))
            
        
        self.tkns = [x for x in self.tkns if x != ''] #symbpl-separated
        f.close()
        self.currenttkn = self.tkns[self.counter]
        
        
        
        
    def countagain(self):
        self.counter = 0
    
    def hasMoreTokens(self):
        '''Are there more commands in the input?'''
        if (len(self.tkns)) >= (self.counter+1):
            return True
        else: 
            return False
        
    
    def advance(self):
        '''Reads the next tkn from
        the input and makes it the current
        . Should be called only
        if hasMoreTokens() is true.
        Initially there is no current tkn.'''
        
        self.currenttkn = self.tkns[self.counter]
        self.counter += 1

    
    def tokenType(self):
        '''
        Return the type of the current tkn
         self.typedic = {KEYWORD, SYMBOL, IDENTIFIER, INT_CONST, STRING_CONST}
        ''' 
        
        if self.currenttkn in ['class', 'constructor','function', 'method',\
                               'field', 'static', 'var', 'int', 'char',\
                               'boolean', 'void', 'true', 'false', 'null',\
                               'this', 'let', 'do', 'if', 'else', 'while','return']:
            return 'KEYWORD'
        elif self.currenttkn in ['{', '}', '(', ')', '[', ']', '.', ',', \
                       ';', '+', '-', '*', '/', '&', \
                       '|', '<', '>', '=', '~']:
            return 'SYMBOL'
        elif self.currenttkn == '"':
            return 'STRING_CONST'
        elif self.currenttkn.isdecimal():
            return 'INT_CONST'
        else:
            return 'IDENTIFIER'

    def xmltagger(self,tag, tkn):
        return '<'+tag+'> '+tkn+' </'+tag+'>\n'
    
    def keyWord(self):
        '''
        '''
        return self.xmltagger('keyword',self.currenttkn)

        
    def symbol(self):
        '''
                self.symbols =['{', '}', '(', ')', '[', ']', '.', ',', \
                       ';', '+', '-', '*', '/', '&', \
                       '|', '<', '>', '=', '~']
        '''
        if self.currenttkn == '<':
            return self.xmltagger('symbol','&lt;')
        elif self.currenttkn == '>':
            return self.xmltagger('symbol','&gt;')
        elif self.currenttkn == '&':
            return self.xmltagger('symbol','&amp;') 
        else:
            return self.xmltagger('symbol', self.currenttkn)

    def identifier(self,tbl):
        '''
        '''
        if self.currenttkn in tbl.ctbl:
            categ = tbl.ctbl[self.currenttkn][1]+str(tbl.ctbl[self.currenttkn][2])
            if self.currenttkn in tbl.mtbl:
                categ = tbl.mtbl[self.currenttkn][1]+str(tbl.mtbl[self.currenttkn][2])
        elif self.currenttkn in tbl.mtbl:
            categ = tbl.mtbl[self.currenttkn][1]+str(tbl.mtbl[self.currenttkn][2])
        else:
            if self.tkns[self.counter-2] in ['field', 'var', 'static']\
                or self.tkns[self.counter] in ['.']:
                categ = 'class'
            elif self.tkns[self.counter-2] in ['.','do']\
                and self.tkns[self.counter] not in ['.']:
                categ = 'subroutine'
            else:
                categ = 'identifier'
        
        # if self.currenttkn == 'var':
        #     return self.xmltagger('var', self.currenttkn)
        # elif self.currenttkn == 'argument':
        #     return self.xmltagger('argument', self.currenttkn)
        # elif self.currenttkn == 'static':
        #     return self.xmltagger('static', self.currenttkn)
        # elif self.currenttkn == 'field':
        #     return self.xmltagger('field', self.currenttkn)
        # elif self.currenttkn == 'class':
        #     return self.xmltagger('class', self.currenttkn) 
        # elif self.currenttkn == 'subroutine':
        #     return self.xmltagger('subroutine', self.currenttkn)
        # else:
        return self.xmltagger(categ, self.currenttkn)
        


    def intVal(self):
        '''
        '''
        
        return self.xmltagger('integerConstant',self.currenttkn)

    def stringVal(self):
        '''self.currenttkn == '"'
        '''
        self.advance()
        while(self.currenttkn != '"'):
            self.advance()
        self.numstr +=1
        return self.xmltagger('stringConstant',self.stringls[self.numstr]), self.stringls[self.numstr]
    
    def deComments(self):
        '''take comments out
        '''
        incomment = False
        for num, line in enumerate(self.lines):
            if '/*' in line : 
                self.lines[num] = line.split('/*')[0]
                incomment = True
            if '*/' in line : 
                self.lines[num] = line.split('*/')[1]
                incomment = False
            if incomment : self.lines[num] = ''
        return None



if __name__ == "__main__":
    # execute only if run as a script
    #tgt = 'C:/Users/ikm1yh/Desktop/nand2tetris/projects/08/FunctionCalls/SimpleFunction/SimpleFunction.vm'
    #tgt = 'C:/Users/ikm1yh/Desktop/nand2tetris/projects/10/example2.jack'
    #tgt = 'C:/Users/ikm1yh/Desktop/nand2tetris/projects/10/Square/SquareGame.jack'
    tgt = args[1]
    print('Tokenizing...'+tgt)
#    asm = Assembler(sys.argv)
#    print(asm)
    tn = JackTokenizer(tgt)
#    path_w = r'C:\\Users\\ikm1yh\\Desktop\\nand2tetris\\projects\\07\\'+vm.asmfile

        


