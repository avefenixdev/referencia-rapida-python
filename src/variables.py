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

#? --------------------------------
#? Números con decimales (float)
#? --------------------------------

precio = 19.99
altura = 1.70
promedio = 8.5

# Operaciones con decimales
precio_con_iva = precio * 1.21
altura_en_cm = altura * 100

print("Precio con IVA:", precio_con_iva)
print(f"Altura en cm: {altura_en_cm}")

#? --------------------------------
#? Booleanos
#? --------------------------------

es_estudiante = True
es_fin_de_semana = False

if es_estudiante:
    print("Es estudiante")

if not es_fin_de_semana:
    print("No es fin de semana")
