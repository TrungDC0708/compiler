import re
from rules import char_rules


class LexicalScanner:
    line_number = 1

    def tokenize(self):
        token_list = '|'.join('(?P<%s>%s)' % c for c in char_rules)
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

                print("token = {0}, lexeme = {1}, row = {2}, column = {3}".format(ttype, tlexeme, self.line_number, col))

        return token, lexeme, row, column
