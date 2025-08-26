from ... import LexerTest


class TestFunctionForward(LexerTest):
    content = '''
        forward test();
    '''

    correct = '''
        FORWARD NAME LPAREN RPAREN SEMICOLON
    '''