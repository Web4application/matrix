
class XLSLInterpreter:
    def __init__(self, ast):
        self.ast = ast

    def run(self):
        return {
            "status": "ok",
            "functions_detected": [f.name for f in self.ast.get("functions", [])]
        }
