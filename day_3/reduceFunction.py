from functools import reduce

numbers = [1, 2, 3, 4, 5]
total = reduce(lambda x, y: x + y, numbers)
print(total)

numbers = [3, 1, 4, 1, 5, 9, 2, 6, 11]
maximum = reduce(lambda x, y: x if x > y else y, numbers)
print(maximum)


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = reduce(
    lambda x, y: x + y, filter(lambda x: x % 2 == 0, map(lambda x: x**2, numbers))
)


print(result)
