sumaEnteros = 0
numero = int(input("Ingrese un numero entero: "))
if numero > 0:
    sumaEnteros = int(numero * (numero + 1) / 2)
    print(f"La suma de los enteros del 1 al {numero} es: {sumaEnteros}")
else:
    print("Ingrese otro numero")