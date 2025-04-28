print("Bienvenidx a la calculadora de compras")
print("Este programa te ayudará a calcular el costo total de tu compra con descuento.")
print("Por favor, ingresa correctamente cada uno de los datos pedido a aguacontinuacion!")
nombre_producto = input("Ingresa el nombre del producto deseado: ")

#Primeramente se muestra un mensaje de bienvenida y  se le explica a el usuario el propósito de la calculadora de compras.
#Luego se le pide al usuario que ingrese el nombre del producto deseado.
while True:
    try:
 #A continuación se le pide al usuario que ingrese el precio unitario del producto, la cantidad de productos adquiridos y el porcentaje de descuento.
        precio_unitario = float(input("Ingresa el precio unitario del producto (en pesos colombianos): "))
        if precio_unitario > 0:
            break
        else:
            print("El precio debe ser un número positivo. Intenta de nuevo.")
    except ValueError:
        print("Por favor, ingresa un número válido.")

while True:
    try:
        cantidad = int(input("Ingresa la cantidad de productos adquiridos: "))    #Se utiliza un bucle while para asegurarse de que el usuario ingrese un número válido
                                                                                  #Y positivo para el precio unitario, la cantidad y el porcentaje de descuento.
                                                                                  #El bucle while se utiliza para validar la entrada del usuario y asegurarse de que los 
                                                                                  #valores ingresados sean válidos.
                                                                                  #Si el usuario ingresa un valor no válido, se le pide que lo intente de nuevo hasta
                                                                                  # que ingrese un valor correcto!
                                                                               
                                                                                
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

    #Se calcula el costo total de la compra y se muestra un resumen con el nombre del producto, el costo sin descuento, el descuento aplicado y el costo total.

costo_sin_descuento = precio_unitario * cantidad

descuento_en_pesos = (descuento / 100) * costo_sin_descuento

costo_total = costo_sin_descuento - descuento_en_pesos

print("\nResumen de la compra:")
print(f"Producto: {nombre_producto}")
print(f"Costo sin descuento: ${costo_sin_descuento:.2f}")
print(f"Descuento aplicado: ${descuento_en_pesos:.2f}")
print(f"Costo total: ${costo_total:.2f}")
print ("MUCHA GRACIAS POR TU COMPRA :) !")

#Finalmente se dan las gracias al usuario por hacer la compra!