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
    def __init__(self, rule):
        self.rule = rule
        self.currentState = 0
        self.type_list = []
        self.token_list = []

    def tokenize(self, char):
        token = ""
        for item in char:
            type = setType(item)
            self.type_list.append([type, item])
            nextState = (self.rule.char_rules[self.rule.startingState.index(str(self.currentState)) + 3][self.rule.wType.index(type)])
            if nextState!= '':
                self.currentState = nextState
                token += item
            else:
                if self.currentState in self.rule.endingState:
                    self.token_list.append(token)
                token = ""
                self.currentState = 0

        return self.token_list

