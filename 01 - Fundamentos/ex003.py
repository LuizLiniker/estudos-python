numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

def adicao():
    soma = numero1 + numero2
    print(f"A soma dos dois números digitados é: {soma}")

def subtracao():
    menos = numero1 - numero2
    print(f"A subtração entre os dois números é: {menos}")

def divisao():
    dividir = numero1 / numero2
    print(f"A divisão entre os dois números é: {dividir}")

def multiplicar():
    multiplicacao = numero1 * numero2
    print(f"A multiplicação entre os dois números é: {multiplicacao}")

adicao()
subtracao()
divisao()
multiplicar()