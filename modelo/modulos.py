import json # Importa el módulo 'json' para trabajar con archivos en formato JSON.
import os  # Importa el módulo 'os' para verificar la existencia de archivos en el sistema.

# Ruta del archivo donde se guardarán los módulos
archivoModulos = 'persistencia/modulos.json' # Define la ruta donde se almacenarán los módulos en formato JSON.

def cargarModulos():
    if not os.path.exists(archivoModulos):
        return []  # Retorna una lista vacía si no existe el archivo
    with open(archivoModulos, 'r') as file:
        return json.load(file)

def guardarModulos(modulos):
    with open(archivoModulos, 'w') as file: # Abre el archivo en modo escritura.
        json.dump(modulos, file, indent = 4) # Guarda los módulos en el json con una indentación de 4 espacios.

def registrarModulo():
    modulos = cargarModulos()
    
    while True:
        try:
            cantidad = int(input("\nCuántos módulos desea ingresar?: "))
            print("_" * 55)

            if cantidad < 1:
                print("\nError. Debe ingresar al menos 1.")
                continue # Si no, vuelve a pedir la cantidad.
            break # Si el valor es válido, sale del bucle.
        except ValueError:  # Captura el error si el usuario no ingresa un número entero.
            print("\nError. Debe ingresar un número entero.")

    for i in range(cantidad):
        print(f"\n>Módulo {i+1}<")  # Mostrar número de módulo

        while True:
            codigo = input("Ingrese el código del módulo: ")
            
            # Validar que el código sea numérico
            if not codigo.isdigit(): # Verifica que el código ingresado sea un número.
                print("\nError. El código debe ser numérico.")
                continue  

            # Verificar si el código del módulo ya existe en la lista.
            if any(modulo['codigo'] == codigo for modulo in modulos): # Comprueba si ya existe un módulo con el mismo código.
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
            break # Si la duración es válida, sale del bucle.

        modulo = { # Crea un diccionario que representa al módulo.
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








