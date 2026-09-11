#desconto secreto no açaí do centro
print("Bem-vindo ao Açaí do Centro!")
print("Temos algumas opcões de açaí hoje! Você pode se servir a vontade, depois vou pesar o pote.")
print("O preço do açaí é de R$ 0,05 por grama.")
peso = float(input("O seu açaí pesa quantos gramas? "))
if peso > 500:
    print("Você ganhou um desconto de 15% por colocar muito!")
    preco = peso * 0.05
    desconto = preco * 0.15
    preco_final = preco - desconto
    print(f"O preço do seu açaí é de R$ {preco_final:.2f}.")
else:
    preco = peso * 0.05
    print(f"O preço do seu açaí é de R$ {preco:.2f}.")