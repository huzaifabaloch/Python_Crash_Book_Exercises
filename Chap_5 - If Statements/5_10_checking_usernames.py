current_users = ['tuna', 'salmon', 'toaster', 'fred', 'john']
new_users = ['permit', 'bob', 'salmon', 'pompano', 'JoHn']

if new_users:
	for each_new_user in new_users:
		if each_new_user.lower() in current_users:
			print("The username " + each_new_user + " is already taken, kindly try other.")
		else:
			print("The username " + each_new_user + " is available")
			
