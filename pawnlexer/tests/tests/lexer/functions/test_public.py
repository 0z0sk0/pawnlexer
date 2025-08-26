from ... import LexerTest


class TestFunctionPublic(LexerTest):
    content = '''
        public test();
    '''

    correct = '''
        PUBLIC NAME LPAREN RPAREN SEMICOLON
    '''