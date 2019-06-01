	
	
# Preventing a Function from Modifying a List
# Using slice notation[:] to make a copy of the original list


# This function contains a list that is a copy of the original list
# that will be called 
def print_models(unprinted_designs, completed_models):
	
	while unprinted_designs:
		current_design = unprinted_designs.pop()
		completed_models.append(current_design)

def show_completed_models(completed_models):
	
	print("\n")
	for completed_model in completed_models:
		print(completed_model.title())
		
unprinted_designs = ['iphone case', 'folder pin', 'robust']
completed_models = []

# Calling functions and using slice notation [:],
# so that original list unprinted_list is not modified
print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)

# Checking to see if original list is not changed.
print("\n\nChecking to see if original list is not changed.\n")
print(unprinted_designs)
