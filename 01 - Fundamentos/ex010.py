cidade = input("Digite o nome de uma cidade com V:")
verificador = cidade.upper()
letra = verificador.startswith("V")

if letra:
    print(f"Essa cidade começa com a letra V: {cidade}")

else:
    print("Essa cidade não começa com a letra V")