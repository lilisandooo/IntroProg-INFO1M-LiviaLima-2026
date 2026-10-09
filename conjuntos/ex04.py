import random
while True:
    numeros =  []
    for i in range(101):
        numeros.append(random.randint(0, 100))
        #gera um número aleatório em um intervalo entre 0 e 101
    print(numeros)
    chute = int(input("Digite quantos números diferentes você consegue contar: "))
    contagem = len(set(numeros))

    if chute > contagem:
        print("Você contou números a mais!")
        print(f"Na verdade, haviam {contagem} números diferentes")
    elif chute < contagem:
        print("Você contou números de menos!")
        print(f"Na verdade, haviam {contagem} números diferentes:")
    else:
        print("PARABÉNS! Acertou em cheio!")

    escolha = input("Quer jogar novamente? [s/n]: ").strip().lower()
    if escolha not in ['n', 'nao']:
        print("\n NOVO JOGO!\n")
    else:
        print("\n OBRIGADA POR JOGAR\n")
        break