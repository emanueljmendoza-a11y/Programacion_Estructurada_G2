#Solicita el precio de un producto y el porcentaje de descuento. Calcula y muestra el descuento aplicado y el precio final.
price = float(input("Ingrese el precio del producto: "))
discount_percentage = float(input("Ingrese el porcentaje de descuento: "))

discount_amount = price * (discount_percentage / 100)
final_price = price - discount_amount

print(f"El descuento aplicado es: {discount_amount:.2f}")
print(f"El precio final es: {final_price:.2f}")