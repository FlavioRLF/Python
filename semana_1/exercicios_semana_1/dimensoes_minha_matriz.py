def dimensoes(minha_matriz):
    x = 0
    list = minha_matriz[:]
    for i in range(len(minha_matriz)):
        y = len(list[x])
        x += 1
    
    print(str(x)+'X'+str(y))

