''''
Elefantes com recursão
'''
def incomodam(n):
    # base de recursao
    if type(n) != int or n < 1:
        return " "

    # chamada recursiva
    else:
        valor = "incomodam"+" "+incomodam(n-1)

        return valor 

def elefantes(n):
    # base de recursao
    if type(n) != int or n < 1:
        return " "

    # chamada recursiva
    else:
        i = 0
        if n == 1:
            return "Um elefante incomoda muita gente\n"
        else:
            valor = str(n)+" elefantes "+n*"incomodam "+" muito mais\n"
            frase = str(n-1)+" elefantes incomodam muita gente\n"
            valor = valor.replace("  "," ") 
            if frase == str(1)+" elefantes incomodam muita gente\n":
                return elefantes(n-1) + valor
            else:
                return elefantes(n-1) + frase + valor

print(elefantes(3))