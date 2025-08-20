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

def p_statement_list(p):
    '''statement_list : statement_list statement
                     | statement
                     | empty'''
    if len(p) == 3:
        p[0] = p[1] + [p[2]]
    elif len(p) == 2 and p[1] is not None:
        p[0] = [p[1]]
    else:
        p[0] = []


def p_statement(p):
    '''statement : variable_declaration
                 | function_declaration
                 | SEMICOLON'''  # Empty statement
    if len(p) > 2 or p[1] != ';':
        p[0] = p[1]
    else:
        p[0] = None  # Skip empty statements