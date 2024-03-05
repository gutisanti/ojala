# Archivo main.p
import os
from cryptography.hazmat.backends import default_backend
from MTO import MotorEncriptacion, EmptyMessage, MinimunCharacters, IncorrectKey
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from base64 import urlsafe_b64encode

# Definir la clase MotorEncriptacion si no está definida
class MotorEncriptacion:
    def __init__(self, clave):
        self.clave = clave

    def encriptar(self, mensaje):
        # Implementa la lógica para encriptar el mensaje
        pass

    def desencriptar(self, mensaje_encriptado):
        # Implementa la lógica para desencriptar el mensaje
        pass

def obtener_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Por favor, ingrese un número entero válido.")

def generar_clave_secreta(password, salt):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt.encode('utf-8'),
        iterations=100000,
        backend=default_backend()
    )
    return urlsafe_b64encode(kdf.derive(password.encode('utf-8')))

def main():
    # Solicitar al usuario que elija entre encriptar o desencriptar
    opcion = input("¿Desea encriptar (E) o desencriptar (D) un mensaje? ").upper()

    # Validar la opción ingresada
    if opcion not in ["E", "D"]:
        print("Opción no válida. Por favor, ingrese 'E' para encriptar o 'D' para desencriptar.")
        exit()

    # Realizar la operación seleccionada por el usuario
    if opcion == "E":
        mensaje = input("Ingrese la palabra: ")  # Cambiado de "mensaje" a "palabra"
        password = input("Ingrese la contraseña para generar la clave: ")
        salt = os.urandom(16).hex()  # Generar un salt aleatorio
        clave_secreta = generar_clave_secreta(password, salt)
        mi_motor = MotorEncriptacion(int.from_bytes(clave_secreta, 'big'))
        palabra_encriptada = mi_motor.encriptar(mensaje)  # Cambiado de "mensaje" a "palabra"
        print("Palabra encriptada:", palabra_encriptada)

        with open("palabra_encriptada.txt", "w", encoding="utf-8") as archivo:
            archivo.write(f"Palabra encriptada: {palabra_encriptada}\n")
            archivo.write(f"Salt: {salt}\n")

        print("Palabra encriptada y salt guardados en 'palabra_encriptada.txt'.")

    elif opcion == "D":
        password = input("Ingrese la contraseña para generar la clave: ")

        try:
            with open("palabra_encriptada.txt", "r", encoding="utf-8") as archivo:
                lineas = archivo.readlines()
                salt = lineas[1].split(":")[1].strip()
        except FileNotFoundError:
            print("No se encontró el archivo 'palabra_encriptada.txt'.")
            exit()
        except (ValueError, IndexError):
            print("Error al leer el salt almacenado.")
            exit()

        clave_secreta = generar_clave_secreta(password, salt)
        mi_motor = MotorEncriptacion(int.from_bytes(clave_secreta, 'big'))

        palabra_encriptada = lineas[0].split(":")[1].strip()
        try:
            palabra_desencriptada = mi_motor.desencriptar(palabra_encriptada)
            print("Palabra desencriptada:", palabra_desencriptada)
        except (ValueError, IncorrectKey, EmptyMessage, MinimunCharacters) as error:
            print(f"Error al desencriptar: {error}")

if __name__ == "__main__":
    main()
