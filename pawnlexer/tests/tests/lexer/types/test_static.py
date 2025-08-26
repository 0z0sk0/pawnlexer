from ... import LexerTest


class TestTypeStatic(LexerTest):
    content = '''
        static x[] = "test";
    '''

    correct = '''
        STATIC NAME LBRACKET RBRACKET ASSIGN STRING SEMICOLON
    '''