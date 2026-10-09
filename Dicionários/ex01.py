# NÃO UTILIZANDO DICIONÁRIO:
nomes = ["Ethan", "Manson", "Lukas", "Mendy"]
notas = [75, 100, 65, 98]
print(f"Meendy: {notas[nomes.index("Mendy")]}")
# O INDEX ele transforma "Meendy" como se fosse uma posição, então ele compara essa mesma posição na lista de notas.
for nome in nomes:
    print(f"{nome}: {notas[nomes.index(nome)]}")
# Para cada nome registrado em nomes ele imprime o nome correspondente à nota, de acordo com a posição dos nomes e das notas nas listas!


# UTILIZANDO UM DICIONÁRIO (MAIS FÁCIL): 
notas = { "Ethan": 75,
        "Manson": 100,
        "Lukas": 65,
        "Mendy": 98 }
print(f"Mendy: {notas["Mendy"]}")
# Ele imprime a nota dada a Mendy no dicionário.
