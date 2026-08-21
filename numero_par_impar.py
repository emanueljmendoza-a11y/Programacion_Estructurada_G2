#Solicita un número entero. Determina si el número es par o impar y muestra el resultado.
number = int(input("Ingrese un número entero: "))

if number % 2 == 0:
    print(f"El número {number} es par.")
else:
    print(f"El número {number} es impar.")