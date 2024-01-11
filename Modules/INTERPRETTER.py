import Modules.LEXER as Lexer
import Modules.PARSER as Parser
import Modules.OPERATION as OP

# Interpreter
class Interpreter:
    def __init__(self, text, Debug):
        self.stack = []
        self.text = text
        self.Debug = Debug

    def TOKENIZE(self):
        pos = 0
        lexer = Lexer.Lexer(self.text, self.Debug)
        while pos < len(self.text):
            self.stack.append(lexer.get_next_token())
            pos += 1
        self.Debug.df("stack", self.stack)
        
    def PARSE(self):
        parser = Parser.Parser(self.stack, self.Debug)
        result = parser.parse()
        for ar in result:
            match ar.op:
                case '+':
                    print(ar.args[0] + ar.args[1])
                case '-':
                    print(ar.args[0] - ar.args[1])
                case '*':
                    print(ar.args[0] * ar.args[1])
                case '/':
                    print(ar.args[0] / ar.args[1])

    




# def interpret(text):
#     lexer = Lexer(text)
#     print("lexer " +str(lexer))
#     parser = Parser(lexer)
#     print("parser "+str(parser))
#     result = parser.parse()
#     return result