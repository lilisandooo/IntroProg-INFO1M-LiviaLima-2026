texto = input("Digite uma frase: ")
vogais = "AEIOUÀÁÂÃÉÈÊÍÌÎÓÒÔÕÚÙÛÜÏÄÖË"
silabas = "BCDFGHJKLMNPQRSTVWXYZÇ"
caracteres = ",<.>;:/?°~^]}º[`{]}=+-_)(*&¨%$#@!.)"
numeros = "1234567890"

n = 0
f = 0
g = 0
h = 0

for letra in texto:
    #upper serve para o python ignorar o cap
    if letra.upper() in vogais:
        n = n + 1
for letra in texto:
    if letra.upper() in silabas:
        f = f + 1
for letra in texto:
    if letra.upper() in caracteres:
        g = g + 1
for letra in texto:
    if letra.upper() in numeros:
        h = h + 1

print(f"Vogais no texto: {n}")
print(f"Sílabas no texto: {f}")
print(f"Caracteres especiais no texto: {g}")
print(f"Números no texto: {h}")
print(f"Total de letras: {n + f + g + h}")