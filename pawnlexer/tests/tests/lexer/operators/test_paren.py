from ... import LexerTest


class TestOperatorParen(LexerTest):
    content = '''
        x = (1 - 2);
    '''

    correct = '''
        NAME ASSIGN LPAREN INTEGER MINUS INTEGER RPAREN SEMICOLON
    '''