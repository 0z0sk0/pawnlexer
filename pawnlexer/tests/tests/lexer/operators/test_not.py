from ... import LexerTest


class TestOperatorNot(LexerTest):
    content = '''
        x = !x;
    '''

    correct = '''
        NAME ASSIGN NOT NAME SEMICOLON
    '''