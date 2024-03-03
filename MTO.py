# Archivo MTO.py

import string
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

class EmptyMessage(Exception):
    """No se puede encriptar un mensaje vacío"""

class MinimunCharacters(Exception):
    """La clave debe contener 4 caracteres mínimo"""

class IncorrectKey(Exception):
    """La clave está incorrecta"""

class MotorEncriptacion:

    def __init__(self, clave):
        if not clave:
            raise ValueError("La clave no puede estar vacía.")
        if isinstance(clave, int):
            self.clave = clave
        elif isinstance(clave, str):
            if len(clave) < 4:
                raise MinimunCharacters("La clave debe contener al menos 4 caracteres.")
            self.clave = self.obtener_valor_clave(clave)
        else:
            raise ValueError("La clave debe ser un número entero o una cadena de letras.")

    def encriptar(self, mensaje):
        if not mensaje:
            raise EmptyMessage("No se puede encriptar un mensaje vacío.")

        cipher = Cipher(algorithms.AES(self.clave.to_bytes(32, byteorder='big')),
                        modes.ECB(),
                        backend=default_backend())

        encryptor = cipher.encryptor()

        mensaje_encriptado = encryptor.update(mensaje.encode('utf-8')) + encryptor.finalize()
        return mensaje_encriptado

    def desencriptar(self, mensaje_encriptado, clave=None):
        if not mensaje_encriptado:
            raise ValueError("El mensaje no ha sido encriptado previamente o está vacío.")

        if clave is None:
            clave = self.clave  # Utiliza la clave guardada si no se proporciona una clave

        if clave != self.clave:
            raise IncorrectKey("La clave proporcionada no coincide con la clave utilizada para encriptar el mensaje.")

        cipher = Cipher(algorithms.AES(clave.to_bytes(32, byteorder='big')),
                        modes.ECB(),
                        backend=default_backend())

        decryptor = cipher.decryptor()

        try:
            mensaje_desencriptado = decryptor.update(mensaje_encriptado) + decryptor.finalize()
            return mensaje_desencriptado.decode('utf-8')
        except ValueError:
            raise ValueError("El mensaje encriptado está corrupto o ha sido modificado.")

    def obtener_valor_clave(self, clave):
        # Convertir cada letra de la clave a su valor numérico y sumarlos
        return sum(ord(letra) for letra in clave)
