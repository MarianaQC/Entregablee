print("Bienvenidx a la calculadora de compras")
print("Este programa te ayudará a calcular el costo total de tu compra con descuento.")
print("Por favor, ingresa correctamente cada uno de los datos pedido acontinuacion!")
nombre_producto = input("Ingresa el nombre del producto deseado: ")
while True:
    try:
        precio_unitario = float(input("Ingresa el precio unitario del producto (en pesos colombianos): "))
        if precio_unitario > 0:
            break
        else:
            print("El precio debe ser un número positivo. Intenta de nuevo.")
    except ValueError:
        print("Por favor, ingresa un número válido.")
while True:
    try:
        cantidad = int(input("Ingresa la cantidad de productos adquiridos: "))
        if cantidad > 0:
            break
        else:
            print("La cantidad debe ser un número positivo. Intenta de nuevo.")
    except ValueError:
        print("Por favor, ingresa un número válido.")

while True:
    try:
        descuento = float(input("Ingresa el porcentaje de descuento (0-100): "))
        if 0 <= descuento <= 100:
            break
        else:
            print("El descuento debe estar entre 0 y 100. Intenta de nuevo.")
    except ValueError:
        print("Por favor, ingresa un número válido.")

costo_sin_descuento = precio_unitario * cantidad

descuento_en_pesos = (descuento / 100) * costo_sin_descuento

costo_total = costo_sin_descuento - descuento_en_pesos

print("\nResumen de la compra:")
print(f"Producto: {nombre_producto}")
print(f"Costo sin descuento: ${costo_sin_descuento:.2f}")
print(f"Descuento aplicado: ${descuento_en_pesos:.2f}")
print(f"Costo total: ${costo_total:.2f}")
print ("MUCHA GRACIAS POR TU COMPRA :) !")