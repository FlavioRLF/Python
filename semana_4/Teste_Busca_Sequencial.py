def busca_sequencial(seq, x):
    #(list, float) -> bool
    for i in range(len(seq)):
        if seq[i] == x:
            return seq[i], i
    return False

numeros = [55,33,0,900,-432,10,77,123,11]

print(busca_sequencial(numeros, 33))