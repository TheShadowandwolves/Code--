import Modules.LEXER as Lexer
import Modules.PARSER as Parser

# Interpreter
class Interpreter:
    def __init__(self, text, Debug):
        self.stack = []
        self.text = text
        self.Debug = Debug

    def TOKENIZE(self):
        pos = 0
        lexer = Lexer.Lexer(self.text)
        while pos < len(self.text):
            self.stack.append(lexer.get_next_token())
            pos += 1
        
    


    def __str__(self):
        self.Debug.df("RESULT",self.result)
        return str(self.result)


# def interpret(text):
#     lexer = Lexer(text)
#     print("lexer " +str(lexer))
#     parser = Parser(lexer)
#     print("parser "+str(parser))
#     result = parser.parse()
#     return result