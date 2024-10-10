print("")
print("guzman")
print("")
#guzman guzman
#efine la distancia
def distancia_dirigida(punto1, punto2):
    #Calcula la distancia dirigida entre dos puntos.
    x1, y1 = punto1
    x2, y2 = punto2
    distancia = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    vector = (x2 - x1, y2 - y1)
    return distancia, vector

#funcion de los puntos
punto_a = (float(input("Introduce la coordenada x del primer punto: ")),
            float(input("Introduce la coordenada y del primer punto: ")))

punto_b = (float(input("Introduce la coordenada x del segundo punto: ")),
            float(input("Introduce la coordenada y del segundo punto: ")))
#imprime
distancia, vector = distancia_dirigida(punto_a, punto_b)
print(f"La distancia entre los puntos es: {distancia:.2f}")
print(f"El vector que va de {punto_a} a {punto_b} es: {vector}")
