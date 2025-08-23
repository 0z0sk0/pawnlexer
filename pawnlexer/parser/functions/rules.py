from pawnlexer.parser.variables import Variable
from pawnlexer.parser.functions import StockFunction


def p_stock_impersonal_function(p):
    '''function_declaration : NAME LPAREN parameter_list RPAREN block
                            | optional_tag NAME LPAREN parameter_list RPAREN block'''
    p[0] = StockFunction(
        return_type=p[1],
        name=p[2],
        params=p[4],
        body=p[6],
        lineno=p.lineno(1)
    )


def p_stock_unbraced_function(p):
    '''function_declaration : STOCK NAME LPAREN parameter_list RPAREN unbraced_block
                            | STOCK optional_tag NAME LPAREN parameter_list RPAREN unbraced_block'''
    if len(p) == 8:
        p[0] = StockFunction(
            return_type=p[2],
            name=p[3],
            params=p[5],
            body=p[7],
            lineno=p.lineno(1)
        )
    else:
        p[0] = StockFunction(
            name=p[2],
            params=p[4],
            body=p[6],
            lineno=p.lineno(1)
        )


def p_stock_function(p):
    '''function_declaration : STOCK NAME LPAREN parameter_list RPAREN block
                            | STOCK optional_tag NAME LPAREN parameter_list RPAREN block'''
    if len(p) == 7:
        p[0] = StockFunction(
            name=p[2],
            params=p[4],
            body=p[6],
            lineno=p.lineno(1)
        )
    elif len(p) == 8:
        p[0] = StockFunction(
            return_type=p[2],
            name=p[3],
            params=p[4],
            body=p[6],
            lineno=p.lineno(1)
        )


def p_block(p):
    '''block : LBRACE statement_list RBRACE'''
    if len(p) == 4:
        p[0] = p[2]
    else:
        p[0] = []


def p_unbraced_block(p):
    '''unbraced_block : statement'''
    p[0] = p[1]


def p_parameter_list(p):
    '''parameter_list : parameter_list COMMA parameter
                     | parameter
                     | empty'''
    if len(p) == 4:
        p[0] = p[1] + [p[3]]
    elif len(p) == 2 and p[1] is not None:
        p[0] = [p[1]]
    else:
        p[0] = []


def p_parameter(p):
    '''parameter : NAME
                 | NAME ASSIGN expression
                 | NAME LBRACKET RBRACKET
                 | NAME LBRACKET expression RBRACKET
                 | CONST NAME LBRACKET RBRACKET
                 | CONST NAME LBRACKET expression RBRACKET
                 | optional_tag NAME
                 | optional_tag NAME ASSIGN expression
                 | optional_tag NAME LBRACKET RBRACKET
                 | optional_tag NAME LBRACKET expression RBRACKET'''
    params = {'name': None, 'tag': None, 'value': None, 'constant': False, 'array_size': None}
    tokens = p[1:] # reject left-value

    if tokens[0] == 'const':
        params['constant'] = True
        tokens = tokens[1:]

    if len(tokens) >= 2 and tokens[1] not in ['=', '[', ']']:
        params['tag'] = tokens[0]
        params['name'] = tokens[1]
        tokens = tokens[2:]
    else:
        params['name'] = tokens[0]
        tokens = tokens[1:]

    # are there any tokens left??
    if tokens:
        if tokens[0] == '=':
            params['value'] = tokens[1]
        elif tokens[0] == '[':
            if tokens[1] == ']':
                params['array_size'] = -1
            else:
                params['array_size'] = tokens[1]

    p[0] = Variable(**params)