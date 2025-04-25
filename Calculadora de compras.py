productos = []
precios = []
cantidades = []
print ("bienvenidx a la calculadora de compras")
num_productos = int(__builtins__.input("vamos a ver cuanto gastaras en tu compra del dia de hoy!"))
for i in range(num_productos):
    print(f"\n--- Producto {i + 1} ---")
    num_productos = int(input("¿Cuántos productos quieres comprar? "))
    nombre_producto = input("Nombre del producto a comprar: ")
    precio_producto = float(input("Precio del producto: (en COP): "))
    cantidades_producto = int(input("Cantidad de productos: "))
    productos.append(nombre_producto)
    precios.append(precio_producto)
    cantidades.append(cantidades_producto)
    descuento = float(input("\nPorcentaje de descuento (0-100): "))
    print(f"Producto: {nombre_producto}")
    print(f"Precio: {precio_producto}")
    print(f"Cantidad: {cantidades_producto}")
    print(f"Subtotal: {precio_producto * cantidades_producto}")
    subtotal = sum(precio * cantidad for precio, cantidad in zip(precios, cantidades))
monto_descuento = (descuento / 100) * subtotal
total = subtotal - monto_descuento
print("\n--- 🧾 RESUMEN DE COMPRA ---")
for producto, precio, cantidad in zip(productos, precios, cantidades):
    print(f"{producto}: {cantidad} x ${precio:,.2f} COP = ${precio * cantidad:,.2f} COP")

    