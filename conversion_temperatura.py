#Solicita una temperatura en grados Celsius. Convierte y muestra su equivalente en grados Fahrenheit.
celsius = float(input("Ingrese la temperatura en grados Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius} grados Celsius equivalen a {fahrenheit} grados Fahrenheit")