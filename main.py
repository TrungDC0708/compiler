import sys
from file import load_code_file, write_to_file
from scanner import LexicalScanner
from rules import Rule

if __name__ == '__main__':
    args = sys.argv
    if len(args) < 1:
        raise RuntimeError('expected 1 file path argument')

    rule = Rule('rules.csv')
    rule.load_rule()
    scanner = LexicalScanner(rule)
    list = load_code_file(args[1])
    token = scanner.tokenize(list)
    write_to_file(token)

