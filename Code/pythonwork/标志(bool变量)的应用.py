prompt = "\nTell me something"
prompt += "(Enter 'quit' to end): "

active = True

while active:
	message = input(prompt)
	
	if message == "quit":
		active = False
	else:
		print(message)
