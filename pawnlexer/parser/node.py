class ASTNode:
    def __init__(self, lineno=None):
        self.lineno = lineno

    def __repr__(self):
        return f"{self.__class__.__name__}()"


