f_languages = {
	'jen' : ['python', 'ruby'],
	'sans' : ['c'],
	'edward' : ['ruby', 'go'],
	'phil' : ['python', 'haskell'],
	}

for name, l in f_languages.items():
	print("\n" + name.title() + ":" )
	print(l)

print("\n")

for name in f_languages.keys():
	print(name.title())

print("\n")
for l in f_languages.items():
	print(l)
