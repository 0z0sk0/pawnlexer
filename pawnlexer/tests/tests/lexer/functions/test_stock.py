from ... import LexerTest


class TestFunctionStock(LexerTest):
    content = '''
        stock test() x++;
    '''

    correct = '''
        STOCK NAME LPAREN RPAREN NAME INCREMENT SEMICOLON
    '''