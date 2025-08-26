from ... import LexerTest


class TestOperatorMod(LexerTest):
    content = '''
        x = 3 % 2;
    '''

    correct = '''
        NAME ASSIGN INTEGER MOD INTEGER SEMICOLON
    '''