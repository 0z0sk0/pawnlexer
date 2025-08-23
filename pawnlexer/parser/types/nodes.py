from pawnlexer.parser.node import ASTNode


class Integer(ASTNode):
    def __init__(self, value, lineno=None):
        super().__init__(lineno)
        self.value = value

    def __repr__(self):
        return f"{self.__class__.__name__}(value={self.value})"


class Float(ASTNode):
    def __init__(self, value, lineno=None):
        super().__init__(lineno)
        self.value = value

    def __repr__(self):
        return f"{self.__class__.__name__}(value={self.value})"


class String(ASTNode):
    def __init__(self, value, size = None, constant = None, static = None, lineno=None):
        super().__init__(lineno)
        self.value = value
        self.size = size if size else (len(value) + 1)
        self.constant = constant
        self.static = static

    def __repr__(self):
        return f"{self.__class__.__name__}(value={self.value}, size={self.size}, constant={self.constant}, static={self.static})"