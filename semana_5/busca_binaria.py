''''
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
                Busca Binária

- Localizar o elemento x em uma lista;
- Considere o elemento m do meio da lista
    • x == m => encontrou!
    • x < m => procure apenas na 1º metade (esquerda)
    • x > m => procure apenas na 2º metade (direita)
- Repita o processo até que x seja encontrado ou 
que a sub-lista em questão seja vazia.
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
            Complexidade da Busca Binária

- Dado uma lista de n elementos;
- No pior caso, teremos que efetuar:
    • Log2(n) comparações
- No exemplo da lista telefônica:
    • Log2(2 milhões) = 20,9
    • Portanto, resposta em menos de 21 milissegundos
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
                    Conlcusão

- Busca Binária é um algoritmo bastante eficiente;
- Ao estudar a eficiência de um algoritmo é interessante:
    • Analisar a complexidade computacional
    • Realizar experimentos medindo o desempenho
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
'''

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

lista = Buscador().lista_aleatoria(100)
#print(lista)
#lista = ['a', 'e', 'i']

antes = time.time()
print(Buscador().busca_binaria(lista, 5))
depois = time.time()

print('Tempo em segundos:', depois - antes)

