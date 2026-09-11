#média aritmética
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
media = (n1 + n2) / 2
if media >= 60:
    print("Aprovado com média:", media)
elif media <60 and media >= 20:
    print("Recuperação com média:", media)
else:
    print("Reprovado com média:", media)