users = []


if users:
	for user in users:
		if user == 'admin':
			print("Hello admin, would you need any help?")
		else:
			print("Hello," + user + ".")
else:
	print("We need to find users")
