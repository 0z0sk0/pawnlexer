from ... import LexerTest


class TestDirectivePragma(LexerTest):
    content = '''
        #pragma unused test
    '''

    correct = '''
        PRAGMA NAME NAME
    '''