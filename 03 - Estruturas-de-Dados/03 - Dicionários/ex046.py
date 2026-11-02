alunos = {
    "Ana": {"idade": 20, "nota": 8.5},
    "Carlos": {"idade": 22, "nota": 6.0},
    "Mariana": {"idade": 19, "nota": 9.2}
}

aprovados = 0
reprovados = 0

for nome, dados in alunos.items():

    if dados["nota"] >= 7:
        dados["situação"] = "Aprovado"
        aprovados += 1
    else:
        dados["situação"] = "Reprovado"
        reprovados += 1

    print(f"{nome} - {dados["situação"]}")

print(f"\nTotal de aprovados: {aprovados}")
print(f"Total de reprovados: {reprovados}")
