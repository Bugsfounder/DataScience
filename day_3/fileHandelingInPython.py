# opening file in write+ mode to write and read
file = open("file.txt", "w+")
file.write("Manisha is a good girl")
file.write("\nManisha is smart")
file.writelines(["\nline1", "\nline2", "\nline3"])
# move file pointer at 0 index
file.seek(0)
print(file.read())  # printing data

# closing file is important
file.close()

# using with
print("using with")
with open("file.txt", "r+") as file:
    print(file.readline())
    file.seek(0)
    print(file.read())
    file.seek(0)
    print(file.readlines())
