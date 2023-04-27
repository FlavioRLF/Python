import random
import time

class Buscador:
    def busca_sequencial(self, lista, x):
        for i in range(len(lista)):
            if lista[i] == x:
                return i
        return -1

    def busca_binaria(self, lista, x):
        primeiro = 0
        ultimo = len(lista) -1

        while primeiro <= ultimo:
            meio = (primeiro + ultimo)//2
            print(meio)
            if lista[meio] == x:
                return meio
                
            else:
                if x < lista[meio]:
                    ultimo = meio - 1
                else:
                    primeiro = meio + 1
        return -1

    def lista_aleatoria(self, n):
        lista_main = [random.randrange(10) for x in range(n)]    
        return lista_main


''''
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
            Teste 
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
'''

#lista = Buscador().lista_aleatoria(100)
#print(lista)

#lista = ['a', 'e', 'i']

#lista = [1, 2, 3, 4, 5]

lista = [1, 2, 3, 4, 5, 6]

antes = time.time()
print(Buscador().busca_binaria(lista, 4))
depois = time.time()

print('Tempo em segundos:', depois - antes)