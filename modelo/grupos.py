import json
import os

# Ruta del archivo donde se guardarán los grupos
archivoGrupos = 'persistencia/grupos.json'

def cargarGrupos():
    if not os.path.exists(archivoGrupos):
        return []  # Retorna una lista vacía si no existe el archivo
    with open(archivoGrupos, 'r') as file:
        return json.load(file)

def guardarGrupos(grupos):
    with open(archivoGrupos, 'w') as file:
        json.dump(grupos, file, indent = 4)

def registrarGrupo():  
    grupos = cargarGrupos()
    
    while True:
        try:
            cantidad = int(input("\nCuántos grupos desea ingresar?: "))
            print("_" * 55)
            
            if cantidad < 1:
                print("\nError. Debe ingresar al menos 1 grupo.")
                continue
            break
        except ValueError:
            print("\nError. Debe ingresar un número entero.")

    for i in range(cantidad):
        print(f"\n>Grupo {i+1}<")  # Mostrar número de grupo

        while True:
            codigo = (input("Ingrese el código del grupo: "))
            
            # Validar que el código sea numérico
            if not codigo.isdigit():
                print("\nError. El código debe ser numérico.")
                continue  

            # Verificar si el grupo ya existe
            if any(grupo['codigo'] == codigo for grupo in grupos):
                print(f"\nError. Ya existe un grupo con el código '{codigo}'.")
                continue  
            
            break  # Si el código es válido, continuar

        nombre = input("Ingrese el nombre del grupo: ")
        sigla = input("Ingrese la sigla del grupo: ")
        print(" ")


        grupo = {
            "codigo": codigo,
            "nombre": nombre,
            "sigla": sigla
        }

        grupos.append(grupo)
        print(f"Grupo '{nombre}' registrado exitosamente.")
        print("_" * 55)

    guardarGrupos(grupos)
    print(f"{cantidad} grupo/s registrado/s exitosamente.")
    print("=" * 55)

