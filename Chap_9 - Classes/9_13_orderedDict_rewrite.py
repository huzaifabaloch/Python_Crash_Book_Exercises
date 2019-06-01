"""
Start with Exercise 6-4 (page 108), where you
used a standard dictionary to represent a glossary. Rewrite the program using
the OrderedDict class and make sure the order of the output matches the order
in which key-value pairs were added to the dictionary.
"""
from collections import OrderedDict

# Creating an instance of OrderedDict class, which will assign
# an empty ordered dictionary.

glossary = OrderedDict()

glossary['print'] = "a function responsible to output data on screen."
glossary['else'] = "if all conditions get failed, finally else will get executed."
glossary['range'] = "a function that genreate a sequence of numbers of any length."
glossary['bool'] = "true or false"


for keyword, meaning in glossary.items():
	print(keyword.title() + " :: " + meaning.title())
