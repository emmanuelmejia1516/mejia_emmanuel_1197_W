print("")
print("Mejia Suarez Emmanuel Alexander:mi programa saca el factorial del numero que escribiste")
print("")
N = int(input("Por favor escribe un número entero: ")) # el número que has escogido de entrada será el que se calcule como factorial
count = 1 # este es un contador que nos permitirá hacer las multiplicaciones sucesivas
for multipler in range(1,N+1):# el ciclo realiza la serie de multiplicaciones hasta el numero ingresado
  count = count*multipler
print(count)