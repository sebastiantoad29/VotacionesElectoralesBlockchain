from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import os

class Persona:
    def __init__(self, id_persona, nombre, clave_electoral, domicilio):
        self.id_persona = id_persona
        self.nombre = nombre
        self._clave_electoral = self.cifrar_clave(clave_electoral)
        self.domicilio = domicilio
        self.key = os.urandom(32)  
        self.iv = os.urandom(16)  

    def __str__(self):
        return f"ID: {self.id_persona}, Nombre: {self.nombre}, Clave Electoral Cifrada: {self._clave_electoral}, Domicilio: {self.domicilio}"


    # Cifrado AES para la clave electoral
    def cifrar_clave(self, clave_electoral):
        
        clave_bytes = clave_electoral.encode('utf-8')

        
        padder = padding.PKCS7(128).padder()
        clave_padded = padder.update(clave_bytes) + padder.finalize()

        
        cifrador = Cipher(algorithms.AES(self.key), modes.CBC(self.iv), backend=default_backend())
        cifrador_encryptor = cifrador.encryptor()

        
        clave_cifrada = cifrador_encryptor.update(clave_padded) + cifrador_encryptor.finalize()
        return clave_cifrada

    
    def descifrar_clave(self):
        cifrador = Cipher(algorithms.AES(self.key), modes.CBC(self.iv), backend=default_backend())
        descifrador = cifrador.decryptor()

        
        clave_padded = descifrador.update(self._clave_electoral) + descifrador.finalize()
        unpadder = padding.PKCS7(128).unpadder()
        clave_bytes = unpadder.update(clave_padded) + unpadder.finalize()

        return clave_bytes.decode('utf-8')