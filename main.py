print("¡Hola Mundo!")

# ! =====================
# ! Variables
# ! =====================

#? ---------------------
#? Cadenas (Strings)
#? ---------------------

nombre = "Maximiliano"
segundo_nombre = "Luis"

print(nombre)
print(segundo_nombre)
print(type(nombre)) # str
print(type(segundo_nombre)) # str

# * Operaciones básicas con cadenas

# Concatenación
nombre_segundo_nombre = nombre + " " + segundo_nombre

# Uso típico
print("Nombre y segundo nombre: ", nombre_segundo_nombre)

# f-strings (forma correcta y moderna)

print(f"Hola, mi nombre es '{nombre}' y mi segundo nombre es '{segundo_nombre}'")

#? ---------------------
#? Enteros (int)
#? ---------------------

mi_edad = 22
cantidad_de_mascotas = 2
print(mi_edad)
print(cantidad_de_mascotas)

# Operaciones básicas
edad_en_12_anios = mi_edad + 12
total_mascotas = cantidad_de_mascotas * 2

print("Edad en 12 años:", edad_en_12_anios)
print("Mascotas totales:", total_mascotas)



