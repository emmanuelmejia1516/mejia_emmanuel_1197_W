print("")
print("Mejia Suarez Emmanuel Alexander: mi práctica se ingresa un número entero para saber si es divisible por 7 y es mayor a 40.")
print("")
def es_divisible_por_7_y_mayor_a_40(numero):
    """
    Verifica si un número entero es divisible por 7 y mayor a 40.

    Args:
        numero (int): El número entero a verificar.

    Returns:
        bool: True si el número es divisible por 7 y mayor a 40, False en caso contrario.
    """
    # Verifica si el número es mayor a 40 y divisible por 7
    return numero > 40 and numero % 7 == 0


# Solicitar al usuario un número entero
numero_entero = int(input("Ingresa un número entero: "))

# Comprobar la condición y mostrar el resultado
if es_divisible_por_7_y_mayor_a_40(numero_entero):
    print(f"{numero_entero} es divisible por 7 y mayor a 40.")
else:
    print(f"{numero_entero} no es divisible por 7 o no es mayor a 40.")