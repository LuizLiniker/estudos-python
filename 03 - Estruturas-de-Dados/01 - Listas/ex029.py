numeros = [10, -5, 20, -8, 10, 30, -5, 40]

soma = 0
positivo = 0
negativo = 0
igual = 0

for i in range(len(numeros)):

    if numeros[i] > 0:
        positivo += 1
    elif numeros[i] < 0:
        negativo += 1

    if numeros[i] == 10:
        igual += 1

    soma += numeros[i]


print(f"Quantidade de números positivos: {positivo}")
print(f"Quantidade de números negativos: {negativo}")
print(f"Quantidade de números 10: {igual}")
print(f"Soma: {soma}")