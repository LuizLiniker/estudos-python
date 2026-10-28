numeros = [10, 5, 20, 3, 40, 7]

for i in range(len(numeros)):

    if i % 2 == 0:
        numeros[i] = numeros[i] * 2

print(f"Lista Modificada: {numeros}")