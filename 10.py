print("")
print("guzman")
print("")
#guzman guzman
def es_vocal(caracter):
    #Devuelve True si el carácter es una vocal, False en caso contrario."
    vocales = 'aeiouAEIOU'
    return caracter in vocales

# imprime
caracter_input = input("Introduce un carácter: ")

if len(caracter_input) == 1:
    resultado = es_vocal(caracter_input)
    print(f"¿El carácter '{caracter_input}' es una vocal? {resultado}")
else:
    print("Por favor, introduce solo un carácter.")
