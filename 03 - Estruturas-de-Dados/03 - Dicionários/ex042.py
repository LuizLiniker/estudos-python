inventario = {
    "Pocao": 5,
    "Escudo": 1,
    "Chave": 1,
    "Madeira": 12,
    "Ferro": 8
}


print(inventario)

escolha_item = str(input("Qual item você deseja do inventário: "))

if escolha_item in inventario:
    print(f"Item selecionado: {escolha_item} - {inventario[escolha_item]}")
else:
    print("Item não encontrado no inventário.")