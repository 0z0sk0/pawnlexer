from ... import LexerTest


class TestDirectiveDefine(LexerTest):
    content = '''
        #define NOT_THREE 3
    '''

    correct = '''
        DEFINE NAME INTEGER
    '''