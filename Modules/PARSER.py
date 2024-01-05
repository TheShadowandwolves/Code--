import Modules.TOKENS as Tok
import Modules.LEXER as Lex
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
        self.length = len(self.TokenStack)
        self.pos = 0
        self.Debug = Debug
    
    @property
    def current_token(self):
        return self.TokenStack[self.pos]

    def error(self):
        raise Exception('Invalid syntax')
    
    def nextToken(self):
        if self.pos < self.length:
            self.pos += 1
            return self.TokenStack[self.pos]
        else:
            self.error()

    def eat(self, token_type):
        if self.current_token['type'] == token_type:
            temp = self.current_token
            self.current_token['type'] = temp['type']
            self.current_token['value'] = temp['value']
        else:
            self.error()
    
    
    
    def factor(self):
        token = self.current_token

        if token['type'] == tokens['NUM']:
            self.eat(tokens['NUM'])
            return token['value']
        elif token['type'] == tokens['LPAREN']:
            self.eat(tokens['LPAREN'])
            result = self.expr()
            self.eat(tokens['RPAREN'])
            return result
        elif token['type'] == tokens['STRING']:
            self.eat(tokens['STRING'])
            return token['value']
        elif token['type'] == tokens['IDENTIFIER']:
            self.eat(tokens['IDENTIFIER'])
            return token['value']
        elif token['type'] == tokens['BOOL']:
            self.eat(tokens['BOOL'])
            return token['value']
        elif token['type'] == tokens['NIL']:
            self.eat(tokens['NIL'])
            return token['value']
        elif token['type'] == tokens['TRUE']:
            self.eat(tokens['TRUE'])
            return token['value']
        elif token['type'] == tokens['FALSE']:
            self.eat(tokens['FALSE'])
            return token['value']
        else:
            self.error()
    
    def term(self):
        result = self.factor()

        while self.current_token['type'] in (tokens['PLUS'], tokens['MINUS'], tokens['MULTIPLY'], tokens['DIVIDE']):
            token = self.current_token
            if token['type'] == tokens['PLUS']:
                self.eat(tokens['PLUS'])
                result += self.factor()
            elif token['type'] == tokens['MINUS']:
                self.eat(tokens['MINUS'])
                result -= self.factor()
            elif token['type'] == tokens['MULTIPLY']:
                self.eat(tokens['MULTIPLY'])
                result *= self.factor()
            elif token['type'] == tokens['DIVIDE']:
                self.eat(tokens['DIVIDE'])
                result /= self.factor()

        return result
    
    def expr(self):
        return self.term()
    
    def parse(self):
        return self.expr()