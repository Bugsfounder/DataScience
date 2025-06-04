number = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, number))
print(squared)


cel_temp = [0, 20, 30, 40]
feh = list(map(lambda c: (c * 9 / 5) + 32, cel_temp))
print(feh)
