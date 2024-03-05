import unittest
import MTO

class TestMotorEncriptacion(unittest.TestCase):

    def test_encriptar_desencriptar(self):
        # Caso de prueba para encriptar y luego desencriptar un mensaje
        entrada = "Hola Mundo"
        clave = 1234
        mi_motor = MTO.MotorEncriptacion(clave)

        # Proceso de encriptación y desencriptación
        mensaje_encriptado = mi_motor.encriptar(entrada)
        mensaje_desencriptado = mi_motor.desencriptar(mensaje_encriptado)

        # Comprobar que el mensaje desencriptado sea igual al original
        self.assertEqual(entrada, mensaje_desencriptado)

    def test_message_number_Encriptar(self):
        # Caso de prueba para un mensaje con números
        entrada = "23432"
        clave = 1232
        mi_motor = MTO.MotorEncriptacion(clave)

        # Proceso de desencriptación
        resultado = mi_motor.encriptar(entrada)

        # Esperado
        esperado = "ԂԃԄԃԂ" 

        # Verificar que el resultado de la desencriptación sea igual al mensaje original
        self.assertEqual(esperado, resultado)

    def test_character_message_Encriptar(self):
        # Caso de prueba para un mensaje con caracteres especiales
        entrada = "-:_.'¿"
        clave = 2550
        mi_motor = MTO.MotorEncriptacion(clave)

        # Proceso de desencriptación
        resultado = mi_motor.encriptar(entrada)

        # Esperado
        esperado = "ਣਰ੕ਤਝવ" 

        # Verificar que el resultado de la desencriptación sea igual al mensaje original
        self.assertEqual(esperado, resultado)
    def test_encriptar_mensaje_vacio(self):
        # Caso de prueba para encriptar un mensaje vacío
        entrada = ""
        clave = 5678
        mi_motor = MTO.MotorEncriptacion(clave)

        # Proceso de encriptación debería lanzar una excepción
        with self.assertRaises(MTO.EmptyMessage):
            mi_motor.encriptar(entrada)

    def test_desencriptar_mensaje_vacio(self):
        # Caso de prueba para desencriptar un mensaje vacío
        mensaje_encriptado = ""
        clave = 5678
        mi_motor = MTO.MotorEncriptacion(clave)

        # Proceso de desencriptación debería lanzar una excepción
        with self.assertRaises(ValueError):
            mi_motor.desencriptar(mensaje_encriptado)

    def test_emoji_message(self):
        # Caso de prueba para encriptar y desencriptar un mensaje con emojis
        entrada = "😊😊😊😊"
        clave = 1234
        mi_motor = MTO.MotorEncriptacion(clave)

        # Proceso de encriptación y desencriptación
        mensaje_encriptado = mi_motor.encriptar(entrada)
        mensaje_desencriptado = mi_motor.desencriptar(mensaje_encriptado)

        # Comprobar que el mensaje desencriptado sea igual al original
        self.assertEqual(entrada, mensaje_desencriptado)

    def test_message_sinograms(self):
        # Caso de prueba para verificar sinogramas en un mensaje
        entrada = "汉字"

        # Comprobar si hay sinogramas en el mensaje
        self.assertTrue(MTO.has_sinogram(entrada))

    def test_minimun_character_key(self):
        # Caso de prueba para una clave con menos de 4 caracteres
        entrada = "Hi bae"
        clave = "140"  # Clave con solo 3 caracteres

        # Proceso de creación del motor debería lanzar una excepción
        with self.assertRaises(MTO.MinimunCharacters) as context:
            mi_motor = MTO.MotorEncriptacion(clave)

        # Verificar que la excepción tiene el mensaje esperado
        self.assertEqual(str(context.exception), "La clave debe contener 4 caracteres minimo")

    def test_modified_encrypted_message(self):
        # Caso de prueba para un mensaje encriptado modificado
        mensaje_encriptado = "ԂԃԄԃԂ"
        # Cambia un carácter del mensaje encriptado
        mensaje_encriptado_modificado = list(mensaje_encriptado)
        # Por ejemplo, cambia el primer carácter de "Ԃ" a "ԃ"
        mensaje_encriptado_modificado[0] = "j"
        mensaje_encriptado_modificado = "".join(mensaje_encriptado_modificado)

        # Key y motor de encriptación
        clave = 1232
        mi_motor = MTO.MotorEncriptacion(clave)

        # Proceso de desencriptación debería lanzar una excepción
        with self.assertRaises(ValueError) as context:
            mi_motor.desencriptar(mensaje_encriptado_modificado)

        # Verificar que la excepción tiene el mensaje esperado
        self.assertEqual(str(context.exception), "El mensaje encriptado está corrupto o ha sido modificado.")

    def test_key_with_letters(self):
        # Caso de prueba para una clave con solo letras
        entrada = "Hello World"
        clave = "abcd"

        # Proceso de creación del motor debería lanzar una excepción
        with self.assertRaises(ValueError) as context:
            mi_motor = MTO.MotorEncriptacion(clave)

        # Verificar que la excepción tiene el mensaje esperado
        self.assertEqual(str(context.exception), "La clave no puede contener solo letras.")

    def test_key_with_spaces(self):
        # Caso de prueba para una clave con espacios
        clave_con_espacios = "12 34 56"

        # Proceso de creación del motor con clave que contiene espacios debería lanzar una excepción
        with self.assertRaises(ValueError) as context:
            mi_motor = MTO.MotorEncriptacion(clave_con_espacios)

        # Verificar que la excepción tiene el mensaje esperado
        self.assertEqual(str(context.exception), "La clave no puede contener espacios.")

    def test_key_with_special_characters(self):
        # Caso de prueba para una clave con solo caracteres especiales
        entrada = "Hello World"
        clave = "!@#$"

        # Proceso de creación del motor debería lanzar una excepción
        with self.assertRaises(ValueError) as context:
            mi_motor = MTO.MotorEncriptacion(clave)

        # Verificar que la excepción tiene el mensaje esperado
        self.assertEqual(str(context.exception), "La clave no puede contener solo caracteres especiales.")

    def test_current_key(self):
        # Caso de prueba para una clave actual
        mensaje_encriptado = "ԚՁԾԳӲԟՇՀԶՁ"
        clave = 1234
        mi_motor = MTO.MotorEncriptacion(clave)

        # Proceso de desencriptación
        resultado = mi_motor.desencriptar(mensaje_encriptado)

        # Esperado
        esperado = "Hola Mundo"

        # Verificar que el resultado de la desencriptación sea igual al mensaje original
        self.assertEqual(esperado, resultado)

    def test_message_number(self):
        # Caso de prueba para un mensaje con números
        mensaje_encriptado = "ԂԃԄԃԂ"
        clave = 1232
        mi_motor = MTO.MotorEncriptacion(clave)

        # Proceso de desencriptación
        resultado = mi_motor.desencriptar(mensaje_encriptado)

        # Esperado
        esperado = "23432"

        # Verificar que el resultado de la desencriptación sea igual al mensaje original
        self.assertEqual(esperado, resultado)

    def test_character_message(self):
        # Caso de prueba para un mensaje con caracteres especiales
        mensaje_encriptado = "ਣਰ੕ਤਝવ"
        clave = 2550
        mi_motor = MTO.MotorEncriptacion(clave)

        # Proceso de desencriptación
        resultado = mi_motor.desencriptar(mensaje_encriptado)

        # Esperado
        esperado = "-:_.'¿"

        # Verificar que el resultado de la desencriptación sea igual al mensaje original
        self.assertEqual(esperado, resultado)

    def test_none_message(self):
        # Caso de prueba para un mensaje None
        entrada = None
        clave = 14074
        mi_motor = MTO.MotorEncriptacion(clave)

        # Proceso de encriptación debería lanzar una excepción
        with self.assertRaises(MTO.EmptyMessage):
            mi_motor.encriptar(entrada)

    def test_incorrect_key(self):
        # Caso de prueba para una clave incorrecta
        mensaje_encriptado = "MensajeEncriptado"
        clave_correcta = 1234
        clave_incorrecta = 5678
        mi_motor = MTO.MotorEncriptacion(clave_correcta)

        # Proceso de desencriptación debería lanzar una excepción
        with self.assertRaises(ValueError) as context:
            mi_motor.desencriptar(mensaje_encriptado, clave_incorrecta)

        # Verificar que la excepción tiene el mensaje esperado
        self.assertEqual(str(context.exception), "La clave proporcionada no coincide con la clave utilizada para encriptar el mensaje.")

    def test_unencrypted_message(self):
        # Caso de prueba para un mensaje no encriptado
        mensaje_no_encriptado = "Hola Mundo"
        clave = 1234
        mi_motor = MTO.MotorEncriptacion(clave)

        # Proceso de desencriptación debería lanzar una excepción
        with self.assertRaises(ValueError) as context:
            mi_motor.desencriptar(mensaje_no_encriptado)

        # Verificar que la excepción tiene el mensaje esperado
        self.assertEqual(str(context.exception), "El mensaje encriptado está corrupto o ha sido modificado.")

    def test_corrupt_message(self):
        # Caso de prueba para un mensaje encriptado corrupto
        mensaje_encriptado_corrupto = "MensajeModificado"
        clave = 1234
        mi_motor = MTO.MotorEncriptacion(clave)

        # Proceso de desencriptación debería lanzar una excepción
        with self.assertRaises(ValueError) as context:
            mi_motor.desencriptar(mensaje_encriptado_corrupto)

        # Verificar que la excepción tiene el mensaje esperado
        self.assertEqual(str(context.exception), "El mensaje encriptado está corrupto o ha sido modificado.")

    def test_empty_key(self):
        # Caso de prueba para una clave vacía
        mensaje_encriptado = ""
        clave = 9876
        mi_motor = MTO.MotorEncriptacion(clave)

        # Proceso de desencriptación debería lanzar una excepción
        with self.assertRaises(ValueError) as context:
            mi_motor.desencriptar(mensaje_encriptado)

        # Verificar que la excepción tiene el mensaje esperado
        self.assertEqual(str(context.exception), "El mensaje no ha sido encriptado previamente o está vacío.")


# Este fragmento de código permite ejecutar la prueba individualmente
if __name__ == '__main__':
    unittest.main()
