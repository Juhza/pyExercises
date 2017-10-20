caixinha = "{} {} {} {} {}"

print(" TOP 5 CHAMPIONS:", caixinha.format('Lulu', 'Soraka', 'Sona', 'Karma', 'Rakan'))
print("\n", caixinha.format('one', 'two', 'three', 'four', 'five'))
print("\n", caixinha.format(True, False, True, True, False))
print("\n", caixinha.format(caixinha, '\t', caixinha, '\t', caixinha))

# PRECISA ter a quantidade de frases igual a quantidade de espaços na caixinha.
print("\n", caixinha.format(
    "STICKS AND STONES\n",
    "they may break this bones\n",
    "...but then-\n",
    "I ' L L  B E  R E A D Y\n",
    "are you ready?\n"
))
