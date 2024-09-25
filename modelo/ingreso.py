import hashlib
import json
import os

# Ruta del archivo donde se guardará la contraseña encriptada
archivoContrasena = 'persistencia/contraseña.json'

def encriptarContraseña(contrasena):
    return hashlib.sha256(contrasena.encode()).hexdigest()

def cargarContraseña():
    if not os.path.exists(archivoContrasena):
        # Si el archivo no existe, se crea con la contraseña por defecto
        guardarContraseña("SISGESA")
    with open(archivoContrasena, 'r') as file:
        data = json.load(file)
    return data['contrasena']

def guardarContraseña(contrasena):
    contrasenaEncriptada = encriptarContraseña(contrasena)
    with open(archivoContrasena, 'w') as file:
        json.dump({'contrasena': contrasenaEncriptada}, file)

def verificarContraseña(contrasenaIngresada):
    contrasenaGuardada = cargarContraseña()
    return encriptarContraseña(contrasenaIngresada) == contrasenaGuardada

def cambiarContraseña(nuevaContrasena):
    guardarContraseña(nuevaContrasena)
