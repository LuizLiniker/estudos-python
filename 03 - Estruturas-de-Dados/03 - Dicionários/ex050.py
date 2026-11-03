produtos = {
    "Notebook": {
        "preco": 3500,
        "estoque": 5
    },
    "Mouse": {
        "preco": 80,
        "estoque": 12
    },
    "Teclado": {
        "preco": 150,
        "estoque": 0
    },
    "Monitor": {
        "preco": 900,
        "estoque": 3
    }
}


qtd_produtos = 0
soma = 0
sem_estoque = 0
com_estoque = 0
produtos_zerados = []
produtos_estoque = []

for nome, dados in produtos.items():
    print(f"Nome: {nome}, Preço: {dados["preco"]} - Estoque: {dados["estoque"]}")

    qtd_produtos += 1

    if dados["estoque"] <= 0:
        sem_estoque += 1
        produtos_zerados.append(nome)

    else: 
        com_estoque += 1
        preco = dados["preco"] * dados["estoque"]

        produtos_estoque.append(nome)

        soma += preco

print(f"\nTotal de produtos sem estoque: {sem_estoque}")
print(f"\nProduto sem estoque: {produtos_zerados}")
print(f"\nTotal de produto com estoque: {com_estoque}")
print(f"\nProduto com estoque: {produtos_estoque}")
print(f"\nValor total no estoque: {soma}")


