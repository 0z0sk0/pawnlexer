from ... import LexerTest


class TestTypeConst(LexerTest):
    content = '''
        const x[] = "test";
    '''

    correct = '''
        CONST NAME LBRACKET RBRACKET ASSIGN STRING SEMICOLON
    '''