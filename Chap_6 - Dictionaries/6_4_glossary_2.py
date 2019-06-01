glossary = {
	"print": "a function responsible to output data on screen.",
	"range": "a function that genreate a sequence of numbers of any length.",
	"pop": "a list's method that can remove item from list to a variable.",
	"for": "for is loop in python used to solve tasks that repeat.",
	"title": "a string method that can capitalize the first word of string",
	"len":	"len is a function that is used to count the length of string or list items",
	"sort": "a method that organize the items in a list.",
	"reverse": "a method that change the order of list items in ASC or DESC permanently.",
	"if":	"a keyword that is used in conditional testing.",
	"elif": "another conditonal testing when one get failed.",
	"else": "if all conditions get failed, finally else will get executed.", 
	}

print("words\t\tmeanings\n")
for word, meaning in glossary.items():
	print(word + '\t\t' +meaning)
