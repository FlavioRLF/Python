def crie_matriz(n_linhas, n_colunas, valor):
	''' (int, int, valor) -> matriz (lista de listas)
	
	Cria e retorna uma matriz com n_linhas linha e n_colunas
	colunas em que cada elemento é igual ao valor dado.
	'''
	
	matriz = [] # lista vazia
	for i in range(n_linhas):
	    # cria a linha i
	    linha = [] # lista vazia
	    for j in range(n_colunas):
	        linha.append(valor)
	
	    # coloque linha na matriz
	    matriz.append(linha)
	
	print(matriz)


crie_matriz(5, 5, 0)