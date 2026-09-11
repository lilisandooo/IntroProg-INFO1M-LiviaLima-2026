#radar eletrônico na avenida
velocidade = float(input("Digite a velocidade do veículo: "))
if velocidade <=60:
    print("Boa viagem. Dirija com segurança!")
elif velocidade > 60 and velocidade < 70:
    print("infração média. Veícula a cima da velocidade permitida. Multa de R$ 130,16 e 4 pontos na carteira.")
else:
    print("infração grave. Veículo a cima da velocidade permitida. Multa de R$ 293,47 e 7 pontos na carteira.")