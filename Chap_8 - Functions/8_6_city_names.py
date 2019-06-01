def city_country(city, country):
	return ('"'+ city.title() + ", " + country.title() + '"')

print(city_country('santiago', 'chili'))
print(city_country('istanbul', 'turkey'))
print(city_country('tokyo', 'japan'))
