from pawnlexer.parser.node import ASTNode


class Variable(ASTNode):
    def __init__(self, name, value = None, tag = None,
                 modificators = None, array_size = None,
                 type = None, lineno = None):
        super().__init__(lineno)
        self.name = name
        self.value = value
        self.tag = 'Integer' if tag == '_' else tag
        self.modificators = modificators
        self.array_size = array_size
        self.type = type

    def __repr__(self):
        params = ', '.join(f"{k}={v}" for k, v in self.__dict__.items())
        return f"{self.__class__.__name__}({params})"