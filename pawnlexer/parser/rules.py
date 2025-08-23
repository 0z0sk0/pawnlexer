def p_error(p):
    if p:
        print(f"Syntax error at line {p.lineno}, token {p.type} ('{p.value}')")
    else:
        print("Syntax error at EOF")


def p_empty(p):
    'empty :'
    p[0] = None
