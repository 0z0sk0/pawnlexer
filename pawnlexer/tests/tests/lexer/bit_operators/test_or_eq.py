from ... import LexerTest


class TestBitOperatorOrEq(LexerTest):
    content = '''
        x |= 7;
    '''

    correct = '''
        NAME BIT_OR_EQ INTEGER SEMICOLON
    '''