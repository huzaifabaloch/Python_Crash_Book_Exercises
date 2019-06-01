
musicians = ["akcent", "blake shelton", "shakira", "usher", "pitbull", "bruno mars", "atif aslam"]

print("The first three items in the list are:.")
for each in musicians[:3]:
	print(each.title())
	
print("\nThe three items from the middle of the list are:.")
for each in musicians[2:4]:
	print(each.title())

print("\nThe last three items from the list are:.")
for each in musicians[4:]:
	print(each.title())
