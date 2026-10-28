soma = 0

while True:
    try:
        quant_numero = int(input("Digite quantos números você quer digitar: "))

        if quant_numero <= 0:
            print("A quantidade deve ser maior que 0. Digite novamente.")
            continue

        break
    except ValueError:
        print("Opção inválida! Digite um número inteiro.")
        continue

for i in range (quant_numero):
    while True:
        try:
            numero = int(input("Digite um número inteiro: "))
            break
        except ValueError:
            print("Opção inválida! Digite um número válido")

    soma += numero
media = soma / quant_numero

print(f"\nA soma dos números informados é: {soma}")
print(f"A média dos números informados é: {media}")