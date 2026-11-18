
produtos = [
    {"nome": "Notebook", "quantidade": 3, "preco": 3500},
    {"nome": "Mouse", "quantidade": 12, "preco": 80},
    {"nome": "Teclado", "quantidade": 0, "preco": 150},
    {"nome": "Monitor", "quantidade": 4, "preco": 900},
    {"nome": "Headset", "quantidade": 8, "preco": 250}
]

def listar_produtos():
    for produto in produtos:
        print(f"{produto['nome']} - Estoque: {produto['quantidade']}")

def calcular_estoque():
    total = 0

    for produto in produtos:
        total += produto["quantidade"] * produto["preco"]

    print(f"Valor total do estoque: R$ {total}")

def produtos_baixo_estoque():
    for produto in produtos:
        if produto["quantidade"] < 5 and produto["quantidade"] > 0:
            print(f"{produto['nome']} - Estoque baixo")
            
        elif produto["quantidade"] == 0:
            print(f"{produto['nome']} - Sem estoque")

def consultar_produto(nome):

    produto_encontrado = False

    verificacao = nome.lower()

    for produto in produtos:
        if produto["nome"].lower() == verificacao:
            print(f"Produto encontrado: {produto['nome']}")
            produto_encontrado = True
            break

    if not produto_encontrado:
        print("O produto não foi encontrado.")


listar_produtos()
calcular_estoque()
produtos_baixo_estoque()
consultar_produto("MOUSE")
