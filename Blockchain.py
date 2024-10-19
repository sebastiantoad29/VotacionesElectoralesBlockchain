class Blockchain:
    def __init__(self):
        self.cadena = []
        self.crear_bloque_genesis()

    def crear_bloque_genesis(self):
        bloque_genesis = Bloque(0, "Bloque Génesis", "0")
        self.cadena.append(bloque_genesis)

    def obtener_ultimo_bloque(self):
        return self.cadena[-1]

    def agregar_bloque(self, datos_voto):
        ultimo_bloque = self.obtener_ultimo_bloque()
        nuevo_bloque = Bloque(len(self.cadena), datos_voto, ultimo_bloque.hash)
        if self.validar_bloque(nuevo_bloque, ultimo_bloque):
            self.cadena.append(nuevo_bloque)

    def validar_bloque(self, bloque_nuevo, bloque_anterior):
        if bloque_nuevo.hash_anterior != bloque_anterior.hash:
            return False
        if bloque_nuevo.hash != bloque_nuevo.calcular_hash():
            return False
        return True

    def mostrar_cadena(self):
        for bloque in self.cadena:
            print(bloque)

