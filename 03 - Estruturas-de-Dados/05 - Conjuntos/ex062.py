inscricoes = [
    {"nome": "Ana", "curso": "Python", "nota": 8.5},
    {"nome": "Carlos", "curso": "Python", "nota": 7.0},
    {"nome": "Mariana", "curso": "Python", "nota": 9.0},
    {"nome": "Pedro", "curso": "Excel", "nota": 6.5},
    {"nome": "Carlos", "curso": "Excel", "nota": 8.0},
    {"nome": "Mariana", "curso": "Excel", "nota": 7.5},
    {"nome": "João", "curso": "Excel", "nota": 5.5},
    {"nome": "Ana", "curso": "Excel", "nota": 9.0}
]

inscritos_python = []
inscritos_excel = []
nomes_python = []
nomes_excel = []


for inscrito in inscricoes:

    if inscrito["curso"] == "Python":
        inscritos_python.append(inscrito)
        

    else: 
        inscritos_excel.append(inscrito)
        

for inscrito in inscritos_python:

    nomes_python.append(inscrito["nome"])

for inscrito in inscritos_excel:

    nomes_excel.append(inscrito["nome"])

conjuntos_python = set(nomes_python)
conjuntos_excel = set(nomes_excel)

ambos_treinamento = conjuntos_python.intersection(conjuntos_excel)
apenas_um_treinamento = conjuntos_excel.symmetric_difference(conjuntos_python)
todos = conjuntos_python.union(conjuntos_excel)

print(apenas_um_treinamento)
print(ambos_treinamento)
print(todos)

