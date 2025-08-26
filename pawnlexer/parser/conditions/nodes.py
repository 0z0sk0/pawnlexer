from pawnlexer.parser.node import ASTNode


class Condition(ASTNode):
    def __init__(self, lvalue = None, rvalue = None, operator = None):
        self.lvalue = lvalue
        self.rvalue = rvalue
        self.operator = operator

    def __repr__(self):
        params = ', '.join(f"{k}={v}" for k, v in self.__dict__.items())
        return f"{self.__class__.__name__}({params})"