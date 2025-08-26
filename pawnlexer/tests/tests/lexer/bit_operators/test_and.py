from ... import LexerTest


class TestBitOperatorAnd(LexerTest):
    content = '''
        x = x & 12;
    '''

    correct = '''
        NAME ASSIGN NAME BIT_AND INTEGER SEMICOLON
    '''