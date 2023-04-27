'''
Recursão
• Muitos problemas contém, dentro de si,
problemas menores:
    - Que são similares ao problema maior; 

• Esses problemas tem uma estrutura recursiva;
• Podemos aplicar um algoritmo recursivo para resolvê-los;

'''

def fatorial(n):
    if n<1:                     # base da recursao
        return 1

    else:
        return n*fatorial(n-1)  # chamada recursiva


print("Teste - 1: ",fatorial(0),"\n")
print("Teste - 2: ",fatorial(1),"\n")
print("Teste - 3: ",fatorial(2),"\n")
print("Teste - 4: ",fatorial(3),"\n")
print("Teste - 5: ",fatorial(4),"\n")
print("Teste - 6: ",fatorial(5),"\n")