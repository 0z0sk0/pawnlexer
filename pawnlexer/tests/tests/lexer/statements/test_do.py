from ... import LexerTest


class TestStatementDo(LexerTest):
    content = '''
        do
        {
            x++;
        }
        while (1 != 2);
    '''

    correct = '''
        DO
        LBRACE
            NAME INCREMENT SEMICOLON
        RBRACE
        WHILE LPAREN INTEGER NEQ INTEGER RPAREN SEMICOLON
    '''