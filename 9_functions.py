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