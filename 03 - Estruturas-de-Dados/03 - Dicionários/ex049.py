produto = {
    "nome": "Notebook",
    "preco": 3500,
    "estoque": 5
}


#retorna apenas as chaves como: nome, preco e estoque
for i in produto.keys():
    print(f"{i}")


#retorna apenas os valores como: Notebook, 3500 e 5
for i in produto.values():
    print(f"{i}")