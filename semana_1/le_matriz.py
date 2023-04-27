def cria_matriz(num_linhas, num_colunas):
    matriz = [] # lista vazia
    for i in range(num_linhas):
        # cria a linha i
        linha = [] # lista vazia 
        for j in range(num_colunas): 
            j = int(input("Digite o elemento [" + str(i) + "][" + str(j) + "]: "))
            linha.append(j)
        # adiciona lista à matriz
        matriz.append(linha)
        

    for i in range(num_linhas):
        #for j in range(num_colunas):    
        print(str(matriz[i]),end="\n")
            
                
    
def le_matriz():
    lin = int(input("Digite o numero de linhas da matriz: "))
    col = int(input("Digite o numero de colunas da matriz: "))

    return cria_matriz(lin, col)

m = le_matriz()
print(m)
