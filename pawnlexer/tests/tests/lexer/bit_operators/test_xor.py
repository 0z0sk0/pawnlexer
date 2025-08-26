from ... import LexerTest


class TestBitOperatorXor(LexerTest):
    content = '''
        x = x ^ 6;
    '''

    correct = '''
        NAME ASSIGN NAME BIT_XOR INTEGER SEMICOLON
    '''