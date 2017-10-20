tiposDePessoas = 10
x = f"Existem {tiposDePessoas} tipos de pessoas."
# Nesse caso, tem que dizer qual variável pega o lugarzinho ali.

binario = "binario"
negacao = "que não"
# Tradução bem feia do inglês pro português.
y = f"As que conhecem {binario} e as {negacao}."

print(x)
print(y)

print(f"Eu disse: {x}")
print(f"E daí disse: '{y}'")

engracadalho = False
boa_piada = "Não é engraçado pra caralh*?! {}"

# Se o format é colocado da forma abaixo, a variável acima não precisa do f.
print(boa_piada.format(engracadalho))

fim = " com duas sentenças."
inicio = "> Essa é uma string"

print(inicio + fim)
