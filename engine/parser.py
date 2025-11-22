
from engine.utils.tokenizer import Tokenizer

class ASTNode: pass

class FuncDef(ASTNode):
    def __init__(self, name, args): self.name=name; self.args=args

class XLSLParser:
    def __init__(self, src):
        self.tokens = Tokenizer(src).tokenize()

    def parse(self):
        # Minimal stub parser
        funcs = []
        for i, t in enumerate(self.tokens):
            if t.value == "define" and i+1 < len(self.tokens):
                name = self.tokens[i+1].value
                funcs.append(FuncDef(name, []))
        return {"functions": funcs}
