soma = 0
positivos = 0
zeros = 0


numeros = [10, -5, 20, 0, -3]

for numero in numeros:
    if numero > 0:
        positivos += 1

    elif numero == 0:
        zeros += 1

    soma += numero

    print(f"Número: {numero}")

print(f"Quantidade de zeros: {zeros}")
print(f"Quantidade de positivos: {positivos}")
print(f"Soma: {soma}")