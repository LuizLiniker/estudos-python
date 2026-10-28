numeros = [10, 25, 7, 40, 15, 25, 8]

contador = 0

for i in range(len(numeros)):
    if numeros[i] == 25:
        contador += 1

print(f"O número 25 aparece {contador} vezes")