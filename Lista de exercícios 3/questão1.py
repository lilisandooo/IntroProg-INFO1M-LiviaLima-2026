
#exercício racha da pizza
print("RESPONDA COM sim OU não")
pizza = input("Ei mano, tô é com fome, bora rachar uma pizza? ")
if pizza == "sim":
    qtd_pessoas = int(input("Bora rachar com quantas pessoas? "))
    print(f"*Vocês comem {qtd_pessoas + 2} pizzas médias e ficam satisfeitos*")
    valor = float(input("Quanto é que deu a conta? "))
    print("Valha... ainda bem que tamo rachando, hein! Hahah")
    print(f"Então bora fazer assim, cada um vai pagar: R$ {valor/qtd_pessoas:.2f}")
elif pizza == "não":
    print("DEIXA DE SER CHATO, DIGA SIM!")
else:
    print("Vou ter que desenhar pra você entender?! É sim ou não. Povo difícil, viu...")