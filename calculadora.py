def calcular(a, b):
    suma = a + b
    resta = a - b
    multi = a * b

    if b != 0:
        division = a / b
    else:
        division = None
        print("No podemos dividir entre 0")

    return suma, resta, multi, division


# Datos de entrada
a = 8
b = 2

# Llamada a la función y desempaquetado
suma, resta, multi, division = calcular(a, b)

print("---Calculando---")
print(f"La suma de {a} + {b} es {suma}")
print(f"La resta de {a} - {b} es {resta}")
print(f"La multiplicación de {a} * {b} es {multi}")

# Validación de la división
if division is not None:
    print(f"La división de {a} / {b} es {division}")
else:
    print("No se pudo realizar la división")
