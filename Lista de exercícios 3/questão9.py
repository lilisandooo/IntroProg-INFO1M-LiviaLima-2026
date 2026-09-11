#Meia-Entrada ou gratuidade no trem
idade = int(input("Qual a sua idade? "))
carteira_ = input("Você possui carteira de estudante? \n [1] sim \n [2] não\n> ")

if idade >= 65:
    print("Você tem direito a meia-entrada no trem.")
elif carteira_ == "1" or idade < 18:
    print("Meia-entrada autorizada!.")
else:
    print("Passagem inteira.")