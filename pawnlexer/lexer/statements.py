reserved = {
    'if': 'IF',
    'else': 'ELSE',
    'elseif': 'ELSEIF',
    'for': 'FOR',
    'while': 'WHILE',
    'do': 'DO',
}

def t_STATEMENT(t):
    r'(elseif|else\s+if|if|else|for|while|do)\b'
    normalized = t.value.replace(' ', '').lower()
    t.type = reserved.get(normalized, 'NAME')
    return t
