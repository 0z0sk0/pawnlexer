from ... import LexerTest


class TestBitOperatorXorEq(LexerTest):
    content = '''
        x ^= 6;
    '''

    correct = '''
        NAME BIT_XOR_EQ INTEGER SEMICOLON
    '''