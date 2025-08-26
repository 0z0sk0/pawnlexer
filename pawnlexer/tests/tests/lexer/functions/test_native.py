from ... import LexerTest


class TestFunctionNative(LexerTest):
    content = '''
        native test();
    '''

    correct = '''
        NATIVE NAME LPAREN RPAREN SEMICOLON
    '''