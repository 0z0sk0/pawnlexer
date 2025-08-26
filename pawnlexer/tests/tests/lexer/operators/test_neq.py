from ... import LexerTest


class TestOperatorNeq(LexerTest):
    content = '''
        x = 2 != 2;
    '''

    correct = '''
        NAME ASSIGN INTEGER NEQ INTEGER SEMICOLON
    '''