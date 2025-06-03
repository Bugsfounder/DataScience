while True:
    print("1 . Play Game")
    print("2. settings")
    print("3. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        print("Starting game...")
    elif choice == "2":
        print("Opening Settings...")
    elif choice == "3":
        print("Good")
        break
    else:
        print("Invalid Choice")
