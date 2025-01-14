# list es una coleccion ordenada
friends = ["mabel", "dipper", "soos", "wendy", "stanley"]
print(friends)
# -1 es para traer el ultimo elemento
print(friends[-1])
# 0 es para traer el primer elemento
print(friends[0])
# 2 es para traer el tercer elemento
print(friends[2])

print(friends[3].title())
print(friends[3].upper())

mensaje = f"hola {friends[0].title()}, yo soy {friends[2].upper()}"
print(mensaje)

motocicleta = ["honda", "yamaha", "suzuki"]
print(motocicleta)
# append sirve para agregar un nuevo valor a la lista
motocicleta.append("kawasaki")
print(motocicleta)

series = []
series.append("breaking bad")
series.append("better call saul")
series.append("slam dunk")
series.append("berserk")
print(series)

series.insert(1,"dark")
print(series)
# del es borrar o remover de una listan utilizando el index(posicion)
del series[3]
print(series)
# pop sirve para sacar o eliminar el ultimo elemento de la lista y develver ese mismo valor
ultima_serie = series.pop()
print(series)
print(f"ultima serie: {ultima_serie}")
# remove es una funcion que sirve para eliminar utilizando su nombre
series.remove("dark")
print(series)

# sort esta funcion sirve para ordenar alfabeticamente y si le pasas el parametro "reverse" con el valor "true" hace lo contrario 
friends.sort(reverse=True)
print(friends)

# sorted hace lo mismo que sort pero de forma temporal
frutas= ["banana", "pina", "manzana", "aguacate"]
print(sorted(frutas))
print(frutas)   

numeros = [1, 2, 3, 4, 5]
numeros.reverse()
print(numeros)

print(f"tengo {len(friends)} amigos\n")

# forloop son acciones repetitivas
magicians= ["harry", "alice", "dabby", "carolina"]
num = 0
for mago in magicians:   
    num += 1
    # num = num + 1 
    print(f"{mago.title()} sos el mago numero {num}")
print("Gracias por el show\n")

# iterar usando un rango: range()
# el itera y para uno antes del valor original
for value in range(1, 6):
    print(value)

#lista_de_numeros = [1, 2, 3, 4, 5]
nuevo_rango = range(1, 6)
lista_de_numeros = list(nuevo_rango)
print(lista_de_numeros)

# lista de numeros pares
rango_par = range(2, 21, 2)
lista_de_numeros_pares = list(rango_par)
print(lista_de_numeros_pares)

# crear una lista elevado al cuadrado
cuadrados = []
for valor in range(1, 11):
    cuadrado = valor ** 2
    cuadrados.append(cuadrado)
print(cuadrados)

# estadisticas
edades = [5, 11, 2, 25, 7, 40, 79]
print(f"la edad minima es {min(edades)}")
print(f"la edad maxima es {max(edades)}")
print(f"la sumatoria de las edades es {sum(edades)}\n")

# list comprehension
cuadrados = [valor**2 for valor in range(1, 11)]
print(cuadrados)


# slice
# con sort() ordene la lista de forma alfabetica
# y con lista_de_nombres[0:3] corte la lista desde posicion 0 una cantidad de 3 elementos
lista_de_nombres = ["juan", "pedro", "anna", "maria", "sabrina"]
lista_de_nombres.sort()
lista_filtrada = lista_de_nombres[0:3]
print(lista_filtrada)

# hacer loop(iterar, repetir acciones) en una lista ordenada alfabeticamente de los tres primeros elementos
for nombre in lista_de_nombres[0:3]:
    print(nombre.title())

# copiar listas
lista_de_bebidas = ["coca-cola", "sprite", "agua", "guarana"]
nueva_lista = lista_de_bebidas[:] # [:] esta copiando la lista
lista_de_bebidas.remove("agua")  
print(nueva_lista)
print(nueva_lista[-3:])

# tuple : se utilizan para definir vectores
dimensiones = (1080, 720)
print(dimensiones[1])
for medida in dimensiones:
    print(medida)