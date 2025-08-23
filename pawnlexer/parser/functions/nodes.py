from pawnlexer.parser.node import ASTNode


class StockFunction(ASTNode):
    def __init__(self, name, params, body, return_type=None, lineno=None):
        super().__init__(lineno)
        self.name = name
        self.params = params
        self.body = body
        self.return_type = return_type

    def __repr__(self):
        ret_type = f'{self.return_type}' if self.return_type else ''
        params = ', '.join(str(p) for p in self.params)
        return f"{self.__class__.__name__}(tag={ret_type}, name={self.name}, parameters=({params}), body=({self.body}))"


class Parameter(ASTNode):
    def __init__(self, name, type=None, default=None, lineno=None, return_type=None, size=1):
        super().__init__(lineno)
        self.name = name
        self.type = type
        self.default = default
        self.return_type = return_type
        self.size = size

    def __repr__(self):
        type_str = f": {self.type}" if self.type else ""
        default_str = f" = {self.default}" if self.default else ""
        return f"{self.__class__.__name__}(tag={self.return_type}, name={self.name}, type={type_str}{default_str})"