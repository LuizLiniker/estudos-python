criatura1 = ("Organismo Abissal", 80, 3)
criatura2 = ("Parasita Mecânico", 120, 4)


nome, vida, ameaca = criatura1
nome2, vida2, ameaca2 = criatura2

print(f"Nome: {nome}, Vida: {vida} e Ameaça: {ameaca}")
print(f"Nome: {nome2}, Vida: {vida2} e Ameaça: {ameaca2}")

if vida > vida2:
    print(f"{nome} tem mais vida")
else:
    print(f"{nome2} tem mais vida")
