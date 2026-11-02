alunos = {
    "Ana": {"idade": 20, "nota": 8.5},
    "Carlos": {"idade": 22, "nota": 6.0},
    "Mariana": {"idade": 19, "nota": 9.2}
}

maior_nota = 0
soma = 0
qtd_alunos = 0
media = 0
aluno_maior_nota = ""
aprovados = 0
reprovados = 0

for nome, dados in alunos.items():

    soma += dados["nota"]

    if dados["nota"] > maior_nota:
        aluno_maior_nota = nome
        maior_nota = dados["nota"]

    if dados["nota"] >= 7:
        aprovados += 1
    else:
        reprovados += 1

    qtd_alunos += 1

media = soma / qtd_alunos

print(f"O aluno com a maior nota é: {aluno_maior_nota} - {maior_nota}")
print(f"Total de aprovados: {aprovados}")
print(f"Total de reprovados: {reprovados}")
print(f"A média da turma é: {media}")