funcionarios = {
    "Ana": {
        "cargo": "Desenvolvedora",
        "salario": 3500
    },
    "Carlos": {
        "cargo": "Analista",
        "salario": 2800
    },
    "Mariana": {
        "cargo": "Designer",
        "salario": 3200
    }
}

funcionarios["Ana"].update({
    "salario": 4000
})

funcionarios["Carlos"].update({
    "cargo": "Desenvolvedor",
    "salario": 3800
})

funcionarios["Pedro"] = {
    "cargo": "Analista",
    "salario": 3000
}

soma = 0
    
for nome, dados in funcionarios.items():
    print(f"Nome: {nome} - Cargo: {dados["cargo"]} - Salário: {dados["salario"]}")

    soma += dados["salario"]

print(f"Total de todos os salários: {soma}")