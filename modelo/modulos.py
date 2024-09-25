import json
import os

# Ruta del archivo donde se guardarán los módulos
archivoModulos = 'persistencia/modulos.json'

def cargarModulos():
    if not os.path.exists(archivoModulos):
        return []  # Retorna una lista vacía si no existe el archivo
    with open(archivoModulos, 'r') as file:
        return json.load(file)

def guardarModulos(modulos):
    with open(archivoModulos, 'w') as file:
        json.dump(modulos, file, indent = 4)

def registrarModulo():
    modulos = cargarModulos()
    
    while True:
        try:
            cantidad = int(input("\nCuántos módulos desea ingresar?: "))
            print("_" * 55)

            if cantidad < 1:
                print("\nError. Debe ingresar al menos 1.")
                continue
            break
        except ValueError:
            print("\nError. Debe ingresar un número entero.")

    for i in range(cantidad):
        print(f"\n>Módulo {i+1}<")  # Mostrar número de módulo

        while True:
            codigo = input("Ingrese el código del módulo: ")
            
            # Validar que el código sea numérico
            if not codigo.isdigit():
                print("\nError. El código debe ser numérico.")
                continue  

            # Verificar si el módulo ya existe
            if any(modulo['codigo'] == codigo for modulo in modulos):
                print(f"\nError. Ya existe un módulo con con el codigo '{codigo}'.")
                continue  

            break  # Si el código es válido, continuar

        nombre = input("Ingrese el nombre del módulo: ")

        while True:
            duracion = input("Ingrese la duración en semanas: ")
            print(" ")
            if not duracion.isdigit():
                print("Error. La duración debe ser un número.")
                continue
            break

        modulo = {
            "codigo": codigo,
            "nombre": nombre,
            "duracion": duracion
        }

        modulos.append(modulo)
        print(f"Módulo '{nombre}' registrado exitosamente.")
        print("_" * 55)

    guardarModulos(modulos)
    print(f"{cantidad} módulo/s registrado/s exitosamente.")
    print("_" * 55)








