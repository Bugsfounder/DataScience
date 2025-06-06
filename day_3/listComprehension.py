# traditional way
squares = []

for x in range(10):
    squares.append(x**2)

# using Comprehension
numbers = [x for x in range(10)]

squares = [x**2 for x in range(1, 10)]

words = ["Hello", "Wordl", "python"]

upper_words = [word.upper() for word in words]

print(numbers, squares, upper_words)


# with condition

even = [x for x in range(100) if x % 2 == 0]
print()
print(even, len(even))

words = ["Manisha", "java", "c++", "JavaScript"]
filteredWord = [word for word in words if len(word) <= 3]
print(filteredWord)

# TODO: Try to understand Complex List comprehension  ---> DONE

# create multi _D array:

arr = [[0 for j in range(3)] for i in range(3)]

multiplicationTable = [[i * j for j in range(1, 6)] for i in range(1, 6)]
print(arr)
print(multiplicationTable)
