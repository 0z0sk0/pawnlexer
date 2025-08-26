from ... import LexerTest


class TestBitOperatorOr(LexerTest):
    content = '''
        x = x | 7;
    '''

    correct = '''
        NAME ASSIGN NAME BIT_OR INTEGER SEMICOLON
    '''