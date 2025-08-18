from .node import ASTNode
from .types import Integer


class BinaryOperation(ASTNode):
    def __init__(self, op, left, right, lineno=None):
        super().__init__(lineno)
        self.op = op
        self.left = left
        self.right = right

    def __repr__(self):
        return f"{self.__class__.__name__}({self.op}, {self.left}, {self.right})"


# yacc rules
def p_expression_plus(p):
    'expression : expression PLUS term'
    p[0] = BinaryOperation(op='+', left=p[1], right=p[3], lineno=p.lineno(2))


def p_expression_minus(p):
    'expression : expression MINUS term'
    p[0] = BinaryOperation(op='-', left=p[1], right=p[3], lineno=p.lineno(2))


def p_expression_term(p):
    'expression : term'
    p[0] = p[1]


def p_term_times(p):
    'term : term TIMES factor'
    p[0] = BinaryOperation(op='*', left=p[1], right=p[3], lineno=p.lineno(2))


def p_term_div(p):
    'term : term DIVIDE factor'
    p[0] = BinaryOperation(op='/', left=p[1], right=p[3], lineno=p.lineno(2))


def p_term_factor(p):
    'term : factor'
    p[0] = p[1]


def p_factor_num(p):
    'factor : INTEGER'
    p[0] = Integer(value=p[1], lineno=p.lineno(1))


def p_factor_expr(p):
    'factor : LPAREN expression RPAREN'
    p[0] = p[2]
