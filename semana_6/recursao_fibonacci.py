''''
Fibonacci
'''

def fibonacci(n):
    if n<2:                                         # base da recursao
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)      # chamada recursiva

print("Teste - 1: ",fibonacci(0),"\n")
print("Teste - 2: ",fibonacci(1),"\n")
print("Teste - 3: ",fibonacci(2),"\n")
print("Teste - 4: ",fibonacci(3),"\n")
print("Teste - 5: ",fibonacci(4),"\n")
print("Teste - 6: ",fibonacci(5),"\n")
print("Teste - 7: ",fibonacci(6),"\n")
print("Teste - 8: ",fibonacci(7),"\n")