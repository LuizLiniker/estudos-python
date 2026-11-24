produtos = {
    "Notebook": 3500,
    "Mouse": 80,
    "Teclado": 150
}

soma = 0
contador = 0

for nome, preco in produtos.items():
    try:
        quantidade = int(input(f"Quantidade de {nome}: "))

        if quantidade < 1 or quantidade > 100:
            print("Quantidade inválida")
            continue

        total = quantidade * preco
        print(f"{nome}: R$ {total}")

        soma += total

        contador += 1

    except ValueError:
        print("Digite uma quantidade numérica")


if contador > 0:

    print(f"Valor total da compra: R${soma}")
    print(f"Produtos com compras válidas: {contador}")

else: 
    print("Nenhuma compra foi válida.")

