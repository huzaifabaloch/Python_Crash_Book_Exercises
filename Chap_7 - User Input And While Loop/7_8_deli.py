
# 1. Moving items from one list to another using while loop

sandwich_orders = ['club', 'jalepeno', 'muffle', 'pastries', 'yongden']
finished_sandwiches = []
counter = 0

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
	


