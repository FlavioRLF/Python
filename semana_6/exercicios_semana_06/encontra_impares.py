''''
Encontra ímpares com recursão
'''
def encontra_impares(lista):
    lista_impar = []
    if len(lista) != 0:
        valor = lista.pop(0)
        if not valor % 2 == 0:
            lista_impar.append(valor)
        lista_impar = lista_impar + encontra_impares(lista)
    return lista_impar