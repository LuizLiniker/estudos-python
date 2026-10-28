numeros = [10, -5, 20, -8, 30, -2]

for i in range(len(numeros)):
    if numeros[i] < 0:
        numeros[i] = 0

print(f"Lista modificada: {numeros}")