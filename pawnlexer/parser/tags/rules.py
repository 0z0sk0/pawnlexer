def p_optional_tag(p):
    '''optional_tag : NAME COLON
                    | empty'''
    if len(p) == 3:
        p[0] = p[1]
    else:
        p[0] = None
