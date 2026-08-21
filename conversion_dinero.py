#Solicita una cantidad en dólares y una tasa de cambio. Calcula y muestra cuánto representa esa cantidad en córdobas.
dollars = float(input("Ingrese la cantidad en dólares: "))
exchange_rate = float(input("Ingrese la tasa de cambio (Córdobas por dólar): "))

cordobas = dollars * exchange_rate

print(f"La cantidad en córdobas es: {cordobas:.2f}")