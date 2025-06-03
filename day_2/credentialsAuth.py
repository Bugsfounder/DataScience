username = "admin"
password = "manisha123"

userInput = input("Enter Your Username: ")
upassword = input("Enter Your password: ")

if userInput == username and password == upassword:
    print("Persmission Granted")
else:
    print("Invalid Credientials")
