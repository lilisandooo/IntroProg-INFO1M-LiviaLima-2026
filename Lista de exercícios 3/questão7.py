#validador de loguin seguro
print("Bem-vindo ao SUAP! Para acessar o sistema, digite a senha padronizada.")
username = input("Digite o nome de usuário: ")
print("Dica: A senha é 'a melhor cor do mundo'.")
password = input("Digite a senha: ")
senha = "Yellow"
while password != senha or password == "Amarelo" or password == senha:
    if password == "Amarelo":
        print("Senha incorreta. Tente novamente.")
        print("Dica: Tente em inglês.")
        username = input("Digite o nome de usuário: ")
        password = input("Digite a senha: ")
    elif password != senha:
        print("Senha incorreta. Tente novamente.")
        print("Dica: A senha é 'a melhor cor do mundo'.")
        username = input("Digite o nome de usuário: ")
        password = input("Digite a senha: ")
    else:
        print("Acesso liberado. Bem-vindo ao SUAP!")
        break