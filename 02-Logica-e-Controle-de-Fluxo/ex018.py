positivos = 0
negativos = 0
zeros = 0



for i in range(5):
    while True:
        try:
            numero = int(input("Digite um número inteiro: "))
            break
        except ValueError:
            print("Opção inválida! Digite um número inteiro.")
            continue

    if numero == 0:
        print("O número é zero.")
        zeros += 1
    elif numero < 0:
        print("O número é negativo.")
        negativos += 1
    elif numero > 0:
        print("O número é positivo.")
        positivos += 1

print(f"\nQuantidade de números positivos: {positivos}")
print(f"\nQuantidade de números negativos: {negativos}")
print(f"\nQuantidade de zeros: {zeros}")

    
                    