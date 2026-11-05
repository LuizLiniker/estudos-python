treinamento_python = ["Ana", "Carlos", "Mariana", "Pedro", "Ana"]
treinamento_excel = ["Carlos", "João", "Mariana", "Lucas", "Carlos"]

#retorna sem repetidos
alunos_python = set(treinamento_python)
alunos_excel = set(treinamento_excel)

print(alunos_python)
print(alunos_excel)


# retorna nomes que tem nos dois
nos_dois = set(treinamento_python).intersection(treinamento_excel)
print(nos_dois)

todos = set(treinamento_python).union(treinamento_excel)
print(todos)

#retorna apenas a diferença
apenas_pyhton = set(treinamento_python).difference(treinamento_excel)
print(apenas_pyhton)