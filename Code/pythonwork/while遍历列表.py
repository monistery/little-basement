uncfmed_users = ['Bai', 'ji', 'cheng']

cfmed_users = []

while uncfmed_users:
	cur_user = uncfmed_users.pop()
	print("CFMED USER: " + cur_user.title())
	cfmed_users.append(cur_user)
	
print("\n")
for cfmed_user in cfmed_users:
	print(cfmed_user.title())
