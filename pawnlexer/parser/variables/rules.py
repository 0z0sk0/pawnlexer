from pawnlexer.parser.variables import Variable


def p_variable_declaration(p):
    '''variable_declaration : NEW NAME SEMICOLON
                            | NEW NAME ASSIGN expression SEMICOLON
                            | NEW NAME LBRACKET expression RBRACKET SEMICOLON
                            | NEW NAME LBRACKET RBRACKET ASSIGN LBRACE expression_list RBRACE SEMICOLON
                            | NEW NAME LBRACKET expression RBRACKET ASSIGN LBRACE expression_list RBRACE SEMICOLON
                            | NEW optional_tag NAME SEMICOLON
                            | NEW optional_tag NAME ASSIGN expression SEMICOLON
                            | NEW optional_tag NAME LBRACKET expression RBRACKET SEMICOLON
                            | NEW optional_tag NAME LBRACKET RBRACKET ASSIGN LBRACE expression_list RBRACE SEMICOLON
                            | NEW optional_tag NAME LBRACKET expression RBRACKET ASSIGN LBRACE expression_list RBRACE SEMICOLON

                            | STATIC NAME SEMICOLON
                            | STATIC NAME ASSIGN expression SEMICOLON
                            | STATIC NAME LBRACKET expression RBRACKET SEMICOLON
                            | STATIC NAME LBRACKET RBRACKET ASSIGN LBRACE expression_list RBRACE SEMICOLON
                            | STATIC NAME LBRACKET expression RBRACKET ASSIGN LBRACE expression_list RBRACE SEMICOLON
                            | STATIC optional_tag NAME SEMICOLON
                            | STATIC optional_tag NAME ASSIGN expression SEMICOLON
                            | STATIC optional_tag NAME LBRACKET expression RBRACKET SEMICOLON
                            | STATIC optional_tag NAME LBRACKET RBRACKET ASSIGN LBRACE expression_list RBRACE SEMICOLON
                            | STATIC optional_tag NAME LBRACKET expression RBRACKET ASSIGN LBRACE expression_list RBRACE SEMICOLON

                            | STOCK NAME SEMICOLON
                            | STOCK NAME ASSIGN expression SEMICOLON
                            | STOCK NAME LBRACKET expression RBRACKET SEMICOLON
                            | STOCK NAME LBRACKET RBRACKET ASSIGN LBRACE expression_list RBRACE SEMICOLON
                            | STOCK NAME LBRACKET expression RBRACKET ASSIGN LBRACE expression_list RBRACE SEMICOLON
                            | STOCK optional_tag NAME SEMICOLON
                            | STOCK optional_tag NAME ASSIGN expression SEMICOLON
                            | STOCK optional_tag NAME LBRACKET expression RBRACKET SEMICOLON
                            | STOCK optional_tag NAME LBRACKET RBRACKET ASSIGN LBRACE expression_list RBRACE SEMICOLON
                            | STOCK optional_tag NAME LBRACKET expression RBRACKET ASSIGN LBRACE expression_list RBRACE SEMICOLON

                            | CONST NAME ASSIGN expression SEMICOLON
                            | CONST optional_tag NAME ASSIGN expression SEMICOLON

                            | NEW CONST NAME SEMICOLON
                            | NEW CONST NAME ASSIGN expression SEMICOLON
                            | NEW CONST NAME LBRACKET RBRACKET SEMICOLON
                            | NEW CONST NAME LBRACKET expression RBRACKET SEMICOLON
                            | NEW CONST NAME LBRACKET RBRACKET ASSIGN LBRACE expression_list RBRACE SEMICOLON
                            | NEW CONST NAME LBRACKET expression RBRACKET ASSIGN LBRACE expression_list RBRACE SEMICOLON
                            | NEW CONST optional_tag NAME SEMICOLON
                            | NEW CONST optional_tag NAME ASSIGN expression SEMICOLON
                            | NEW CONST optional_tag NAME LBRACKET expression RBRACKET SEMICOLON
                            | NEW CONST optional_tag NAME LBRACKET RBRACKET ASSIGN LBRACE expression_list RBRACE SEMICOLON
                            | NEW CONST optional_tag NAME LBRACKET expression RBRACKET ASSIGN LBRACE expression_list RBRACE SEMICOLON

                            | NEW STOCK NAME SEMICOLON
                            | NEW STOCK NAME ASSIGN expression SEMICOLON
                            | NEW STOCK NAME LBRACKET RBRACKET SEMICOLON
                            | NEW STOCK NAME LBRACKET expression RBRACKET SEMICOLON
                            | NEW STOCK NAME LBRACKET RBRACKET ASSIGN LBRACE expression_list RBRACE SEMICOLON
                            | NEW STOCK NAME LBRACKET expression RBRACKET ASSIGN LBRACE expression_list RBRACE SEMICOLON
                            | NEW STOCK optional_tag NAME SEMICOLON
                            | NEW STOCK optional_tag NAME ASSIGN expression SEMICOLON
                            | NEW STOCK optional_tag NAME LBRACKET expression RBRACKET SEMICOLON
                            | NEW STOCK optional_tag NAME LBRACKET RBRACKET ASSIGN LBRACE expression_list RBRACE SEMICOLON
                            | NEW STOCK optional_tag NAME LBRACKET expression RBRACKET ASSIGN LBRACE expression_list RBRACE SEMICOLON

                            | STATIC CONST NAME SEMICOLON
                            | STATIC CONST NAME ASSIGN expression SEMICOLON
                            | STATIC CONST NAME LBRACKET expression RBRACKET SEMICOLON
                            | STATIC CONST NAME LBRACKET RBRACKET ASSIGN LBRACE expression_list RBRACE SEMICOLON
                            | STATIC CONST NAME LBRACKET expression RBRACKET ASSIGN LBRACE expression_list RBRACE SEMICOLON
                            | STATIC CONST optional_tag NAME SEMICOLON
                            | STATIC CONST optional_tag NAME ASSIGN expression SEMICOLON
                            | STATIC CONST optional_tag NAME LBRACKET expression RBRACKET SEMICOLON
                            | STATIC CONST optional_tag NAME LBRACKET RBRACKET ASSIGN LBRACE expression_list RBRACE SEMICOLON
                            | STATIC CONST optional_tag NAME LBRACKET expression RBRACKET ASSIGN LBRACE expression_list RBRACE SEMICOLON

                            | CONST STATIC NAME ASSIGN expression SEMICOLON
                            | CONST STATIC optional_tag NAME ASSIGN expression SEMICOLON

                            | STOCK CONST NAME SEMICOLON
                            | STOCK CONST NAME ASSIGN expression SEMICOLON
                            | STOCK CONST NAME LBRACKET expression RBRACKET SEMICOLON
                            | STOCK CONST NAME LBRACKET expression RBRACKET ASSIGN LBRACE expression_list RBRACE SEMICOLON
                            | STOCK CONST optional_tag NAME SEMICOLON
                            | STOCK CONST optional_tag NAME ASSIGN expression SEMICOLON
                            | STOCK CONST optional_tag NAME LBRACKET expression RBRACKET SEMICOLON
                            | STOCK CONST optional_tag NAME LBRACKET expression RBRACKET ASSIGN LBRACE expression_list RBRACE SEMICOLON

                            | STATIC STOCK NAME SEMICOLON
                            | STATIC STOCK NAME ASSIGN expression SEMICOLON
                            | STATIC STOCK NAME LBRACKET expression RBRACKET SEMICOLON
                            | STATIC STOCK NAME LBRACKET expression RBRACKET ASSIGN LBRACE expression_list RBRACE SEMICOLON
                            | STATIC STOCK optional_tag NAME SEMICOLON
                            | STATIC STOCK optional_tag NAME ASSIGN expression SEMICOLON
                            | STATIC STOCK optional_tag NAME LBRACKET expression RBRACKET SEMICOLON
                            | STATIC STOCK optional_tag NAME LBRACKET expression RBRACKET ASSIGN LBRACE expression_list RBRACE SEMICOLON

                            | STATIC STOCK CONST NAME SEMICOLON
                            | STATIC STOCK CONST NAME ASSIGN expression SEMICOLON
                            | STATIC STOCK CONST NAME LBRACKET expression RBRACKET SEMICOLON
                            | STATIC STOCK CONST NAME LBRACKET expression RBRACKET ASSIGN LBRACE expression_list RBRACE SEMICOLON
                            | STATIC STOCK CONST optional_tag NAME SEMICOLON
                            | STATIC STOCK CONST optional_tag NAME ASSIGN expression SEMICOLON
                            | STATIC STOCK CONST optional_tag NAME LBRACKET expression RBRACKET SEMICOLON
                            | STATIC STOCK CONST optional_tag NAME LBRACKET expression RBRACKET ASSIGN LBRACE expression_list RBRACE

                            | NEW STOCK CONST NAME SEMICOLON
                            | NEW STOCK CONST NAME ASSIGN expression SEMICOLON
                            | NEW STOCK CONST NAME LBRACKET RBRACKET SEMICOLON
                            | NEW STOCK CONST NAME LBRACKET expression RBRACKET SEMICOLON
                            | NEW STOCK CONST NAME LBRACKET RBRACKET ASSIGN LBRACE expression_list RBRACE SEMICOLON
                            | NEW STOCK CONST NAME LBRACKET expression RBRACKET ASSIGN LBRACE expression_list RBRACE SEMICOLON
                            | NEW STOCK CONST optional_tag NAME SEMICOLON
                            | NEW STOCK CONST optional_tag NAME ASSIGN expression SEMICOLON
                            | NEW STOCK CONST optional_tag NAME LBRACKET expression RBRACKET SEMICOLON
                            | NEW STOCK CONST optional_tag NAME LBRACKET RBRACKET ASSIGN LBRACE expression_list RBRACE SEMICOLON
                            | NEW STOCK CONST optional_tag NAME LBRACKET expression RBRACKET ASSIGN LBRACE expression_list RBRACE SEMICOLON'''
    params = {
        'name': None,
        'tag': None,
        'value': None,
        'modificators': [],
        'array_size': None,
        'type': None
    }

    parameters = []
    for param in p:
        parameters.append(param)
    parameters.pop(0) # reject left-value

    if not parameters:
        return

    def pop_parameter(key):
        parameters.remove(key)

    # No semicolon, are you sure?
    if ';' not in parameters:
        return
    pop_parameter(';')

    if 'static' in parameters:
        params['modificators'].append('STATIC')
        pop_parameter('static')
    if 'const' in parameters:
        params['modificators'].append('CONSTANT')
        pop_parameter('const')

    # interpret variable type
    if 'stock' in parameters:
        if 'new' in parameters:
            params['modificators'].append('STOCK')
        else:
            params['type'] = 'STOCK'
        pop_parameter('stock')
    if 'new' in parameters:
        params['type'] = 'NEW'
        pop_parameter('new')

    # interpret array size
    if '[' in parameters:
        index = parameters.index('[')
        if parameters[index + 1] == ']':
            params['array_size'] = -1
            for i in range(2):
                parameters.pop(index)
        else:
            params['array_size'] = parameters[index + 1]
            for i in range(3):
                parameters.pop(index)

    # interpret assign
    if '=' in parameters:
        if '{' in parameters:
            index = parameters.index('{')
            if parameters[index + 1] != '}':
                params['value'] = parameters[index + 1]
                for i in range(4):
                    parameters.pop(index - 1)
            else: # {}
                for i in range(2):
                    parameters.pop(index)
        else:
            index = parameters.index('=')
            params['value'] = parameters[index + 1]
            for i in range(2):
                parameters.pop(index)

    if len(parameters) == 2:
        params['tag'] = parameters[0]
        parameters.pop(0)
    params['name'] = parameters[0]

    p[0] = Variable(**params)
