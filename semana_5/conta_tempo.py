''''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
Módulo time
-Função time()
-Devolve o tempo decorrido (em segundos) desde 1/1/1970 (no Unix)
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
import time

antes = time.time()
algoritmo_a_ser_cronometrado()
depois = time.time()
print("A execução demorou ", depois - antes, "segundos")
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
'''
import Selecao_Direta
import random
import time

class ContaTempos:
    
    def lista_aleatoria(self, n):
        lista_main = [random.randrange(1000) for x in range(n)]    
        return lista_main

    def lista_quase_ordenada(self, n):
        lista = [x for x in range(n)]
        lista[n//10] = -500
        return lista

    def compara(self, n):

        # defini listas
        lista1 = self.lista_aleatoria(n)
        lista2 = lista1[:]
        lista3 = lista1[:]
        lista4 = lista1[:]

        lista5 = self.lista_quase_ordenada(n)


        o = Selecao_Direta.Ordenador()

        ''''
        TESTE DE TEMPO DOS MÉTODOS - LISTAS ALEATORIAS
        '''
        
        print('\nTESTE DE TEMPO DOS MÉTODOS - LISTAS ALEATORIAS\n')

        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

        # bolha com lista aleatoria
        antes = time.time()
        o.bolha(lista1)
        depois = time.time()
        print('Bolha demorou ', depois - antes)

        # bolha_curta com lista totalmente aleatoria 
        antes = time.time()
        o.bolha_curta(lista4)
        depois = time.time()
        print('Bolha curta demorou ', depois - antes)

        # selecao_direta com lista aleatoria
        antes = time.time()
        o.selecao_direta(lista2)
        depois = time.time()
        print('Seleção direta demorou ', depois - antes)

        # sort com lista aleatoria
        antes = time.time()
        o.sort(lista3)
        depois = time.time()
        print('Sort demorou ', depois - antes)
        
        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")

        ''''
        TESTE DE TEMPO DOS MÉTODOS - LISTAS QUASE ORDENADAS
        '''

        print('TESTE DE TEMPO DOS MÉTODOS - LISTAS QUASE ORDENADAS\n')

        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
        # bolha com lista quase ordenada
        antes = time.time()
        o.bolha(lista5)
        depois = time.time()
        print('Bolha demorou ', depois - antes)

        # bolha_curta com lista quase ordenada 
        antes = time.time()
        o.bolha_curta(lista5)
        depois = time.time()
        print('Bolha curta demorou ', depois - antes)

        # selecao_direta com lista quase ordenada
        antes = time.time()
        o.selecao_direta(lista5)
        depois = time.time()
        print('Seleção direta demorou ', depois - antes)

        # sort com lista quase ordenada
        antes = time.time()
        o.sort(lista5)
        depois = time.time()
        print('Sort demorou ', depois - antes)

        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")


''''
Sorting Algorithms Simulation

    nicolasandre.com.br/sorting/
'''

c = ContaTempos()
c.compara(5000)
