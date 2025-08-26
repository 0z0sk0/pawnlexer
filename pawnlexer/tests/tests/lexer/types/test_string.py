from ... import LexerTest


class TestTypeString(LexerTest):
    content = '''
        new x[] = "test";
    '''

    correct = '''
        NEW NAME LBRACKET RBRACKET ASSIGN STRING SEMICOLON
    '''