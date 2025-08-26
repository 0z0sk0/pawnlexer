from ... import LexerTest


class TestOperatorParen(LexerTest):
    content = '''
        x[5] = {2, ...};
    '''

    correct = '''
        NAME LBRACKET INTEGER RBRACKET ASSIGN LBRACE INTEGER COMMA DOT DOT DOT RBRACE SEMICOLON
    '''