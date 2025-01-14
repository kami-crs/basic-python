# el while loops va a correr miestras cierta condicion sea verdadera
# 1. contar desde 1 a 5
numero_actual = 1
while numero_actual <= 5:
    print(numero_actual)
    numero_actual += 1
print(f"El numero actual es {numero_actual}")

prompt = "\nDime algo y te lo repetire."
prompt += "\nEscribe 'salir' para terminar el programa: "
mensaje = ""
while mensaje != 'salir':
    mensaje = input(prompt)
    if mensaje != 'salir':
        print(mensaje)

# 2. flag: bandera 
activo = True
while activo:
    mensaje = input(prompt)
    if mensaje == 'salir':
        activo = False
    else:
        print(mensaje)

# 3. utilizando break para salir del loop
prompt = "\nDime las ciudades que haz visitado."
prompt += "\nEscribe 'salir' para finalizar: "
while True:
    ciudad = input(prompt)
    if ciudad == 'salir':
        break
    else:
        print(f"Tambien me gustaria conocer {ciudad.title()}!")

# 4. usar continue en un loop 
# un loop que cuente del 1 al 10 e imprima los impares
numero_actual = 0 
while numero_actual < 10:
    numero_actual += 1 
    if numero_actual % 2 == 0:
        continue
    print(numero_actual)

# evitar bucles infinitos
print("\n")
x = 1
while x <= 5:
    print(x)
    x += 1

# usar while loops con listas y diccionarios
# mover items de una lista a otra
usuarios_confirmados = []
usuarios_no_confirmados = ["torres", "oliver", "noham"]
while usuarios_no_confirmados:
    usuario = usuarios_no_confirmados.pop()
    usuarios_confirmados.append(usuario)
    print(f"{usuario.title()} ha sido confirmado")
print(f"Todos los usuarios confirmados son {usuarios_confirmados}")

# remover todas las instancias que tengan un valor especifico dentro de una lista
mascotas = ["perro", "gato", "perro", "nemo", "gato", "conejo", "gato"]
print(f"\n{mascotas}")
while "gato" in mascotas:
    mascotas.remove("gato")
print(mascotas)

# rellenar un diccionario con input() de usuarios
respuestas = {}
# crear una bandera para indicar que la encuesta esta activa
encuesta = True
while encuesta:
    nombre = input("\nComo es tu nombre? ")
    respuesta = input("\nCual es tu lugar favorito para vacacionar?: ")
    # guardar respuesta en el diccionario
    respuestas[nombre] = respuesta
    # verificar si existe otra persona que va a responder la encuesta
    repetir = input("\nTe gustaria dejar que otra persona responda? (si / no): ")
    if repetir == "no":
        encuesta = False

# encuesta completa, mostrar resultado
for nombre, respuesta in respuestas.items():
    print(f"\nA {nombre} le gusta vacacionar en {respuesta}")