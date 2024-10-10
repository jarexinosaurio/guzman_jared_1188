print("")
print("guzman")
print("")
#guzman guzman
#funcion para verificar el email
def es_email_valido(email):
    """Verifica si la dirección de email es válida."""
    return "@" in email
#funcion para capturar el email
def capturar_email():
    """Captura una dirección de email y verifica su validez."""
    email = input("Introduce tu dirección de email: ")
    if es_email_valido(email):
        print("La dirección de email es válida.")
    else:
        print("La dirección de email no es válida.")

# imprime el resultado
capturar_email()
