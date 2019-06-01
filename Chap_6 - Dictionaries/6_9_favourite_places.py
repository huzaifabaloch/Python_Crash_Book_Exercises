favourite_places = {
	'huzaifa': ['turkey', 'uk', 'makkah'],
	'sahal': ['greenland', 'turkey', 'mongolia'],
	'maher': ['qatar', 'usa'],
	}

for name, places in favourite_places.items():
	print(name.title() + " wants to visit ")
	for place in places:
		print("\t" + place.title())
