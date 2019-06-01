# NESTING
# A LIST IN A DICTIONARIES 

#-----------------------------------------------

# Store information about a pizza being ordered.
pizza = {
	'crust': 'thick',
	'toppings': ['mushrooms', 'extra cheese'],
	}
	
# Summarize the order
print("You ordered a " + pizza['crust'] + "-crust pizza " +
	"with the following toppings: ")
	
for topping in pizza['toppings']:
	print("\t" + topping)

'''   

You can nest a list inside a dictionary any time you want more than
one value to be associated with a single key in a dictionary

'''

print("\n\n")

favourite_languages = {
	'dale': ['python', 'c#'],
	'peter':['go', 'python'],
	'carl': ['perl', 'ruby', 'c#'],
	'sarah': ['go']
	}

for name, language in favourite_languages.items():
	if len(language) != 1:
		print("\n" + name.title() + "'s favourite languages are:")
		for each_language in language:
			print("\t" + each_language.title())
	else:
		print("\n" + name.title() + "'s favourite language is:")
		for each_language in language:
			print("\t" + each_language.title())
	

