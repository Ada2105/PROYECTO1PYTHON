from interfaz import menu # Importa el módulo 'menu' desde 'interfaz'
from modelo import ingreso # Importa el módulo 'ingreso' desde 'modelo', el cual gestiona la verificación de contraseñas

def iniciarSesion(): #Solicita usuario y contrasena
    usuario = input(">>> Ingrese su nombre de usuario <<<: ") #Ese json aun no esta creado
    contrasenaIntentada = input(">>> Ingrese la contraseña <<<: ") 
    
    if not ingreso.verificarContraseña(contrasenaIntentada): # Llama a la función verificarContraseña del módulo 'ingreso' para validar la contraseña.
        print("Contraseña incorrecta. Saliendo.")
        return False # Retorna False indicando que la autenticación falló.
    
    return True # Si la contraseña es correcta, retorna True para proceder con la ejecución.

def main(): # Función principal del programa.
    if iniciarSesion():  # Si la función iniciarSesion devuelve True (autenticación exitosa).
        menu.gestionarOpciones() # Llama a la función 'gestionarOpciones' desde el módulo 'menu', que permite interactuar con las opciones del menú.
    else:
        return  # Si la autenticación falla, la función 'main' simplemente retorna sin hacer nada más.

if __name__ == "__main__": # Comprueba si el script se está ejecutando 
    main()  # Llama a la función 'main' para iniciar el programa.
