'''
number = int(input("Escolha um número qualquer: "))

if number % 4 == 0:
    print(number, "é par e múltiplo de 4.")
    pass
elif number % 2 == 0:
    print(number, "é par.")
    pass
else:
    print(number, "é ímpar.")
'''

number = int(input("Escolha um número qualquer: "))
check = int(input("Escolha outro número qualquer: "))

if number % check == 0:
    print(f"{number} é divisível por {check}.")
    pass
else:
    print(f"{number} não é divisível por {check}.")
