rivers = {
	'nile': 'egypt',
	'mississipi': 'usa',
	'amazon': 'brazil',
	}
	
for river, country in rivers.items():
	if country == 'usa':
		print("The " + river.title() + " runs through " + country.upper())
	else:
		print("The " + river.title() + " runs through " + country.title())

