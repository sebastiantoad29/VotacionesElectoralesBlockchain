import hashlib
import time

class Bloque:
    def __init__(self, index, datos, hash_anterior):
        self.index = index
        self.timestamp = time.time()
        self.datos = datos  # Información del voto
        self.hash_anterior = hash_anterior
        self.hash = self.calcular_hash()

    def calcular_hash(self):
        bloque_cadena = str(self.index) + str(self.timestamp) + str(self.datos) + str(self.hash_anterior)
        return hashlib.sha256(bloque_cadena.encode()).hexdigest()

    def __str__(self):
        return f"Bloque {self.index} [Hash: {self.hash}, Anterior: {self.hash_anterior}, Datos: {self.datos}]"
