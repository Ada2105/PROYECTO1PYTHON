import json
import os

# Rutas de los archivos
archivoEstudiantes = 'persistencia/estudiantes.json'
archivoDocentes = 'persistencia/docentes.json'
archivoModulos = 'persistencia/modulos.json'
archivoAsistencia = 'persistencia/asistencia.json'

def cargarEstudiantes():  # lista de estudiantes desde el archivo JSON
    if not os.path.exists(archivoEstudiantes):
        return []
    with open(archivoEstudiantes, 'r') as file:
        return json.load(file)

def cargarDocentes():  # lista de docentes desde el archivo JSON
    if not os.path.exists(archivoDocentes):
        return []
    with open(archivoDocentes, 'r') as file:
        return json.load(file)

def cargarModulos():  # lista de módulos desde el archivo JSON
    if not os.path.exists(archivoModulos):
        return []
    with open(archivoModulos, 'r') as file:
        return json.load(file)

def cargarAsistencia():  # lista de asistencia desde el archivo JSON
    if not os.path.exists(archivoAsistencia):
        return []
    with open(archivoAsistencia, 'r') as file:
        return json.load(file)

def consultarEstudiantesGrupo(codigoGrupo):  # estudiantes matriculados en un grupo específico
    estudiantes = cargarEstudiantes()
    estudiantesEnGrupo = [est for est in estudiantes if est['grupo'] == codigoGrupo]  # Cambiado a 'grupo'

    if not estudiantesEnGrupo:
        print(f"No hay estudiantes matriculados en el grupo {codigoGrupo}.")
        return

    print(f"\nEstudiantes en el grupo {codigoGrupo}:")
    for estudiante in estudiantesEnGrupo:
        print(f"- {estudiante['nombre']} (Código: {estudiante['codigo']})")
        print("=" * 55)

def consultarEstudiantesModulo(codigoModulo):  # estudiantes inscritos en un módulo específico
    asistencia = cargarAsistencia()
    estudiantes = cargarEstudiantes()

    estudiantesEnModulo = [
        asis['codigoEstudiante'] for asis in asistencia if asis['codigoModulo'] == codigoModulo
    ]

    if not estudiantesEnModulo:
        print(f"No hay estudiantes inscritos en el módulo {codigoModulo}.")
        return

    print(f"\nEstudiantes en el módulo {codigoModulo}:")
    for codigo in estudiantesEnModulo:
        estudiante = next((est for est in estudiantes if est['codigo'] == codigo), None)
        if estudiante:
            print(f"- {estudiante['nombre']} (Código: {codigo})")

def consultarDocentesModulo(codigoModulo):
    docentes = cargarDocentes()

    docentesEnModulo = [docente for docente in docentes if codigoModulo in docente['modulos']]

    if not docentesEnModulo:
        print(f"No hay docentes que imparten el módulo {codigoModulo}.")
        return

    print(f"\nDocentes que imparten el módulo {codigoModulo}:")
    for docente in docentesEnModulo:
        print(f"- {docente['nombre']} (Cédula: {docente['cedula']})")

def consultarEstudiantesDocenteModulo(cedulaDocente, codigoModulo):
    docentes = cargarDocentes()
    estudiantes = cargarEstudiantes()

    docente = next((docente for docente in docentes if docente['cedula'] == cedulaDocente), None)
    if not docente:
        print(f"No existe un docente con la cédula {cedulaDocente}.")
        return

 
    estudiantesEnModulo = [est for est in estudiantes if codigoModulo in est['modulos']]

    if not estudiantesEnModulo:
        print(f"No hay estudiantes a cargo del docente {cedulaDocente} en el módulo {codigoModulo}.")
        return

    print(f"\nEstudiantes a cargo del docente {cedulaDocente} en el módulo {codigoModulo}:")
    for estudiante in estudiantesEnModulo:
        print(f"- {estudiante['nombre']} (Código: {estudiante['codigo']})")
        print("=" * 55)
