print("")
print("guzman")
print("")
#guzman guzman
#funcion matematica
import math

def area_circulo(radio):

    #Calcula el área de un círculo.

    return math.pi * radio ** 2

def volumen_cilindro(radio, altura):

    #Calcula el volumen de un cilindro.

    area = area_circulo(radio)
    return area * altura

print(area_circulo(6))  
print(volumen_cilindro(7, 17))  
