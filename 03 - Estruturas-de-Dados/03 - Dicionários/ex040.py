inventario = {
    "Pocao": 5,
    "Escudo": 1,
    "Chave": 1,
    "Madeira": 12,
    "Ferro": 8
}

qtd_total = 0
tipos = 0 

for item, quantidade in inventario.items():
    print(f"{item}: {quantidade}")

    qtd_total += quantidade

    tipos += 1


print(qtd_total)
print(tipos)