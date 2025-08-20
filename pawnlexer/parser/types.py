from .node import ASTNode


class Integer(ASTNode):
    def __init__(self, value, lineno=None):
        super().__init__(lineno)
        self.value = value

    def __repr__(self):
        return f"{self.__class__.__name__}({self.value})"


class Float(ASTNode):
    def __init__(self, value, lineno=None):
        super().__init__(lineno)
        self.value = value

    def __repr__(self):
        return f"{self.__class__.__name__}({self.value})"
