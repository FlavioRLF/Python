'''
Soma Lista com Recursão
'''
def soma_lista(lista):
    # base da recursao
    if len(lista) == 1:
        return lista[0]

    # chamada recursiva
    else:
        return lista[0] + soma_lista(lista[1:])

