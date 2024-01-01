import Modules.TOKENS as Token
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
    'NULL': 'NULL',
}
class Lexer:
    def __init__(self, text, Debug: DEBUG.Debug):
        self.text = text
        self.pos = 0
        self.df = Debug.df

    def error(self):
        self.df("ERROR", "Invalid character")
        raise Exception('Invalid character')

    def get_next_token(self):
        text = self.text
        self.df("GET_NEXT_TOKEN", f"pos: {self.pos}, text: {text}")
        if self.pos >= len(text):
            self.df("GET_NEXT_TOKEN", f"EOF, pos: {self.pos}")
            return Token.Token('EOF', None, pos=self.pos)

        current_char = self.df("CURRENT_TEXT",text[self.pos])

        if current_char == '#':
            # exclude the comment from the token list
            self.df("COMMENT", f"COMMENT, pos: {self.pos}")
            while self.pos < len(text) and text[self.pos] != '\n':
                self.pos += 1
            return self.get_next_token()

        if current_char.isspace():
            self.df("SPACE", f"SPACE, pos: {self.pos}")
            self.pos += 1
            return self.get_next_token()

        if current_char.isdigit():
            num = ""
            while self.pos < len(text) and text[self.pos].isdigit():
                num += text[self.pos]
                self.pos += 1
            return Token.Token('NUM', int(num), pos=self.pos)
        
        if current_char == '"' or current_char == "'":
            self.pos += 1
            string = ""
            while self.pos < len(text) and text[self.pos] != '"':
                string += text[self.pos]
                self.pos += 1
            self.pos += 1
            return Token.Token('STRING', string, pos=self.pos)

        if current_char == '+':
            token = Token.Token('PLUS', current_char, pos=self.pos)
            self.pos += 1
            return token

        if current_char == '-':
            token = Token.Token('MINUS', current_char, pos=self.pos)
            self.pos += 1
            return token

        if current_char == '(':
            token = Token.Token('LPAREN', current_char, pos=self.pos)
            self.pos += 1
            return token

        if current_char == ')':
            token = Token.Token('RPAREN', current_char, pos=self.pos)
            self.pos += 1
            return token

        if current_char.isalpha():
            word = ""
            while self.pos < len(text) and text[self.pos].isalpha():
                word += text[self.pos]
                self.pos += 1
            if word == "print":
                while self.pos < len(text):
                    self.pos += 1
                return Token.Token('PRINT', word, self.pos)
            elif word in tokens:
                return Token.Token(tokens[word], word, self.pos)
            else:
                self.error()

        self.error()

    def tokenize(self):
        tokens = []
        while self.pos < len(self.text):
            tokens.append(self.get_next_token())
        return tokens


