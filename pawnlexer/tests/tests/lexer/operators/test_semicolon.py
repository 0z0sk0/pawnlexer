from ... import LexerTest


class TestOperatorSemicolon(LexerTest):
    content = '''
        new x;
    '''

    correct = '''
        NEW NAME SEMICOLON
    '''