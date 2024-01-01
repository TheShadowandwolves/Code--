import re
from Modules import INTERPRETTER 
from Modules import DEBUG

COMPILE_RUN = True
Debug = DEBUG.Debug()

while COMPILE_RUN:
    text = input('compilerAI> ')
    if text == 'exit':
        COMPILE_RUN = False
        Debug.end()
        break
    Debug.now()
    Debug.df("Text input",text)
    interpretter = INTERPRETTER.Interpreter(text, Debug)
    print(interpretter)

