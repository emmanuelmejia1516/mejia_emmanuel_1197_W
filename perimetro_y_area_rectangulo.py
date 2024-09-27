print("")
print("Mejia Suarez Emmanuel Alexander:mi programa dice el perímetro y el área de un rectángulo ingresando la base b y la altura h.")
print("")
def calcular_perimetro_area_rectangulo(base, altura):
    """
    Calcula el perímetro y el área de un rectángulo dado su base y altura.

    Args:
        base (float): La base del rectángulo.
        altura (float): La altura del rectángulo.

    Returns:
        tuple: Un tuple que contiene el perímetro y el área del rectángulo.
    """
    # Calcular el perímetro como la suma de todos los lados
    perimetro = 2 * (base + altura)
    # Calcular el área como base por altura
    area = base * altura
    return perimetro, area


# Solicitar al usuario la base y altura del rectángulo
base = float(input("Ingresa la base del rectángulo: "))
altura = float(input("Ingresa la altura del rectángulo: "))

# Calcular el perímetro y área del rectángulo
perimetro, area = calcular_perimetro_area_rectangulo(base, altura)

# Mostrar los resultados
print(f"El perímetro del rectángulo es: {perimetro}")
print(f"El área del rectángulo es: {area}")
