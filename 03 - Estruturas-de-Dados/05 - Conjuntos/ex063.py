participantes = [
    {"nome": "Ana", "evento": "Python", "nota": 8.5},
    {"nome": "Carlos", "evento": "Python", "nota": 7.0},
    {"nome": "Mariana", "evento": "Python", "nota": 9.0},
    {"nome": "Pedro", "evento": "Excel", "nota": 6.5},
    {"nome": "Carlos", "evento": "Excel", "nota": 8.0},
    {"nome": "Lucas", "evento": "Excel", "nota": 7.5},
    {"nome": "João", "evento": "Python", "nota": 5.5},
    {"nome": "Ana", "evento": "Excel", "nota": 9.0},
    {"nome": "Lucas", "evento": "Python", "nota": 8.0},
    {"nome": "Mariana", "evento": "Excel", "nota": 7.5}
]

participantes_python = []
participantes_excel = []
nomes_python = []
nomes_excel = []
soma_python = 0
soma_excel = 0

for participante in participantes:

    if participante["evento"] == "Python":
        participantes_python.append(participante)

    elif participante["evento"] == "Excel":
        participantes_excel.append(participante)

    else:
        print("Esse participante não está em nenhum evento.")

print(participantes_excel)
print(participantes_python)

for participante in participantes_python:

    nomes_python.append(participante["nome"])

for participante in participantes_excel:

    nomes_excel.append(participante["nome"])

conjuntos_python = set(nomes_python)
conjuntos_excel = set(nomes_excel)

ambos_eventos = conjuntos_python.intersection(conjuntos_excel)
pelo_menos_um = conjuntos_python.union(conjuntos_excel)
unicos = conjuntos_python.symmetric_difference(conjuntos_excel)

for participante in participantes_python:

    soma_python += participante["nota"]

for participante in participantes_excel:

    soma_excel += participante["nota"]
    
media_python = soma_python / len(participantes_python)
media_excel = soma_excel / len(participantes_excel)

print(media_python)
print(media_excel)

if media_excel >= 7:
    print(f"O evento de Excel atingiu a meta de média mínima de 7. \n Média: {media_excel}")

else:
    print("Média mínima do evento de Excel não foi atendida.")

if media_python >= 7:
    print(f"\nO evento de Python atingiu a meta de média mínima de 7. \n Média: {media_python}")

else:
    print("Média mínima do evento de Python não foi atendida.")


print(f"Quantidade de pessoas que participaram de apenas um evento: {len(unicos)}")
print(f"Quantidade de pessoas que participaram dos dois eventos: {len(ambos_eventos)}")
print(f"Quantidade de pessoas que participaram do evento de Python: {len(participantes_python)}")
print(f"Quantidade de pessoas que participaram do evento de Excel: {len(participantes_excel)}")
print(f"Quantidade de pessoas que participaram de pelo menos um evento: {len(pelo_menos_um)}")