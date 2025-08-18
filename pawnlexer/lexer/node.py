t_ignore = ' \r\t\f'

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_whitespace(t):
    r'\s+'
    pass


def t_single_comment(t):
    r'/(\\\n)?/(\n|(.|\n)*?[^\\]\n)'
    pass

def t_multiline_comment(t):
    r'/(\\\n)?\*[\w\W]*?\*(\\\n)?/'
    pass