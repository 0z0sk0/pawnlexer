from ... import LexerTest


class TestStatementWhile(LexerTest):
    content = '''
        while (1 != 2)
        {
            x++;
        }
    '''

    correct = '''
        WHILE LPAREN INTEGER NEQ INTEGER RPAREN
        LBRACE
            NAME INCREMENT SEMICOLON
        RBRACE
    '''