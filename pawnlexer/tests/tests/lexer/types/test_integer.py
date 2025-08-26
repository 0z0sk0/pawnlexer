from ... import LexerTest


class TestTypeInteger(LexerTest):
    content = '''
        new x = 3;
    '''

    correct = '''
        NEW NAME ASSIGN INTEGER SEMICOLON
    '''
