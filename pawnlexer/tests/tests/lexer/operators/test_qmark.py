from ... import LexerTest


class TestOperatorQMark(LexerTest):
    content = '''
        x = 1 ? 1 : 1;
    '''

    correct = '''
        NAME ASSIGN INTEGER QMARK INTEGER COLON INTEGER SEMICOLON
    '''