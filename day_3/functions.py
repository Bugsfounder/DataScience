def add(*args):
    print(sum(args))

    sumN = 0
    for x in args:
        sumN += x
    return sumN


def kwargs(**kwargsV):
    print(kwargsV.items())


def add_numbers(a, b):
    return a + b


def fullName(name):
    return name.split()[0], name.split()[1]


def get_even_numbers(max_number):
    return [x for x in range(max_number) if x % 2 == 0]


def greet(name):
    return f"Hello {name}"


def areaOfRect(length, width):
    return length * width


def cel_to_feh(cel):
    # (cel*9/5) + 32
    return (cel * (9 / 5)) + 32


def feh_to_cel(feh):
    return (feh - 32) * (5 / 9)


if __name__ == "__main__":
    add(1, 2, 3, 4, 5, 6)

    print(greet("manisha"))

    print(areaOfRect(10, 12))

    print(get_even_numbers(10))
    print(fullName("manisha Kumari"))

    print(cel_to_feh(30))
    print(feh_to_cel(67))
