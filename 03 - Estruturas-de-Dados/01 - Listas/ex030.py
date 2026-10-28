numeros = [15, 8, 42, 23, 7, 31]

maior = numeros[0]

for i in range(len(numeros)):

    if  numeros[i] > maior:
        maior = numeros[i]


print(f"O maior número da lista é: {maior}")