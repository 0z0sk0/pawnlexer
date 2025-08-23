from pawnlexer.parser.variables import NewVariable, StaticVariable


def p_array_declaration(p):
    '''array_declaration : LBRACE expression_list RBRACE
                        | LBRACE RBRACE'''
    if len(p) == 4:
        p[0] = Node('ArrayLiteral', p[2])
    else:
        p[0] = Node('ArrayLiteral', [])

def p_variable_declaration(p):
    '''variable_declaration : NEW NAME SEMICOLON
                            | NEW NAME ASSIGN expression SEMICOLON
                            | NEW NAME LBRACKET expression RBRACKET SEMICOLON
                            | NEW NAME LBRACKET RBRACKET ASSIGN expression SEMICOLON
                            | NEW NAME LBRACKET expression RBRACKET ASSIGN expression SEMICOLON
                            | NEW optional_tag NAME ASSIGN expression SEMICOLON
                            | NEW optional_tag NAME SEMICOLON
                            | NEW optional_tag NAME LBRACKET RBRACKET SEMICOLON
                            | NEW optional_tag NAME LBRACKET RBRACKET ASSIGN expression SEMICOLON
                            | NEW optional_tag NAME LBRACKET expression RBRACKET ASSIGN expression SEMICOLON

                            | CONST NAME ASSIGN expression SEMICOLON
                            | CONST NAME SEMICOLON
                            | CONST NAME LBRACKET RBRACKET SEMICOLON
                            | CONST NAME LBRACKET RBRACKET ASSIGN expression SEMICOLON
                            | CONST NAME LBRACKET expression RBRACKET ASSIGN expression SEMICOLON
                            | CONST optional_tag NAME ASSIGN expression SEMICOLON
                            | CONST optional_tag NAME SEMICOLON
                            | CONST optional_tag NAME LBRACKET RBRACKET SEMICOLON
                            | CONST optional_tag NAME LBRACKET RBRACKET ASSIGN expression SEMICOLON
                            | CONST optional_tag NAME LBRACKET expression RBRACKET ASSIGN expression SEMICOLON

                            | STATIC NAME ASSIGN expression SEMICOLON
                            | STATIC NAME SEMICOLON
                            | STATIC NAME LBRACKET RBRACKET SEMICOLON
                            | STATIC NAME LBRACKET RBRACKET ASSIGN expression SEMICOLON
                            | STATIC NAME LBRACKET expression RBRACKET ASSIGN expression SEMICOLON
                            | STATIC optional_tag NAME ASSIGN expression SEMICOLON
                            | STATIC optional_tag NAME SEMICOLON
                            | STATIC optional_tag NAME LBRACKET RBRACKET SEMICOLON
                            | STATIC optional_tag NAME LBRACKET RBRACKET ASSIGN expression SEMICOLON
                            | STATIC optional_tag NAME LBRACKET expression RBRACKET ASSIGN expression SEMICOLON

                            | STATIC CONST NAME ASSIGN expression SEMICOLON
                            | STATIC CONST NAME SEMICOLON
                            | STATIC CONST NAME LBRACKET RBRACKET SEMICOLON
                            | STATIC CONST NAME LBRACKET RBRACKET ASSIGN expression SEMICOLON
                            | STATIC CONST NAME LBRACKET expression RBRACKET ASSIGN expression SEMICOLON
                            | STATIC CONST optional_tag NAME ASSIGN expression SEMICOLON
                            | STATIC CONST optional_tag NAME SEMICOLON
                            | STATIC CONST optional_tag NAME LBRACKET RBRACKET SEMICOLON
                            | STATIC CONST optional_tag NAME LBRACKET RBRACKET ASSIGN expression SEMICOLON
                            | STATIC CONST optional_tag NAME LBRACKET expression RBRACKET ASSIGN expression SEMICOLON'''
    var_type = 'NEW'
    params = {'name': None, 'tag': None, 'value': None, 'constant': False, 'array_size': None}

    tokens = list(p[1:]) # reject left-value

    if tokens and tokens[0] == 'static':
        var_type = 'STATIC'
        tokens = tokens[1:]
    if tokens and tokens[0] == 'const':
        params['constant'] = True
        tokens = tokens[1:]
    if tokens and tokens[0] == 'new':
        var_type = 'NEW'
        tokens = tokens[1:]

    if len(tokens) >= 2 and isinstance(tokens[0], str) and tokens[1] not in ['=', '[', ']']:
        params['tag'] = tokens[0]
        params['name'] = tokens[1]
        tokens = tokens[2:]
    else:
        params['name'] = tokens[0]
        tokens = tokens[1:]

    if tokens and tokens[0] == '[':
        if len(tokens) >= 3 and tokens[1] == ']':
            params['array_size'] = -1
            tokens = tokens[2:]
        elif len(tokens) >= 4 and tokens[2] == ']':
            params['array_size'] = tokens[1]
            tokens = tokens[3:]

    if tokens and tokens[0] == '=':
        if len(tokens) >= 2:
            params['value'] = tokens[1]
            tokens = tokens[2:]

    if var_type == 'STATIC':
        p[0] = StaticVariable(**params)
    elif var_type == 'NEW':
        p[0] = NewVariable(**params)
