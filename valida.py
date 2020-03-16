'''
Crawler Clube Bene
'''

# Imports   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

import tweepy
import sqlite3
import palavras


def busca_tweets(username):

    # Info Tweets   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    consumer_key = 'p9euHIjQlpj3AcISPUFm8kX4o'
    consumer_secret = 'v2blKirsrkGfvchAssQbLmjWkt6ZZgzNLjmDCd2N8PDc3Bjson'

    access_key = '1235992186371674113-ix3j86qoytD310UZ4GT0Iauxcs7mUy'
    access_secret = '2joHDgNVtcqtwrV8aBAZOk3d7bP1ZOonb7O94VkrbCedy'

    autenticacao = tweepy.OAuthHandler(consumer_key, consumer_secret)
    autenticacao.set_access_token(access_key, access_secret)

    twitter = tweepy.API(autenticacao)

    # Criar BD  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    connection = sqlite3.connect('dadosbene.db')

    c = connection.cursor()

    
    c.execute('CREATE TABLE IF NOT EXISTS dados (codigo integer, usuario text, \
                post text)')

    # Buscar Tweets - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    tweetsFind = twitter.search(q=username)

    # Validar Tweet - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    n = -1
    clube = 'SoudoBené'
    cod = input('Insira o codigo da missao: ')

    for tweet in tweetsFind:
        if clube in tweet.text:
            if cod in tweet.text:
                print('__ Post encontrado\n')
                usu = tweet.user.name
                pst = tweet.text
                n = palavras.testa_tweet(pst)

    # Atualizando BD  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
    if (n == 0):
        c.execute("INSERT INTO dados (codigo, usuario, post) VALUES (?, ?, ?) ", \
              (cod, usu, pst))
        print('__ DADOS COLOCADOS NO BANCO DE DADOS\n')
        
    elif (n==-1):print('__ ERRO NA ALOCACAO DE DADOS\n')

    else:
        txt_imp = "tweet improprio"
        c.execute("INSERT INTO dados (codigo, usuario, post) VALUES (?, ?, ?) ", \
              (cod, usu, txt_imp))
        print('__ ERRO NA ALOCACAO DE PONTOS: CONTEUDO IMPROPRIO!\n')

    connection.commit()

    return n