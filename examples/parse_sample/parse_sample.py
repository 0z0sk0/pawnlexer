from pawnlexer import PawnLexer


if __name__ == '__main__':
    pawnlexer = PawnLexer()

    with open('sample.pwn', 'r') as file:
        data = file.read()
        parsed = pawnlexer.parse(data)
        print(parsed)