class Car:
    """Un simple intento, representar un vehiculo"""
    def __init__(self, make, model, year, charge=["combustible"]):
        self.make = make
        self.model = model
        self.year = year
        self.kilometraje = 0
        self.carga = charge

    
    def describir_vehiculo(self):
        print(f"{self.make} {self.model} {self.year}")
    
    def tipo_vehiculo(self):
        return self.carga