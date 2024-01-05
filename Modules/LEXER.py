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

        match current_char:
            case '#':
                # exclude the comment from the token list
                self.df("COMMENT", f"COMMENT, pos: {self.pos}")
                while self.pos < len(text) and text[self.pos] != '\n':
                    self.pos += 1
                return self.get_next_token()
                
            case '+':
                self.df("PLUS", f"PLUS, pos: {self.pos}")
                self.pos += 1
                return Token.Token('PLUS', current_char, pos=self.pos)
            
            case '-':
                self.df("MINUS", f"MINUS, pos: {self.pos}")
                self.pos += 1
                return Token.Token('MINUS', current_char, pos=self.pos)
            
            case '*':
                self.df("MULTIPLY", f"MULTIPLY, pos: {self.pos}")
                self.pos += 1
                return Token.Token('MULTIPLY', current_char, pos=self.pos)
            
            case '/':
                self.df("DIVIDE", f"DIVIDE, pos: {self.pos}")
                self.pos += 1
                return Token.Token('DIVIDE', current_char, pos=self.pos)
            
            case '(':
                self.df("LPAREN", f"LPAREN, pos: {self.pos}")
                self.pos += 1
                return Token.Token('LPAREN', current_char, pos=self.pos)
            
            case ')':
                self.df("RPAREN", f"RPAREN, pos: {self.pos}")
                self.pos += 1
                return Token.Token('RPAREN', current_char, pos=self.pos)
            
            case '{':
                self.df("LBRACE", f"LBRACE, pos: {self.pos}")
                self.pos += 1
                return Token.Token('LBRACE', current_char, pos=self.pos)
            
            case '}':
                self.df("RBRACE", f"RBRACE, pos: {self.pos}")
                self.pos += 1
                return Token.Token('RBRACE', current_char, pos=self.pos)
            
            case '=':
                self.df("EQUALS", f"EQUALS, pos: {self.pos}")
                self.pos += 1
                return Token.Token('EQUALS', current_char, pos=self.pos)
            
            case ' ':
                self.df("SPACE", f"SPACE, pos: {self.pos}")
                self.pos += 1
                return self.get_next_token()
            
            case '\n':
                self.df("NEWLINE", f"NEWLINE, pos: {self.pos}")
                self.pos += 1
                return self.get_next_token()
            
            case current_char.isdigit():
                self.df("NUM", f"NUM, pos: {self.pos}")
                num = ""
                while self.pos < len(text) and text[self.pos].isdigit():
                    num += text[self.pos]
                    self.pos += 1
                return Token.Token('NUM', int(num), pos=self.pos)
            
            case current_char.isalpha():
                self.df("IDENTIFIER", f"IDENTIFIER, pos: {self.pos}")
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
                    return Token.Token('IDENTIFIER', word, self.pos)

            case '"':
                self.df("STRING", f"STRING, pos: {self.pos}")
                self.pos += 1
                string = ""
                while self.pos < len(text) and text[self.pos] != '"':
                    string += text[self.pos]
                    self.pos += 1
                self.pos += 1
                return Token.Token('STRING', string, pos=self.pos)
            
            case "'":
                self.df("STRING", f"STRING, pos: {self.pos}")
                self.pos += 1
                string = ""
                while self.pos < len(text) and text[self.pos] != "'":
                    string += text[self.pos]
                    self.pos += 1
                self.pos += 1
                return Token.Token('STRING', string, pos=self.pos)
            
            case _:
                self.df("ERROR", f"ERROR, pos: {self.pos}")
                self.pos += 1
                return Token.Token('ERROR', current_char, pos=self.pos)


