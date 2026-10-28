numeros = []

while True:
    try:
        quant_numeros = int(input("Digite quantos números irá informar: "))

        if quant_numeros <= 0:
            print("Digite um núemro maior que 0.")

        else:
            break
    except ValueError:
        print("ERRO! Digite um número INTEIRO.")
        continue

for i in range(quant_numeros):
    while True:
        try:
            numeros.append(int(input(f"Digite o {i + 1}° número: ")))
            break
        except ValueError:
            print("ERRO! Digite apenas números INTEIROS.")

print(f"Lista: {numeros}")
print(f"Primeiro número: {numeros[0]}")
print(f"Último número: {numeros[-1]}")
print(f"Quantidade  de números informados: {len(numeros)}")