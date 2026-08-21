#Upgrade de Skin
print("Cara, você viu que lançou uma skin icônica do flash, por tempo limitado, no DC:Dark Legion!?")
print("CAAARA QUE DAORA! Vou comprar!")
print("Mas custa 10000 diamantes, você tem dinheiro pra isso? Quantos diamantes você tem?")
diamantes = int(input("Eu tenho... "))
if diamantes >= 10000:
    print("EIITA RICO!")
    print("*SISTEMA* Compra realizada com sucesso! Aproveite sua nova skin do flash!")

else:
    print("Você não tem dinheiro suficiente para comprar a skin.")
    print(f"Faltam {abs(10000 - diamantes)} diamantes para você conseguir comprar a skin.")