from ... import LexerTest


class TestOperatorIncrement(LexerTest):
    content = '''
        x++;
    '''

    correct = '''
        NAME INCREMENT SEMICOLON
    '''