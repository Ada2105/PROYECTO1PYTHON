from interfaz import menu # Importa el módulo 'menu' desde 'interfaz'
from modelo import ingreso # Importa el módulo 'ingreso' desde 'modelo', el cual gestiona la verificación de contraseñas.

def iniciarSesion():#Solicita usuario y contrasena
    usuario = input(">>> Ingrese su nombre de usuario <<<: ")  # Puedes añadir lógica para el nombre de usuario si es necesario
    contrasenaIntentada = input(">>> Ingrese la contraseña <<<: ")
    
    if not ingreso.verificarContraseña(contrasenaIntentada):
        print("Contraseña incorrecta. Saliendo.")
        return False
    
    return True

def main():
    if iniciarSesion():
        menu.gestionarOpciones()
    else:
        return

if __name__ == "__main__":
    main()
