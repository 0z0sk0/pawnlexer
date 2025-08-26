from ... import LexerTest


class TestTypeFloat(LexerTest):
    content = '''
        new Float:x = 3.0;
    '''

    correct = '''
        NEW NAME COLON NAME ASSIGN FLOAT SEMICOLON
    '''