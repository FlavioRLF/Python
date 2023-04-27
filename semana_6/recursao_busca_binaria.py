''''
Busca Binária
'''

def busca_binaria(lista, elemento, min = 0, max = None):
    if max == None:
        max = len(lista)-1

    if max< min:
        return False
    
    else:
        meio = min + (max-min)//2

    if lista[meio]>elemento:
        return busca_binaria(lista, elemento, min, meio-1)

    elif lista[meio]<elemento:
        return busca_binaria(lista, elemento, meio+1, max)

    else:
        return meio

a = [10,20,30,40,50,60]

print(busca_binaria(a,50))