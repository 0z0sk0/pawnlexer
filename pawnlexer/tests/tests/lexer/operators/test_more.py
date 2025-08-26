from ... import LexerTest


class TestOperatorMore(LexerTest):
    content = '''
        x = x > 2 ? 1 : 2;
    '''

    correct = '''
        NAME ASSIGN NAME MORE INTEGER QMARK INTEGER COLON INTEGER SEMICOLON
    '''