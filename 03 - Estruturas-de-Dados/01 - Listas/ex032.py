numeros = [12, -5, 8, 0, 23, -10, 8, 15, -3, 0]

negativo = 0
positivo = 0
numero_oito = 0
zero = 0
soma = 0
media = 0
maior = numeros[0]
menor = numeros[0]

for i in range(len(numeros)):

    if numeros[i] > 0:
        positivo += 1
    elif numeros[i] < 0:
        negativo += 1
    else:
        zero += 1

    if numeros[i] == 8:
        numero_oito += 1

    if numeros[i] > maior:
        maior = numeros[i]
    elif numeros[i] < menor:
        menor = numeros[i]

    soma += numeros[i]

media = soma / len(numeros)

print(f"Quantidade de números positivos: {positivo}")
print(f"Quantidade de números negativos: {negativo}")
print(f"Quantidade de números 8: {numero_oito}")
print(f"Quantidade de zeros: {zero}")
print(f"O maior número: {maior}")
print(f"O menor número: {menor}")
print(f"A soma dos números: {soma}")
print(f"A média dos números: {media}")