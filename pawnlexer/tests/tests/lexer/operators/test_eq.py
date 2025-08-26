from ... import LexerTest


class TestOperatorEq(LexerTest):
    content = '''
        x = 2 == 2;
    '''

    correct = '''
        NAME ASSIGN INTEGER EQ INTEGER SEMICOLON
    '''