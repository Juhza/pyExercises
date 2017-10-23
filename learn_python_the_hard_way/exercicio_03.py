# Sobre os símbolos matemáticos.
print('''
Esse exercício é sobre matemática.

'=' igualdade, mas usado para declarar variáveis.
'+' adiciona.
'-' subtrai.
'*' multiplica.
'/' divide.
'%' dá o resto de uma divisão.
'**' é exponencial.

Comparativos abaixo:
'<' menor que.
'>' maior que.
'<=' menor ou igual.
'>=' maior ou igual.
'==' igualdade.
''')

# Exercício útil pra minha vida acadêmica
print("Minhas notas de Circuitos Digitais estão bem ruins.")

m1 = (6 * 3 + 5.7 * 7) / 10
m2 = (10 * 2 + 10 * 2 + 1 * 6) / 10
print("M1 ", m1, "\t já definida")
print("M2 ", m2, "\t incerta")


print("\nMinha M3 precisa ser...")
m3 = 18 - (((6 * 3 + 5.7 * 7) / 10) + ((10 * 2 + 10 * 2 + 1 * 6) / 10))
print(m3)

print("\nSe eu tirar 10 nos trabalhos, minha nota da prova precisa ser...")
prova = (m3 * 10 - (10 * 2 + 10 * 2)) / 10
print(prova)


print("\nSe minha nota da prova da M2 for zero, precisarei tirar")

m3 = 18 - (((6 * 3 + 5.7 * 7) / 10) + ((10 * 2 + 10 * 2 + 0 * 6) / 10))
print(m3, " na M3 e")

prova = (m3 * 10 - (10 * 2 + 10 * 2)) / 10
print(prova, " na prova da M3.")


print("\n\nCom essas notas, estarei aprovada?", m1 + m2 + m3 >= 18)
