def verificar(numero):
    if numero == 0:
        print("O número é zero.")
    elif numero < 0:
        print("O número é negativo.")
    else:
        print("O número é positivo.")



while True:

    try:
        numero = int(input("Digite um número inteiro: "))
    except ValueError:
        print("Opção inválida! Digite novamente.")
        continue

    verificar(numero)

    try:
        sair = int(input("Para sair do programa digite 0 para continuar digite 1: "))

        if sair == 0:
            print("Você está saindo do programa! Até a próxima.")
            break
        elif sair == 1:
            continue
        else:
            print("Opção inválida!")
    except ValueError:
        print("Opção inválida! Digite novamente.")
        continue
    