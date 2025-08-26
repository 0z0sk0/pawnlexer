from ... import LexerTest


class TestBitOperatorLeftShift(LexerTest):
    content = '''
        x = x << 2;
    '''

    correct = '''
        NAME ASSIGN NAME BIT_LEFTSHIFT INTEGER SEMICOLON
    '''