# Funções com Strings 
x = "   o Brasil é muito grAnde  "

# -> variável.upper() : retorna a str maiúscula 
print(x.upper())

# -> variável.lower() : retorna a str minúscula 
print(x.lower())

# -> variável.captalize() : retorna a str com apenas a primeira letra em maiúsculo 
print(x.capitalize()) # -> ao retornar a str a primeira letra da frase continua minúsculo por haver espaços antes da primeira letra

# -> "  variável  ".strip() : retorna "variável" sem os espaços no início e no fim
print(x.strip())

# -> "variável".count() : ao indicar o valor a ser contado, a função retorna a quantidade de repetições do valor indicado
print(x.count("a"))

# -> "variável".replace("x","y") : substitui uma parte indicada por outra str
print(x.replace("Brasil","Canadá"))

# -> a função .center(x) retorna a str com x espaços em ambos os lados
# -> em Python é possível concatenar as funções, por exemplo:
y = "  bla Bla blA  "
print(y.strip().capitalize().center(80)) 

# -> "variável".find("x") : retorna a posição do caracter indicado 
print(x.find("m"))

frase = "São Paulo é a maior cidade do Brasil"

print(frase.find("o"))

#=-=-=--==-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-
''''
Comparação de strings 

x = "teoria"
y = "prtática"

x == y : False

x != y : True

z = "teoria"

x == z : True

x is z : True -> str são imutáveis, ela é guardada em apenas um lugar da memória e ambos x e z acessam essa variável;

fução (ord()) indica a ordem lexicográfica
'''

''''
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
Atribuição Aumentada

x = x + 10 --> x += 10

x = x * 2 --> x *=2

x = x ** 10 --> x **=10

=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-
Valores Padrão para Parâmetros

def pagamento_semanal(valor_por_hora, num_horas = 40): --> valor padrao, que pode ser alterado
    return valor_por_hora * num_hora

=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
Asserção de invariantes

def pagamento_semanal(valor_por_hora, num_horas = 40): --> valor padrao, que pode ser alterado
    assert valor_por_hora >= 0 and num_horas > 0 --> valida os valores que devem ser aplicados -- AssertionError
    return valor_por_hora * num_hora
'''