from ... import LexerTest


class TestOperatorBrace(LexerTest):
    content = '''
        stock test() 
        { 
            x++;
        }
    '''

    correct = '''
        STOCK NAME LPAREN RPAREN 
        LBRACE 
            NAME INCREMENT SEMICOLON
        RBRACE
    '''