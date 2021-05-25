# Trabalho Prático
# tokenizer para a linguagem
#
#
#       in: (3-1)*5+8/3
#       out: PA NUM SUB NUM PF MUL NUM ADD NUM DIV NUM
#------------------------------------------------------------

import ply.lex as lex # importar só a parte léxica do ply
import sys

# Token declarations
tokens = [
    'START', 'END',
    'INT', 'NUM',
    'ID',
    'ATRIB',
    'ADD','SUB','MUL','DIV','MOD',
    'EQ','DIFF','GRT','GEQ','LWR','LEQ',
    'AND','OR','NOT',
    'READ','WRITE',
    'IF','THEN','ELSE',
    'FOR','DO'
]

literals = ['(',')','{','}']

# Token regex

# Tokens with some action code
def t_NUM(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_INT(t):
    r'int'
    return t

def t_ADD(t):
    r'add'
    return t

def t_SUB(t):
    r'sub'
    return t

def t_DIV(t):
    r'div'
    return t

def t_MUL(t):
    r'mul'
    return t

def t_MOD(t):
    r'mod'
    return t

def t_EQ(t):
    r'eq'
    return t

def t_DIFF(t):
    r'diff'
    return t

def t_GRT(t):
    r'grt'
    return t

def t_GEQ(t):
    r'geq'
    return t

def t_LWR(t):
    r'lwr'
    return t

def t_LEQ(t):
    r'leq'
    return t

def t_AND(t):
    r'and'
    return t

def t_OR(t):
    r'or'
    return t

def t_NOT(t):
    r'not'
    return t

def t_READ(t):
    r'read'
    return t

def t_WRITE(t):
    r'write'
    return t

def t_IF(t):
    r'if'
    return t

def t_THEN(t):
    r'then'
    return t

def t_ELSE(t):
    r'else'
    return t

def t_FOR(t):
    r'for'
    return t

def t_DO(t):
    r'do'
    return t

def t_ATRIB(t):
    r'atrib'
    return t

def t_START(t):
    r'start|START'
    return t

def t_END(t):
    r'end|END'
    return t

def t_ID(t):
    r'\_?[a-zA-Z]+\d*'
    return t

# Tracking line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Characters to be ignored
t_ignore = " \t"

# Errors
def t_error(t):
    print(f"Caráter errado {t.value[0]}")
    t.lexer.skip(1)

# build the lexer
lexer = lex.lex()

# reading input
for linha in sys.stdin:
    lexer.input(linha)
    for tok in lexer:
        print(tok)