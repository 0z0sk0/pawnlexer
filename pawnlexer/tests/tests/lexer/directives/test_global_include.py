from ... import LexerTest


class TestDirectiveGlobalInclude(LexerTest):
    content = '''
        #include <test.pwn>
    '''

    correct = '''
        GLOBAL_INCLUDE
    '''