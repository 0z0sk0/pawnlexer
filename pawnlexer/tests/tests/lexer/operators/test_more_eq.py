from ... import LexerTest


class TestOperatorMoreEq(LexerTest):
    content = '''
        x = x >= 2 ? 1 : 2;
    '''

    correct = '''
        NAME ASSIGN NAME MORE_EQ INTEGER QMARK INTEGER COLON INTEGER SEMICOLON
    '''