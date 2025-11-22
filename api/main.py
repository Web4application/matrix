
from fastapi import FastAPI
from engine.parser import XLSLParser
from engine.interpreter import XLSLInterpreter

app = FastAPI()

@app.post('/run')
def run_xlsl(source: str):
    ast = XLSLParser(source).parse()
    result = XLSLInterpreter(ast).run()
    return result
