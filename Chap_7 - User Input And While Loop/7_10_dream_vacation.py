
# 3. multiple user input in dictionary using while loop

user_vacations = {}

active_polling = True
prompt1 = "what is your name? "
prompt2 = "If you could visit one place in the world, where would you go? "
prompt3 = "Would you like to continue for other? (yes | no) "
while active_polling:
	user_name = input(prompt1.title())
	dream_vacation = input(prompt2.title())
	
	user_vacations[user_name] = dream_vacation
	
	repeat = input(prompt3.title())
	if repeat == 'no':
		active_polling = False

print("\n----- RESULTS OF THE POLL ------\n")
for name, vacation in user_vacations.items():
	print(name.title() + " has a dream of visiting " + vacation.title() + ".")
