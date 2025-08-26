from ... import LexerTest


class TestStatementElse(LexerTest):
    content = '''
        if (x == 1)
        {
            x++;
        }
        else
        {
            x--;
        }
    '''

    correct = '''
        IF LPAREN NAME EQ INTEGER RPAREN 
        LBRACE 
            NAME INCREMENT SEMICOLON 
        RBRACE 
        ELSE 
        LBRACE 
            NAME DECREMENT SEMICOLON 
        RBRACE
    '''