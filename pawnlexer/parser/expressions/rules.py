from pawnlexer.parser.expressions import BinaryOperation
from pawnlexer.parser.types import Integer, Float, String


def p_expression_list(p):
    '''expression_list : expression
                       | expression_list COMMA expression'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]


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


def p_factor_float(p):
    'factor : FLOAT'
    p[0] = Float(value=p[1], lineno=p.lineno(1))

def p_factor_string(p):
    'factor : STRING'
    p[0] = String(value=p[1], lineno=p.lineno(1))


def p_factor_expr(p):
    'factor : LPAREN expression RPAREN'
    p[0] = p[2]
