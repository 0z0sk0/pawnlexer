from ... import LexerTest


class TestBitOperatorNot(LexerTest):
    content = '''
        x = ~x;
    '''

    correct = '''
        NAME ASSIGN BIT_NOT NAME SEMICOLON
    '''