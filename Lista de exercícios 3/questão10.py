#juiz de ímpar ou par lógico
print("Quem que tá jogando?")
jogador1 = input("Jogador 1: ")
jogador2 = input("Jogador 2: ")
lado = int(input(f"Primeiro tu, {jogador1}, escolha entre ímpar ou par: "))
numero1 = int(input(f"{jogador1}, escolha um número: "))
numero2 = int(input(f"Agora tu, {jogador2}, escolha um número: "))
soma = numero1 + numero2
if lado == "par" and soma % 2 == 0:
    print(f"{jogador1} venceu!")
elif lado == "ímpar" and soma % 2 != 0:
    print(f"{jogador1} venceu!")
else:
    print(f"{jogador2} venceu!")