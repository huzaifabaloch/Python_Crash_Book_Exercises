
# Use a conditional test in the while statement to stop the loop.

message = ""

while message != 'quit':
	message = input("What's your name? ")
	print("Hello, " + message.title())

# Use a break statement to exit the loop when the user enters a 'quit' value.

message = ""

while message != 'quit':
	message = input("What's your name? ")
	if message == 'quit':
		break
	else:
		print("Hello, " + message.title())

# Use an active variable to control how long the loop runs

active = True

while active:
	number = int(input("Enter a number, -ve to quit: "))
	if number < 0:
		active = False
	else:
		print(number)
