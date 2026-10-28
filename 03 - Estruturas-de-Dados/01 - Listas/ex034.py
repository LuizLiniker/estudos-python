numeros = [12, -5, 8, 0, 23, -10, 8, 15, -3, 0]
soma = 0
positivos_lista = []
maior = 0

for i in numeros:

    if i > 0:
        soma += i
        positivos_lista.append(i)

    if i > maior:
        maior = i

print(soma)
print(maior)
print(positivos_lista)

    