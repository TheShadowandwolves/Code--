import Modules.LEXER as Lexer
import Modules.PARSER as Parser

# Interpreter
class Interpreter:
    def __init__(self, text, Debug):
        self.lexer = Lexer.Lexer(text, Debug)
        self.parser = Parser.Parser(self.lexer, Debug)
        self.result = self.parser.parse()
        self.Debug = Debug

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