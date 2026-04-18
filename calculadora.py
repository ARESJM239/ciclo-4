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


print(calcular(8, 2))