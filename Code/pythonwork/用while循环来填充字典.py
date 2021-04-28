respons = {}

a = True

while a:
	name = input("\nWhat's your name? ")
	respon = input("ni xiang qu pa na ge shan? ")
	
	respons[name] = respon
	
	
	b = input("hai you qi ta ren yao hui da ma? ")
	if b == 'no':
		a = False

for name, re in respons.items():
	print(name.title() + " xiang pa " + re + ".")	
