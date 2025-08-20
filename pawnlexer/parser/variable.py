from .node import ASTNode


class NewVariable(ASTNode):
    def __init__(self, name, value=None, tag=None, lineno=None):
        super().__init__(lineno)
        self.name = name
        self.value = value
        self.tag = 'Integer' if tag == '_' else tag

    def __repr__(self):
        return f"{self.__class__.__name__}(tag={self.tag}, name={self.name}, value={self.value})"

def p_variable_declaration(p):
    '''variable_declaration : NEW NAME ASSIGN expression SEMICOLON
                            | NEW NAME SEMICOLON
                            | NEW optional_tag NAME ASSIGN expression SEMICOLON
                            | NEW optional_tag NAME SEMICOLON'''
    lineno = p.lineno(1)
    if len(p) == 6:
        p[0] = NewVariable(name=p[2], value=p[4], lineno=lineno)
    else:
        p[0] = NewVariable(name=p[2], lineno=lineno)
