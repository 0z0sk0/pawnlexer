tokens = (
    'PUBLIC',
    'STOCK',
    'NATIVE'
)


def t_STOCK(t):
    r'\bstock\b'
    return t


def t_PUBLIC(t):
    r'\bpublic\b'
    return t