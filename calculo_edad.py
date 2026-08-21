#Solicita el año de nacimiento de una persona. Calcula aproximadamente su edad tomando como referencia el año actual.
import datetime

current_year = datetime.datetime.now().year

birth_year = int(input("Ingrese su año de nacimiento: "))

age = current_year - birth_year

print(f"Tienes aproximadamente {age} años.")