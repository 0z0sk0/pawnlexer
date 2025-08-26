from ... import LexerTest


class TestOperatorPlus(LexerTest):
    content = '''
        x = 1 + 2;
    '''

    correct = '''
        NAME ASSIGN INTEGER PLUS INTEGER SEMICOLON
    '''