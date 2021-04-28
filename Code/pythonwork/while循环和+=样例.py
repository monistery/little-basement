a = "Please tell me your age "
a += "(Enter '-1' to end): "

age = " "

while age != -1:
	age = int(input(a))
	if age == -1:
		continue
	if age < 3:
		print("Price is free")
	elif age >= 3 and age <= 12:
		print("Price is 10 dollars")
	else:
		print("Price is 15 dollars")
