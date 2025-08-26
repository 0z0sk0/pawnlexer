from ... import LexerTest


class TestOperatorAssign(LexerTest):
    content = '''
        x = 1;
    '''

    correct = '''
        NAME ASSIGN INTEGER SEMICOLON
    '''