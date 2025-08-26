import ply.lex as lex
import ply.yacc as yacc

from .tokens import tokens
from .lexer import lex_rules, tokens, reserved
from .parser import parse_rules, start


class PawnLexer:
    def __init__(self):
        self.start = start
        self.tokens = tokens
        self.reserved = reserved

        for name, rule in lex_rules.items():
            setattr(self, name, rule)
        self.lexer = lex.lex(module=self)

        for name, rule in parse_rules.items():
            setattr(self, name, rule)
        self.parser = yacc.yacc(module=self)

    def tokenize(self, line):
        tokenized_data = []
        self.lexer.input(line)
        for token in self.lexer:
            tokenized_data.append(token)
        return tokenized_data

    def parse(self, line):
        return self.parser.parse(line, lexer=self.lexer)