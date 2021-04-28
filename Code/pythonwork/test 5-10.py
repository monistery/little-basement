current_users = ['Joe', 'faker', 'Roger', 'Baby', 'admin']

new_users = ['joe', 'Bai', 'Ji' ,'Cheng', 'FAKER', 'Admin']

for user in new_users:
	if user in current_users or user.title() in current_users or user.upper() in current_users or user.lower() in current_users:
		print("wrong name")
	else:
		print("rignt name")
