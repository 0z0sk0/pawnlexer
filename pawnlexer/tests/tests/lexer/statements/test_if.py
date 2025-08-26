from ... import LexerTest


class TestStatementIf(LexerTest):
    content = '''
        if (x == 1)
        {
            x++;
        }
    '''

    correct = '''
        IF LPAREN NAME EQ INTEGER RPAREN 
        LBRACE 
            NAME INCREMENT SEMICOLON 
        RBRACE
    '''