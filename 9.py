print("")
print("guzman")
print("")
#guzman guzman
def suma(numeros):

    #Suma todos los números de una lista.

    total = 0
    for numero in numeros:
        total += numero
    return total

def multiplicar(numeros):

    #Multiplica todos los números de una lista.

    resultado = 1
    for numero in numeros:
        resultado *= numero
    return resultado

# imprime la funcion
print(suma([1, 2, 3, 4]))  
print(multiplicar([1, 2, 3, 4]))  