from ... import LexerTest


class TestStatementElseIf(LexerTest):
    content = '''
        if (x == 1)
        {
            x++;
        }
        else if (x == 2)
        {
            x = x + 1;
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
        ELSEIF LPAREN NAME EQ INTEGER RPAREN 
        LBRACE 
            NAME ASSIGN NAME PLUS INTEGER SEMICOLON 
        RBRACE
        ELSE 
        LBRACE 
            NAME DECREMENT SEMICOLON 
        RBRACE
    '''