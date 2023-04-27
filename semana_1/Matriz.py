def cria_matriz(num_linhas, num_colunas, valor):
    matriz = [] # lista vazia
    for i in range(num_linhas):
        # cria a linha i
        linha = []  # lista vazia 
        for j in range(num_colunas): 
            linha.append(valor)

        # adiciona lista à matriz
        matriz.append(linha)

    return matriz

