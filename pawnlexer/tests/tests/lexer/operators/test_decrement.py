from ... import LexerTest


class TestOperatorDecrement(LexerTest):
    content = '''
        x--;
    '''

    correct = '''
        NAME DECREMENT SEMICOLON
    '''