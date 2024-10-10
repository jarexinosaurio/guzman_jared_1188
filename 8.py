print("")
print("guzman")
print("")
#guzman guzman
#funcion de numeros y saca el mayor
def mayor_de_tres(num1, num2, num3):
    #Devuelve el mayor de tres números.
    return max(num1, num2, num3)

# Ejemplo de uso
numero1 = float(input("Introduce el primer número: "))
numero2 = float(input("Introduce el segundo número: "))
numero3 = float(input("Introduce el tercer número: "))

mayor = mayor_de_tres(numero1, numero2, numero3)
print(f"El mayor de los tres números es: {mayor}")
