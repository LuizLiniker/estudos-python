numeros = [4, 7, 4, 2, 7, 9, 2, 1]

sem_duplicados = []

for i in numeros:

    if i not in sem_duplicados:
        sem_duplicados.append(i)


print(sem_duplicados)