# Calculadora

# Função responsável por pedir um número ao usuário.
# O while mantém a pergunta ativa até que seja digitado um valor válido.
def pedir_numero(mensagem):
    while True:
        try:
            # float permite que o usuário digite números inteiros ou decimais.
            numero = float(input(mensagem))
            return numero

        # Caso o usuário digite algo que não possa ser convertido para número,
        # o programa não quebra: mostra uma mensagem e pede novamente.
        except ValueError:
            print("⚠️ Valor inválido, tente novamente.")


# Função responsável pela operação de soma.
def soma(numero1, numero2):
    adicao = numero1 + numero2
    print(f"O resultado da soma é: {adicao}")


# Função responsável pela operação de subtração.
def sub(numero1, numero2):
    subtracao = numero1 - numero2
    print(f"O resultado da subtração é: {subtracao}")


# Função responsável pela divisão.
def dividir(numero1, numero2):
    divisao = numero1 / numero2
    print(f"O resultado da divisão é: {divisao}")


# Função responsável pela multiplicação.
def mult(numero1, numero2):
    multiplicacao = numero1 * numero2
    print(f"O resultado da multiplicação é: {multiplicacao}")


# Função responsável pela operação de potência.
def pot(numero1, numero2):
    potencia = numero1 ** numero2
    print(f"O resultado da potência é: {potencia}")


# Função responsável por encontrar o resto de uma divisão.
def resto(numero1, numero2):
    sobra = numero1 % numero2
    print(f"O resultado é: {sobra}")


# Função responsável pela divisão inteira.
def divisao_int(numero1, numero2):
    inteira = numero1 // numero2
    print(f"O resultado é: {inteira}")


# O while True mantém a calculadora funcionando
# até que o usuário escolha a opção de sair.
while True:

    print("Calculadora")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Divisão")
    print("4 - Multiplicação")
    print("5 - Potência")
    print("6 - Resto")
    print("7 - Divisão inteira")
    print("8 - Sair")

    try:
        # Tenta transformar a escolha do usuário em um número inteiro.
        escolha = int(input("Digite o número respectivo da operação que você necessita: "))

    # Evita que o programa seja encerrado caso o usuário digite letras
    # ou outro valor que não possa ser convertido para inteiro.
    except ValueError:
        print("⚠️ Opção inválida. Por favor, digite uma opção válida para continuar.")
        continue

    # Verifica se o usuário escolheu sair antes de pedir os números.
    # Assim, não precisamos solicitar números que não serão utilizados.
    if escolha == 8:
        break

    # Pede os dois números necessários para realizar a operação escolhida.
    numero1 = pedir_numero("Digite o primeiro número: ")
    numero2 = pedir_numero("Digite o segundo número: ")

    # Verifica se a operação escolhida possui divisão.
    # O número 0 não pode ser utilizado como divisor.
    if escolha in (3, 6, 7) and numero2 == 0:
        print("O número 0 é invalido para divisão, digite outro")
        continue

    # Verifica qual operação o usuário escolheu
    # e chama a função correspondente.
    elif escolha == 1:
        soma(numero1, numero2)

    elif escolha == 2:
        sub(numero1, numero2)

    elif escolha == 3:
        dividir(numero1, numero2)

    elif escolha == 4:
        mult(numero1, numero2)

    elif escolha == 5:
        pot(numero1, numero2)

    elif escolha == 6:
        resto(numero1, numero2)

    elif escolha == 7:
        divisao_int(numero1, numero2)