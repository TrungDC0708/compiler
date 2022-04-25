import re
from rules import *


def setType(c):
    a = ord(c)
    if 97 <= a < 101 or 101 < a <= 122 or 65 <= a < 69 or 69 < a <= 90:
        return "character"
    elif 48 <= a <= 57:
        return "number"
    elif c == "<":
        return "<"
    elif c == ">":
        return ">"
    elif c == "!":
        return "!"
    elif c == "&":
        return "&"
    elif c == "+" or c == "-":
        return "-+"
    elif c == "*":
        return "*"
    elif c == ".":
        return "."
    elif c == "=":
        return "="
    elif c == "e" or c == "E":
        return "eE"
    elif c == "|":
        return "|"
    else:
        return "other"


class LexicalScanner:

    def tokenize(self, words):
        currentState = 0
        print(words)
        type_list = []
        token_list = []
        token = ""
        for item in words:
            type = setType(item)
            type_list.append([type, item])
            nextState = (char_rules[startingState.index(str(currentState)) + 3][wType.index(type)])
            if nextState!= '':
                currentState = nextState
                token += item
            else:
                if currentState in endingState:
                    token_list.append(token)
                token = ""
                currentState = 0
        print(type_list)
        print(token_list)
        return token_list

    def analyze(self, code, token_list):
        line_start = 0
        token, lexeme, row, column, = [], [], [], []
        for i in re.finditer(token_list, code):
            ttype = i.lastgroup
            tlexeme = i.group(ttype)

            if ttype == 'NEWLINE':  # new line
                line_start = i.end()
                self.line_number += 1
            elif ttype == 'GAP':  # space or tabs
                continue
            elif ttype == 'OTHER':  # unexpected character
                raise RuntimeError('unexpect %r on line %d' %
                                   (tlexeme, self.line_number))
            else:
                col = i.start() - line_start
                column.append(col)
                row.append(self.line_number)
                token.append(ttype)
                lexeme.append(tlexeme)

                print(
                    "token = {0}, lexeme = {1}, row = {2}, column = {3}".format(ttype, tlexeme, self.line_number, col))

        return token, lexeme, row, column
