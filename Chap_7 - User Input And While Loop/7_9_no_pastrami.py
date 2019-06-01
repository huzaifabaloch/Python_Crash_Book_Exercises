
# 2. Removing the multiple occurence of specific instance or item in list
#	using while loop

sandwich_orders = ['club', 'yongden', 'pastrami', 'muffle', 'pastrami', 'blouter', 'pastrami']
finished_sandwiches = []
counter = 0

print("The deli has run out of pastrami.\n")

# Checking is pastrami is in list and repeating until we left with zero 
# pastrami.
while 'pastrami' in sandwich_orders:
	sandwich_orders.remove('pastrami')
	

while sandwich_orders:
	# the counter is used so that we pop the order that come 
	# first in the sandwich_orders list, there is no need 
	# to increment counter because while popping, python
	# automatically adjust the indexing.
	current_sandwich = sandwich_orders.pop(counter)
	print("I made your " + current_sandwich + " sandwich")
	finished_sandwiches.append(current_sandwich)

print("\nSandwiches made today:")
for finished_sandwich in finished_sandwiches:
	print(finished_sandwich)
	



