from .node import ASTNode


class Program(ASTNode):
    def __init__(self, statements):
        super().__init__()
        self.statements = statements

    def __repr__(self):
        return f"{self.__class__.__name__}({self.statements})"


# yacc rules
def p_program(p):
    '''program : program statement
              | statement'''
    if len(p) == 3:
        p[0] = Program(statements=p[1].statements + [p[2]])
    else:
        p[0] = Program(statements=[p[1]])

def p_statement(p):
    '''statement : variable_declaration
                 | expression SEMICOLON'''
    p[0] = p[1]