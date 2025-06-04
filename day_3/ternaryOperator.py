label = ["even" if x % 2 == 0 else "odd" for x in range(1, 11)]
print(label)

numbers = [-2, 3, -1, 4, -5]
abs_numbers = [x if x >= 0 else -x for x in numbers]
print(abs_numbers)

