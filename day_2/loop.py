# for loop --> definite

n = int(input("Enter a number:"))

# range iteration
for i in range(n):
    print(i)


# string iteration
var = "manisha"

for char in var:
    print(char)

# list iteration
lst = ["mani", 1, 2, 4, 5, 2]

for item in lst:
    print(item)

# dictionary iteration
myDict = {"name": "manisha", "age": 20}

for key, value in myDict.items():
    print(f"{key} : {value}")


# while  --> indefinite

# counter
counter = 0

while counter < 5:
    print(counter)
    counter += 1

password = ""

# check password
while password != "secret":
    password = input("Enter Correct Password: ")

    if password != "secrect":
        print("wrong password")
    else:
        print("Correct password")


# search algo

target = "apple"
lst = ["graps", "orange", "apple", "litchi", "mango"]

for i, item in enumerate(lst):
    if item == target:
        print(f"{target} Found at: {i}")

