tokens = (
    'NEW',
    'FLOAT',
    'INTEGER',
    'STRING',
    'ID'
)


def t_NEW(t):
    r'\bnew\b'
    return t


def t_FLOAT(t):
    r'(\d+\.\d*|\.\d+|\d+[fF])[fF]?'
    t.value = float(t.value)
    return t


def t_INTEGER(t):
    r'\d+[LlUu]*'
    t.value = int(t.value)
    return t


def t_STRING(t):
    r'\"([^\\\n]|(\\.))*?\"'
    t.value = t.value[1:-1]
    return t


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    return t