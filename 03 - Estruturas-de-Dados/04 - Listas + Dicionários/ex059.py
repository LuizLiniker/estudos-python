funcionarios = [
    {
        "nome": "Ana",
        "cargo": "Desenvolvedora",
        "salario": 4000
    },
    {
        "nome": "Carlos",
        "cargo": "Analista",
        "salario": 3800
    },
    {
        "nome": "Mariana",
        "cargo": "Designer",
        "salario": 3200
    }
]

def cadastrar_funcionario():
    nome = str(input("Digite o nome do funcionário: "))
    cargo = str(input("Digite o cargo do funcionário: "))
    salario = int(input("Digite o salário do funcionário: "))

    funcionarios.append({
        "nome": nome,
        "cargo": cargo,
        "salario": salario
    })

    print("Funcionário cadastrado")

def consultar_funcionario():
    nome = str(input("Digite o nome do funcionário: "))

    encontrou_funcionario = False

    for funcionario in funcionarios:

        if nome == funcionario["nome"]:
            print(f"Nome: {funcionario["nome"]} - Cargo: {funcionario["cargo"]} - Salario: {funcionario["salario"]}")
            encontrou_funcionario = True

    if not encontrou_funcionario:
        print("Este funcionário não está cadastrado.")

                

def apagar_funcionario():
    nome = str(input("Digite o nome do funcionário: "))

    encontrar_funcionario = False

    for funcionario in funcionarios:
        if funcionario["nome"] == nome:

            funcionarios.remove(funcionario)
            print("Funcionário removido")
            encontrar_funcionario = True
            return

    if not encontrar_funcionario:
        print("Este funcionário não está cadastrado.")

def todos_funcionarios():

    for funcionario in funcionarios:
        print(f"Nome: {funcionario["nome"]} - Cargo: {funcionario["cargo"]} - Salário: {funcionario["salario"]}")

print("CADASTRO DE FUNCIONÁRIOS")

while True:

    print("MENU")  
    print("1 - Cadastrar Funcionário")
    print("2 - Consultar Funcionário")
    print("3 - Apagar Funcionário")
    print("4 - Todos os Funcionários'")
    print("0 - Sair")

    try:
        escolha = int(input("Digite qual função deseja acessar: "))

        if escolha < 0 or escolha >= 5:
            print("Digite uma opção válida")
            continue

    except ValueError:
        print("Digite uma opção válida")
        continue

    if escolha == 1:
        cadastrar_funcionario()
    elif escolha == 2:
        consultar_funcionario()
    elif escolha == 3:
        apagar_funcionario()
    elif escolha == 4:
        todos_funcionarios()
    else:
        break