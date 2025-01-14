# imput pasa todo a string"" 
# >>> mensaje = input("Escribe un numero: ")
# Escribe un numero: 3
# >>> mensaje
# '3'
# >>> int(mensaje)
# 3
mensaje = input("Todo lo que me escribas te lo voy a repetir: ")
print(f'Tu mensaje es {mensaje}\n')

prompt = "Si me compartes tu nombre te lo podemos personalizar."
prompt += "\nCual es tu nombre? "
name = input(prompt)
print(f"Hola {name}!")

# Usando int para aceptar valores numericos
edad = input("Cual es tu edad? ")
# edad = int(edad)
if int(edad) > 21:
    print("Ya eres lo suficientemente grande")
else:
    print("Aun eres menor")

# operador de modulo
print(f"4 % 2: {4 % 2}")
print(f"7 % 3: {7 % 3}")

# juego de par o impar
numero = input("Elije un numero y te dire si es par o impar: ")
numero = int(numero)
if numero % 2 == 0:
    print(f"El numero {numero} es par")
else:
    print(f"El numero {numero} es impar")
