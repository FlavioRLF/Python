'''Escreva uma função que recebe uma lista de Strings contendo nomes 
de pessoas como parâmetro e devolveo nome mais curto. A função deve 
ignorar espaços antes e depois do nome e deve devolver o nome 
"captalizado", i.e, apenas com a 1ª letra maiúscula.'''

def menor_nome(lista_nome):
    lista_nome = lista_nome

    tamanho = []    # cria uma lista que irá informar o tamanho das strings da lista com nomes          
    
    for i in range(len(lista_nome)):    # percorre todos os strings da lista com nomes 
        lista_nome[i] = lista_nome[i].strip().capitalize()  # organiza todos as strings, retirando espaços em excesso e apenas a primeira letra maiúscula
        tamanho.append(len(lista_nome[i]))  # adiciona o valor inteiro do string formatado na lista tamanho

    return lista_nome[(tamanho.index(min(tamanho)))]    # retorna o menor nome formatado da lista com nomes     

