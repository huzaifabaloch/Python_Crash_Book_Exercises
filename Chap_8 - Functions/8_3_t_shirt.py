
# Use of positional and keyword arguments in python

def make_shirt(size, message_on_shirt):
	print("The size of the shirt is " + size.title() + 
	", and message to be printed is " + message_on_shirt.title() + ".")

make_shirt('small', 'the world make some noisy funny faces!')
make_shirt(message_on_shirt = 'acer baktub baki', size = 'medium')
