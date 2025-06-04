output = lambda x, y: x + y

squareLambda = lambda x: x**2

print(output(12, 21))
print(squareLambda(2))

greeting = lambda name: f"Hello {name}"


def myFunc():
    print("manisha is a good girl")

    return lambda name: f"Hello {name}"


# TODO: practice and understand (map, reduce, filter) functions in python

print(greeting("Manisha"))
m = myFunc()
print(m("manisha"))
