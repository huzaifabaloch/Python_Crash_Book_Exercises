poll = {
	'bob': 'ruby',
	'dale': 'python',
	'ken': 'c#',
	'sarah': 'python',
	}
	
people_to_poll = ['mary', 'mark', 'dale', 'sarah', 'jim', 'bob', 'ken']

print("Polled Languages")
for value in set(poll.values()):
	print(value)
print("\n\n")


for each_people in sorted(people_to_poll):
	if each_people in poll.keys():
		print("Thanks " + each_people.title() + " for responding.")
	else:
		print("Hey " + each_people.title() + ", kindly take the poll.")
	print("\n")
