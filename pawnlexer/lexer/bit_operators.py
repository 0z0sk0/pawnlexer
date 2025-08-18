tokens = [
    'BIT_AND',
    'BIT_AND_EQ',
    'BIT_OR',
    'BIT_OR_EQ',
    'BIT_XOR',
    'BIT_XOR_EQ',
    'BIT_NOT',
    'BIT_LEFTSHIFT',
    'BIT_LEFTSHIFT_EQ',
    'BIT_RIGHTSHIFT',
    'BIT_RIGHTSHIFT_EQ'
]


def t_BIT_AND(t):
    r'&(?!&|=)'
    return t


def t_BIT_AND_EQ(t):
    r'&='
    return t


def t_BIT_OR(t):
    r'\|(?!\||=)'
    return t


def t_BIT_OR_EQ(t):
    r'\|='
    return t


def t_BIT_XOR(t):
    r'\^(?!=)'
    return t


def t_BIT_XOR_EQ(t):
    r'\^='
    return t


def t_BIT_NOT(t):
    r'~'
    return t


def t_BIT_LEFTSHIFT(t):
    r'<<(?!=)'
    return t


def t_BIT_RIGHTSHIFT(t):
    r'>>(?!=)'
    return t


def t_BIT_LEFTSHIFT_EQ(t):
    r'<<='
    return t


def t_BIT_RIGHTSHIFT_EQ(t):
    r'>>='
    return t