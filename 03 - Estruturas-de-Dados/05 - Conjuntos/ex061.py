usuarios_ativos = ["Ana", "Carlos", "Mariana", "Pedro", "João", "Ana"]

usuarios_premium = ["Carlos", "Mariana", "Lucas", "Pedro", "Carlos"]

ativos = set(usuarios_ativos)
premium = set(usuarios_premium)

print(ativos)
print(premium)

possuem_premium = set(ativos).intersection(premium)
print(possuem_premium)

nao_possui = set(ativos).difference(premium)
print(nao_possui)

cadastrados = set(ativos).union(premium)
print(cadastrados)

inativos_preumim = set(premium).difference(ativos)
print(inativos_preumim)