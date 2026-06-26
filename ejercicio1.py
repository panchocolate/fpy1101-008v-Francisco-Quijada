
especialistas_senior = 0
residentes_junior = 0
print("===============================")
print("    REGISTRO DE MÉDICOS  ")
print("Hospital Central Metropolitano")
print("===============================")

while True:
    try:
        num_medicos = int(input("Ingrese la cantidad de médicos que desea registrar: "))
        if num_medicos > 0:
            break
        else:
            print("¡Registro médico inválido! Ingresa un entero positivo para continuar.")
    except ValueError:
        print("¡Registro médico inválido! Ingresa un entero positivo para continuar.")

for i in range(num_medicos):
    print(f"\n--- Registro del Médico N°{i + 1} ---")
    
    while True:
        nombre = input("Ingrese nombre profesional (mínimo 6 caracteres, sin espacios): ").strip()
        if len(nombre) >= 6 and " " not in nombre:
            break
        else:
            print("¡Error de nombre! Debe tener al menos 6 caracteres y no incluir espacios.")
            print("Ejemplos válidos: DrCardio7, NeuroSpec2, SurgMasterX.")

    while True:
        try:
            experiencia = int(input(f"Ingrese los años de experiencia de {nombre}: "))
            if experiencia >0:
                break
            else:
                print("¡Error clínico! Ingresa un número entero positivo para la experiencia.")
        except ValueError:
            print("¡Error clínico! Ingresa un número entero positivo para la experiencia.")

    if experiencia > 5:
        especialistas_senior += 1
        print(f"Resultado: {nombre} ha sido clasificado como Especialista Senior.")
    else:
        residentes_junior += 1
        print(f"Resultado: {nombre} ha sido clasificado como Residente Junior.")

print("\n=================================================================================================")
print(f"¡El hospital cuenta con {especialistas_senior} Especialistas Senior y {residentes_junior} Residentes Junior! ¡Sistema listo para operar!")
print("=================================================================================================")
