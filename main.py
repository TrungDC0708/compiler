import sys
from buffer import Buffer
from scanner import LexicalScanner

if __name__ == '__main__':
    # args = sys.argv
    # if len(args) < 1:
    #     raise RuntimeError('expected 1 file path argument')

    scanner = LexicalScanner()
    with open('hello.vc') as f:
        lines = f.read()
    list=[]
    for i in lines:
        list.append(i)
    print(list)
    token = scanner.tokenize(list)
    # token, lexeme = [], []
    # for value in b.load_file(args[1]):
    #     t, l, r, c = scanner.analyze(value, rule)
    #     token += t
    #     lexeme += l
    #
    #
    # print(token)
    # f = open('output.vctok', 'w')
    # for l in set(lexeme):
    #     f.write(l+"\n")
    # f.close()
