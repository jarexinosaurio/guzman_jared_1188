print("")
print("guzman")
print("")
#guzman guzman
def calcular_total_factura(cantidad_sin_iva, porcentaje_iva=21):
    # Calcular el total con IVA
    total_con_iva = cantidad_sin_iva * (1 + porcentaje_iva / 100)
    return total_con_iva

# Ejemplo de uso
cantidad = float(input("Introduce la cantidad sin IVA: "))
porcentaje = input("Introduce el porcentaje de IVA (deja en blanco para 21%): ")

# Si el usuario no introduce un porcentaje, se usa 21%
if porcentaje == "":
    total = calcular_total_factura(cantidad)
else:
    total = calcular_total_factura(cantidad, float(porcentaje))

print(f"El total de la factura es: {total:.2f}")
