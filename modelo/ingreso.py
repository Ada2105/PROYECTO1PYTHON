import hashlib # Importa el módulo 'hashlib' para usar algoritmos de encriptación como SHA-256.
import json
import os

# Ruta del archivo donde se guardará la contraseña encriptada
archivoContrasena = 'persistencia/contraseña.json'  # Define la ruta del archivo donde se almacenará la contraseña encriptada.

def encriptarContraseña(contrasena):
    return hashlib.sha256(contrasena.encode()).hexdigest() # Convierte la contraseña en un hash utilizando SHA-256.

def cargarContraseña():
    if not os.path.exists(archivoContrasena): # Verifica si el archivo de la contraseña existe.
        # Si el archivo no existe, se crea con la contraseña por defecto
        guardarContraseña("SISGESA")
    with open(archivoContrasena, 'r') as file:  # Abre el archivo en modo lectura.
        data = json.load(file)
    return data['contrasena']

def guardarContraseña(contrasena):
    contrasenaEncriptada = encriptarContraseña(contrasena) # Encripta la contraseña proporcionada.
    with open(archivoContrasena, 'w') as file:  # Abre el archivo en modo escritura.
        json.dump({'contrasena': contrasenaEncriptada}, file)  # Almacena la contraseña encriptada en un json.


def verificarContraseña(contrasenaIngresada):
    contrasenaGuardada = cargarContraseña()  # Carga la contraseña encriptada almacenada en el archivo.
     # Compara la versión encriptada de la contraseña ingresada con la contraseña encriptada guardada.
    return encriptarContraseña(contrasenaIngresada) == contrasenaGuardada

def cambiarContraseña(nuevaContrasena):
    guardarContraseña(nuevaContrasena) # Encripta y guarda la nueva contraseña.
