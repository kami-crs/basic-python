# difine una funcion con la palabra def 
# la triple comilla sirve para describir la funcion """"""
def saludar_usuario():
    """esta funcion es para saludar"""
    print("hola")

saludar_usuario()

# pasar informacion a una funcion
# la variable valor se le llama parametro al momento de definir la funcion
def saludar_por_nombre(valor):
    """mostrar un saludo"""
    print(f"hola {valor}")
# la variable string "vicen" en el momento de llamar la funcion se conoce como argumento 
saludar_por_nombre("vicen")
saludar_por_nombre("sabri")

# 1. parametros segun su posicion 
def describir_mascota(clase, nombre):
    """mostrar informacion sobre mascotas"""
    print(f"yo tengo un {clase}")
    print(f"mi {clase} se llama {nombre}")
describir_mascota("gato", "kitty")

# 2. argumentos usando claves
describir_mascota(nombre="milo", clase="perro")

# valores por defecto
def describir_mascota2(nombre, clase="perro"):
    """mostrar informacion sobre mascotas"""
    print(f"\nyo tengo un {clase}")
    print(f"mi {clase} se llama {nombre}")
    
describir_mascota2("milo2", "gato")

# retornar valores
def nombre_completo(nombre, apellido):
    """devuelve el nombre completo"""
    union = f"{nombre} {apellido}"
    return union
nombre_apellido = nombre_completo("katiaa", "balbuena")
print("\n"+nombre_apellido)

# retornar valores con argumentos opcionales
def primer_segundo_nombre(nombre, apellido, segundo_nombre=""):
    """devuelve primer y segundo nombre"""
    if segundo_nombre:
        unir = f"{nombre} {segundo_nombre} {apellido}"
    else:
        unir = f"{nombre} {apellido}"
    return unir
primer_segundo = primer_segundo_nombre("katita", "Balbuena", "sabrina")
print(primer_segundo)

# retornar un diccionario
def crear_persona(primer_nombre, segundo_nombre):
    """Esta funcion crea una diccionario para los nombres"""
    persona= {
        'primer': primer_nombre, 
        'segundo': segundo_nombre
    }
    return persona
print(crear_persona("tainy", "sofia"))

def crear_persona2(primer_nombre, segundo_nombre, edad=None):
    """retorna un diccionario de informacion sobre una persona"""
    persona= {
        'primer': primer_nombre,
        'segundo': segundo_nombre
    }
    if edad:
        persona['edad'] = edad
    return persona
print(crear_persona2("katherine", "fiorella", 47))
print(crear_persona2("Ana", "sofia"))

# pasar una lista como parametro
def saludar_usuarios(usuarios):
    """esta funcion sirve para iterar una lista y saludar a cada uno de los usuarios""" 
    for usuario in usuarios:
        print(f"Hola {usuario.title()}!")
saludar_usuarios(["ana", "sofia", "sabrina"])
saludar_usuarios(["sabrina"])

# usar una funcion para modificar una lista
libros_sin_imprimir= ["harry potter", "el principito", "pinocho"]
libros_impresos= []
while libros_sin_imprimir:
    libro_para_imprimir = libros_sin_imprimir.pop()
    print(f"Imprimiendo el libro {libro_para_imprimir}")
    libros_impresos.append(libro_para_imprimir)
print(libros_impresos)


# pasando un numero arbitrario de argumentos
def preparar_pizza(*ingredientes):
    """imprimir la lista de indredientes como tuples"""
    print(f"\n {ingredientes}")
preparar_pizza("queso")
preparar_pizza("queso", "pepperoni")


# mezclar parametros con argumentos arbitrarios
def preparar_pizza2(masa, *ingredientes):
    """Descripcion de la pizza"""
    print(f"\nEl pedido de la pizza fue con masa tipo {masa}, con los siguinetes ingredientes: ")
    for ingrediente in ingredientes:
        print(ingrediente)
preparar_pizza2("fina", "queso", "pepperoni", "carne")


# guardar una funcion dentro de un diccionario
def hello():
    print("hola")
persona = {
    'nombre': "ana",
    'edad': 25,
    'amigos': ["sofia", "florencia"],
    'ubicacion': {
        'ciudad': "cde",
        'avenida': "san jose"
    },
    'saludar': hello
}
persona['saludar']()