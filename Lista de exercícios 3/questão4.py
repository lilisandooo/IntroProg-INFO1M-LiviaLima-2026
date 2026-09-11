mensagem = input("Digite uma mensagem: ")
#len serve para contar o tamanho da string
tamanho = len(mensagem)
if tamanho < 3 or tamanho > 140:
    print("Mensagem inválida. A mensagem deve ter entre 3 e 140 caracteres.")
else:
    print("Mensagem enviada com sucesso.")