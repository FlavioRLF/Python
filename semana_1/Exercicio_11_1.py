#-------------------------------------------------------
def leia_matriz():
    matriz = []
    
    lin = int(input('Digite o número de linhas: '))
    col = int(input('Digite o número de colunas: '))

    for i in range(lin):
        linha = []
        for j in range(col):
            
            print("\nLinha "+ str(i) + " = ", linha)
            valor = int(input('Digite o elemento (' +str(i)+ ')(' +str(j)+ '): '))
            linha.append(valor)
            
        matriz.append(linha)
        

    return matriz

#-----------------------------------------------------
# teste
a_mat = leia_matriz()
print(a_mat)