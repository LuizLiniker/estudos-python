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


funcionarios.append({
    "nome": "Pedro",
    "cargo": "Analista",
    "salario": 3000
})

funcionarios.append({
    "nome": "Lucas",
    "cargo": "Desenvolvedor",
    "salario": 4500
})

soma = 0

for funcionario in funcionarios:
    print(f"Nome: {funcionario["nome"]} - Cargo: {funcionario["cargo"]} - Salário: {funcionario["salario"]}.")

    soma += funcionario["salario"]

print(f"A soma total de todos os salários: {soma}")