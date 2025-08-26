from ... import LexerTest


class TestBitOperatorRightShiftEq(LexerTest):
    content = '''
        x >>= 2;
    '''

    correct = '''
        NAME BIT_RIGHTSHIFT_EQ INTEGER SEMICOLON
    '''