

#função para verificar qual número é o maior.
def maior(numero1, numero2, numero3):

    if numero3 == numero1 == numero2:
        print("Os três números são iguais")

    elif numero2 == numero1 and numero2 > numero3:
        print(f"Número 1 e o Número 2 são iguais e maiores que o número 3: {numero3}. {numero1} e {numero2}")

    elif numero2 == numero3 and numero2 > numero1:
       print(f"Número 2 e o Número 3 são iguais e maiores que o número 1: {numero1}. {numero2} e {numero3}")

    elif numero1 == numero3 and numero1 > numero2:
         print(f"Número 1 e o Número 3 são iguais e maiores que o número 2: {numero2}. {numero1} e {numero3}")

    elif numero1 > numero2 and numero1 > numero3:
        print(f"O maior número é: {numero1}")

    elif numero2 > numero1 and numero2 > numero3:
        print(f"O maior número é: {numero2}")

    else:
        print(f"O maior número é: {numero3}")



while True:


#valida se a entrada que o usuário forneceu é válida para este programa
    try:

        numero1 = int(input("\nDigite o primeiro número: "))
        numero2 = int(input("Digite o segundo número: "))
        numero3 = int(input("Digite o terceiro número: "))

        
    except ValueError:
        print("Erro! Digite algo válido.")
        continue

    maior(numero1, numero2, numero3)


#caso o usuário queira encerrar o programa
    try:
        sair = int(input("Para sair do programa DIGITE 0 e para continuar digite 1: "))

        if sair == 0:

            print("Você está saindo do programa! Até a proxima.")

            break

        elif sair == 1:

            continue

        else:
            print("Opção inválida. Digite 0 para sair ou 1 para continuar.")

    except ValueError:
        print("Erro! Digite algo válido")
        continue
