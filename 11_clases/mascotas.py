class Mascota:
    """Un simple intento de definir cualquier tipo de mascota"""
    def __init__(self, tipo, nombre):
        self.tipo = tipo
        self.nombre = nombre

    def correr(self):
        print(f"El {self.tipo} esta corriendo.")

    def llamar(self):
        print(f"El {self.tipo} se llama {self.nombre}")