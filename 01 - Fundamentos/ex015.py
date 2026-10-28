
#função para verificar se o número é par ou ímpar
def verificador(numero):

    # Se o resto da divisão for igual a zero, o número é par; caso contrário, é ímpar.
    if numero % 2 == 0:

        print(f"O número {numero} é par")
    else:

        print(f"O número {numero} é ímpar")
    

while True:

    #faz a pergunta para o usuário
    try:
        numero = int(input("Digite um número inteiro: "))
    # Se o usuário digitar algo que não seja um número inteiro,
    # evita que o programa seja encerrado e solicita a entrada novamente.
    except ValueError:
        print("Erro! Digite algo válido")
        continue

    verificador(numero)

    break