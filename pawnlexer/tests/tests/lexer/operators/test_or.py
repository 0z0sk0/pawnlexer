from ... import LexerTest


class TestOperatorOr(LexerTest):
    content = '''
        x = 2 || 2;
    '''

    correct = '''
        NAME ASSIGN INTEGER OR INTEGER SEMICOLON
    '''