from buffer import Buffer
from scanner import LexicalScanner


if __name__ == '__main__':
    b = Buffer()
    scanner = LexicalScanner()
    rule = scanner.tokenize()

    token, lexeme = [], []
    for value in b.load_file("hello.vc"):
        t, l, r, c = scanner.analyze(value, rule)
        token += t
        lexeme += l

    print(token)
    print(set(lexeme))
