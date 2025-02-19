from auto import Car
from mascotas import Mascota

gato = Mascota("gato", "michi")
gato.correr()
gato.llamar()

perro = Mascota("perro", "pupi")
perro.llamar()

audi = Car("audi", "a4", 2024)
audi.describir_vehiculo()
print(audi.tipo_vehiculo())

vmw = Car("vmw", "suv", 2030, ["flex"])
vmw.describir_vehiculo()
print(f"{vmw.tipo_vehiculo()}")