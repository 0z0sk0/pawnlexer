from pawnlexer.parser.node import ASTNode


class NewVariable(ASTNode):
    def __init__(self, name, value = None, tag = None, constant = None, array_size = None, lineno = None):
        super().__init__(lineno)
        self.name = name
        self.value = value
        self.tag = 'Integer' if tag == '_' else tag
        self.constant = constant
        self.array_size = array_size

    def __repr__(self):
        return f"{self.__class__.__name__}(tag={self.tag}, name={self.name}, value={self.value}, constant={self.constant}, array_size={self.array_size})"


class StaticVariable(ASTNode):
    def __init__(self, name, value = None, tag = None, constant = None, array_size = None, lineno = None):
        super().__init__(lineno)
        self.name = name
        self.value = value
        self.tag = 'Integer' if tag == '_' else tag
        self.constant = constant
        self.array_size = array_size

    def __repr__(self):
        return f"{self.__class__.__name__}(tag={self.tag}, name={self.name}, value={self.value}, constant={self.constant}, array_size={self.array_size})"
