from ... import LexerTest


class TestBitOperatorLeftShiftEq(LexerTest):
    content = '''
        x <<= 2;
    '''

    correct = '''
        NAME BIT_LEFTSHIFT_EQ INTEGER SEMICOLON
    '''