import sys
from buffer import Buffer
from scanner import LexicalScanner


if __name__ == '__main__':
    args = sys.argv
    if len(args) < 1:
        raise RuntimeError('expected 1 file path argument')

    b = Buffer()
    scanner = LexicalScanner()
    rule = scanner.tokenize()

    token, lexeme = [], []
    for value in b.load_file(args[1]):
        t, l, r, c = scanner.analyze(value, rule)
        token += t
        lexeme += l

    print(token)
    print(set(lexeme))
