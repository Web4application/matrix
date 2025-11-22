
import re

class Token:
    def __init__(self, type_, value):
        self.type = type_
        self.value = value
    def __repr__(self): return f"Token({self.type}, {self.value})"

class Tokenizer:
    TOKEN_REGEX = r"""(
        (?P<NUMBER>[0-9]+(?:\.[0-9]+)?) |
        (?P<IDENT>[A-Za-z_][A-Za-z0-9_]*) |
        (?P<OP>[+\-*/=<>!]+) |
        (?P<LPAREN>\() |
        (?P<RPAREN>\)) |
        (?P<COLON>:) |
        (?P<NEWLINE>\n)
    )"""

    def __init__(self, text):
        self.text = text

    def tokenize(self):
        tokens = []
        for match in re.finditer(self.TOKEN_REGEX, self.text, re.VERBOSE):
            kind = match.lastgroup
            value = match.group().strip()
            if value:
                tokens.append(Token(kind, value))
        return tokens
