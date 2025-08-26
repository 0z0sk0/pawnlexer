from ... import LexerTest


class TestStatementFor(LexerTest):
    content = '''
        for (new i = 0; i < 5; i++)
        {
            x = i + 1;
        }
    '''

    correct = '''
        FOR LPAREN NEW NAME ASSIGN INTEGER SEMICOLON NAME LESS INTEGER SEMICOLON NAME INCREMENT RPAREN
        LBRACE
            NAME ASSIGN NAME PLUS INTEGER SEMICOLON
        RBRACE
    '''