from ... import LexerTest


class TestMiscSingleComment(LexerTest):
    content = '''
        // some useful text
    '''

    correct = '''''' # Because comments must be bypassed