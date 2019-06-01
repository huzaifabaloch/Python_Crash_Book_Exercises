from collections import OrderedDict

# The call to OrderedDict() creates an empty ordered dictionary for us,
# and stores it in favorite_languages
favourite_languages = OrderedDict()

favourite_languages['jen'] = 'python'
favourite_languages['sarah'] = 'c'
favourite_languages['edward'] = 'ruby'
favourite_languages['phil'] = 'python'

for name, language in favourite_languages.items():
	print("{}'s favourite language is {}.".format(name.title(), language.title()))
