my_strings = "i can't go"
print(my_strings.title())

name = "ADA lovelace"
print(name)
# la funcion title sirve para formatear el texto
print(name.title())

paragraph = "hoy dia martes 26 de noviembre inicie mi cuerso."
# la funcion upper sirve para pasar todo a mayuscula
print(paragraph.upper())
# la funcion lower sirve para pasar todo a minuscula
print(name.lower())

# f: format
first_name = "ada"
last_name = "lovelace"
full_name = f"hello, {first_name.title()} {last_name.title()}."
print (full_name)

# newline or tabs
print("python")
print("\tpython")
print("languages:\n\tpython\n\tjavascript\n\tc")

# remover espacio
favorite_languages = " python"
print(favorite_languages.strip())

# remover prefijos
url = "https://www.youtube.com"
url = url.removeprefix("https://")
print(url)  