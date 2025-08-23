from pawnlexer.parser.node import ASTNode


class Program(ASTNode):
    def __init__(self, statements):
        super().__init__()
        self.statements = statements

    def __repr__(self):
        return f"{self.__class__.__name__}({self.statements})"