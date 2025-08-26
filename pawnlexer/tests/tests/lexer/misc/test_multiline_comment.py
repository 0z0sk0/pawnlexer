from ... import LexerTest


class TestMiscMultilineComment(LexerTest):
    content = '''
        /*
        Very Useful Text
        */
    '''

    correct = '''''' # Because comments must be bypassed