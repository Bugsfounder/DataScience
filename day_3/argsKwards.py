# args --> take limitless amount of arguments as list
def add(*args):
    print(sum(args))

    sumN = 0
    for x in args:
        sumN += x
    return sumN


# kwards --> key value paris
def kwargs(**kwargsV):
    # print(kwargsV.items())

    return [i for i, v in kwargsV.items()], [v for i, v in kwargsV.items()]


if __name__ == "__main__":
    add(1, 2, 3, 4, 5, 6)
    # kwargs(name="manisha", classM="mca", rollNo="024142010009")
    key, value = kwargs(name="manisha", classM="mca", rollNo="024142010009")

    print(key, value)
