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

    print(f"{escolha_item} selecionado.")

    if inventario[escolha_item] > 0:
        print(f"Você usou {escolha_item}.")
        item_usado = inventario[escolha_item] - 1
        print(f"{escolha_item} - {item_usado}.")
        inventario[escolha_item] = item_usado

        print(inventario)

    elif inventario[escolha_item] == 0:
        print(f"{escolha_item} - {inventario[escolha_item]}")
        print(f"{escolha_item} esgotado.")
else:
    print("Item não encontrado no inventário.")
