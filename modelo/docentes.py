import json
import os

# Ruta del archivo donde se guardarán los docentes
archivoDocentes = 'persistencia/docentes.json'
archivoGrupos = 'persistencia/grupos.json'
archivoModulos = 'persistencia/modulos.json'

def cargarDocentes():
    if not os.path.exists(archivoDocentes):
        return []  # Retorna una lista vacía si no existe el archivo
    with open(archivoDocentes, 'r') as file:
        return json.load(file)

def guardarDocentes(docentes):
    with open(archivoDocentes, 'w') as file:
        json.dump(docentes, file, indent = 4)

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

def registrarDocente():
    docentes = cargarDocentes()
    
    while True:
        try:
            cantidad = int(input("Cuántos docentes desea ingresar?: "))
            print("=" * 55)
            if cantidad < 1:
                print("Error. Debe ingresar al menos 1.")
                continue
            break
        except ValueError:
            print("Error. Debe ingresar un número entero.")

    for i in range(cantidad):
        print(f"\n> Docente {i + 1} <")  # Mostrar número de docente

        while True:
            cedula = input("Ingrese la cédula del docente: ")
            
            # Verificar si el docente ya existe
            if any(docente['cedula'] == cedula for docente in docentes):
                print(f"Error. Ya existe un docente con la cédula '{cedula}'.")
                continue  
            
            break  # Si la cédula es válida, continuar

        nombre = input("Ingrese el nombre del docente: ")

        # Solicitar grupo
        grupos = cargarGrupos()
        print("\nGrupos disponibles:")
        for grupo in grupos:
            print(f"- {grupo['codigo']}: {grupo['nombre']}")
        
        grupoCodigo = input("Ingrese el código del grupo al que desea asignar al docente: ")
        print("-" * 55)
        
        # Validar que el grupo existe
        if not any(grupo['codigo'] == grupoCodigo for grupo in grupos):
            print(f"\nError. No existe un grupo con el código '{grupoCodigo}'.")
            continue
        
        # Solicitar módulos
        modulos = cargarModulos()
        print("\nMódulos disponibles:")
        for modulo in modulos:
            print(f"- {modulo['codigo']}: {modulo['nombre']}")
        
        modulosAsignados = []
        while len(modulosAsignados) < 3:
            moduloCodigo = input("Ingrese el código del módulo (o 'fin' para terminar): ")
            if moduloCodigo.lower() == 'fin':
                break
            # Validar que el módulo existe
            if not any(modulo['codigo'] == moduloCodigo for modulo in modulos):
                print(f"\nError. No existe un módulo con el código '{moduloCodigo}'.")
                continue
            if moduloCodigo in modulosAsignados:
                print(f"\nError. Ya ha asignado el módulo '{moduloCodigo}'.")
                continue
            modulosAsignados.append(moduloCodigo)

        docente = {
            "cedula": cedula,
            "nombre": nombre,
            "grupo": grupoCodigo,
            "modulos": modulosAsignados  # Guardar módulos asignados
        }

        docentes.append(docente)
        print(f"Docente '{nombre}' registrado exitosamente.")
        print("_" * 55)

    guardarDocentes(docentes)
    print(f"{cantidad} docente/s registrado/s exitosamente.")
    print("=" * 55)
