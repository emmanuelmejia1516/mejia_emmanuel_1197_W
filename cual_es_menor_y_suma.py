print("")
print("Mejia Suarez Emmanuel Alexander: mi programa lee dos valores que escribes,determinar cual de los dos valores es el menor,tambien los suma y lo escribe en pantalla")
print("")
# Función para leer dos valores, sumarlos y determinar cuál suma es menor
def determinar_suma_menor():
    # Leer dos valores del usuario
    valor1 = float(input("Ingrese el primer valor: "))
    valor2 = float(input("Ingrese el segundo valor: "))
    
    # Sumar los dos valores
    suma = valor1 + valor2
    
    # Comparar los dos valores originales para determinar el menor
    if valor1 < valor2:
        print(f"El valor menor es: {valor1}")
    elif valor2 < valor1:
        print(f"El valor menor es: {valor2}")
    else:
        print("Ambos valores son iguales.")
    
    # Mostrar la suma de los dos valores
    print(f"La suma de {valor1} y {valor2} es: {suma}")

# Llamada a la función
determinar_suma_menor()