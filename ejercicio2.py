stock_dispo = 120
capacidad_max = 120
prestamos_activos = 0

print("¡Bienvenido al sistema de gestión de préstamos de la Biblioteca Central!")

while True:
    print("\n=== MENÚ PRINCIPAL ===")
    print("1. Libros disponibles")
    print("2. Realizar préstamo")
    print("3. Devolver préstamo")
    print("4. Historial de préstamos")
    print("5. Salir")
    
    opcion = input("Seleccione una opción: ").strip()
    
    if opcion == "1":
        print(f"\n[INFO] Cantidad actual de libros libres: {stock_dispo}")
        
    elif opcion == "2":
        print(f"\n--- REALIZAR PRÉSTAMO (Disponibles: {stock_dispo}) ---")
        if stock_dispo == 0:
            print("No hay libros disponibles en este momento para realizar préstamos.")
            continue
            
        while True:
            try:
                cantidad = int(input("Ingrese la cantidad de libros a prestar: "))
                if cantidad <= 0:
                    print("La cantidad a prestar debe ser mayor a 0. Intente nuevamente.")
                elif cantidad > stock_dispo:
                    print(f"No hay suficientes libros. El stock disponible actual es de {stock_dispo}.")
                else:
                    stock_dispo -= cantidad
                    prestamos_activos += cantidad
                    print(f"¡Préstamo exitoso! Se han prestado {cantidad} libro(s).")
                    break
            except ValueError:
                print("Por favor, ingrese un número entero válido.")
                
    elif opcion == "3":
        print(f"\n--- DEVOLVER PRÉSTAMO (Espacio libre en biblioteca: {capacidad_max - stock_dispo}) ---")
        if stock_dispo >= capacidad_max:
            print("Todos los libros ya están en la biblioteca. No se pueden recibir más devoluciones.")
            continue
            
        while True:
            try:
                cantidad = int(input("Ingrese la cantidad de libros a devolver: "))
                if cantidad <= 0:
                    print("La cantidad a devolver debe ser mayor a 0. Intente nuevamente.")
                elif stock_dispo + cantidad > capacidad_max:
                    limite_permitido = capacidad_max - stock_dispo
                    print(f"Error de devolución. No puede superar la capacidad máxima de {capacidad_max} libros.")
                    print(f"Como máximo solo puede devolver {limite_permitido} libro(s) en este momento.")
                else:
                    stock_dispo += cantidad
                    prestamos_activos = max(0, prestamos_activos - cantidad)
                    print(f"¡Devolución exitosa! Se han reintegrado {cantidad} libro(s).")
                    break
            except ValueError:
                print("Por favor, ingrese un número entero válido.")
                
    elif opcion == "4":
        print(f"\n=== HISTORIAL DE PRÉSTAMOS ===")
        print(f"Cantidad total de préstamos activos durante la sesión: {prestamos_activos}")
        
    elif opcion == "5":
        print("\n===========================================================")
        print("\nGracias por utilizar nuestro software, hasta la próxima.")
        print("\n===========================================================")
        break
        
    else:
        print("\n[!] Opción inválida. Por favor, elija un número del 1 al 5.")
