inventario = {
    "Pocao": 5,
    "Escudo": 1,
    "Chave": 1,
    "Madeira": 12,
    "Ferro": 8
}

qtd_estoque_baixo = 0

for item, quantidade in inventario.items():

    if quantidade <= 2:
        print("Estoque baixo:")
        print(f"{item}: {quantidade}")
        

        qtd_estoque_baixo += 1


print(f"Total de itens com estoque baixo: {qtd_estoque_baixo}")