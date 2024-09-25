import json
import os

# Rutas de los archivos donde se guardarán los datos
archivoEstudiantes = 'persistencia/estudiantes.json'
archivoGrupos = 'persistencia/grupos.json'
archivoModulos = 'persistencia/modulos.json'

def cargarEstudiantes():
    if not os.path.exists(archivoEstudiantes):
        return []   # Si el archivo no existe, retorna una lista vacía
    with open(archivoEstudiantes, 'r') as file:
        return json.load(file) # Cargar y devolver los datos en un json

def guardarEstudiantes(estudiantes):
    with open(archivoEstudiantes, 'w') as file:
        json.dump(estudiantes, file, indent = 4)

def cargarGrupos():
    if not os.path.exists(archivoGrupos):
        return []  # Retorna una lista vacía si no existe el archivo
    with open(archivoGrupos, 'r') as file:
        return json.load(file)

def cargarModulos():
    if not os.path.exists(archivoModulos):
        return []  # Retorna una lista vacía si no existe el archivo
    with open(archivoModulos, 'r') as file:
        return json.load(file)

def registrarEstudiantes():
    estudiantes = cargarEstudiantes()  # Cargar los estudiantes existentes

    while True:
        try:
            n = int(input("\nCuántos estudiantes desea ingresar?: "))
            print("_" * 55)

            if n < 1:
                print("\nError. Debe ingresar al menos 1.")
                continue
            break
        except ValueError:
            print("\nError. Debe ingresar un número entero.")

    for i in range(n):
        print(f"\n>Estudiante {i + 1}<")  # Muestra el número de estudiante a registrar
        while True:
            codigo = input("Ingrese el código del estudiante: ")
            
            # Validar que el código sea numérico
            if not codigo.isdigit():
                print("\nError. El código debe ser numérico.")
                continue  
            
            # Verificar si el estudiante ya existe
            if any(estudiante['codigo'] == codigo for estudiante in estudiantes):
                print(f"\nError. Ya existe un estudiante con el código '{codigo}'.")
                continue  
            
            break  # Si pasa todas las validaciones, sale del bucle

        # Solicitar el resto de los datos del estudiante
        nombre = input("Ingrese el nombre del estudiante: ")
        sexo = input("Ingrese el sexo del estudiante (M/F/O): ")
        edad = input("Ingrese la edad del estudiante: ")
        print("_")

        # Solicitar grupo
        grupos = cargarGrupos()
        print("\nGrupos disponibles:")
        for grupo in grupos:
            print(f"- {grupo['codigo']}: {grupo['nombre']}")
        
        grupoCodigo = input("Ingrese el código del grupo al que desea asignar al estudiante: ")
        print("_")
        # Validar que el grupo existe
        if not any(grupo['codigo'] == grupoCodigo for grupo in grupos):
            print(f"\nError. No existe un grupo con el código '{grupoCodigo}'.")
            continue
        
        # Solicitar módulos
        modulos = cargarModulos()
        print("\n> De estos modulos disponibles puede elejir de 1 a 3:")
        for modulo in modulos:
            print(f"- {modulo['codigo']}: {modulo['nombre']}")
        
        modulosAsignados = []
        while len(modulosAsignados) < 3:
            moduloCodigo = input("Ingrese el código del módulo (o 'fin' para terminar): ")

            if moduloCodigo.lower() == 'fin':
                print("=" * 55)
                break
            # Validar que el módulo existe
            if not any(modulo['codigo'] == moduloCodigo for modulo in modulos):
                print(f"Error. No existe un módulo con el código '{moduloCodigo}'.")
                continue
            if moduloCodigo in modulosAsignados:
                print(f"Error. Ya ha asignado el módulo '{moduloCodigo}'.")
                continue
            modulosAsignados.append(moduloCodigo)

        estudiante = {
            "codigo": codigo,
            "nombre": nombre,
            "sexo": sexo,
            "edad": edad,
            "grupo": grupoCodigo,
            "modulos": modulosAsignados  
        }

        # Agregar el estudiante al listado
        estudiantes.append(estudiante)
        print(f"Estudiante '{nombre}' registrado exitosamente.")
        print("_" * 55)

    # Guardar los estudiantes al finalizar
    guardarEstudiantes(estudiantes)
    print(f"{n} estudiante/s registrado/s exitosamente.")
    print("=" * 55)
