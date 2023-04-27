def soma_matrizes(m1, m2):
    Soma = []
   # numero de linhas e colunas das matrizes
    nLinhasm1 = len(m1)
    nLinhasm2 = len(m2)
    nColm1 = len(m1[0])
    nColm2 = len(m2[0])
    #se num de linhas da matriz 1 for igual num linhas matriz 2
    # num colunas matriz 1 for igual num colunas matriz 2
    if (nLinhasm1 == nLinhasm2) and (nColm1 == nColm2):
        # i percorre a quantidade de linhas da matriz 1
        for i in range(nLinhasm1):
            # cira uma lista com o mesmo numero de colunas
            linha = [0]*nColm1
            # adiciona os valores das linhas para a matriz soma, linha por linha
            Soma.append(linha)
            for j in range(nColm1):
                Soma[i][j] = m1[i][j] + m2[i][j]
    
        return Soma
    else:
        return bool(False)
