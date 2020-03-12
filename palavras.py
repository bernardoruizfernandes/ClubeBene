'''
Palavras Improprias Clube Bene

2020

Bernardo Fernandes

'''


def testa_tweet(post):

    l_palavras = open('palavras_improprias.txt', 'r')
    l_pal = []
    n = 0
    
    for linha in l_palavras:
        l_pal.append(linha.rstrip())

    l_post = post.split(' ')
    for pal_post in l_post:
        if pal_post in l_pal:
            n+=1
        
    return n




