"""
ZeroDivisionError
ValueError
TypeError
FileNotFoundError
IndexError
"""

# give error --> program not run
# result = 10 / 0
# print(result)

# handling error so program will and print error message
try:
    result = 10 / 0
    print(result)
except Exception as err:
    print(err)  # division by zero


# Another Problem
try:
    num = int(input("Enter Number: "))
    result = 100 / num
    print(result)
except ZeroDivisionError as err:
    # except Exception as err:
    print(err)  # division by zero
