from ... import LexerTest


class TestOperatorLessEq(LexerTest):
    content = '''
        x = x <= 2 ? 1 : 2;
    '''

    correct = '''
        NAME ASSIGN NAME LESS_EQ INTEGER QMARK INTEGER COLON INTEGER SEMICOLON
    '''