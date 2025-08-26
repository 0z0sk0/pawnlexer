from ... import LexerTest


class TestOperatorTimes(LexerTest):
    content = '''
        x = 1 * 2;
    '''

    correct = '''
        NAME ASSIGN INTEGER TIMES INTEGER SEMICOLON
    '''