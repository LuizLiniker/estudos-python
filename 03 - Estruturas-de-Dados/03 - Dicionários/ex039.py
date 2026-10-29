inventario = {
    "Pocao": 3,
    "Espada": 1,
    "Escudo": 1
}

print(inventario["Pocao"])

print("O jogador encontrou mais duas poções")
print("Obteve 2 Poções")
inventario["Pocao"] = inventario["Pocao"] + 2
 
print(inventario["Pocao"])

print("Jogador utilizou a espada.")
del inventario["Espada"]

print("Jogador encontrou uma chave!")
print("Obteve uma chave!")

inventario["Chave"] = 1

print(inventario)