tokens = (
    'STOCK',
    'FORWARD',
    'PUBLIC',
    'NATIVE'
)


def t_STOCK(t):
    r'\bstock\b'
    return t


def t_FORWARD(t):
    r'\bforward\b'
    return t


def t_PUBLIC(t):
    r'\bpublic\b'
    return t


def t_NATIVE(t):
    r'\bnative\b'
    return t