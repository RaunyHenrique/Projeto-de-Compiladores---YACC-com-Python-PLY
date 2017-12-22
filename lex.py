import ply.lex as lex

#terminais
tokens = [
    'ID', 'CTE', 'OPADI', 'OPSUB', 'OPMULT', 'OPDIV',
    'PVIRG', 'DPONTOS', 'VIRG', 'ATRIB', 'APAR', 'FPAR',
    'MAIORIG', 'PONTO', 'MENORIG', 'MAIORQ', 'MENORQ', 'EQ',
    'NE', 'ASPASIMP'
]

#não terminais
palavras_reser = {
    'select': 'SELECT',
    'update': 'UPDATE',
    'delete': 'DELETE',
    'from': 'FROM',
    'where': 'WHERE',
    'and': 'AND',
    'or': 'OR',
    'like': 'LIKE'
}

tokens += list(palavras_reser.values())#add palavras reservadas a lista de tokens

def t_ID(t):
    r'[a-zA-Z][a-zA-Z0-9]*'
    t.type = palavras_reser.get(t.value, 'ID')
    return t

#expressões regulares
t_ASPASIMP = r'\''
t_PONTO = r'\.'
t_MAIORIG = r'\>\='
t_MENORIG = r'\<\='
t_MAIORQ = r'\>'
t_MENORQ = r'\<'
t_EQ = r'\=\='
t_NE = r'\!\='
t_APAR = r'\('
t_FPAR = r'\)'
t_ATRIB = r'\='
t_VIRG = r'\,'
t_DPONTOS = r'\:'
t_PVIRG = r'\;'
t_CTE = r'\d+'
t_OPADI = r'\+'
t_OPSUB = r'\-'
t_OPMULT = r'\*'
t_OPDIV = r'\/'


#ignora espaços em branco
t_ignore = " \t"

#linhas
def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

#erros lexicos
def t_error(t):
    print("Erro lexico encontrado! Caracter invalido => '%s'" % t.value[0])
    t.lexer.skip(1)


#inicilizando lex
lexer = lex.lex()