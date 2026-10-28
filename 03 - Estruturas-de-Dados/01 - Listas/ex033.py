numeros = [12, -5, 8, 0, 23, -10, 8, 15, -3, 0]

positivos = 0
negativos = 0
qtd_oito = 0
zeros = 0

for i in numeros:

    if i > 0:
        positivos += 1

    if i < 0:
        negativos += 1

    if i == 8:
        qtd_oito += 1

    if i == 0:
        zeros += 1

print(positivos)
print(negativos)
print(qtd_oito)
print(zeros)