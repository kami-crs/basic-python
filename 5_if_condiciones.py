# condiciones : statements, conditions
# acciones para llevar acabo o ejecutar condiciones
cars = ["audi", "vmw", "subaru", "toyota"]
for car in cars:
    if car == "vmw":
        print(car.upper())
    else:
        print(car)

promt = "Audi"
if cars[0] == promt.lower():
    print(f"\nEncontramos el {promt}\n") 

# condiciones no iguales: inequality operator
if "harry" != "Harry":
    print("No es igual\n")
else:
    print("Es igual\n") 

# condicion: and: sirve para verificar si los dos o mas valores son iguales al mismo tiempo
name_1 = "ana" 
name_2 = "sabrina"
if name_1 == "Ana" and name_2 == "sabrina":
    print("El nombre es igual\n")
else:
    print("Uno de los nombres no es igual\n")

# numeros
if 10 > 9:
    print("Es mayor\n")
else:
    print("No es mayor\n")


if 10 == 9:
    print("Es igual\n")
else:
    print("No es igual\n")


if 10 >= 10:
    print("Es mayor o igual\n")
else:
    print("No es igual\n")

# or: sirve para verificar si cualciera de los valores se cumplen
num_1 = 2
num_2 = 3
if num_1 == 5 or num_2 == 3:
    print("Uno o ambos de los numeros es igual\n")

# verificar cuando el valor de una lista existe
ingredientes = ["cebolla", "aji", "queso"]
if "comino" in ingredientes:
    print("agregar ingrediente")
else:
    print("no tenemos este ingrediente")

# verificar cuando el valor no existe en la lista
if "comino" not in ingredientes:
    print("este ingrediente no existe")

# expreciones boleanas: boolean
juego_activo = True
puedo_editar = False
if puedo_editar:
    print("El archivo se ha editado")

if juego_activo:
    print("El juego esta activo\n")

# comparar edades
edad = 17
mayor_de_edad = 18
if edad >= mayor_de_edad:
    print("estas en edad de votar")
else:
    print("lo siento, no puede votar")

# cadena if - elif - else
# si tiene menos de 4, gratis
# si esta entre 4 y 18 son 25$
# si es mayor de 18 son 40$
# si es mayor de 65, gratis
edad_de_la_persona = 66

precio = 40
if edad_de_la_persona < 4:
    precio = 0 
elif edad_de_la_persona < 18:
    precio = 25
elif edad_de_la_persona > 65:
    precio = 0
elif edad_de_la_persona > 18:
    precio = 40

print(f"tenes {edad_de_la_persona} debes pagar {precio}\n")

lista_covertura = ["championiones", "aceituna", "queso", "pimienta"]
for covertura in lista_covertura:
    if covertura == "pimienta":
        print(f"lo siento, ya no tenemos {covertura}")
    else: 
        print(f"agregar {covertura}")
print("la pizza esta lista\n".upper())

# buscar en la lista vacia
lista_de_bebidas = ["coca", "gulp", "pessi", "guarana"]
# lista_de_bebidas = []

if lista_de_bebidas:
    for bebida in lista_de_bebidas:
        print(f"agregar {bebida}\n")
else:
    print("favor seleccionar una bebida")

# multiples listas
lista_disponible = ["coca", "pepsi", "guarana"]
lista_pedidos = ["coca", "pepsi", "guarana", "gulp"]
#  el for es un bucle que va repitiendo la ACCION hasta que terminen los itens(pedido)
for pedido in lista_pedidos:
    if pedido in lista_disponible:
        print(f"servir {pedido}")
    else:
        print(f"lo siento, no tenemos {pedido}")