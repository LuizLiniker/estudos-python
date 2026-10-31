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

alunos["Ana"]["nota"] = 9.5
alunos["Mariana"]["idade"] = 20
alunos["Carlos"]["aprovado"] = True

print(alunos["Ana"])
print(alunos["Mariana"])
print(alunos["Carlos"])
