print("")
print("guzman")
print("")
#guzman guzman
#definimos el factorial
def factorial(n):
    if n < 0:
        return #El número debe ser un entero positivo.
    elif n == 0 or n == 1:
        return 1
    else:
        resultado = 1
        for i in range(2, n + 1):
            resultado *= i
        return resultado

# lo que imprime en pantalla
numero = int(input("Por favor, introduce un entero positivo: "))
print(f"El factorial de {numero} es: {factorial(numero)}")
