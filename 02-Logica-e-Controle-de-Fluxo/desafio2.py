soma = 0
positivos = 0
negativos = 0
zeros = 0
       
while True:
    try:
        quant_numero = int(input("Digite a quantidade de números a serem informados: "))

        if quant_numero <= 0:
            print("Opção inválida! Informe um número maior que 0.")
            continue

        break
    except ValueError:
        print("Opção inválida! Digite um número inteiro.")
        continue

for i in range(quant_numero):
    while True:
        try:
            numero = int(input("Digite um número inteiro: "))

            if numero == 0:
                print("zero")
                zeros += 1

            elif numero > 0:
                print("positivo")
                positivos += 1

            else:
                print("negativo")
                negativos += 1

            break
        except ValueError:
            print("Opção inválida! Digite um número inteiro.")

    soma += numero

media= soma / quant_numero

print(f"A soma dos números é: {soma}")
print(f"A média dos números é: {media}")
print(f"A quantidade de números iguais à zero é: {zeros}")
print(f"A quantidade de números positivos é: {positivos}")
print(f"A quantidade de números negativos é: {negativos}")
