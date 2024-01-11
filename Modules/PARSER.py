import Modules.TOKENS as Tok
import Modules.OPERATION as OP
import Modules.DEBUG as DEBUG

tokens = {
    'COMMENT': '#',
    'EOF': 'EOF',
    'ERROR': 'ERROR',
    'PLUS': '+',
    'MINUS': '-',
    'MULTIPLY': '*',
    'DIVIDE': '/',
    'LPAREN': '(',
    'RPAREN': ')',
    'LBRACE': '{',
    'RBRACE': '}',
    'EQUALS': '=',
    'SEMICOLON': ';',
    'COLON': ':',
    'COMMA': ',',
    'DOT': '.',
    'IDENTIFIER': 'IDENTIFIER',
    'KEYWORD': 'KEYWORD',
    'STRING': 'STRING',
    'BOOL': 'BOOL',
    'AND': 'AND',
    'OR': 'OR',
    'NOT': 'NOT',
    'LESS_THAN': '<',
    'GREATER_THAN': '>',
    'LESS_THAN_EQUAL': '<=',
    'GREATER_THAN_EQUAL': '>=',
    'EQUAL_EQUAL': '==',
    'NOT_EQUAL': '!=',
    'IF': 'IF',
    'ELSE': 'ELSE',
    'ELIF': 'ELIF',
    'WHILE': 'WHILE',
    'FOR': 'FOR',
    'FUNC': 'FUNC',
    'RETURN': 'RETURN',
    'CLASS': 'CLASS',
    'NEW': 'NEW',
    'THIS': 'THIS',
    'SUPER': 'SUPER',
    'NIL': 'NIL',
    'TRUE': 'TRUE',
    'FALSE': 'FALSE',
    'VAR': 'VAR',
    'PRINT': 'PRINT',
    'PRINTLN': 'PRINTLN',
    'INPUT': 'INPUT',
    'INPUTS': 'INPUTS',
    'INPUTI': 'INPUTI',
    'INPUTF': 'INPUTF',
    'INPUTB': 'INPUTB',
    'NUM': 'NUM',
    'EXCEPT': 'EXCEPT',
    'TRY': 'TRY',
    'RAISE': 'RAISE',
    'FINALLY': 'FINALLY',
    'ASSERT': 'ASSERT',
    'PASS': 'PASS',
    'BREAK': 'BREAK',
    'CONTINUE': 'CONTINUE',
    'IMPORT': 'IMPORT',
    'FROM': 'FROM',
    'AS': 'AS',
    'IN': 'IN',
    'IS': 'IS',
    'DEL': 'DEL',
    'EXEC': 'EXEC',
    'GLOBAL': 'GLOBAL',
    'LOCAL': 'LOCAL',

}
class Parser:
    def __init__(self, stack, Debug):
        self.TokenStack = stack
        self.length = len(stack)
        self.bin = []
        self.pos = 0
        self.Debug = Debug
    
    @property
    def current_token(self):
        i = self.pos
        if i >= self.length:
            return Tok.Token(tokens['EOF'], None, self.pos)
        self.Debug.df("current_token", self.TokenStack[i])
        return self.TokenStack[i]

    def error(self):
        raise Exception('Invalid syntax')
    
    def nextToken(self):
        if self.pos < self.length -1:
            self.pos += 1
            return self.TokenStack[self.pos]
        else:
            return Tok.Token(tokens['EOF'], None, self.pos)

    def peek(self):
        if self.pos < self.length -1:
            return self.TokenStack[self.pos + 1]
        else:
            return Tok.Token(tokens['EOF'], None, self.pos)


    def eat(self, token_type):
        if self.current_token.type == token_type:
            temp = self.nextToken()
            self.current_token.type = temp.type
            self.current_token.value = temp.value
        else:
            self.error()
    

    def factor(self, i):
        self.pos = i 
        token = self.current_token()
        self.Debug.df("factor", token.type)
        match token.type:
            case 'PLUS':
                self.Debug.df("bin", self.bin)
                if (self.bin[-1].type == 'NUM' or self.bin[-1].type == 'STRING'):
                    next = self.peek()
                    self.bin.append(next)
                    args.append(self.bin.pop().value)
                    args.append(self.peek().value)
                    return OP.Operation('+', args)
                else:
                    self.error()
            case 'MINUS':
                self.eat(tokens['MINUS'])
                if (self.bin[-1] == tokens['NUM']):
                    return self.bin.pop() - self.factor()
                else:
                    self.error()
            case 'MULTIPLY':
                self.eat(tokens['MULTIPLY'])
                if (self.bin[-1] == tokens['NUM']):
                    return self.bin.pop() * self.factor()
                else:
                    self.error()
            case 'DIVIDE':
                self.eat(tokens['DIVIDE'])
                if (self.bin[-1] == tokens['NUM']):
                    return self.bin.pop() / self.factor()
                else:
                    self.error()
            case 'NUM':
                self.eat(tokens['NUM'])
                self.bin.append(token)
                return token.value
            case 'STRING':
                self.eat(tokens['STRING'])
                self.bin.append(token)
                return token.value
            case 'IDENTIFIER':
                self.eat(tokens['IDENTIFIER'])
                self.bin.append(token.value)
                return token.value
            case 'BOOL':
                self.eat(tokens['BOOL'])
                self.bin.append(token.value)
                return token.value
            case 'NIL':
                self.eat(tokens['NIL'])
                self.bin.append(token.value)
                return token.value
            case 'LPAREN':
                self.eat(tokens['LPAREN'])
                args = []
                while self.current_token['type'] != tokens['RPAREN']:
                    args.append(self.expr())
                self.eat(tokens['RPAREN'])
                return args
            case 'EOF':
                self.eat(tokens['EOF'])
                return None
            case 'ERROR':
                self.eat(tokens['ERROR'])
                return None
            case 'COMMENT':
                self.eat(tokens['COMMENT'])
                return None
            case 'KEYWORD':
                self.eat(tokens['KEYWORD'])
                return None
            case 'PRINT':
                self.eat(tokens['PRINT'])
                return None
            case _:
                self.error()

    
    def expr(self):
        com = []
        for i in range(self.length):
            self.Debug.df("expr", i)
            com.append(self.factor(i))
        return com
    
    def parse(self):
        return self.expr()