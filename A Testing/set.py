
'''

When you wrap set() around a list that contains duplicate items, Python
identifies the unique items in the list and builds a set from those items

'''

favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
	print(language.title())
