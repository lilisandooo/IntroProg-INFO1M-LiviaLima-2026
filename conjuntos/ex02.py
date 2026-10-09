
# Conceito de desempacotamento, troca de informações
# Jeito difícil:
a = "Primeiro(a)"
b = "Segundo(b)"
aux = b
b = a
a = aux
print(a, b)

a = "Primeiro//a"
b = "Segundo//b"
a, b = b,a
print(a, b)