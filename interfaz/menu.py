from modelo.asistencia import estudiantesLleganTarde, estudiantesNoFaltaron, estudiantesRetiraronAntes, porcentajeAsistenciaModulo 
# Importa funciones desde el módulo 'asistencia'.
from modelo import asistencia, ingreso, consultas, docentes, grupos,modulos,estudiantes
# Se importan modulos 


def mostrarMenu():  #Muestra el menú principal al usuario.
    
    print("=" * 55)
    print("\n***    MENU DE GESTION DE ASISTENCIA ACADEMICA    ***")
    print("=" * 55)
    print("1. Registro de grupos")
    print("2. Registro de módulos")
    print("3. Registro de estudiantes")
    print("4. Registro de docentes")
    print("5. Registro de asistencia")
    print("6. Consultas de información")
    print("7. Generación de informes")
    print("8. Cambio de contraseña")
    print("9. Salir")
    print("=" * 55)

def mostrarMenuConsultas(): # Muestra el menú específico para realizar consultas.
    print("=" * 55)
    print("\n***   Menú de Consultas   ***")
    print("=" * 55)
    print("1. Consultar Estudiantes por Grupo")
    print("2. Consultar Estudiantes por Módulo")
    print("3. Consultar Docentes por Módulo")
    print("4. Consultar Estudiantes por Docente y Módulo")
    print("5. Salir al Menú Principal")
    print("=" * 55)

def mostrarMenuInformes(): # Muestra el menú de generación de informes.
    print("=" * 55)
    print("\n***   Menú de Informes   ***")
    print("=" * 55)
    print("1. Estudiantes que han llegado tarde")
    print("2. Estudiantes que se retiraron antes")
    print("3. Estudiantes con asistencia perfecta")
    print("4. Porcentaje de asistencia por módulo")
    print("5. Salir al Menú Principal")
    print("=" * 55)

def gestionarOpciones(): # Función que gestiona las opciones del menú.
    while True: # Bucle que mantiene el menú activo hasta decida salir.
        mostrarMenu()
        try:
            opcion = int(input("Seleccione una opción del menu principal: "))
            print("_" * 55)
            if opcion == 1:
                grupos.registrarGrupo()
                print("Registro de grupos seleccionado.")
            elif opcion == 2:
                modulos.registrarModulo()
                print("Registro de módulos seleccionado.")
            elif opcion == 3:
                estudiantes.registrarEstudiantes()
                print("Registro de estudiantes seleccionado.")
            elif opcion == 4:
                docentes.registrarDocente()
                print("Registro de docentes seleccionado.")
            elif opcion == 5:
                asistencia.registrarAsistencia()
                print("Registro de asistencia seleccionado.")
            elif opcion == 6:

                while True:
                    mostrarMenuConsultas()
                    opcionConsulta = input("Seleccione una opción de consulta: ")
                    
                    if opcionConsulta == "1":
                        codigoGrupo = input("Ingrese el código del grupo: ")
                        consultas.consultarEstudiantesGrupo(codigoGrupo)
                    elif opcionConsulta == "2":
                        codigoModulo = input("Ingrese el código del módulo: ")
                        consultas.consultarEstudiantesModulo(codigoModulo)
                    elif opcionConsulta == "3":
                        codigoModulo = input("Ingrese el código del módulo: ")
                        consultas.consultarDocentesModulo(codigoModulo)
                    elif opcionConsulta == "4":
                        cedulaDocente = input("Ingrese la cédula del docente: ")
                        codigoModulo = input("Ingrese el código del módulo: ")
                        consultas.consultarEstudiantesDocenteModulo(cedulaDocente, codigoModulo)
                    elif opcionConsulta == "5":
                        break  # Sale del submenú de consultas.
                    else:
                        print("Opción no válida. Intente nuevamente.") # Mensaje de error si la opción no es válida.

            elif opcion == 7:
                while True:
                    mostrarMenuInformes()
                    opcionInforme = input("Seleccione una opción de informe: ")

                    if opcionInforme == "1":
                        mes = int(input("Ingrese el mes (1-12): "))
                        estudiantesLleganTarde(mes)  # Llamada a la función
                    elif opcionInforme == "2":
                        mes = int(input("Ingrese el mes (1-12): "))
                        estudiantesRetiraronAntes(mes)  # Llamada a la función
                    elif opcionInforme == "3":
                        mes = int(input("Ingrese el mes (1-12): "))
                        estudiantesNoFaltaron(mes)  # Llamada a la función
                    elif opcionInforme == "4":
                        codigoModulo = input("Ingrese el código del módulo: ")
                        mes = int(input("Ingrese el mes (1-12): "))
                        porcentajeAsistenciaModulo(codigoModulo, mes)  # Llamada a la función
                    elif opcionInforme == "5":
                        break  # Sale del submenú de informes.
                    else:
                        print("Opción no válida. Intente nuevamente.")

            elif opcion == 8:
                cambiarContraseña() 
            elif opcion == 9:
                print("Saliendo del sistema. Adiós.")
                break

            else:
                print("Opción no válida. Por favor, elija una opción del 1 al 9.")
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número del 1 al 9.")

def iniciarSesion(): # Proceso de inicio de sesion 

    while True:
        contrasenaIngresada = input("Ingrese la contraseña: ") # Solicita la contraseña al usuario.
        if ingreso.verificarContraseña(contrasenaIngresada):
            print("Inicio de sesión exitoso.")
            gestionarOpciones()
            break
        else:
            print("Contraseña incorrecta. Intente nuevamente.")

def cambiarContraseña(): # Cambiar contrasena
    nuevaContrasena = input("Ingrese la nueva contraseña: ") # Solicita la nueva contraseña.
    ingreso.cambiarContraseña(nuevaContrasena) # Llama a la función para cambiar la contraseña.
    print("Contraseña cambiada exitosamente.")
