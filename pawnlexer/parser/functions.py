from .node import ASTNode
from .variable import NewVariable


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


# yacc rules
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
    p[0] = StockFunction(
        return_type=p[2],
        name=p[3],
        params=p[5],
        body=p[7],
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
                 | optional_tag NAME
                 | optional_tag NAME ASSIGN expression'''
    # | optional_tag NAME LBRACKET RBRACKET
    # | optional_tag NAME LBRACKET expression RBRACKET
    if len(p) == 3: # tag:name
        p[0] = NewVariable(tag=p[1], name=p[2])
    elif len(p) == 4: # name = value
        p[0] = NewVariable(name=p[1], value=p[3])
    elif len(p) == 5: # tag:name = value
        p[0] = NewVariable(tag=p[1], name=p[2], value=p[4])
    else:
        p[0] = NewVariable(name=p[1])
    # todo: strings, arrays, variable args
    #elif len(p) == 5:  # tag:name[]
    #    p[0] = Parameter(name=p[2], return_type=return_type)
    #else:  # tag:name[size]
    #    p[0] = Parameter(name=p[2], return_type=return_type, size=p[4])