# Sistema de gestión de notas

# Lista global para almacenar las notas ingresadas
notas_ingresadas = []

# Función para calcular el promedio de las notas
def calcular_promedio():
    print("\n--- INGRESAR NOTAS PARA PROMEDIO ---")
    
    # Validamos que el número de notas a ingresar sea un entero mayor que cero
    while True:
        try:
            cantidad = int(input("¿Cuántas notas vas a ingresar? (mínimo 1): "))
            if cantidad > 0:
                break
            print("Debes ingresar al menos una nota.")
        except ValueError:
            print("Ingresa un número entero válido.")

    # Se ingresan las notas una por una, validando que estén entre 0 y 100
    for i in range(cantidad):
        while True:
            try:
                nota = float(input(f"Ingresa la nota {i+1} (0-100): "))
                if 0 <= nota <= 100:
                    notas_ingresadas.append(nota)  # Se guarda la nota en la lista
                    break
                print("La nota debe estar entre 0 y 100.")
            except ValueError:
                print("Ingresa un número válido.")

    # Cálculo del promedio: suma de notas dividido por la cantidad
    promedio = sum(notas_ingresadas) / len(notas_ingresadas)
    print(f"\n→ Tu promedio es: {promedio:.2f}")

    # Se muestra un mensaje según el nivel del promedio
    if promedio >= 80:
        print("¡Excelente promedio! Sigue así.")
    elif promedio >= 60:
        print("Promedio aprobatorio, pero puedes mejorar.")
    else:
        print("Promedio reprobatorio, necesitas estudiar más.")

# Función para contar cuántas notas son mayores a un valor dado
def contar_mayores():
    # Validamos si ya hay notas guardadas
    if not notas_ingresadas:
        print("Primero debes ingresar notas usando la opción 1.")
        return

    print(" CONTAR NOTAS MAYORES A UN VALOR")
    
    # Se valida que el valor ingresado esté entre 0 y 100
    while True:
        try:
            valor = float(input("Ingresa el valor de comparación (0-100): "))
            if 0 <= valor <= 100:
                break
            print("El valor debe estar entre 0 y 100.")
        except ValueError:
            print("Ingresa un número válido.")

    # Se cuentan cuántas notas son mayores que el valor dado
    contador = sum(1 for nota in notas_ingresadas if nota > valor)
    print(f"Tienes {contador} nota(s) mayores que {valor}.")

# Función para buscar cuántas veces aparece una nota específica
def buscar_nota():
    # Validamos si hay notas previamente ingresadas
    if not notas_ingresadas:
        print("Primero debes ingresar notas usando la opción 1.")
        return

    print(" BUSCAR UNA NOTA ESPECÍFICA")
    
    # Se valida que la nota a buscar esté entre 0 y 100
    while True:
        try:
            buscar = float(input("Ingresa la nota a buscar (0-100): "))
            if 0 <= buscar <= 100:
                break
            print("La nota debe estar entre 0 y 100.")
        except ValueError:
            print("Ingresa un número válido.")

    # Se cuenta cuántas veces aparece la nota específica
    veces = notas_ingresadas.count(buscar)
    if veces > 0:
        print(f"La nota {buscar} aparece {veces} vez/veces.")
    else:
        print(f"La nota {buscar} no aparece en tus notas.")

# Bucle principal del programa: muestra el menú y permite elegir opciones
while True:
    print("MENÚ")
    print("1. Calcular promedio")
    print("2. Contar notas mayores a un valor")
    print("3. Buscar una nota específica")
    print("4. Salir")
    
    # Se solicita al usuario que elija una opción
    opcion = input("Elige una opción (1-4): ")

    # Dependiendo de la opción, se llama a la función correspondiente
    if opcion == "1":
        calcular_promedio()
    elif opcion == "2":
        contar_mayores()
    elif opcion == "3":
        buscar_nota()
    elif opcion == "4":
        print("¡Gracias por usar el sistema de notas! ¡Hasta pronto!")
        break  # Se rompe el ciclo y finaliza el programa
    else:
        # En caso de que el usuario ingrese una opción inválida
        print("Opción no válida. Por favor ingresa un número del 1 al 4.")
# Este programa permite al usuario ingresar notas, calcular promedios, contar notas mayores a un valor y buscar notas específicas.