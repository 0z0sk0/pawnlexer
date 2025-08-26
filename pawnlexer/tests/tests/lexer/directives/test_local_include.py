from ... import LexerTest


class TestDirectiveLocalInclude(LexerTest):
    content = '''
        #include "test.pwn"
    '''

    correct = '''
        LOCAL_INCLUDE
    '''