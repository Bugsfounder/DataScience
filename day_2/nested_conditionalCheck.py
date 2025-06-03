age = int(input("Enter your age: "))
is_student = True
order_amount = 150
is_first_time = False
discount = 0
if age < 30 and is_student:
    print("Student Discount: 20% OFF")
    discount = 0.20
elif order_amount > 100 or is_first_time:
    print("Special Discount 10% OFF")
    discount = 0.10
elif not is_first_time and age >= 65:
    print("senior Citizen Discount : 15% OFF")
    discount = 0.15
else:
    print("Regular Price applies.")
    discount = 0.0

final_amount = order_amount * (1 - discount)

print("Final Amount: ", final_amount)
