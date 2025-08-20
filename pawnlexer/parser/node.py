class ASTNode:
    def __init__(self, lineno=None):
        self.lineno = lineno

    def __repr__(self):
        return f"{self.__class__.__name__}()"


# yacc rules
def p_error(p):
    if p:
        print(f"Syntax error at line {p.lineno}, token {p.type} ('{p.value}')")
    else:
        print("Syntax error at EOF")


def p_empty(p):
    'empty :'
    p[0] = None

