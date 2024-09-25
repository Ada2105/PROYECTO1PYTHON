import json
import os
from datetime import datetime

# Ruta de archivos donde se guardarán los registros
archivoAsistencia = 'persistencia/asistencia.json'
archivoEstudiantes = 'persistencia/estudiantes.json'
archivoModulos = 'persistencia/modulos.json'

def cargarArchivo(ruta):
    if not os.path.exists(ruta):
        return []
    with open(ruta, 'r') as file:
        return json.load(file)

def guardarArchivo(ruta, datos):
    with open(ruta, 'w') as file:
        json.dump(datos, file, indent=4)

def verificarExistenciaEstudiante(codigoEstudiante, estudiantes):
    return any(estudiante['codigo'] == codigoEstudiante for estudiante in estudiantes)

def verificarExistenciaModulo(codigoModulo, modulos):
    return any(modulo['codigo'] == codigoModulo for modulo in modulos)

# Funciones de asistencia
def registrarAsistencia():
    asistencia = cargarArchivo(archivoAsistencia)
    estudiantes = cargarArchivo(archivoEstudiantes) 
    modulos = cargarArchivo(archivoModulos)

    # Validar existencia de estudiante
    while True:
        codigoEstudiante = input("Ingrese el código del estudiante: ")
        if verificarExistenciaEstudiante(codigoEstudiante, estudiantes):
            break
        else:
            print(f"Error. No existe un estudiante con el código '{codigoEstudiante}'. Intente nuevamente.")
            

    # Validar existencia de módulo
    while True:
        codigoModulo = input("Ingrese el código del módulo: ")
        if verificarExistenciaModulo(codigoModulo, modulos):
            break
        else:
            print(f"Error. No existe un módulo con el código '{codigoModulo}'. Intente nuevamente.")


    fechaHoraEntrada = datetime.now().isoformat()

    # Simular entrada y salida para la asistencia
    input("Presione Enter para registrar la salida del estudiante...")
    fechaHoraSalida = datetime.now().isoformat()

    registro = {
        "codigoEstudiante": codigoEstudiante,
        "codigoModulo": codigoModulo,
        "fechaHoraEntrada": fechaHoraEntrada,
        "fechaHoraSalida": fechaHoraSalida
    }

    asistencia.append(registro)
    guardarArchivo(archivoAsistencia, asistencia)
    print("Asistencia registrada exitosamente.")

def listarAsistencia():
    asistencia = cargarArchivo(archivoAsistencia)
    if not asistencia:
        print("No hay registros de asistencia.")
        return

    print("\n   **Registros de Asistencia**    ")
    for i, registro in enumerate(asistencia, start=1):
        print(f"{i}. Estudiante: {registro['codigoEstudiante']}, Módulo: {registro['codigoModulo']}, "
              f"Entrada: {registro['fechaHoraEntrada']}, Salida: {registro['fechaHoraSalida']}")
        print("=" * 55)

# Funciones de informes
def estudiantesLleganTarde(mes):
    asistencia = cargarArchivo(archivoAsistencia)
    estudiantesTarde = []
    
    for registro in asistencia:
        fechaEntrada = datetime.fromisoformat(registro['fechaHoraEntrada'])
        if fechaEntrada.month == mes and fechaEntrada.hour > 8:  # Se asume una hora de inicio (8:00 AM)
            estudiantesTarde.append(registro['codigoEstudiante'])

    if estudiantesTarde:
        print(f"\nEstudiantes que llegaron tarde en el mes {mes}:")
        for codigoEstudiante in set(estudiantesTarde):
            print(f"- Código del estudiante: {codigoEstudiante}")
    else:
        print(f"\nNo hubo estudiantes que llegaran tarde en el mes {mes}.")

def estudiantesRetiraronAntes(mes):
    asistencia = cargarArchivo(archivoAsistencia)
    estudiantesAntes = []

    for registro in asistencia:
        fechaSalida = datetime.fromisoformat(registro['fechaHoraSalida'])
        if fechaSalida.month == mes and fechaSalida.hour < 10:  # Asumimos hora de finalización (10:00 AM)
            estudiantesAntes.append(registro['codigoEstudiante'])

    if estudiantesAntes:
        print(f"\nEstudiantes que se retiraron antes en el mes {mes}:")
        for codigoEstudiante in set(estudiantesAntes):
            print(f"- Código del estudiante: {codigoEstudiante}")
    else:
        print(f"\nNo hubo estudiantes que se retiraran antes en el mes {mes}.")

def estudiantesNoFaltaron(mes):
    asistencia = cargarArchivo(archivoAsistencia)
    estudiantes = cargarArchivo(archivoEstudiantes)

    estudiantesAsistieron = [registro['codigoEstudiante'] for registro in asistencia if datetime.fromisoformat(registro['fechaHoraEntrada']).month == mes]
    estudiantesNoFaltaron = [estudiante['codigo'] for estudiante in estudiantes if estudiante['codigo'] in estudiantesAsistieron]

    if estudiantesNoFaltaron:
        print(f"\nEstudiantes que no faltaron en el mes {mes}:")
        for codigoEstudiante in set(estudiantesNoFaltaron):
            print(f"- Código del estudiante: {codigoEstudiante}")
    else:
        print(f"\nNo hubo estudiantes que asistieran a todas las clases en el mes {mes}.")

def porcentajeAsistenciaModulo(codigoModulo, mes):
    asistencia = cargarArchivo(archivoAsistencia)
    estudiantes = cargarArchivo(archivoEstudiantes)
    modulos = cargarArchivo(archivoModulos)

    # Verificar si el módulo existe
    if not verificarExistenciaModulo(codigoModulo, modulos):
        print(f"\nError: No existe un módulo con el código '{codigoModulo}'.")
        return

    # Cambiar la forma de obtener los estudiantes matriculados en el módulo
    estudiantesMatriculados = [est['codigo'] for est in estudiantes if codigoModulo in est.get('modulos', [])]
    
    asistenciasModulo = [registro['codigoEstudiante'] for registro in asistencia 
                         if registro['codigoModulo'] == codigoModulo and datetime.fromisoformat(registro['fechaHoraEntrada']).month == mes]

    if estudiantesMatriculados:
        porcentajeAsistencia = (len(asistenciasModulo) / len(estudiantesMatriculados)) * 100
        print(f"\nPorcentaje de asistencia en el módulo {codigoModulo} para el mes {mes}: {porcentajeAsistencia:.2f}%")
        print("=" * 55)
    else:
        print(f"\nNo hay estudiantes matriculados en el módulo {codigoModulo} para el mes {mes}.")
