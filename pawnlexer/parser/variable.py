from .node import ASTNode


class NewVariable(ASTNode):
    def __init__(self, name, value=None, lineno=None):
        super().__init__(lineno)
        self.name = name
        self.value = value

    def __repr__(self):
        val = f" = {self.value}" if self.value else ""
        return f"{self.__class__.__name__}({self.name}{val})"

def p_variable_declaration(p):
    '''variable_declaration : NEW NAME ASSIGN expression SEMICOLON
                            | NEW NAME SEMICOLON'''
    lineno = p.lineno(1)
    if len(p) == 6:
        p[0] = NewVariable(name=p[2], value=p[4], lineno=lineno)
    else:
        p[0] = NewVariable(name=p[2], lineno=lineno)
