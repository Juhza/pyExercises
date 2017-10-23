name = input("Qual seu nome? ")
age = input("E a sua idade? ")
number = input("Escolha um número: ")

print("{}, você terá 100 anos em {}. \n"
    .format(name, 2017 - int(age) + 100) * int(number))

'''
name = input("What is your name: ")
age = int(input("How old are you: "))
year = str((2014 - age)+100)
print(name + " will be 100 years old in the year " + year)
'''
