'''
TODO: Read starting state, ending state, transaction table and all mapping from
automaton file (???) instead of using re package and const character rules
'''

char_rules = [
    ('START', r'#'),
    ('MAIN', r'main'),                      # main
    ('INT', r'int'),                        # int
    ('FLOAT', r'float'),                    # float
    ('IF', r'if'),                          # if
    ('ELSE', r'else'),                      # else
    ('WHILE', r'while'),                    # while
    ('READ', r'read'),                      # read
    ('PRINT', r'printf'),                   # print
    ('IDEN', r'[a-zA-Z]\w*'),               # identifiers
    ('FLOAT_CONST', r'\d(\d)*\.\d(\d)*'),   # float const
    ('EFLOAT', r'[+-]?\d+?[Ee][+-]?\d+'),   # e notation float
    ('INTEGER_CONST', r'[-+]?\d+'),         # int const
    ('NEWLINE', r'\n'),                     # new line
    ('GAP', r'[ \t]+'),                     # space and tabs
    ('INCLUDE', r'include'),                # include
    ('DEFINE', r'define'),                  # define
    ('FORMAT', r'\%[cidsefg]'),             # format specifier, might not need or need more
    ('LINECMT', r'\/\/'),                   # //
    ("LBLOCKCMT", r'\/\*'),                 # /*
    ("RBLOCKCMT", r'\*\/'),                 # */
    ('EQ', r'=='),                          # ==
    ('NE', r'!='),                          # !=
    ('LE', r'<='),                          # <=
    ('GE', r'>='),                          # >=
    ('OR', r'\|\|'),                        # ||
    ('AND', r'&&'),                         # &&
    ('ATTR', r'\='),                        # =
    ('LT', r'<'),                           # <
    ('GT', r'>'),                           # >
    ('PLUS', r'\+'),                        # +
    ('MINUS', r'-'),                        # -
    ('MULT', r'\*'),                        # *
    ('DIV', r'\/'),                         # /
    # ('LBRACKET', r'\('),                    # (
    # ('RBRACKET', r'\)'),                    # )
    # ('LBRACE', r'\{'),                      # {
    # ('RBRACE', r'\}'),                      # }
    # ('COMMA', r','),                        # ,
    # ('PCOMMA', r';'),                       # ;
    # ('OTHER', r'.'),                        # another character
]
