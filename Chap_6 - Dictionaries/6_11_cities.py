cities = {
	'karachi': {
		'country': 'pakistan',
		'population': 3929321,
		'fact': 'a city that never sleeps',
		},
		
	'istanbul': {
		'country': 'turkey',
		'population': 2229955,
		'fact': 'a large tourist point',
		},
	
	'new york': {
		'country': 'america',
		'population': 2998194,
		'fact': 'all things available',
		}, 
	}


for city_name, city_info in cities.items():
	print(city_name.title() + ":")
	print("\tCountry: " + city_info['country'].title())
	print("\tPopulation: " + str(city_info['population']))
	print("\tFact: " + city_info['fact'].title())
	print("\n")
