
# Use of default values in python

def make_shirt(size = 'large', message_on_shirt = 'i love python'):
	print("The size of the shirt is " + size.title() + 
	", and message to be printed is " + message_on_shirt.title() + ".")


# using function default arguments
make_shirt()

# one default with positional argument
make_shirt('small')
make_shirt('medium')

# one default and one keyword argument
make_shirt(message_on_shirt = 'Bark Tub Baki.')
make_shirt(size = 'small')

make_shirt(message_on_shirt = 'the world make some noisy funny faces!')
make_shirt(message_on_shirt = 'the world make some noisy funny faces!', size = 'small')
