# ! ======================
# ! Operadores
# ! ======================

#? -----------------------
#? Operadores aritméticos
#? -----------------------

a = 22
b = 2

print(a + b)  # Suma -> 24
print(a - b)  # Resta -> 20
print(a * b)  # Multiplicación -> 44
print(a / b)  # División (float) -> 11.0
print(a // b) # División entera -> 11
print(a % b)  # Módulo (resto) -> 0
print(a ** b) # Potencia -> 484

#? -------------------------
#? Operadores de asignación
#? -------------------------

x = 5  # asignación
print(x) # 5
x += 2 # x = x + 2 # incremento
print(x) # 7
x -= 1 # x = x - 1 # decremento
print(x) # 6
x *= 3 # x = x * 3 # multiplicación compuesta
print(x) # 18
x /= 2 # x = x / 2 # división compuesta
print(x) # 9.0

#? -------------------------
#? Operadores de comparación
#? -------------------------
# Siempre devuelven booleanos

edad = 18

print(edad == 18) # Igualdad -> True
print(edad != 21) # Igualdad -> True
print(edad > 16) # Mayor que -> True
print(edad < 30) # Menor que -> True
print(edad >= 18) # Mayor o igual -> True
print(edad <= 17) # Menor o igual -> False

#? -------------------------
#? Operadores lógicos
#? -------------------------

es_estudiante = True
tiene_descuento = False

print(es_estudiante and tiene_descuento) # True | True si ambos son True
print(es_estudiante or tiene_descuento) # True | True si uno es True
print(not es_estudiante) # False | Niega el valor
