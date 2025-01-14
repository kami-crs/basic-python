# un diccionario simple: dictionary
# un diccionario en python es una coleccion de parejas clave-valor (key-value)
player = { 
    'nombre': "dipper",
    'edad': 8,
    'direccion': "gravity falls",
    'amigos': ["mabel", "soos"] 
    }

print(f"mi nombre es {player['nombre']}, mi edad es {player['edad']}" )

vehiculo = { 
    'ruedas': 4, 
    'color': "rojo", 
    'combustible': "diesel" 
    }

# -25.5093328,-54.6436277,
posicion = {'lat': -25.5093328, 'lng': -54.6436277}
print(posicion['lat'])

# diccionario vacio
dog = {}
dog['edad'] = 4
dog['color'] = "marron"
dog['nombre'] = "milo"
print(dog)

# usar claves para incrementar valores
car = {
    'marca': "audi", 
    'pos_x': 0,
    'pos_y': 0,
    'velocidad': 2
}
movimiento = "y"

if movimiento == "x":
    car['pos_x'] += car['velocidad']
elif movimiento == "y":
    car['pos_y'] += car['velocidad']

print(f"{car['marca'].upper()} va a la velocidad de {car['velocidad']} y de encuentra en la posicion x: {car['pos_x']} y: {car['pos_y']}\n")

# remover los pares de clave-valor
planetas = {
    'platena1': "mercurio",
    'planeta2': "venus",
    'planeta3': "tierra"
}
del planetas["platena1"]
print(planetas)

# diccionario de objetos similares
# get() es una funcion del diccionario que no tira errores si el valor no existe
fav_lag = {
    'mark': "javascript",
    'elon': "rust",
    'jeff': "python"
}
# jeff_fav_lag = fav_lag['jeff']
jeff_fav_lag = fav_lag.get("jefff")
print(f"el lenguaje favorito de jeff es {jeff_fav_lag}\n")

# usar get() para acceder a los valores
barco = {
    'nombre': "marry",
    'color': "blanco",
    'velocidad': "9 nudos"
}
print(barco.get('color',"Esta clave no existe"))

# bucle atraves de todas las parejas(clave-valor) de un diccionario
print("\n")
usuario_0 = {
    'nombre': "sabri",
    'apellido': "bareiro",
    'nik_name': "sabribareir0"
}
# la funcion items() sirve para extraer ambos, clave y valor
for clave, valor in usuario_0.items():
    print(f"la clave {clave} tiene un valor de {valor}")
# la funcion keys() sirve para extraer solamente la clave
for clave in usuario_0.keys():
    print(clave)
# la funcion values sirve para extraer solamente los valores
for valor in usuario_0.values():
    print(valor)

# ejercicio de validacion de permiso de usuario
administradores = ["milo", "willi", "kamila", "sabri"]
usuario_1 = {
    'nombre': "sabri",
    'apellido': "bareiro",
    'nik_name': "sabribareir0",
    'administrador': False
}

# for admin in administradores:
#     if admin == usuario_1['nombre']:
#         usuario_1['administrador'] = True
if usuario_1['nombre'] in administradores:
    usuario_1['administrador'] = True

if usuario_1['administrador']:
    print(f"el usuario {usuario_1['nombre']} tiene permiso")
else:
    print(f"el usuario {usuario_1['nombre']} no tiene permiso")

# sorted : ordena de forma alfabetica pero dando prioridad a las mayusculas
lenguaje_favoritos = {
    'mark': "javascript",
    'elon': "rust",
    'jeff': "python",
    'nigel': "c",
    'usop': "c",
    'sanji': "javascript",
}

print(lenguaje_favoritos)
print(sorted(lenguaje_favoritos.keys()))

for item in sorted(lenguaje_favoritos.keys()):
    print(item)

# loop atraves de todos los valores favoritos 
print("\n")
for valor in lenguaje_favoritos.values():
    print(valor)

# hacer loop sin repeticiones usando set()
print("\n")
for valor in set(lenguaje_favoritos.values()):
    print(valor)

# nesting : muñeca rusa, encajar
alien1 = {
    'color' : "amarillo",
    'puntaje' : 2
}

alien2 = {
    'color' : "verde",
    'puntaje' : 3
}

alien3 = {
    'color' : "gris",
    'puntaje' : 1
}

aliens = [alien1, alien2, alien3]
print("\n")
for alien in aliens:
    print(alien["color"])

# range : vamos a crear una lista de range usando range
lista_de_aliens = []
print("\n")
for index in range(30):
    nuevo_alien = {
        'color' : "verde",
        'puntaje' : index
    }
    lista_de_aliens.append(nuevo_alien)

print(lista_de_aliens)

# ver solo los cinco primeros
print('\n')
for alien in lista_de_aliens[0:5]:
    print(alien)

# len : muestra la cantidad de itens que existe en una lista
print(len(lista_de_aliens))

# nesting : lista dentro de diccionario
print("\n")
pizza = {
    'tipo': "4 quesos",
    'ingredientes': ["mozarela", "roquefort", "robiola", "parmesano"]
}
print(f"Ordenaste una pizza {pizza['tipo']} con los siguientes ingresientes: ")
for ingrediente in pizza['ingredientes']:
    print(ingrediente)

# doble forloop + if
print("\n")
programadores = {
    'sabri': ["python", "js"],
    'katherine': ["python", "c"],
    'dipper': ["python", "c", 'js'],
    'willi': ["python"]
}
for programador, lenguajes in programadores.items():
    if len(lenguajes) > 1:
        print(f"los lesguajes favoritos de {programador} son: ")
        for lenguaje in lenguajes:
            print(lenguaje)
    else:
        print(f"el lenguaje favorito de {programador} es {lenguajes[0]}")

# diccionario dentro de diccionario
print("\n")
usuarios= {
    'goku2.0': {
        'nombre': "goku",
        'apellido': "segundo"
    },
    'gohan3.0': {
        'nombre': "gohan",
        'apellido': "tercero"
    }
}
for clave,valor in usuarios.items():
    print(f"{clave} se llama {valor['nombre']} {valor['apellido']}")