nome = 'Julia'
idade = 21
nascimento = '15/01/1996'
peso = 49
altura_em_cm = 158
serie_favorita = "Grey's Anatomy"
endereco = 'Balneário Camboriú, SC, Brasil'
nome_pet = 'Gaia'
idade_pet = 3

print("Boo-hoo! Meu nome é " + nome + " e essa é a " + nome_pet + " :)")
# Aparentemente, quando você usa um print("alguma", coisa), fica tudo junto no
# cmd. Mas se usar print("alguma" + coisa) ele dá o espaçamento. O que, honestly,
# faz todo o sentido.

print(f'''
Nasci em {nascimento} e, portanto, tenho {idade} anos. A {nome_pet} tem {idade_pet}.
Eu peso {peso}kg e tenho {altura_em_cm}cm de altura.
Moramos em {endereco}.
Nossa série favorita é {serie_favorita}.
''')
