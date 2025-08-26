from ... import LexerTest


class TestBitOperatorAndEq(LexerTest):
    content = '''
        x &= 12;
    '''

    correct = '''
        NAME BIT_AND_EQ INTEGER SEMICOLON
    '''