data = [x for x in range(100)]
f_data = list(filter(lambda x: x % 2 == 0, data))
print(f_data)
print(len(f_data))


# data to remove: None, 0, "", False
mixed_list = [1, 0, "hello", "", None, "world", False, 42]
truthy_value = list(filter(None, mixed_list))
print(truthy_value)
