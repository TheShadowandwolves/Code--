import re

# Token types
INTEGER = 'INTEGER'
PLUS = 'PLUS'
MINUS = 'MINUS'
PRINT = 'PRINT'
LPAREN = 'LPAREN'
RPAREN = 'RPAREN'
COMMENT = 'COMMENT'
EOF = 'EOF'
ERROR = 'ERROR'

# Token class
class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __str__(self):
        return f'Token({self.type}, {self.value})'

    def __repr__(self):
        return self.__str__()

# Lexer
class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = 0

    def error(self):
        raise Exception('Invalid character')

    def get_next_token(self):
        text = self.text

        if self.pos >= len(text):
            return Token(EOF, None)

        current_char = text[self.pos]

        if current_char == '#':
            content = ""
            while self.pos < len(text) and text[self.pos] != '\n':
                content += text[self.pos]
                self.pos += 1
            return Token(COMMENT, content)

        if current_char.isspace():
            self.pos += 1
            return self.get_next_token()

        if current_char.isdigit():
            token = Token(INTEGER, int(current_char))
            self.pos += 1
            return token

        if current_char == '+':
            token = Token(PLUS, current_char)
            self.pos += 1
            return token

        if current_char == '-':
            token = Token(MINUS, current_char)
            self.pos += 1
            return token

        if current_char == '(':
            token = Token(LPAREN, current_char)
            self.pos += 1
            return token

        if current_char == ')':
            token = Token(RPAREN, current_char)
            self.pos += 1
            return token

        if current_char.isalpha():
            word = ""
            while self.pos < len(text) and text[self.pos].isalpha():
                word += text[self.pos]
                self.pos += 1
            if word == "print":
                return Token(PRINT, word)
            else:
                self.error()

        self.error()

    def __str__(self):
        return f'Lexer({self.text})'

# Parser
class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()

    def error(self):
        raise Exception('Invalid syntax')

    def eat(self, token_type):
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            self.error()

    def factor(self):
        token = self.current_token

        if token.type == INTEGER:
            self.eat(INTEGER)
            return token.value
        elif token.type == LPAREN:
            self.eat(LPAREN)
            result = self.expr()
            self.eat(RPAREN)
            return result

    def term(self):
        result = self.factor()

        while self.current_token.type in (PLUS, MINUS):
            token = self.current_token
            if token.type == PLUS:
                self.eat(PLUS)
                result += self.factor()
            elif token.type == MINUS:
                self.eat(MINUS)
                result -= self.factor()
            elif token.type == PRINT:
                self.eat(PRINT)
                print(result)
                return result
            elif token.type == COMMENT:
                self.eat(COMMENT)
                return result

        return result

    def expr(self):
        return self.term()

    def parse(self):
        return self.expr()
    
    def __str__(self):
        return f'Parser({self.lexer})'

# Interpreter
def interpret(text):
    lexer = Lexer(text)
    print("lexer " +str(lexer))
    parser = Parser(lexer)
    print("parser "+str(parser))
    result = parser.parse()
    return result

# Test the interpreter
text = """
print hello world
"""

try:
    print(text)
    result = interpret(text)
    print(result)
except Exception as e:
    print(f"Error: {e}")
