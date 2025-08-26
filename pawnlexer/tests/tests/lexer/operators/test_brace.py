from ... import LexerTest


class TestOperatorBrace(LexerTest):
    content = '''
        stock test() { return 1; });
    '''

    correct = '''
        STOCK NAME LPAREN RPAREN LBRACE RETURN INTEGER SEMICOLON RBRACE
    '''