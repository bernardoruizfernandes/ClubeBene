'''
BD Lance um desafio Clube Bene

2020

Bernardo Fernandes

'''
import sqlite3

def cria_BD_LD():


    connection = sqlite3.connect('lanceumdesafio.db')

    c = connection.cursor()

    
    c.execute('CREATE TABLE IF NOT EXISTS desafio (usuario text, desafio text, \
            descricao text, votos integer, pontos integer, data text)')


    c.execute("INSERT INTO desafio VALUES ('usua1', 'des1', 'fazer a coisa 1', 0, 25, '12-03-2020 14-40') ")
    c.execute("INSERT INTO desafio VALUES ('usua2', 'des2', 'fazer a coisa 2', 0, 20, '12-03-2020 14-50') ")
    c.execute("INSERT INTO desafio VALUES ('usua3', 'des3', 'fazer a coisa 3', 0, 100, '12-03-2020 14-20') ")
    c.execute("INSERT INTO desafio VALUES ('usua4', 'des4', 'fazer a coisa 4', 0, 55, '12-03-2020 14-10') ")
    c.execute("INSERT INTO desafio VALUES ('usua5', 'des5', 'fazer a coisa 5', 0, 10, '12-03-2020 14-15') ")
    c.execute("INSERT INTO desafio VALUES ('usua6', 'des6', 'fazer a coisa 6', 0, 5, '12-03-2020 14-25') ")


    connection.commit()

    return


cria_BD_LD()
