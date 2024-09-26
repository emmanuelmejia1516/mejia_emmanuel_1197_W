print("")
print("Mejia Suarez Emmanuel Alexander: mi práctica desarrolla un algoritmo que permita leer tres valores y almacenarlos en las variables: A, B y C respectivamente.El algoritmo debe imprimir cual es el mayor y cual es el menor.")
print("")
#Función para leer tres valores distintos y determinar el mayor y el menor.
def encontrar_mayor_y_menor():
    A = int(input("Ingrese el valor de A: "))
    B = int(input("Ingrese el valor de B: "))
    C = int(input("Ingrese el valor de C: "))
# Verificación de que los valores introducidos sean distintos.
    if A == B or A == C or B == C:
        print("Los tres valores deben ser distintos.Escribe otros valores porfavor")
        return  # Salir de la función si hay valores iguales.

    # Inicializar variables para almacenar el mayor y el menor.
    mayor = A
    menor = A

    # Comparaciones para encontrar el mayor valor.
    if B > mayor:
        mayor = B
    if C > mayor:
        mayor = C

    # Comparaciones para encontrar el menor valor.
    if B < menor:
        menor = B
    if C < menor:
        menor = C

    # Imprimir los resultados.
    print(f"El valor mayor es: {mayor}")
    print(f"El valor menor es: {menor}")

# Llamada a la función principal
encontrar_mayor_y_menor()
