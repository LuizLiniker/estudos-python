numeros = [10, 15, 20, 25, 30, 35]

for i in range(len(numeros)):

    if numeros[i] % 2 == 0:
        numeros[i] = numeros[i] * 2
        print(f"Número: {i}")

print(f"Lista modificada: {numeros}")