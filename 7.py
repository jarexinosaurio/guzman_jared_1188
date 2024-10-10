print("")
print("guzman")
print("")
#guzman guzman
#funcion
def longitud_ultima_palabra(texto):

    #Devuelve la longitud de la última palabra.

    palabras = texto.split()
    if palabras:
        return len(palabras[-1])
    return 0

# imprime
print(longitud_ultima_palabra("dinosaurio"))  
