import ply.yacc as yacc
import lex

#tokens/palavras reservadas do arquivo lex
tokens = lex.tokens


#regras de produção
def p_main(p):
    '''
    main : select items where condition
    '''
    print('Sintese reconhecida :D')


def p_select(p):
    '''
    select : SELECT
           | UPDATE
           | DELETE
    '''


def p_items(p):
    '''
    items : OPMULT
          | identifiers
    '''

def p_identifiers(p):
    '''
    identifiers : ID
                | ID VIRG identifiers
    '''


def p_where(p):
    '''
    where : FROM ID WHERE
    '''


def p_condition(p):
    '''
    condition : ID ATRIB  ID
              | ID ATRIB ASPASIMP ID ASPASIMP
              | ID MENORQ ID
              | ID MENORQ ASPASIMP ID ASPASIMP
              | ID MAIORQ ID
              | ID MAIORQ ASPASIMP ID ASPASIMP
              | ID MENORIG ID
              | ID MENORIG ASPASIMP ID ASPASIMP
              | ID MAIORIG ID
              | ID MAIORIG ASPASIMP ID ASPASIMP
              | ID EQ ID
              | ID EQ ASPASIMP ID ASPASIMP
              | ID NE ID
              | ID NE ASPASIMP ID ASPASIMP
              | ID OR ID
              | ID OR ASPASIMP ID ASPASIMP
              | ID AND ID
              | ID AND ASPASIMP ID ASPASIMP
              | ID LIKE ID
              | ID LIKE ASPASIMP ID ASPASIMP
              | ID ATRIB ID AND condition
              | ID ATRIB ASPASIMP ID ASPASIMP AND condition
              | ID ATRIB ID OR condition
              | ID ATRIB ASPASIMP ID ASPASIMP OR condition
              | ID EQ ID AND condition
              | ID EQ ASPASIMP ID ASPASIMP AND condition
              | ID EQ ID OR condition
              | ID EQ ASPASIMP ID ASPASIMP OR condition
              | ID NE ID AND condition
              | ID NE ASPASIMP ID ASPASIMP AND condition
              | ID NE ID OR condition
              | ID NE ASPASIMP ID ASPASIMP OR condition
              | ID MAIORQ ID AND condition
              | ID MAIORQ ASPASIMP ID ASPASIMP AND condition
              | ID MAIORQ ID OR condition
              | ID MAIORQ ASPASIMP ID ASPASIMP OR condition
              | ID MENORQ ID AND condition
              | ID MENORQ ASPASIMP ID ASPASIMP AND condition
              | ID MENORQ ID OR condition
              | ID MENORQ ASPASIMP ID ASPASIMP OR condition
              | ID MAIORIG ID AND condition
              | ID MAIORIG ASPASIMP ID ASPASIMP AND condition
              | ID MAIORIG ID OR condition
              | ID MAIORIG ASPASIMP ID ASPASIMP OR condition
              | ID MENORIG ID AND condition
              | ID MENORIG ASPASIMP ID ASPASIMP AND condition
              | ID MENORIG ID OR condition
              | ID MENORIG ASPASIMP ID ASPASIMP OR condition
    '''


def p_error(t):
    print("Erro sintatico, tente novamente. => '%s'" % t.value)


def main():

    while True:
        try:
            #pegando query inserida pelo usuario
            data = input('Digite uma query: ')
            # iniciando o YACC (parser)
            parser = yacc.yacc()
            parser.parse(data.lower())
        except Exception:
            print("Query inválida! Tente novamente.")


if __name__ == "__main__":
    main()