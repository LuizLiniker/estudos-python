alunos = {
    "Ana": {
        "idade": 20,
        "nota": 8.5,
        "frequencia": 90
    },
    "Carlos": {
        "idade": 22,
        "nota": 6.0
    },
    "Mariana": {
        "idade": 19,
        "nota": 9.2,
        "frequencia": 85
    }
}

for nome, dados in alunos.items():

    print(f"Nome: {nome} \n idade: {dados.get("idade", "Não informada")} \n nota: {dados.get("nota", "Não informada")} \n Frequência: {dados.get("frequencia", "Não informada")}\n")