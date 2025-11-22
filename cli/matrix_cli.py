
import sys
from engine.parser import XLSLParser
from engine.interpreter import XLSLInterpreter

if __name__ == "__main__":
    src = open(sys.argv[1]).read()
    ast = XLSLParser(src).parse()
    print(XLSLInterpreter(ast).run())
