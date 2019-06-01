# We can reorganize this code by writing two functions, each of which 
# does one specific job.

def print_models(unprinted_designs, completed_designs):
	
	while unprinted_designs:
		current_design = unprinted_designs.pop()
		print("Printing model: " + current_design)
		completed_designs.append(current_design)


def show_completed_models(completed_models):
	
	print("\nThe following models have been printed:")
	for completed_model in completed_models:
		print(completed_model)
	

unprinted_designs = ['metal stake', 'samsung case', 'robust']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
