''''
Algoritmo de Ordenação Seleção Direta

Seleção Direta
- Menor elemento colocado no inicio;
- Busca pelos menores elementos e os coloca em ordem crescente;
'''

class Ordenador:
    def selecao_direta(self, lista):
        fim = len(lista)

        for i in range(fim - 1):
            # inicialmente, o menor elemento ja visto é o i-ésimo
            posicao_do_min = i

            for j in range(i + 1, fim):
                if lista[j] < lista[posicao_do_min]:
                    posicao_do_min = j

                # Coloca o menor elemento encontrado no inicio da sub-lista
                # Para isso, troca de lugar os elementos nas posições i e posicao_do_min

            lista[i], lista[posicao_do_min] = lista[posicao_do_min], lista[i]

        
    def bolha(self, lista):
        fim  =len(lista)

        for i in range(fim-1, 0, -1):
            for  j in range(i):
                if lista[j] > lista[j+1]:
                    lista[j], lista[j+1] = lista[j+1], lista[j]
                    print(lista)
        return(lista)

    def bolha_curta(self, lista):
        fim  =len(lista)

        for i in range(fim-1, 0, -1):
            trocou = False
            for  j in range(i):
                if lista[j] > lista[j+1]:
                    lista[j], lista[j+1] = lista[j+1], lista[j]
                    print(lista)
                    trocou = True
            if not trocou:
                return

    
    def sort(self, lista):
        return sorted(lista)
        