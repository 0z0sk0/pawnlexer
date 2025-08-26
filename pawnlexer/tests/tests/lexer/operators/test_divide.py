from ... import LexerTest


class TestOperatorDivide(LexerTest):
    content = '''
        x = 2 / 2;
    '''

    correct = '''
        NAME ASSIGN INTEGER DIVIDE INTEGER SEMICOLON
    '''