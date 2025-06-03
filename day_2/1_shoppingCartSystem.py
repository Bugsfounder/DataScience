shopping_cart = []

shopping_cart.append({"item": "laptop", "price": 1200})
shopping_cart.append({"item": "chocolate", "price": 1400})
shopping_cart.append({"item": "pen", "price": 20})
shopping_cart.append({"item": "pencil", "price": 600})

total = sum(item["price"] for item in shopping_cart)

print(total)
