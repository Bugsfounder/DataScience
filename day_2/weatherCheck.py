temperature = int(input("Enter temp: "))
humidity = 80
if temperature > 40:
    print("Extreme Heat")
elif temperature > 30:
    if humidity > 70:
        print("Hot and humid")
    else:
        print("Hot day")
elif temperature > 20:
    print("Pleasant weather, greate for outdoor activity")
elif temperature > 10:
    print("cool weather, consider wearing a jacket")
else:
    print("Cold Weather")
