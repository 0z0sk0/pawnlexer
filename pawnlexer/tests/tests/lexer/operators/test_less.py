from ... import LexerTest


class TestOperatorLess(LexerTest):
    content = '''
        x = x < 2 ? 1 : 2;
    '''

    correct = '''
        NAME ASSIGN NAME LESS INTEGER QMARK INTEGER COLON INTEGER SEMICOLON
    '''