'''
Controlador Geral Clube Bene

2020

Bernardo Fernandes

'''

# Imports   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

import valida
import pontos


def roda_busca():
    
    username = str(input('Insira o usuario: '))
    pnt = valida.busca_tweets(('#'+username))

    if pnt == 0:
        pontos.gerir_pontos(username)
        
    return


roda_busca()

print("Operacao finalizada\n")


