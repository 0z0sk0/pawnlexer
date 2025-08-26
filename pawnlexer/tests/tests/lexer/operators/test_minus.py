from ... import LexerTest


class TestOperatorMinus(LexerTest):
    content = '''
        x = 1 - 2;
    '''

    correct = '''
        NAME ASSIGN INTEGER MINUS INTEGER SEMICOLON
    '''