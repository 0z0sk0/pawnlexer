import ply.lex as lex

from .tokens import tokens
from .lexer import lex_rules, tokens, start


class PawnLexer:
    def __init__(self):
        self.start = start
        self.tokens = tokens

        for name, rule in lex_rules.items():
            setattr(self, name, rule)
        self.lexer = lex.lex(module=self)

    def tokenize(self, line):
        tokenized_data = []
        self.lexer.input(line)
        for token in self.lexer:
            tokenized_data.append(token)
        return tokenized_data