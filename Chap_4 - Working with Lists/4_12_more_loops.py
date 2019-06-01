foods = ["fish", "ginger bread", "brinjal"]
friend_foods = foods[:]

foods.insert(1, "pasta")
friend_foods.insert(1, "curd")

print("Foods I love are,\n")
for each in foods:
	print(each.title())

print("\nFoods my friend love,\n")
for each in friend_foods:
	print(each.title())
