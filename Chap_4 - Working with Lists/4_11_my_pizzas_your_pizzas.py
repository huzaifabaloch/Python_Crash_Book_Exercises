pizzas = ["fajita", "pepperroni", "chicken cheese"]
friend_pizzas = pizzas[:]  # made a copy of list 

pizzas.append("afghan")
friend_pizzas.append("pasta")

print("My favourite pizzas are:")
for each in pizzas:
	print(each.title())
	
print("\nMy friend's favourite pizzas are:")
for each in friend_pizzas:
	print(each.title())

