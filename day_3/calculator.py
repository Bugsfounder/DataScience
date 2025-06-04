def calculator(operation, a, b):
    if operation == "add".lower() or operation == "+":
        return a + b
    if operation == "substract".lower() or operation == "-":
        return a - b
    if operation == "multiply".lower() or operation == "*":
        return a * b
    if operation == "divide".lower() or operation == "/":
        return a / b
    if operation == "remainder".lower() or operation == "%":
        return a % b
    else:
        return "invalid operation"


print(calculator("add", 12, 32))
print(calculator("+", 12, 32))
print(calculator("subtract", 23, 11))
print(calculator("multiply", 2, 32))
