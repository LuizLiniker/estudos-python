alunos = {
    "Ana": {
        "idade": 20,
        "nota": 8.5
    },
    "Carlos": {
        "idade": 22,
        "nota": 6.0
    },
    "Mariana": {
        "idade": 19,
        "nota": 9.2
    }
}

soma = 0
qtd_alunos = 0

for nome, dados in alunos.items():
    print(f"{nome} - idade: {dados["idade"]} - nota: {dados["nota"]}")

    soma += dados["nota"]
    qtd_alunos += 1

media = soma / qtd_alunos

print(f"A média geral da turma é {media}")
    