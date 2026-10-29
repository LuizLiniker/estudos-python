numeros = [12, -5, 8, 0, 23, -10, 8, 15, -3, 0]

pares = []
impares = []

for i in numeros:

    if i % 2 == 0:
        pares.append(i)
        
    elif i % 2 != 0:
        impares.append(i)
        
print(pares)
print(impares)