tokens = (
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'MOD',
    'EQ',
    'NEQ',
    'OR',
    'NOT',
    'INCREMENT',
    'DECREMENT',
    'LPAREN',
    'RPAREN',
    'LBRACE',
    'RBRACE',
    'LBRACKET',
    'RBRACKET',
    'COMMA',
    'SEMICOLON',
    'COLON',
    'DOT',
    'ASSIGN',
    'QMARK'
)


def t_PLUS(t):
    r'\+'
    return t


def t_MINUS(t):
    r'-'
    return t


def t_TIMES(t):
    r'\*'
    return t


def t_DIVIDE(t):
    r'/'
    return t


def t_MOD(t):
    r'%'
    return t


def t_EQ(t):
    r'=='
    return t


def t_NEQ(t):
    r'!='
    return t


def t_AND(t):
    r'&&'
    return t


def t_OR(t):
    r'\|\|'
    return t


def t_LPAREN(t):
    r'\('
    return t


def t_RPAREN(t):
    r'\)'
    return t


def t_LBRACE(t):
    r'\{'
    return t


def t_RBRACE(t):
    r'\}'
    return t


def t_COLON(t):
    r':'
    return t


def t_DOT(t):
    r'\.'
    return t


def t_LBRACKET(t):
    r'\['
    return t


def t_NOT(t):
    r'\!'
    return t


def t_RBRACKET(t):
    r'\]'
    return t


def t_SEMICOLON(t):
    r';'
    return t


def t_ASSIGN(t):
    r'='
    return t


def t_COMMA(t):
    r','
    return t


def t_INCREMENT(t):
    r'\+\+'
    return t


def t_DECREMENT(t):
    r'--'
    return t


def t_QMARK(t):
    r'\?'
    return t
