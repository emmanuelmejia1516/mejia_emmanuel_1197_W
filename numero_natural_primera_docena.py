print("")
print("Mejia Suarez Emmanuel Alexander:mi programa Solicitar al usuario un número natural y verificar que el número ingresado se encuentre dentro de la primera docena de números naturales,")
print("")
def verificar_numero_natural(numero):
    """
    Verifica si un número natural está en el rango de la primera docena.

    Args:
        numero (int): El número natural a verificar.

    Returns:
        bool: True si el número está entre 1 y 12, False en caso contrario.
    """
    # Verifica si el número está en el rango de 1 a 12
    return 1 <= numero <= 12


# Solicitar al usuario un número natural
numero_natural = int(input("Ingresa un número natural (1-12): "))

# Comprobar si el número está en la primera docena y mostrar el resultado
if verificar_numero_natural(numero_natural):
    print(f"{numero_natural} está en la primera docena de números naturales.")
else:
    print(f"{numero_natural} no está en la primera docena de números naturales.")
