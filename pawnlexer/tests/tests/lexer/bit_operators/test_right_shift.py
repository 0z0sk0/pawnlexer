from ... import LexerTest


class TestBitOperatorRightShift(LexerTest):
    content = '''
        x = x >> 2;
    '''

    correct = '''
        NAME ASSIGN NAME BIT_RIGHTSHIFT INTEGER SEMICOLON
    '''