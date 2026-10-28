numeros = [15, 8, 42, 23, 7, 31]

menor = numeros[0]

for i in range(len(numeros)):

    if numeros[i] < menor:
        menor = numeros[i]


print(f"O menor número da lista é: {menor}")