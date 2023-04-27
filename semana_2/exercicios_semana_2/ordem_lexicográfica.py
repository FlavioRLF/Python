'''
Escreva uma função que recebe um array de strings como parâmetro
e devolve o primeiro string na ordem lexicográfica, ignorando-se
letras maiúsculas e minúsculas. 
'''

def maiusculas(frase):
    import re
    frase = frase
    lista = []
    letras = []
    lista.append(re.findall('[A-Z]',frase))
    x = len(lista[0])
    for i in range(x):
        letras.append(lista[0][i])
    y = ""
    y = str(y) 
    for i in letras:
        y += i

    return y

