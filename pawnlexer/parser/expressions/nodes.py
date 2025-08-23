from pawnlexer.parser.node import ASTNode


class BinaryOperation(ASTNode):
    def __init__(self, op, left, right, lineno=None):
        super().__init__(lineno)
        self.op = op
        self.left = left
        self.right = right

    def __repr__(self):
        return f"{self.__class__.__name__}({self.op}, {self.left}, {self.right})"