'''
Pontos Clube Bene

2020

Bernardo Fernandes

'''


# Imports   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

import sqlite3

def gerir_pontos(usu):

    # Criar BD  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    connection = sqlite3.connect('dadosbene.db')

    c = connection.cursor()
    
    c.execute('CREATE TABLE IF NOT EXISTS pontos (usuario text, pontos intenger)')

    # Pegar e gerir usuario - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    c.execute('SELECT * FROM pontos WHERE usuario = ?', (usu,))
    row = c.fetchall()

    if not row:
        
        pnts = 10
        c.execute("INSERT INTO pontos (usuario, pontos) VALUES (?, ?) ", \
              (usu, pnts))

    else:
        pnts = row[0][1] + 10
        c.execute('UPDATE pontos SET pontos = ? WHERE usuario = ?', (pnts, usu))
            

    connection.commit()
    print('__ PONTOS COLOCADOS NO BANCO DE DADOS\n')


    return
