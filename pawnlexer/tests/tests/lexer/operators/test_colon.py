from ... import LexerTest


class TestOperatorColon(LexerTest):
    content = '''
        x = 1 ? 1 : 2;
    '''

    correct = '''
        NAME ASSIGN INTEGER QMARK INTEGER COLON INTEGER SEMICOLON
    '''